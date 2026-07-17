# PAID-ADS — Zernio로 유료 광고 (검증: zernio.com, 2026-07-16)

Zernio Ads API 하나로 **Meta(FB/IG)·Google·TikTok·LinkedIn·Pinterest·X** 7개
플랫폼의 캠페인을 관리한다. 개발자 앱·앱 리뷰·플랫폼별 SDK 없이 Bearer 토큰 하나.
Zernio 발행(포스팅) API를 이미 쓰고 있다면 **같은 계정/키**를 그대로 쓴다.

## 돈 게이트 (MANDATORY — 발행 게이트보다 엄격)

1. **캠페인 단위 명시 승인**: 플랫폼 + 예산(금액/일일·총액) + 기간 + 타깃을 유저에게
   제시하고 명시적 "go"를 받기 전에는 어떤 ads 엔드포인트도 호출 금지.
   "광고 알아봐줘"는 승인 아님; "이 예산으로 돌려줘"가 승인.
2. **타임아웃 ≠ 실패**: 애매한 에러/타임아웃 시 `GET /v1/ads/campaigns`로 목록
   먼저 조회 — 블라인드 재시도 = 중복 캠페인 = 중복 과금.
3. 생성 응답의 상태를 ASSERT — 의도와 다르면(즉시 라이브 등) 즉시 유저에게 보고.
4. 모든 호출은 Python urllib + utf-8 (curl+cp1252 이모지 크래시 — 발행 API에서
   실제 사고). 업데이트는 **PUT** (발행 API에서 PATCH는 405였다 — 동일 서버).
5. 선행 조건: MEASUREMENT.md §6 (GA4↔Ads 연결, 잠재고객, generate_lead 전환,
   랜딩 URL에 UTM) 완료. 측정 없는 지출은 시작하지 않는다.

## Setup

- 키: `ZERNIO_API_KEY` (키 파일에 저장, 문서/채팅에 값 기록 금지).
- Base `https://zernio.com/api/v1`, `Authorization: Bearer $ZERNIO_API_KEY`.
- 광고 계정 연결: Zernio Dashboard → Accounts에서 각 플랫폼의 **광고 계정**
  (Meta는 `act_…` ad account)까지 연결돼 있어야 한다. VERIFY:
  `GET /v1/accounts`에 대상 플랫폼 + adAccount가 보이는지.
- 전체 문서: docs.zernio.com (ads/boost-post, platforms/meta-ads 등).

## A. 오가닉 포스트 부스트 (가장 흔한 경로)

Zernio로 발행/스케줄한 포스트의 postId를 그대로 쓴다.

```
POST /v1/ads/boost
{
  "postId": "POST_ID",            // Zernio 발행 포스트 ID
  "accountId": "ACCOUNT_ID",      // 연결된 소셜 계정
  "adAccountId": "act_123456789", // 광고 계정
  "platform": "facebook",
  "name": "Summer sale boost",
  "goal": "traffic",              // traffic | conversions | ...
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
    "imageUrl": "https://...",        // presign 업로드한 publicUrl 재사용 가능
    "callToAction": "SHOP_NOW",
    "landingPageUrl": "https://...?utm_source=facebook&utm_medium=cpc&utm_campaign=..."
  },
  "targeting": { "age_min": 25, "age_max": 55, "countries": ["US"],
                 "interests": [{ "id": "6003139266461", "name": "DevOps" }] }
}
```

- 피드 이미지: JPEG/PNG ≤30MB, 권장 1080×1080(1:1) 또는 1200×628(1.91:1).
- landingPageUrl에는 **반드시 UTM** (MEASUREMENT.md §5 규칙).

## C. 오디언스

- `POST /v1/ads/audiences` — 커스텀 오디언스 생성 (고객 리스트 / 웹사이트 /
  룩얼라이크).
- `POST /v1/ads/audiences/{id}/users` — 고객 리스트 추가 (SHA-256 해싱 자동).
  CRM의 리드 리스트를 여기로 밀어 리타깃/룩얼라이크 모수로 쓸 수 있다.

## D. 운영 · 분석 루프

- `GET /v1/ads/{id}` — 상태/지출 확인. `PUT /v1/ads/{id}` — 예산·일정·타깃 수정,
  일시정지.
- `GET /v1/ads/{id}/analytics` — spend, impressions, clicks, CTR, CPC, CPM, ROAS
  (연령/성별/국가/기기 브레이크다운). `GET /v1/ads/campaigns` — 전체 캠페인 목록.
- 리포팅: Zernio analytics(플랫폼 지표) + GA4(랜딩 후 전환, UTM 기준)를 함께 봐야
  전체 퍼널이 잡힌다. 캠페인 시작 후 24–48h 내 1차 점검(집행·CTR·CPC), 이후 예산
  조정은 다시 유저 승인.

## 완료 체크

- [ ] MEASUREMENT.md §6 선행 조건 완료 (Ads 연결·잠재고객·전환·UTM)
- [ ] GET /v1/accounts에 플랫폼 + adAccount 확인
- [ ] 유저 승인: 플랫폼/예산/기간/타깃 명시 "go"
- [ ] 생성 응답 상태 ASSERT + 캠페인 ID 기록 (project notes)
- [ ] 24–48h 후 analytics 1차 점검 리포트
