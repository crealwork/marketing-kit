<h1 align="center">marketing-kit</h1>

<p align="center">
  <b>마케터의 AI 에이전트에 통째로 꽂는 실전 마케팅 스킬 10종.</b><br>
  전부 실제 비즈니스에서 돌려본 것만 — SEO 기반 공사부터 콜드메일, CRM, 카드뉴스, 미팅 리서치까지.
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

| 스킬 | 하는 일 | 트리거 예시 |
|---|---|---|
| **seo-setup** | 검색엔진 5종 등록(Google·Naver·Bing·Daum·Pinterest) + GA4/GTM/Clarity 측정 + 로컬 SEO + Zernio 광고. 퍼블리시 head 체크리스트(favicon·OG·title 복붙 템플릿) 포함 | "이 사이트 SEO 세팅해줘" |
| **card-news-generator** | 인스타/스레드 카드뉴스 — 리서치→브랜드 디자인→PNG. 브랜드 프리셋 시스템 | "카드뉴스 만들어줘" |
| **ppt-slide-generator** | 16:9 발표자료 — 리서치 + 2단계 검수 + PDF/Google Slides 딜리버리 | "이 주제로 PPT" |
| **mailerlite-newsletter** | MailerLite 캠페인 제작/발송 — 실전 API 함정 문서화 | "뉴스레터 보내줘" |
| **instantly-cold-email** | Instantly.ai 콜드메일 캠페인·시퀀스·리드 업로드 — 유저 승인 게이트 | "콜드메일 캠페인" |
| **close-crm** | Close.com 리드/딜/파이프라인 관리 — status_id 함정 등 | "CRM에 리드 추가" |
| **cyrano** | 미팅 상대 사전 리서치 → 소스 인용 브리핑 (Slack/Telegram/이메일 전달) | "이 사람 누구야?" |
| **yc-office-hours** | 아이디어·캠페인·GTM을 YC 파트너 스타일로 검증 | "이거 할만한 아이디어야?" |
| **go-viral-or-die** | 바이럴/스턴트 마케팅 아이디어 (Roy Lee 플레이북) | "바이럴 아이디어 줘" |
| **first-principles-coach** | 가격·프로덕트·그로스 가정을 근본부터 점검 | "가정 점검해줘" |

한국 시장 특화 내용(네이버·다음·카카오·네이버 플레이스) + 글로벌 공통(GSC·Bing·GA4·Yelp)을 함께 다룹니다.

## 필요한 키 (쓰는 스킬만)

전부 환경변수로 — 파일이나 채팅에 키를 쓰지 마세요.

| 스킬 | 환경변수 |
|---|---|
| mailerlite-newsletter | `MAILERLITE_API_KEY` |
| instantly-cold-email | `INSTANTLY_API_KEY` |
| close-crm | `CLOSE_API_KEY` |
| seo-setup (G4 광고만) | `ZERNIO_API_KEY` |
| cyrano (전달 채널) | `CYRANO_SLACK_WEBHOOK` / `CYRANO_TELEGRAM_TOKEN` / `CYRANO_SMTP_PASS` |

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
