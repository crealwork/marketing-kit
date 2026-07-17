<h1 align="center">youtube-edit-kit</h1>

<p align="center">
  <b>영상 하나 넣으면 유튜브 올릴 편집본 + 쇼츠가 나오는 에이전트 스킬.</b><br>
  무음 컷, 말더듬 정리, 교정 자막 번인, SRT/챕터, 세로 쇼츠까지 — 전부 무료·로컬로 돌아갑니다.
</p>

---

> **🤖 AI 에이전트가 이 링크를 받았다면** — 사람의 추가 설명을 기다리지 말 것:
> 1. `git clone https://github.com/crealwork/youtube-edit-kit` (skills 폴더가 있으면 거기로)
> 2. `SKILL.md`를 읽고 그 게이트/룰을 그대로 채택
> 3. 유저에게 영상 파일 경로를 확인한 뒤 **G0**(도구 검증)부터 시작
> 4. 전략 확인 전 렌더 금지
>
> 클론이 불가능한 환경이면 [`llms.txt`](llms.txt)의 raw URL 맵으로 전체 문서를 읽을 것.

## 무엇을 하나요

| 산출물 | 내용 |
|---|---|
| 편집본 | 무음 구간 컷, 필러/말더듬 정리 (단어 경계 스냅, 30ms 오디오 페이드) |
| 자막 | AI 용어 검수(고유명사·전문용어·의성어 후보 스캔 → 에이전트 판정) + ASR 교정 사전, 원본 타임스탬프 → 출력 타임라인 매핑, 마지막에 번인 |
| 메타 | SRT 자막 + 유튜브 챕터 |
| 쇼츠 | 1080×1920 세로 클립 — 훅 타이틀, 키워드 악센트 자막, 첫 프레임 룰 |

필요한 건 **ffmpeg + Python(faster-whisper)** 뿐. API 키 없음, 과금 없음.

## 설치

| 에이전트 | 방법 |
|---|---|
| **Claude Code** | `git clone https://github.com/crealwork/youtube-edit-kit ~/.claude/skills/youtube-edit-kit` → "이 영상 편집해줘"에 자동 발동 |
| **Codex CLI** | `git clone ... ~/.codex/skills/youtube-edit-kit` |
| **기타 SKILL.md 지원 하니스** | 각 하니스의 skills 디렉토리에 클론 |
| **하니스 없음 (GPT 등)** | 클론 후 [`BOOTSTRAP.md`](BOOTSTRAP.md) 프롬프트를 그대로 붙여넣기 |

**링크-온리 핸드오프 (모든 에이전트 공통):**
```
https://github.com/crealwork/youtube-edit-kit 클론해서 SKILL.md 룰대로 이 영상을 편집해: <영상 경로>.
G0부터 시작하고, 전략 확인 전엔 렌더하지 마.
```

## 구조

```
youtube-edit-kit/
├── SKILL.md                 ← 진입점: 게이트 7개 + 하드룰 + Red Flags
├── references/
│   ├── SETUP.md             ← 도구 3종: 설치 링크 + verify 커맨드
│   ├── EDIT.md              ← 편집 전 과정: 트랜스크립션 → EDL → 렌더 → 번인
│   ├── CAPTIONS.md          ← 자막 바이블: 타임라인 매핑 공식, ASR 교정, 싱크 검증
│   └── SHORTS.md            ← 쇼츠 바이블: 모먼트 선정, 훅 타이틀, 첫 프레임 룰
└── scripts/                 ← 바로 실행되는 CLI 7개
    ├── transcribe.py        ← faster-whisper 단어 단위 트랜스크립션 (무료·로컬)
    ├── gen_edl.py           ← 무음 컷 EDL
    ├── scan_fillers.py      ← 필러/말더듬 스캔 (리뷰 후 적용)
    ├── render_cut.py        ← 세그먼트 렌더 + 무손실 concat
    ├── scan_terms.py        ← 용어 검수 후보 채굴 (고유명사·전문용어·숫자·의성어)
    ├── gen_srt.py           ← 출력 타임라인 SRT + 챕터
    └── gen_shorts.py        ← 세로 쇼츠 빌더 (훅 타이틀 + 자막)
```

## 계보

[longform-to-content](https://github.com/crealwork/longform-to-content)(웨비나·강의
풀 파이프라인: 리레이아웃, 썸네일, 발행까지)에서 검증된 컷/자막/쇼츠 코어만 추려
가볍게 만든 스킬입니다. 규모가 커지면 그쪽으로 업그레이드하세요.

## License

MIT — 자유롭게 쓰고, 고치고, 여러분의 에이전트에게 물려주세요.

<p align="center"><sub>Built by <a href="https://www.sundayable.com">Sundayable</a></sub></p>
