<h1 align="center">marketing-kit</h1>

<p align="center">
  <b>마케터의 AI 에이전트에 통째로 꽂는 실전 마케팅 스킬 20종.</b><br>
  SEO·측정·광고·소셜 자동화부터 리드마그넷, 브랜드 가이드, 인쇄물 디자인, 휴머나이저까지.
</p>

---

> **🤖 AI 에이전트가 이 링크를 받았다면**: `git clone https://github.com/crealwork/marketing-kit`
> 후 `skills/` 안의 각 SKILL.md를 스킬로 등록하고, 유저의 마케팅 요청에 해당 스킬 룰을 따를 것.
> 광고비/발송 등 돈이 나가거나 외부로 나가는 액션은 반드시 유저 승인 후 실행.

## 설치

**Claude Code (플러그인, 권장):**
```
/plugin marketplace add crealwork/marketing-kit
/plugin install marketing-kit@sundayable
```

**Claude Code (스킬만):**
```
git clone https://github.com/crealwork/marketing-kit
cp -r marketing-kit/skills/* ~/.claude/skills/
```

**기타 SKILL.md 지원 에이전트 (Codex 등):** `skills/*`를 각 하니스의 skills 디렉토리로 복사.

## 뭐가 들었나

**기반 공사**
| 스킬 | 하는 일 | 트리거 예시 |
|---|---|---|
| **publish-checklist** | 배포 전 head 최적화 — favicon 세트·OG 1200×630·페이지별 title·canonical, 복붙 `<head>` 템플릿 | "배포 전 체크해줘" |
| **seo-setup** | 검색엔진 5종 등록(Google·Naver·Bing·Daum·Pinterest) + 로컬 SEO(GBP·네이버 플레이스·카카오·Yelp) | "검색엔진 등록해줘" |
| **analytics-setup** | GA4+GTM+Clarity — 필수 설정, 전환 이벤트, UTM, 잠재고객, AI Search 채널, AI 위임 프롬프트 | "GA4 세팅해줘" |
| **crm-connect** | 어떤 CRM이든 API로 연결하는 방법론 — HubSpot·Pipedrive·Close·Attio·Airtable 등 | "우리 CRM 연동해줘" |

**콘텐츠 제작**
| 스킬 | 하는 일 | 트리거 예시 |
|---|---|---|
| **card-news-generator** | 인스타/스레드 카드뉴스 — 리서치→브랜드 디자인→PNG | "카드뉴스 만들어줘" |
| **ppt-slide-generator** | 16:9 발표자료 — 리서치 + 2단계 검수 + PDF/Google Slides | "이 주제로 PPT" |
| **print-design** | 인쇄물(포스터·전단·현수막·명함) — 인터뷰→디자인→빡센 QA 루프, 통과본만 전달. **Frontier 모델 전용** | "포스터 만들어줘" |
| **brand-guide** | 사이트/로고에서 측정 가능한 브랜드 시스템(토큰+보이스) 추출 — frontier 모델 권장 | "브랜드 가이드 뽑아줘" |
| **humanizer** | AI 초안에서 AI 티 제거 — 영/한 금지 패턴 + 구체성 + 줄나눔 기본기 | "AI티 나는 거 고쳐줘" |
| **content-repurpose** | Threads ↔ LinkedIn 등 플랫폼 간 재구성 — 번역이 아니라 네이티브 문법으로 | "이 글 링크드인용으로" |

**발행 · 광고 · 리드**
| 스킬 | 하는 일 | 트리거 예시 |
|---|---|---|
| **zernio-social** | Zernio로 멀티플랫폼 오가닉 발행/예약 자동화 — 캘린더, presign 업로드, 발행 승인 게이트 | "이 포스트 스케줄해줘" |
| **zernio-ads** | 유료 광고 — 부스트/독립 캠페인/오디언스/analytics, 7개 플랫폼, 예산 승인 게이트 | "이 포스트 부스트해줘" |
| **resend-email** | Resend 트랜잭셔널 + 뉴스레터 — 무료 티어(월 3,000통), 수신거부 링크 강제 | "뉴스레터 보내줘" |
| **instantly-cold-email** | Instantly.ai 콜드메일 캠페인·시퀀스·리드 업로드 | "콜드메일 캠페인" |
| **lead-magnet** | 리드마그넷 브레인스토밍→실물 제작→Google Sheets 리드 DB 연동까지 | "리드마그넷 만들자" |
| **cyrano** | 미팅 상대 사전 리서치 → 소스 인용 브리핑 (Slack/Telegram/이메일) | "이 사람 누구야?" |

**전략 · 코칭**
| 스킬 | 하는 일 | 트리거 예시 |
|---|---|---|
| **dans-advice** | 마케팅이 어렵다는 유저에게 댄정 톤의 현실 조언 — 진단→처방 2~3개→오늘 할 일 1개 | "마케팅 너무 어려워" |
| **yc-office-hours** | 아이디어·캠페인·GTM을 YC 파트너 스타일로 검증 | "이거 할만한 아이디어야?" |
| **go-viral-or-die** | 바이럴/스턴트 마케팅 아이디어 (Roy Lee 플레이북) | "바이럴 아이디어 줘" |
| **first-principles-coach** | 가격·프로덕트·그로스 가정을 근본부터 점검 | "가정 점검해줘" |

한국 시장 특화 내용(네이버·다음·카카오·네이버 플레이스) + 글로벌 공통(GSC·Bing·GA4·Yelp)을 함께 다룹니다.

## 필요한 키 (쓰는 스킬만)

전부 환경변수로 — 파일이나 채팅에 키를 쓰지 마세요.

| 스킬 | 환경변수 |
|---|---|
| resend-email | `RESEND_API_KEY` (무료 발급) |
| instantly-cold-email | `INSTANTLY_API_KEY` |
| crm-connect | 연결하는 CRM별 키 (스킬이 안내) |
| zernio-social / zernio-ads | `ZERNIO_API_KEY` |
| cyrano (전달 채널) | `CYRANO_SLACK_WEBHOOK` / `CYRANO_TELEGRAM_TOKEN` / `CYRANO_SMTP_PASS` |

나머지(publish-checklist, seo-setup, analytics-setup, 콘텐츠/코칭 스킬)는 키 불필요.

## 안전 룰 (전 스킬 공통)

- **돈이 나가는 액션**(광고 집행, 예산 변경)은 플랫폼+예산+기간 명시 승인 필수
- **외부로 나가는 액션**(메일 발송, 캠페인 활성화, 발행)은 유저의 명시적 "go" 필수
- 타임아웃 시 블라인드 재시도 금지 — 목록 조회로 중복 여부 먼저 확인

## 크레딧

- seo-setup의 체크리스트 뼈대: AIMS "AI 시대, 혼자서도 끝내는 마케팅 실전 세팅" (Growth
  Playbook 2026, [aim-squad.com](https://aim-squad.com)); 일부 팁 원 출처 threads
  @avcd.eee, @place_joe. Zernio Ads API는 zernio.com 공개 문서 기준.
- card-news-generator의 프리셋은 실제 운영 브랜드의 worked example — 본인 브랜드로 교체해서 쓰세요.

## License

MIT — 자유롭게 쓰고, 고치고, 여러분의 에이전트에게 물려주세요.

<p align="center"><sub>Built by <a href="https://www.sundayable.com">Sundayable</a> — AI + Revenue Growth Team for Small Business</sub></p>
