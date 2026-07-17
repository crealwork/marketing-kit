# CREAL Theme — Presentation Slides

Professional presentation design system based on the CREAL brand identity.
Navy + Yellow palette creates a trustworthy yet energetic feel suitable for
business presentations and educational materials.

---

## Brand Defaults

### Color Palette (CREAL B.I. Guideline)

**Main colors:**
- Navy (Primary): `#1A2A4F` — headings, dark backgrounds, key text
- Yellow (Accent): `#FFCC4E` — highlights, CTAs, emphasis, badges

**Sub colors:**
- Black: `#000000` — body text on light backgrounds
- White: `#FFFFFF` — text on dark backgrounds
- Warm Gray: `#A39F94` — secondary text, dividers, subtle elements
- Coral: `#D77A61` — charts, secondary accents, warning highlights

### Backgrounds

- Default (content slides): `#F8F5F0` (ivory cream) — NOT pure white
- Dark slides (Cover, Section Divider, Ending): `#1A2A4F` (Navy)

### Font

Pretendard Variable — loaded via CDN in SKILL.md common rules.

### Logo

**Files:** `G:\My Drive\01_CREAL\02_Logo and Branding\01_Logo Package\PNG\`

- Prefer the **Text logo** variant for slide footer
- On dark backgrounds: White or Yellow variant
- On light backgrounds: Black or Blue variant
- Target size: `120px ~ 160px` width, maintain aspect ratio
- Position: bottom-right or bottom-center per slide type

**Fallback (if G: drive unavailable):** Text-only footer:

```html
<div class="slide-footer">
  <span class="logo-text">CREAL</span>
</div>
```

```css
.logo-text {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 4px;
}
/* On dark bg: color: #FFCC4E; On light bg: color: #1A2A4F; */
```

---

## Design Language

- **Mood:** Clean, professional, trustworthy + energetic
- **Shadows:** Soft shadows for depth on content blocks (`box-shadow: 0 4px 20px rgba(0,0,0,0.08)`)
- **Decorative elements:** Yellow accent lines (2-4px), geometric shapes as subtle background elements
- **Whitespace:** Generous — content should breathe, not crowd
- **Contrast:** High contrast for readability — Navy on ivory, White on Navy

---

## Tone & Language Guide

- **Default language:** Korean (한국어)
- **Tone:** 전문적이면서 명확 — 불필요한 수식어 없이 핵심을 전달
- **Technical terms:** 영문 원어를 병기하되, 슬라이드에는 가독성 우선
  - e.g., "마케팅 자동화 (Marketing Automation)"
- **Slide text:** Concise bullet points, NOT full sentences
- **One key message per slide** — if you have 2-3 ideas, split into separate slides

---

## Slide Types

### 1. Cover Slide

The first impression. Navy background, centered content, CREAL branding prominent.

```html
<div class="slide slide-cover" id="slide-1">
  <div class="cover-content">
    <div class="cover-tag">CREAL Presentation</div>
    <h1 class="cover-title">슬라이드 제목</h1>
    <p class="cover-subtitle">부제 또는 한 줄 설명</p>
    <div class="cover-meta">
      <span>발표자명</span>
      <span>2026.03.19</span>
    </div>
  </div>
  <div class="slide-footer">
    <img src="data:image/png;base64,..." class="logo" alt="CREAL" />
  </div>
</div>
```

```css
.slide-cover {
  background: #1A2A4F;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.cover-tag {
  font-size: 22px;
  font-weight: 600;
  color: #FFCC4E;
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
  font-size: 32px;
  font-weight: 400;
  color: #A39F94;
  margin-bottom: 48px;
}
.cover-meta {
  font-size: 22px;
  color: #A39F94;
  display: flex;
  gap: 32px;
  justify-content: center;
}
```

**Usage notes:**
- If a Gemini-generated background image is available, apply it as `background-image` with a dark overlay: `background: linear-gradient(rgba(26,42,79,0.85), rgba(26,42,79,0.85)), url(data:image/png;base64,...); background-size: cover;`
- No slide number on Cover
- Date should use the current date, never hardcoded

### 2. Agenda Slide

Clean numbered list on ivory cream background.

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
    <img src="data:image/png;base64,..." class="logo" alt="CREAL" />
  </div>
  <div class="slide-number">2 / Total</div>
</div>
```

```css
.slide-agenda { background: #F8F5F0; }
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #1A2A4F;
  margin-bottom: 60px;
}
.agenda-list { display: flex; flex-direction: column; gap: 40px; }
.agenda-item { display: flex; align-items: center; gap: 32px; }
.agenda-num {
  font-size: 48px;
  font-weight: 900;
  color: #FFCC4E;
  min-width: 80px;
}
.agenda-text {
  font-size: 34px;
  font-weight: 600;
  color: #1A2A4F;
}
```

**Usage notes:**
- Slide number shown (e.g., `2 / 15`)
- Keep to 3-5 agenda items max
- Each agenda item maps to a Section Divider slide later

### 3. Section Divider

Full Navy background, large section number in Yellow. Signals a new chapter.

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
  background: #1A2A4F;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.section-num {
  font-size: 96px;
  font-weight: 900;
  color: #FFCC4E;
}
.section-title {
  font-size: 52px;
  font-weight: 800;
  margin-top: 24px;
}
.section-accent {
  width: 80px;
  height: 4px;
  background: #FFCC4E;
  margin: 32px auto 0;
}
```

**Usage notes:**
- No slide number on Section Dividers
- Section number matches the Agenda numbering (01, 02, 03...)
- Optional: add a one-line subtitle below the title in Warm Gray

### 4. Body (Text)

The workhorse slide. Title + bullet points on ivory cream.

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
    <img src="data:image/png;base64,..." class="logo" alt="CREAL" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-body { background: #F8F5F0; }
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
.bullet { color: #FFCC4E; font-size: 20px; margin-top: 8px; }
.item-text { font-size: 30px; font-weight: 400; color: #000000; line-height: 1.6; }
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #A39F94;
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
- Can add a subtle Yellow accent line under the title:
  `border-bottom: 3px solid #FFCC4E; padding-bottom: 16px;`

### 5. Body (Data/Chart)

Data-focused slide with chart area.

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
    <img src="data:image/png;base64,..." class="logo" alt="CREAL" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-data { background: #F8F5F0; }
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
  color: #1A2A4F;
  min-width: 160px;
  text-align: right;
}
.bar-track {
  flex: 1;
  height: 48px;
  background: #E8E4DE;
  border-radius: 8px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #1A2A4F, #2A3F6F);
  border-radius: 8px;
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
  color: #A39F94;
  text-align: right;
  margin-top: 16px;
}
```

**Usage notes:**
- One insight per data slide — don't cram multiple charts
- Use Coral (#D77A61) as a secondary chart color for contrast
- Big number callouts should be 72px+ with font-weight 900
- Always attribute the data source

### 6. Quote/Highlight

Centered emphasis slide for key statements.

```html
<div class="slide slide-quote" id="slide-N">
  <div class="quote-content">
    <span class="quote-mark">"</span>
    <p class="quote-text">핵심 인용문 또는 강조하고 싶은 문장</p>
    <p class="quote-author">— 출처 또는 화자</p>
  </div>
  <div class="slide-footer">
    <img src="data:image/png;base64,..." class="logo" alt="CREAL" />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-quote {
  background: #F8F5F0;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.quote-content { max-width: 1400px; }
.quote-mark {
  font-size: 120px;
  color: #FFCC4E;
  line-height: 0.8;
  display: block;
}
.quote-text {
  font-size: 40px;
  font-weight: 700;
  color: #1A2A4F;
  line-height: 1.5;
  margin: 32px auto;
}
.quote-author {
  font-size: 24px;
  color: #A39F94;
  margin-top: 24px;
}
```

**Usage notes:**
- Use for research findings, expert quotes, or key takeaways that deserve emphasis
- Keep quote text under 2 lines for maximum impact
- Optional: add a Gemini-generated illustration alongside the quote

### 7. Ending/CTA

Closing slide. Navy background, thank you message, contact info.

```html
<div class="slide slide-ending" id="slide-N">
  <div class="ending-content">
    <h2 class="ending-title">감사합니다</h2>
    <p class="ending-subtitle">질문이 있으시면 편하게 말씀해주세요</p>
    <div class="ending-contact">
      <span>email@example.com</span>
      <span>@crealwork</span>
    </div>
  </div>
  <div class="slide-footer">
    <img src="data:image/png;base64,..." class="logo logo-ending" alt="CREAL" />
  </div>
</div>
```

```css
.slide-ending {
  background: #1A2A4F;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.ending-title {
  font-size: 64px;
  font-weight: 800;
  margin-bottom: 24px;
}
.ending-subtitle {
  font-size: 30px;
  color: #A39F94;
  margin-bottom: 48px;
}
.ending-contact {
  display: flex;
  gap: 48px;
  font-size: 24px;
  color: #FFCC4E;
  justify-content: center;
}
.logo-ending {
  height: 48px;
  margin-top: 60px;
}
```

**Usage notes:**
- No slide number on Ending
- Contact info uses presenter info from Step 0
- Use Yellow (#FFCC4E) for contact info for visibility on dark background
- Optional: "Q&A" as the title instead of "감사합니다" for lecture/workshop settings

---

## Data Visualization Guidelines

### Color usage in charts
- Primary bars/segments: Navy `#1A2A4F`
- Secondary/contrast: Coral `#D77A61`
- Highlight/emphasis: Yellow `#FFCC4E`
- Background/track: `#E8E4DE` (slightly darker than ivory cream)

### Chart types and when to use
- **Bar chart:** Comparing quantities across categories
- **Donut/pie (SVG):** Showing proportions of a whole
- **Progress bar:** Showing completion or adoption rates
- **Big number block:** Single standout statistic (72px+ font)
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
2. **Inconsistent backgrounds** — ivory cream (#F8F5F0) for content, Navy (#1A2A4F) for Cover/Section/Ending only.
3. **Yellow overuse** — Yellow is an accent, not a primary. Use sparingly for highlights, numbers, decorative elements.
4. **Missing slide numbers** — every content slide needs `N / Total` except Cover, Section Divider, and Ending.
5. **Charts without labels** — every data point needs a readable label.
6. **Tiny text** — presentation fonts must be large. Never go below the minimums in SKILL.md.
7. **No brand presence** — every slide needs the CREAL logo or text footer.
8. **Full sentences** — use concise bullet points. Cut unnecessary words.
9. **Crowded data slides** — one insight per slide, not a dashboard.
10. **Ignoring word-break** — Korean text MUST use `word-break: keep-all` to prevent mid-word line breaks.
