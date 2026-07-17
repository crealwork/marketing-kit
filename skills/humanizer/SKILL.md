---
name: humanizer
description: Use when text needs to sound human-written — rewriting AI-generated drafts, removing AI tells from marketing copy, emails, blog posts, social posts, or newsletters, in English or Korean. Triggers: "휴머나이즈해줘", "AI티 나는 거 고쳐줘", "사람이 쓴 것처럼", "make this sound human", "this sounds like ChatGPT", "de-AI this", or before publishing any AI-drafted prose.
---

# Humanizer

AI 초안을 사람 글로 바꾼다. 원칙: **문장을 예쁘게 다듬는 게 아니라, AI 특유의
패턴을 제거하고 구체성을 주입하는 것.** 코드 주석은 대상이 아니다.

## Process

1. **진단** — 아래 금지 목록과 대조해 문제 구절을 전부 표시한다 (고치기 전에).
2. **재작성** — 패턴 제거 + 구체성 주입. 의미 보존, 길이는 보통 10–20% 줄어든다.
3. **소리 내어 읽기 테스트** — 머릿속으로 읽어서 보도자료처럼 들리면 다시 쓴다.
4. 유저에게 무엇을 왜 바꿨는지 2–3줄로 보고 (전체 diff 나열 금지).

## Universal rules (언어 공통)

- **문장 길이에 리듬을** — 짧게 친다. 그리고 숨이 긴 문장이 따라온다. 전부 같은
  길이로 앉아 있으면 AI다.
- **헤지 제거**: "generally", "typically", "often", "it's worth noting",
  "arguably" — 그냥 말해라.
- 한 문장 한 아이디어. 쉼표로 절 세 개 쌓지 않는다.
- **형용사 삼단 나열 금지** ("fast, reliable, and scalable") — 하나만 고르거나
  다시 써라.
- **목 가다듬기 오프닝 제거**: "In today's world", "As we all know",
  "It's important to understand".
- 모든 문장이 완벽하게 대구를 이루면 오히려 티가 난다 — 일부러 흐트러뜨린다.

## English — AI tells (DO NOT USE)

- "It's not just X, it's Y" / "X isn't just Y — it's Z" 구문
- "delve", "nuanced", "multifaceted", "robust", "seamless", "leverage"(동사),
  "unlock", "elevate", "empower", "navigate the complexities"
- "In the realm of", "In the world of", "At its core", "That said,"
- Em-dash 남용 — 문단에 하나 넘으면 마침표나 쉼표로 바꾼다
- 연속 문단을 "I'll" / "Let's" / "Here's"로 시작
- "Dive into", "unpack", "explore"를 필러 동사로
- "Whether you're X or Y, [product] has you covered"로 마무리

## Korean — AI tells (DO NOT USE)

- 번역투: "~것이다", "~인 것입니다", "~할 수 있습니다" 남발 → 상황에 맞게
  "~예요", "~해요", "~합니다"로 자연화
- "매우", "정말", "굉장히" 같은 빈 강조부사 → 빼거나 구체적 수치로
- "흥미롭게도", "주목할 만한 점은", "다시 말해" 같은 메타 전환구
- 과도한 "귀하", "저희" 반복 — 한 번 쓰고 생략
- 영어 직역 느낌: "~에 있어서", "~라는 측면에서", "~을 통해"
- 존댓말·반말 혼용 — 한 글 안에서 톤 고정

## Instead, aim for

- 영어는 축약형 (it's, don't, you're) — 격식 문서 제외
- 한국어는 구어체 허용 (SNS·이메일 오프닝): "이거 진짜 괜찮아요" 같은 리듬
- **추상 대신 구체**: "saves significant time" → "saves 4 hours/week"
- **구체적 동사**: "ship", "cut", "fix" — not "implement", "reduce", "address"

## Before / After

**EN before:** "Our robust platform leverages cutting-edge AI to seamlessly
empower your team, unlocking unprecedented productivity gains."
**EN after:** "Your team ships twice as fast. The AI handles the busywork —
scheduling, follow-ups, reports — so people don't have to."

**KR before:** "저희의 혁신적인 솔루션을 통해 귀하의 비즈니스는 매우 효율적인
성장을 달성할 수 있습니다."
**KR after:** "도입한 팀들은 주당 4시간을 아꼈어요. 반복 업무를 AI가 대신하니까요."

## Line breaks — 화면에 보이는 텍스트라면 (KR/EN 공통 기본기)

카피가 헤드라인·카드·슬라이드·배너에 올라갈 때는 줄나눔이 문장력만큼 중요하다:

- **한국어**: `word-break: keep-all` 기본 적용 (단어 중간 줄바꿈 방지). 제목은
  의미 단위로 수동 줄바꿈 — 조사에서 끊지 않는다. "성수동에서 / 만나요" OK,
  "성수동에 / 서 만나요" 실패.
- **영어**: 마지막 줄에 한 단어만 남는 고아(orphan) 금지, 줄 끝을 전치사/관사
  (of, to, the, a)로 끝내지 않기. 2줄 제목은 위가 길고 아래가 짧게.
- 숫자+단위, 이름, 브랜드명은 줄 사이에서 쪼개지 않는다 (`&nbsp;` 또는 span).
- 모바일 폭(~390px)에서 한 번 확인 — 데스크톱에서 예쁜 줄바꿈은 모바일에서 깨진다.

## Red flags — 다 고쳤다고 착각하는 순간

- 금지어만 동의어로 치환하고 문장 구조는 그대로 → 여전히 AI다. 구조부터 다시.
- 모든 문단이 3문장 → 리듬이 없다는 뜻.
- 숫자·고유명사·사례가 하나도 없는 문단 → 구체성 주입 실패.
