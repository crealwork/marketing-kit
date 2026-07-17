"""cyrano — pre-meeting contact intelligence engine.

The thin, deterministic layer under the cyrano skill:
  - config : load + merge config.json, resolve env-backed secrets
  - filter : detect external attendees from calendar events
  - state  : dedup store so the same meeting isn't briefed twice
  - deliver: channel adapters (return | slack | telegram | email)
  - fetch_bridge: proxy to the bundled insane-search fetch engine

All judgement (research, summarising, angle-finding) lives in SKILL.md and is
done by the host agent. This package only does the mechanical parts.
"""

__version__ = "0.1.0"
