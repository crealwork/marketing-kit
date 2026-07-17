"""Dedup store — don't brief the same (event, person) twice.

A morning routine may fire more than once (retries, manual re-runs, overlapping
cron windows). Research is expensive (many page fetches), so before spending it
we check a small JSON ledger keyed on (event_id, email).

We deliberately do NOT key on a date. Google Calendar hands out
occurrence-unique event ids for recurring instances (e.g. `abc_20260710T...`),
so the id alone identifies a specific meeting. Freshness is time-based instead:
an entry older than `window_hours` is ignored, so next week's occurrence of a
recurring meeting is briefed again while a same-day re-run is suppressed. Keying
on a sweep date would break dedup the moment the sweep runs on a different day
than the meeting.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


def _path(cfg: dict[str, Any]) -> Path:
    return Path(cfg["dedup"]["state_file"])


def _load(path: Path) -> dict[str, float]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def key(event_id: str, email: str) -> str:
    return f"{event_id}:{email.strip().lower()}"


def is_briefed(cfg: dict[str, Any], event_id: str, email: str) -> bool:
    window_s = float(cfg["dedup"].get("window_hours", 20)) * 3600
    ledger = _load(_path(cfg))
    ts = ledger.get(key(event_id, email))
    if ts is None:
        return False
    return (time.time() - ts) < window_s


def mark(cfg: dict[str, Any], event_id: str, email: str) -> None:
    path = _path(cfg)
    path.parent.mkdir(parents=True, exist_ok=True)
    ledger = _load(path)
    ledger[key(event_id, email)] = time.time()
    # prune anything older than 30 days so the file can't grow forever
    cutoff = time.time() - 30 * 86400
    ledger = {k: v for k, v in ledger.items() if v >= cutoff}
    path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")


def clear(cfg: dict[str, Any]) -> None:
    path = _path(cfg)
    if path.exists():
        path.unlink()
