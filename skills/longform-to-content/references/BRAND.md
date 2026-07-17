# BRAND — Gate 1: get a DESIGN.md before rendering anything

A DESIGN.md with MEASURABLE tokens must exist before Gate 2. "I'll just pick nice
colors" is forbidden — every visual decision traces to a token in this file.

## Decision flow (mandatory order)

1. **User already has a brand guideline / DESIGN.md** → use it. If values are vague
   ("우리는 파란 느낌"), convert to hex by sampling their real assets (step 2).
2. **User has a website, deck, or logo** → derive: screenshot/open the asset, pixel-sample
   the 2 dominant non-neutral colors (PIL, sample text/accent areas — never gradients),
   identify the closest Google Font for headings/body, extract the wordmark treatment.
   Show the derived tokens to the user for a YES before proceeding.
3. **User has nothing** → run the 3-question interview:
   - "브랜드 이름을 어떻게 표기하나요? (정확한 대소문자/기호)"
   - "메인 컬러 하나만 고르면? (모르면 업종만 알려주세요 — 제가 2안 제시)"
   - "느낌은 어느 쪽? A) 클래식/세리프 B) 모던/산세리프"
   Then fill the template below and get a YES.
4. **User refuses to engage** → apply the Neutral Editorial default AND say so explicitly:
   ink #1C1917 on cream #FAF7F2, one accent #303F9F, Noto Serif (CJK) / Inter (Latin).

## DESIGN.md template (fill every field — no blanks)

```markdown
# DESIGN.md — <Brand> video system
## Tokens
| token | value | usage | limit |
|---|---|---|---|
| canvas | #...... | shorts/thumbnail background | only allowed bg |
| ink | #...... | titles, captions text | |
| accent | #...... | keyword highlights, kicker | ≤ 2 elements per frame |
## Type
- Caption font selection rule: use the BRAND's font if it (a) ships a real Bold weight
  and (b) stays legible at the 22px floor at phone scale. Otherwise defaults:
  KR → Pretendard, pan-CJK → Noto CJK, Latin → Inter (links in SETUP.md §5).
- Caption font file (static bold, for libass): <path>
- Layout font file (VF ok, for PIL): <path>
- Wordmark: exact string "<Brand>" — never recolor, never letterspace
## Fixed geometry (from the pipeline, keep unless brand demands otherwise)
- Full video: PIP 432x243 @ (1460,809) r14; caption style per PIPELINE.md §7
- Shorts 1080x1920: wordmark y96 / title y158 64px / slide card 1040x585@(20,352)
  / captions y1010 / cam 700x394@(190,1360) / footer y1832
## Anti-patterns (binary)
AP-1 gradients AP-2 pure #000/#FFF canvas AP-3 >2 accent elements/frame
AP-4 decorative icons/emoji AP-5 shadows on text
## Copy
- Hook titles ≤ 2 lines x ≤ 10 chars, exactly one accent span, no ending punctuation
- No fabricated numbers — only numbers spoken in the source video
```

## Hard rules

- Minimum readable text: 22px effective at 1080-wide (verify at 0.35x phone scale).
- Accent color is pixel-sampled from real assets, never guessed from memory.
- Wordmark casing/punctuation is sacred (e.g. `Sundayable.` keeps its period).
- The user approves the DESIGN.md ONCE, then it is law for the whole project —
  do not re-litigate per deliverable.
