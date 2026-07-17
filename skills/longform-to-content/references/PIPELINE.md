# PIPELINE — Gate 2: recording → full edit + shorts (all steps mandatory)

Reference implementations in `scripts/` (adapt the constants at the top of each file —
paths and geometry are per-project). Proven on an 81-min Google Meet webinar → 61-min
published edit + 6 shorts (2026-07-10).

## 0. Project layout

```
<work>/recording.mp4          # copy of source, never edited in place
<work>/edit/                  # transcripts/, assets/, clips_full/, shorts/, verify/, project.md
<work>/final/                 # deliverables only
```
Windows rules W1–W4 (SETUP.md §2/§8 + PIL in-place save ban) apply to every step.

## 1. Transcribe ONCE (cached)

`video-use` helpers → word-level verbatim JSON + packed phrase view. Default backend is
FREE local whisper.cpp; switch to paid Scribe only for multi-speaker recordings
(diarization) or heavy ASR errors — both emit the same JSON (SETUP.md §4):
```
# default (free): whisper.cpp
uv run python helpers/transcribe_whispercpp.py <work>/recording.mp4 --edit-dir <work>/edit
# upgrade (paid, multi-speaker): ElevenLabs Scribe
uv run python helpers/transcribe.py <work>/recording.mp4 --edit-dir <work>/edit --language <xx>
PYTHONUTF8=1 uv run python helpers/pack_transcripts.py --edit-dir <work>/edit
```
Never re-transcribe an unchanged file. Never phrase/SRT mode (kills gap data).
READ the entire packed transcript before cutting — cut decisions come from reading,
not from heuristics.

## 2. Discover structure (before any cut)

- Extract 8 spread frames; READ them (layout, waiting room, screen-share type).
- Slide/scene timeline: 5s-interval thumbnails of the content region → PIL grayscale
  diff (change = >1% pixels differ by >30). ffmpeg scene-detect misses light slides.
  → `scripts/scan_slides.py` (ready to run).
- MEASURE the layout per recording (never reuse blindly): PIL brightness-run bounds on
  3 frames from different sections must agree ±4px. → `scripts/measure_layout.py`
  (ready to run; exits nonzero on disagreement, reports no-webcam sources). Example (Google Meet 1080p):
  share `crop=1440:810:0:135`, webcam tile `crop=480:270:1440:405` — constant across
  speaker switches; browser shares letterbox INSIDE the same region (keep one crop).
- **Recordings VARY — derive the layout, never assume it.** Three source shapes:
  (a) share + webcam (the worked example), (b) share only / NO webcam → skip the PIP
  branch entirely, content fills the frame (§5), shorts drop the face card
  (SHORTS.md §2), (c) talking head only / no share → face track is the main visual
  (SHORTS.md §2 inversion; full video = the face framed 16:9, no PIP).
- **Close discovery with a strategy confirmation — WAIT for the user's OK before any
  rendering:** estimated final length + cut approach, shorts COUNT + hook list
  (see §8 count table), thumbnail concepts, posting cadence. Executing before the
  user confirms is a violation, not initiative.

## 3. EDL — what stays

- Cut pre-start waiting room entirely; open on the presenter's first content sentence.
- Interactive dead-air (quizzes, polls): manual keep-list — question + answer only,
  target ≤ 50% of raw length. Q&A: keep, gap-trim only.
- Silence: split at inter-word gaps > 1.75s; pads head 0.30 / tail 0.35 / edges
  0.15–0.25; merge segments < 0.8s. Every edge ON a word boundary. → `scripts/gen_edl.py`

## 4. Disfluency pass (말더듬)

`scripts/scan_fillers.py` rules: standalone fillers (어/음/uh/um; dur ≥ 0.12s, gapped),
`--`/`-` false starts, comma-restarts (uni+bigram), emphasis whitelist (정말/너무/really…).
Expected 5–30s total removed — outside that range means the rules misfired; stop and inspect.

## 5. Relayout render

Per-segment ffmpeg → lossless `-c copy` concat (NEVER one-pass filtergraph). Content
region scaled to full frame + webcam as rounded PIP (mask via alphamerge, shadow plate).
Identical codec params on every clip: `libx264 -crf 18 -preset veryfast -pix_fmt yuv420p
-r <src fps> -video_track_timescale 90000` + `aac 192k 48k stereo`.
30ms afade in/out at EVERY boundary. Audio stays original — no denoise/EQ/loudnorm
unless the user opts in after an A/B sample. → `scripts/render_full.py`
- No-webcam source: drop the PIP/mask/shadow inputs from the filter graph — content
  crop → full frame is the whole video track. No-share source: crop/frame the face
  track to 16:9; there is no PIP to place.

## 6. Cold open + cards

- 4–6 clips, 25–35s, word-snapped, each from a different visual moment; no
  out-of-context-risk quotes (legal/medical/gray-area claims).
- **Clip #1 = the thumbnail's claim.** Non-negotiable (see THUMBNAILS.md).
- Intro card: real title frame, stale text PIL-erased, ~4.5s, fade from canvas color,
  BGM only here + outro (fade in 1.0 / out 1.4, vol 0.9). → `scripts/gen_final_v4.py`
- BGM sourcing (royalty-free ONLY, never generated speech services): Mixkit
  (https://mixkit.co — no attribution) first, then Incompetech (CC-BY), Pixabay.
  Calm pick metric: spectral centroid < 900 (librosa), longer than needed.

## 7. Captions (burned) + SRT + chapters — full depth in CAPTIONS.md (read it first)

- Chunk words: break at ≥26 chars (CJK) / sentence punctuation / gap ≥ 0.7s.
- Map to OUTPUT timeline: `out = t - piece.src_start + piece.out_offset`.
- Build an ASR-correction dictionary for the brand/domain (`scripts/corrections.py` is
  the worked example): products, phonetic acronyms, numerals. Ordered longest-first;
  scope short patterns to context (a generic rule corrupted an unrelated word once);
  repair particles when hangul→latin swaps change the final sound.
  SELF-TEST: grep the final SRT for the top-5 known wrong forms → all zero.
- Style: opaque ink box + canvas-color text over light content (exact ASS line in
  scripts/gen_final_v4.py); cue width must clear the PIP (≤1360px at 1920).
- Burn LAST after every overlay, `-c:a copy`. Emit .srt + chapters.txt (`M:SS label`).

## 8. Shorts (1080x1920) — full depth in SHORTS.md (read it first)

How many shorts? Scale with runtime, cap by QUALITY, confirm with the user:

| source runtime | default count |
|---|---|
| < 20 min | 2–3 |
| 20–45 min | 3–5 |
| 45–90 min | 5–7 |
| > 90 min | 6–8 |

Counts are ceilings, not quotas — only moments passing ALL SHORTS.md §1 criteria ship;
never pad with weak clips. Propose the count + hook list at strategy confirmation (§2)
and let the user adjust before rendering.

Selection: self-contained 40–65s argument, number/contrarian hook, on-screen content
matches the topic (check the slide timeline), spread across the runtime, no gray-area
claims. Layout + type from DESIGN.md fixed geometry. Internal gap-split 0.9s.
Endcard 1.4s. Captions: corrected, keyword accents (1–3/short, numbers first), burned
LAST; `--captions-only` mode re-burns without re-render. → `scripts/gen_shorts.py`
Zone architecture, hook-title rules, first-frame rule, platform envelope, and the
blocking self-tests live in references/SHORTS.md.

## 9. MANDATORY self-review before showing the user

1. Full video: extract + READ frames at cold-open start, card transition, content
   start, 2 mid, interactive section, last 2s. Check layout / caption box / PIP /
   cards clean / corrections visible.
2. Shorts: first frame + caption frame + endcard each; 0.35x phone-scale text check.
3. `ffprobe` duration vs EDL expectation ±1s.
4. Fix → re-render → re-check, max 3 loops, then flag leftovers honestly.
5. Deliver: auto-open files AND folder. Append `edit/project.md` session log
   (strategy / decisions / reasoning / outstanding).
