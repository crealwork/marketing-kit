# Aviator Dental Hygiene Theme — Presentation Slides

Warm, spa-inspired presentation design system for Aviator Dental Hygiene.
Coral accent + warm beige backgrounds create a welcoming, modern wellness feel
suitable for client education, partnerships, team onboarding, and community outreach.

---

## Brand Defaults

### Color Palette

**Primary:**
- Accent (Aviator Coral): `#F18D8D` — logo, CTA buttons, accent text, highlights, chart emphasis
- Accent Light: `#FFF5F5` — subtle highlight boxes, callout backgrounds

**Backgrounds:**
- Default (content slides): `#F7F8F9` (cool off-white) — clean, breathable
- Warm alt: `#f3ebe8` (beige) — use on 1-2 content slides for visual variety
- White: `#FFFFFF` — cards, stat blocks, data containers on beige backgrounds

**Text:**
- Heading: `#222222` — high contrast, bold
- Body: `#333C5E` — dark blue-gray, readable
- Secondary: `#575760` — subheadings, descriptions
- Muted: `#B2B2BE` — captions, labels, slide numbers

**Dark slides (Cover, Section Divider, Ending):**
- Background: `#F18D8D` (Aviator Coral)
- Text: `#FFFFFF`
- Muted text: `rgba(255,255,255,0.7)`

### Font

Host Grotesk — loaded via Google Fonts CDN:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Host+Grotesk:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
```

Apply globally: `font-family: 'Host Grotesk', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;`

### Logo

Aviator wordmark — coral "AVIATOR." with heart replacing the "O". Embed as base64:

```html
<img class="slide-logo" src="data:image/png;base64,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" alt="AVIATOR." />
```

**CSS:**

```css
.slide-logo {
  height: 28px;
  width: auto;
}
/* On coral backgrounds: */
.slide-logo-white {
  height: 28px;
  width: auto;
  filter: brightness(0) invert(1);
}
```

---

## Design Language

- **Mood:** Warm, welcoming, spa-inspired — a modern wellness experience, not clinical
- **Shadows:** Soft and warm (`box-shadow: 0 4px 20px rgba(241,141,141,0.1)`)
- **Decorative elements:**
  - Heart SVG motif as accent on cover and section dividers
  - Thin coral accent lines (3px)
  - Subtle curved/organic divider shapes
  - No harsh geometric patterns
- **Whitespace:** Generous — clean and uncluttered, like a spa
- **Contrast:** Dark text on warm off-white for body; white on coral for feature slides
- **Border radius:** Rounded — `12px` for cards, `8px` for bars, `9999px` for pill buttons
- **Heart SVG:** Use as decorative element on Cover and Section slides:

```html
<svg class="heart-decor" viewBox="0 0 24 24" fill="rgba(255,255,255,0.15)">
  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
</svg>
```

```css
.heart-decor {
  position: absolute;
  width: 320px;
  height: 320px;
  opacity: 0.12;
}
.heart-decor-top-right {
  top: -40px;
  right: -40px;
}
.heart-decor-bottom-left {
  bottom: -40px;
  left: -40px;
}
```

---

## Tone & Language Guide

- **Default language:** English
- **Tone:** Warm, friendly, approachable — professional but not clinical.
  Talk like a trusted neighbor, not a textbook.
- **Writing style:** Short, benefit-driven sentences. Action-oriented CTAs.
  Positive, optimistic framing. Avoid overly medical/clinical language.
- **Slide text:** Concise bullet points, NOT full sentences
- **One key message per slide** — if you have 2-3 ideas, split into separate slides
- **Korean text:** If bilingual content is needed, use `word-break: keep-all` on all text elements

---

## Slide Types

### 1. Cover Slide

Coral background with heart motif. Centered, warm, inviting.

```html
<div class="slide slide-cover" id="slide-1">
  <svg class="heart-decor heart-decor-top-right" viewBox="0 0 24 24" fill="rgba(255,255,255,0.12)">
    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
  </svg>
  <svg class="heart-decor heart-decor-bottom-left" viewBox="0 0 24 24" fill="rgba(255,255,255,0.08)">
    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
  </svg>
  <div class="cover-content">
    <div class="cover-tag">Aviator Dental Hygiene</div>
    <h1 class="cover-title">Presentation Title</h1>
    <div class="cover-rule"></div>
    <p class="cover-subtitle">Subtitle or one-line description</p>
    <div class="cover-meta">
      <span>Presenter Name</span>
      <span>2026.04.14</span>
    </div>
  </div>
  <div class="slide-footer">
    <img class="slide-logo-white" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
</div>
```

```css
.slide-cover {
  background: #F18D8D;
  color: #FFFFFF;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.cover-tag {
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.7);
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
  color: rgba(255,255,255,0.8);
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
- Date should reflect the current date
- The heart SVG motifs add brand identity — do not remove them
- Replace `[LOGO_BASE64]` with the full data URI of the embedded logo

### 2. Agenda Slide

Clean, warm background. Coral numbers set rhythm.

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
    <img class="slide-logo" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
  <div class="slide-number">2 / Total</div>
</div>
```

```css
.slide-agenda { background: #F7F8F9; }
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #222222;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 3px solid #F18D8D;
}
.agenda-list { display: flex; flex-direction: column; gap: 36px; margin-top: 48px; }
.agenda-item { display: flex; align-items: center; gap: 32px; }
.agenda-num {
  font-size: 44px;
  font-weight: 900;
  color: #F18D8D;
  min-width: 80px;
}
.agenda-text {
  font-size: 32px;
  font-weight: 600;
  color: #222222;
  word-break: keep-all;
}
```

**Usage notes:**
- Slide number shown (e.g., `2 / 12`)
- Keep to 3-5 agenda items max
- Each agenda item maps to a Section Divider slide later
- Coral underline on the title is the brand accent

### 3. Section Divider

Coral background with heart motif. Signals a new chapter.

```html
<div class="slide slide-section" id="slide-N">
  <svg class="heart-decor heart-decor-top-right" viewBox="0 0 24 24" fill="rgba(255,255,255,0.1)">
    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
  </svg>
  <div class="section-content">
    <span class="section-num">01</span>
    <h2 class="section-title">Section Title</h2>
    <div class="section-rule"></div>
  </div>
</div>
```

```css
.slide-section {
  background: #F18D8D;
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
- Optional: add a one-line subtitle in `rgba(255,255,255,0.65)`

### 4. Body (Text)

Workhorse slide. Title with coral underline, clean bullet list.

```html
<div class="slide slide-body" id="slide-N">
  <h2 class="slide-title">Slide Title</h2>
  <ul class="body-list">
    <li class="body-item">
      <span class="bullet-heart">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#F18D8D">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
      </span>
      <span class="item-text">Main point — keep it concise and scannable</span>
    </li>
    <li class="body-item">
      <span class="bullet-heart">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#F18D8D">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
      </span>
      <span class="item-text">Second point</span>
    </li>
    <li class="body-item">
      <span class="bullet-heart">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#F18D8D">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
      </span>
      <span class="item-text">Third point</span>
    </li>
  </ul>
  <div class="slide-footer">
    <img class="slide-logo" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-body { background: #F7F8F9; }
.slide-title {
  font-size: 44px;
  font-weight: 800;
  color: #222222;
  padding-bottom: 20px;
  border-bottom: 3px solid #F18D8D;
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
.bullet-heart {
  flex-shrink: 0;
  margin-top: 6px;
}
.item-text {
  font-size: 30px;
  font-weight: 400;
  color: #333C5E;
  line-height: 1.6;
  word-break: keep-all;
}
.slide-number {
  position: absolute;
  bottom: 40px;
  right: 60px;
  font-size: 18px;
  color: #B2B2BE;
  font-family: 'Host Grotesk', sans-serif;
}
.slide-footer {
  position: absolute;
  bottom: 40px;
  left: 60px;
}
```

**Usage notes:**
- Heart SVG bullets instead of dots or dashes — this is the core brand differentiator
- Max 5-6 bullet points per slide. If more, split into two slides
- If only 2-3 bullets, scale up font sizes to fill the space
- Coral underline on the title is always present

### 4b. Body (Text) — Warm Variant

Use beige background on 1-2 content slides for visual variety.

```css
.slide-body-warm { background: #f3ebe8; }
```

Same HTML structure as Body (Text). Switch `slide-body` to `slide-body-warm`.

### 5. Body (Data/Chart)

Data-focused slide with coral-toned charts.

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
    </div>
  </div>
  <p class="chart-source">Source: Report Name, Year</p>
  <div class="slide-footer">
    <img class="slide-logo" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-data { background: #F7F8F9; }
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
  color: #222222;
  min-width: 200px;
  text-align: right;
  word-break: keep-all;
}
.bar-track {
  flex: 1;
  height: 48px;
  background: #f3ebe8;
  border-radius: 8px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #F18D8D, #f5a3a3);
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
  font-size: 18px;
  color: #B2B2BE;
  text-align: right;
  margin-top: 16px;
}
```

**Usage notes:**
- One insight per data slide
- Bar track uses beige `#f3ebe8` instead of gray — warmer feel
- Big number callouts: 72px+, `font-weight: 900`, `color: #F18D8D`
- Always attribute the data source
- For a secondary chart color, use `#575760` (secondary text gray) for contrast

### 6. Quote/Highlight

Centered emphasis slide. Heart icon instead of quote mark.

```html
<div class="slide slide-quote" id="slide-N">
  <div class="quote-content">
    <svg class="quote-heart" width="80" height="80" viewBox="0 0 24 24" fill="#F18D8D">
      <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
    </svg>
    <p class="quote-text">Key quote or statement you want to emphasize</p>
    <p class="quote-author">— Source or Speaker</p>
  </div>
  <div class="slide-footer">
    <img class="slide-logo" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
  <div class="slide-number">N / Total</div>
</div>
```

```css
.slide-quote {
  background: #F7F8F9;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.quote-content { max-width: 1400px; }
.quote-heart {
  display: block;
  margin: 0 auto 24px;
}
.quote-text {
  font-size: 40px;
  font-weight: 700;
  color: #222222;
  line-height: 1.5;
  margin: 32px auto;
  word-break: keep-all;
}
.quote-author {
  font-size: 24px;
  color: #B2B2BE;
  margin-top: 24px;
  font-weight: 500;
}
```

**Usage notes:**
- Uses a heart SVG instead of traditional quote marks — on-brand
- Keep quote text under 2 lines for maximum impact
- Can optionally use beige background (`#f3ebe8`) for variety

### 7. Ending/CTA

Coral background. Thank you + contact + all 3 locations.

```html
<div class="slide slide-ending" id="slide-N">
  <svg class="heart-decor heart-decor-top-right" viewBox="0 0 24 24" fill="rgba(255,255,255,0.1)">
    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
  </svg>
  <div class="ending-content">
    <h2 class="ending-title">Thank You</h2>
    <div class="ending-rule"></div>
    <p class="ending-subtitle">Your Health Starts with Your Smile</p>
    <div class="ending-contact">
      <span>672.855.2875</span>
      <span>aviatordentalhygiene.com</span>
    </div>
    <div class="ending-locations">
      <span>Burnaby</span>
      <span>Vancouver</span>
      <span>Langley</span>
    </div>
  </div>
  <div class="slide-footer">
    <img class="slide-logo-white" src="[LOGO_BASE64]" alt="AVIATOR." />
  </div>
</div>
```

```css
.slide-ending {
  background: #F18D8D;
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
  color: rgba(255,255,255,0.8);
  margin-bottom: 48px;
  font-weight: 400;
  font-style: italic;
  word-break: keep-all;
}
.ending-contact {
  display: flex;
  gap: 48px;
  font-size: 24px;
  color: rgba(255,255,255,0.9);
  font-weight: 600;
  justify-content: center;
  margin-bottom: 24px;
}
.ending-locations {
  display: flex;
  gap: 32px;
  font-size: 20px;
  color: rgba(255,255,255,0.65);
  font-weight: 400;
  justify-content: center;
  text-transform: uppercase;
  letter-spacing: 3px;
}
```

**Usage notes:**
- No slide number on Ending
- Contact info uses Aviator's actual phone and website
- 3 locations listed below contact
- Use italic tagline "Your Health Starts with Your Smile"
- Can swap "Thank You" for "Book Your Visit" for CTA-style endings

---

## Data Visualization Guidelines

### Color usage in charts
- Primary bars/segments: Aviator Coral `#F18D8D`
- Gradient fill: `linear-gradient(90deg, #F18D8D, #f5a3a3)`
- Secondary/contrast: `#575760` (secondary text gray)
- Background/track: Beige `#f3ebe8`
- Emphasis/highlight: Coral at full opacity; use `rgba(241,141,141,0.3)` for de-emphasized

### Chart types and when to use
- **Bar chart:** Comparing quantities (treatment popularity, patient stats)
- **Donut/pie (SVG):** Proportions (`#F18D8D` + `#f3ebe8` as the two-color pair)
- **Progress bar:** Adoption rates, satisfaction scores
- **Big number block:** Single standout stat — 72px+, `font-weight: 900`, `color: #F18D8D`
- **Side-by-side comparison:** Before/after treatments, cost comparisons
- **Timeline/process flow:** Steps in a treatment; coral dots connected by beige lines

### Rules
- Mix at least 2-3 different chart types per presentation
- Each data slide = one key insight
- All numbers must match the approved content from Gate 2
- Always show the source
- Numbers in chart must match text on slide
- Percentages must add up correctly

---

## Brand-Specific Content Notes

### Key Differentiators (always available for slide content)
- Open 7 days a week including evenings
- 3 BC locations (Burnaby, Vancouver, Langley)
- Direct billing — no upfront payment
- All ages welcome
- CDCP Partner Clinic
- Mobile dental services
- Spa-inspired experience
- Bilingual service (English & Korean)

### 11 Signature Treatments
1. Dental Cleaning
2. Interim Stabilization Therapy
3. Dental Sealant
4. Silver Diamine Fluoride (SDF)
5. Oral Cancer Screening
6. Desensitization Treatment
7. Teeth Whitening
8. Tooth Gems
9. Dental Mobile Services
10. Guided Biofilm Therapy
11. Orofacial Myofunctional Therapy

---

## Common Mistakes to Avoid

1. **Too clinical** — this is a wellness brand, not a medical institution. Keep language warm and accessible.
2. **Too much text** — max 5-6 bullet points per slide. Use whitespace generously.
3. **Inconsistent backgrounds** — `#F7F8F9` for most content, `#f3ebe8` for 1-2 warm variety slides, `#F18D8D` for Cover/Section/Ending only.
4. **Coral overuse** — Coral is accent, not everywhere. Use for numbers, underlines, hearts, bar fills, highlights. Not for body text.
5. **Missing slide numbers** — every content slide needs `N / Total` except Cover, Section Divider, Ending.
6. **Missing logo** — every slide needs the logo footer. Coral logo on light bg, white logo on coral bg.
7. **Missing heart motif** — heart SVGs on Cover, Section, and Ending slides are mandatory brand elements. Heart bullets on body slides.
8. **Charts without labels** — every data point needs a readable label and value.
9. **Tiny text** — minimum sizes from SKILL.md apply. This is for projection/sharing — text must be large.
10. **Full sentences** — use concise bullet points. Cut unnecessary words. Benefit-first language.
