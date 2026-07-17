---
name: lead-magnet
description: Use when creating a lead magnet end-to-end — brainstorming the offer with the user through Q&A, building the actual deliverable (checklist, guide PDF, template, swipe file), and wiring captured leads into a Google Sheets database. Triggers: "리드마그넷 만들자", "리드 마그넷 브레인스토밍", "무료 자료 만들어서 리드 모으고 싶어", "lead magnet", "무료 가이드 만들어줘", "이메일 수집하게 자료 하나". 뉴스레터 발송 자체는 resend-email로.
---

# Lead Magnet

리드마그넷을 **아이디어 브레인스토밍 → 실물 제작 → 리드 DB(Google Sheets) 연동**
까지 끝낸다. 산출물은 "리드마그넷 아이디어 목록"이 아니라 배포 가능한 실물 +
리드가 쌓이는 시트다.

## G1 — 브레인스토밍 (질문 주고받기, 대화로)

한 번에 다 묻지 말고 라운드로 — 답이 다음 질문을 결정한다:
1. **누구의 어떤 고통?** 타깃 1문장 + 그들이 지금 검색/고민하는 문제 1개.
2. **비즈니스 연결**: 이 리드가 결국 뭘 사게 되나? (마그넷은 본상품으로 가는
   첫 계단이어야 — 무관한 인기 자료는 쓰레기 리드만 모은다.)
3. **약속 1개**: "이거 받으면 10분 안에 ___할 수 있다"가 성립하는가.
4. **포맷 제안 2–3개** (아래 기준으로) → 유저 선택.

**좋은 마그넷 기준**: 10분 내 소비 가능 · 즉시 실행 가능한 결과 1개 · 본상품의
필요성을 자연스럽게 증명 · 제목만 보고 가치를 아는 이름 ("체크리스트 12항목"처럼
구체 수치 포함).

**포맷 옵션**: 체크리스트(가장 빠름) / 실전 가이드 PDF / 템플릿·스와이프 파일
(복붙 가능한 것) / 미니 진단(점수+처방) / 계산기·시트.

## G2 — 실물 제작

- 브랜드 토큰 적용 (DESIGN.md 있으면 그대로, 없으면 brand-guide 스킬로 최소
  토큰부터). 카피는 humanizer 룰 통과.
- PDF형: HTML → PDF (표지 + 본문, 페이지당 아이디어 1개, 마지막 페이지 = 본상품
  CTA + 연락처). 템플릿형: 복사 가능한 Google Docs/Sheets 링크로.
- **셀프 QA**: 약속한 결과가 실제로 10분 안에 나오는가를 처음부터 따라해 본다.
  안 나오면 내용 보강 — 얇은 마그넷은 이메일 주소보다 신뢰를 더 많이 태운다.
- 파일명/제목에 버전 넣지 않기 (`가이드_v3_최종.pdf` 금지).

## G3 — 수집 동선

- 랜딩(또는 기존 페이지 섹션): 헤드라인 = 약속, 폼 필드는 **이메일 (+이름)만** —
  필드 하나 늘 때마다 전환이 떨어진다. 광고/PPC 랜딩이면 네비게이션 제거.
- 제출 직후 **자동 전달 메일** (resend-email): 감사 + 다운로드 링크. 이 메일의
  hard bounce = 가짜 이메일 → 시트에서 즉시 표시/삭제 (진짜 사람만 남기기).
- UTM 태깅: 어떤 채널이 리드를 가져왔는지 폼 hidden 필드로 함께 수집.

## G4 — 리드 DB: Google Sheets 연동

시트 스키마 (1행 고정): `timestamp | email | name | source(utm) | magnet |
status(new/delivered/bounced) | notes`

연동 방법 (상황별):
- **A. Google Forms** (가장 빠름, 노코드): Forms → 응답 → Sheets 자동 연결.
  폼을 랜딩에 임베드. 단점: 디자인 제약.
- **B. 자체 폼 → Apps Script 웹훅** (커스텀 랜딩용): 시트에서 확장 프로그램 →
  Apps Script → `doPost(e)`로 append하는 스크립트 배포(웹 앱, 액세스: 모든 사용자)
  → 폼이 그 URL로 POST. 스크립트 뼈대:

```javascript
function doPost(e) {
  const p = JSON.parse(e.postData.contents);
  SpreadsheetApp.openById("SHEET_ID").getSheetByName("leads")
    .appendRow([new Date(), p.email, p.name || "", p.utm_source || "",
                p.magnet || "", "new", ""]);
  return ContentService.createTextOutput("ok");
}
```

- **C. 폼 서비스** (Tally/Typeform 등): 서비스의 Google Sheets 네이티브 연동 사용.
- 어느 방법이든 VERIFY: 테스트 제출 1건 → 시트에 행이 붙고 전달 메일이 오는지
  직접 확인.

## G5 — 후속

- 전달 메일 후 시퀀스 2–3통 (가치 → 사례 → 본상품 제안) — resend-email의
  브로드캐스트/오디언스로. 리스트가 크면 CRM으로 승격 (crm-connect).
- 주간 점검: 시트 리드 수 + 채널(utm)별 전환 — 안 되는 채널은 끄고 되는 채널에
  집중.
