# EDIT — source video → published-quality cut (all steps in order)

Scripts live in `scripts/` and are runnable CLIs. Work dir convention:

```
<work>/source.mp4            # copy of source, never edited in place
<work>/edit/                 # transcripts/, edl.json, clips/, cut.mp4, cut.srt
```

## 1. Transcribe ONCE (cached)

```
python scripts/transcribe.py <work>/source.mp4 --edit-dir <work>/edit --language ko
```

Word-level verbatim JSON + a packed phrase view (`.packed.md`). Never re-transcribe
an unchanged file; never phrase/SRT mode (it collapses the inter-word gap data that
drives every cut). READ the entire packed transcript before cutting — cut decisions
come from reading, not from heuristics.

Whisper caveat: it normalizes some fillers away and drifts more than paid ASR.
The edge padding below absorbs the drift; if the recording has multiple speakers
or heavy domain-term errors, offer the Scribe upgrade (SETUP.md §4).

## 2. Strategy confirmation (BLOCKING — before any render)

Present to the user and WAIT for their OK:
- estimated final length + cut approach (what gets removed and why)
- whether a shorts pass follows, and if so the count + hook list (SHORTS.md)
Executing before the user confirms is a violation, not initiative.

## 3. EDL — what stays

```
python scripts/gen_edl.py <work>/edit/transcripts/source.json --source <work>/source.mp4 \
    -o <work>/edit/edl.json
```

- Silence: split at inter-word gaps > 1.75s; pads head 0.30 / tail 0.35 / edges
  0.15–0.25; merge segments < 0.8s. Every edge ON a word boundary — never cut
  inside a word.
- Dead sections (waiting room, off-topic tangents): author keep-windows by reading
  the packed transcript, pass via `--windows windows.json` (`[[start,end],...]`).

## 4. Disfluency pass

```
python scripts/scan_fillers.py <transcript> --edl <edl> -o filler_cuts.json
python scripts/gen_edl.py <transcript> --source <src> --subtract filler_cuts.json -o edl.json
```

Rules: standalone fillers (KR 어/음 + EN uh/um; dur ≥ 0.12s, gapped), `--` false
starts, comma-restarts (uni+bigram), emphasis whitelist. REVIEW the printed context
lines before applying. Expected 5–30s removed per hour of speech — far outside that
range means the rules misfired; stop and inspect.

## 5. Render the cut

```
python scripts/render_cut.py <work>/edit/edl.json -o <work>/edit/cut.mp4
```

Per-segment ffmpeg extract → lossless `-c copy` concat (NEVER one-pass
filtergraph — it double-encodes when overlays are added later). Identical codec
params on every clip. 30ms afade in/out at EVERY boundary. Audio stays original —
no denoise/EQ/loudnorm unless the user opts in after an A/B sample.

## 6. Captions + SRT + chapters — full depth in CAPTIONS.md (read it first)

**6a. Term review (BLOCKING — before any burn).** ASR mangles proper nouns,
jargon, onomatopoeia, numbers. You — the agent — are the reviewer:

```
python scripts/scan_terms.py <transcript> -o corrections_todo.md
```

Read every candidate it surfaces AND the full packed transcript (the scan only
catches mechanical patterns; pure-hangul errors like 챗 피티 only surface by
reading). Resolve each with your own knowledge; ASK THE USER for canonical
spellings you can't verify. Write `corrections.json` (CAPTIONS.md §4) — an empty
`[]` is valid only after this review actually happened.

**6b. Generate + burn:**

```
python scripts/gen_srt.py <transcript> --edl <edl> -o <work>/edit/cut.srt \
    --corrections corrections.json [--chapters chapters_src.txt]
```

Burn (LAST, after any overlays, audio untouched):

```
ffmpeg -i cut.mp4 -vf "subtitles=cut.srt:force_style='FontName=Pretendard,Fontsize=18,Bold=1,Outline=2'" \
    -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a copy -movflags +faststart cut_captioned.mp4
```

Run from the directory containing the SRT — relative path only (Windows `C:`
breaks the filter). Ship the .srt alongside for platform CC.

## 7. MANDATORY self-review before showing the user

1. Extract + READ frames: content start, 2 mid-video, right after a disfluency
   cut, last 2s. Check caption box, corrections visible, no leftover cut words.
2. `ffprobe` duration vs EDL expectation ±1s (render_cut.py prints this).
3. Spot-check sync: 3 cues spread across the runtime — extract 2s audio at each,
   confirm the spoken words are the cue words (CAPTIONS.md §6).
4. Fix → re-render → re-check, max 3 loops, then flag leftovers honestly.
