---
name: close-crm
description: Use when the user asks to update, search, create, or manage Close.com CRM data — leads, contacts, opportunities, activities, notes, tasks. Trigger on mentions of Close, CRM, 리드, 딜, 파이프라인, or sales pipeline updates.
---

# Close CRM

Manage Close.com CRM via REST API.

## Authentication

```bash
curl https://api.close.com/api/v1/{endpoint} -u "$CLOSE_API_KEY:"
```

- **API Key**: env var `CLOSE_API_KEY` (Close → Settings → API Keys; never hardcode)
- **Method**: HTTP Basic Auth (API key = username, password = empty)
- **Base URL**: `https://api.close.com/api/v1/`

## Quick Reference

| Operation | Method | Endpoint |
|-----------|--------|----------|
| List leads | GET | `/lead/?_limit=100` |
| Get lead | GET | `/lead/{id}/` |
| Create lead | POST | `/lead/` |
| Update lead | PUT | `/lead/{id}/` |
| Delete lead | DELETE | `/lead/{id}/` |
| Search leads/contacts | POST | `/data/search/` |
| List contacts | GET | `/contact/?lead_id={id}` |
| Create contact | POST | `/contact/` |
| Update contact | PUT | `/contact/{id}/` |
| List opportunities | GET | `/opportunity/?lead_id={id}` |
| Create opportunity | POST | `/opportunity/` |
| Update opportunity | PUT | `/opportunity/{id}/` |
| List activities | GET | `/activity/?lead_id={id}` |
| Create note | POST | `/activity/note/` |
| Create task | POST | `/task/` |
| Lead statuses | GET | `/status/lead/` |
| Opportunity statuses | GET | `/status/opportunity/` |
| Custom fields (lead) | GET | `/custom_field/lead/` |
| Custom fields (contact) | GET | `/custom_field/contact/` |

## CRM Structure

Orgs differ — discover the live structure before writing. Don't trust cached status IDs:
```bash
curl https://api.close.com/api/v1/pipeline/ -u "$CLOSE_API_KEY:"        # pipelines + their statuses
curl https://api.close.com/api/v1/status/lead/ -u "$CLOSE_API_KEY:"    # lead statuses
```

**Trap: `status_label` values repeat across pipelines** (e.g. "New Lead" exists in several).
Setting an opportunity by label can land it in the wrong pipeline. Always resolve the
`status_id` from the intended pipeline's status list, then write with `status_id`.

## Common Operations

### Create a lead with contact
```bash
curl -X POST https://api.close.com/api/v1/lead/ \
  -u "$CLOSE_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Company Name",
    "status_label": "Potential",
    "contacts": [{
      "name": "John Doe",
      "title": "CEO",
      "emails": [{"email": "john@example.com", "type": "office"}],
      "phones": [{"phone": "+16041234567", "type": "mobile"}]
    }]
  }'
```

### Update lead status
```bash
curl -X PUT https://api.close.com/api/v1/lead/{lead_id}/ \
  -u "$CLOSE_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{"status_label": "Qualified"}'
```

### Search leads by name
```bash
curl -X POST https://api.close.com/api/v1/data/search/ \
  -u "$CLOSE_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "type": "and",
      "queries": [
        {"type": "object_type", "object_type": "lead"},
        {"type": "field_condition",
         "field": {"type": "regular_field", "object_type": "lead", "field_name": "lead_name"},
         "condition": {"type": "text", "mode": "full_words", "value": "SEARCH_TERM"}}
      ]
    }
  }'
```

### Add a note to a lead
```bash
curl -X POST https://api.close.com/api/v1/activity/note/ \
  -u "$CLOSE_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "lead_id": "lead_xxx",
    "note": "Note content here"
  }'
```

### Create an opportunity
```bash
curl -X POST https://api.close.com/api/v1/opportunity/ \
  -u "$CLOSE_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "lead_id": "lead_xxx",
    "status_id": "stat_U1Ym0nS...",
    "value": 5000,
    "value_period": "one_time"
  }'
```

## Pagination

- `_limit`: results per page (default 100, max 200)
- `_skip`: offset for pagination
- Response includes `has_more` boolean

```bash
# Page 1
curl "https://api.close.com/api/v1/lead/?_limit=100&_skip=0" -u "$CLOSE_API_KEY:"
# Page 2
curl "https://api.close.com/api/v1/lead/?_limit=100&_skip=100" -u "$CLOSE_API_KEY:"
```

## Custom Fields

Set via `custom.{field_id}` in request body. List available fields first:
```bash
curl https://api.close.com/api/v1/custom_field/lead/ -u "$CLOSE_API_KEY:"
```

Multi-value fields support `.add` / `.remove` suffixes.

## Important Notes

- **Rate limits**: 100 requests/10 seconds per org
- Load the API key from the environment at runtime — never write it into files
- Use `_fields` query param to limit response size: `?_fields=id,display_name,status_label`
- **Use `status_id` not `status_label`** when updating lead status — `status_label` only matches default pipeline
- **Use Python `json.dumps()`** for note/activity creation — curl with special characters causes JSON parse errors
- Always **search before creating** to avoid duplicate leads
