---
name: kit-onboarding
description: 'Use FIRST after installing the AI + Marketing Kit — sets up the foundation files every other skill reads (DESIGN.md brand tokens, BRAND-VOICE.md, CLAUDE.md basics, API keys). Triggers: "온보딩 시작", "킷 세팅해줘", "마케팅 킷 시작", "set up my marketing kit", "start here", "get started". ALSO use when any kit skill needs brand tokens and finds no DESIGN.md — route here before improvising a brand.'
---

# Kit Onboarding

킷의 다른 스킬들이 전부 읽는 **기초 파일 3개**를 깔고 시작한다: DESIGN.md(브랜드
토큰), BRAND-VOICE.md(말투), CLAUDE.md(에이전트 상시 규칙). 이거 없이 스킬을
돌리면 매번 브랜드를 즉석에서 지어내게 된다 — 온보딩이 그걸 막는다.

**소요: 10–15분.** 이미 파일이 있으면 그 항목은 건너뛰고 검증만.

## G1 — 인터뷰 (한 번에, 질문 도구로)

1. **비즈니스 한 줄**: 무엇을 누구에게 파는가.
2. **사이트/자료**: 라이브 사이트 URL? 로고 파일? (있으면 G2가 추출 모드,
   없으면 인터뷰 모드)
3. **주 언어/시장**: 콘텐츠 언어(한/영/둘 다), 타깃 지역.
4. **지금 쓰는 채널**: 인스타/스레드/링크드인/유튜브/뉴스레터 중 뭘 운영 중인가.
5. **첫 목표**: 다음 30일에 마케팅으로 얻고 싶은 것 하나.

## G2 — DESIGN.md (브랜드 토큰)

`marketing/DESIGN.md` 생성 — **brand-guide 스킬로 위임** (사이트 있으면 추출,
없으면 인터뷰 모드). 최소 스키마:

```markdown
# DESIGN.md — {Brand}
## Colors
primary: #XXXXXX / accent: #XXXXXX / ink: #XXXXXX / background: #XXXXXX
## Typography
heading: {font} {weight} / body: {font} {weight} (+ font source links)
## Logo
files: {paths} · min size · clear space · 금지 사례
## Shape
radius / shadow / photo tone
```

carousel-generator, ppt-slide-generator, print-design, ad-video, thumbnail-maker가
이 파일을 읽는다 — 여기 없는 값은 그 스킬들이 지어내지 못하게 채워둔다.

## G3 — BRAND-VOICE.md (말투)

`marketing/BRAND-VOICE.md` 생성 (brand-guide G4 + 인터뷰):

```markdown
# BRAND-VOICE.md — {Brand}
형용사 3개: {a} · {b} · {c}   (서로 긴장 관계가 있게)
톤: 존댓말/반말 · 이모지 정책 · 문장 길이 경향
Do (실제 예문 3개): "..."
Don't (실제 예문 3개): "..."
금지어/필수어: ...
```

humanizer·content-repurpose·e-blast-newsletter·dans-advice가 카피를 쓸 때 이
파일 기준으로 쓴다. 예문은 유저의 실제 카피에서 — 없으면 유저 승인 문장으로.

## G4 — CLAUDE.md 기초 블록

프로젝트(또는 글로벌) CLAUDE.md에 아래 블록을 **유저에게 보여주고 승인 후**
append (기존 내용 덮어쓰기 금지):

```markdown
## Marketing (AI + Marketing Kit)
- Brand: {한 줄} — tokens: marketing/DESIGN.md · voice: marketing/BRAND-VOICE.md
- 콘텐츠 언어: {언어}. 모든 카피는 발행 전 humanizer 룰 통과.
- 새 웹페이지/랜딩은 배포 전 publish-checklist 자동 적용.
- 돈이 나가는 액션(광고)과 외부 발신(발송·발행)은 반드시 내 승인 후.
- 이미지/영상 생성: 전부 Higgsfield CLI 경유(기본 gpt_image_2), 성과형 비주얼은 A/B 변형 세트.
```

## G5 — 키 체크리스트 + 첫 퀵윈

- G1에서 확인한 채널에 필요한 env 키만 안내 (README 키 표 참조) — 지금 다 채울
  필요 없음, 해당 스킬 첫 사용 때 세팅해도 된다.
- 마무리는 **오늘 할 일 딱 하나** 제안 (dans-advice 톤): 사이트가 있으면
  "publish-checklist 한 번 돌려요", 콘텐츠가 급하면 "캐러셀 하나 뽑아요" —
  유저의 첫 목표(G1-5)에 맞는 가장 작은 실행.

## Hard rules

1. 기존 CLAUDE.md/DESIGN.md를 덮어쓰지 않는다 — append/보완만, diff를 보여주고.
2. 브랜드 값을 지어내지 않는다 — 추출하거나 물어본다 (brand-guide 룰).
3. 온보딩 없이 브랜드가 필요한 스킬이 호출되면, 즉석 브랜드 대신 이 스킬을
   먼저 제안한다.
