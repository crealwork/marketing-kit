"""Hero background via Nano Banana (Gemini image) — explicit switch after
gpt-image-2 billing_hard_limit_reached, reported to user."""
import base64, json, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8")

keys = {}
for l in open(r"C:\Users\Dan\.config\env\.keys.txt", encoding="utf-8", errors="ignore"):
    if "=" in l:
        k, v = l.split("=", 1)
        keys[k.strip()] = v.strip()
KEY = keys.get("GEMINI_API_KEY") or keys.get("GOOGLE_AI_API_KEY")
if not KEY:
    sys.exit("no gemini key")

PROMPT = (
    "Wide 3:2 abstract editorial background for a marketing toolkit banner. "
    "Warm cream paper texture (#FBF8F1) as the base, with elegant flat geometric "
    "marketing motifs scattered sparsely near the edges: a small rising bar chart, "
    "an upward arrow, an envelope, a magnifying glass, a speech bubble — drawn as "
    "minimal ink-navy (#14212B) thin line icons with occasional coral (#E8756A) "
    "accents. Keep the center-left area almost empty for a title overlay. Subtle, "
    "sophisticated, print-design aesthetic, lots of breathing room. "
    "Absolutely no text, no letters, no words anywhere in the image."
)

MODEL = "gemini-2.5-flash-image"
req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
    data=json.dumps({"contents": [{"parts": [{"text": PROMPT}]}]}).encode(),
    headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
try:
    r = json.loads(urllib.request.urlopen(req, timeout=300).read().decode("utf-8"))
    saved = False
    for part in r["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            out = r"C:\Users\Dan\Desktop\ClaudeCodeDeskTop\sundayable\marketing-kit\assets\hero_bg.png"
            open(out, "wb").write(base64.b64decode(part["inlineData"]["data"]))
            print("saved", out)
            saved = True
    if not saved:
        print("no image part:", json.dumps(r)[:400])
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode("utf-8", "ignore")[:400])
