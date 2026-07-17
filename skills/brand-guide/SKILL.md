---
name: brand-guide
description: 'Use when extracting or creating brand guidelines — from an existing website, logo, deck, or materials — into a measurable brand system (colors, typography, logo rules, voice) that agents and designers can apply. Triggers: "브랜드 가이드 뽑아줘", "브랜드 가이드라인 만들어줘", "이 사이트에서 브랜드 시스템 추출", "make a brand guide from this site", "define our brand voice", "DESIGN.md 만들어줘". Best run on a frontier model (Claude Fable 5 class) — taste calls dominate this task.'
---

# Brand Guide

사이트/로고/자료에서 **측정 가능한 브랜드 시스템**을 뽑아낸다. 산출물은 감상문이
아니라 다른 에이전트가 그대로 적용할 수 있는 토큰: hex 코드, 폰트 이름/웨이트,
간격 수치, 금지 규칙.

> **모델 권장**: 팔레트 판정·보이스 추출·응용 규칙은 취향 판단이 대부분이라
> frontier 모델(Claude Fable 5급)에서 돌리는 걸 권장. 작은 모델은 색을 평균내고
> 보이스를 뭉갠다.

## Gates

**G1 — 인테이크.** 소스 확인: 라이브 사이트 URL? 로고 파일? 기존 덱/자료?
아무것도 없으면 브랜드 인터뷰(아래 §4)로 전환. 그리고 용도 확인: 에이전트용
토큰(DESIGN.md)만? 사람에게 전달할 가이드라인 문서(PDF)까지?

**G2 — 캡처.** 사이트가 있으면:
- 주요 페이지 3–5개 풀페이지 스크린샷 (데스크톱+모바일) → 눈으로 READ.
- CSS에서 실측: `:root` 변수, computed color 빈도 상위권, font-family/weight
  실사용 조합, border-radius/shadow 패턴, 버튼·링크 상태.
- 카피 수집: 히어로 헤드라인, CTA 문구, about 문단 — 보이스 추출 원료.
스크린샷 없이 CSS만 읽고 판정하지 않는다 — 렌더된 화면이 진실이다.

**G3 — 토큰 증류.** 측정 가능한 형태로만 기록:
- **컬러**: 역할별 hex — primary / accent / ink(본문) / background / muted.
  역할당 1개, 전체 5–7개로 제한. "다양한 파란색들" 같은 기술은 실패.
- **타이포**: display/heading/body/mono 각각 폰트 이름 + 실제 웨이트 + 용례.
  폰트 파일 소스(구글폰트 링크 등)까지.
- **로고 룰**: 최소 크기, 여백(clear space), 허용 배경(어두운 배경엔 어떤 버전),
  금지 사례(늘리기, 색 변경, 그림자).
- **형태 언어**: radius 값, 그림자 유무/값, 보더 스타일, 사진 톤(있다면).

**G4 — 보이스.** 수집한 카피에서 추출:
- 형용사 3개 (서로 긴장 관계가 있어야 좋다 — 예: "따뜻한 + 정확한").
- Do/Don't 각 3–5개, **실제 문장 예시 쌍**으로 ("이렇게 씀 → 이렇게 안 씀").
- 톤 고정: 존댓말/반말, 이모지 정책, 문장 길이 경향.
- 카피가 부족하면 유저 인터뷰로 보강 — 지어내지 않는다.

**G5 — 산출.**
- **DESIGN.md** (필수): 위 토큰 전부, 에이전트가 파싱할 수 있는 구조로. 이 파일
  하나로 카드뉴스·덱·사이트·영상 자막까지 브랜드 일관성이 유지되는 게 목표
  (carousel-generator, ppt-slide-generator가 이 파일을 읽는다).
- **가이드라인 문서** (요청 시): DESIGN.md를 사람용으로 조판 — 페이지당 규칙
  하나, 실물 목업, do/don't 대비 스프레드.

## 4. 브랜드가 아직 없을 때 (인터뷰 모드)

기존 자산이 없으면 추출 대신 결정을 돕는다: 업종/타깃/경쟁사 3곳 → 무드 방향
2–3안(각각 팔레트+폰트 페어 시안) → 유저 선택 → G3–G5 동일. 시안 없이 말로만
"모던하고 미니멀" 같은 합의는 금지 — 눈에 보이는 안으로 고르게 한다.

## Hard rules

1. 모든 값은 실측 — 스크린샷/CSS에서 뽑은 hex, 실제 웨이트. 추정 금지.
2. 역할 없는 컬러를 팔레트에 넣지 않는다 (어디 쓰는 색인지 없으면 삭제).
3. 보이스 예시는 실제 카피 기반 — 없으면 유저에게 확인받은 문장으로.
4. 산출 전 셀프테스트: DESIGN.md만 보고 SNS 카드 1장을 만들 수 있는가?
   못 만들면 토큰이 부족한 것 — 돌아가서 채운다.
