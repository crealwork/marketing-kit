"""Publish: long-form -> YouTube now; 6 shorts -> IG Reels + YouTube, one/day for 6 days.

Verifies every response status. Scheduled posts must return status=scheduled.
"""
import sys, json, os, urllib.request, urllib.error, mimetypes
sys.stdout.reconfigure(encoding="utf-8")

WORK = "<absolute path to the project work dir>"
# Read the key from the user's environment or secure keys file. NEVER hardcode it,
# NEVER print it, NEVER copy it into a skill/handoff document.
KEY = os.environ.get("ZERNIO_API_KEY") or "<resolve from user's keys file>"
BASE = "https://zernio.com/api/v1"
YT = "<youtube accountId — discover via GET /v1/accounts>"
IG = "<instagram accountId — discover via GET /v1/accounts>"


def call(method, path, body=None, timeout=60):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{BASE}{path}", data=data, method=method,
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} {path}: {e.read().decode('utf-8','ignore')[:500]}")


def upload(path):
    name = os.path.basename(path)
    ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
    pre = call("POST", "/media/presign", {"filename": name, "contentType": ctype})
    up, pub = pre["uploadUrl"], pre["publicUrl"]
    data = open(path, "rb").read()
    req = urllib.request.Request(up, data=data, method="PUT",
                                 headers={"Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=1800) as r:
        assert r.status in (200, 201), r.status
    print(f"  uploaded {name} ({len(data)/1e6:.0f} MB)")
    return pub


DESC = """AI 에이전트가 실제 비즈니스에서 어떻게 일하는지, 사례로 정리한 웨비나 풀버전입니다.
전화 예약 자동화부터 1인 기업의 에이전트 15개 운영, 그리고 오늘 바로 시작할 수 있는 5단계 플레이북까지.

챕터
{chapters}

Sundayable — AI 마케팅 웨비나는 매주 목요일에 열립니다.
https://www.sundayable.com"""

SHORTS = [
    dict(f="short1-99-percent-give-up.mp4", day="2026-07-12",
         title="99%는 여기서 포기합니다 — AI를 잘 쓰는 1%의 차이",
         cap="AI로 뭘 만들다 두세 번 막히면 다들 거기서 접습니다. 끝까지 파고드는 1%가 결국 자동화를 완성해요. 매주 목요일, Sundayable AI 마케팅 웨비나. #AI에이전트 #AI자동화 #스몰비즈니스마케팅 #Sundayable"),
    dict(f="short4-skip-nocode-tools.mp4", day="2026-07-13",
         title="노코드 툴, 배우지 마세요",
         cap="메이크닷컴, 재피어, n8n… 배우는 시간이 더 아깝습니다. 코딩 에이전트한테 말로 시키세요. #노코드 #AI자동화 #AI에이전트 #Sundayable"),
    dict(f="short5-claude-vs-chatgpt-20usd.mp4", day="2026-07-14",
         title="$20라면 클로드 vs 챗GPT, 뭘 살까",
         cap="글쓰기와 마케팅이 목적이면 클로드, 두루두루 쓰려면 챗GPT. 이미 익숙한 걸 계속 쓰는 게 정답입니다. #챗GPT #클로드 #AI툴추천 #Sundayable"),
    dict(f="short6-ai-lies-workflow-problem.mp4", day="2026-07-15",
         title="AI는 거짓말을 합니다 — 그래도 자동화하는 이유",
         cap="할루시네이션 때문에 자동화를 포기해야 할까요? 사람도 실수하고 거짓말합니다. 문제는 AI가 아니라 워크플로우예요. #AI #할루시네이션 #AI자동화 #Sundayable"),
    dict(f="short3-93-percent-never-call-back.mp4", day="2026-07-16",
         title="고객 93%는 다시 전화하지 않습니다",
         cap="부재중 전화 한 통이 매출을 잃는 순간입니다. 고객은 30분 안에 답이 없으면 다른 업체로 갑니다. #스몰비즈니스 #고객관리 #AI자동화 #Sundayable"),
    dict(f="short2-document-or-no-automation.mp4", day="2026-07-17",
         title="글로 못 쓰면 자동화도 없습니다",
         cap="머릿속에만 있는 일은 자동화할 수 없습니다. 글로 정의하는 순간 시작돼요. #워크플로우 #AI자동화 #문서화 #Sundayable"),
]

# ---------- long-form ----------
print("uploading long-form video + thumbnail...")
video_url = upload(f"{WORK}/final/webinar-s02-full-1080p.mp4")
thumb_url = upload(f"{WORK}/final/thumbs/thumb1.png")
chapters = open(f"{WORK}/final/webinar-s02-chapters.txt", encoding="utf-8").read().strip()

res = call("POST", "/posts", {
    "content": DESC.format(chapters=chapters),
    "mediaItems": [{"type": "video", "url": video_url, "thumbnail": thumb_url}],
    "platforms": [{
        "platform": "youtube", "accountId": YT,
        "platformSpecificData": {
            "title": "AI 에이전트, 99%는 여기서 포기합니다 | 실전 사례부터 시작 플레이북까지 (풀 웨비나)",
            "visibility": "public", "madeForKids": False,
        },
    }],
    "publishNow": True,
})
p = res.get("post", res)
print(f"LONG-FORM: id={p.get('_id')} status={p.get('status')}")

# ---------- shorts, one per day 17:00 PT (=00:00 UTC next day) ----------
for s in SHORTS:
    url = upload(f"{WORK}/final/shorts/{s['f']}")
    res = call("POST", "/posts", {
        "content": s["cap"],
        "mediaItems": [{"type": "video", "url": url}],
        "platforms": [
            {"platform": "instagram", "accountId": IG,
             "platformSpecificData": {"contentType": "reels", "shareToFeed": True}},
            {"platform": "youtube", "accountId": YT,
             "platformSpecificData": {"title": s["title"], "visibility": "public",
                                      "madeForKids": False}},
        ],
        "scheduledFor": f"{s['day']}T00:00:00Z",
        "timezone": "UTC",
    })
    p = res.get("post", res)
    status = p.get("status")
    print(f"SHORT {s['f']}: id={p.get('_id')} status={status} for={p.get('scheduledFor')}")
    assert status == "scheduled", f"NOT scheduled: {json.dumps(p, ensure_ascii=False)[:400]}"

print("ALL DONE")
