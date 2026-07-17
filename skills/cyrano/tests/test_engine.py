"""Smoke + unit tests for the cyrano engine. Run: python -m pytest -q (or plain python)."""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

# allow `import engine.*` when run from the skill dir
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine import config as cfg_mod  # noqa: E402
from engine import filter as filter_mod  # noqa: E402
from engine import state as state_mod  # noqa: E402
from engine import deliver as deliver_mod  # noqa: E402


def _cfg(tmp: Path) -> dict:
    return cfg_mod._with_defaults({
        "own_domains": ["crealwork.com", "sundayable.com"],
        "internal_emails": ["contractor@gmail.com"],
        "dedup": {"state_file": str(tmp / "briefed.json"), "window_hours": 20},
        "delivery": {"mode": "return"},
    })


def test_filter_picks_only_external():
    cfg = _cfg(Path(tempfile.mkdtemp()))
    payload = {
        "date": "2026-07-08",
        "events": [
            {"id": "e1", "title": "Intro", "start": "T10",
             "attendees": ["jane@acme.com", "host@example.com"]},
            {"id": "e2", "title": "Team sync", "start": "T11",
             "attendees": ["host@example.com", "colleague@example.com"]},
            {"id": "e3", "title": "Solo focus", "start": "T12", "attendees": []},
            {"id": "e4", "title": "Room", "start": "T13",
             "attendees": ["room@resource.calendar.google.com", "host@example.com"]},
            {"id": "e5", "title": "Excluded contractor", "start": "T14",
             "attendees": ["contractor@gmail.com", "host@example.com"]},
        ],
    }
    out = filter_mod.select(payload, cfg)
    emails = [t["email"] for t in out["targets"]]
    assert emails == ["jane@acme.com"], emails
    assert out["skipped"]["internal_only"] >= 2
    assert out["skipped"]["no_attendees"] == 1


def test_state_dedup_roundtrip():
    tmp = Path(tempfile.mkdtemp())
    cfg = _cfg(tmp)
    assert not state_mod.is_briefed(cfg, "e1", "jane@acme.com")
    state_mod.mark(cfg, "e1", "jane@acme.com")
    assert state_mod.is_briefed(cfg, "e1", "JANE@acme.com")  # case-insensitive
    # a different meeting (event id) is fresh
    assert not state_mod.is_briefed(cfg, "e2", "jane@acme.com")


def test_state_window_expiry():
    import json as _json
    import time as _time
    tmp = Path(tempfile.mkdtemp())
    cfg = _cfg(tmp)
    cfg["dedup"]["window_hours"] = 1
    state_mod.mark(cfg, "e1", "jane@acme.com")
    # backdate the entry beyond the window -> treated as fresh again
    p = Path(cfg["dedup"]["state_file"])
    ledger = _json.loads(p.read_text())
    ledger[state_mod.key("e1", "jane@acme.com")] = _time.time() - 2 * 3600
    p.write_text(_json.dumps(ledger))
    assert not state_mod.is_briefed(cfg, "e1", "jane@acme.com")


def test_filter_skips_already_briefed():
    tmp = Path(tempfile.mkdtemp())
    cfg = _cfg(tmp)
    state_mod.mark(cfg, "e1", "jane@acme.com")
    payload = {"date": "2026-07-08", "events": [
        {"id": "e1", "title": "Intro", "start": "T10",
         "attendees": ["jane@acme.com", "host@example.com"]}]}
    out = filter_mod.select(payload, cfg)
    assert out["targets"] == []
    assert out["skipped"]["already_briefed"] == 1
    # --all (skip_briefed=False) includes it
    out2 = filter_mod.select(payload, cfg, skip_briefed=False)
    assert len(out2["targets"]) == 1


def test_deliver_return_mode():
    cfg = _cfg(Path(tempfile.mkdtemp()))
    res = deliver_mod.send("hello brief", cfg)
    assert res["ok"] and res["mode"] == "return" and res["brief"] == "hello brief"


def test_deliver_slack_missing_env():
    cfg = _cfg(Path(tempfile.mkdtemp()))
    cfg["delivery"] = {"mode": "slack", "slack": {"webhook_url_env": "NOPE_NOT_SET"}}
    os.environ.pop("NOPE_NOT_SET", None)
    res = deliver_mod.send("x", cfg)
    assert res["ok"] is False and res["mode"] == "slack"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"\n{len(fns)} passed")
