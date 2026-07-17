# SHORTS — vertical clips that survive a cold feed

A short is watched by someone who never saw the long-form, mid-scroll,
sound-maybe-on. Every rule serves one test: **does a cold viewer get the full
argument with zero context in under 65 seconds?**

## 1. Moment selection (from the packed transcript — read it, don't grep it)

How many (confirm with the user before rendering; ceilings, not quotas):

| source runtime | default count |
|---|---|
| < 20 min | 2–3 |
| 20–45 min | 3–5 |
| 45–90 min | 5–7 |
| > 90 min | 6–8 |

Candidate criteria (ALL must hold):
- **Self-contained**: opens a claim and closes it. Needs "as I said earlier"? Not a short.
- **Hook in the first sentence**: a number (99%, $20), a contrarian imperative
  ("don't learn no-code tools"), or a meta-reveal. No hook = no short.
- **40–65s after internal tightening** (IG ceiling is 90s total).
- **No out-of-context risk**: no legal/medical/gray-area claims needing surrounding nuance.

Series composition: spread moments across the whole runtime, vary hook types
(number / contrarian / meta / stat — never two of the same back-to-back), keep a
used-hooks list across episodes.

## 2. Layout (1080x1920, crop mode — gen_shorts.py)

The kit center-crops the source to 9:16 (pass `--crop-x` if the speaker is
off-center — extract a frame and LOOK first). Safe zones:

| zone | y-range | content |
|---|---|---|
| top ~140px | 0–140 | platform status chrome — nothing load-bearing |
| hook title | ~150–400 | 2 lines, ONE accent span (this is the short's "thumbnail") |
| speaker | middle | the footage itself |
| caption band | ~1150–1300 | word-timed cues, 12–14 chars (CJK) |
| bottom ~350px | 1570–1920 | platform UI (caption/buttons) — nothing load-bearing |

## 3. Hook titles (the 2 lines above the fold)

- ≤ 10 chars per line (CJK) / ~4 words (Latin), 2 lines max, no ending punctuation.
- Exactly ONE accent span (`*asterisks*` in `--title`) — the number or the verb,
  never the whole line.
- Quotable from the clip itself — no promises the clip doesn't say.
- Unique across the series AND across episodes.

## 4. Build (per short)

```
python scripts/gen_shorts.py source.mp4 --transcript t.json --start 841.5 --end 897.2 \
    --title "99% quit\nright *here*" --accent-words 99% -o shorts/short_01.mp4
```

- Word-snapped segments; internal gap-split **0.9s** (tighter than the 1.75s
  long-form threshold — shorts pacing dies on 1s pauses); 30ms afades everywhere.
- Captions burned LAST; `--captions-only` re-burns text fixes in seconds without
  re-rendering segments (the `_raw` file is kept for exactly this).
- Corrections dictionary applies here too (`--corrections`, CAPTIONS.md §4).

## 5. First-frame rule (this IS the shorts cover)

YouTube Shorts and IG Reels use frame #1 as the cover. Frame #1 must show the
full layout with the hook title readable — never black, never mid-fade.
SELF-TEST: `ffmpeg -ss 0.04 -i short.mp4 -frames:v 1 f.png` and READ it.

## 6. Platform envelope

1080x1920 (9:16), H.264 + AAC, ≤ 90s total, source fps is fine (24/30 — don't
resample for platform myths). IG profile-grid covers crop to a CENTER 1:1 square —
if publishing to IG Reels with a dedicated cover, keep everything load-bearing
inside y≈420–1500.

## 7. Self-tests before delivery (blocking)

1. Duration 40–90s — outside = reselect or retighten.
2. Frame t=0.04: full layout + title visible.
3. Phone test: 0.35x downscale — title and captions readable, nothing under 22px effective.
4. Accent spans render; no known-bad ASR forms in any cue.
5. Series check: hooks distinct, moments spread across the runtime.
