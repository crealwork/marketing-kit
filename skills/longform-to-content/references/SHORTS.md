# SHORTS — vertical clips that survive a cold feed (all rules mandatory)

A short is watched by someone who never saw the long-form, mid-scroll, sound-maybe-on.
Every design decision below serves one test: **does a cold viewer get the full argument
with zero context in under 65 seconds?**

## 1. Moment selection (from the packed transcript — read it, don't grep it)

How many: use the runtime table in PIPELINE.md §8 (2–3 for <20min up to 6–8 for 90min+),
capped by qualified candidates, and CONFIRM the count with the user before rendering.

Candidate criteria (ALL must hold):
- **Self-contained**: the excerpt opens a claim and closes it. If understanding needs
  the previous slide or "as I said earlier", it's not a short.
- **Hook in the first sentence**: a number (99%, $20, 93%), a contrarian imperative
  ("배우지 마세요"), or a meta-reveal ("이거 AI가 만들었습니다"). No hook = no short.
- **40–65s after internal tightening** (endcard adds ~1.4s; IG ceiling is 90s total).
- **On-screen match**: the slide/scene visible during the excerpt must relate to the
  claim — verify against the slide-change timeline (PIPELINE.md §2). A "$20 tool" quote
  over an unrelated diagram reads broken.
- **No out-of-context risk**: no legal/medical/gray-area claims that need surrounding
  nuance. (A $1.8B telehealth story was rejected for exactly this in the proven run.)

Series composition (for N shorts):
- Spread source moments across the whole runtime — not three clips from one chapter.
- Hook DIVERSITY: number / contrarian / meta / stat — no two shorts with the same hook
  type back-to-back in the schedule.
- Short #1 (first published) = the long-form thumbnail's claim (YOUTUBE.md §5).

## 2. Canvas architecture (1080x1920) — zones and why

| zone | y-range | content | rationale |
|---|---|---|---|
| header | 0–140 | wordmark (44px, y96 center) | top ~108px sits under platform status chrome — keep only brand, no info |
| hook title | 140–330 | 2 lines, 64px/88lh, ONE accent span | restates the claim for sound-off scrollers; this is the short's "thumbnail" |
| main visual | 352–937 | slide/content card 1040x585 @ (20,352), r18 + shadow | the SHARPEST source (downscaled) carries information |
| caption band | ~1010–1300 | ASS Alignment 8, MarginV 1010 | between visual and face = natural eye path |
| face card | 1360–1754 | webcam 700x394 @ (190,1360), r20 + shadow | face builds trust; cap upscale at 1.5x of source or it goes mushy — NEVER blow a 480px webcam to full width |
| footer | ~1832 | series label, 30px gray | bottom ~350px overlaps platform UI (caption/buttons) — nothing load-bearing here |

Canvas = brand canvas color; card shadows blur 16 alpha ~110; all geometry lives in
DESIGN.md so the whole series is identical.

Source-shape variants (measure the recording first — PIPELINE.md §2):
- **No screen share (pure talking head):** invert — face card becomes the main zone
  (still ≤1.5x upscale; crop tighter instead of scaling bigger), slide zone dropped,
  captions move to the freed center.
- **No webcam (screen/slides only):** drop the face card entirely; recenter the
  content card vertically (~y420), caption band moves to ~y1120, and tighten cues to
  ≤12 chars — a face-less short lives or dies on the hook title + captions. Do NOT
  stretch the 16:9 content card to fill the face zone.

## 3. Hook titles (the 2 lines above the fold)

- ≤ 10 chars per line (CJK), 2 lines max, no ending punctuation.
- Exactly ONE accent-colored span — the number or the verb, never the whole line.
- Must be quotable from the clip itself (no promises the clip doesn't say).
- Unique across the series AND across episodes — keep a used-hooks list; reusing
  a framing reads as template spam.
- Worked set: `99%는 여기서 / 포기합니다` · `노코드 툴, / 배우지 마세요` ·
  `$20라면, / 클로드 vs 챗GPT`.

## 4. Build (per short)

1. Segments: word-snapped ranges; internal gap-split at **0.9s** (tighter than the
   1.75s long-form threshold — shorts pacing dies on 1s pauses); pads 0.20/0.25s;
   30ms afades every boundary.
2. Background PNG (PIL): canvas + wordmark + hook title + card shadows + footer —
   ONE static image per short; video layers composite onto it.
3. Per-segment ffmpeg: bg → content crop scaled into card (alphamerge rounded mask) →
   webcam crop into face card (same) → identical codec params as long-form → concat
   `-c copy`.
4. Endcard 1.4s: brand wordmark + series line, silent audio track (anullsrc), fade-in
   0.25s. Same codec or the concat breaks.
5. Captions LAST onto the concat (CAPTIONS.md; shorts specifics: 12–14 char cues,
   plain ink, keyword accents 1–3 per short — numbers first, chosen from the hook).
6. `--captions-only` mode: keep the pre-caption concat (`_raw`) so text fixes re-burn
   in seconds without re-rendering segments.

## 5. First-frame rule (this IS the shorts thumbnail)

YouTube Shorts and IG Reels use frame #1 as the cover. Frame #1 must show the full
designed layout with the hook title readable — never a black frame, never mid-fade,
never a transition. SELF-TEST: extract frame at t=0.04 and READ it.

## 6. Platform envelope (one file serves both)

- 1080x1920 (9:16), H.264 + AAC, ≤ 90s total (IG hard ceiling; YT Short ≤ 3min but
  match IG), ≤ 300MB (ours are 3–6MB).
- **IG Reels MUST ship a dedicated cover** (`platformSpecificData.instagramThumbnail`,
  presigned URL). The profile grid crops covers to a CENTER 1:1 square — design the
  cover 1080x1920 with everything load-bearing inside y≈420–1500: hook title
  (2 lines, ~96px, one accent span) + the person's cutout + brand mark. Frame 1 of
  the video is NOT an acceptable cover (its title sits above the grid crop).
  SELF-TEST: center-crop the cover to 1:1 and READ it — title + face fully visible.
- Cover cannot be changed via API after publish — attach it BEFORE the scheduled
  time. If a reel already went live without one, the user sets it manually in the
  IG app (profile → reel → 수정 → 커버) with the generated cover file.
- Source fps is fine (24/30); don't resample just for platform myths.
- Title/caption/hashtag rules: YOUTUBE.md §5; scheduling cadence: YOUTUBE.md §6.

## 7. Self-tests before delivery (blocking)

1. Duration 40–90s including endcard — outside = reselect or retighten.
2. Frame t=0.04: full layout + title visible (rule §5).
3. Phone test: 0.35x downscale — hook title, captions, slide headline all readable;
   nothing below 22px effective.
4. Keyword accents render (frame at an accented cue) and corrections applied
   (no known-bad ASR forms in any cue).
5. Endcard present, last frame clean.
6. Series check: hooks distinct, moments spread, short #1 = thumbnail claim.
