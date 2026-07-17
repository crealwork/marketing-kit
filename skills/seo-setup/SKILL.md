---
name: seo-setup
description: Use when setting up SEO or measurement for a site — search engine registration (Google Search Console, Naver Search Advisor, Bing, Daum, Pinterest), GA4/GTM/Clarity setup, conversion events, UTM tagging, local SEO (Google Business Profile, Naver Place, Kakao Maps, Yelp), or launching paid ads via Zernio. Triggers: "SEO 세팅", "검색엔진 등록해줘", "서치콘솔 등록", "네이버 웹마스터", "GA4 세팅해줘", "전환 추적", "로컬 SEO", "플레이스 최적화", "광고 돌려줘", "boost this post", new site launch.
---

# SEO Setup

사이트 하나를 받아 **검색엔진 전 채널 등록 → 측정 기초(GA4/GTM/Clarity) → 로컬 SEO → 유료 광고(Zernio)** 까지 끝내는 체크리스트 스킬. 새로 런칭한 사이트든 방치된 사이트든 같은 게이트를 통과시킨다.

## When NOT to use

- 블로그 글 작성/발행, 콘텐츠 제작(카드뉴스/영상), 이메일 캠페인 — 별도 제작·발송 도구의 영역. 이 스킬은 **노출과 측정의 기반 공사**만 담당한다.

## Gates (해당하는 것만, 순서대로)

**G0 — 준비물 확인.** references/PUBLISH.md의 head 체크리스트(favicon 세트, 페이지별 title/description, OG 1200×630, canonical)를 통과시키고 `sitemap.xml` + `robots.txt` 확인. 없으면 먼저 만든다 — 복붙용 `<head>` 템플릿이 PUBLISH.md에 있다. **새 사이트를 만들 때도 이 체크리스트를 배포 전에 자동 적용한다.** Daum 인증이 robots.txt를 수정하므로 robots.txt 접근 권한을 먼저 확인.

**G1 — 검색엔진 등록.** references/ENGINES.md. Google(URL 접두어!), Naver, Bing(GSC 임포트), Daum(PIN→robots.txt), Pinterest(RSS 자동 핀). 등록 자체는 브라우저 작업 — 유저 계정 로그인이 필요하니 각 단계에서 유저에게 안내하거나 브라우저 도구로 진행.

**G2 — 측정 기초.** references/MEASUREMENT.md. GA4 속성 + GTM 설치(중복 설치 금지), 필수 3설정, 전환 이벤트, UTM 규칙, Ads/GSC 연결, 잠재고객, AI Search 채널. **광고비를 쓰기 전에 반드시 끝낸다.** 복붙용 AI 위임 프롬프트 포함.

**G3 — 로컬 SEO** (오프라인 매장/지역 서비스일 때만). references/LOCAL.md. GBP 리뷰 전략, Naver Place 대표 키워드 5종 조합, Kakao, Yelp.

**G4 — 유료 광고 (Zernio).** references/PAID-ADS.md. 오가닉 포스트 부스트 또는 독립 캠페인. **돈이 나가는 게이트 — 플랫폼·예산·기간을 명시한 유저 승인 없이는 어떤 광고 API 호출도 금지.**

## Hard rules

1. GSC는 '도메인'이 아닌 **'URL 접두어'** 방식으로 등록.
2. GA4는 gtag.js 직접 설치와 GTM 설치를 **동시에 하지 않는다** (데이터 2배).
3. 내부 트래픽 필터는 정의만 하면 제외 안 됨 — **'활성'까지 전환**해야 적용.
4. Google Ads ↔ GA4 연결은 **소급 불가** — 광고 시작 전에 최우선으로 연결.
5. 잠재고객은 설정 시점부터 쌓임 — 광고 계획이 있으면 **미리** 생성.
6. UTM은 소문자 + 언더바 통일; 모르면 구글 사전정의 채널 규칙을 따른다.
7. 전환 이벤트(generate_lead 등)는 자동 생성에 맡기지 말고 직접 지정 + 사람 검토. 폼 전환은 서버 접수 확인 시점의 dataLayer.push가 원칙.
8. 광고 지출은 캠페인 단위 유저 승인(플랫폼+예산+기간) 필수. 타임아웃 시 목록 조회 먼저 — 블라인드 재시도 = 중복 캠페인 = 중복 과금.
9. 검증은 눈으로: GA4 Realtime에서 UTM/이벤트 집계 확인, GTM 미리보기 통과 후 게시.

## Quick reference

| 작업 | 위치 |
|---|---|
| 퍼블리시 head 체크리스트 (favicon·title·OG 템플릿) | references/PUBLISH.md |
| 검색엔진 5종 등록 (GSC·Naver·Bing·Daum·Pinterest) | references/ENGINES.md |
| GA4·GTM·Clarity + 전환·UTM·잠재고객·AI Search 채널 | references/MEASUREMENT.md |
| 로컬 SEO (GBP·Naver Place·Kakao·Yelp) | references/LOCAL.md |
| Zernio 광고 API (boost·create·audiences·analytics) | references/PAID-ADS.md |

## Credits

체크리스트의 뼈대는 AIMS의 무료 가이드 "AI 시대, 혼자서도 끝내는 마케팅 실전 세팅" (Growth Playbook 2026, [aim-squad.com](https://aim-squad.com))을 기반으로 재구성했다. 일부 팁의 원 출처: threads @avcd.eee (GSC 등록 방식, GBP 리뷰), @place_joe (Naver Place 키워드). Zernio Ads API 섹션은 zernio.com 공개 문서 기준 (2026-07-16 검증).
