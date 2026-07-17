"""Turn a day's calendar events into a list of external people to research.

The host agent reads the calendar with whatever tool it has (Google Calendar
MCP, etc.) and hands us a normalised events payload. We apply the deterministic
rules the LLM tends to get wrong: domain matching, resource/room filtering,
self-exclusion, and dedup.

Input JSON (stdin or --events file):
{
  "date": "2026-07-08",
  "events": [
    {"id": "evt1", "title": "Intro call",
     "start": "2026-07-08T10:00:00-07:00",
     "attendees": ["jane@acme.com", "host@example.com"]}
  ]
}

Output JSON:
{
  "date": "2026-07-08",
  "targets": [
    {"event_id": "evt1", "title": "Intro call", "start": "...",
     "email": "jane@acme.com", "domain": "acme.com"}
  ],
  "skipped": {"internal_only": 1, "already_briefed": 0, "no_attendees": 0}
}
"""
from __future__ import annotations

from typing import Any

from . import config as cfg_mod
from . import state as state_mod

# addresses that are never people
_NON_PERSON_SUFFIXES = (
    "resource.calendar.google.com",
    "group.calendar.google.com",
    "calendar.google.com",
)


def _domain(email: str) -> str:
    return email.split("@", 1)[1].lower() if "@" in email else ""


def _is_person(email: str) -> bool:
    d = _domain(email)
    return bool(d) and not any(d.endswith(s) for s in _NON_PERSON_SUFFIXES)


def select(payload: dict[str, Any], cfg: dict[str, Any], skip_briefed: bool = True) -> dict[str, Any]:
    own = cfg_mod.own_domains(cfg)
    internal = cfg_mod.internal_emails(cfg)
    date = payload.get("date", "")

    targets: list[dict[str, Any]] = []
    skipped = {"internal_only": 0, "already_briefed": 0, "no_attendees": 0}
    seen: set[str] = set()

    for ev in payload.get("events", []):
        event_id = str(ev.get("id", "")) or ev.get("title", "")
        attendees = [a.strip() for a in ev.get("attendees", []) if a and "@" in a]
        externals = [
            a for a in attendees
            if _is_person(a)
            and _domain(a) not in own
            and a.lower() not in internal
        ]
        if not attendees:
            skipped["no_attendees"] += 1
            continue
        if not externals:
            skipped["internal_only"] += 1
            continue
        for email in externals:
            dedup_id = state_mod.key(event_id, email)
            if dedup_id in seen:
                continue
            seen.add(dedup_id)
            if skip_briefed and state_mod.is_briefed(cfg, event_id, email):
                skipped["already_briefed"] += 1
                continue
            targets.append({
                "event_id": event_id,
                "title": ev.get("title", ""),
                "start": ev.get("start", ""),
                "email": email,
                "domain": _domain(email),
            })

    return {"date": date, "targets": targets, "skipped": skipped}
