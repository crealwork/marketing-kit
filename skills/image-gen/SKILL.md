---
name: image-gen
description: Use when generating marketing images via API — newsletter heroes, blog covers, ad creatives, card news backgrounds, social visuals. Only two models are allowed: OpenAI gpt-image-2 (default) and Google Nano Banana (Gemini image). Triggers: "이미지 만들어줘", "뉴스레터 이미지", "블로그 커버", "광고 소재 이미지", "generate an image for", "hero image". 유튜브 썸네일 → thumbnail-maker. 사이트/카드 UI 디자인 → 해당 제작 스킬.
---

# Image Gen

마케팅 이미지 생성의 단일 창구. **허용 모델은 딱 둘**: OpenAI `gpt-image-2`(기본)과
Google Nano Banana(Gemini 이미지 모델). **다른 모델·서드파티 생성 서비스로의
폴백 금지** — 실패하면 유저에게 보고하고 지시를 받는다. Higgsfield 등 중개 서비스
대신 각 API에 직접 붙는다.

## 모델 정책 (hard rules)

1. **기본 = gpt-image-2.** Nano Banana는 유저가 지정하거나 아래 라우팅에 해당할 때.
2. **라우팅 가이드**: 텍스트/워드마크가 이미지 안에 필요 → gpt-image-2 (텍스트
   렌더 정확도 우위). 입력 이미지 기반 편집·인물 일관성·장면 합성 → Nano Banana
   (이미지 입력 네이티브).
3. **No fallback**: 선택 모델이 실패(쿼터/정책/에러)하면 다른 모델로 **말없이
   넘어가지 않는다** — 실패 내용을 보고하고 유저가 결정.
4. **변형은 기본 복수 생성**: 한 용도당 최소 3개 변형 (구도/톤/컨셉 다르게).
   **광고 소재는 A/B 테스트 전제 — 반드시 여러 버전** (권장 4개+, 훅/비주얼 축을
   달리해서). 1장만 뽑고 끝내는 것은 이 스킬 위반.
5. **생성 후 눈으로 검증**: 각 이미지를 READ — 이미지 속 텍스트는 글자 단위로
   (이미지 모델은 $20을 0으로 렌더한 전과가 있다), 손가락/로고 왜곡, 브랜드 컬러.
   텍스트가 중요한 이미지는 **텍스트를 굽지 말고 HTML/PIL 오버레이**가 기본.
6. 키는 env로만: `OPENAI_API_KEY`, `GEMINI_API_KEY`(또는 GOOGLE_AI_API_KEY).
7. 실존 인물 이미지는 유저가 제공한 사진 기반 편집만 — 얼굴을 지어내지 않는다.

## A. gpt-image-2 (OpenAI)

```python
import base64, json, os, urllib.request
req = urllib.request.Request(
    "https://api.openai.com/v1/images/generations",
    data=json.dumps({
        "model": "gpt-image-2",
        "prompt": PROMPT,
        "size": "1536x1024",      # 1024x1024 | 1536x1024 | 1024x1536
        "n": 1,                    # 변형은 프롬프트 축을 바꿔 반복 호출이 품질상 유리
    }).encode(),
    headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
             "Content-Type": "application/json"})
r = json.loads(urllib.request.urlopen(req, timeout=180).read().decode("utf-8"))
open(OUT, "wb").write(base64.b64decode(r["data"][0]["b64_json"]))
```

- 조직 인증(verified org) 필요할 수 있음 — 403이면 유저에게 안내.
- 편집(입력 이미지)은 `/v1/images/edits` (multipart, image+prompt).
- `billing_hard_limit_reached`(400) = 크레딧 소진 — 보고, 폴백 금지.

## B. Nano Banana (Gemini)

```python
import base64, json, os, urllib.request
MODEL = "gemini-2.5-flash-image"   # Nano Banana; Pro급 텍스트/디테일 필요 시 최신 pro image 모델
req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
    data=json.dumps({"contents": [{"parts": [{"text": PROMPT}]}]}).encode(),
    headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"],
             "Content-Type": "application/json"})
r = json.loads(urllib.request.urlopen(req, timeout=180).read().decode("utf-8"))
for part in r["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        open(OUT, "wb").write(base64.b64decode(part["inlineData"]["data"]))
```

- 입력 이미지 편집: parts에 `{"inline_data": {"mime_type": "image/png", "data": b64}}`
  를 프롬프트와 함께 — 인물/제품 일관성 유지에 강함.
- 모델명은 시점에 따라 갱신 — 실패 시 models 목록 API로 현행 이미지 모델 확인.

## 용도별 스펙

| 용도 | 크기 | 변형 수 | 비고 |
|---|---|---|---|
| 뉴스레터 히어로 | 1536×1024 → 1200폭 리사이즈 | 3 | 텍스트 없는 비주얼 + 제목은 이메일 HTML로 |
| 블로그 커버 | 1536×1024 | 3 | OG 1200×630 크롭 겸용 고려 |
| 광고 소재 | 플랫폼 규격(1080×1080/1200×628) | **4+ (A/B 필수)** | 훅 축·비주얼 축 각각 다르게, zernio-ads로 집행 |
| 카드뉴스 배경 | 1080×1350 | 2–3 | 텍스트 영역 비워달라고 프롬프트에 명시 |

## Workflow

1. 용도/크기/브랜드 톤(DESIGN.md 있으면 팔레트·무드 반영) 확인 → 모델 라우팅.
2. 변형 축 설계 (예: A=인물 중심 / B=제품 클로즈업 / C=추상 그래픽) → 각각 생성.
3. 전 변형 READ 검증 (§hard rule 5) → 불합격은 재생성 (같은 모델로).
4. 파일명 규칙: `{용도}_{axis}_{n}.png` — A/B 추적이 가능해야 한다.
5. 유저에게 변형 세트로 제시 + 어떤 축이 다른지 한 줄씩.
