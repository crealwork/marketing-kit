"""Channel adapters — where the finished brief goes.

Modes (config.delivery.mode):
  return    -> print the brief to stdout; the HOST agent relays / delivers it
  slack     -> POST to a Slack incoming webhook
  telegram  -> POST to the Telegram Bot API sendMessage
  email     -> send via SMTP (env-configured)

Everything is stdlib urllib — no third-party HTTP dependency, so the skill
installs cleanly into any agent's environment. Adapters never raise; they
return a structured result so the CLI can report cleanly and the caller can
decide whether to fall back to "return".
"""
from __future__ import annotations

import json
import smtplib
import urllib.error
import urllib.request
from email.message import EmailMessage
from typing import Any

from . import config as cfg_mod

_TIMEOUT = 20


def _post_json(url: str, payload: dict[str, Any]) -> tuple[bool, str]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
            body = resp.read().decode("utf-8", "ignore")
            return True, body[:500]
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}"
    except Exception as e:  # noqa: BLE001 - adapters must not raise
        return False, f"{type(e).__name__}: {e}"


def _slack(brief: str, cfg: dict[str, Any]) -> dict[str, Any]:
    conf = cfg["delivery"].get("slack", {})
    url = cfg_mod.resolve_env(conf.get("webhook_url_env"))
    if not url:
        return {"ok": False, "mode": "slack",
                "detail": f"env {conf.get('webhook_url_env')!r} not set"}
    ok, detail = _post_json(url, {"text": brief})
    return {"ok": ok, "mode": "slack", "detail": detail}


def _telegram(brief: str, cfg: dict[str, Any]) -> dict[str, Any]:
    conf = cfg["delivery"].get("telegram", {})
    token = cfg_mod.resolve_env(conf.get("bot_token_env"))
    chat_id = conf.get("chat_id")
    if not token or not chat_id:
        return {"ok": False, "mode": "telegram",
                "detail": "bot_token env or chat_id missing"}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    ok, detail = _post_json(url, {"chat_id": chat_id, "text": brief,
                                  "disable_web_page_preview": True})
    return {"ok": ok, "mode": "telegram", "detail": detail}


def _email(brief: str, cfg: dict[str, Any], subject: str) -> dict[str, Any]:
    conf = cfg["delivery"].get("email", {})
    host = cfg_mod.resolve_env(conf.get("smtp_host_env")) or conf.get("smtp_host")
    port = int(conf.get("smtp_port", 587))
    user = cfg_mod.resolve_env(conf.get("smtp_user_env")) or conf.get("smtp_user")
    password = cfg_mod.resolve_env(conf.get("smtp_pass_env"))
    to = conf.get("to")
    if not (host and user and password and to):
        return {"ok": False, "mode": "email",
                "detail": "smtp host/user/pass/to incomplete"}
    msg = EmailMessage()
    msg["From"] = conf.get("from", user)
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(brief)
    try:
        with smtplib.SMTP(host, port, timeout=_TIMEOUT) as s:
            s.starttls()
            s.login(user, password)
            s.send_message(msg)
        return {"ok": True, "mode": "email", "detail": f"sent to {to}"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "mode": "email", "detail": f"{type(e).__name__}: {e}"}


def send(brief: str, cfg: dict[str, Any], subject: str = "cyrano brief") -> dict[str, Any]:
    mode = cfg["delivery"].get("mode", "return")
    if mode == "return":
        return {"ok": True, "mode": "return", "detail": "returned to host", "brief": brief}
    if mode == "slack":
        return _slack(brief, cfg)
    if mode == "telegram":
        return _telegram(brief, cfg)
    if mode == "email":
        return _email(brief, cfg, subject)
    return {"ok": False, "mode": mode, "detail": f"unknown delivery mode {mode!r}"}
