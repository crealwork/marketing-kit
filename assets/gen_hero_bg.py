"""Hero background via gpt-image-2 (image-gen skill policy: no fallback)."""
import base64, json, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8")

KEY = next(l.split("=", 1)[1].strip()
           for l in open(r"C:\Users\Dan\.config\env\.keys.txt",
                         encoding="utf-8", errors="ignore")
           if l.startswith("OPENAI_API_KEY="))

PROMPT = (
    "Wide abstract editorial background for a marketing toolkit banner. "
    "Warm cream paper texture (#FBF8F1) as the base, with elegant flat geometric "
    "marketing motifs scattered sparsely: a small rising bar chart, an upward arrow, "
    "an envelope, a magnifying glass, a speech bubble — drawn as minimal ink-navy "
    "(#14212B) line icons with occasional coral (#E8756A) accents. Generous empty "
    "space in the center-left for a title to be overlaid later. Subtle, sophisticated, "
    "print-design aesthetic, thin lines, lots of breathing room. Absolutely no text, "
    "no letters, no words anywhere."
)

req = urllib.request.Request(
    "https://api.openai.com/v1/images/generations",
    data=json.dumps({"model": "gpt-image-2", "prompt": PROMPT,
                     "size": "1536x1024", "quality": "high"}).encode(),
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
try:
    r = json.loads(urllib.request.urlopen(req, timeout=300).read().decode("utf-8"))
    out = r"C:\Users\Dan\Desktop\ClaudeCodeDeskTop\sundayable\marketing-kit\assets\hero_bg.png"
    open(out, "wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    print("saved", out)
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode("utf-8", "ignore")[:400])
