# GEO — Generative Engine Optimization (AI 검색에 인용되기)

검색의 새 축: ChatGPT·Perplexity·Gemini·Copilot이 답변에 **인용하는 소스**가
되는 것. 클릭 없이 답이 소비되는 시대에, 인용 안 되면 존재하지 않는 것이다.
측정은 analytics-setup의 AI Search 채널로 (이미 세팅돼 있어야 한다).

## 1. 크롤러 접근 — robots.txt부터 (5분, 최우선)

AI 크롤러를 차단하고 있으면 나머지는 전부 무의미. robots.txt에서 아래 봇들이
**Allow**인지 확인 (보안 플러그인/CDN이 기본 차단하는 경우가 흔하다):

```
GPTBot, OAI-SearchBot, ChatGPT-User     # OpenAI (학습/검색/브라우징)
ClaudeBot, Claude-SearchBot             # Anthropic
PerplexityBot                           # Perplexity
Google-Extended                         # Gemini 그라운딩
Bingbot                                 # Copilot + ChatGPT 검색의 기반 인덱스
CCBot                                   # Common Crawl (다수 모델의 학습 소스)
```

- 학습 제외를 원하면 GPTBot/CCBot/Google-Extended만 막고 **검색 봇
  (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot)은 열어두는** 분리
  전략도 가능 — 유저와 정책을 확인.
- VERIFY: `curl {site}/robots.txt` + Cloudflare 등 CDN의 "AI bots 차단" 설정 확인.

## 2. 인덱스 기반 (ENGINES.md와 한 세트)

- **Bing 등록이 GEO의 절반** — Copilot과 ChatGPT 웹검색이 Bing 인덱스를 쓴다.
  GSC 임포트로 5분 (ENGINES.md §3).
- GSC 등록 = Gemini에 사이트 정보 전달 (ENGINES.md §1).

## 3. llms.txt

사이트 루트에 `llms.txt` — AI 에이전트용 사이트 맵/요약:

```
# {브랜드}
> 한 줄 정의 (무엇을 누구에게 제공하는가)

## 핵심 페이지
- [서비스](https://{domain}/services): 한 줄 설명
- [가격](https://{domain}/pricing): 한 줄 설명
- [FAQ](https://{domain}/faq): 한 줄 설명
```

## 4. 인용되기 좋은 콘텐츠 구조

AI는 "질문에 대한 명확한 직답 + 근거"를 인용한다:

- **질문형 H2 + 첫 문단 직답** (40–60단어 안에 결론) — 그 아래 상세.
- **숫자·통계·1차 데이터** 포함 — 출처 있는 구체 수치가 인용 확률을 크게 올린다.
  자체 데이터/사례가 최강 (남의 통계 재인용은 원출처가 인용됨).
- **FAQ 섹션** — 실제 고객 질문 그대로를 질문 문장으로.
- **날짜 표기** — 갱신일 명시, 오래된 콘텐츠는 갱신 (AI는 최신성 가중).
- 페이지당 주제 하나, 명확한 정의문("X는 ~이다") 포함.

## 5. 구조화 데이터 + 엔티티 일관성

- JSON-LD: `Organization`(About), `FAQPage`, `Article`(author/datePublished),
  로컬이면 `LocalBusiness`. 검증: validator.schema.org.
- **엔티티 일관성**: 브랜드명·한 줄 설명·주소가 사이트/GBP/LinkedIn/디렉토리에서
  동일해야 AI가 같은 실체로 인식한다. About 페이지에 "누가·무엇을·누구에게"
  정의문을 명시.

## 6. 언급 시그널

AI 답변은 Reddit·커뮤니티·리뷰를 많이 인용한다 — 로컬이면 GBP 리뷰(LOCAL.md
리뷰 전략이 GEO도 겸한다), B2B/SaaS면 관련 커뮤니티에서 언급될 만한 것(무료 도구,
공개 데이터, 비교 자료)을 만드는 게 백링크보다 빠르다.

## 7. 측정 + 점검 루프

- analytics-setup의 **AI Search 채널**(chatgpt|gemini|claude|perplexity… 정규식)로
  유입 추적.
- 분기 1회: 주요 AI 검색(ChatGPT/Perplexity/Gemini)에 내 고객이 물을 질문 5개를
  직접 물어보고 — 우리가 인용되는지, 경쟁사가 인용되면 그 페이지 구조가 뭐가
  다른지 기록 → §4 콘텐츠 백로그로.

## 완료 체크

- [ ] robots.txt AI 크롤러 허용 확인 (+CDN 설정)
- [ ] Bing 등록 완료 (ENGINES.md)
- [ ] llms.txt 루트 배포
- [ ] 핵심 페이지 3개: 질문형 구조 + 직답 + FAQ + JSON-LD
- [ ] About 엔티티 정의문 + 채널 간 일관성
- [ ] AI Search 채널 유입 확인 + 분기 점검 리마인더
