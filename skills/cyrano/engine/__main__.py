"""cyrano engine CLI — the deterministic helpers the skill leans on.

    python -m engine filter  [--events FILE] [--all]
    python -m engine deliver [--brief FILE] [--subject S]
                             [--mark EVENT_ID EMAIL]
    python -m engine mark    EVENT_ID EMAIL
    python -m engine check   EVENT_ID EMAIL           # exit 0 = fresh, 1 = briefed
    python -m engine state   show|clear
    python -m engine fetch   URL [-- passthrough args to insane-search]
    python -m engine config                            # resolved config, secrets masked

Reads JSON from a file arg or, when omitted, from stdin.
"""
from __future__ import annotations

import argparse
import json
import sys

# Windows consoles default to cp1252; the brief is Korean + emoji. Harden stdout
# so a print never crashes the routine. (See feedback_python_windows_encoding.)
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from . import config as cfg_mod
from . import deliver as deliver_mod
from . import filter as filter_mod
from . import state as state_mod
from . import fetch_bridge


def _read_json(path: str | None) -> dict:
    raw = open(path, encoding="utf-8").read() if path else sys.stdin.read()
    return json.loads(raw)


def _read_text(path: str | None) -> str:
    return open(path, encoding="utf-8").read() if path else sys.stdin.read()


def _emit(obj: dict) -> None:
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    # guard against lone surrogates sneaking in from a mangled pipe
    text = text.encode("utf-8", "replace").decode("utf-8")
    print(text)


def cmd_filter(args) -> int:
    cfg = cfg_mod.load()
    payload = _read_json(args.events)
    result = filter_mod.select(payload, cfg, skip_briefed=not args.all)
    _emit(result)
    return 0


def cmd_deliver(args) -> int:
    cfg = cfg_mod.load()
    brief = _read_text(args.brief)
    result = deliver_mod.send(brief, cfg, subject=args.subject)
    if args.mark and result.get("ok"):
        state_mod.mark(cfg, *args.mark)
        result["marked"] = args.mark
    _emit(result)
    return 0 if result.get("ok") else 1


def cmd_mark(args) -> int:
    cfg = cfg_mod.load()
    state_mod.mark(cfg, args.event_id, args.email)
    _emit({"ok": True, "marked": [args.event_id, args.email]})
    return 0


def cmd_check(args) -> int:
    cfg = cfg_mod.load()
    briefed = state_mod.is_briefed(cfg, args.event_id, args.email)
    _emit({"briefed": briefed})
    return 1 if briefed else 0


def cmd_state(args) -> int:
    cfg = cfg_mod.load()
    if args.action == "clear":
        state_mod.clear(cfg)
        _emit({"ok": True, "cleared": cfg["dedup"]["state_file"]})
    else:
        try:
            data = json.loads(open(cfg["dedup"]["state_file"], encoding="utf-8").read())
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        _emit({"state_file": cfg["dedup"]["state_file"], "entries": data})
    return 0


def cmd_fetch(args) -> int:
    code, out = fetch_bridge.fetch(args.url, args.passthrough)
    sys.stdout.write(out)
    if not out.endswith("\n"):
        sys.stdout.write("\n")
    return code


def _mask(v):
    return v[:4] + "…" if isinstance(v, str) and len(v) > 4 else v


def cmd_config(args) -> int:
    cfg = cfg_mod.load()
    _emit({
        "config_path": str(cfg_mod.config_path()),
        "own_domains": sorted(cfg_mod.own_domains(cfg)),
        "delivery_mode": cfg["delivery"].get("mode"),
        "insane_search_bundled": fetch_bridge.available(),
        "research": cfg.get("research"),
        "dedup": cfg.get("dedup"),
    })
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m engine", description="cyrano engine")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("filter", help="calendar events -> external targets")
    f.add_argument("--events", help="events JSON file (default: stdin)")
    f.add_argument("--all", action="store_true", help="include already-briefed")
    f.set_defaults(func=cmd_filter)

    d = sub.add_parser("deliver", help="send a brief via the configured channel")
    d.add_argument("--brief", help="brief text file (default: stdin)")
    d.add_argument("--subject", default="cyrano brief")
    d.add_argument("--mark", nargs=2, metavar=("EVENT_ID", "EMAIL"),
                   help="mark briefed on success")
    d.set_defaults(func=cmd_deliver)

    m = sub.add_parser("mark", help="record a brief as delivered")
    m.add_argument("event_id"); m.add_argument("email")
    m.set_defaults(func=cmd_mark)

    c = sub.add_parser("check", help="exit 0 if fresh, 1 if already briefed")
    c.add_argument("event_id"); c.add_argument("email")
    c.set_defaults(func=cmd_check)

    s = sub.add_parser("state", help="inspect / clear the dedup ledger")
    s.add_argument("action", choices=("show", "clear"))
    s.set_defaults(func=cmd_state)

    ft = sub.add_parser("fetch", help="read a (possibly blocked) URL via insane-search")
    ft.add_argument("url")
    ft.add_argument("passthrough", nargs=argparse.REMAINDER,
                    help="args forwarded to insane-search after --")
    ft.set_defaults(func=cmd_fetch)

    cf = sub.add_parser("config", help="show resolved config (secrets masked)")
    cf.set_defaults(func=cmd_config)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
