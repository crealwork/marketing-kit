---
name: crm-connect
description: 'Use when connecting an AI agent to ANY CRM via its API — HubSpot, Pipedrive, Close, Attio, Salesforce, Zoho, Airtable/Notion-as-CRM, or a Korean CRM — to read/write leads, contacts, deals, notes, tasks. Triggers: "CRM 연동해줘", "우리 CRM에 연결", "리드 넣어줘", "딜 업데이트", "connect my CRM", "sync leads to CRM", or any CRM task where no dedicated skill for that CRM exists.'
---

# CRM Connect

특정 CRM 전용 스킬이 아니라 **어떤 CRM이든 API로 연결하는 방법론**. 한 번 연결하면
프로젝트에 "연결 카드"를 남겨 다음 세션부터 재사용한다.

## Gates (처음 연결할 때, 순서대로)

**G1 — CRM 식별.** 유저에게 묻는다: 어떤 CRM? 어떤 작업(리드 입력/딜 관리/리포트)?
그 CRM의 공식 API 문서를 찾는다 (웹 검색 또는 문서 도구). 문서 없이 엔드포인트를
추측하지 않는다.

**G2 — 인증.** 우선순위: API 키 > Personal Access Token > OAuth2(에이전트에겐
최후 수단). 키는 **env 변수로만** (`HUBSPOT_API_KEY`, `PIPEDRIVE_API_TOKEN` 등
CRM별 이름). 파일/채팅에 키 값 기록 금지. 유저가 키 발급 위치를 모르면 해당 CRM의
Settings → API/Integrations 경로를 안내.

**G3 — 최소 읽기로 검증.** 가장 싼 read 호출(연락처 1건 목록 등)이 200을 반환하는지
확인. 실패 시 인증 방식(헤더 vs Basic vs query param)부터 재확인 — CRM마다 다르다.

**G4 — 엔티티 매핑.** 아래 표로 이 CRM의 용어를 확인하고 유저와 맞춘다:

| 개념 | HubSpot | Pipedrive | Close | Salesforce | Attio |
|---|---|---|---|---|---|
| 사람 | contact | person | contact | Contact/Lead | person record |
| 회사 | company | organization | **lead** (회사 단위!) | Account | company record |
| 거래 | deal | deal | opportunity | Opportunity | (custom object) |
| 활동/메모 | engagement | activity/note | activity | Task/Event | note |

Close처럼 "lead"가 회사를 뜻하는 CRM이 있다 — 용어를 확인하지 않고 쓰면 데이터가
엉뚱한 곳에 들어간다.

**G5 — 연결 카드 작성.** 프로젝트 루트에 `CRM.md`를 만들어 기록: CRM 이름, base
URL, 인증 방식 + env 변수명, 검증된 엔드포인트 목록, 엔티티 용어 매핑, 파이프라인/
스테이지 ID 목록, 커스텀 필드 ID, rate limit. **다음 세션은 이 카드부터 읽는다.**

## Hard rules (모든 CRM 공통 — 전부 실제 사고 기반)

1. **Search before create** — 생성 전에 이메일/이름으로 검색해 중복 방지.
2. **ID로 쓰고 label로 쓰지 않는다** — 스테이지/상태 label은 파이프라인 간에
   중복된다. 의도한 파이프라인의 status/stage **ID**를 조회해서 그걸로 쓴다.
3. **삭제·병합·대량 업데이트는 유저 승인 필수** — 건수와 대상을 먼저 보여준다.
4. 쓰기 작업 후 결과 요약 보고 (몇 건 생성/수정, 레코드 링크).
5. 특수문자/이모지 포함 본문은 Python `json.dumps()`로 — curl 인라인 JSON은 깨진다.
6. 페이지네이션 확인 없이 "전체"를 단정하지 않는다 (`has_more`/cursor/offset).
7. Rate limit을 문서에서 확인하고 대량 작업은 스로틀 (기본 안전값: 5 req/s).
8. 캐시된 ID를 신뢰하지 않는다 — 파이프라인/커스텀 필드는 쓰기 직전에 라이브 조회.

## 자주 하는 작업 패턴

- **리드 유입 → CRM**: 폼/랜딩의 리드를 사람+회사로 생성, 소스(utm)를 커스텀
  필드나 메모로 기록, 담당자 할당 규칙은 유저에게 확인.
- **CRM → 광고 오디언스**: 리드 이메일 목록 추출 → 광고 플랫폼 커스텀 오디언스로
  (paid-ads 스킬 C절).
- **미팅 브리핑**: 캘린더 참석자 이메일 → CRM에서 기존 기록 조회 → cyrano 스킬로
  외부 리서치와 합쳐 브리핑.
- **주간 파이프라인 리포트**: 스테이지별 딜 수/금액 집계 — ID 기준으로 집계하고
  label은 표시용으로만.

## Airtable/Notion을 CRM으로 쓰는 경우

정식 CRM API보다 단순하다: 테이블/데이터베이스 스키마를 먼저 읽고(G4의 엔티티
매핑을 유저 스키마에 적용), 나머지 하드룰 동일. select 필드의 옵션 이름이 스테이지
역할 — 옵션 추가는 승인 후.
