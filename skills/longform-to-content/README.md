<p align="center">
  <img src="assets/hero.png" alt="longform-to-content" width="820">
</p>

<h1 align="center">longform-to-content</h1>

<p align="center">
  <b>통영상 하나 → 풀편집 + 쇼츠 + 썸네일 + 발행까지, AI 에이전트가 처음부터 끝까지.</b><br>
  웨비나·강의·팟캐스트 녹화본을 넣으면 유튜브에 올라갈 완성본이 나오는 에이전트 스킬입니다.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/agent%20skill-SKILL.md-720A22">
  <img src="https://img.shields.io/badge/license-MIT-1C1917">
  <img src="https://img.shields.io/badge/battle--tested-81min%20webinar%20%E2%86%92%20live-FAF7F2">
</p>

---

> **🤖 AI 에이전트가 이 링크를 받았다면** — 사람의 추가 설명을 기다리지 말 것:
> 1. `git clone https://github.com/crealwork/longform-to-content` (skills 폴더가 있으면 거기로)
> 2. `SKILL.md` → `BOOTSTRAP.md` 순서로 읽고 그 운영 룰을 그대로 채택
> 3. 유저에게 영상 파일 경로를 확인한 뒤 **Gate 0**(도구 검증)부터 시작
> 4. 전략 확인 전 렌더 금지, 유저 승인 없는 발행 금지
>
> 클론이 불가능한 환경이면 [`llms.txt`](llms.txt)의 raw URL 맵으로 전체 문서를 읽을 것.

## 무엇을 하나요

81분짜리 Google Meet 웨비나 녹화 하나가 이 파이프라인을 거쳐 **당일에** 이렇게 나왔습니다:

| 산출물 | 내용 |
|---|---|
| 풀영상 (61분) | 대기실 컷, 슬라이드 풀프레임 리레이아웃 + 웹캠 PIP, 무음·말더듬 정리, 콜드오픈 하이라이트, 브랜드 인트로/아웃트로, ASR 교정 자막 번인 |
| 쇼츠 6개 (1080×1920) | 훅 타이틀 + 슬라이드 카드 + 얼굴 + 키워드 악센트 자막 + 엔드카드 |
| 썸네일 3종 | CTR 리서치 룰 기반, 실제 얼굴 레퍼런스 통생성, 썸네일 문구 = 영상 첫 발화 매칭 |
| 메타데이터 | SRT 자막, 유튜브 챕터, 제목/설명/해시태그 |
| 발행 | 유튜브 즉시 업로드 + IG 릴스/유튜브 쇼츠 6일 스케줄 (Zernio API) |

모든 단계가 **mandatory 게이트**로 짜여 있고, 각 룰에는 실제 프로덕션 사고에서 나온
셀프테스트가 붙어 있습니다. 에이전트가 "대충 비슷하게"를 할 수 없게 만든 스킬입니다.

## 에이전트별 설치 — 전부 같은 SKILL.md 하나로 동작합니다

| 에이전트 | 설치 | 시작 방법 |
|---|---|---|
| **Claude Code** | `git clone https://github.com/crealwork/longform-to-content ~/.claude/skills/longform-to-content` | 다음 세션부터 "이 녹화 편집해서 올려줘"에 자동 발동 |
| **Codex CLI** | `git clone ... ~/.codex/skills/longform-to-content` | 동일 — SKILL.md 자동 인식 |
| **OpenClaw** | `git clone ... ~/.openclaw/skills/longform-to-content` (버전에 따라 workspace `skills/`) | 스킬 목록에 잡히면 트리거 문구로 발동 |
| **Gemini CLI / 기타 SKILL.md 지원** | `git clone ... <skills-dir>/longform-to-content` | 각 하니스의 스킬 활성화 방식 사용 |
| **Hermes/GPT 등 하니스 없음** | 클론만 | [`BOOTSTRAP.md`](BOOTSTRAP.md) 프롬프트를 그대로 붙여넣기 |
| **링크만 줄 때 (제일 간단)** | 없음 | 아래 한 줄 메시지 전달 |

**링크-온리 핸드오프 (모든 에이전트 공통):**
```
https://github.com/crealwork/longform-to-content 클론해서 SKILL.md와 BOOTSTRAP.md 룰대로
이 영상을 처리해: <영상 경로>. Gate 0부터 시작하고, 전략 확인 전엔 렌더하지 마.
```
README 최상단의 에이전트 안내와 [`llms.txt`](llms.txt)가 나머지를 스스로 찾게 해줍니다
(클론 불가 환경은 raw URL로 전체 문서 접근).

## 구조 — 뭐가 어디 있나

```
longform-to-content/
├── SKILL.md                  ← 진입점: 게이트 5개 + Red Flags (전부 실제 사고 기반)
├── references/
│   ├── SETUP.md              ← 필요 도구 8종: 설치 링크 + verify 커맨드 + OS 노트
│   ├── BRAND.md              ← 브랜드 가이드 없는 유저 온보딩 → DESIGN.md 템플릿
│   ├── PIPELINE.md           ← 롱폼 편집 전 과정 (EDL·말더듬 컷·리레이아웃·콜드오픈)
│   ├── CAPTIONS.md           ← 자막 바이블: 타임라인 매핑 공식, ASR 교정 사전, 싱크 검증
│   ├── SHORTS.md             ← 쇼츠 바이블: 모먼트 선정, 존 아키텍처, 훅 타이틀, 첫 프레임 룰
│   ├── THUMBNAILS.md         ← CTR 리서치 룰 + 얼굴 레퍼런스 통생성 + 썸네일-인트로 매치
│   ├── YOUTUBE.md            ← 패키징 삼각형, 제목/설명/챕터 규격, 캐던스, 애널리틱스 루프
│   └── PUBLISHING.md         ← Zernio 계정 없는 유저 온보딩 + API + 중복발행 방지 룰
└── scripts/                  ← 실전에서 돌린 레퍼런스 구현 10개 (+ 적응 가이드 README)
```

## 시작 전 필요한 것

에이전트가 Gate 0에서 전부 검증하고, 없으면 설치 방법을 유저에게 안내합니다.
전체 목록과 verify 커맨드는 [`references/SETUP.md`](references/SETUP.md).

- [ffmpeg](https://ffmpeg.org/download.html) · Python 3.11+ (Pillow, numpy)
- [video-use](https://github.com/browser-use/video-use) — 단어 단위 트랜스크립션 헬퍼
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) — 트랜스크립션 디폴트 (무료·로컬). 다중 화자·고난도 오디오만 [ElevenLabs Scribe](https://elevenlabs.io) 유료 옵션 (키는 환경변수로만, 문서 기록 금지)
- 자막 폰트 — 브랜드 폰트 우선 (Bold 있고 가독성 통과 시), 한글 디폴트 [Pretendard](https://github.com/orioncactus/pretendard), pan-CJK 폴백 [Noto CJK](https://github.com/notofonts/noto-cjk)
- gpt-image-2/Nano Banana direct API (image-gen skill) — 썸네일 생성 (OpenAI gpt-image-2 폴백 가능)
- [Zernio](https://zernio.com) — 발행/스케줄 (없으면 스킬이 온보딩 안내, 수동 업로드 폴백 있음)

## 왜 "빡센" 스킬인가

이 스킬의 Red Flags 테이블은 가상의 주의사항이 아니라 **전부 한 번씩 실제로 터졌던
사고**입니다. 몇 개만:

- "POST가 타임아웃됐으니 재시도하자" → 서버엔 이미 생성돼 있었다. **목록 조회 먼저, 블라인드 재시도 = 중복 발행.**
- "이미지 모델이 텍스트 잘 쓰겠지" → `$20`을 `0`으로 렌더링. **글자 단위로 읽고 검증, 오타는 재생성.**
- "편집본을 다시 트랜스크립션해서 자막 만들자" → 컷마다 ~1초 드리프트 누적. **원본 타임스탬프 + 매핑 공식만.**
- "자막 먼저 굽고 오버레이 올리자" → 오버레이가 자막을 가림. **자막은 무조건 마지막.**

## License

MIT — 자유롭게 쓰고, 고치고, 여러분의 에이전트에게 물려주세요.

<p align="center"><sub>Built by <a href="https://www.sundayable.com">Sundayable</a> — proven on a real webinar, shipped the same day.</sub></p>
