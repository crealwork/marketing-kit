---
name: image-gen
description: Use when generating marketing images or AI video clips — newsletter heroes, blog covers, ad creatives, card news backgrounds, social visuals. All generation goes through the Higgsfield CLI (default model gpt_image_2). Triggers: "이미지 만들어줘", "뉴스레터 이미지", "블로그 커버", "광고 소재 이미지", "generate an image for", "hero image", "AI 영상 클립". 유튜브 썸네일 → thumbnail-maker. 사이트/카드 UI 디자인 → 해당 제작 스킬.
---

# Image Gen

마케팅 이미지·AI 영상 생성의 단일 창구. **모든 생성은 Higgsfield CLI 경유** —
모델 카탈로그(gpt_image_2, FLUX 계열, 시네마틱/영상 모델)를 한 계정으로 쓴다.
기본 이미지 모델은 **gpt_image_2** (텍스트/워드마크 재현 강함).

## Hard rules

1. **Higgsfield가 유일한 생성 경로.** 직접 API 호출은 힉스필드가 불가능한
   환경에서만 (부록), 그것도 유저에게 알리고.
2. **생성 전 계정 확인 필수**: `higgsfield account status` — 계정 이메일과
   크레딧을 확인하고 시작한다. 잘못된 계정의 지출은 되돌릴 수 없다.
3. **기본 모델 = gpt_image_2.** 다른 모델(FLUX 등)은 유저 지정 또는 스타일 특성상
   필요할 때 — `higgsfield model list --image`로 카탈로그 확인. 실패 시 다른
   모델로 **말없이 전환 금지** — 보고하고 유저가 결정.
4. **변형은 기본 복수 생성**: 용도당 최소 3개 (구도/톤/컨셉 다르게). **광고
   소재는 A/B 전제 — 4개+** (훅 축 × 비주얼 축). 1장 생성은 이 스킬 위반.
5. **생성 후 눈으로 검증**: 각 결과를 READ — 이미지 속 텍스트는 글자 단위로,
   손가락/로고 왜곡, 브랜드 컬러. 텍스트가 핵심인 이미지는 **텍스트를 굽지 말고
   HTML/PIL 오버레이**가 기본.
6. 실존 인물은 유저 제공 사진 기반(`--image` 레퍼런스)만 — 얼굴을 지어내지 않는다.
7. Windows에서 CLI는 전체 경로로: `%APPDATA%\npm\higgsfield.cmd`.

## Setup (1회)

```
npm i -g @higgsfield/cli          # Node 필요
higgsfield auth login             # 브라우저 로그인
higgsfield account status         # VERIFY: 이메일 + 크레딧
higgsfield model list --image     # 카탈로그 확인 (gpt_image_2 포함)
```

## 생성

```bash
# 텍스트 → 이미지
higgsfield generate create gpt_image_2 \
  --prompt "<장면 서술>" --aspect_ratio 16:9 --quality high --resolution 2k \
  --wait --json

# 이미지 입력 (실물 사진/디자인 레퍼런스 — 목업 합성, 인물 유지)
higgsfield generate create gpt_image_2 --image ./reference.png \
  --prompt "<이 이미지를 정확히 유지한 채 ...>" --aspect_ratio 9:16 \
  --quality high --resolution 2k --wait --json
```

- 응답 JSON에서 `result_url` 파싱 → 다운로드는 Python `urllib.request.urlretrieve`
  (Windows curl 인코딩 함정 회피).
- 일시적 502 → **1회만** 재시도. 반복 실패는 보고.
- 레퍼런스 충실도가 중요한 합성은 프롬프트에 "reproduce EXACTLY as provided,
  same layout/text/colors, no redesign" 를 명시 — 그래도 잔글씨는 근사치임을
  유저에게 고지 (정본은 원본 파일).
- AI 영상 클립: `higgsfield model list --video`로 모델 확인 후 동일 패턴 —
  편집/합성 파이프라인은 ad-video·hyperframes가 소유.

## 용도별 스펙

| 용도 | 비율 | 변형 수 | 비고 |
|---|---|---|---|
| 뉴스레터 히어로 | 16:9 → 1200폭 리사이즈 | 3 | 텍스트 없는 비주얼 + 제목은 이메일 HTML로 |
| 블로그 커버 | 16:9 | 3 | OG 1200×630 크롭 겸용 고려 |
| 광고 소재 | 1:1 / 16:9 플랫폼별 | **4+ (A/B 필수)** | 훅 축·비주얼 축 각각 다르게, paid-ads로 집행 |
| 카드뉴스 배경 | 4:5 | 2–3 | 텍스트 영역 비워달라고 프롬프트에 명시 |
| 목업 합성 | 장면에 맞게 | 2+ | `--image`로 실제 디자인 입력, EXACTLY 보존 지시 |

## Workflow

1. `account status` 확인 → 용도/비율/브랜드 톤(DESIGN.md) 확인 → 모델 선택.
2. 변형 축 설계 (예: A=인물 / B=제품 클로즈업 / C=추상) → 각각 생성.
3. 전 변형 READ 검증 → 불합격 재생성 (같은 모델).
4. 파일명 `{용도}_{axis}_{n}.png` — A/B 추적 가능하게.
5. 변형 세트로 제시 + 축 설명 한 줄씩 + 크레딧 사용량 언급.

## 부록 — 직접 API (Higgsfield 불가 환경 전용)

- OpenAI `gpt-image-2`: `POST /v1/images/generations` (env `OPENAI_API_KEY`;
  `billing_hard_limit_reached` = 크레딧 소진 보고). 편집은 `/v1/images/edits`.
- Google Nano Banana: Gemini `generateContent` + `inline_data` 이미지 입력
  (env `GEMINI_API_KEY`).
둘 다 유저 고지 후에만. 그 외 모델/서비스 금지.
