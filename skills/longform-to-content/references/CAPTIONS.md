# CAPTIONS — getting subtitles exactly right (timing, text, style)

Captions are the most-watched pixels in the video. A caption that is 300ms late, types
the wrong product name, or covers the speaker reads as broken. Every rule here is
mandatory; each traces to a real failure.

## 1. Transcription contract (timing foundation)

- **Word-level verbatim only.** Phrase/SRT modes collapse inter-word gaps — you lose the
  data that drives both cuts and cue timing. Fillers must NOT be normalized away (they
  are editorial signal for the disfluency pass).
- **Known drift:** Scribe word timestamps drift 50–100ms. Whisper drifts more and
  normalizes fillers. This is why every cut edge carries 150–350ms padding and why cues
  get +0.22s tail — the padding absorbs the drift.
- **NEVER transcribe a concatenated edit to make captions.** ASR over a stitched file
  drifts up to ~1s at every cut and compounds. Timing ALWAYS comes from the ORIGINAL
  source transcription, mapped through the edit math (§2). One source file = one cached
  transcription, reused for cuts, full-video captions, shorts captions, SRT.
- Multi-source projects: transcribe each source separately, keep per-source word lists;
  never merge timelines before mapping.

## 2. Output-timeline mapping (the core math)

The edit is a list of kept pieces `(src_start, src_end, out_offset)` in output order,
where `out_offset` = sum of durations of everything before it (highlight clips, intro
card, prior segments). For any word:

```
out_time = word.t - piece.src_start + piece.out_offset   (only if word inside the piece)
```

Mandatory mechanics:
- Build the piece table from the FINAL concat order — if you reorder the cold open,
  regenerate the table; stale offsets desync every cue after the change.
- A cue lives entirely inside ONE piece. Clamp `cue.end ≤ piece_out_end`. A cue that
  crosses a cut boundary shows text over the wrong footage.
- Words that fall inside removed intervals (silence cuts, disfluency cuts) simply
  disappear from captions — filter words by piece bounds, never by "close enough".
  This keeps audio and captions saying the same thing (a cut "특--" must vanish
  from both).
- Cards (intro/outro/endcard) are pieces WITHOUT words → no cues can exist there.
  SELF-TEST: extract a frame mid-card; any caption visible = mapping bug.
- Overlap clamping: after sorting cues, `cue[i].end = min(cue[i].end, cue[i+1].start − 0.02)`.
- Transitions: if you use dissolves/xfades anywhere, EMPTY the cue window during the
  dissolve — text hanging across a blend looks broken.

## 3. Chunking (what one cue contains)

Accumulate words in transcript order; close the chunk when ANY fires:
- length ≥ 26 chars (CJK full video) / ≥ 12–14 chars (CJK shorts) / ~42 chars (Latin)
- the word ends a sentence (`.?!`)
- next-word gap ≥ 0.7s (full) / 0.5s (shorts)

Cue start = first word start (mapped). Cue end = last word end + 0.22s reading tail,
clamped per §2. One line per cue on the full video (26 chars ≈ 1200px at 46px serif —
must stay ≤1360px so it never touches a bottom-right PIP at x=1460). Shorts allow 2
wrapped lines (Alignment 8 grows downward — verify the block clears the element below).

## 4. Text correctness (ASR correction dictionary)

ASR mangles domain terms — one hour of Korean produced ~95 systematic errors
(챗 피티→챗GPT, 크램→CRM, brand names, spelled-out numbers). Method:
1. READ the full packed transcript once; catalog every wrong form while reading.
   EFFORT FLOOR (measurable): for 60+ min of domain speech expect 30–100+ entries;
   fewer than 20 means you skimmed — read again. Coverage test: pick 10 random
   packed-transcript lines containing product/tech terms; every ASR error in them
   must already be in your dictionary.
2. Build an ORDERED replace list, longest/most-specific first
   (`scripts/corrections.py` is the worked example).
3. Scope short patterns to context. Real incident: generic `비, → B, ` (quiz option)
   corrupted `위고비` → `위고B`. If a pattern is ≤2 chars, anchor it with surrounding
   words.
4. Repair particles/grammar when a replacement changes the final sound
   (제미나인은→제미나이는, not 제미나이은).
5. Convert spelled-out numbers ONLY via explicit pairs (구십삼 퍼센트→93%); never a
   generic numeral regex (it eats numbers inside words).
6. Apply to cue text AFTER chunking, BEFORE styling, in every surface (full, shorts, SRT).
7. SELF-TEST (blocking): `grep -c` the top known wrong forms in the final SRT — all 0.
8. Smoke-test the dictionary on 15–20 real transcript sentences BEFORE the burn; fix
   collisions there, not after a 61-minute re-encode.

## 5. Styling (per surface, exact)

- Font choice follows BRAND.md (brand font if Bold + readable; else Pretendard for KR,
  Noto CJK pan-CJK, Inter Latin). The worked ASS line below uses one example family —
  swap `FontName` for the chosen font.
- Fonts for libass: STATIC bold file in a project `fonts/` dir, referenced RELATIVELY
  (`subtitles=x.ass:fontsdir=assets/fonts` with cwd set). Windows absolute `C:` paths
  break the filter at the colon. Variable fonts render at default weight in libass —
  use them only in PIL.
- Over light/busy content (slides, screen shares): opaque box style —
  `BorderStyle=3`, box = ink at ~88% alpha, text = canvas color, `Outline` value is the
  box padding (9), `Shadow=0`, Alignment 2, MarginV 42. Worked line:
  `Style: Cap,Noto Serif CJK KR,46,&H00F2F7FA,&H00FFFFFF,&H2017191C,&H2017191C,-1,0,0,0,100,100,0,0,3,9,0,2,60,60,42,1`
- Over a designed flat canvas (shorts): plain ink text, no box, no outline; keyword
  accents via inline `{\c&H<BGR>&}word{\c&H<ink BGR>&}` — 1–3 per short, numbers first.
- ASS colors are &HAABBGGRR (BGR + alpha, 00=opaque). Triple-check channel order.
- Encoding: write .ass as UTF-8 with BOM (`utf-8-sig`).
- Readability floor: 22px effective at 1080-wide; verify at 0.35x phone scale.

## 6. Burn order + verification (blocking gates)

- Captions burn LAST — after relayout, overlays, PIP, cards. One re-encode pass over
  the final concat with `-c:a copy` (audio untouched).
- Verify by LOOKING, not by exit code:
  1. Frame at a known cue → text matches the SRT text at that timestamp.
  2. Frame mid-card → no text.
  3. Frame at the longest cue → clears PIP/elements.
  4. Frame right after a disfluency cut → the cut word is absent from the caption.
  5. Spot-check sync: pick 3 cues spread across the runtime, extract 2s of audio at
     each (`ffmpeg -ss <cue.start> -t 2 -vn`), confirm the spoken words are the cue
     words. Off by >300ms → piece table is stale; rebuild, re-burn.
- SRT ships alongside the burned file (same cues) for platform CC; chapters
  (`M:SS label`) are computed through the same piece table.
