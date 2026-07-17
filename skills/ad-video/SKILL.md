---
name: ad-video
description: 'Use when making a short paid-ad or promo VIDEO (15–60s) that combines motion graphics with AI-generated visuals — social video ads, launch promos, brand sizzles for Meta/TikTok/YouTube/Reels placements. Triggers: "광고 영상 만들어줘", "프로모 비디오", "이 제품 광고 영상", "make a video ad", "launch video", "30초 광고". 기존 촬영 푸티지 편집 → youtube-edit-kit/longform-to-content, 정지 이미지 광고 → image-gen.'
---

# Ad Video

모션그래픽 + AI 생성 비주얼로 **광고 영상**을 만든다. 렌더 엔진은 HyperFrames
(HTML→video), 비주얼 소스는 image-gen 정책(Higgsfield CLI), 성과 원칙은
**A/B 변형 — 영상도 1개만 뽑으면 학습 없는 지출이다.**

**전제**: `hyperframes` 스킬 설치 필수 (없으면 `npx skills add heygen-com/hyperframes --all`).
이 스킬은 워크플로우 오케스트레이터 — 렌더 규칙은 hyperframes가 소유한다.

## Workflow

**1. 브리프 (한 번에).** 무엇을 파는가(제품/URL), 타깃 플레이스먼트(Reels/TikTok
9:16, 피드 1:1, YouTube 16:9), 길이(기본 30s, 범위 15–60s), 훅 후보, 브랜드 토큰
(DESIGN.md — 없으면 brand-guide 먼저), CTA. **광고 집행까지 갈 거면 예산/기간은
paid-ads 게이트에서** — 이 스킬은 제작만.

**2. 라우팅 (hyperframes 규칙 준수).**
- 제품/사이트가 있으면 → `/product-launch-video` (사이트 캡처 + 브랜드 토큰)
- 모션이 곧 메시지인 ≤10s 컷 → `/motion-graphics`
- 소재만 있는 자유 구성 → `/general-video`
라우팅 후 `npx hyperframes skills update <workflow>` — 라우터 지시대로.

**3. AI 비주얼 (image-gen 정책 그대로).**
- 장면용 이미지가 필요하면 image-gen 스킬로: **Higgsfield CLI 경유, 기본
  gpt_image_2, 폴백 금지**, 생성물 READ 검증. 텍스트는 이미지에 굽지 않는다 —
  카피는 전부 HyperFrames 타이포 레이어로.
- 제품 누끼: `rembg` + `birefnet-portrait`(인물) — 로컬, 무료.
- BGM/SFX/아이콘은 media-use 스킬로 해결 (로열티프리만).

**4. A/B 변형 (MANDATORY).** 캠페인당 **최소 2개, 권장 3개** — 축을 다르게:
- **훅 축**: 첫 3초를 다르게 (숫자 훅 / 문제 제기 / 결과 먼저)
- **비주얼 축**: 제품 중심 vs 상황 중심 vs 타이포 중심
공유 씬은 서브컴포지션으로 재사용해 변형 비용을 낮춘다. 네이밍
`{campaign}_{hook축}_{visual축}.mp4`.

**5. 광고 규격 체크 (배포 전 blocking).**
- 첫 3초에 훅 + 브랜드 노출 (사운드 오프 시청 전제 — 핵심 카피는 화면 텍스트로)
- 세이프존: 9:16은 상단 ~140px/하단 ~350px에 로드베어링 요소 금지
- 한국어 카피 줄나눔: keep-all, 조사에서 끊지 않기 (humanizer 룰)
- CTA는 마지막 3초 고정 + 로고 엔드카드
- 파일: H.264, 플랫폼 규격 (Meta ≤4GB/240min이지만 실무는 <100MB, 릴스 9:16 ≤90s)
- 렌더 후 프레임 추출 READ: 첫 프레임/훅 카피/CTA/엔드카드 4장 육안 검증

**6. 핸드오프.** 변형 세트 + 각 변형의 축 설명 한 줄 → 유저 승인 → 집행은
**paid-ads**(예산 게이트), 오가닉 게시는 **organic-social**. 24–48h 후 성과로
진 변형 끄고 이긴 축으로 다음 세트.
