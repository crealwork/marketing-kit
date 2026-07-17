---
name: analytics-setup
description: 'Use when setting up web analytics and measurement — GA4 property + GTM install, Microsoft Clarity, conversion/key events, UTM tagging, Google Ads / Search Console links, audiences, or the AI Search channel group. Triggers: "GA4 세팅해줘", "GTM 설치", "전환 추적 붙여줘", "UTM 어떻게", "애널리틱스 연결", "잠재고객 만들어줘", "set up GA4", "conversion tracking". 광고 집행 자체는 paid-ads, 검색엔진 등록은 seo-setup.'
---

# Analytics Setup

## Hard rules

1. gtag.js 직접 설치와 GTM 설치를 **동시에 하지 않는다** (데이터 2배).
2. 내부 트래픽 필터는 정의만 하면 제외 안 됨 — **'활성'까지 전환**해야 적용.
3. Google Ads ↔ GA4 연결은 **소급 불가** — 광고 시작 전에 최우선으로 연결.
4. 잠재고객은 설정 시점부터 쌓임 — 광고 계획이 있으면 **미리** 생성.
5. UTM은 소문자 + 언더바 통일; 모르면 구글 사전정의 채널 규칙을 따른다.
6. 전환 이벤트는 자동 생성에 맡기지 말고 직접 지정 + 사람 검토.
7. 검증은 눈으로: GA4 Realtime + GTM 미리보기 통과 후 게시.

측정 없이 광고를 켜는 것 = 결과를 모르는 채로 돈을 쓰는 것. 유료 광고(paid-ads 스킬)로 가기 전에 §1–§7이 완료돼 있어야 한다.

## 1. GA4 속성 + GTM 설치

- analytics.google.com → 관리 → 속성 만들기 → 측정 ID(G-XXXXXXXXXX) 확보.
- 설치는 GTM 권장: GTM → 새 태그 → "Google 애널리틱스: GA4 구성" → 측정 ID →
  트리거 All Pages → **미리보기 모드에서 발동 확인 후** 게시.
- **경고: gtag.js 직접 설치와 GTM 설치를 병행하지 말 것** — 데이터가 2배로 잡힌다.
  기존 사이트라면 먼저 어느 방식이 깔려 있는지 확인(Omnibug, 소스 검색)하고 하나만.

## 2. Microsoft Clarity (GTM으로)

- GA4가 "몇 명이 왔나"라면 Clarity는 "왜 나갔나" — 세션 녹화 + 히트맵.
- GTM → 사용자 정의 HTML 태그에 Clarity 스니펫 → 트리거 All Pages.

## 3. 필수 기본 설정 3가지 (기본값이 전부 틀려 있다)

1. **구글 신호 데이터 활성화**: 관리 → 속성 → 데이터 설정 → 데이터 수집.
   기기 간 이동을 한 사람으로 인식.
2. **데이터 보존 14개월**: 관리 → 속성 → 데이터 설정 → 데이터 보존.
   기본 2개월 — 안 바꾸면 탐색 분석에서 과거 데이터가 사라진다.
3. **내부 트래픽 필터**: 관리 → 데이터 스트림 → 태그 설정 구성 → 내부 트래픽
   정의 → 내 IP 입력. **정의만 하면 제외 안 됨 — 필터를 '활성'으로 전환까지.**

옵션 — 트래픽 적은 초기: 보고 ID를 **기기 기반**으로 (관리 → 데이터 표시 → 보고
ID). 데이터 임계값으로 숫자가 가려지는 것을 방지 (크로스 디바이스 추적은 약해짐).

## 4. 전환 이벤트 — 핵심만 골라 마킹

- 관리 → 이벤트 → 토글 → 키 이벤트(전환)로 표시.
- 마킹 대상: 폼 제출 완료, 감사 페이지 도달, 전화/카톡 버튼 클릭.
- **구글 사전정의 이벤트명 사용** (폼 제출 = `generate_lead`) → 비즈니스 목표
  보고서에 자동 편입. 참고: support.google.com/analytics/answer/9267735
- 폼 전환의 원칙: **서버가 접수를 확인한 시점에 `dataLayer.push`** (A안).
  코드 접근 불가면 맞춤 HTML 태그로 대체하되 신뢰성 한계 감수 (B안).
- CTA 클릭은 버튼마다 이벤트를 만들지 말고 태그 하나 + `cta_location` 파라미터로
  구분. 맞춤 측정기준으로 등록.

## 5. UTM — 어디서 왔는지 태깅

UTM 없는 링크 공유 = `(direct)/(none)` = 채널 효과 측정 불능.

```
utm_source   = 유입 출처 (google, threads, newsletter)
utm_medium   = 매체 유형 (cpc, social, email)
utm_campaign = 캠페인명 (spring_sale_2026)
utm_content  = 소재 구분 (banner_a, text_link)
utm_term     = 키워드 (검색광고)
```

- 규칙: **소문자 통일, 띄어쓰기 대신 언더바.** 생성은 Google Campaign URL Builder.
- 익숙치 않으면 구글 사전정의 채널 규칙에 맞는 값 사용 → 채널 단위 분류가 자동.
  참고: support.google.com/analytics/answer/9756891

## 6. 제품 연결 + 잠재고객 (광고 준비)

- **Google Ads 연결 — 최우선**: 관리 → 제품 링크 → Google Ads. 연결 전 데이터는
  소급 불가(실시간 동기화 방식)라 하루라도 빨리. GSC 연결은 조회 방식이라 소급
  가능 — 급하지 않지만 같이.
- **잠재고객 미리 생성** (설정 시점부터 쌓임): ① 리드 제출자(주요 타겟)
  ② 세션 3초+ ③ 조회수 2회+ (②③ = 단순 유입이 아닌 광고 모수).
- **AI Search 채널 추가**: 기본 채널 그룹 복제 → 최상단에 "AI Search" 채널,
  조건은 소스 정규식:
  `chatgpt|openai|oaistatic|gemini|bard|claude|perplexity|genspark|clovax|wrtn|copilot|getliner|deepseek|grok|you\.com|poe\.com`

## 7. 검증 (게시 = 끝이 아니다)

- GA4 [보고서] → 실시간: 이벤트 이름별 이벤트 수 카드에서 이벤트 확인, 아무
  이벤트 클릭 → campaign/medium/source 파라미터로 UTM 값 확인.
- Omnibug 크롬 확장(F12 → Omnibug 탭): 어떤 태그가 언제 발동하는지 실측.
- GTM 미리보기 통과 없이 게시 금지.

## 8. AI 위임 프롬프트 (바이브코딩 사이트일 때 복붙)

전제: 사이트에 GTM 삽입, GA/GTM API + 클로드 연결, (A안) 코드 저장소 접근,
**사이트 className 규칙 문서** (없으면 AI가 정규식 트리거를 짜서 유지보수 불능).

```
1. GTM 연결해서 내 컨테이너(GTM-XXXXXXX) 찾아줘
2. GA4 측정 ID를 상수 변수 ga4_ID로 만들고, Google 태그를 Initialization - All Pages 트리거로
3. 버튼 전부 이벤트로 만들지 말고, 전환이랑 핵심만 골라줘. CTA 클릭은 태그 하나로 묶고
   어느 버튼인지는 파라미터(cta_location)로 구분. 트리거 조건은 내가 준 className 규칙 기준으로.
4. 폼 제출은 버튼 클릭 말고, 서버가 접수 확인했을 때만 generate_lead 이벤트가 발행되게
   코드에 dataLayer.push 넣어줘. (코드 접근이 안 되면 맞춤 HTML로 대체하되 신뢰성 한계 감안.)
5. 미리보기 확인했으면 버전 게시해줘
```

```
GA4 기본 세팅 해줘.
① 데이터 보존 14개월 ② 구글 신호 데이터 활성화
③ 내 IP 내부 트래픽 등록 + 필터 '활성' 전환
④ 보고 ID 기기 기반 ⑤ generate_lead 키 이벤트 + cta_location 맞춤 측정기준
⑥ 잠재고객: 리드 제출자, CTA 클릭, 참여 사용자
⑦ 기본 채널 그룹 복제해서 AI Search 채널 최상단 추가 (소스 정규식은 §6)
```

**경고: 전환 이벤트는 자동 생성에 다 맡기지 말 것** — 매체 전환값으로 내보내는
축이라 여기가 어긋나면 광고 최적화가 통째로 틀어진다. 반드시 사람이 검토.
