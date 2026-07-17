# PPT Slide Generator — Claude Code Skill

AI가 리서치부터 디자인까지 자동으로 프레젠테이션 슬라이드를 만들어주는 Claude Code 스킬입니다.

## 설치법

1. 다운로드한 ZIP 파일을 압축 해제
2. `ppt-slide-generator` 폴더를 `~/.claude/skills/` 에 복사

```bash
# macOS / Linux
cp -r ppt-slide-generator ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse ppt-slide-generator "$env:USERPROFILE\.claude\skills\"
```

3. Claude Code를 재시작하면 자동 인식!

## 사용법

Claude Code에서 이렇게 말하면 됩니다:

- "PPT 만들어줘"
- "발표자료 제작해줘"
- "AI 마케팅 주제로 슬라이드 만들어줘"
- "presentation about [topic]"

## 파이프라인

1. **테마 선택** — 원하는 디자인 테마 고르기
2. **리서치** — AI가 주제를 웹 검색으로 조사
3. **아웃라인 검토** — 슬라이드 구성을 미리 확인하고 승인
4. **상세 콘텐츠 검토** — 각 슬라이드 내용을 확인하고 승인
5. **이미지 생성** (선택) — Gemini AI로 배경/삽화 생성
6. **HTML 생성** — 1920x1080 (16:9) 슬라이드 HTML 파일 생성
7. **PDF 다운로드** — 브라우저에서 PDF로 저장

## 포함된 테마

| 테마 | 스타일 | 적합한 용도 |
|------|--------|-----------|
| **Minimal** | 깔끔 모노톤 + 블루 악센트 | 범용, 미니멀 선호 |
| **Corporate** | 딥 블루 + 골드 | 비즈니스, 공식 발표 |

## 나만의 테마 만들기

`themes/` 폴더에 `.md` 파일을 추가하면 자동으로 테마 목록에 표시됩니다.

### 테마 파일 구조

```markdown
# [테마 이름] Theme — Presentation Slides

[간단한 설명]

---

## Brand Defaults
### Color Palette
- Background: `#HEXCODE` — 배경색
- Text: `#HEXCODE` — 본문 텍스트
- Primary: `#HEXCODE` — 주요 색상 (커버, 섹션 배경)
- Accent: `#HEXCODE` — 강조색 (번호, 하이라이트)
- Secondary: `#HEXCODE` — 보조 텍스트

### Font
Google Fonts CDN 링크 + font-family 설정

### Logo
로고 파일 경로 또는 텍스트 폴백

---

## Design Language
디자인 무드, 그림자, 장식 요소, 여백 규칙

---

## Tone & Language Guide
언어, 톤, 텍스트 작성 규칙

---

## Slide Types
7가지 슬라이드 타입 각각에 HTML + CSS 레퍼런스 코드:
1. Cover
2. Agenda
3. Section Divider
4. Body (Text)
5. Body (Data/Chart)
6. Quote/Highlight
7. Ending/CTA

---

## Data Visualization Guidelines
차트 색상, 종류, 규칙

---

## Common Mistakes to Avoid
10가지 주의사항
```

### 브랜드 컬러 찾는 팁

- 회사 웹사이트에서 개발자 도구(F12) → 컬러 확인
- [Coolors.co](https://coolors.co) 에서 팔레트 생성
- 브랜드 가이드라인 PDF가 있다면 그대로 사용

## 이미지 추가하는 법

### 방법 1: Gemini AI 자동 생성 (추천)
스킬이 자동으로 각 슬라이드에 맞는 이미지를 제안합니다.
승인하면 Gemini 3.1 Flash로 생성 후 슬라이드에 삽입됩니다.

**필요 조건:** `GOOGLE_AI_API_KEY` 환경변수 설정

### 방법 2: 직접 이미지 삽입
생성된 HTML 파일을 텍스트 에디터로 열어서:

```html
<!-- 배경 이미지 추가 -->
<div class="slide slide-cover" style="
  background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
              url('your-image.jpg');
  background-size: cover;
">

<!-- 인라인 이미지 추가 -->
<img src="your-image.png" style="max-width: 600px; border-radius: 12px;" />
```

### 방법 3: base64 인라인 (외부 파일 없이)
이미지를 base64로 변환하면 HTML 파일 하나로 모든 것이 포함됩니다:

```html
<img src="data:image/png;base64,iVBORw0KGgo..." />
```

변환 방법 (Python):
```python
import base64
with open("image.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()
print(f'data:image/png;base64,{b64}')
```

## PDF로 내보내기

1. 브라우저에서 HTML 파일 열기
2. 하단 "PDF로 다운로드" 버튼 클릭
3. 인쇄 대화상자에서 "PDF로 저장" 선택
4. 용지 크기가 자동으로 1920x1080에 맞춰집니다

## 요구사항

- **Claude Code** (Claude Pro 또는 Max 구독)
- **브라우저** (Chrome 추천) — HTML 미리보기 및 PDF 다운로드용
- **Google AI API Key** (선택) — Gemini 이미지 생성 시 필요

## 만든 사람

**Dan Jeong, PMP®** — @crealwork
Lovable Ambassador | Marketing Strategist | Tech Startup Co-founder

---

Made with CREAL
