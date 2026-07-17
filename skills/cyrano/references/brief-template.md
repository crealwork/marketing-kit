# 브리핑 템플릿

모바일 Slack/Telegram에서 스크롤 없이 읽히는 게 목표. 짧게, 스캔 가능하게.

## 포맷

```
🗓️ {시작시각} — {미팅제목} · {이름} ({회사})

👤 {이름} · {직책} @ {회사} · {근속}
   {한 줄 배경} · {LinkedIn 등 링크}

🏢 {회사} — {한 문장 정의}, {단계/펀딩}, {규모}, {위치}

📈 Signals
   • {시그널 1}
   • {시그널 2}
   • {시그널 3}

🎯 Angles
   • {앵글/연결고리 1}
   • {앵글/연결고리 2}
   • 질문: {열린 질문}

🔗 {소스1} · {소스2} · {소스3}
   Confidence: 사람 {High/Med/Low} · 회사 {…} · 시그널 {…}
```

## 예시 (채워진 것)

```
🗓️ 10:00 — Intro call · Jane Doe (Acme Health)

👤 Jane Doe · VP Growth @ Acme Health · ~2yr
   ex-Shopify 그로스, UBC · linkedin.com/in/janedoe

🏢 Acme Health — 치과 클리닉용 예약+청구 SaaS, Series A $8M(2026-03), ~40명, Toronto

📈 Signals
   • Series A 직후 — 세일즈 6명 채용 중(성장 드라이브)
   • 지난달 "AI 리콜" 기능 출시
   • Jane, 2주 전 LinkedIn에 "clinic no-shows" 포스트

🎯 Angles
   • no-show/recall 통증 ↔ 우리 reactivation 플레이 직결
   • Series A = 예산 있음 + ROI 증명 urgency
   • 질문: 멀티로케이션 클리닉은 지금 어떻게 처리하시나요?

🔗 linkedin.com/in/janedoe · acme.co · techcrunch.com/acme-series-a
   Confidence: 사람 High · 회사 High · 시그널 Med
```

## 규칙

- **미팅당 1개.** 같은 미팅에 외부 참석자 여럿이면 `👤`/`🏢` 블록을 사람 수만큼
  쌓되 헤더·앵글은 하나로.
- **길이:** 화면 한 장. 시그널·앵글 각 3개 이하.
- **소스 필수:** 모든 브리핑에 `🔗` 줄. 링크 없으면 그 주장은 뺀다.
- **Confidence 필수:** 세 축(사람/회사/시그널) 각각 High/Med/Low. 못 찾았으면 Low +
  본문에 "확인 못 함" 명시.
- **역할 계정**(info@ 등)이면 `👤` 생략, 회사 브리핑만.
- **신원 미확정**이면 최상단에 `⚠️ 신원 미확정(동명이인 가능)` 한 줄.
- Slack `mrkdwn`은 `*굵게*`·`_기울임_`·`` `코드` ``를 지원. 필요하면 강조에 사용
  (과하지 않게).
