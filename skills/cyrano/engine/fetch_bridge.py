"""Bridge to the bundled insane-search fetch engine.

cyrano ships insane-search alongside it (the fork bundle), so blocked sites
(LinkedIn, X, etc.) can be read without a separate install. This is a thin
convenience wrapper: `python -m engine fetch <url>` routes to the sibling
engine. The host agent may also call insane-search directly per its SKILL.md.

If the bundled engine is missing, we say so clearly so the caller can fall back
to WebFetch / firecrawl instead of failing silently.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from .config import SKILL_DIR

_INSANE_DIR = SKILL_DIR.parent / "insane-search"


def available() -> bool:
    return (_INSANE_DIR / "engine" / "__main__.py").exists()


def fetch(url: str, extra: list[str] | None = None) -> tuple[int, str]:
    if not available():
        return 3, (
            "insane-search engine not bundled at "
            f"{_INSANE_DIR}. Fall back to WebFetch / firecrawl for this URL."
        )
    cmd = [sys.executable, "-m", "engine", url, *(extra or [])]
    # Force UTF-8 in the child: insane-search prints page text straight to
    # stdout, which crashes on a Windows cp1252 console for any non-Latin1
    # character. PYTHONUTF8=1 makes the child's stdout UTF-8 without patching
    # the bundled upstream. (See feedback_python_windows_encoding.)
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    try:
        proc = subprocess.run(
            cmd, cwd=str(_INSANE_DIR), capture_output=True,
            text=True, encoding="utf-8", errors="replace", timeout=120, env=env,
        )
    except subprocess.TimeoutExpired:
        return 4, f"insane-search timed out on {url}"
    out = proc.stdout or ""
    if proc.returncode != 0 and proc.stderr:
        out += "\n[stderr]\n" + proc.stderr
    return proc.returncode, out
