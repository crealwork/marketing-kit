# PUBLISHING — Gate 4: Zernio setup + posting (user-gated)

**The agent's ceiling is staged/scheduled posts with explicit user approval per
destination. "편집해줘" is not publish approval; "올려줘/스케줄해줘" is.**

## If the user has NO Zernio account — onboarding script (give verbatim)

1. Sign up: https://zernio.com (free tier covers scheduling basics).
2. Connect platforms: Dashboard → Accounts → Connect → authorize YouTube (the Google
   account owning the channel) and Instagram (must be a Business/Creator account linked
   to a Facebook Page — personal IG accounts cannot API-post; convert in IG app:
   Settings → Account type and tools → Switch to professional account).
3. Create an API key: Dashboard → Settings → API Keys → Create.
4. Store it where the agent can read it, e.g. line `ZERNIO_API_KEY=sk_...` in the
   user's keys file (never paste keys into chat or commit them).
5. Agent verifies: `GET /v1/profiles` returns 200 and `GET /v1/accounts` lists the
   connected platforms with account IDs. Record the accountIds in the project notes.

No Zernio at all and the user declines? Fall back to manual instructions: YouTube
Studio upload (studio.youtube.com → Create → set title/desc/chapters/thumbnail/
visibility) + Meta Business Suite for reels scheduling — and still prepare all copy
(titles, descriptions, captions, hashtags) as a paste-ready file.

## API facts (verified 2026-07-10)

- Base `https://zernio.com/api/v1`, header `Authorization: Bearer $ZERNIO_API_KEY`.
- All calls: Python urllib + utf-8 decode (curl+cp1252 caused a real double-post).
- Media: `POST /media/presign {filename, contentType}` → `{uploadUrl, publicUrl}` →
  PUT the bytes → use publicUrl in mediaItems.
- Create post: `POST /posts` with `content`, `mediaItems`, `platforms[]`,
  and EITHER `publishNow: true` OR `scheduledFor: <ISO-8601 UTC>` (+`timezone`).
  Response `post.status` ∈ scheduled|published|draft|pending — ASSERT the expected one.
- YouTube platformSpecificData: `{title (≤100), visibility, madeForKids}`;
  custom thumbnail = `mediaItems[].thumbnail` URL (<2MB, ≥640px; regular videos only —
  Shorts cannot take custom thumbnails). ≤3-min vertical video auto-classifies as a Short.
- Instagram platformSpecificData: `{contentType: "reels", shareToFeed: true}`;
  reels: 9:16, 3–90s, ≤300MB, H.264.
- One post may target multiple platforms — use a single post per short with
  `platforms: [instagram, youtube]` so both fire at the same scheduledFor.
- Rescheduling / "publish now": update with `PUT /posts/{id}` (PATCH returns 405).
  To fire immediately, PUT `scheduledFor` = now + 2 minutes (past times may be
  rejected), then poll GET every 30s until every platform shows `published` and
  report the platformPostUrls. Instagram publishes 1–3 min behind YouTube — that lag
  is normal, not a failure.

## MANDATORY safety rules (each one is a real incident)

1. **Timeout ≠ failure.** Large-video POSTs can exceed client timeouts while the server
   succeeds. On ANY timeout/ambiguous error: `GET /v1/posts?limit=10`, look for your
   content, and only retry if it is genuinely absent. Blind retry = duplicate upload.
2. Use timeout ≥ 180s for posts carrying video; ≥ 1800s for the PUT of a long video.
3. Scheduled posts: assert `status == "scheduled"` in the response; a silent
   `published` means it went live NOW — tell the user immediately, don't hide it.
4. Verify the long-form after publish: GET the post until platform status =
   `published`, then report the `platformPostUrl` to the user.
5. Custom thumbnail application is not API-verifiable — tell the user to eyeball the
   watch page (fallback: set it in YouTube Studio manually).

## Copy standards for posts

- Long-form description: 2-sentence summary + full chapter list + one link. No emoji
  walls, no AI-tell phrasing, no fabricated claims.
- Shorts: title ≤ 60 chars restating the hook; caption 1–2 sentences + ≤5 hashtags.
- Schedule cadence default: one short/day at a fixed local prime hour; lead with the
  short that matches the long-form thumbnail claim.
