# ENGINES — 검색엔진 등록 (점유율 전방위 확장)

전제: sitemap.xml + robots.txt 준비 완료 (SKILL.md G0). 각 엔진 등록 후 사이트맵
제출까지가 한 세트다. 등록만 하고 사이트맵을 안 내면 절반만 한 것.

## 1. Google Search Console — 반드시 'URL 접두어'로

- search.google.com/search-console → 속성 추가 → **URL 접두어** (도메인 방식 금지)
  - 데이터 분리: 서브도메인과 안 섞여 메인 성과 측정이 명확
  - 이슈 파악: URL별 에러 + 크롤 버짓 관리 용이
  - 링크 거부(disavow): URL 접두어 방식에서만 원활
- 전 세계 점유율 1위 + **Gemini(AI 검색)** 에 사이트 정보를 전달하는 필수 통로.
- 등록 후: 사이트맵 제출 → 색인 요청(주요 페이지 URL 검사 → 색인 생성 요청).

## 2. Naver Search Advisor (한국 필수)

- searchadvisor.naver.com → 웹마스터 도구 → 사이트 등록 + 소유 확인(HTML 태그).
- 국내 점유율 1위 — 미등록이면 한국 잠재고객 50%+ 를 놓친다.
- 네이버는 **title/description 태그 규칙 준수를 까다롭게** 본다 — 페이지별 고유
  title, 자연어 description을 먼저 점검하고 등록.
- 등록 후: 사이트맵 제출 + 웹페이지 수집 요청.

## 3. Bing Webmaster Tools

- bing.com/webmasters → **"Google Search Console에서 가져오기"** 로 클릭 몇 번에
  인증 없이 임포트 (GSC 등록을 먼저 해야 하는 이유).
- 전 세계 3~4%지만 북미 7~9%; **Copilot(AI 검색)의 기반 인덱스**.
- DuckDuckGo, Yahoo 등이 Bing 인덱스를 공유 — 등록 1회 = 다중 채널 노출.

## 4. Daum 웹마스터 도구 (한국)

- webmaster.daum.net → 사이트 등록 → **발급받은 PIN 코드를 robots.txt에 직접
  삽입**해서 인증. 이게 완료돼야 사이트맵 수집이 시작된다.
- 카카오톡 검색 + 국내 다음 검색 유입 최적화.
- robots.txt 수정 권한이 없으면 이 단계에서 멈추고 유저에게 요청.

## 5. Pinterest — 비주얼 SEO (자동 유입 통로)

- **비즈니스 계정 전환 필수** — 이미지별 클릭 데이터 분석 제공.
- **RSS 피드 연동**: 블로그/사이트 RSS를 연결하면 새 글마다 핀 자동 생성 —
  콘텐츠 노출 자동화의 핵심.
- 보드(Board) 큐레이션: 카테고리별 보드 + 관련 핀. 핀 제목/설명은 구글에도
  인덱싱 → **장기 백링크 역할**.
- 인스타와 달리 유입 수명이 매우 길다 — 보드를 꾸준히 업데이트하면 복리 노출.

## 완료 체크

- [ ] GSC: URL 접두어 등록 + 사이트맵 제출 + 주요 페이지 색인 요청
- [ ] Naver: 소유 확인 + 사이트맵 + title/description 점검
- [ ] Bing: GSC 임포트 완료
- [ ] Daum: PIN이 robots.txt에 반영되고 인증 통과
- [ ] Pinterest: 비즈니스 계정 + RSS 연동 (콘텐츠 사이트일 때)
- [ ] GSC ↔ GA4 제품 링크 연결 (MEASUREMENT.md §6)
