---
name: paid-ads
description: 'Use when running paid ads through Zernio — boosting a published social post, creating a standalone ad campaign, managing audiences, or pulling ad analytics across Meta (FB/IG), Google, TikTok, LinkedIn, Pinterest, X. Triggers: "광고 돌려줘", "이 포스트 부스트해줘", "boost this post", "run ads", "광고 성과 보여줘", "캠페인 일시정지", "광고 예산 바꿔줘". NOT for organic posting/scheduling, and NOT for SEO (use seo-setup).'
---

# Zernio Ads

Zernio Ads API 하나로 **Meta(FB/IG)·Google·TikTok·LinkedIn·Pinterest·X** 7개
플랫폼의 유료 캠페인을 관리한다. 개발자 앱·앱 리뷰·플랫폼별 SDK 없이 Bearer 토큰
하나. Zernio 발행(포스팅) API를 이미 쓰고 있다면 같은 계정/키를 그대로 쓴다.
(검증: zernio.com 공개 문서, 2026-07-16)

## 돈 게이트 (MANDATORY — 이 스킬의 존재 이유)

1. **캠페인 단위 명시 승인**: 플랫폼 + 예산(금액/일일·총액) + 기간 + 타깃을 유저에게
   제시하고 명시적 "go"를 받기 전에는 어떤 ads 엔드포인트도 호출 금지.
   "광고 알아봐줘"는 승인 아님; "이 예산으로 돌려줘"가 승인.
2. **타임아웃 ≠ 실패**: 애매한 에러/타임아웃 시 `GET /v1/ads/campaigns`로 목록
   먼저 조회 — 블라인드 재시도 = 중복 캠페인 = 중복 과금.
3. 생성 응답의 상태를 ASSERT — 의도와 다르면(즉시 라이브 등) 즉시 유저에게 보고.
4. 모든 호출은 Python urllib + utf-8 (Windows에서 curl+cp1252는 이모지 응답에
   크래시). 업데이트는 **PUT** (이 서버에서 PATCH는 405).
5. **측정 선행 조건**: GA4↔Google Ads 연결, 전환 이벤트, 랜딩 URL UTM이 준비돼
   있어야 한다 (analytics-setup 스킬). 측정 없는 지출은 시작하지 않는다.
6. **A/B는 선택이 아니라 기본**: 캠페인당 creative **최소 2개, 권장 3–4개**
   (훅 축 × 비주얼 축을 다르게 — image-gen 스킬로 변형 세트 생성). 단일 소재
   캠페인은 학습 없는 지출이다. 네이밍 `{campaign}_{axis}` 로 성과 추적,
   24–48h 점검에서 진 소재는 PUT으로 일시정지.

## Setup

- 키: env `ZERNIO_API_KEY` (파일/채팅에 값 기록 금지).
- Base `https://zernio.com/api/v1`, `Authorization: Bearer $ZERNIO_API_KEY`.
- 광고 계정 연결: Zernio Dashboard → Accounts에서 각 플랫폼의 **광고 계정**
  (Meta는 `act_…`)까지 연결. VERIFY: `GET /v1/accounts`에 플랫폼 + adAccount 확인.
- 전체 문서: docs.zernio.com (ads/boost-post, platforms/meta-ads 등).

## A. 오가닉 포스트 부스트 (가장 흔한 경로)

Zernio로 발행/스케줄한 포스트의 postId를 그대로 쓴다.

```
POST /v1/ads/boost
{
  "postId": "POST_ID",
  "accountId": "ACCOUNT_ID",
  "adAccountId": "act_123456789",
  "platform": "facebook",
  "name": "Summer sale boost",
  "goal": "traffic",
  "budget": { "amount": 25, "type": "daily" },
  "schedule": { "startDate": "2026-01-15", "endDate": "2026-01-22" },
  "targeting": { "age_min": 25, "age_max": 55, "countries": ["US", "GB"] }
}
```

## B. 독립 캠페인 (creative부터)

```
POST /v1/ads/create
{
  "platform": "metaads",
  "accountId": "acc_metaads_123",
  "adAccountId": "act_1234567890",
  "name": "Spring sale - US Feed",
  "goal": "conversions",
  "budget": { "amount": 75, "type": "daily" },
  "schedule": { "startDate": "...", "endDate": "..." },
  "placements": ["facebook_feeds", "instagram_feeds", "instagram_reels"],
  "creative": {
    "headline": "...", "body": "...",
    "imageUrl": "https://...",
    "callToAction": "SHOP_NOW",
    "landingPageUrl": "https://...?utm_source=facebook&utm_medium=cpc&utm_campaign=..."
  },
  "targeting": { "age_min": 25, "age_max": 55, "countries": ["US"],
                 "interests": [{ "id": "6003139266461", "name": "DevOps" }] }
}
```

- 피드 이미지: JPEG/PNG ≤30MB, 권장 1080×1080(1:1) 또는 1200×628(1.91:1).
- landingPageUrl에는 **반드시 UTM** (소문자+언더바).

## C. 오디언스

- `POST /v1/ads/audiences` — 커스텀 오디언스 (고객 리스트 / 웹사이트 / 룩얼라이크).
- `POST /v1/ads/audiences/{id}/users` — 고객 리스트 추가 (SHA-256 해싱 자동).
  CRM의 리드 리스트를 밀어 리타깃/룩얼라이크 모수로 쓸 수 있다 (crm-connect 스킬).

## D. 운영 · 분석 루프

- `GET /v1/ads/{id}` — 상태/지출. `PUT /v1/ads/{id}` — 예산·일정·타깃 수정, 일시정지.
- `GET /v1/ads/{id}/analytics` — spend, impressions, clicks, CTR, CPC, CPM, ROAS
  (연령/성별/국가/기기 브레이크다운). `GET /v1/ads/campaigns` — 전체 목록.
- 리포팅: Zernio analytics(플랫폼 지표) + GA4(랜딩 후 전환)를 함께 봐야 퍼널이
  잡힌다. 시작 24–48h 내 1차 점검(집행·CTR·CPC); 이후 예산 조정은 다시 유저 승인.

## 완료 체크

- [ ] 측정 선행 조건 완료 (GA4↔Ads·전환·UTM — seo-setup MEASUREMENT)
- [ ] GET /v1/accounts에 플랫폼 + adAccount 확인
- [ ] 유저 승인: 플랫폼/예산/기간/타깃 명시 "go"
- [ ] 생성 응답 상태 ASSERT + 캠페인 ID 기록
- [ ] 24–48h 후 analytics 1차 점검 리포트
