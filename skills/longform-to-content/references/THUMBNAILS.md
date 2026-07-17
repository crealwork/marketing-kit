# THUMBNAILS — Gate 3: CTR-style, face required, intro-matched

Produce 3 candidates, 1280x720 PNG, in `final/thumbs/`. The user picks; default = #1.

## Research-backed rules (encode ALL of them in every prompt)

Sourced 2026-07: Ampifire/ClickyApps CTR guides, MrBeast pattern analyses, KR thumbnail
guides. These are requirements, not suggestions:
1. Real human face, 25–40% of canvas, EXAGGERATED emotion (shock/confidence) —
   faces beat object-only thumbnails by 25–30% CTR.
2. Text ≤ 12 characters (KR) / 3–5 words (EN), two lines max, LEFT side
   (bottom-right is covered by the duration badge on mobile).
3. ONE focal point. Face + short text + one number stake. Nothing else.
4. "Impossible contrast": rim-lit subject on a clean saturated background;
   80/20 saturation (subject pops).
5. A number or stake visible (99%, $20, 93%).
6. Legible at 168x94 (YouTube list size) — verify by actually downscaling and READING.

## Generation

Full one-shot generation via the **Higgsfield CLI** (`generate create gpt_image_2
--image photo.png`) WITH the person's real photo as reference — no other route,
no fallback (SETUP.md §6; snippets in the `image-gen` skill). NEVER
AI-generate a face from nothing; NEVER use an illustration-only thumbnail for
YouTube. **Always produce 3+ variants** (expression × composition × background
axes) so the user can A/B them with YouTube Test & compare.

Prompt template:
> YouTube thumbnail, 16:9. The [person] from the reference photo — preserve his/her
> exact face, hairstyle and likeness — [shocked wide-eyed / confident smirk], positioned
> on the right 40 percent of the frame, bright rim lighting. On the left, giant
> ultra-bold [language] text: '[LINE1]' in [color] and '[LINE2]' in [color]. Render this
> text EXACTLY, thick bold gothic sans-serif [+ subtle dark outline on dark bg].
> Background: [one clean saturated color/scene]. Professional [KR] business YouTube
> thumbnail style, extreme contrast, one focal point, vivid colors that pop on mobile.
> No other text, no logos, no watermark.

Ops notes: transient 5xx → retry once with the SAME model (never switch models
silently); resize output → 1280x720; thumbnail file must be < 2MB for YouTube
(convert to JPEG q90 if over).
Cutouts (if compositing instead): local `rembg` with `birefnet-portrait`.

## SELF-TESTS (all mandatory)

1. READ the output: generated text matches character-for-character. Any wrong glyph
   (models drop symbols like "$20"→"0") → REGENERATE with a character-by-character
   instruction. Never inpaint, never ship a typo.
2. Likeness: compare against the reference photo; distorted face → regenerate.
3. 168x94 downscale is legible (text + expression).
4. The 3 candidates are visually distinct (different bg, claim, expression).

## THE MATCH RULE (non-negotiable)

The chosen thumbnail's claim = the FIRST spoken line of the video's cold open.
If they don't match, reorder the cold-open clips (cheap: concat order + caption/SRT/
chapter regen + one burn pass — see scripts/gen_final_v4.py). A thumbnail that the
first 5 seconds doesn't repay trains viewers to bounce.
