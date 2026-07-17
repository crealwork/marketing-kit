# YOUTUBE — packaging, metadata, cadence, verification (all mandatory)

Packaging = thumbnail + title + first 5 seconds, designed as ONE unit. A viewer clicks
the thumbnail's claim, the title restates it, and the cold open's first spoken line
repays it. Break any leg of that triangle and CTR or retention dies.

## 1. The packaging triangle (blocking rule)

- Thumbnail claim (THUMBNAILS.md) == title's hook == first spoken line of the video.
- If the best thumbnail concept changes late, REORDER the cold open to match
  (concat order + caption/SRT/chapter regen + one burn pass — cheap). Never ship
  a mismatch "because the render is done".

## 2. Titles (long-form)

- ≤ 100 chars accepted, but the FIRST ~60 chars must carry the whole hook
  (search/suggested truncate the rest).
- Structure: `[hook claim] | [searchable descriptor] ([format tag])`
  e.g. `AI 에이전트, 99%는 여기서 포기합니다 | 실전 사례부터 시작 플레이북까지 (풀 웨비나)`.
- MUST contain: the thumbnail's number/claim + one search keyword the target viewer
  would type. MUST NOT: ALL-CAPS runs > 1 word, emoji, fabricated numbers, claims the
  video doesn't deliver (mismatch trains bounce and kills suggested reach).
- Write 3 candidates, pick by: (a) triangle match, (b) keyword presence, (c) reads
  naturally aloud. No AI-tell phrasing.

## 3. Descriptions (long-form)

- First 125 chars = the mobile fold: 1-sentence value promise (no links, no hashtags
  in the fold — they truncate the promise).
- Full structure, in order:
  1. 2–3 sentence summary (what the viewer walks away with — concrete nouns/numbers)
  2. blank line, then `챕터`/`Chapters` + the chapter list
  3. one primary link (site or signup) + recurring-schedule line if a series
  4. ≤ 3 hashtags (more dilutes; YouTube shows only 3 above the title)
- ≤ 5,000 chars. No emoji walls. Same language as the video.

## 4. Chapters (format is strict — YouTube silently rejects violations)

- Plain lines `M:SS Label` (or H:MM:SS past an hour), FIRST line must be `0:00`,
  minimum 3 entries, strictly ascending, each segment ≥ 10s.
- Labels ≤ 20 chars, content-descriptive, no clickbait, numbered parts match the
  actual on-screen sections.
- Compute timestamps through the edit's piece table (CAPTIONS.md §2) — never from the
  source timeline. Recompute after ANY re-cut.
- VERIFY on the live watch page: the progress bar shows chapter segments. If not,
  the format broke one of the rules above.

## 5. Shorts metadata + strategy

- Auto-classification: ≤ 3 min AND 9:16 → Short. No custom thumbnails on Shorts —
  the FIRST FRAME is the thumbnail, so shorts must open on the designed layout with
  the hook title visible (our template does; never open on a black/transition frame).
- Title ≤ 60 chars restating the short's hook; `#shorts` tag is unnecessary.
- Description: 1–2 sentences + ≤ 5 hashtags (shared with the IG caption is fine).
- Each short's last frame = endcard with brand + series line (drives channel visit).
- Ordering strategy: Short #1 = the long-form thumbnail's claim (compounds the same
  hook), then alternate contrarian / searchable / stat hooks. Spread source moments
  across the runtime so the series doesn't feel like one chapter.

## 6. Cadence + scheduling

- Long-form: publish at the audience's prime hour (evening local for consumer,
  morning commute for B2B). Series → same weekday+hour every week, say it in the
  outro and description.
- Shorts: exactly one per day at a fixed hour (algorithm + habit). Convert the chosen
  local hour to UTC for `scheduledFor`; state the local-time table to the user for
  approval BEFORE scheduling.
- Never dump all shorts at once; never leave >2 gap days inside the series window.

## 7. CTR research floor (encode, don't re-derive)

Numbers from 2025–26 CTR studies (Ampifire, ClickyApps, Vidooly, MrBeast analyses):
- Real face with exaggerated emotion: +25–30% CTR vs object-only. Face ≥ 15% of canvas
  area (we target 25–40%).
- Thumbnail text < 12 chars beats text-heavy. One focal point (≤ 3 elements).
- Contrasting colors ≈ +30% CTR. 80/20 saturation (subject pops).
- Average channel CTR 3–4%; top performers 5–10% via systematic A/B.
- Always verify at 168x94 px — the actual browse size.

## 8. Post-publish verification (blocking, do every item)

1. GET the post until platform status = `published`; report `platformPostUrl`.
2. Open the watch page mentally-checklist: custom thumbnail applied? (not API-verifiable —
   if the auto frame shows, instruct the user: Studio → video → thumbnail → upload file)
3. Chapters render on the seek bar.
4. Title/description characters intact (no encoding damage).
5. Playback spot-check instruction for the user: 0:00, one mid chapter, last 30s.
6. Scheduled shorts: re-list all posts, confirm every one is `scheduled` with the
   agreed timestamp; give the user the full table (date, hook, platforms, post id).

## 9. The 48–72h analytics loop (MANDATORY: set the reminder at publish time)

At publish time, SCHEDULE a +72h reminder to the user through whatever channel they
already use (cloud routine / cron / OS task scheduler / calendar event / messenger
bot). Do not rely on anyone remembering. The reminder message must contain:
(a) the video URL + analytics dashboard link, (b) the CTR<3% → swap-to-alternate-
thumbnail instruction WITH the alternates' file paths, (c) first-30s drop-off check,
(d) shorts performance comparison → next episode's thumbnail angle.
If no scheduling channel exists, hand the user the checklist and an explicit date.

- Check CTR + average view duration after 48–72h.
- CTR < 3% → swap to an alternate thumbnail (we always ship 3 candidates; YouTube's
  built-in Test & Compare can also A/B them).
- Big drop-off inside the first 30s → the cold open over-promised; note it for the
  next episode's packaging (do not silently re-edit a live video).
- Best-performing short's hook = leading candidate for next episode's thumbnail angle.
