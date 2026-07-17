---
name: ppt-slide-generator
description: >
  Professional presentation slide (PPT) generator with multi-theme system.
  Creates HTML-based 16:9 slides with research, 2-stage content review,
  AI image generation, and PDF download.
  Use this skill whenever the user mentions: PPT, PPT 만들어줘, 프레젠테이션,
  발표자료, 슬라이드, slide deck, presentation, 강의자료, 발표 슬라이드,
  프레젠테이션 만들어줘, 발표자료 제작, lecture slides, or wants to create
  presentation slides. Also trigger when the user says "이 주제로 PPT 만들어줘",
  "[topic] 발표자료", "슬라이드 제작", or any variation of creating presentation
  slide content. Also use when the deliverable is a Google Slides deck
  (구글 슬라이드, Google Slides로 만들어줘, redesign an existing Google Slides/PDF
  deck) — see the Google Slides delivery section.
---

# PPT Slide Generator (프레젠테이션 슬라이드 자동 생성기)

This skill creates professional HTML-based presentation slides (1920x1080, 16:9)
through a complete pipeline: theme selection, topic confirmation, deep research,
2-stage content review, AI image generation, and HTML generation with PDF download.

> **Output format fork — decide FIRST:**
> - Default deliverable (HTML → PDF): follow the steps below.
> - **Editable Google Slides deck** requested (구글 슬라이드, Google Slides,
>   collaborative deck, redesigning an existing Slides deck): read
>   `google-slides-export.md` in this skill folder and build with python-pptx
>   instead of HTML. Content/research/review steps (0-3.5) still apply;
>   Step 4 (HTML) and the download button do not.
> - Redesigning an existing deck from a PDF: skip research/outline gates —
>   extract content + page renders with PyMuPDF (`fitz`), keep copy 1:1,
>   redesign the template only.
> - Both at once (PDF redesign → Google Slides): PDF-redesign rules govern
>   content (skip gates, copy 1:1); Google Slides rules govern build/delivery.

---

## Step 0: Theme Selection + Topic Confirmation

First, check available themes:

1. Read the list of `.md` files in the `themes/` folder (relative to this SKILL.md)
2. Present the available themes to the user and ask them to select one
3. Read the selected theme file to load the design system

Then confirm:
1. **Topic** — What is the presentation about?
2. **Purpose** — Business presentation or educational/lecture material?
3. **Slide count preference** — Short (5-8) / Normal (10-15) / Deep (16-25)
4. **Presenter info** — Name, date, contact (for cover and ending slides)

Don't over-interview. Get the topic confirmed and move to research quickly.

---

## Step 1: Deep Research

Once topic is confirmed, do thorough web research. Research quality directly
determines whether the presentation is valuable or just looks nice.

### What to search for (5-10 searches)

- Key statistics and recent numbers
- Latest trends and market changes
- Comparable data points for before/after or vs. comparisons
- Visualizable data (percentages, growth rates, rankings)
- Real examples or quotable insights
- Source-backed facts (not vague claims)

### Organize your research

After researching, compile:

```
Topic summary (1 line)
Key data points (5-8)
Chart-ready data (numbers that can become visuals)
Memorable example or quote
Key takeaways (3-5)
```

---

## Step 1.5: Narrative Strategy

Design the presentation arc before writing the outline.

### Opening (slides 1-3) must:
1. **Hook the audience** — a bold claim, surprising statistic, or provocative question
2. **Establish the problem/opportunity** clearly
3. **Preview the value** — "by the end of this presentation, you will..."

### Middle (core slides):
- Build logical progression — each slide sets up the next
- Alternate between data/evidence slides and insight/implication slides
- Place the strongest data point at the climax, not the beginning

### Closing (last 2-3 slides):
- Summarize key takeaways (no new information)
- Clear call-to-action or next steps
- End with impact — not a whimper

---

## Step 2: Outline Review (Gate 1)

Present the slide outline to the user for review:

```
Slide 1 [Cover]: Title — "..."
Slide 2 [Agenda]: 3 sections
Slide 3 [Section Divider]: Section 1 — "..."
Slide 4 [Body-Text]: Key message — "..."
Slide 5 [Body-Data]: Chart — "..."
...
Slide N [Ending]: Thank you + contact
```

**Revision loop:** Wait for explicit approval before proceeding.
- If the user requests changes: apply revisions and re-present the updated outline
- Repeat until the user approves
- If the user wants to change the topic direction significantly, go back to Step 1

Only proceed to Gate 2 after explicit approval.

---

## Step 3: Detailed Content Review (Gate 2)

Present full text/data for each slide:

```
Slide 4 [Body-Text]
  Title: "AI 마케팅 도입률 현황"
  Bullet 1: "2026년 기준 글로벌 기업 72%가 ..."
  Bullet 2: "한국 시장은 ..."
  Source: McKinsey 2026 Report
```

Present ALL slides with their complete content. Wait for explicit approval.

**Revision loop:**
- If the user requests changes: apply revisions to specific slides and re-present only the changed slides
- Repeat until the user approves
- If structural changes are needed (add/remove/reorder slides), go back to Gate 1

Only proceed to image generation after explicit approval.

---

## Step 3.5: Image Generation (Optional)

After content approval, before HTML generation:

1. Analyze each slide and identify where images would enhance the presentation
2. Present image prompt proposals to the user:
   ```
   Slide 1 [Cover]: Background — "Professional abstract geometric pattern in navy and gold tones"
   Slide 6 [Quote]: Illustration — "Business team collaborating with AI dashboard"
   → Approve / Edit prompt / Skip all images
   ```
3. For approved prompts, generate images using Gemini API
4. Embed generated images as base64 `data:image/png;base64,...` in the HTML

### Gemini API Call

**Model:** `gemini-3.1-flash-image-preview`

**Authentication:** Uses `GOOGLE_AI_API_KEY` from global environment.

**API pattern:**

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents="Create a professional presentation background: [prompt]",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",  # for slide backgrounds
            image_size="2K"
        )
    )
)

for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("slide-bg.png")
```

**Aspect ratios:**
- Slide backgrounds: `16:9`
- Inline illustrations: `4:3` or `1:1`

### Error Handling

All image generation failures are non-blocking:
- API timeout → skip image, log warning
- Rate limit → wait 5s, retry once, then skip
- Invalid response → skip, proceed without image
- User can skip image generation entirely

If any image fails, note which slides were intended to have images so the user
can retry later.

---

## Step 4: HTML Generation

Read the selected theme file and generate a single HTML file containing all slides.

### Critical Rules

**Rule 1: Static HTML only for slides.**
Every `<div class="slide">` must exist directly in the `<body>`. Never generate
slides with JavaScript. JS-generated slides won't render in preview.

**Rule 2: JavaScript is only for the download button and slide navigator.**
No JS for slide rendering.

**Rule 3: Use Pretendard font via CDN.**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
```

```css
:root {
  --font-main: 'Pretendard Variable', 'Pretendard', 'Apple SD Gothic Neo',
               'Malgun Gothic', 'NanumGothic', sans-serif;
}

* {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

`word-break: keep-all` is mandatory for Korean. Without it, the browser breaks lines
in the middle of words (character by character), which looks broken. `keep-all` forces
line breaks only at spaces, keeping Korean phrases intact.

**Rule 4: Deliver the HTML file directly.** One HTML file, no separate viewer.

**Rule 5: Photos and headshots — use `<img>` with `object-fit` (vector-first path).**

The PRIMARY export path is now Playwright (vector PDF, see Rule 6). Playwright honors `object-fit: cover` perfectly. The html2canvas raster path is fallback-only.

Use `<img>` for photos that need to fit a fixed-ratio container:

```html
<img class="headshot" src="data:image/jpeg;base64,..." alt="Speaker name" />
```

```css
.speaker-photo { width:520px; height:680px; overflow:hidden; }
.headshot { width:100%; height:100%; object-fit:cover; object-position:center top; }
```

**Why not `background-image`:** Chrome's Ctrl+P "Background graphics" checkbox is OFF by default — `<div>` with background-image disappears from the printed PDF. `<img>` always renders. This was a real Dave Kim deck bug.

The old html2canvas-friendly background-image pattern is still acceptable as a fallback only if you can't move to Playwright export.

**Rule 6: Use Playwright for PDF export — html2canvas/Ctrl+P are fallbacks.**

Playwright `page.pdf({width:'1920px', height:'1080px'})` is the only method that guarantees exact 16:9 page size regardless of user environment. Chrome's Ctrl+P UI ignores `@page` CSS when user picks Letter/Legal manually. Always create `render-pdf.py` alongside the deck HTML:

```python
"""Render the deck to a 1920×1080 landscape PDF via Playwright."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent
HTML = HERE / "deck.html"  # adjust to actual filename
OUT = Path.home() / "Downloads" / "deck.pdf"  # adjust


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        ctx = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await ctx.new_page()
        await page.goto(HTML.as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")  # wait for web fonts (FOUT guard)
        await page.pdf(
            path=str(OUT), width="1920px", height="1080px",
            print_background=True,
            margin={"top":"0","right":"0","bottom":"0","left":"0"},
            prefer_css_page_size=False,
        )
        await browser.close()
    print(f"PDF written to {OUT} ({OUT.stat().st_size:,} bytes)")


asyncio.run(main())
```

**Auto-open after creation/modification (MANDATORY):**
After running render-pdf.py, always chain `start "" "<output.pdf>"` so the user sees the result immediately. Same for the source HTML during iteration:

```bash
python render-pdf.py && start "" "%USERPROFILE%\Downloads\deck.pdf"
```

If the PDF is locked by an open viewer (PermissionError), fall back to V{N+1}.pdf naming (e.g., V4 → V5).

**Print CSS still required** for the rare Ctrl+P fallback path:

```css
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body {
    background: #fff !important; margin: 0; padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  .slide-nav, .download-section { display: none !important; }
  .deck { padding: 0 !important; }
  .slide {
    margin: 0 !important; box-shadow: none !important;
    page-break-after: always; page-break-inside: avoid; break-after: page;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  .slide:last-child { page-break-after: auto; break-after: auto; }
}
```

`print-color-adjust:exact` prevents Chrome's ink-saver from stripping accent colors. The html2canvas download button stays as a tertiary fallback in the download section.

### Slide Dimensions

Each slide: `width: 1920px; height: 1080px` (16:9 ratio).

```css
.slide {
  width: 1920px;
  height: 1080px;
  padding: 80px 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
}
```

`position: relative` is required so that absolutely-positioned children (slide-number,
slide-footer) are positioned relative to the slide, not the viewport.

### Font Size Minimums

| Element | Size | Weight |
|---------|------|--------|
| Slide title | 48px ~ 64px | 800 |
| Subtitle / section heading | 36px ~ 44px | 700 |
| Body text | 28px ~ 34px | 400-500 |
| Number callouts | 72px ~ 120px | 900 |
| Caption / source | 20px ~ 24px | 400 |
| Slide number | 18px ~ 20px | 400 |

These are MINIMUM sizes. If a slide has less content, scale UP the font sizes
to fill the space rather than leaving empty areas.

### Heading Letter Spacing

All headings (h1, h2) must have `letter-spacing: 0.02em` to prevent tight kerning
at large sizes. Add this as a global CSS rule:

```css
h1, h2 { letter-spacing: 0.02em; }
```

### Spacing Rules

- Slide padding: `80px ~ 100px`
- Content block gap: `40px+`
- Bullet point spacing: `32px+`

### Data Visualization

For stable PNG rendering, do NOT use external chart libraries (Chart.js, etc.).

**Allowed methods:**
- Inline SVG
- HTML/CSS div-based charts (width percentages, flexbox bars, etc.)

**Recommended chart types (mix at least 2-3 per presentation):**
- Donut/pie charts (SVG)
- Bar charts (CSS divs)
- Comparison bars (side-by-side CSS)
- Progress bars
- Big number + label blocks
- Timeline/process flow (CSS flexbox)

**Checklist:**
- Numbers in the chart match the text
- Percentages add up correctly
- Sources are attributed
- Each data slide focuses on one insight

### Slide Numbering

All slides except Cover and Ending/CTA display a slide number.
Position: bottom-right. Format: `N / Total` (e.g., `3 / 15`).

### Slide Navigator (Browser Preview)

Since 1920x1080 slides are larger than typical browser viewports, add a navigation
helper at the top of the HTML:

```html
<div class="slide-nav" id="slideNav">
  <span>Slide Navigator</span>
  <a href="#slide-1">1</a> <a href="#slide-2">2</a> ...
</div>
```

Each slide gets `id="slide-N"`. The nav bar is fixed at top and is NOT inside
any `.slide` element, so it's automatically excluded from PNG capture.

```css
.slide-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: #333;
  color: #fff;
  padding: 8px 16px;
  z-index: 100000;
  display: flex;
  gap: 8px;
  align-items: center;
  font-family: var(--font-main);
  font-size: 14px;
}
.slide-nav a {
  color: #fff;
  background: #555;
  padding: 4px 10px;
  border-radius: 4px;
  text-decoration: none;
}
.slide-nav a:hover { background: #777; }
```

### Year References

Always use the current year. Never hardcode a specific year.

### Download Button (PDF)

Add a download section at the bottom of the HTML (after all slides, before `</body>`).

**Libraries (EXACT CDN URLs — copy exactly, do NOT change versions):**

```html
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.2/dist/jspdf.umd.min.js"></script>
```

CRITICAL:
- Use html2canvas `@1.4.1` + jsPDF `@2.5.2`. Access jsPDF via `window.jspdf.jsPDF`.
- Do NOT use dom-to-image-more — it depends on viewport size and breaks in web/narrow
  browser environments where viewport < 1920px.
- html2canvas `windowWidth: 1920` forces correct rendering regardless of viewport.
- **Use `scale: 3`** (not 2) for crisp text rasterization. Scale 2 produces visible
  jagged edges on large serif/sans headings. Scale 3 ≈ laser-print quality.
- **Use JPEG `quality: 0.95`** (not 0.92). At scale 3, 0.92 adds mosquito noise
  around text edges; 0.95 removes it while still keeping ~5–8MB total for 15 slides.
- The rasterized button output is a *fallback*. The primary path must be **Ctrl+P /
  Cmd+P → "Save as PDF"**, which preserves text as vectors. See Rule 6 and the
  Download Section template below — Ctrl+P must be shown prominently, button small.
- Output is ALWAYS PDF, never PNG ZIP.

**Complete download JS:**

```js
document.getElementById('downloadBtn').addEventListener('click', async function() {
  var btn = this;
  var status = document.getElementById('downloadStatus');
  btn.disabled = true;
  status.textContent = 'PDF 생성 중...';

  try {
    var jsPDF = window.jspdf.jsPDF;
    var pdf = new jsPDF({ orientation: 'landscape', unit: 'px', format: [1920, 1080], hotfixes: ['px_scaling'] });
    var slides = document.querySelectorAll('.slide');

    for (var i = 0; i < slides.length; i++) {
      status.textContent = '슬라이드 처리 중: ' + (i + 1) + '/' + slides.length;

      var canvas = await html2canvas(slides[i], {
        width: 1920,
        height: 1080,
        scale: 3,
        useCORS: true,
        allowTaint: true,
        scrollX: 0,
        scrollY: -window.scrollY,
        windowWidth: 1920,
        windowHeight: 1080
      });

      var imgData = canvas.toDataURL('image/jpeg', 0.95);
      if (i > 0) pdf.addPage([1920, 1080], 'landscape');
      pdf.addImage(imgData, 'JPEG', 0, 0, 1920, 1080);
    }

    status.textContent = 'PDF 저장 중...';
    pdf.save('{topic}-presentation.pdf');
    status.textContent = '✓ 다운로드 완료!';
  } catch (error) {
    console.error('Download failed:', error);
    status.textContent = '오류: ' + error.message;
  } finally {
    btn.disabled = false;
  }
});
```

Replace `'{topic}-presentation.pdf'` with the actual sanitized topic name
(lowercase, hyphens, no special characters). Example: `'ai-marketing-presentation.pdf'`

**File naming:** `{topic}-presentation.pdf`

**Download Section UI (MANDATORY pattern):**

The download area must prominently promote **Ctrl/Cmd+P** as the best-quality path.
The html2canvas download button is shown as a smaller, de-emphasized fallback next
to it. Never lead with the rasterized button.

```html
<div class="download-section">
  <div class="best-option">
    <div class="best-label">★ Recommended — Best Quality</div>
    <div class="best-title">Press <kbd>Ctrl</kbd>+<kbd>P</kbd> → “Save as PDF”</div>
    <div class="best-note">Windows: <b>Ctrl+P</b> &nbsp;·&nbsp; Mac: <b>Cmd+P</b><br>Text stays vector-perfect. Use this option.</div>
  </div>
  <div class="fallback">
    <div class="fallback-label">Or — rasterized fallback</div>
    <button id="downloadBtn">Download PDF</button>
    <div id="downloadStatus"></div>
  </div>
</div>
```

```css
.download-section {
  max-width: 1400px; margin: 60px auto 80px; text-align: center;
  color: #fff; font-family: var(--font-main, 'Inter', sans-serif);
  display: flex; gap: 24px; align-items: stretch; justify-content: center;
  flex-wrap: wrap;
}
.best-option {
  flex: 1 1 520px; max-width: 680px;
  background: #1a1a1a; border: 2px solid var(--accent, #3B82F6);
  padding: 36px 44px; border-radius: 10px;
  display: flex; flex-direction: column; justify-content: center;
}
.best-label {
  color: var(--accent, #3B82F6); font-size: 12px; font-weight: 700;
  letter-spacing: 4px; text-transform: uppercase; margin-bottom: 14px;
}
.best-title {
  color: #fff; font-size: 30px; font-weight: 600;
  margin-bottom: 10px; line-height: 1.2;
}
.best-title kbd {
  background: #fff; color: #000; padding: 6px 14px;
  border-radius: 6px; font-family: 'SF Mono', 'Monaco', monospace;
  font-size: 22px; margin: 0 4px; font-weight: 700;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.35);
}
.best-note { color: #bbb; font-size: 14px; line-height: 1.5; }
.fallback {
  flex: 0 1 340px; opacity: 0.55;
  display: flex; flex-direction: column; justify-content: center;
  padding: 20px;
}
.fallback-label {
  color: #888; font-size: 11px; letter-spacing: 2px;
  text-transform: uppercase; margin-bottom: 12px; font-weight: 600;
}
#downloadBtn {
  background: transparent; color: #bbb; border: 1px solid #444;
  padding: 12px 28px; font-size: 13px; font-weight: 500;
  letter-spacing: 1.5px; text-transform: uppercase; cursor: pointer;
  border-radius: 4px;
}
#downloadBtn:hover { background: #333; color: #fff; border-color: #666; }
#downloadBtn:disabled { opacity: 0.5; cursor: not-allowed; }
#downloadStatus { margin-top: 14px; color: #888; font-size: 12px; }
```

The accent border on `.best-option` should use the theme's accent color so the
Ctrl+P card feels native to the deck. Everything else stays neutral dark.

---

## Step 4.5: Self-Review (MANDATORY before delivery)

**Never deliver a deck without running self-review first.** Capture each slide as a PNG via Playwright, Read each PNG to inspect visually, fix any issues found, then re-render. Only after all issues resolved → render PDF + auto-open + show user.

### screenshot-slides.py (drop alongside render-pdf.py)
```python
"""Capture each slide as PNG for self-review."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent
HTML = HERE / "deck.html"  # adjust to actual filename
OUT_DIR = HERE / "_review"

async def main():
    OUT_DIR.mkdir(exist_ok=True)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        ctx = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await ctx.new_page()
        await page.goto(HTML.as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        slides = await page.locator(".slide").all()
        for i, slide in enumerate(slides, 1):
            path = OUT_DIR / f"slide-{i:02d}.png"
            await slide.screenshot(path=str(path))
            print(path)
        await browser.close()

asyncio.run(main())
```

### Review checklist for EACH slide
After running `python screenshot-slides.py`, Read each PNG and inspect for:

1. **Line breaks (줄나눔)** — words split mid-sentence in unintended places, "It was" orphaned to next line, Korean mid-word break. Fix with explicit `<br>` placement or font-size reduction.
2. **Image cropping (이미지 잘림)** — headshot off-frame, logo wall last logo cut on right, background-image stripped (if any remaining), photo without `object-fit:cover`. Fix with grid gap, max-width adjustment, or migrate to `<img>` tag.
3. **Text overflow (글 잘림)** — statement-line exceeding max-width, split slide right column truncated, cover-meta colliding with cover-sub (absolute positioning collision), footer wordmark cut. Fix with max-width adjustment, padding correction, or content trim.
4. **Size mismatch (사이즈 안맞음)** — content overflow beyond 1920×1080 (hidden by `overflow:hidden`), asymmetric split columns (gap+padding miscalculated), billboard-sized type (>180px H1), insufficient whitespace.
5. **Brand consistency** — if the deck belongs to a brand, check its brand guide (`DESIGN.md`) rules: correct fonts for emphasis/italic, accent colors only in allowed positions, wordmark reproduced exactly (including punctuation quirks).

### Iteration loop
- Found issues → list them concretely (slide N + issue) → fix CSS/copy → re-run screenshot script → re-Read affected slides → repeat until clean
- All clear → `python render-pdf.py && start "" "<output>.pdf"`
- Tell user what was caught & fixed:
  > Self-review 1회 돌렸고 N개 이슈 잡아서 수정했어요: [list]. PDF 열었어요.

If genuinely zero issues:
> Self-review 통과. PDF 열었어요.

### Skip conditions (rare)
- User explicitly says "빨리 보여줘", "review skip", "skip review"
- Single-line copy edit on already-shown deck (and visual layout unchanged)
- Non-visual changes (memory update, code-only refactor)

---

## Step 5: Quality Check

Before delivering, verify:

### Content
- All data points are current and accurately represented
- Text matches what was approved in Gate 2
- Narrative arc flows logically from opening to closing
- No slide has more than one key message

### Design
- Visual tone is consistent across all slides
- Text density is comfortable (not wall-of-text)
- Accent colors used sparingly, not overwhelming
- Charts are easy to read at a glance
- Font sizes meet minimums from the table above
- Slide numbers are correct and sequential

### Technical
- HTML renders without errors
- All slides are exactly 1920x1080
- Download button functions correctly
- No external image/resource dependencies (everything is inline)
- Base64 images render correctly
- Korean text wraps at word boundaries, not mid-character

---

## Delivery

Save the final HTML to the outputs folder:

**Output path:** `WARP/ppt-slides/{topic}/{topic}-presentation.html`

Example: `WARP/ppt-slides/ai-marketing/ai-marketing-presentation.html`

Create the folder automatically if it doesn't exist. Then auto-open both the HTML
(`start "" <file>`) and its folder in Explorer. The user previews with the slide
navigator; the delivered PDF comes from `render-pdf.py` (auto-opened as well).
