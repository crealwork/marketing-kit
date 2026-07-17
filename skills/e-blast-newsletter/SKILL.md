---
name: e-blast-newsletter
description: 'Use when sending email via Resend — transactional sends, newsletters/broadcasts to an audience, contact list management, or setting up a sending domain. Free tier covers 3,000 emails/mo. Triggers: "이메일 보내줘", "뉴스레터 발송", "Resend로 보내줘", "무료로 이메일 마케팅", "send a newsletter", "email blast", "구독자한테 보내줘". NOT for cold outreach sequences (use b2b-cold-email — cold mail from your main domain burns its reputation).'
---

# Resend Email

Resend 하나로 트랜잭셔널 메일 + 뉴스레터(브로드캐스트)를 처리한다.
**Free 티어: $0, 월 3,000통, 일 100통, 도메인 1개** — 소규모 뉴스레터는 무료로
충분하다. (검증: resend.com/pricing, 2026-07-16)

## Hard rules

1. **발송은 유저 게이트** — "작성해줘"는 발송 승인이 아니다. 브로드캐스트는
   반드시 초안 상태로 만들어 유저 확인 후 send.
2. **브로드캐스트에는 `{{{RESEND_UNSUBSCRIBE_URL}}}` 필수** — 수신거부 링크 없는
   마케팅 메일은 스팸법 위반(CAN-SPAM/개인정보보호법).
3. **본발송 전 셀프 테스트** — 자기 주소로 1통 보내 렌더링/링크/머지태그 확인.
4. 일 100통 제한(Free) — 100명 넘는 리스트는 일 단위 분할 또는 Pro($20/mo, 5만통)
   업그레이드를 유저에게 안내.
5. 콜드 아웃리치 금지 — Resend는 permission 기반. 콜드메일은 별도 도메인 +
   전용 툴로 (b2b-cold-email).
6. Windows에서 API 호출은 Python urllib + utf-8 (curl+cp1252 이모지 크래시).
7. **제목은 A/B 전제** — 브로드캐스트마다 제목 후보 3개(다른 축: 숫자/질문/
   직설)를 만들어 유저가 고르고, 리스트가 1,000+ 이면 오디언스를 세그먼트로
   나눠 실제 A/B 발송 → 오픈율 승자를 다음 호 기본 축으로. 히어로 이미지가
   있으면 image-gen 스킬로 변형 2–3개.

## Setup (1회)

1. resend.com 가입 → API Keys → env `RESEND_API_KEY` (`re_...`) 저장.
2. **도메인 인증**: Dashboard → Domains → Add (또는 `POST /domains`) → 발급된
   SPF/DKIM DNS 레코드를 도메인 DNS에 추가 → Verify. `from`은 인증된 도메인의
   주소만 가능 (`뉴스레터 <news@yourdomain.com>`).
3. Base `https://api.resend.com`, `Authorization: Bearer $RESEND_API_KEY`.
4. VERIFY: `GET /domains` 에 status "verified".

## A. 트랜잭셔널 (1:1)

```
POST /emails
{ "from": "Acme <hello@yourdomain.com>", "to": ["user@example.com"],
  "subject": "...", "html": "..." }
```

- 대량 개별 발송: `POST /emails/batch` — 한 번에 최대 100개 객체.
- `reply_to`, `cc`, `bcc`, `attachments` 지원.

## B. 뉴스레터 (Audience + Broadcast)

```
# 1) 오디언스 생성 (리스트당 1개)
POST /audiences            { "name": "Newsletter" }

# 2) 구독자 추가
POST /audiences/{id}/contacts
{ "email": "user@example.com", "first_name": "Jane", "unsubscribed": false }

# 3) 브로드캐스트 생성 (초안)
POST /broadcasts
{ "audience_id": "aud_...",
  "from": "News <news@yourdomain.com>",
  "name": "2026-07 뉴스레터",
  "subject": "이번 달 소식",
  "html": "Hi {{{contact.first_name|there}}}, ...
           <a href='{{{RESEND_UNSUBSCRIBE_URL}}}'>수신거부</a>" }

# 4) 유저 승인 후 발송 (즉시 또는 예약)
POST /broadcasts/{id}/send            # 즉시
POST /broadcasts/{id}/send  { "scheduled_at": "2026-07-20T09:00:00+09:00" }
```

- 머지 태그: `{{{contact.first_name|fallback}}}` — 파이프 뒤가 기본값.
- 생성 시 `"send": true` + `"scheduled_at": "in 1 hour"`(자연어 허용)로 한 번에
  예약도 가능 — 단 rule 1 때문에 기본은 초안 → 승인 → send 2단계.
- 수신거부는 Resend가 자동 처리 (`unsubscribed: true`로 마킹, 이후 브로드캐스트
  자동 제외).

## C. 확인 · 운영

- `GET /emails/{id}` — 발송 상태 (delivered/bounced/complained).
- 바운스/컴플레인은 리스트에서 정리 — 가짜 리드 필터링에도 쓴다 (리드 수집 직후
  자동 환영 메일 → hard bounce = 가짜 DB 즉시 삭제).
- 도달률 기본기: SPF/DKIM 인증 완료, from 주소 고정, 제목 낚시 금지,
  텍스트 버전 자동 생성 확인.

## MailerLite 등에서 이사올 때

CSV로 구독자 내보내기 → `unsubscribed` 상태 보존해서 contacts로 임포트 (수신거부자
재구독 처리 절대 금지) → 첫 브로드캐스트는 소규모 세그먼트로 도달률 확인 후 전체.
