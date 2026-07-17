# Corporate Theme — Presentation Slides

Generic professional presentation design system for business contexts.
Deep corporate blue + warm amber/gold palette creates a trustworthy, structured,
and authoritative feel suitable for pitches, reports, and corporate presentations.

---

## Brand Defaults

### Color Palette

**Main colors:**
- Primary (Corporate Blue): `#0F4C81` — headings, dark backgrounds, key text
- Accent (Warm Amber): `#E8952E` — highlights, CTAs, emphasis, badges

**Sub colors:**
- Text (Dark Charcoal): `#212529` — body text on light backgrounds
- White: `#FFFFFF` — text on dark backgrounds
- Secondary (Medium Gray): `#6C757D` — secondary text, slide numbers, dividers
- Light (Divider/Track): `#DEE2E6` — dividers, bar chart tracks, subtle elements

### Backgrounds

- Default (content slides): `#F8F9FA` (light gray-white) — NOT pure white
- Dark slides (Cover, Section Divider, Ending): `#0F4C81` (Corporate Blue)

### Font

Inter — loaded via Google Fonts CDN:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

Apply globally: `font-family: 'Inter', sans-serif;`

### Logo Fallback

No brand logo by default. Use text-only footer:

```html
<div class="slide-footer">
  <span class="logo-text">Company Name</span>
</div>
```

```css
.logo-text {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
}
/* On dark bg: color: #E8952E; On light bg: color: #0F4C81; */
```

Replace "Company Name" with the presenter's organization from Step 0.

---

## Design Language

- **Mood:** Professional, trustworthy, structured — clean hierarchy with purposeful use of space
- **Shadows:** Subtle shadows on content blocks (`box-shadow: 0 2px 16px rgba(0,0,0,0.06)`)
- **Decorative elements:** Amber accent lines (3-4px), thin blue rule lines for structure
- **Whitespace:** Generous — content should breathe with clear visual hierarchy
- **Contrast:** High contrast for readability — Blue on light gray, White on Blue

---

## Tone & Language Guide

- **Default language:** Korean (한국어)
- **Tone:** 전문적이고 간결 — 권위 있는 어조로 핵심만 전달
- **Technical terms:** 영문 원어를 병기하되, 슬라이드에는 가독성 우선
  - e.g., "리스크 관리 (Risk Management)"
- **Slide text:** Concise bullet points, NOT full sentences
- **One key message per slide** — if you have 2-3 ideas, split into separate slides

---

## Slide Types

### 1. Cover Slide

The first impression. Deep blue background, centered content, gold accent line.

```html
<div class="slide slide-cover" id="slide-1">
  <div class="cover-accent-line"></div>
  <div class="cover-content">
    <div class="cover-tag">Business Presentation</div>
    <h1 class="cover-title">슬라이드 제목</h1>
    <p class="cover-subtitle">부제 또는 한 줄 설명</p>
    <div class="cover-meta">
      <span>발표자명</span>
      <span>2026.03.19</span>
    </div>
  </div>
  <div class="slide-footer">
    <span class="logo-text" style="color: #E8952E;">Company Name</span>
  </div>
</div>
```

```css
.slide-cover {
  background: #0F4C81;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
  word-break: keep-all;
}
.cover-accent-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: #E8952E;
}
.cover-tag {
  font-size: 18px;
  font-weight: 600;
  color: #E8952E;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-bottom: 32px;
}
.cover-title {
  font-size: 64px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 24px;
}
.cover-subtitle {
  font-size: 30px;
  font-weight: 400;
  color: #DEE2E6;
  margin-bottom: 48px;
}
.cover-meta {
  font-size: 20px;
  color: #6C757D;
  display: flex;
  gap: 32px;
  justify-content: center;
}
```

**Usage notes:**
- No slide number on Cover
- Date should use the current date, never hardcoded
- The gold accent line at the top of the cover is a signature element — do not remove it

### 2. Agenda Slide

Clean numbered list on light background, blue numbers with gold accent.

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
    <span class="logo-text">Company Name</span>
  </div>
  <div class="slide-number">2 / Total</div>
</div>
```

```css
.slide-agenda {
  background: #F8F9FA;
  word-break: keep-all;
}
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #0F4C81;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 3px solid #E8952E;
}
.agenda-list { display: flex; flex-direction: column; gap: 36px; margin-top: 48px; }
.agenda-item { display: flex; align-items: center; gap: 32px; }
.agenda-num {
  font-size: 44px;
  font-weight: 900;
  color: #E8952E;
  min-width: 80px;
}
.agenda-text {
  font-size: 32px;
  font-weight: 600;
  color: #212529;
}
```

**Usage notes:**
- Slide number shown (e.g., `2 / 15`)
- Keep to 3-5 agenda items max
- Each agenda item maps to a Section Divider slide later
- Gold underline on the title reinforces structure

### 3. Section Divider

Full corporate blue background, large gold section number, white title. Signals a new chapter.

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
  background: #0F4C81;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
  word-break: keep-all;
}
.section-num {
  font-size: 96px;
  font-weight: 900;
  color: #E8952E;
  line-height: 1;
}
.section-title {
  font-size: 52px;
  font-weight: 800;
  margin-top: 24px;
}
.section-accent {
  width: 80px;
  height: 4px;
  background: #E8952E;
  margin: 32px auto 0;
}
```

**Usage notes:**
- No slide number on Section Dividers
- Section number matches the Agenda numbering (01, 02, 03...)
- Optional: add a one-line subtitle below the title in `#DEE2E6`

### 4. Body (Text)

The workhorse slide. Title + bullet points on light background.

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
    <span class="logo-text">Company Name</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-body {
  background: #F8F9FA;
  word-break: keep-all;
}
.body-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 36px;
  padding: 0;
  margin: 0;
}
.body-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}
.bullet { color: #E8952E; font-size: 20px; margin-top: 8px; }
.item-text { font-size: 30px; font-weight: 400; color: #212529; line-height: 1.6; }
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #6C757D;
}
.slide-footer {
  position: absolute;
  bottom: 40px;
  left: 60px;
}
```

**Usage notes:**
- Max 5-6 bullet points per slide. If more, split into two slides
- If only 2-3 bullets, scale up font sizes to fill the space
- Can add a gold accent line under the title: `border-bottom: 3px solid #E8952E; padding-bottom: 16px;`

### 5. Body (Data/Chart)

Data-focused slide with chart area using blue/amber colors.

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
    </div>
  </div>
  <p class="chart-source">Source: McKinsey 2026 Report</p>
  <div class="slide-footer">
    <span class="logo-text">Company Name</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-data {
  background: #F8F9FA;
  word-break: keep-all;
}
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
  color: #0F4C81;
  min-width: 160px;
  text-align: right;
}
.bar-track {
  flex: 1;
  height: 48px;
  background: #DEE2E6;
  border-radius: 6px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #0F4C81, #1A6BB5);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 16px;
  font-size: 22px;
  font-weight: 700;
  color: #FFFFFF;
}
.chart-source {
  font-size: 20px;
  color: #6C757D;
  text-align: right;
  margin-top: 16px;
}
```

**Usage notes:**
- One insight per data slide — don't cram multiple charts
- Use Amber (`#E8952E`) as a secondary chart color for contrast and emphasis
- Big number callouts should be 72px+ with font-weight 900 in `#0F4C81`
- Always attribute the data source

### 6. Quote/Highlight

Centered emphasis slide for key statements. Gold quote mark, blue text.

```html
<div class="slide slide-quote" id="slide-N">
  <div class="quote-content">
    <span class="quote-mark">"</span>
    <p class="quote-text">핵심 인용문 또는 강조하고 싶은 문장</p>
    <p class="quote-author">— 출처 또는 화자</p>
  </div>
  <div class="slide-footer">
    <span class="logo-text">Company Name</span>
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-quote {
  background: #F8F9FA;
  justify-content: center;
  align-items: center;
  text-align: center;
  word-break: keep-all;
}
.quote-content { max-width: 1400px; }
.quote-mark {
  font-size: 120px;
  color: #E8952E;
  line-height: 0.8;
  display: block;
}
.quote-text {
  font-size: 40px;
  font-weight: 700;
  color: #0F4C81;
  line-height: 1.5;
  margin: 32px auto;
}
.quote-author {
  font-size: 24px;
  color: #6C757D;
  margin-top: 24px;
}
```

**Usage notes:**
- Use for research findings, expert quotes, or key takeaways that deserve emphasis
- Keep quote text under 2 lines for maximum impact
- Optional: add a thin gold rule line above `.quote-author` for visual separation

### 7. Ending/CTA

Closing slide. Deep blue background, white thank-you message, gold contact info.

```html
<div class="slide slide-ending" id="slide-N">
  <div class="ending-content">
    <h2 class="ending-title">감사합니다</h2>
    <p class="ending-subtitle">질문이 있으시면 편하게 말씀해주세요</p>
    <div class="ending-contact">
      <span>email@example.com</span>
      <span>company.com</span>
    </div>
  </div>
  <div class="slide-footer">
    <span class="logo-text" style="color: #E8952E;">Company Name</span>
  </div>
</div>
```

```css
.slide-ending {
  background: #0F4C81;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
  word-break: keep-all;
}
.ending-title {
  font-size: 64px;
  font-weight: 800;
  margin-bottom: 24px;
}
.ending-subtitle {
  font-size: 30px;
  color: #DEE2E6;
  margin-bottom: 48px;
}
.ending-contact {
  display: flex;
  gap: 48px;
  font-size: 24px;
  color: #E8952E;
  justify-content: center;
}
```

**Usage notes:**
- No slide number on Ending
- Contact info uses presenter info from Step 0
- Use Amber (`#E8952E`) for contact info for visibility on dark background
- Optional: "Q&A" as the title instead of "감사합니다" for lecture/workshop settings

---

## Data Visualization Guidelines

### Color usage in charts
- Primary bars/segments: Corporate Blue `#0F4C81`
- Gradient fill (light end): `#1A6BB5`
- Secondary/contrast: Amber `#E8952E`
- Highlight/emphasis: Amber `#E8952E` at higher opacity
- Background/track: Light Gray `#DEE2E6`

### Chart types and when to use
- **Bar chart:** Comparing quantities across categories
- **Donut/pie (SVG):** Showing proportions of a whole
- **Progress bar:** Showing completion or adoption rates
- **Big number block:** Single standout statistic (72px+ font, `#0F4C81`)
- **Side-by-side comparison:** Before/after or A vs B
- **Timeline/process flow:** Showing steps or chronological progression

### Rules
- Mix at least 2-3 different chart types per presentation
- Each data slide = one key insight
- All numbers must match the approved content from Gate 2
- Always show the source
- Numbers in the chart must match the text on the slide
- Percentages must add up correctly

---

## Common Mistakes to Avoid

1. **Too much text per slide** — presentations are projected, not read. Max 5-6 bullet points.
2. **Inconsistent backgrounds** — light gray-white (`#F8F9FA`) for content, Corporate Blue (`#0F4C81`) for Cover/Section/Ending only.
3. **Amber overuse** — Amber is an accent, not a primary. Use sparingly for numbers, decorative elements, and highlights.
4. **Missing slide numbers** — every content slide needs `N / Total` except Cover, Section Divider, and Ending.
5. **Charts without labels** — every data point needs a readable label and value.
6. **Tiny text** — presentation fonts must be large. Never go below the minimums in SKILL.md.
7. **No brand presence** — every slide needs the company logo or text footer.
8. **Full sentences** — use concise bullet points. Cut unnecessary words.
9. **Crowded data slides** — one insight per slide, not a dashboard.
10. **Ignoring word-break** — Korean text MUST use `word-break: keep-all` to prevent mid-word line breaks.
