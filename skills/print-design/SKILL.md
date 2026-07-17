---
name: print-design
description: 'Use when designing anything for PRINT — posters, flyers, banners, business cards, menus, signage, festival banners, brochures. Runs a user interview, designs at exact physical dimensions, then a harsh visual QA loop; only quality-passing output reaches the user. Triggers: "포스터 만들어줘", "전단지 디자인", "배너 디자인", "명함 만들어줘", "현수막", "print poster", "flyer design". FRONTIER MODEL ONLY (Claude Fable 5 class) — on a smaller model, tell the user quality will suffer and recommend switching before proceeding.'
---

# Print Design

인쇄물은 배포 후 수정이 불가능하다. 그래서 이 스킬의 구조는 **인터뷰 → 스펙 고정 →
디자인 → 빡센 QA 루프 → 통과본만 유저에게**. 중간 과정의 미완성본을 유저에게
보여주지 않는다.

> **모델 게이트**: 타이포/여백/컬러 판단이 작업의 대부분 — frontier 모델
> (Claude Fable 5급) 전용으로 설계됐다. 작은 모델에서 실행 중이면 시작 전에
> 유저에게 알리고 모델 전환을 권한다.

## G1 — 인터뷰 (디자인 전에, 반드시)

한 번에 몰아서 묻는다 (질문 도구 사용):
1. **용도/장소**: 어디에 붙나? 관람 거리? (거리 = 최소 글자 크기를 결정)
2. **물리 스펙**: 최종 크기(예: A2, 24"×36", 현수막 26"×70"), 인쇄 방식
   (디지털/오프셋/현수막 실사출력), 단면/양면.
3. **내용 원고**: 확정 텍스트 전부 (제목/일시/장소/연락처/QR 링크). **원고를
   지어내지 않는다** — 빈 곳은 유저에게 받는다.
4. **브랜드**: DESIGN.md/로고 파일 있나? 없으면 brand-guide 스킬로 최소 토큰부터.
5. **마감**: 인쇄소 입고일 + 인쇄소 스펙 요구사항(있다면 그게 우선).

## G2 — 스펙 고정 (숫자로)

- **Trim + Bleed**: 재단 크기 + 사방 3mm(0.125") 블리드. 배경/사진은 블리드까지
  확장, **텍스트·로고는 재단선 안쪽 5mm+ safe margin**.
- **해상도**: 래스터 이미지 300 DPI(근거리) / 100–150 DPI(현수막 등 원거리).
  텍스트와 도형은 벡터로 — HTML→PDF 렌더는 텍스트가 벡터로 남는다.
- **최소 글자**: 본문 7pt 이상(명함 6pt), 포스터 관람거리 1m당 헤드라인 ~28pt.
- **컬러**: HTML→PDF는 RGB다. 오프셋 인쇄면 인쇄소에 RGB→CMYK 변환을 확인하고,
  진한 검정은 리치블랙 이슈를 인쇄소 스펙으로 확인. 형광/네온 계열은 인쇄에서
  칙칙해진다 — 화면 시안에 주의 문구.
- 구현: HTML을 실제 물리 치수로 (`@page { size: {W}mm {H}mm; margin: 0 }`,
  요소는 mm 단위), Playwright/Chromium PDF로 출력.

## G3 — 디자인

- 브랜드 토큰 적용, 위계는 3단계 이하 (제목/보조/세부).
- **줄나눔 규칙 (KR/EN 공통 필수)**: 한국어는 `word-break: keep-all` + 제목은
  의미 단위로 수동 `<br>` (조사에서 끊지 않는다 — "성수동에서 / 만나요" OK,
  "성수동에 / 서 만나요" 실패). 영어 제목은 고아 단어(마지막 줄 한 단어) 금지,
  전치사/관사로 줄 끝내지 않기.
- QR 코드는 최소 2×2cm + 대비 확보, 실제 스캔 테스트.

## G4 — QA 루프 (이 스킬의 심장, MANDATORY)

렌더 → 스크린샷 추출 → **눈으로 READ** → 수정 → 반복. 아래 전부 통과할 때까지
유저에게 보여주지 않는다 (최대 5루프, 그래도 남으면 남은 이슈를 정직하게 보고):

1. **재단 시뮬레이션**: 블리드 라인에서 크롭한 버전 확인 — 잘리면 안 되는 요소가
   재단선 5mm 안에 있는가.
2. **거리 테스트**: 25% 축소 스크린샷 — 헤드라인/핵심 정보가 그래도 읽히는가.
3. **글자 단위 교정**: 모든 텍스트를 글자 단위로 READ — 날짜/전화번호/URL/가격은
   원고와 대조. 오타 하나 = 전량 재인쇄다.
4. **줄나눔 검사**: G3 규칙 위반(조사 끊김, 고아 단어, 단어 중간 줄바꿈) 전수 확인.
5. **대비/가독**: 배경 사진 위 텍스트 대비, 작은 글자 뭉개짐.
6. **브랜드**: 로고 최소 크기/여백/금지 배경 준수.
7. **정렬**: 그리드에서 벗어난 요소, 어중간한 여백.

## G5 — Print-ready 마감 (폰트 아웃라인 + 컬러)

QA 통과본을 인쇄소가 그대로 받는 파일로 마감한다. 도구는 **Ghostscript** —
VERIFY: `gswin64c -version` (Windows) / `gs -version`. 없으면 설치:
github.com/ArtifexSoftware/ghostpdl-downloads/releases (Windows `gs*w64.exe /S`),
macOS `brew install ghostscript`.

**1. 폰트 아웃라인 (기본).** Chromium PDF는 폰트를 서브셋 임베드하지만, 아웃라인
(전 텍스트 → 벡터 패스)이 가장 안전하다 — 인쇄소 RIP 호환·폰트 라이선스 이슈가
사라진다:

```
gswin64c -o {name}_print.pdf -sDEVICE=pdfwrite -dNoOutputFonts {name}_qa.pdf
```

**2. CMYK 변환 (인쇄소가 요구할 때만).** 위 명령에 추가:
`-sColorConversionStrategy=CMYK -dProcessColorModel=/DeviceCMYK`
ICC 프로파일 없는 RGB→CMYK는 색이 틀어진다(특히 비비드/네온) — **인쇄소에 먼저
물어라**: 디지털 인쇄는 RGB PDF를 받는 곳이 많고, 그 경우 변환하지 않는 게 낫다.

**3. 마감 검증 (blocking).**
- 폰트 제거 확인: `mutool info -F {name}_print.pdf` → 폰트 목록이 **비어야** 한다
  (mutool 없으면 winget `ArtifexSoftware.mutool`).
- 아웃라인 후 재렌더 육안 비교: `mutool draw -o check.png -r 72 {name}_print.pdf`
  → QA본과 나란히 READ — 글리프 깨짐/헤어라인 두께 변화 확인. 아웃라인 변환은
  드물게 얇은 획을 바꾼다.
- 파일 크기 확인 — 텍스트 많은 문서는 아웃라인 후 커진다(정상), 10배 이상이면 조사.

**4. 딜리버리.**
- `{name}_print.pdf` (블리드+재단표시+아웃라인, 요구 시 CMYK) + `{name}_preview.png`
  + **인쇄소 전달용 스펙 한 줄** (재단 크기/블리드/컬러모드/용지 권장/"폰트
  아웃라인 완료").
- 유저에게는 시안 1–2개만 — QA를 통과한 것만. "여러 버전 중 골라보세요"로
  미완성본을 떠넘기지 않는다.
