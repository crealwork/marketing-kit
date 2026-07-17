---
name: seo-geo-setup
description: Use when registering a site with search engines (Google Search Console, Naver, Bing, Daum, Pinterest), optimizing for AI search engines / GEO (ChatGPT, Perplexity, Gemini, Copilot citations, llms.txt, AI crawler access), or setting up local SEO (Google Business Profile, Naver Place, Kakao Maps, Yelp). Triggers: "SEO 세팅", "검색엔진 등록해줘", "서치콘솔", "네이버 웹마스터", "GEO", "AI 검색에 뜨게 해줘", "챗GPT가 우리를 인용 안 해", "llms.txt", "로컬 SEO", "플레이스 최적화", "구글에 안 떠요". Head 태그/OG → publish-checklist, GA4/GTM → analytics-setup, 광고 → zernio-ads.
---

# SEO / GEO Setup

사이트를 **검색엔진(글로벌+한국) + AI 검색(ChatGPT·Perplexity·Gemini·Copilot)**
전 채널에 뜨게 만들고 로컬 노출까지 잡는 체크리스트 스킬. 측정(analytics-setup),
퍼블리시 최적화(publish-checklist), 광고(zernio-ads)는 각자 스킬로 — 이 스킬은
"검색과 AI 답변에 존재하게 만드는 것"만 담당한다.

## Gates

**G0 — 준비물.** `sitemap.xml` + `robots.txt` 존재 확인 (Daum 인증이 robots.txt를
수정하므로 접근 권한 먼저). 페이지 head 태그(title/OG/favicon)가 엉망이면 등록
전에 **publish-checklist 스킬**부터 — 네이버는 title/description 규칙을 까다롭게
보므로 등록 품질에 직결된다.

**G1 — 검색엔진 등록.** references/ENGINES.md. Google(URL 접두어!), Naver,
Bing(GSC 임포트), Daum(PIN→robots.txt), Pinterest(RSS 자동 핀). 등록은 브라우저
작업 — 유저 계정 로그인이 필요하니 단계별로 안내하거나 브라우저 도구로 진행.
각 엔진은 **사이트맵 제출까지가 한 세트**.

**G2 — GEO (AI 검색).** references/GEO.md. AI 크롤러 robots.txt 허용(최우선),
llms.txt 배포, 인용되기 좋은 콘텐츠 구조(직답+숫자+FAQ), JSON-LD, 엔티티 일관성,
분기 점검 루프. Bing 등록(G1)이 GEO의 기반 인덱스다.

**G3 — 로컬 SEO** (오프라인 매장/지역 서비스일 때만). references/LOCAL.md.
GBP 리뷰 전략(GEO 겸용), Naver Place 대표 키워드 5종 조합, Kakao, Yelp.

**다음 단계 핸드오프**: 등록이 끝나면 측정(analytics-setup — GSC↔GA4 연결,
AI Search 채널 포함) → 필요 시 광고(zernio-ads).

## Hard rules

1. GSC는 '도메인'이 아닌 **'URL 접두어'** 방식으로 등록 (데이터 분리·크롤버짓·
   링크거부).
2. Bing은 GSC 임포트로 — GSC 등록을 먼저 끝내는 이유이자 **GEO의 기반**
   (Copilot·ChatGPT 검색이 Bing 인덱스를 쓴다).
3. Daum은 PIN을 robots.txt에 삽입해야 사이트맵 수집이 시작된다.
4. **AI 크롤러를 막고 있으면 GEO는 시작도 못 한다** — robots.txt + CDN의 봇 차단
   설정을 가장 먼저 확인 (GEO.md §1).
5. 등록만 하고 사이트맵을 안 내면 절반만 한 것 — 완료 체크리스트로 마감.

## Quick reference

| 작업 | 위치 |
|---|---|
| 검색엔진 5종 등록 + 완료 체크 | references/ENGINES.md |
| GEO: AI 크롤러·llms.txt·인용 구조·측정 루프 | references/GEO.md |
| 로컬 SEO (GBP·Naver Place·Kakao·Yelp) | references/LOCAL.md |
| head 태그/favicon/OG | `publish-checklist` 스킬 |
| GA4/GTM/Clarity 측정 + AI Search 채널 | `analytics-setup` 스킬 |
| 유료 광고 집행 | `zernio-ads` 스킬 |

## Thanks

**AIMS** ([aim-squad.com](https://aim-squad.com)) 옆에서 많이 배우고 있습니다 — 고맙습니다.
