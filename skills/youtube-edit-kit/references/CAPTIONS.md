# CAPTIONS — getting subtitles exactly right (timing, text, style)

Captions are the most-watched pixels in the video. A caption that is 300ms late,
types the wrong product name, or lingers over a cut reads as broken. Every rule
here traces to a real production failure.

## 1. Timing foundation

- **Word-level verbatim only.** Phrase/SRT transcription modes collapse inter-word
  gaps — you lose the data that drives both cuts and cue timing.
- **NEVER transcribe an edited/concatenated file to make captions.** ASR over a
  stitched file drifts up to ~1s at every cut and compounds. Timing ALWAYS comes
  from the ORIGINAL source transcription, mapped through the edit math (§2).
  One source file = one cached transcription, reused for cuts, captions, shorts, SRT.
- ASR word timestamps drift 50–100ms (whisper more). This is why cut edges carry
  150–350ms padding and cues get a +0.22–0.25s reading tail — padding absorbs drift.

## 2. Output-timeline mapping (the core math — implemented in gen_srt.py)

The edit is a piece table `(src_start, src_end, out_offset)` in FINAL concat order:

```
out_time = word.t - piece.src_start + piece.out_offset   (only if word inside the piece)
```

- Rebuild the table whenever concat order changes — stale offsets desync every cue
  after the change.
- A cue lives entirely inside ONE piece; clamp `cue.end ≤ piece_out_end`. A cue
  crossing a cut shows text over the wrong footage.
- Words inside removed intervals disappear from captions — filter by piece bounds,
  never "close enough". Audio and captions must say the same thing.
- Intro/outro cards are pieces WITHOUT words → no cues there. SELF-TEST: frame
  mid-card shows no text.
- Overlap clamping: `cue[i].end = min(cue[i].end, cue[i+1].start − 0.02)`.

## 3. Chunking (what one cue contains)

Close the chunk when ANY fires:
- length ≥ 26 chars (CJK full video) / 12–14 (CJK shorts) / ~42 (Latin full) / ~26 (Latin shorts)
- word ends a sentence (`.?!`)
- next-word gap ≥ 0.7s (full) / 0.5s (shorts)

Cue start = first word start (mapped); end = last word end + reading tail, clamped.

## 4. Text correctness (ASR correction dictionary)

ASR mangles domain terms — an hour of Korean speech produces 30–100+ systematic
errors (챗 피티→챗GPT, brand names, spelled-out numbers). The reviewer is YOU,
the agent — apply your own knowledge of the domain's proper nouns and jargon,
and ask the user for any canonical spelling you can't verify. Method:

0. Run `scripts/scan_terms.py <transcript>` — it mines mechanical candidates
   (latin/brand tokens, inconsistent spellings, spelled acronyms, spelled-out
   numbers, onomatopoeia) into corrections_todo.md. Hints only; it does not
   replace the read in step 1.
1. READ the full packed transcript; catalog every wrong form while reading.
   Fewer than 20 entries on 60+ min of domain speech means you skimmed — read again.
2. Build an ORDERED replace list, longest/most-specific first:
   `corrections.json` = `[["챗 피티", "챗GPT"], ["구십삼 퍼센트", "93%"], ...]`
3. Scope short patterns: a generic ≤2-char rule WILL corrupt unrelated words
   (real incident: `비,`→`B,` turned 위고비 into 위고B). Anchor with surrounding words.
4. Repair particles when a replacement changes the final sound (제미나인은→제미나이는).
5. Numbers ONLY via explicit pairs — never a generic numeral regex.
6. Apply AFTER chunking, in every surface (full video, shorts, SRT) — gen_srt.py
   and gen_shorts.py both take `--corrections`.
7. SELF-TEST (blocking): grep the final SRT for the top known wrong forms → all 0.
8. Smoke-test the dictionary on 15–20 real transcript lines BEFORE the burn.

## 5. Styling

- Font per SETUP.md §3 (brand font if Bold + readable; else Pretendard KR / Inter Latin).
- Over busy footage: bold white text + dark outline (the kit default), or an opaque
  box (`BorderStyle=3`) over light content like slides.
- Shorts keyword accents: 1–3 per short, numbers first, via inline ASS color spans
  (gen_shorts.py `--accent-words`). ASS colors are &HAABBGGRR (BGR!) — triple-check.
- Write .ass as UTF-8 with BOM (`utf-8-sig`). Readability floor: 22px effective at
  1080-wide; verify at 0.35x phone scale.

## 6. Burn order + verification (blocking gates)

- Captions burn LAST — after every overlay — with `-c:a copy`.
- Verify by LOOKING, not by exit code:
  1. Frame at a known cue → text matches the SRT at that timestamp.
  2. Frame at the longest cue → clears every screen element.
  3. Frame right after a disfluency cut → the cut word is absent.
  4. Sync spot-check: 3 cues spread across the runtime, extract 2s audio at each
     (`ffmpeg -ss <cue.start> -t 2 -vn`), confirm spoken words = cue words.
     Off by >300ms → the piece table is stale; rebuild, re-burn.
