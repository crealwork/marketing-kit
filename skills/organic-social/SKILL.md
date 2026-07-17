---
name: organic-social
description: 'Use when publishing or scheduling ORGANIC social media posts via Zernio — one post to multiple platforms (YouTube, Instagram, TikTok, LinkedIn, Facebook, X, Pinterest, Threads), content calendars, media upload, or automating a posting cadence. Triggers: "이 포스트 올려줘", "스케줄해줘", "인스타랑 유튜브에 같이 올려줘", "포스팅 자동화", "content calendar", "schedule this post", "cross-post". Paid promotion → paid-ads. 발행 승인 없는 자동 게시는 금지.'
---

# Zernio Social

Zernio 발행 API 하나로 여러 플랫폼에 오가닉 포스트를 올리고 예약한다. 콘텐츠
캘린더 자동화의 실행 레이어. (API 사실관계 검증: 2026-07)

## 발행 게이트 (MANDATORY)

**에이전트의 상한선은 "유저 승인 하의 예약"이다.** "만들어줘/써줘"는 발행 승인이
아니다 — "올려줘/스케줄해줘"가 승인이며, **목적지(플랫폼)별로** 받는다.
자동화 루프(캘린더)도 최초 셋업 때 캘린더 전체를 승인받고, 콘텐츠가 바뀌면 다시.

## Setup

- 계정: zernio.com 가입 → Dashboard → Accounts → 각 플랫폼 연결.
  Instagram은 Business/Creator 계정만 API 게시 가능 (개인 계정은 IG 앱에서 전환:
  설정 → 계정 유형 및 도구 → 프로페셔널 계정으로 전환).
- 키: env `ZERNIO_API_KEY`. Base `https://zernio.com/api/v1`,
  `Authorization: Bearer`.
- VERIFY: `GET /v1/profiles` 200 + `GET /v1/accounts`에 대상 플랫폼 accountId.
- Windows: 모든 호출 Python urllib + utf-8 (curl+cp1252는 이모지 응답에 크래시 —
  실제 중복 게시 사고의 원인이었다).

## A. 미디어 업로드 (presign)

```
POST /media/presign   { "filename": "...", "contentType": "video/mp4" }
→ { uploadUrl, publicUrl }
→ PUT 바이트를 uploadUrl로 (긴 영상은 timeout ≥ 1800s)
→ publicUrl을 mediaItems에 사용
```

## B. 포스트 생성 (즉시 / 예약)

```
POST /posts
{ "content": "캡션...",
  "mediaItems": [{ "url": "https://...", "thumbnail": "https://..." }],
  "platforms": ["instagram", "youtube"],
  "scheduledFor": "2026-07-20T09:00:00Z", "timezone": "Asia/Seoul" }
  // 또는 "publishNow": true
```

- 한 포스트로 여러 플랫폼 동시 타깃 — 같은 시각에 함께 나간다.
- 응답 `post.status` ∈ scheduled|published|draft|pending — **기대값을 ASSERT**.
  scheduled를 기대했는데 published면 이미 라이브 — 즉시 유저에게 보고.
- YouTube `platformSpecificData`: `{title(≤100), visibility, madeForKids}`;
  커스텀 썸네일은 `mediaItems[].thumbnail` (<2MB, ≥640px, 일반 영상만 — Shorts는
  불가; ≤3분 세로 영상은 자동으로 Short 분류).
- Instagram: `{contentType: "reels", shareToFeed: true}`; 릴스 9:16, 3–90s,
  ≤300MB, H.264. 릴스 커버는 발행 **전에** 첨부 — 발행 후 API 변경 불가.
- IG는 YouTube보다 1–3분 늦게 게시된다 — 정상이지 실패가 아니다.

## C. 수정 · 즉시 발행 · 확인

- 재예약/수정: `PUT /posts/{id}` (**PATCH는 405**).
- "지금 올려줘": PUT으로 `scheduledFor` = now+2분 (과거 시각은 거부될 수 있음)
  → 30초 간격 GET 폴링 → 전 플랫폼 `published` 확인 → platformPostUrl 보고.
- **타임아웃 ≠ 실패**: 대용량 POST는 클라이언트 타임아웃 후에도 서버에서 성공해
  있을 수 있다. 애매하면 `GET /v1/posts?limit=10`에서 내 콘텐츠를 먼저 찾고,
  진짜 없을 때만 재시도. 블라인드 재시도 = 중복 게시.

## D. 자동화 패턴 (캘린더)

- **캐던스 기본값**: 쇼츠/릴스는 하루 1개, 현지 프라임 타임 고정 시각. 첫 발행은
  대표 콘텐츠(썸네일 주장과 일치하는 것)부터.
- **배치 스케줄**: N개 콘텐츠 → 승인된 캘린더(날짜×플랫폼 표)를 유저에게 확인받고
  → 포스트별 생성 → 생성 후 `GET /posts`로 전체 스케줄 재조회해 표로 보고.
- **리퍼포즈 연계**: 플랫폼 간 변환은 content-repurpose 스킬로 재작성 후 이
  스킬로 발행. 유료 부스트는 paid-ads로.
- 발행 카피 기준: 제목 낚시 금지, 이모지 벽 금지, 해시태그 플랫폼 관행에 맞게
  (셀프체크: humanizer 스킬).

## Zernio가 없다면 (수동 폴백)

YouTube Studio 업로드 + Meta Business Suite 예약으로 안내하고, 제목/설명/캡션/
해시태그는 전부 복붙 가능한 파일로 준비해 준다.
