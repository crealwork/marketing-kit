# Lovable Theme — Presentation Slides

Warm, vibrant, gradient-heavy presentation design system based on the Lovable brand identity.
Cream backgrounds with the signature blue → lavender → pink → red → orange gradient creates
an energetic, modern, and human feel — ideal for product pitches, tech presentations, and
startup-style storytelling.

---

## Brand Defaults

### Color Palette (Lovable Brand Guidelines)

**Neutral Base:**
- Cream (Background): `#FFFCF2` — soft, inviting background for all content slides
- Black (Text): `#1C1C1C` — headings, key text (NOT pure black)
- Gray: `#5F5F5E` — secondary/placeholder text
- Light Gray: `#999999` — captions, footnotes, slide numbers

**Signature Gradient Colors:**
- Blue: `#4D8FF7`
- Lavender: `#B8A4F8`
- Pink: `#FF6CB4`
- Hot Pink/Red: `#FF1A62`
- Orange: `#F18422`
- Warm Orange: `#F5B800`

**Gradient (CSS):**
```css
background: linear-gradient(135deg, #4D8FF7, #B8A4F8, #FF6CB4, #FF1A62, #F18422);
```

The gradient flows Blue → Lavender → Pink → Red → Orange. Used for Cover backgrounds,
Section Dividers, Ending slides, accent lines, and decorative elements.

### Backgrounds

- Default (content slides): `#FFFCF2` (cream) — NOT pure white
- Dark/Vibrant slides (Cover, Section Divider, Ending): gradient above
- Bar chart track: `#F0EDE8` (slightly darker cream)

### Font

**Primary:** Inter — loaded via Google Fonts CDN:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

All slides use `font-family: 'Inter', sans-serif;`

**Ideal (if available locally):** Camera Plain Regular — geometric sans-serif with letter-spacing: -3%, line-height: 115%

**Serif accent (if available):** Freight Text Pro — for large copy moments. Use Inter as fallback.

### Logo

**Files:** `<assets-dir>\lovable\Logo\`

- `lovable-dark-png.png` — **preferred for light/cream slides** (dark text logo)
- `lovable-light-png.png` — **preferred for dark/gradient slides** (light text logo)
- `lovable-logo-bg-light.png` — full logo on light background (black text + gradient heart)
- `lovable-logo-bg-dark.png` — full logo on dark background
- `lovable-icon-bg-light.png` — icon only, light background
- `lovable-icon-bg-dark.png` — icon only, dark background
- `lovable-logo-icon.png` — standalone gradient heart icon

**Usage rules:**
- On cream/light slides: use `lovable-dark-png.png`
- On gradient/dark slides: use `lovable-light-png.png`
- Target size: height `36px` in footer, maintain aspect ratio
- Position: bottom-left footer

**Fallback (if local file unavailable):** Text-only footer:

```html
<div class="slide-footer">
  <span class="logo-text">Lovable</span>
</div>
```

```css
.logo-text {
  font-family: 'Inter', sans-serif;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #4D8FF7, #FF6CB4, #F18422);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
/* On gradient/dark bg: color: #FFFFFF; -webkit-text-fill-color: #FFFFFF; */
```

---

## Design Language

- **Mood:** Warm, vibrant, energetic, human, modern — approachable yet professional
- **Signature element:** The blue→lavender→pink→red→orange gradient — use it for covers, section breaks, accents, and progress fills
- **Shadows:** Soft shadows for content cards (`box-shadow: 0 4px 24px rgba(0,0,0,0.06)`)
- **Decorative elements:** Gradient accent lines (3-4px), the gradient heart icon as a subtle background watermark
- **Whitespace:** Generous — content breathes, never crowded
- **Contrast:** Cream (#FFFCF2) backgrounds with near-black (#1C1C1C) text; white text on gradient backgrounds
- **Letter-spacing:** Tight, especially for headings (`letter-spacing: -0.02em` to `-0.03em`)
- **Border-radius:** Rounded elements — bars, cards, badges use `border-radius: 8px` to `16px`

---

## Tone & Language Guide

- **Default language:** Korean (한국어)
- **Tone:** 친근하면서도 전문적 — 사람 냄새 나는 언어, 과도한 격식 없이 핵심 전달
- **Technical terms:** 영문 원어를 병기하되, 슬라이드에는 가독성 우선
  - e.g., "바이브 코딩 (Vibe Coding)"
- **Slide text:** Concise bullet points, NOT full sentences
- **One key message per slide** — if you have 2-3 ideas, split into separate slides
- **Numbers:** Bold, large callout stats feel very on-brand for Lovable

---

## Slide Types

### 1. Cover Slide

The first impression. Signature gradient background, centered content, white text, Lovable logo prominent.

```html
<div class="slide slide-cover" id="slide-1">
  <div class="cover-content">
    <div class="cover-tag">Lovable Presentation</div>
    <h1 class="cover-title">슬라이드 제목</h1>
    <p class="cover-subtitle">부제 또는 한 줄 설명</p>
    <div class="cover-meta">
      <span>발표자명</span>
      <span>2026.03.19</span>
    </div>
  </div>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-light-png.png" class="logo" alt="Lovable" />
  </div>
</div>
```

```css
.slide-cover {
  background: linear-gradient(135deg, #4D8FF7, #B8A4F8, #FF6CB4, #FF1A62, #F18422);
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.cover-tag {
  font-size: 20px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.80);
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-bottom: 32px;
}
.cover-title {
  font-size: 64px;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  margin-bottom: 24px;
}
.cover-subtitle {
  font-size: 30px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 48px;
}
.cover-meta {
  font-size: 20px;
  color: rgba(255, 255, 255, 0.65);
  display: flex;
  gap: 32px;
  justify-content: center;
}
```

**Usage notes:**
- No slide number on Cover
- Date should use the current date, never hardcoded
- The gradient background IS the brand — do not replace with a flat color
- Optional: overlay the gradient heart icon (`lovable-logo-icon.png`) at large scale (400-600px, opacity 0.08) as a background watermark

### 2. Agenda Slide

Clean numbered list on cream background. Numbers carry the gradient.

```html
<div class="slide slide-agenda" id="slide-2">
  <h2 class="slide-title">목차</h2>
  <div class="agenda-list">
    <div class="agenda-item">
      <span class="agenda-num">01</span>
      <span class="agenda-text">섹션 제목</span>
    </div>
    <div class="agenda-item">
      <span class="agenda-num">02</span>
      <span class="agenda-text">섹션 제목</span>
    </div>
    <div class="agenda-item">
      <span class="agenda-num">03</span>
      <span class="agenda-text">섹션 제목</span>
    </div>
  </div>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-dark-png.png" class="logo" alt="Lovable" />
  </div>
  <div class="slide-number">2 / Total</div>
</div>
```

```css
.slide-agenda { background: #FFFCF2; }
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #1C1C1C;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
  padding-bottom: 20px;
  border-bottom: 3px solid transparent;
  border-image: linear-gradient(90deg, #4D8FF7, #FF6CB4, #F18422) 1;
}
.agenda-list { display: flex; flex-direction: column; gap: 40px; margin-top: 24px; }
.agenda-item { display: flex; align-items: center; gap: 32px; }
.agenda-num {
  font-size: 48px;
  font-weight: 900;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #4D8FF7, #FF6CB4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  min-width: 80px;
}
.agenda-text {
  font-size: 34px;
  font-weight: 600;
  color: #1C1C1C;
  letter-spacing: -0.02em;
}
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #999999;
}
.slide-footer {
  position: absolute;
  bottom: 40px;
  left: 60px;
}
.slide-footer .logo { height: 36px; }
```

**Usage notes:**
- Slide number shown (e.g., `2 / 15`)
- Keep to 3-5 agenda items max
- Each agenda item maps to a Section Divider slide later
- Gradient numbers are the visual hook — keep them large

### 3. Section Divider

Full gradient background, large section number, white text. Signals a new chapter.

```html
<div class="slide slide-section" id="slide-N">
  <div class="section-content">
    <span class="section-num">01</span>
    <h2 class="section-title">섹션 제목</h2>
    <div class="section-accent"></div>
  </div>
</div>
```

```css
.slide-section {
  background: linear-gradient(135deg, #4D8FF7, #B8A4F8, #FF6CB4, #FF1A62, #F18422);
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.section-num {
  font-size: 96px;
  font-weight: 900;
  letter-spacing: -0.04em;
  color: rgba(255, 255, 255, 0.30);
  line-height: 1;
  display: block;
}
.section-title {
  font-size: 52px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-top: 16px;
  color: #FFFFFF;
}
.section-accent {
  width: 80px;
  height: 4px;
  background: rgba(255, 255, 255, 0.50);
  border-radius: 2px;
  margin: 32px auto 0;
}
```

**Usage notes:**
- No slide number on Section Dividers
- Section number matches the Agenda numbering (01, 02, 03...)
- The large ghost number in 30% opacity white creates depth without distraction
- Optional: add a one-line subtitle below the title in `rgba(255,255,255,0.70)`

### 4. Body (Text)

The workhorse slide. Title + bullet points on cream background.

```html
<div class="slide slide-body" id="slide-N">
  <h2 class="slide-title">슬라이드 제목</h2>
  <ul class="body-list">
    <li class="body-item">
      <span class="bullet">●</span>
      <span class="item-text">본문 텍스트 — 핵심 내용을 간결하게</span>
    </li>
    <li class="body-item">
      <span class="bullet">●</span>
      <span class="item-text">두 번째 포인트</span>
    </li>
    <li class="body-item">
      <span class="bullet">●</span>
      <span class="item-text">세 번째 포인트</span>
    </li>
  </ul>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-dark-png.png" class="logo" alt="Lovable" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-body { background: #FFFCF2; }
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #1C1C1C;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
  padding-bottom: 20px;
  border-bottom: 3px solid transparent;
  border-image: linear-gradient(90deg, #4D8FF7, #FF6CB4, #F18422) 1;
}
.body-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 36px;
  padding: 0;
  margin: 24px 0 0 0;
}
.body-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}
.bullet {
  font-size: 18px;
  margin-top: 8px;
  background: linear-gradient(135deg, #4D8FF7, #FF6CB4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  flex-shrink: 0;
}
.item-text {
  font-size: 30px;
  font-weight: 400;
  color: #1C1C1C;
  line-height: 1.6;
  word-break: keep-all;
}
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #999999;
}
.slide-footer {
  position: absolute;
  bottom: 40px;
  left: 60px;
}
.slide-footer .logo { height: 36px; }
```

**Usage notes:**
- Max 5-6 bullet points per slide. If more, split into two slides
- If only 2-3 bullets, scale up font sizes to fill the space
- The gradient accent line under the title is the Lovable signature touch — always include it
- `word-break: keep-all` is required for Korean text to prevent mid-word line breaks

### 5. Body (Data/Chart)

Data-focused slide with chart area on cream background.

```html
<div class="slide slide-data" id="slide-N">
  <h2 class="slide-title">데이터 제목</h2>
  <div class="chart-area">
    <!-- Example: CSS bar chart -->
    <div class="bar-chart">
      <div class="bar-row">
        <span class="bar-label">항목 A</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 72%;">72%</div>
        </div>
      </div>
      <div class="bar-row">
        <span class="bar-label">항목 B</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 45%;">45%</div>
        </div>
      </div>
      <div class="bar-row">
        <span class="bar-label">항목 C</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: 88%;">88%</div>
        </div>
      </div>
    </div>
  </div>
  <p class="chart-source">Source: Lovable 2026 Report</p>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-dark-png.png" class="logo" alt="Lovable" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-data { background: #FFFCF2; }
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
  font-size: 26px;
  font-weight: 600;
  color: #1C1C1C;
  min-width: 160px;
  text-align: right;
  letter-spacing: -0.01em;
}
.bar-track {
  flex: 1;
  height: 48px;
  background: #F0EDE8;
  border-radius: 8px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #4D8FF7, #FF6CB4);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 16px;
  font-size: 22px;
  font-weight: 700;
  color: #FFFFFF;
  transition: width 0.6s ease;
}
.chart-source {
  font-size: 20px;
  color: #999999;
  text-align: right;
  margin-top: 16px;
}
```

**Usage notes:**
- One insight per data slide — don't cram multiple charts
- Big number callouts should be 72px+ with font-weight 900, color `#1C1C1C`
- For a secondary chart color, use `#F18422` (Orange) or `#B8A4F8` (Lavender) as contrast fills
- Always attribute the data source
- For donut/pie charts, use the gradient colors in sequence: Blue, Lavender, Pink, Orange

### 6. Quote/Highlight

Centered emphasis slide for key statements. Cream background with gradient quote mark.

```html
<div class="slide slide-quote" id="slide-N">
  <div class="quote-content">
    <span class="quote-mark">"</span>
    <p class="quote-text">핵심 인용문 또는 강조하고 싶은 문장</p>
    <p class="quote-author">— 출처 또는 화자</p>
  </div>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-dark-png.png" class="logo" alt="Lovable" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-quote {
  background: #FFFCF2;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.quote-content { max-width: 1400px; }
.quote-mark {
  font-size: 120px;
  line-height: 0.8;
  display: block;
  background: linear-gradient(135deg, #4D8FF7, #FF6CB4, #F18422);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.quote-text {
  font-size: 40px;
  font-weight: 700;
  color: #1C1C1C;
  line-height: 1.5;
  letter-spacing: -0.02em;
  word-break: keep-all;
  margin: 32px auto;
}
.quote-author {
  font-size: 24px;
  color: #5F5F5E;
  margin-top: 24px;
  font-weight: 400;
}
```

**Usage notes:**
- Use for research findings, expert quotes, or key takeaways that deserve emphasis
- Keep quote text under 2 lines for maximum impact
- Alternative: use the gradient background (Cover style) for an extra-punchy highlight quote — in that case use white text and `lovable-light-png.png` logo
- `word-break: keep-all` required for Korean text

### 7. Ending/CTA

Closing slide. Signature gradient background, white text, contact info.

```html
<div class="slide slide-ending" id="slide-N">
  <div class="ending-content">
    <h2 class="ending-title">감사합니다</h2>
    <p class="ending-subtitle">질문이 있으시면 편하게 말씀해주세요</p>
    <div class="ending-contact">
      <span>email@example.com</span>
      <span>@lovable</span>
    </div>
  </div>
  <div class="slide-footer">
    <img src="<assets-dir>\lovable\Logo\lovable-light-png.png" class="logo logo-ending" alt="Lovable" />
  </div>
</div>
```

```css
.slide-ending {
  background: linear-gradient(135deg, #4D8FF7, #B8A4F8, #FF6CB4, #FF1A62, #F18422);
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.ending-title {
  font-size: 64px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 24px;
}
.ending-subtitle {
  font-size: 30px;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 48px;
  font-weight: 400;
}
.ending-contact {
  display: flex;
  gap: 48px;
  font-size: 24px;
  color: #FFFFFF;
  font-weight: 600;
  justify-content: center;
}
.logo-ending { height: 48px; }
```

**Usage notes:**
- No slide number on Ending
- Contact info uses presenter info from Step 0
- White contact text is readable on the gradient — no color change needed
- Optional: "Q&A" or "함께 만들어봐요" as alternative title for workshop/product settings
- Optional: overlay the gradient heart icon at large scale (opacity 0.08) as a background watermark

---

## Data Visualization Guidelines

### Color usage in charts

- Primary bars/segments: Blue `#4D8FF7`
- Secondary/contrast: Pink `#FF6CB4`
- Tertiary: Orange `#F18422`
- Fourth: Lavender `#B8A4F8`
- Fifth: Warm Orange `#F5B800`
- Background/track: `#F0EDE8` (slightly darker cream)
- Gradient fills (for single-series bars): `linear-gradient(90deg, #4D8FF7, #FF6CB4)`

### Chart types and when to use

- **Bar chart:** Comparing quantities across categories — use gradient fill for single series
- **Donut/pie (SVG):** Showing proportions — use gradient color sequence (Blue, Lavender, Pink, Orange)
- **Progress bar:** Showing completion or adoption rates — gradient fill mandatory
- **Big number block:** Single standout statistic (72px+ font, `#1C1C1C`, weight 900)
- **Side-by-side comparison:** Before/after or A vs B — Blue vs Pink
- **Timeline/process flow:** Showing steps — use the gradient as a connecting line

### Rules

- Mix at least 2-3 different chart types per presentation
- Each data slide = one key insight
- All numbers must match the approved content from Gate 2
- Always show the source
- Numbers in the chart must match the text on the slide
- Percentages must add up correctly
- Gradient fills preferred over flat colors for single-metric charts — it's the Lovable signature

---

## Common Mistakes to Avoid

1. **Too much text per slide** — presentations are projected, not read. Max 5-6 bullet points.
2. **Inconsistent backgrounds** — cream (`#FFFCF2`) for content slides, gradient for Cover/Section/Ending only. Never swap these.
3. **Flat colors instead of gradient** — the gradient IS the Lovable brand. Cover, Section, and Ending slides must use the full gradient, not a single solid color.
4. **Missing slide numbers** — every content slide needs `N / Total` except Cover, Section Divider, and Ending.
5. **Charts without labels** — every data point needs a readable label. Never show a chart with unlabeled bars.
6. **Tiny text** — presentation fonts must be large. Never go below the minimums in SKILL.md.
7. **No brand presence** — every slide needs the Lovable logo or text footer (gradient text fallback).
8. **Full sentences** — use concise bullet points. Cut unnecessary words.
9. **Crowded data slides** — one insight per slide, never a dashboard.
10. **Ignoring word-break** — Korean text MUST use `word-break: keep-all` to prevent mid-word line breaks. Apply to `.item-text`, `.quote-text`, and any wrapping body copy.
