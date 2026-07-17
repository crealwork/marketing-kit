---
name: card-news-generator
description: >
  Instagram/Threads card news (카드뉴스) auto-generator with multi-brand template system.
  Creates professional HTML card news with deep research, branded design,
  data visualization, and PNG download. Supports preset brands (CREAL, Red Seal Pro, Sundayable, custom)
  and any topic. Use this skill whenever the user mentions: 카드뉴스, card news, 인스타 카드,
  SNS 정보 카드, 인포그래픽 카드뉴스, slide cards, Instagram carousel, or wants to create
  visual information cards for social media. Also trigger when the user says "카드뉴스 만들어줘",
  "[topic] 카드뉴스", "인스타 카드뉴스 제작", "SNS용 정보 카드 만들어줘", or any variation of
  creating visual card-format content for Instagram or Threads.
---

# Card News Generator (카드뉴스 자동 생성기)

This skill creates professional Instagram/Threads card news (4:5 ratio, 1080x1350px) through a
complete pipeline: brand selection, topic confirmation, deep research, card flow planning,
HTML generation with neumorphism design, and PNG download capability.

The goal is not just pretty cards -- it's a full content pipeline where research quality and
message flow matter more than decoration.

---

## Brand Templates

This generator supports multiple brand presets. If the user doesn't specify a brand,
ask which one to use via AskUserQuestion. If context makes the brand obvious (e.g., the user
mentions a specific brand name or account), use that preset directly.

**The presets below are worked examples** (real brands run with this skill in
production). Treat them as the template for defining YOUR brand's preset: copy one,
swap the account/palette/tone/footer, and add it as a new preset section. If a brand
has its own dedicated card-news skill installed, that skill wins over these presets.

### Preset: CREAL (댄정 @crealwork)

**Account**: @crealwork
**Brand name**: 댄정
**Footer text**: `댄정 @crealwork`
**Content domain**: AI + Marketing (AI 활용법, 마케팅 자동화, 생산성, 트렌드 등)
**Language**: Korean
**CTA button text**: `Follow Dan`

**Tone**: 쉽고 실용적인 정보형 -- 전문 용어를 쓰더라도 한 번은 쉽게 풀어서 설명하고,
독자가 "이거 저장해야지"라고 느낄 수 있게 구체적이고 실행 가능한 내용 위주로 쓴다.
가볍지만 근거 있는 톤. 과장하지 않되, 임팩트는 살린다.

**Color Palette (CREAL B.I. Guideline):**
- Navy (Primary): `#1A2A4F` -- headings, key text, dark backgrounds
- Yellow (Accent): `#FFCC4E` -- highlights, CTAs, emphasis, badges
- Black: `#000000` -- body text on light backgrounds
- White: `#FFFFFF` -- text on dark backgrounds
- Warm Gray: `#A39F94` -- secondary text, dividers, subtle elements
- Coral: `#D77A61` -- charts, secondary accents
- Background: `#F8F5F0` (ivory cream) for light mode, `#1A2A4F` for dark mode

**Default style**: Style A (Light Neumorphism) for general audiences.
**Logo**: CREAL Text logo in footer. White/Yellow on dark, Black/Blue on light.

### Preset: Red Seal Pro

**Account**: @redseal.pro
**Brand name**: RED SEAL PRO
**Footer text**: `RED SEAL PRO @redseal.pro`
**Content domain**: Contractor tips, home improvement, trades, HVAC, plumbing, electrical
**Language**: English
**CTA button text**: `Follow @redseal.pro`

**Tone**: Direct, authoritative, practical. Speaks contractor-to-contractor.
No fluff, real-world advice. Professional but approachable.

**Color Palette:**
- Dark charcoal (Primary): `#1A1A1A` -- backgrounds, headings
- Red (Accent): `#C0392B` -- highlights, CTAs, emphasis
- White: `#FFFFFF` -- text on dark backgrounds
- Light gray: `#F5F5F5` -- secondary backgrounds
- Medium gray: `#888888` -- secondary text

**Default style**: Style B (Dark Neumorphism) for premium/professional feel.

### Preset: Sundayable

*(Synced to the live site sundayable.com on 2026-07-16. If in doubt, the live site and
the brand portal at proof.getsundayable.com/brand win over this file.)*

**Account**: @sundayable
**Brand name**: Sundayable.
**Footer text**: `Sundayable.` (wordmark only, period included, never burgundy)
**Content domain**: Sunday, the AI operator, ships finished work for small business —
pages, ads, reels, cold outreach, CRM ops, weekly workflows. Positioning: "AI + Revenue
Growth Team for Small Business". Key line: "People don't need more software. They need
the work done." Never call Sunday a tool or copilot; it's an operator that ships.
**Language**: English (Korean OK for Korean-market audiences)
**CTA button text**: `Book a Free Demo` (site CTA) or `Follow Dan Jeong at Sundayable` for follow-type cards
**Site**: sundayable.com · Brand kit: proof.getsundayable.com/brand

**Tone**: Editorial-minimal. Magazine typography meets a clean iOS message thread.
Direct, declarative, no jargon. **No em-dashes. No emojis. No exclamation marks.**
Contractions OK. Talks like a person, not a brand.

**Color Palette (warm — never cool grays, never pure-white backgrounds):**
- Paper (Background): `#EFECE6` -- warm cream, main background
- Card: `#FFFFFF` -- cards/panels sitting on paper
- Ink (Primary): `#0A0A0A` -- headings, primary text, wordmark
- Body: `#1F1F1F` -- body text on paper
- Muted: `#5F5A50` -- subtext, descriptions, meta labels
- Subtle: `#98927F` -- disclaimers, fine print
- Divider: `#DDD8CC` -- borders, separators
- Surface: `#E7E3D9` -- card insets, alternating sections
- Burgundy (Accent): `#800020` -- italic emphasis, CTA fills, accent bars (hover `#660019`)
- **No burgundy tints** (rose-soft `#F2DEE3` was killed 2026-07-16): full-strength burgundy or nothing. Sunday's bubbles/status pills sit on Surface `#E7E3D9` with the burgundy S avatar for differentiation

**Typography (override Pretendard with these):**
- Display headings: `Instrument Serif` (400) -- Google Fonts
- Italic emphasis only: `DM Serif Display` (400 italic) -- burgundy color
- Body: `Inter` (300-700) -- Google Fonts
- Wordmark `Sundayable.` is **always Instrument Serif**, ink color, period included

**Italic emphasis pattern** -- ONE per card max (max 2-3 per deck total):
```html
<em style="font-family: 'DM Serif Display'; font-style: italic; color: #800020;">phrase</em>
```

**Hard rules (Sundayable-specific):**
1. **Hard ban: em-dashes, emojis, exclamation marks.** No exceptions.
2. **Hard ban words**: leverage, unlock, seamless, dive into, AI-powered, robust, navigate the complexities, in the realm of.
3. **One italic emphasis per card max.** Don't stack.
4. **Wordmark `Sundayable.`** -- the period is part of the wordmark, never colored separately, never burgundy.
4b. **S mark is minimal-use ONLY** (Dan, 2026-07-16): favicons, point icons, Sunday's chat avatar. Never next to the wordmark, never as a card's brand mark, no lockups. On cards the brand is always the wordmark.
5. **Burgundy is for**: italic emphasis spans, CTA button fills, accent bars only. Nothing else competes.
6. **No gradients. No multi-tone shadows. No stock photos. No illustrations.**
7. **Body never below 16px** (cards: ≥ 24px since cards are mobile-first social).
8. **CTAs are pill-shaped** (`border-radius: 999px`) with burgundy fill, white text.
9. **Footer pattern**: `Sundayable.` wordmark left, `topic-slug · NN / NN` muted right.

**Default style**: Custom editorial (NOT neumorphism). Warm cream paper background, generous whitespace, restrained shadows, ink typography. Minimal divider lines instead of card outlines.

**Phone mockup specs (when used):**
- iMessage user (the owner / viewer): `#007AFF` blue, RIGHT-aligned, `border-bottom-right-radius: 6px`
- iMessage other party (Sunday / coach / etc.): `#E9E9EB` gray, LEFT-aligned, `border-bottom-left-radius: 6px`
- Sunday avatar (when shown): `#800020` burgundy circle with cream "S" (official monogram SVG in the brand kit)

**Operator profile series — fixed closing card (Sundayable IG @sundayable.ai):**

When building IG profile cards on iconic salespeople / operators (Tom Ferry, Joe Girard, future
ones), the last card is ALWAYS this exact CTA, industry-unspecific:

- Hero: `Sales,<br/><em class="emph" ...>decoded</em>.`
- Lead: `Sundayable studies the operators who built modern sales. The math, the scripts, the discipline. Follow for more.`
- CTA button: `Follow @sundayable.ai` linking to `https://instagram.com/sundayable.ai`
- Background: dark ink (`var(--ink)`)
- Italic emphasis color: `#FFB6C1` (lighter pink for contrast on dark)

**Never use industry-specific language** ("real estate sales", "car sales", etc.) in this
closing because the same closing must work across operators from different industries
(Tom Ferry = real estate, Joe Girard = cars, etc.). One-off campaigns (skill launches,
product announcements) can have custom closings.

### Custom Brand

When the user specifies a brand not in the presets, collect:
1. **Brand name** and **account handle**
2. **Footer text**
3. **Color palette** (at minimum: primary, accent, background)
4. **Tone description** (1-2 sentences)
5. **Content domain/topic focus**
6. **Language** (Korean, English, etc.)
7. **CTA button text**
8. **Logo** (optional -- file path or "none")

Use provided values and fill reasonable defaults for anything not specified.

---

## Step 0: Brand & Topic Confirmation

Determine the brand and topic. If the user's message makes both clear, confirm and proceed.
Otherwise ask via AskUserQuestion:

1. **Brand** -- Which brand template? (CREAL / Red Seal Pro / custom)
2. **Topic** -- What specific subject?
3. **Purpose** -- What's the main goal? (저장/공유 유도 / 팔로워 증가 / 교육 / 브랜드 신뢰)

Optionally check:
4. **Card count preference** -- 짧게 5-7장 / 일반 8-12장 / 깊이 있게 13-19장
5. **Must-include or must-avoid** -- 특정 서비스, 통계, 금지 표현 등

Don't over-interview. Once brand + topic are clear, move to research quickly.

---

## Step 1: Deep Research

Once you have the user's input, do thorough web research. This is the most important step --
the quality of your research directly determines whether the card news is worth saving or just
looks nice but says nothing.

### What to search for (5-10 searches)

- Key statistics and recent numbers
- Latest trends and market changes
- Comparable data points for before/after or vs. comparisons
- Visualizable data (percentages, growth rates, rankings)
- Real examples or quotable insights
- Source-backed facts (not vague claims)

### For general/beginner audiences, also find

- **Empathy hooks**: why people struggle, common misconceptions, relatable frustrations
- **Shock points**: surprising stats that flip assumptions
- **Success stories**: ordinary people who got results (non-experts, side-hustlers, beginners)
- **Low barrier evidence**: free tools exist, low cost, quick first results

### Organize your research

After researching, compile:

```
Topic summary (1 line)
Key data points (5-8)
Chart-ready data (numbers that can become visuals)
Memorable example or quote
Reader empathy points (3)
Shock stat (1-2)
Key takeaways (3)
```

### Show the draft plan before designing

Present to the user:
- Proposed card flow (which cards cover what)
- Key messages per card
- Main data points you'll use
- Expected card count

Wait for approval before proceeding to design. This prevents expensive rework.

---

## Step 1.5: Hooking Strategy

The first 1-2 cards decide whether anyone reads the rest. Design them strategically.

### Reader persona (quick sketch)

Think about:
- What's their situation/job?
- What problem are they dealing with?
- What scares them most about this topic?
- What result do they want?

### Cover card (Card 1) must do three things simultaneously

1. **Stop the scroll** -- a bold statement or surprising number
2. **Communicate the topic instantly** -- no ambiguity
3. **Hint at value** -- why should I keep reading?

### Card 2 answers "Why should I care?"

- Name the reader's problem clearly
- Show what they'll gain from reading
- Build trust (data-backed, not hype)

### Hooking styles to choose from

- **Info-shock**: lead with a surprising number or counterintuitive fact
- **Empathy**: lead with the reader's frustration or situation
- **Success story**: lead with a relatable person's result

---

## Step 2: Design System

Choose one of two base styles based on the brand mood and topic:

### Style A: Light Neumorphism

Best for: bright/friendly brands, beginner audiences, readability-first, Instagram-native feel.
Features: light background, soft shadows for depth, high readability, approachable feel.

### Style B: Dark Neumorphism

Best for: tech/IT feel, premium brands, immersive experience, high-contrast data display.
Features: dark background, sophisticated atmosphere, numbers and highlights pop harder.

### Bento Grid Layout

Inside each card, use a bento grid approach -- information blocks of varying sizes arranged
together so cards feel dynamic, not like a boring slide deck.

The key balance: cards should share the same design language but vary enough in internal
layout that scrolling through them feels engaging, not repetitive.

---

## Step 3: Card Flow Design

Card count is flexible (5-19 cards) based on how much good content you have from research.

### Recommended flow

1. **Hook cover** -- stop the scroll
2. **Problem/empathy** -- why this matters to you
3. **Shock data** -- key evidence
4. **Background** -- context that makes the data meaningful
5. **Solution/method** -- what to actually do
6. **Real example** -- proof it works
7. **Common mistakes** -- what to avoid
8. **Key tips** -- actionable advice
9. **Summary** -- core takeaways in one card
10. **CTA** -- follow, save, share, comment

### CTA card (last card) design rules

The CTA card is the final card that encourages follow/save/share. Follow these rules strictly:

1. **Follow button text**: Use the brand's CTA button text from the Brand Templates section
2. **Center alignment**: The follow button and all CTA content must be **centered** horizontally
3. **Visibility**: Section headers must have strong contrast against the background.
   Never use a light/faded color that blends into the background.
4. **Button style**: Brand accent color background with contrasting text, rounded corners,
   centered in the card. Make it visually prominent.
5. **Layout**: Center all elements vertically and horizontally. Don't left-align the button
   while centering other text -- everything should be consistently centered.

For shorter card news, compress the middle. For longer ones, expand with more data/examples.

### One message per card

Each card should communicate exactly one key point. If you catch yourself putting 2-3 ideas on
one card, split them. Cards are meant to be swiped through quickly.

---

## Step 4: Data Visualization

For stable PNG rendering, do NOT use external chart libraries like Chart.js or canvas-based tools.
They break during PNG capture.

### Allowed methods

- Inline SVG
- HTML/CSS div-based charts (width percentages, flexbox bars, etc.)

### Recommended chart types (mix at least 3 different types)

- Donut charts (SVG)
- Bar charts (CSS divs)
- Comparison bars (side-by-side CSS)
- Progress bars
- Ratio cards (big number + label)
- Number counter blocks

### Visualization checklist

- Numbers in the chart match the text
- Percentages add up correctly
- Sources are mentioned naturally in context when needed
- No card has too many charts crammed together

---

## Step 5: HTML Generation

Generate a single HTML file containing all cards. This is the core deliverable.

### Critical rules for Cowork compatibility

These rules ensure the card news displays correctly in Claude's preview AND exports cleanly as PNG:

**Rule 1: Static HTML only for cards.**
Every `<div class="card">` must exist directly in the `<body>`. Never generate cards with JavaScript.
JS-generated cards won't show in Cowork preview.

**Rule 2: JavaScript is only for the download button.**
No JS for card rendering. Only for PNG capture and ZIP download.

**Rule 3: Use Pretendard font via CDN.**

Pretendard is the designated brand font. Load it via CDN `<link>` tag in the HTML `<head>`:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
```

Then set the font stack and Korean text rules:

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

`word-break: keep-all` is essential for Korean. Without it, the browser breaks lines in the
middle of words (character by character), which looks broken. `keep-all` forces line breaks
only at spaces, keeping Korean phrases intact.

This CSS-only `<link>` tag works in Cowork preview (unlike JS-based font loading).
For PNG capture, inline the font in the download JS to ensure it embeds in the PNG output.

**Rule 4: Deliver the HTML file directly.**
No separate viewer files. One self-contained HTML file in the client's project folder.

**Rule 5: Inline ALL images as base64 data URIs.**

Never reference external images via relative path or absolute URL — they break during
`dom-to-image-more` PNG capture due to file:// CORS restrictions and resource loading races.

**Always do this:**
1. Resize source image first (e.g., 640x640 JPEG @88% quality via PIL/Pillow)
2. Base64-encode the result
3. Embed as `<img src="data:image/jpeg;base64,...">` directly in the HTML

```bash
# Quick base64 inline pattern
python3 -c "
from PIL import Image
import base64
img = Image.open('source.png').convert('RGB')
img.thumbnail((640, 640))
img.save('out.jpg', 'JPEG', quality=88, optimize=True)
data = base64.b64encode(open('out.jpg','rb').read()).decode()
print(f'data:image/jpeg;base64,{data}')
"
```

A 640x640 JPEG @88% typically produces a ~50KB PNG → ~65KB base64 string. Negligible HTML
bloat, total reliability for PNG capture and offline viewing.

### Card dimensions

Each card: `width: 1080px; height: 1350px` (4:5 ratio for Instagram/Threads).

### CRITICAL: Card layout and spacing

Content must fill the full 1080x1350 canvas. Do NOT let text cluster in one corner
with the rest of the card empty. This is the #1 visual quality issue.

**Card container CSS:**
```css
.card {
  width: 1080px;
  height: 1350px;
  padding: 80px 72px;
  display: flex;
  flex-direction: column;
  justify-content: center;   /* vertically center content */
  box-sizing: border-box;
}
```

**Font size minimums (카드뉴스는 모바일에서 보는 콘텐츠이므로 글씨가 커야 함):**
- Card title / heading: `42px` ~ `56px`, font-weight 800
- Subheading: `32px` ~ `38px`, font-weight 700
- Body text / descriptions: `26px` ~ `30px`, font-weight 400-500
- Number callouts (statistics): `64px` ~ `96px`, font-weight 900
- Footer: `20px` ~ `22px`
- List item text: `26px` ~ `30px`

These are MINIMUM sizes. If the card has less content, scale UP the font sizes
to fill the space rather than leaving empty areas.

**Spacing rules:**
- Use generous `gap` or `margin` between content blocks (at least `32px`)
- Numbered lists should have `48px+` spacing between items
- Stat blocks (e.g., "59% - 더 많은 문서") should be large and spread out,
  not compressed into a small area
- If a card has only 3-4 bullet points, increase line-height to `1.8`+
  and font-size to fill the vertical space

### CRITICAL: Use `safe center` for vertical centering

`justify-content: center` on a flex column lets content overflow **upward** when it's
taller than the container. Result: hero text bleeds OVER the eyebrow label at the top
of the card. Use the CSS `safe` keyword to fall back to start when content overflows:

```css
.center-y { display: flex; flex-direction: column; justify-content: safe center; }
```

`safe center` centers when content fits, falls back to `flex-start` when it would cause
overflow. Browser support: Chrome 93+, Firefox 71+, Safari 16+. Use it as the default.

### CRITICAL: The `align-items: center` flex pitfall

**The bug:** When you set `align-items: center` on a flex column container, child block
elements (like `<h1>`) get sized to their `max-content` width — but the browser computes
that based on the LONGEST WORD, not the longest line. A headline like:

```html
<h1>Steal it.<br/><em>Free.</em></h1>
```

inside an `align-items: center` flex parent gets sized to ~330px (width of "Free." italic),
which then forces "Steal it." to wrap awkwardly into "Steal" / "it." even though the parent
container is 904px wide. This wastes hours of debugging if you don't know the cause.

**The fix:** Don't use `align-items: center` for centering wide hero content. Instead:

```html
<!-- ❌ Causes word-level wrapping bug -->
<div style="display: flex; flex-direction: column; align-items: center;">
  <h1 style="text-align: center;">Steal it.<br/>Free.</h1>
</div>

<!-- ✅ Use width: 100% on h1 + text-align: center for safe centering -->
<div style="display: flex; flex-direction: column; text-align: center;">
  <h1 style="text-align: center; width: 100%;">Steal it.<br/>Free.</h1>
  <p style="margin: 64px auto 0; max-width: 760px;">...lead text...</p>
</div>
```

For child elements that need horizontal centering, use `margin: 0 auto` with an explicit
`max-width` instead of relying on `align-items: center`.

### CRITICAL: Hero/lead vertical overlap

Serif display fonts (Instrument Serif, DM Serif Display) at large sizes have descenders
that extend BELOW the CSS line box when `line-height` is set tight (< 1.05). Combined with
a small `margin-top` on the next element, this causes the lead paragraph to visually
overlap the bottom of the hero.

**Mandatory minimums:**
- Hero `line-height: 1.05` minimum (1.08-1.12 for serif)
- Lead `margin-top: 56px` minimum after a multi-line hero (64-80px for safety)
- Use flex `gap: 56px` on the parent instead of per-child margins for predictability

### CRITICAL: Footer wordmark and meta wrapping

Inside a flex `.foot` with `justify-content: space-between`, both the wordmark and meta
text can shrink and wrap when the container has any layout pressure. A wordmark like
"Sundayable." breaking to "Sundaya / ble." is a classic visual disaster.

**Always apply** to wordmark + foot-meta + section eyebrow elements:

```css
.wordmark, .foot-meta, .meta {
  white-space: nowrap;
  flex-shrink: 0;
}
```

### CRITICAL: Italic emphasis text width

Italic display fonts (DM Serif Display Italic, etc.) are typically 10-15% wider than
their upright counterparts. A phrase like "whole skill" in italic at 132px can grow to
~880px and barely fit (or overflow) a 904px container.

**Mandatory rule: italic emphasis MUST stay on a single line.** When italic emphasis
wraps mid-phrase ("who ever / lived"), it loses brand voice impact. Apply globally:

```css
em.emph {
  font-family: var(--font-display);
  font-style: italic;
  color: var(--burgundy);
  font-weight: 400;
  white-space: nowrap;  /* mandatory */
}
```

The autofit script will shrink the hero font as needed to make the nowrap-italic fit.
This trades font size (which still reads big) for visual integrity (the italic stays
together as one phrase). Always preferable to a broken italic.

Additional guidelines:
1. Plan italic emphasis on SHORT phrases (1-3 words). "Law of 250" works. "who ever
   lived" works (3 words). Whole clauses don't.
2. If a long italic phrase forces hero below ~80px, rewrite the headline shorter.

### CRITICAL: iMessage chat mockup conventions

When showing a conversation in a card (e.g., "Live example"), the user/viewer is the
character the audience identifies with. Follow iOS convention strictly:

- **User / viewer / customer**: RIGHT side, blue iMessage bubble (`#007AFF`),
  `border-bottom-right-radius: 6px`
- **Other party** (coach, AI, support, brand): LEFT side, gray (`#E9E9EB`) or dark bubble,
  `border-bottom-left-radius: 6px`

Inverting this confuses the reader — they expect to see "themselves" on the right.

**Anti-pattern (DO NOT):**
- Small text clustered in top-left with 60%+ of card empty
- Body text under 24px
- Stat numbers under 48px
- List items squeezed together with minimal spacing

### Color palette

Use the selected brand's color palette (see Brand Templates section).
Apply the brand's primary color for headings/dark backgrounds, accent for highlights/CTAs,
and background color for card backgrounds. Do NOT use pure white (#FFFFFF) as card background
unless the brand explicitly specifies it -- a warm off-white gives a softer, more premium feel.

### Footer

Every card gets a `.card-footer` with the selected brand's footer text. Same text on every card,
no variations, no omissions.

### Year references

Always use the current year. Never hardcode a specific year -- check the current date and use that.

---

## Step 6: Download Button

Add a download section at the bottom of the HTML (after all cards, before `</body>`).

### What it does

1. Renders each card as individual PNG (1080x1350)
2. Bundles them into a ZIP file
3. Downloads with one click

### Libraries to use (EXACT CDN URLs -- copy these exactly)

Use these EXACT script tags. Do NOT change the version numbers. These have been verified to work.

```html
<script src="https://cdn.jsdelivr.net/npm/dom-to-image-more@3.1.6/dist/dom-to-image-more.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/file-saver@2.0.5/dist/FileSaver.min.js"></script>
```

CRITICAL version notes:
- dom-to-image-more: Use `@3.1.6` ONLY. Other versions (e.g., 4.x) do NOT exist on jsdelivr and will 404.
- The global variable is `domtoimage` (all lowercase). NOT `domToImageMore`.
- Why not html2canvas: it breaks neumorphism shadows and SVG rendering.

### File naming

- Individual: `{topic}-cardnews-01.png`, `{topic}-cardnews-02.png`, ...
- ZIP: `{topic}-cardnews.zip`

### Font handling for PNG capture

Do NOT try to inline fonts via fetch(). The HTML is opened from file:// protocol where
fetch() is blocked by CORS. The Pretendard font is already loaded and rendered in the browser
via the CSS `<link>` tag -- dom-to-image-more will capture the rendered text as-is.

Simply skip font inlining entirely. No `inlineFontsForCapture()` function needed.

### Download button: complete JS reference

Copy this pattern EXACTLY. Do not modify the library calls or add font inlining.

The key technique: before capturing each card, temporarily set it to `position: fixed`
at top-left with explicit 1080x1350 dimensions. This ensures the card renders at FULL SIZE
regardless of the browser viewport width.

**MANDATORY: include the autofit safety net.** Long copy or inline images can overflow
the 1350px box, pushing footer content off the card. The autofit script defines
`window.autofitCard(card)` and the download loop calls it AT 1080x1350 right before each
PNG capture. This eliminates the timing race where users click download before page-load
autofit finishes, AND guarantees fit at the exact capture dimensions.

**Add this `<style>` + `<script>` pair before `</head>`:**

```html
<style>
  .card .grow { min-height: 0; }
  .card { overflow: hidden; }
  .cover-figure img { width: 280px !important; height: 280px !important; }
  .editorial-img { max-height: 420px; }
</style>
<script>
(function () {
  const CARD_H = 1350;
  const HERO_MIN = 48, LEAD_MIN = 18, IMG_MIN = 200, COVER_MIN = 180;
  const STEP_FONT = 0.96, STEP_IMG = 0.92, MAX_PASSES = 50;

  function shrinkFont(el, minSize, step) {
    if (!el) return false;
    let size = parseFloat(getComputedStyle(el).fontSize);
    if (size <= minSize) return false;
    el.style.fontSize = Math.max(minSize, size * step) + 'px';
    return true;
  }
  function shrinkImgHeight(el, minH, step) {
    if (!el) return false;
    let h = el.offsetHeight;
    if (h <= minH) return false;
    h = Math.max(minH, h * step);
    el.style.height = h + 'px'; el.style.maxHeight = h + 'px';
    return true;
  }
  function shrinkCoverImg(el, minDim, step) {
    if (!el) return false;
    let w = el.offsetWidth;
    if (w <= minDim) return false;
    w = Math.max(minDim, w * step);
    el.style.width = w + 'px'; el.style.height = w + 'px';
    return true;
  }
  async function waitForReady(card) {
    if (document.fonts && document.fonts.ready) {
      try { await document.fonts.ready; } catch (e) {}
    }
    const imgs = Array.from(card.querySelectorAll('img'));
    await Promise.all(imgs.map(img => img.complete ? Promise.resolve()
      : new Promise(r => { img.onload = img.onerror = r; })));
    await new Promise(r => requestAnimationFrame(r));
    await new Promise(r => requestAnimationFrame(r));
  }
  window.autofitCard = async function (card) {
    await waitForReady(card);
    let pass = 0;
    while (card.scrollHeight > CARD_H && pass < MAX_PASSES) {
      let didShrink = false;
      const editorialImg = card.querySelector('.editorial-img');
      if (editorialImg && shrinkImgHeight(editorialImg, IMG_MIN, STEP_IMG)) didShrink = true;
      if (card.scrollHeight <= CARD_H) break;
      const coverImg = card.querySelector('.cover-figure img');
      if (coverImg && shrinkCoverImg(coverImg, COVER_MIN, STEP_IMG)) didShrink = true;
      if (card.scrollHeight <= CARD_H) break;
      if (shrinkFont(card.querySelector('.lead'), LEAD_MIN, STEP_FONT)) didShrink = true;
      if (card.scrollHeight <= CARD_H) break;
      if (shrinkFont(card.querySelector('.hero'), HERO_MIN, STEP_FONT)) didShrink = true;
      if (!didShrink) break;
      pass++;
    }
  };
  window.addEventListener('load', async () => {
    for (const card of document.querySelectorAll('.card')) {
      try { await window.autofitCard(card); } catch (e) { console.warn(e); }
    }
  });
})();
</script>
```

**Then the download handler MUST call autofitCard per card at the capture size:**

```js
document.getElementById('downloadBtn').addEventListener('click', async function() {
  const btn = this;
  const status = document.getElementById('downloadStatus');
  btn.disabled = true;
  status.textContent = '준비 중...';

  try {
    const cards = document.querySelectorAll('.card');
    const zip = new JSZip();

    for (let i = 0; i < cards.length; i++) {
      status.textContent = `카드 처리 중: ${i + 1}/${cards.length}`;
      const card = cards[i];

      // Save original inline style
      const originalStyle = card.getAttribute('style') || '';

      // Force full-size rendering (prevents viewport clipping)
      card.style.position = 'fixed';
      card.style.left = '0';
      card.style.top = '0';
      card.style.width = '1080px';
      card.style.height = '1350px';
      card.style.zIndex = '99999';
      card.style.overflow = 'hidden';
      card.style.margin = '0';

      // Wait for browser reflow at the new size
      await new Promise(r => setTimeout(r, 200));
      // CRITICAL: re-run autofit at exact 1080x1350 before capture
      if (window.autofitCard) await window.autofitCard(card);
      await new Promise(r => setTimeout(r, 100));

      try {
        const png = await domtoimage.toPng(card, {
          width: 1080,
          height: 1350
        });
        zip.file(`cardnews-${String(i+1).padStart(2,'0')}.png`, png.split(',')[1], {base64: true});
      } catch (cardErr) {
        console.warn(`Card ${i+1} failed, retrying...`, cardErr);
        await new Promise(r => setTimeout(r, 500));
        const png = await domtoimage.toPng(card, { width: 1080, height: 1350 });
        zip.file(`cardnews-${String(i+1).padStart(2,'0')}.png`, png.split(',')[1], {base64: true});
      }

      // Restore original style
      if (originalStyle) {
        card.setAttribute('style', originalStyle);
      } else {
        card.removeAttribute('style');
      }
    }

    status.textContent = 'ZIP 생성 중...';
    const blob = await zip.generateAsync({type: 'blob'});
    saveAs(blob, 'cardnews.zip');
    status.textContent = '✓ Download complete!';
    status.style.color = 'var(--color-primary, #1A2A4F)';
  } catch (error) {
    console.error('Download failed:', error);
    status.textContent = 'Error: ' + error.message;
    status.style.color = 'var(--color-accent, #D77A61)';
  } finally {
    btn.disabled = false;
  }
});
```

---

## Step 7: Quality Check

Before delivering, verify:

### Content

- Is everything based on current data?
- Are numbers, ratios, and comparisons accurate?
- Are the first 2 cards strong enough to stop a scroll?
- Does the card flow feel natural?
- Does the CTA match the original purpose?

### Design

- Is the visual tone consistent across cards?
- Is text density comfortable (not wall-of-text)?
- Are accent colors used sparingly, not overwhelming?
- Are charts easy to read at a glance?
- Will anything get cut off on mobile?

### Technical

- Does the HTML render without errors?
- Does the download button work?
- Does ZIP generation complete?
- Are there zero external image dependencies?
- Is every card exactly 1080x1350?

---

## Plain Language Guide

When writing for general/beginner audiences, simplify jargon:

- "Funnel optimization" -> "Making sure people don't drop off halfway through"
- "Workflow automation" -> "Setting up tasks to run automatically"
- "Onboarding" -> "The process of getting started smoothly"

For expert-level topics: define the term once in simple language, then use the short version after.

---

## Common Mistakes to Avoid

### Content
1. **Skipping research** -- pretty cards with shallow content don't get saved
2. **Multiple messages per card** -- one card = one point
3. **Weak cover card** -- it needs to stop thumbs, not just look nice
4. **Repetitive chart types** -- mix at least 3 different visualization styles
5. **Too much text** -- card news is scanned, not read like a document
6. **No brand presence** -- every card needs the footer; otherwise it looks generic

### Layout & technical
7. **Using `align-items: center` on the hero parent** -- causes word-level wrap bug.
   Use `text-align: center` + `width: 100%` on the h1 instead.
8. **Tight `line-height` on serif heroes (< 1.05)** -- descenders bleed into the next
   element. Minimum 1.05, prefer 1.08-1.12.
9. **Skinny `margin-top` between hero and lead (< 56px)** -- visual overlap on serif
   fonts. Use 64-80px or use flex `gap` on the parent.
10. **Letting wordmark/eyebrow/foot-meta wrap** -- always `white-space: nowrap` +
    `flex-shrink: 0`.
11. **External image references (relative path or URL)** -- breaks PNG capture.
    Always inline images as base64 data URIs (resize to ~640px first).
12. **Italic emphasis on long phrases without `nowrap`** -- DM Serif Display Italic
    is 10-15% wider than upright. Add `white-space: nowrap` and reduce hero font 5-10%.
13. **iMessage chat with user on the LEFT** -- inverts iOS convention. The viewer
    expects to see "themselves" on the right (blue), other party on the left (gray).
14. **Inline `style="margin-top: 32px"` after a multi-line hero** -- not enough.
    Use 56-80px or convert to flex `gap` on parent.

---

## Self-review before delivery (mandatory)

Run `python render_cards.py cards.html _review/` (script below) and Read 2-3 of the
rendered PNGs yourself before showing the user anything. Check: line breaks and orphans,
wordmark/foot-meta wrapping, italic emphasis staying on one line, chart legibility,
footer present on every card, mobile legibility (body ≥24px at 1080 source). Fix,
re-render, then deliver.

## Delivery

Save the final HTML into the client's project folder (never WARP root), then auto-open
the file (`start "" <file>`) and its folder in Explorer.
The user can open it in a browser, preview all cards, and click the download button to get PNGs.

### Recommended (Windows): Local Python renderer — bypasses MOTW entirely

**The browser download path always triggers Windows MOTW.** PNGs from a browser-downloaded
ZIP get tagged with Zone.Identifier and Windows blocks them on extraction. The PERMANENT
fix is to skip the browser download entirely: render PNGs locally via Playwright + Chromium.
Files written by Python have no MOTW because they never enter the internet zone.

**Always offer this script alongside the HTML deck.** Save as `render_cards.py` next to
the HTML file:

```python
#!/usr/bin/env python
"""Local PNG renderer. Bypasses browser/MOTW. Usage:
    python render_cards.py cards.html out/
"""
import sys, os, pathlib
from playwright.sync_api import sync_playwright

def render(html_path, out_dir, width=1080, height=1350):
    html_path = os.path.abspath(html_path)
    os.makedirs(out_dir, exist_ok=True)
    file_url = pathlib.Path(html_path).as_uri()
    base = os.path.splitext(os.path.basename(html_path))[0]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": width + 80, "height": height + 100},
            device_scale_factor=2,  # retina 2x for IG sharpness
        )
        page = ctx.new_page()
        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(1500)

        cards = page.locator(".card")
        count = cards.count()
        for i in range(count):
            page.evaluate(
                """async (idx) => {
                    const card = document.querySelectorAll('.card')[idx];
                    card.style.position='fixed'; card.style.left='0'; card.style.top='0';
                    card.style.width='1080px'; card.style.height='1350px';
                    card.style.zIndex='99999'; card.style.overflow='hidden'; card.style.margin='0';
                    await new Promise(r => setTimeout(r, 250));
                    if (window.autofitCard) await window.autofitCard(card);
                    await new Promise(r => setTimeout(r, 100));
                }""",
                i,
            )
            out_path = os.path.join(out_dir, f"{base}-{i+1:02d}.png")
            cards.nth(i).screenshot(path=out_path)
            print(f"  -> {out_path}")
            page.evaluate(
                "(idx) => document.querySelectorAll('.card')[idx].removeAttribute('style')",
                i,
            )
        browser.close()

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
```

**One-time Windows setup (~3 min):**
```powershell
pip install playwright
python -m playwright install chromium
```

**Then for any card deck:**
```powershell
python render_cards.py cards.html out/
```

PNGs land directly in `out/` with zero MOTW friction. Reads the same `window.autofitCard()`
the browser uses, so output matches preview exactly. Ships at retina 2x (2160x2700 actual
pixel) which IG/LinkedIn accept and downscale crisply.

The browser download button stays as a fallback for non-Windows users or quick previews.

### Fallback: Windows browser download (Mark of the Web cleanup)

When the user downloads the ZIP via the browser button, Windows tags the ZIP with
"Zone.Identifier" (Mark of the Web). On extraction, every PNG inherits the mark and
Windows blocks them with `Windows found that this file is potentially harmful.`

**Tell the Windows user to do this BEFORE extracting:**

```powershell
# Unblock the ZIP, then extract — extracted files inherit no MOTW
$zip = "$HOME\Downloads\cardnews.zip"
Unblock-File $zip
Expand-Archive $zip -DestinationPath "$HOME\Downloads\cardnews" -Force
```

**Or after extracting (if already unzipped with the warning):**

```powershell
Get-ChildItem -Path "$HOME\Downloads\cardnews" -Recurse | Unblock-File
```

The PNGs themselves are safe — Windows is just being cautious about files from the
internet zone. Either command above clears the mark in one shot.
