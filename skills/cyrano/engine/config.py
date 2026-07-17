"""Config loading + env-backed secret resolution.

Search order for the active config file:
  1. $CYRANO_CONFIG (explicit path)
  2. <skill_dir>/config.json          (user's real config, git-ignored)
  3. <skill_dir>/config.example.json  (checked-in defaults, so the engine
                                        always runs even before setup)

Secrets are NEVER stored in the config file. A field like
"webhook_url_env": "SLACK_BRIEF_WEBHOOK" names an environment variable; the
resolver reads the value from os.environ at call time.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parent.parent


def config_path() -> Path:
    env = os.environ.get("CYRANO_CONFIG")
    if env:
        return Path(env)
    real = SKILL_DIR / "config.json"
    if real.exists():
        return real
    return SKILL_DIR / "config.example.json"


def load() -> dict[str, Any]:
    path = config_path()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError as e:
        raise SystemExit(f"cyrano: config at {path} is not valid JSON: {e}")
    return _with_defaults(data)


def _with_defaults(data: dict[str, Any]) -> dict[str, Any]:
    data.setdefault("own_domains", [])
    data.setdefault("internal_emails", [])
    data.setdefault("calendar", {"source": "host"})
    delivery = data.setdefault("delivery", {})
    delivery.setdefault("mode", "return")
    research = data.setdefault("research", {})
    research.setdefault("use_insane_search", True)
    research.setdefault("depth", "standard")
    research.setdefault("sections", ["profile", "company", "signals", "angles"])
    dedup = data.setdefault("dedup", {})
    dedup.setdefault("state_file", str(SKILL_DIR / ".state" / "briefed.json"))
    dedup.setdefault("window_hours", 20)
    return data


def resolve_env(name_field: str | None) -> str | None:
    """Resolve a *_env config field to its actual environment value."""
    if not name_field:
        return None
    return os.environ.get(name_field)


def own_domains(data: dict[str, Any]) -> set[str]:
    return {d.strip().lower().lstrip("@") for d in data.get("own_domains", []) if d.strip()}


def internal_emails(data: dict[str, Any]) -> set[str]:
    return {e.strip().lower() for e in data.get("internal_emails", []) if e.strip()}
