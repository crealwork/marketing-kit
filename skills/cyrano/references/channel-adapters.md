# 채널 어댑터 설정

`config.json`(없으면 `config.example.json` 복사)에서 `delivery.mode`로 결정한다.
시크릿은 **절대 config에 넣지 않고** 환경변수 이름만 적는다(`*_env` 필드).

## mode: return (기본)

엔진은 브리핑을 그대로 반환만 한다. 실제 전송은 **호스트 에이전트**가 자기 채널로.
Dan의 배포는 이거 — 선데이/헤르메스가 반환된 브리핑을 자기 Slack DM으로 보냄.

```json
"delivery": { "mode": "return" }
```

## mode: slack (Incoming Webhook)

1. Slack 앱 → Incoming Webhooks 켜기 → 채널(또는 본인 DM) 웹훅 URL 생성.
2. URL을 env로: `export CYRANO_SLACK_WEBHOOK="https://hooks.slack.com/services/..."`
3. config:
```json
"delivery": { "mode": "slack", "slack": { "webhook_url_env": "CYRANO_SLACK_WEBHOOK" } }
```
본문은 `text`로 전송되어 Slack `mrkdwn`으로 렌더된다.

## mode: telegram

1. @BotFather로 봇 생성 → 토큰. env: `export CYRANO_TELEGRAM_TOKEN="123:abc..."`
2. 봇과 1:1 대화 시작 후 chat_id 확인
   (`https://api.telegram.org/bot<TOKEN>/getUpdates` → `chat.id`).
3. config:
```json
"delivery": { "mode": "telegram",
  "telegram": { "bot_token_env": "CYRANO_TELEGRAM_TOKEN", "chat_id": "<YOUR_CHAT_ID>" } }
```

## mode: email (SMTP)

```json
"delivery": { "mode": "email", "email": {
  "to": "you@domain.com", "from": "bot@domain.com",
  "smtp_host": "smtp.gmail.com", "smtp_port": 587,
  "smtp_user": "bot@domain.com", "smtp_pass_env": "CYRANO_SMTP_PASS" } }
```
Gmail은 앱 비밀번호 필요. `export CYRANO_SMTP_PASS="..."`.

## 외부 감지 도메인 (필수)

```json
"own_domains": ["yourcompany.com"],
"internal_emails": ["contractor@gmail.com"]
```
`own_domains` 안의 이메일은 "내부"로 간주되어 브리핑 대상에서 빠진다. 개인메일을
쓰는 내부 인원은 `internal_emails`에 개별 추가.

## 확인

```bash
python -m engine config     # 해석된 설정 + 시크릿 마스킹 + insane-search 번들 여부
```
