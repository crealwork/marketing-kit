# Google Slides Delivery Pipeline

Use this path when the deliverable must be an **editable Google Slides deck**
(user says "구글 슬라이드로 만들어줘", "Google Slides", wants to collaborate/present
in Slides) — instead of the default HTML → PDF path in SKILL.md.

Verified end-to-end 2026-07-03 (33-slide Korean webinar deck).

## Pipeline

```
python-pptx build → Drive upload w/ conversion → Slides URL
                       ↓ (same file id, PATCH = stable URL)
              export PDF → PyMuPDF render → visual self-review → fix → re-upload
```

1. **Build** the deck as `.pptx` with python-pptx (installed). Slide size
   `Inches(13.333) x Inches(7.5)`. Type scale: HTML theme px値 ÷ 2 ≈ pt
   (1920px deck ↔ 960pt slide width).
2. **Upload + convert** with `scripts/gdrive.py` →
   `upload_pptx_as_slides(pptx, name)` — uses the clasp OAuth token
   (`~/.clasprc.json`, has `drive.file` scope; account = whichever Google
   account ran `clasp login`). Returns file id →
   `https://docs.google.com/presentation/d/{id}/edit`.
3. **Iterate on the SAME file id**: `upload_pptx_as_slides(pptx, name, file_id=...)`
   PATCHes in place so the shared URL never changes.
4. **Self-review loop (mandatory)**: `export_pdf(file_id, "export.pdf")` →
   render pages with PyMuPDF (`page.get_pixmap(dpi=96)`) → Read each PNG →
   fix layout/copy → rebuild → re-upload. This inspects Google's actual
   rendering, not a local approximation. Never deliver without it.
   (This **replaces** SKILL.md Step 4.5's Playwright screenshot review;
   the Step 5 content/design quality checklist still applies.)
5. Cleanup: `delete_file(id)` for any probe/temp files.

## Font compatibility (pptx → Google Slides conversion)

Fonts are matched **by name string**. Known fonts render as web fonts; unknown
ones silently fall back to Arial (Latin) / Batang·Gulim (Korean).

| Verified OK (2026-07) | FAILS (falls back) |
|---|---|
| Instrument Serif, DM Serif Display (italic), Playfair Display, EB Garamond, Inter, Work Sans | Noto Serif KR |
| Nanum Myeongjo, Nanum Gothic, Gothic A1, Noto Sans KR, Song Myung | |

**Role mapping (Korean editorial deck default):** KR display headings =
Nanum Myeongjo (regular weight at large sizes) · KR body/bullets = Noto Sans KR ·
Latin display + numerals = Instrument Serif · Latin italic emphasis =
DM Serif Display italic · kickers/meta/URLs = Inter (tracked uppercase).

**Korean/Latin run-splitting rule:** setting a Latin `font.name` + east-asian
`<a:ea>` fallback **in one run is unreliable** through conversion. Split text
into separate runs by script:
- Korean run → `font.name = "Nanum Myeongjo"` (its built-in Latin glyphs are fine)
- Latin-only run (kickers, numerals, URLs) → `font.name = "Instrument Serif"` / `"Inter"`

**Probe pattern (do this for any unverified font):** build a 1-slide pptx with
sample lines per font → upload/convert → `export_pdf` → `fitz.open(pdf)[0].get_fonts()`.
`ArialMT`/`Batang`/`Gulim`/`TimesNewRomanPSMT` in the list = a fallback happened;
render the page PNG to see which line. (Arrows `→` and some punctuation in serif
runs harmlessly fall back — check visually before chasing.)

## Styling notes (python-pptx)

- Letter tracking: `run._r.get_or_add_rPr().set("spc", "260")` (1/100 pt).
- Strikethrough: `rPr.set("strike", "sngStrike")` — survives conversion.
- Kill autoshape shadows: `shape.shadow.inherit = False`.
- Hairlines = thin filled rectangles (`height ≈ 1/72 in`), not connectors.
- Rounded card: `MSO_SHAPE.ROUNDED_RECTANGLE` + `shape.adjustments[0] = 0.1`.
- Line breaks: use separate paragraphs, not `\n` inside a run.

## Image generation

All spot-illustration generation goes through the **Higgsfield CLI** (default
model `gpt_image_2` — strong at accurate text/wordmarks). Setup, account check
(`higgsfield account status` BEFORE spending) and command pattern: the
`image-gen` skill in this kit. No silent fallback to other routes.

**Spot-illustration polish (before embedding on white slides):** AI images come
back with near-white (not pure white) backgrounds that show as gray boxes.
Post-process with PIL: white-point lift (`v > 232 → 255`) → autocrop content
bbox → pad to square with ~12% margin.

## Gotchas

- Key/config files may contain non-UTF8 bytes — always
  `read_text(encoding="utf-8", errors="ignore")`.
- Drive `export` can 500 right after conversion — retry with backoff
  (built into `scripts/gdrive.py`).
- The converted deck lands in the clasp account's My Drive root; share or move
  if the user works in another account.
