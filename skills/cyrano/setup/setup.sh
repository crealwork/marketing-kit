#!/usr/bin/env bash
# cyrano first-run setup. Idempotent, non-blocking, no network, no telemetry.
# Ensures a config.json exists and reports what still needs filling in.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$HERE/.." && pwd)"
CONFIG="$SKILL_DIR/config.json"
EXAMPLE="$SKILL_DIR/config.example.json"

if [ ! -f "$CONFIG" ]; then
  if [ -f "$EXAMPLE" ]; then
    cp "$EXAMPLE" "$CONFIG"
    echo "cyrano: created config.json from example — edit own_domains + delivery."
  else
    echo "cyrano: no config.example.json found; cannot bootstrap." >&2
    exit 1
  fi
else
  echo "cyrano: config.json already present."
fi

# Best-effort status readout (needs python, but never fails the script).
if command -v python3 >/dev/null 2>&1; then PY=python3; else PY=python; fi
if command -v "$PY" >/dev/null 2>&1; then
  ( cd "$SKILL_DIR" && CYRANO_CONFIG="$CONFIG" "$PY" -m engine config ) 2>/dev/null || true
fi

echo ""
echo "Next: set own_domains, pick delivery.mode, and export any channel secrets."
echo "See references/channel-adapters.md."
exit 0
