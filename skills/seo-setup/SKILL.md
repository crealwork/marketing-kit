---
name: seo-setup
description: Use when registering a site with search engines — Google Search Console, Naver Search Advisor, Bing Webmaster, Daum, Pinterest — or setting up local SEO (Google Business Profile, Naver Place, Kakao Maps, Yelp). Triggers: "SEO 세팅", "검색엔진 등록해줘", "서치콘솔 등록", "네이버 웹마스터", "사이트맵 제출", "로컬 SEO", "플레이스 최적화", "구글에 안 떠요". Head 태그/OG → publish-checklist, GA4/GTM → analytics-setup, 광고 → zernio-ads.
---

# SEO Setup

사이트를 **검색엔진 전 채널에 등록하고(글로벌+한국) 로컬 노출까지** 잡는 체크리스트
스킬. 측정(analytics-setup), 퍼블리시 최적화(publish-checklist), 광고(zernio-ads)는
각자 스킬로 — 이 스킬은 "검색에 뜨게 만드는 것"만 담당한다.

## Gates

**G0 — 준비물.** `sitemap.xml` + `robots.txt` 존재 확인 (Daum 인증이 robots.txt를
수정하므로 접근 권한 먼저). 페이지 head 태그(title/OG/favicon)가 엉망이면 등록
전에 **publish-checklist 스킬**부터 — 네이버는 title/description 규칙을 까다롭게
보므로 등록 품질에 직결된다.

**G1 — 검색엔진 등록.** references/ENGINES.md. Google(URL 접두어!), Naver,
Bing(GSC 임포트), Daum(PIN→robots.txt), Pinterest(RSS 자동 핀). 등록은 브라우저
작업 — 유저 계정 로그인이 필요하니 단계별로 안내하거나 브라우저 도구로 진행.
각 엔진은 **사이트맵 제출까지가 한 세트**.

**G2 — 로컬 SEO** (오프라인 매장/지역 서비스일 때만). references/LOCAL.md.
GBP 리뷰 전략, Naver Place 대표 키워드 5종 조합, Kakao, Yelp.

**다음 단계 핸드오프**: 등록이 끝나면 측정(analytics-setup — GSC↔GA4 연결 포함)
→ 필요 시 광고(zernio-ads).

## Hard rules

1. GSC는 '도메인'이 아닌 **'URL 접두어'** 방식으로 등록 (데이터 분리·크롤버짓·
   링크거부).
2. Bing은 GSC 임포트로 — GSC 등록을 먼저 끝내는 이유.
3. Daum은 PIN을 robots.txt에 삽입해야 사이트맵 수집이 시작된다.
4. 등록만 하고 사이트맵을 안 내면 절반만 한 것 — 완료 체크리스트(ENGINES.md)로
   마감.

## Quick reference

| 작업 | 위치 |
|---|---|
| 검색엔진 5종 등록 + 완료 체크 | references/ENGINES.md |
| 로컬 SEO (GBP·Naver Place·Kakao·Yelp) | references/LOCAL.md |
| head 태그/favicon/OG | `publish-checklist` 스킬 |
| GA4/GTM/Clarity 측정 | `analytics-setup` 스킬 |
| 유료 광고 집행 | `zernio-ads` 스킬 |

## Credits

체크리스트의 뼈대는 AIMS의 무료 가이드 "AI 시대, 혼자서도 끝내는 마케팅 실전 세팅" (Growth Playbook 2026, [aim-squad.com](https://aim-squad.com))을 기반으로 재구성했다. 일부 팁의 원 출처: threads @avcd.eee (GSC 등록 방식, GBP 리뷰), @place_joe (Naver Place 키워드).
