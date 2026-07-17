# Minimal Theme — Presentation Slides

Clean, whitespace-forward presentation design system. Monochrome base with a
single blue accent. Works for any audience, any industry, any language. No
brand-specific elements — just timeless clarity.

---

## Brand Defaults

### Color Palette

**Core:**
- Background: `#FAFAFA` — near-white, used on all content slides
- Text: `#1A1A1A` — near-black, used for all headings and body copy
- Accent: `#3B82F6` — clean blue, used for numbers, highlights, CTAs, emphasis
- Secondary: `#6B7280` — gray, used for subtitles, meta text, slide numbers
- Light Gray: `#E5E7EB` — dividers, bar track backgrounds, ruled lines

**Dark slides (Cover, Section Divider, Ending):**
- Background: `#3B82F6` (Accent blue)
- Text: `#FFFFFF`
- Muted text: `rgba(255,255,255,0.65)`

### Font

Inter — loaded via Google Fonts CDN. Include in the `<head>` of every output file:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

All elements use `font-family: 'Inter', sans-serif;`

### Logo

No logo file. Use a text fallback on every slide footer:

```html
<div class="slide-footer">
  <span class="logo-text">Presentation</span>
</div>
```

```css
.logo-text {
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #6B7280;
}
/* On dark (blue) backgrounds: color: rgba(255,255,255,0.65); */
```

Replace "Presentation" with the presenter's name or organization if provided in Step 0.

---

## Design Language

- **Mood:** Calm, precise, confident — the design stays out of the way of the content
- **Shadows:** Avoid heavy shadows. Use a single subtle shadow when needed: `box-shadow: 0 2px 12px rgba(0,0,0,0.06)`
- **Decorative elements:** Thin rules, accent underlines (3px solid `#3B82F6`), and generous whitespace only. No gradients, no patterns, no textures.
- **Whitespace:** Aggressive — content should feel uncrowded. Increase padding before adding more content.
- **Contrast:** Near-black on near-white for body; white on blue for dark slides.
- **Border radius:** Subtle — `6px` for bars and tags, `0` for most containers.

---

## Tone & Language Guide

- **Default language:** Match the user's input language. If Korean, use `word-break: keep-all` on all text elements.
- **Tone:** Direct and confident — no filler words, no hedging
- **Technical terms:** Use the language of the audience. Minimize jargon unless the content demands it.
- **Slide text:** Tight bullet points, NOT full sentences
- **One key message per slide** — if you have 2-3 ideas, split into separate slides

---

## Slide Types

### 1. Cover Slide

Centered, blue background. Title with a white underline rule for emphasis.

```html
<div class="slide slide-cover" id="slide-1">
  <div class="cover-content">
    <div class="cover-tag">Presentation</div>
    <h1 class="cover-title">Slide Title Here</h1>
    <div class="cover-rule"></div>
    <p class="cover-subtitle">Subtitle or one-line description</p>
    <div class="cover-meta">
      <span>Presenter Name</span>
      <span>2026.03.19</span>
    </div>
  </div>
  <div class="slide-footer">
    <span class="logo-text" style="color: rgba(255,255,255,0.65);">Presentation</span>
  </div>
</div>
```

```css
.slide-cover {
  background: #3B82F6;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.cover-tag {
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.65);
  text-transform: uppercase;
  letter-spacing: 5px;
  margin-bottom: 36px;
}
.cover-title {
  font-size: 64px;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 24px;
  word-break: keep-all;
}
.cover-rule {
  width: 64px;
  height: 3px;
  background: rgba(255,255,255,0.5);
  margin: 0 auto 28px;
}
.cover-subtitle {
  font-size: 28px;
  font-weight: 400;
  color: rgba(255,255,255,0.75);
  margin-bottom: 48px;
  word-break: keep-all;
}
.cover-meta {
  font-size: 20px;
  color: rgba(255,255,255,0.65);
  display: flex;
  gap: 32px;
  justify-content: center;
}
```

**Usage notes:**
- No slide number on Cover
- Date should reflect the current date, never hardcoded
- Replace "Presentation" tag with the deck's category (e.g., "Q2 Review", "Strategy")

### 2. Agenda Slide

Light background. Accent blue numbers set the visual rhythm.

```html
<div class="slide slide-agenda" id="slide-2">
  <h2 class="slide-title">Agenda</h2>
  <div class="agenda-list">
    <div class="agenda-item">
      <span class="agenda-num">01</span>
      <span class="agenda-text">Section Title</span>
    </div>
    <div class="agenda-item">
      <span class="agenda-num">02</span>
      <span class="agenda-text">Section Title</span>
    </div>
    <div class="agenda-item">
      <span class="agenda-num">03</span>
      <span class="agenda-text">Section Title</span>
    </div>
  </div>
  <div class="slide-footer">
    <span class="logo-text">Presentation</span>
  </div>
  <div class="slide-number">2 / Total</div>
</div>
```

```css
.slide-agenda { background: #FAFAFA; }
.slide-title {
  font-size: 40px;
  font-weight: 800;
  color: #1A1A1A;
  margin-bottom: 56px;
  word-break: keep-all;
}
.agenda-list { display: flex; flex-direction: column; gap: 36px; }
.agenda-item { display: flex; align-items: center; gap: 36px; }
.agenda-num {
  font-size: 44px;
  font-weight: 900;
  color: #3B82F6;
  min-width: 80px;
  line-height: 1;
}
.agenda-text {
  font-size: 32px;
  font-weight: 600;
  color: #1A1A1A;
  word-break: keep-all;
}
```

**Usage notes:**
- Slide number shown (e.g., `2 / 15`)
- Keep to 3-5 agenda items max
- Each agenda item maps to a Section Divider slide later

### 3. Section Divider

Full accent-blue background. Section number large and white. Signals a new chapter.

```html
<div class="slide slide-section" id="slide-N">
  <div class="section-content">
    <span class="section-num">01</span>
    <h2 class="section-title">Section Title</h2>
    <div class="section-rule"></div>
  </div>
</div>
```

```css
.slide-section {
  background: #3B82F6;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.section-num {
  font-size: 88px;
  font-weight: 900;
  color: rgba(255,255,255,0.25);
  line-height: 1;
  display: block;
  margin-bottom: 16px;
}
.section-title {
  font-size: 52px;
  font-weight: 800;
  color: #FFFFFF;
  word-break: keep-all;
}
.section-rule {
  width: 48px;
  height: 3px;
  background: rgba(255,255,255,0.5);
  margin: 28px auto 0;
}
```

**Usage notes:**
- No slide number on Section Dividers
- Section number matches the Agenda numbering (01, 02, 03...)
- Optional: add a one-line subtitle below the title in `rgba(255,255,255,0.65)`

### 4. Body (Text)

The workhorse slide. Title with accent underline, clean bullet list.

```html
<div class="slide slide-body" id="slide-N">
  <h2 class="slide-title">Slide Title</h2>
  <ul class="body-list">
    <li class="body-item">
      <span class="bullet">—</span>
      <span class="item-text">Main point — keep it concise and scannable</span>
    </li>
    <li class="body-item">
      <span class="bullet">—</span>
      <span class="item-text">Second point</span>
    </li>
    <li class="body-item">
      <span class="bullet">—</span>
      <span class="item-text">Third point</span>
    </li>
  </ul>
  <div class="slide-footer">
    <span class="logo-text">Presentation</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-body { background: #FAFAFA; }
.slide-title {
  font-size: 40px;
  font-weight: 800;
  color: #1A1A1A;
  padding-bottom: 20px;
  border-bottom: 3px solid #3B82F6;
  margin-bottom: 52px;
  word-break: keep-all;
}
.body-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding: 0;
  margin: 0;
}
.body-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}
.bullet {
  color: #3B82F6;
  font-size: 28px;
  font-weight: 700;
  margin-top: 2px;
  flex-shrink: 0;
}
.item-text {
  font-size: 28px;
  font-weight: 400;
  color: #1A1A1A;
  line-height: 1.6;
  word-break: keep-all;
}
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #6B7280;
  font-family: 'Inter', sans-serif;
}
.slide-footer {
  position: absolute;
  bottom: 40px;
  left: 60px;
}
```

**Usage notes:**
- Max 5-6 bullet points per slide. If more, split into two slides
- If only 2-3 bullets, scale up `item-text` font size to fill the space
- The `border-bottom: 3px solid #3B82F6` on the title is the primary accent — keep it on every body slide

### 5. Body (Data/Chart)

Data-focused slide. Blue bars on a light gray track.

```html
<div class="slide slide-data" id="slide-N">
  <h2 class="slide-title">Data Title</h2>
  <div class="chart-area">
    <div class="bar-chart">
      <div class="bar-row">
        <span class="bar-label">Item A</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 72%;">72%</div>
        </div>
      </div>
      <div class="bar-row">
        <span class="bar-label">Item B</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 45%;">45%</div>
        </div>
      </div>
      <div class="bar-row">
        <span class="bar-label">Item C</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 60%;">60%</div>
        </div>
      </div>
    </div>
  </div>
  <p class="chart-source">Source: Report Name, Year</p>
  <div class="slide-footer">
    <span class="logo-text">Presentation</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-data { background: #FAFAFA; }
.chart-area {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 0;
}
.bar-chart { width: 100%; max-width: 1400px; }
.bar-row {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 28px;
}
.bar-label {
  font-size: 24px;
  font-weight: 600;
  color: #1A1A1A;
  min-width: 160px;
  text-align: right;
  word-break: keep-all;
}
.bar-track {
  flex: 1;
  height: 48px;
  background: #E5E7EB;
  border-radius: 6px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: #3B82F6;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 16px;
  font-size: 20px;
  font-weight: 700;
  color: #FFFFFF;
}
.chart-source {
  font-size: 18px;
  color: #6B7280;
  text-align: right;
  margin-top: 16px;
}
```

**Usage notes:**
- One insight per data slide — do not stack multiple charts
- Big number callouts should be 72px+ with `font-weight: 900` and `color: #3B82F6`
- Always attribute the data source in `.chart-source`
- For a secondary color in charts, use `#6B7280` (gray) to contrast with blue

### 6. Quote/Highlight

Centered emphasis slide. Oversized blue quote mark, large dark text.

```html
<div class="slide slide-quote" id="slide-N">
  <div class="quote-content">
    <span class="quote-mark">"</span>
    <p class="quote-text">Key quote or statement you want to emphasize</p>
    <p class="quote-author">— Source or Speaker</p>
  </div>
  <div class="slide-footer">
    <span class="logo-text">Presentation</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-quote {
  background: #FAFAFA;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.quote-content { max-width: 1400px; }
.quote-mark {
  font-size: 120px;
  color: #3B82F6;
  line-height: 0.8;
  display: block;
  font-weight: 900;
}
.quote-text {
  font-size: 38px;
  font-weight: 700;
  color: #1A1A1A;
  line-height: 1.5;
  margin: 32px auto;
  word-break: keep-all;
}
.quote-author {
  font-size: 22px;
  color: #6B7280;
  margin-top: 24px;
  font-weight: 500;
}
```

**Usage notes:**
- Use for research findings, expert quotes, or key takeaways that deserve full-slide emphasis
- Keep quote text under 2 lines for maximum visual impact
- The quote mark is purely decorative — adjust `line-height` if it crowds the text

### 7. Ending/CTA

Closing slide. Blue background matches Cover. White text, muted contact details.

```html
<div class="slide slide-ending" id="slide-N">
  <div class="ending-content">
    <h2 class="ending-title">Thank You</h2>
    <div class="ending-rule"></div>
    <p class="ending-subtitle">Questions? Let's talk.</p>
    <div class="ending-contact">
      <span>email@example.com</span>
      <span>@handle</span>
    </div>
  </div>
  <div class="slide-footer">
    <span class="logo-text" style="color: rgba(255,255,255,0.65);">Presentation</span>
  </div>
</div>
```

```css
.slide-ending {
  background: #3B82F6;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.ending-title {
  font-size: 64px;
  font-weight: 800;
  margin-bottom: 24px;
  word-break: keep-all;
}
.ending-rule {
  width: 48px;
  height: 3px;
  background: rgba(255,255,255,0.4);
  margin: 0 auto 28px;
}
.ending-subtitle {
  font-size: 28px;
  color: rgba(255,255,255,0.75);
  margin-bottom: 48px;
  font-weight: 400;
  word-break: keep-all;
}
.ending-contact {
  display: flex;
  gap: 48px;
  font-size: 22px;
  color: rgba(255,255,255,0.9);
  font-weight: 500;
  justify-content: center;
}
```

**Usage notes:**
- No slide number on Ending
- Contact info uses presenter details from Step 0
- Alternative title: "Q&A" for lecture or workshop settings
- Keep the ending as sparse as the opening — resist adding bullet points here

---

## Data Visualization Guidelines

### Color usage in charts

- Primary bars/segments: Accent `#3B82F6`
- Secondary/contrast: Secondary `#6B7280`
- Background/track: Light Gray `#E5E7EB`
- Emphasis/highlight: Keep using `#3B82F6` at full opacity; use `rgba(59,130,246,0.3)` for de-emphasized bars

### Chart types and when to use

- **Bar chart:** Comparing quantities across categories
- **Donut/pie (SVG):** Showing proportions of a whole (use `#3B82F6` and `#E5E7EB` as the two-color pair)
- **Progress bar:** Showing completion or adoption rates
- **Big number block:** Single standout statistic — 72px+, `font-weight: 900`, `color: #3B82F6`
- **Side-by-side comparison:** Before/after or A vs B
- **Timeline/process flow:** Showing steps; use `#3B82F6` dots connected by `#E5E7EB` lines

### Rules

- Mix at least 2-3 different chart types per presentation
- Each data slide = one key insight
- All numbers must match the approved content from Gate 2
- Always show the source in `.chart-source`
- Numbers in the chart must match the text on the slide
- Percentages must add up correctly

---

## Common Mistakes to Avoid

1. **Too much text per slide** — this theme rewards restraint. Max 5-6 bullet points. Use whitespace boldly.
2. **Inconsistent backgrounds** — `#FAFAFA` for all content slides; `#3B82F6` for Cover, Section Divider, and Ending only.
3. **Accent overuse** — `#3B82F6` is reserved for numbers, underlines, bullets, bar fills, and quote marks. Do not apply it to body copy.
4. **Missing slide numbers** — every content slide needs `N / Total` in `.slide-number`. Exceptions: Cover, Section Divider, Ending.
5. **Charts without labels** — every bar, segment, or data point needs a readable label inside or beside it.
6. **Tiny text** — minimum font sizes from SKILL.md apply. Never go below them; this theme's font scale is already conservative.
7. **No footer on content slides** — every slide (including dark ones) needs the `.slide-footer` logo-text, even if it is barely visible.
8. **Full sentences in bullets** — use concise fragments. Cut articles, cut hedges, cut filler.
9. **Crowded data slides** — one chart per slide. If you have two datasets, use two slides.
10. **Missing `word-break: keep-all` on Korean text** — apply it to every text element when the presentation language is Korean to prevent mid-word line breaks.
