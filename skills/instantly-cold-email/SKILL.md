---
name: instantly-cold-email
description: Use when creating, managing, or automating cold email campaigns via Instantly.ai API. Trigger when user mentions Instantly, cold email, outbound email, email sequence, lead upload, or wants to set up cold outreach campaigns.
---

# Instantly Cold Email (API v2)

Create and manage Instantly.ai cold outreach campaigns: sequences, leads, sending accounts.

**Many "intuitive" details are wrong.** Every gotcha in [Common pitfalls](#common-pitfalls) is something this skill author hit on a live campaign. Read that section first when something doesn't work.

## API basics

- **Base URL**: `https://api.instantly.ai/api/v2`
- **Auth**: `Authorization: Bearer $INSTANTLY_API_KEY`
- **Key location**: env var `INSTANTLY_API_KEY` (Instantly → Settings → Integrations → API; never hardcode)
- **Rate limit**: 10 req/sec total. For bulk ops (>1000 leads) throttle to ~5 RPS.
- **Pagination**: cursor `starting_after` + `next_starting_after` in response.

```bash
INST_KEY=$INSTANTLY_API_KEY
```

## Campaign creation workflow

1. Confirm sending account ready (`/accounts`) — `daily_limit`, `stat_warmup_score`.
2. Create campaign (`POST /campaigns`) with sequences + schedule.
3. Upload leads with custom vars (`POST /leads/add`).
4. Verify lead-campaign binding (via `/leads/list` `search` filter).
5. **User activates** (`POST /campaigns/{id}/activate`) — never auto-activate.

### 1) Create campaign

```python
payload = {
  "name": "Cold — Offer A — 2026-05",
  "email_list": ["you@yourdomain.com"],
  "campaign_schedule": {
    "schedules": [{
      "name": "BC weekday hours",
      "timing": {"from": "09:00", "to": "17:00"},
      "days":   {"1": True, "2": True, "3": True, "4": True, "5": True},
      "timezone": "America/Dawson"
    }]
  },
  "sequences": [{
    "steps": [
      {"type":"email","delay":3,"variants":[{"subject":"{{subjectLine}}","body": STEP1_HTML}]},
      {"type":"email","delay":3,"variants":[{"subject":"",               "body": STEP2_HTML}]},
      {"type":"email","delay":0,"variants":[{"subject":"",               "body": STEP3_HTML}]}
    ]
  }]
}
requests.post(f"{API}/campaigns", headers=H, json=payload)
```

Key points:
- `campaign_schedule` is an **object** `{schedules: [...]}`, not a bare array. Inner: `timing.from/to` (24h "HH:MM"), `days` is a `{"1": true, ...}` dict (Monday=1), `timezone` (see [timezone whitelist](#timezone-whitelist)).
- `type` is lowercase `"email"` (uppercase 400s).
- Subject + body live inside `variants: [{subject, body}]`, not flat on the step.
- `delay` semantics — see [step delay](#step-delay-this-step--next-step-gap) below. **Set delay on the LAST step to 0**; setting first step delay to 0 fires step 2 immediately = duplicate spam.
- Empty `subject: ""` on follow-up steps = reply thread (same subject as step 1).
- Only `sequences[0]` is used. Don't add more.

### 2) Upload leads — correct endpoint is `/leads/add`

```python
body = {
  "campaign_id": campaign_id,
  "leads": [{
    "email":        "lead@example.com",
    "first_name":   "John",
    "last_name":    "Doe",
    "company_name": "Acme Corp",
    "phone":        "+15551234567",
    "custom_variables": {"hookParagraph": "Saw your Strathcona listing — sharp ask."}
  }],
  "skip_if_in_workspace": False,   # see flag semantics below
  "skip_if_in_campaign":  False
}
r = requests.post(f"{API}/leads/add", headers=H, json=body)
# response: {status, leads_uploaded, duplicated_leads, skipped_count, invalid_email_count, created_leads}
```

- Endpoint is `POST /leads/add`. `/leads/bulk-add` returns **404** (the skill docs floating around show this — wrong).
- Suggested chunk size: 100 leads/request (works comfortably under any rate limit and gives smaller failure blast radius).
- For larger lists, paginate and `time.sleep(0.4)` between chunks.

**Dedup flag semantics** — both default to false on Instantly's side; be explicit:

| Flag | True effect | When to use |
|------|-------------|-------------|
| `skip_if_in_workspace` | If lead exists anywhere in workspace, SKIP — don't add to this campaign either. | Almost never. This blocks legitimate re-uploads. |
| `skip_if_in_campaign`  | If lead already in *any other* campaign, SKIP. | When you don't want a lead in two active campaigns at once. |

For fresh campaign uploads where workspace may have prior versions of the same leads: **both flags → False** (the "force-add" path).

### 3) Verify lead binding

`/leads/list` returns leads but its `campaign_id` query param is **silently ignored** — filter client-side via `lead.campaign == cid`. Search a specific email instead:

```python
r = requests.post(f"{API}/leads/list", headers=H,
                  json={"search": email, "limit": 10})
for l in r.json().get("items", []):
    if l["email"].lower() == email.lower() and l.get("campaign") == campaign_id:
        # bound, good
        print(l["payload"])  # custom vars are stored here as flat keys
```

A lead's `campaign` field is `None` if it lives in workspace but isn't attached to any campaign — usually a sign upload failed silently or used wrong endpoint.

### 4) Activate (USER ACTION ONLY)

```bash
curl -X POST "https://api.instantly.ai/api/v2/campaigns/$CID/activate" \
  -H "Authorization: Bearer $INST_KEY"
```

**Never auto-activate cold campaigns.** Hand the curl back; let the user run it. Blast radius (domain reputation, spam complaints) is asymmetric.

## Template variables

### Built-in (from lead fields)

| Variable | Lead field |
|----------|-----------|
| `{{firstName}}` | `first_name` |
| `{{lastName}}`  | `last_name` |
| `{{companyName}}` | `company_name` |
| `{{email}}` | `email` |
| `{{phone}}` | `phone` |

**Note**: variables are **camelCase**, not snake_case. `{{first_name}}` does NOT render.

### Custom variables

Set under `custom_variables` on upload — Instantly stores them flat into `payload`:

```python
"custom_variables": {"hookParagraph": "Saw your ...", "subjectLine": "your Strathcona listing"}
```

Reference in body/subject as **`{{varName}}`** — NOT `{{custom.varName}}` (skill docs floating around show this, wrong, the sanitizer keeps the literal text but it never resolves to anything).

Verify a stored variable on a lead:
```python
lead["payload"].get("hookParagraph")  # flat key, no "custom." prefix
```

### Per-lead update (PATCH)

```python
requests.patch(f"{API}/leads/{lead_id}", headers=H,
               json={"custom_variables": {"subjectLine": "your Strathcona listing"}})
# 200 with merged payload back
```

PATCH merges custom_variables — existing keys are preserved unless overwritten.

## HTML sanitizer — variables must be inside an element

Instantly's PATCH on `/campaigns/{id}` runs a sanitizer that **drops raw text outside of HTML elements**.

```html
<!-- WRONG — {{hookParagraph}} is stray text between <p> tags, gets stripped silently -->
<p>Hi {{firstName}},</p>{{hookParagraph}}<p>I'm Dan…</p>

<!-- RIGHT — wrap in a paragraph or span -->
<p>Hi {{firstName}},</p>
<p>{{hookParagraph}}</p>
<p>I'm Dan…</p>
```

If `hookParagraph` is empty for a lead, the rendered email shows an empty `<p></p>` — a small blank line. Acceptable; Instantly v2 has no conditional template support.

## Step delay — "this step → next step" gap

Instantly's UI label is **"Send next message in N days"**. The `delay` field stores that gap.

For 3-step sequence with 3-day spacing:

```python
[
  {"type":"email","delay":3, ...},   # step 1 fires immediately on activate; step 2 fires +3d
  {"type":"email","delay":3, ...},   # step 3 fires +3d after step 2
  {"type":"email","delay":0, ...}    # last step, value irrelevant — but set to 0 to avoid confusion
]
```

**Bug pattern**: `step1.delay=0` makes step 2 fire **the same minute as step 1** — recipients get hit twice in the same email thread instantly. Always `delay=3` (or whatever cadence) on step 1.

## Schedule timezone — whitelist quirk

Instantly's schedule timezone validates against a whitelist that **rejects** `America/Vancouver` and `America/Los_Angeles`. Use `America/Dawson` (Yukon, fixed UTC-7) for Pacific Time scheduling — fires at the right local hours year-round.

Full memory note: `reference_instantly_timezone_quirk.md` if working in this user's environment.

## Updating campaigns — PATCH replaces, doesn't merge

`PATCH /campaigns/{id}` with `{"sequences": [...]}` **replaces** the entire `sequences` array. Passing a single-step `sequences` overwrites a 3-step setup and silently destroys 2 steps of copy.

**Always GET-then-modify:**

```python
g = requests.get(f"{API}/campaigns/{cid}", headers=H).json()
steps = g["sequences"][0]["steps"]
# mutate `steps` in place — change subject/body/delay
g_steps_new = []
for i, s in enumerate(steps):
    v = s["variants"][0]
    g_steps_new.append({
        "type": "email", "delay": s["delay"],
        "variants": [{"subject": v["subject"], "body": v["body"]}],
    })
requests.patch(f"{API}/campaigns/{cid}", headers=H,
               json={"sequences": [{"steps": g_steps_new}]})
```

The same applies to `campaign_schedule` — pass the whole object, not partial.

## Sending account management

```bash
# list all
curl -s "$API/accounts?limit=100" -H "Authorization: Bearer $INST_KEY"

# get one (path uses EMAIL, not id — even though docs say id)
curl -s "$API/accounts/you@yourdomain.com" -H "Authorization: Bearer $INST_KEY"

# bump daily limit
curl -X PATCH "$API/accounts/you@yourdomain.com" \
  -H "Authorization: Bearer $INST_KEY" -H "Content-Type: application/json" \
  -d '{"daily_limit": 50}'
```

Key fields on the GET response:
- `daily_limit` — campaigns share this across the workspace per sender. Two campaigns on the same sender will split the cap, not double it.
- `stat_warmup_score` — 100 means warmed up and ready. 0-50 = keep warming.
- `warmup_status: 0` means warmup is **inactive** (either not started yet OR completed). Cross-check with `timestamp_warmup_start` + `stat_warmup_score`.

## Common pitfalls

| Symptom | Cause | Fix |
|---------|-------|-----|
| 404 on `POST /leads/bulk-add` | Wrong endpoint (skill docs are wrong) | Use `POST /leads/add` |
| Upload returns "added: N" but campaign is empty | Used `/leads/list` instead of `/leads/add` — `/leads/list` is the *search* endpoint and returns 200 with `items: []` regardless | Switch to `/leads/add`. Verify with `lead.campaign != None` |
| Variable `{{X}}` not interpolating in send | Used `{{custom.X}}` syntax | Use `{{X}}` (flat) — Instantly stores custom vars at top of `payload`, no `custom.` namespace |
| Variable disappears from saved body after PATCH | Variable was raw text outside any HTML element — sanitizer dropped it | Wrap in `<p>{{X}}</p>` or similar |
| Sequence becomes 1 step after PATCH | PATCH `sequences` replaces the whole array | GET first, modify in place, PATCH the full array |
| `DELETE /campaigns/{id}` returns 400 | Instantly disallows DELETE on draft (status=0) campaigns | PATCH the name to `[ARCHIVED] ...` and leave paused/draft. They won't send unless activated. |
| Step 2 fires immediately after step 1 (double-send) | `step1.delay = 0` | Set first step delay to your real cadence (e.g. 3 days). Last step delay can be 0 |
| Schedule validation rejects `America/Vancouver` / `Los_Angeles` | Timezone whitelist | Use `America/Dawson` (UTC-7, no DST) for Pacific Time |
| `verify_emails: true` ignored on `/leads/add` | Not supported in v2 lead upload | Pre-verify with Reoon or similar before upload |
| `POST /emails/send-test` returns 404 | Endpoint doesn't exist in v2 | Preview in the Instantly UI; there is no API test-send |
| `POST /leads/bulk-delete` returns 404 | Endpoint doesn't exist in v2 | `DELETE /leads/{id}` per lead (slow), or leave orphan leads (they don't send unless attached to an active campaign) |
| Campaigns sharing one sender don't split the 50/day cap evenly | Instantly assigns leads round-robin across active campaigns on the sender | If you need strict 25/25, add another verified sender |

## Endpoint reference (validated 2026-05-11)

| Endpoint | Method | Use | Notes |
|----------|--------|-----|-------|
| `/campaigns` | POST | Create campaign | |
| `/campaigns` | GET  | List campaigns | `?status=1` for active |
| `/campaigns/{id}` | GET | Read | |
| `/campaigns/{id}` | PATCH | Update | **Replaces** `sequences` and `campaign_schedule` — GET-then-modify |
| `/campaigns/{id}/activate` | POST | Start sending | User action only |
| `/campaigns/{id}/pause`    | POST | Pause | |
| `/campaigns/{id}` | DELETE | Delete | 400 on drafts; archive via rename instead |
| `/leads/add` | POST | Upload leads | Bind to campaign via `campaign_id` in body |
| `/leads/list` | POST | Search/list (body, not query) | `search` param works; `campaign_id` is ignored, filter client-side |
| `/leads/{id}` | PATCH | Update lead | Merges `custom_variables` |
| `/leads/{id}` | DELETE | Delete lead | |
| `/leads/move` | POST | Move leads between campaigns | |
| `/accounts` | GET | List senders | |
| `/accounts/{email}` | GET / PATCH | Read / update one | Path takes email, not id |

## Lead status codes (from `lead.status`)

- 1 — active
- 2 — paused / not contacted
- 3 — replied
- 4 — bounced
- (more — search Instantly community for full table)

## Campaign status codes (from `campaign.status`)

- 0 — draft
- 1 — active (sending)
- 2 — paused
- 3 — completed (all leads finished)
- 4 — archived

## Doc provenance

Validated against live API by author 2026-05-11. The skill carried inherited mistakes from older v1 docs and a misread "skill template" — all corrected here. When in doubt, hit the endpoint, look at the response, and update this file.
