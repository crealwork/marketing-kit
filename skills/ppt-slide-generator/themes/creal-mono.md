# CREAL Mono Theme — Modern Minimal Presentation

A modern, editorial, near-monochrome theme for CREAL brand presentations.
Off-white background, deep black text, CREAL Yellow as the single subtle
accent. The antithesis of the Navy-heavy `creal.md` — use this for IR decks,
investor updates, product announcements, and any context where a "2026 keynote"
feel is required.

**This theme OVERRIDES the SKILL.md defaults for font and letter-spacing.**
Follow the declarations in this file, not the Pretendard defaults.

---

## Brand Defaults

### Color Palette

**Neutrals (primary surfaces):**
- Background: `#FAFAFA` — off-white (NEVER pure white — too harsh under projection)
- Primary Text: `#0A0A0A` — near-black, not pure black
- Secondary Text: `#737373` — neutral gray for captions, meta, sub-info
- Muted Text: `#A3A3A3` — for lowest-priority labels
- Divider / Hairline: `#E5E5E5` — 1px hairlines only (never thick borders)
- Surface Elevated: `#F3F3F3` — chart tracks, subtle content blocks

**Accent (strict minimal use):**
- CREAL Yellow: `#FFCC4E` — reserved for micro-details ONLY

**Yellow usage rules (ENFORCE STRICTLY — this is the whole point of the theme):**
- Max 1-2 yellow elements per slide
- Total yellow pixel area should be < 2% of the slide
- Allowed yellow uses:
  - A 4px horizontal line under headings
  - Single bullet dot
  - A single highlighted number or percentage
  - A left-side 4px vertical bar on quote slides
  - Slide page number accent
- FORBIDDEN yellow uses:
  - Large filled backgrounds
  - More than one yellow element in the same visual group
  - Yellow text on yellow or yellow inside colored blocks
  - Decorative yellow shapes for "liveliness"

### Backgrounds

**All slides use `#FAFAFA`.** No dark-background cover/section/ending slides
(unlike `creal.md`). The modern minimal aesthetic depends on consistent surface.

### Font

Inter (Latin) + SUITE Variable (Korean) — loaded from jsDelivr CDN.
Do NOT use Pretendard for this theme.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
  @font-face {
    font-family: 'SUITE Variable';
    font-weight: 100 900;
    font-display: swap;
    src: url('https://cdn.jsdelivr.net/gh/sunn-us/SUITE/fonts/variable/woff2/SUITE-Variable.woff2') format('woff2-variations'),
         url('https://cdn.jsdelivr.net/gh/sunn-us/SUITE/fonts/variable/woff2/SUITE-Variable.woff2') format('woff2');
  }
</style>
```

```css
:root {
  --font-main: 'Inter', 'SUITE Variable', -apple-system, BlinkMacSystemFont,
               'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;

  /* Color tokens */
  --bg: #FAFAFA;
  --ink: #0A0A0A;
  --ink-2: #737373;
  --ink-3: #A3A3A3;
  --line: #E5E5E5;
  --surface: #F3F3F3;
  --yellow: #FFCC4E;
}

* { word-break: keep-all; overflow-wrap: break-word; }

/* OVERRIDE of SKILL.md default: headings use NEGATIVE letter-spacing for modern sans-serif kerning */
h1, h2, h3 { letter-spacing: -0.025em; font-feature-settings: "ss01", "cv11"; }
```

**Why `font-feature-settings`:** Inter has OpenType alternates (`ss01` = stylistic
set 1, `cv11` = character variant for a single-storey `a`) that make it feel more
geometric and editorial. Turn them on globally.

**Why SUITE Variable over Pretendard:** SUITE is more geometric, slightly wider,
and has a more neutral tone. It pairs visually with Inter better than Pretendard
(which has a more traditional humanist feel). For a keynote-style modern deck,
SUITE is the stronger choice.

### Logo

**Files:** `G:\My Drive\01_CREAL\02_Logo and Branding\01_Logo Package\PNG\`

- Use the **Black text-only** logo variant (on light background only)
- Target size: `32px ~ 40px` height (smaller than `creal.md` — restraint)
- Position: top-right corner of every slide except Cover
- No yellow or blue logo variants in this theme

**Fallback text logo:**

```html
<div class="brand-mark"><span>CREAL</span></div>
```

```css
.brand-mark {
  position: absolute;
  top: 56px;
  right: 80px;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: var(--ink);
}
```

---

## Design Language

- **Mood:** Editorial, confident, quiet. Like reading The New Yorker's design issue.
- **Shadows:** NONE. No box-shadows. Depth comes from typography, not elevation.
- **Borders:** Only 1px hairlines in `var(--line)`. Never thick borders.
- **Whitespace:** MASSIVE. At least 40% of every slide should be empty.
- **Contrast:** High contrast via typography weight + size, not color.
- **Type scale:** Brutally hierarchical. Title 2-3x bigger than body.
- **No decorative shapes:** No background patterns, no rounded cards, no pills.

### Heading treatment

Headings use `font-weight: 800-900` with `letter-spacing: -0.025em` and
`line-height: 1.05`. This creates the modern "tight, confident" keynote look.

### Body treatment

Body uses `font-weight: 400-500` with `letter-spacing: -0.005em` and
`line-height: 1.55`. Korean text reads slightly loose-tracked for comfort.

---

## Tone & Language Guide

- **Default language:** Korean (한국어), English freely mixed for product terms
- **Tone:** 선언적 — 완결된 짧은 문장. 장식적 수식어 금지.
- **Slide text:** One sentence fragments. "이것이 본질이다" 같은.
- **No multi-line bullets.** Each bullet is one crisp line.
- **Numbers are heroes.** Big number callouts are the theme's signature.

---

## Slide Types

### 1. Cover Slide

Full-bleed off-white. Massive title top-left. Meta at bottom-left. Yellow 4px
horizontal line separating title and meta. Brand mark top-right.

```html
<div class="slide slide-cover" id="slide-1">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="cover-content">
    <div class="cover-eyebrow">CREAL Modern Template</div>
    <h1 class="cover-title">
      모던의<br/>
      본질은<br/>
      제거다.
    </h1>
    <div class="cover-accent"></div>
  </div>

  <div class="cover-meta">
    <div class="cover-meta-row">
      <span class="cover-meta-label">PRESENTER</span>
      <span class="cover-meta-value">Dan Jeong</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">DATE</span>
      <span class="cover-meta-value">2026.04.14</span>
    </div>
  </div>
</div>
```

```css
.slide-cover {
  background: var(--bg);
  justify-content: space-between;
  padding: 120px 120px 100px;
}
.cover-content { max-width: 1500px; }
.cover-eyebrow {
  font-size: 20px;
  font-weight: 600;
  color: var(--ink-2);
  text-transform: uppercase;
  letter-spacing: 0.32em;
  margin-bottom: 48px;
}
.cover-title {
  font-size: 176px;
  font-weight: 900;
  color: var(--ink);
  line-height: 0.95;
  letter-spacing: -0.035em;
  margin: 0;
}
.cover-accent {
  width: 120px;
  height: 4px;
  background: var(--yellow);
  margin-top: 64px;
}
.cover-meta {
  display: flex;
  gap: 80px;
}
.cover-meta-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.cover-meta-label {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink-3);
  letter-spacing: 0.2em;
}
.cover-meta-value {
  font-size: 22px;
  font-weight: 500;
  color: var(--ink);
}
```

**Usage notes:**
- No slide number on Cover
- Title should be 1-3 short words per line, maximum impact
- The yellow 4px line is the ENTIRE color accent on this slide — do not add more
- Date uses the current date dynamically, never hardcoded

### 2. Agenda Slide

Numbered list with hairline dividers. Numbers are large and near-black (NOT yellow
— yellow is reserved). Section labels in plain black.

```html
<div class="slide slide-agenda" id="slide-2">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="slide-eyebrow">CONTENTS</div>
  <h2 class="slide-title">목차</h2>

  <ul class="agenda-list">
    <li class="agenda-item">
      <span class="agenda-num">01</span>
      <span class="agenda-text">디자인 원칙</span>
      <span class="agenda-meta">Design Principles</span>
    </li>
    <li class="agenda-item">
      <span class="agenda-num">02</span>
      <span class="agenda-text">타이포그래피</span>
      <span class="agenda-meta">Typography</span>
    </li>
    <li class="agenda-item">
      <span class="agenda-num">03</span>
      <span class="agenda-text">컬러 시스템</span>
      <span class="agenda-meta">Color System</span>
    </li>
    <li class="agenda-item">
      <span class="agenda-num">04</span>
      <span class="agenda-text">레이아웃</span>
      <span class="agenda-meta">Layout</span>
    </li>
  </ul>

  <div class="slide-number">02</div>
</div>
```

```css
.slide-agenda { background: var(--bg); padding: 120px 120px 100px; }
.slide-eyebrow {
  font-size: 16px;
  font-weight: 700;
  color: var(--ink-3);
  letter-spacing: 0.32em;
  margin-bottom: 24px;
}
.slide-title {
  font-size: 88px;
  font-weight: 900;
  color: var(--ink);
  line-height: 1;
  letter-spacing: -0.03em;
  margin: 0 0 80px 0;
}
.agenda-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.agenda-item {
  display: grid;
  grid-template-columns: 140px 1fr auto;
  align-items: baseline;
  gap: 48px;
  padding: 36px 0;
  border-top: 1px solid var(--line);
}
.agenda-item:last-child { border-bottom: 1px solid var(--line); }
.agenda-num {
  font-size: 40px;
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.agenda-text {
  font-size: 44px;
  font-weight: 600;
  color: var(--ink);
  letter-spacing: -0.02em;
}
.agenda-meta {
  font-size: 20px;
  font-weight: 500;
  color: var(--ink-3);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
```

**Usage notes:**
- 3-5 agenda items MAX. More than 5 = split into two topics.
- The English `agenda-meta` is optional but adds editorial weight
- No yellow on this slide — hairlines and typography carry the design

### 3. Section Divider

Massive section number (200px+) in near-black. Yellow 4px line below number.
Section title below the line.

```html
<div class="slide slide-section" id="slide-3">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="section-content">
    <span class="section-num">01</span>
    <div class="section-line"></div>
    <h2 class="section-title">디자인 원칙</h2>
    <p class="section-sub">Design Principles</p>
  </div>
</div>
```

```css
.slide-section {
  background: var(--bg);
  justify-content: center;
  align-items: flex-start;
  padding: 0 120px;
}
.section-content { max-width: 1600px; }
.section-num {
  display: block;
  font-size: 280px;
  font-weight: 900;
  color: var(--ink);
  line-height: 0.85;
  letter-spacing: -0.05em;
  font-variant-numeric: tabular-nums;
}
.section-line {
  width: 120px;
  height: 4px;
  background: var(--yellow);
  margin: 56px 0 40px;
}
.section-title {
  font-size: 80px;
  font-weight: 800;
  color: var(--ink);
  line-height: 1;
  letter-spacing: -0.03em;
  margin: 0 0 12px 0;
}
.section-sub {
  font-size: 22px;
  font-weight: 500;
  color: var(--ink-2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0;
}
```

**Usage notes:**
- No slide number on Section Dividers
- The giant numeral IS the visual hook — do not add extra decoration
- Keep section title to 1 line, English subtitle to 1 line

### 4. Body (Text)

Eyebrow + large title + 3-5 short bullet statements. Hairline dividers between
bullets. No yellow.

```html
<div class="slide slide-body" id="slide-4">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="slide-eyebrow">01 — DESIGN PRINCIPLES</div>
  <h2 class="slide-title">본질만 남긴다</h2>

  <ul class="body-list">
    <li class="body-item">
      <span class="body-item-num">01</span>
      <span class="body-item-text">장식적 요소는 정보를 희석시킨다.</span>
    </li>
    <li class="body-item">
      <span class="body-item-num">02</span>
      <span class="body-item-text">여백은 비어있는 것이 아니라 작동하는 공간이다.</span>
    </li>
    <li class="body-item">
      <span class="body-item-num">03</span>
      <span class="body-item-text">한 슬라이드에 하나의 메시지만 담는다.</span>
    </li>
    <li class="body-item">
      <span class="body-item-num">04</span>
      <span class="body-item-text">색은 강조를 위한 최후의 수단이어야 한다.</span>
    </li>
  </ul>

  <div class="slide-number">04</div>
</div>
```

```css
.slide-body { background: var(--bg); padding: 120px 120px 100px; }
.slide-body .slide-title { font-size: 72px; margin-bottom: 80px; }
.body-list { list-style: none; padding: 0; margin: 0; }
.body-item {
  display: grid;
  grid-template-columns: 120px 1fr;
  align-items: baseline;
  gap: 40px;
  padding: 32px 0;
  border-top: 1px solid var(--line);
}
.body-item:last-child { border-bottom: 1px solid var(--line); }
.body-item-num {
  font-size: 24px;
  font-weight: 700;
  color: var(--ink-3);
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.02em;
}
.body-item-text {
  font-size: 36px;
  font-weight: 500;
  color: var(--ink);
  line-height: 1.4;
  letter-spacing: -0.015em;
}
```

**Usage notes:**
- 3-5 bullets max. If you have 6+, split into two slides.
- Each bullet is ONE sentence fragment — no multi-line wrapping.
- Eyebrow repeats the current section for context (`01 — DESIGN PRINCIPLES`)

### 5. Body (Data / Big Number)

This is the theme's signature slide. One hero number at massive scale. Supporting
text small. Single yellow accent on the unit or highlight digit.

```html
<div class="slide slide-data" id="slide-5">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="slide-eyebrow">01 — DESIGN PRINCIPLES</div>
  <h2 class="slide-title">노란색은 전체의 <span class="hero-accent">2%</span> 이하</h2>

  <div class="hero-number-block">
    <span class="hero-number">02<span class="hero-unit">%</span></span>
    <p class="hero-caption">
      슬라이드 표면 대비 노란색 픽셀 비율의 상한선. 이 규칙을 지켜야
      액센트가 강조로 작동하고, 초과하면 주목성이 붕괴한다.
    </p>
  </div>

  <div class="data-bars">
    <div class="data-bar-row">
      <span class="data-bar-label">Neutral surface</span>
      <div class="data-bar-track"><div class="data-bar-fill" style="width: 98%;"></div></div>
      <span class="data-bar-value">98%</span>
    </div>
    <div class="data-bar-row">
      <span class="data-bar-label">Yellow accent</span>
      <div class="data-bar-track"><div class="data-bar-fill data-bar-fill--accent" style="width: 2%;"></div></div>
      <span class="data-bar-value">2%</span>
    </div>
  </div>

  <p class="data-source">Source: CREAL Mono Theme spec, 2026</p>
  <div class="slide-number">05</div>
</div>
```

```css
.slide-data { background: var(--bg); padding: 120px 120px 100px; }
.slide-data .slide-title { font-size: 56px; margin-bottom: 60px; }
.hero-accent { color: var(--yellow); }  /* single-digit inline yellow */

.hero-number-block {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 80px;
  align-items: end;
  margin-bottom: 80px;
}
.hero-number {
  font-size: 320px;
  font-weight: 900;
  color: var(--ink);
  line-height: 0.85;
  letter-spacing: -0.05em;
  font-variant-numeric: tabular-nums;
}
.hero-unit {
  font-size: 180px;
  font-weight: 700;
  color: var(--yellow);
}
.hero-caption {
  font-size: 22px;
  font-weight: 400;
  color: var(--ink-2);
  line-height: 1.6;
  max-width: 540px;
  margin: 0 0 48px 0;
}

.data-bars { display: flex; flex-direction: column; gap: 20px; margin-top: 40px; }
.data-bar-row {
  display: grid;
  grid-template-columns: 200px 1fr 80px;
  align-items: center;
  gap: 24px;
}
.data-bar-label {
  font-size: 18px;
  font-weight: 600;
  color: var(--ink-2);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
.data-bar-track {
  height: 2px;
  background: var(--line);
  position: relative;
}
.data-bar-fill {
  height: 2px;
  background: var(--ink);
}
.data-bar-fill--accent { background: var(--yellow); height: 4px; margin-top: -1px; }
.data-bar-value {
  font-size: 18px;
  font-weight: 700;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  text-align: right;
}
.data-source {
  position: absolute;
  bottom: 56px;
  left: 120px;
  font-size: 14px;
  color: var(--ink-3);
  letter-spacing: 0.04em;
}
```

**Usage notes:**
- One big number per slide, never two
- Yellow can accent either the unit (%, $, x) or a single highlighted digit — never both
- Bar charts use 2px hairlines, not filled rectangles
- The caption is SHORT — 2-3 lines, not a paragraph

### 6. Quote / Highlight

Minimal centered quote. No quotation marks — use a 4px yellow vertical bar as
the left edge instead. That's the entire accent.

```html
<div class="slide slide-quote" id="slide-6">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="quote-wrapper">
    <div class="quote-bar"></div>
    <div class="quote-content">
      <p class="quote-text">완벽함이란 더 이상 더할 것이 없을 때가 아니라,<br/>더 이상 뺄 것이 없을 때 달성된다.</p>
      <p class="quote-author">— 앙투안 드 생텍쥐페리 <span class="quote-author-sub">Antoine de Saint-Exupéry</span></p>
    </div>
  </div>

  <div class="slide-number">06</div>
</div>
```

```css
.slide-quote {
  background: var(--bg);
  justify-content: center;
  align-items: center;
  padding: 0 160px;
}
.quote-wrapper {
  display: grid;
  grid-template-columns: 4px 1fr;
  gap: 56px;
  align-items: start;
  max-width: 1500px;
}
.quote-bar {
  width: 4px;
  min-height: 280px;
  background: var(--yellow);
}
.quote-content { padding-top: 8px; }
.quote-text {
  font-size: 60px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.25;
  letter-spacing: -0.025em;
  margin: 0 0 48px 0;
}
.quote-author {
  font-size: 22px;
  font-weight: 600;
  color: var(--ink-2);
  letter-spacing: 0.02em;
  margin: 0;
}
.quote-author-sub {
  color: var(--ink-3);
  font-weight: 500;
  margin-left: 12px;
  letter-spacing: 0.06em;
}
```

**Usage notes:**
- Quote text max 2 lines. If it's longer, you have the wrong quote.
- Yellow vertical bar is the entire accent — do NOT add quotation marks
- Always attribute the author in both Korean and original-language form when possible

### 7. Ending / CTA

Mirror of the Cover, closing the loop. Large "Thank you" headline, yellow
horizontal accent line, contact info below in small gray.

```html
<div class="slide slide-ending" id="slide-7">
  <div class="brand-mark"><span>CREAL</span></div>

  <div class="ending-content">
    <div class="cover-eyebrow">END OF DECK</div>
    <h1 class="ending-title">
      Thank<br/>
      you.
    </h1>
    <div class="cover-accent"></div>
  </div>

  <div class="ending-meta">
    <div class="cover-meta-row">
      <span class="cover-meta-label">EMAIL</span>
      <span class="cover-meta-value">hello@example.com</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">WEB</span>
      <span class="cover-meta-value">crealwork.com</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">SOCIAL</span>
      <span class="cover-meta-value">@crealwork</span>
    </div>
  </div>
</div>
```

```css
.slide-ending {
  background: var(--bg);
  justify-content: space-between;
  padding: 120px 120px 100px;
}
.ending-content { max-width: 1500px; }
.ending-title {
  font-size: 240px;
  font-weight: 900;
  color: var(--ink);
  line-height: 0.9;
  letter-spacing: -0.04em;
  margin: 0;
}
.ending-meta {
  display: flex;
  gap: 80px;
}
```

**Usage notes:**
- No slide number on Ending
- "Thank you" can be replaced with "Q&A", "Questions?", or a bold one-word CTA
- Email/web/social are optional — show what's relevant to the context

---

## Global Slide Infrastructure

### Slide container

```css
.slide {
  width: 1920px;
  height: 1080px;
  box-sizing: border-box;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: var(--font-main);
  color: var(--ink);
  background: var(--bg);
}
```

### Brand mark (top-right on every slide except Cover)

```css
.brand-mark {
  position: absolute;
  top: 64px;
  right: 120px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.32em;
  color: var(--ink);
}
```

### Slide number (bottom-right on content slides)

```css
.slide-number {
  position: absolute;
  bottom: 56px;
  right: 120px;
  font-size: 14px;
  font-weight: 600;
  color: var(--ink-3);
  letter-spacing: 0.08em;
  font-variant-numeric: tabular-nums;
}
```

Format: zero-padded 2-digit (`01`, `02`, `03`) — no `/Total`. The minimalism
of the theme doesn't tolerate the extra slash.

---

## Data Visualization Guidelines

### Color usage in charts
- Primary bars / segments: `var(--ink)` (near-black)
- Baseline / track: `var(--line)` (1-2px hairline)
- Highlight / accent: `var(--yellow)` (exactly ONE element per chart)
- Secondary: `var(--ink-2)` (mid gray)

### Chart style
- Bars are 2-4px tall hairlines, NOT filled rectangles
- Pie/donut charts use stroke, not fill (1.5px-3px stroke-width)
- Numbers in tabular-nums font-variant
- No gridlines — whitespace is the gridline
- No legends if only 2 categories — label inline

---

## Common Mistakes to Avoid

1. **Using yellow as a primary color** — It's an accent. If you see more than 2
   yellow elements on a slide, delete one.
2. **Adding box-shadows for depth** — This theme has NO shadows. Period.
3. **Using Pretendard** — This theme mandates Inter + SUITE Variable. The other
   CREAL theme (`creal.md`) uses Pretendard; this one does NOT.
4. **Positive letter-spacing on headings** — Modern sans-serif at large sizes
   needs NEGATIVE kerning (`-0.025em` to `-0.04em`). The SKILL.md default of
   `+0.02em` is for serif and must be overridden.
5. **Pure white background** — `#FFFFFF` is too harsh under projection. Use
   `#FAFAFA`.
6. **Navy anywhere** — This theme is explicitly the NON-navy CREAL variant.
   Don't reach for `#1A2A4F` out of habit.
7. **Decorative cards / rounded corners** — Keep it flat. Hairlines only.
8. **Filling whitespace "because it looks empty"** — If a slide has 40% empty
   space, it's working correctly. Do not add content.
9. **Multiple data points on one data slide** — This theme has ONE hero number
   per slide. If you have two stats, split into two slides.
10. **Long quotes** — Quote slides in this theme max out at 2 lines. Find a
    shorter quote.

---

## When to use this theme vs `creal.md`

| Context | Theme |
|---------|-------|
| Lectures, workshops, educational | `creal.md` (Navy+Yellow, warmer) |
| IR / investor decks / fundraising | **`creal-mono.md`** |
| Product announcements (B2B) | **`creal-mono.md`** |
| Sales decks / client pitches | **`creal-mono.md`** |
| Brand / marketing showcase | **`creal-mono.md`** |
| Workshop slides with lots of visual examples | `creal.md` |
| Short-form (5-8 slides), high-stakes | **`creal-mono.md`** |
| Long-form (20+), content-heavy | `creal.md` |

Pick `creal-mono.md` when the audience is decision-makers and the room is quiet.
Pick `creal.md` when the audience is learners and the room is engaged.
