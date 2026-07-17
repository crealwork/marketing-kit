---
name: thumbnail-maker
description: 'Use when making video thumbnails — YouTube longform (1280×720), Shorts/Reels covers (1080×1920) — always as a multi-variant set for A/B testing. Image generation via the Higgsfield CLI (default model gpt_image_2). Triggers: "썸네일 만들어줘", "썸네일 뽑아줘", "유튜브 썸네일", "커버 이미지", "make thumbnails", "CTR 썸네일". 일반 마케팅 이미지는 image-gen.'
---

# Thumbnail Maker

썸네일은 CTR 장치다 — 예쁜 이미지가 아니라 **클릭 근거**. 항상 **변형 세트
(기본 4개)** 로 뽑아 A/B 테스트에 넘긴다. 생성 정책은 image-gen 스킬과 동일:
**모든 생성은 Higgsfield CLI 경유, 기본 모델 gpt_image_2** — 다른 경로로
말없이 전환 금지 (실패 = 보고).

## Hard rules

1. **1장 금지, 항상 4개+ 변형** — 축을 달리해서: 표정/구도 × 문구 × 배경 컨셉.
   YouTube "Test & compare"(썸네일 3개 A/B)에 바로 쓸 수 있게 최소 3개는 같은
   영상용 경쟁 후보로.
2. **문구 = 영상의 첫 주장과 일치.** 콜드 오픈 첫 대사(또는 훅)와 썸네일 문구가
   어긋나면 이탈률로 돌아온다. 문구는 ≤4단어(EN) / ≤8자(KR), 낚시 금지.
3. **텍스트는 굽지 않는다** — 배경/인물은 이미지 모델로, **문구는 HTML/PIL
   오버레이**로 얹는다 (이미지 모델의 글자 렌더는 신뢰 불가). 통생성은 유저가
   원할 때만, 그 경우 글자 단위 READ 검증 필수.
4. **실제 얼굴 사용**: 인물 썸네일은 유저가 준 실제 사진 기반 (Higgsfield
   `--image` 레퍼런스 편집) — 얼굴 각도/표정 변형은 OK, 얼굴을 지어내는
   것은 금지.
5. 검증은 눈으로: 각 변형을 **모바일 스케일(약 320px 폭)로 축소해 READ** —
   문구 읽히고 표정 보이면 합격. 데스크톱 크기로만 보고 통과시키지 않는다.
6. 셋업/명령 스니펫은 image-gen 스킬 — `higgsfield account status`로 계정·크레딧
   확인 후 생성.

## 규격

| 대상 | 크기 | 비고 |
|---|---|---|
| YouTube 롱폼 | 1280×720 (16:9), <2MB | 업로드는 organic-social의 mediaItems[].thumbnail |
| Shorts/Reels 커버 | 1080×1920 | 첫 프레임 룰 우선 — 커버는 IG 그리드 1:1 센터 크롭 안전영역(y 420–1500) 고려 |
| 커뮤니티/배너 | 용도별 | image-gen으로 라우팅 |

## Workflow

1. **재료 수집**: 영상의 훅/첫 대사(트랜스크립트 있으면 그대로), 얼굴 사진(인물형
   일 때), 브랜드 토큰(DESIGN.md).
2. **변형 축 설계 (4개 기본)**: ① 인물 리액션 + 큰 문구 ② 결과물/비포애프터
   ③ 숫자 훅 중심 타이포 ④ 호기심 갭(가림/화살표). 축이 겹치는 4장은 A/B가
   아니라 같은 카드 4장이다.
3. **배경 생성** (모델 정책대로) → **문구 오버레이** (HTML→PNG 또는 PIL; 외곽선/
   그림자로 대비 확보, 한국어 줄나눔은 의미 단위).
4. **QA**: 320px 축소 READ (문구/표정), 글자 검증, 얼굴 왜곡 체크, 파일 크기
   (<2MB).
5. **딜리버리**: `thumb_A~D.png` + 각 변형의 축 설명 한 줄 + 추천 1순위와 이유.
   YouTube면 Test & compare에 3개 걸라고 안내; CTR 결과로 다음 세트를 학습.
