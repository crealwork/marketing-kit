---
name: publish-checklist
description: Use when publishing or deploying ANY website, landing page, or web deliverable, or when auditing head tags — favicon set, OG image/tags, per-page titles, meta description, canonical, mobile typography. Triggers: "배포 전 체크해줘", "OG 태그 넣어줘", "파비콘 만들어줘", "메타태그 최적화", "링크 공유하면 카드 안 떠", "publish checklist", "head 최적화", and automatically before any new site ships.
---

# Publish Checklist

**모든 새 사이트/랜딩/딜리버러블 페이지에 자동 적용하는 체크리스트.** 페이지를
"완성"이라고 부르기 전에 이 파일의 템플릿이 채워져 있어야 한다. 기존 사이트를 점검할 때도(seo-setup G0) 같은 기준을 쓴다.

## 1. 복붙 템플릿 (`<head>`)

플레이스홀더만 바꿔서 그대로 쓴다. 모든 URL은 **절대 경로**.

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{Primary Keyword} — {Brand}</title>
<meta name="description" content="{150자 내외, 구체적 베네핏 + 행동 유도}">
<link rel="canonical" href="https://{domain}/{path}">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{Brand}">
<meta property="og:title" content="{공유 카드에 보일 제목 — title과 달라도 됨}">
<meta property="og:description" content="{공유 카드용 한 줄}">
<meta property="og:image" content="https://{domain}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://{domain}/{path}">
<meta property="og:locale" content="ko_KR">  <!-- 영어 사이트는 en_US -->

<!-- Twitter/X -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og:title과 동일}">
<meta name="twitter:description" content="{og:description과 동일}">
<meta name="twitter:image" content="https://{domain}/og.png">

<!-- Favicon 세트 -->
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><!-- 180x180 -->
<link rel="manifest" href="/site.webmanifest"><!-- icon-192.png, icon-512.png -->
<meta name="theme-color" content="{브랜드 배경색 hex}">
```

`<html lang="ko">` (또는 해당 언어) 잊지 말 것.

## 2. 규칙

**Title**
- 페이지마다 고유. 패턴: 내부 페이지 `{키워드} — {Brand}`, 홈은 `{Brand} — {한 줄 가치제안}`.
- 50–60자(영) / ~30자(한) — 넘치면 검색결과에서 잘린다. 네이버는 title 규칙을
  특히 까다롭게 본다 (ENGINES.md §2).

**Description**
- 페이지마다 고유, 150–160자(영) / 70–80자(한). 키워드 나열이 아니라 클릭할
  이유를 쓴다.

**OG 이미지**
- **1200×630 고정**, 페이지당 1장, 온브랜드 (로고+타이틀 텍스트가 안전영역
  중앙 1000×524 안에). 텍스트는 모바일 카드에서도 읽히게 40px+.
- 절대 URL 필수 — 상대 경로는 카카오톡/슬랙 미리보기에서 깨진다.
- 없으면 만들어서라도 넣는다. OG 없는 페이지는 공유되는 순간 죽은 링크처럼 보인다.

**Favicon**
- 최소 세트 4개: `favicon.ico`(32), `icon.svg`(다크모드 대응 가능), 
  `apple-touch-icon.png`(180×180, 여백 포함 불투명 배경), `icon-192/512.png`+manifest.
- 브랜드 심볼이 없으면 워드마크 이니셜로라도 — 기본 지구본/빈 파비콘 금지.

**한국어 페이지 타이포**
- `word-break: keep-all` 을 본문/헤드라인에 적용 — 단어 중간 줄바꿈 방지.
- 모바일 뷰포트에서 헤드라인 오버플로 확인.

## 3. 검증 (배포 후 즉시)

1. 카톡/슬랙에 URL 붙여넣기 → 카드 미리보기(이미지+제목+설명) 확인. 캐시가
   남으면: Facebook Sharing Debugger(developers.facebook.com/tools/debug)로 재수집.
2. 브라우저 탭 + 모바일 홈화면 추가로 favicon 세트 확인.
3. `view-source:`로 og:image가 절대 URL인지, canonical이 최종 도메인인지 확인
   (스테이징 도메인이 박힌 채 배포되는 사고가 흔하다).
4. 페이지 2~3개 랜덤 골라 title/description이 서로 다른지 확인 — 전 페이지
   동일 title은 가장 흔한 실수.
