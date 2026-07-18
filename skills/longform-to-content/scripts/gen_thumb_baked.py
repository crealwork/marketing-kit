"""DEFAULT thumbnail generator — gpt_image_2 bakes faces + logos + Korean TEXT in one shot.

Proven on S03 (8/8 Korean lines rendered perfectly). Verify each output char-for-char
(THUMBNAILS.md SELF-TESTS); regenerate garbled ones with the same model. PIL overlay
(gen_thumb_scenes.py + gen_thumb_text.py) is the FALLBACK, not the default.

Adapt: REF (side-by-side collage of the real people), PROMPTS (per-variant scene + exact
Korean text + style/position). Make a dramatic family AND a family matching the target
channel's feed (study their real thumbnails first).
"""
import subprocess, sys, os, json, urllib.request, re
sys.stdout.reconfigure(encoding="utf-8")

HF = os.path.expandvars(r"%APPDATA%\npm\higgsfield.cmd")   # Windows; else "higgsfield"
OUT = "<WORK>/edit/assets/thumbs"
REF = f"{OUT}/ref_both.png"
INPUT_REF_HOST = "d2ol7oe51mr4n9"   # drop this host from result urls

FACES = ("Use the TWO real people from the reference collage and preserve their exact faces "
         "— LEFT <man desc>, RIGHT <woman desc>. ")
TXT = ("Render every Korean character EXACTLY as written, spelled perfectly, thick bold gothic "
       "sans-serif, crisp and legible. No other text, no watermark. ")

PROMPTS = {
 # dramatic family
 "thumb1": ("YouTube thumbnail, 16:9, high-CTR Korean tech channel. " + FACES +
   "<expressions, background, logos>. At the TOP, a two-line Korean title: first line in yellow "
   "reads exactly \"<LINE1>\", second line in white reads exactly \"<LINE2>\". " + TXT),
 # feed family — warm podcast desk 2-shot, highlight boxes / callouts (match the channel)
 "feed1": ("Photoreal YouTube thumbnail, 16:9, warm Korean podcast channel style, NOT neon. " +
   FACES + "Warm wooden podcast desk, studio mics, bookshelf + plants, natural light, laptop. "
   "At the TOP, first line white bold reads exactly \"<LINE1>\"; second line inside a rounded "
   "YELLOW highlight box with dark text reads exactly \"<LINE2>\". " + TXT),
}

def gen(name, prompt):
    dst = f"{OUT}/baked_{name}.png"
    cmd = [HF, "generate", "create", "gpt_image_2", "--image", REF, "--prompt", prompt,
           "--aspect_ratio", "16:9", "--quality", "high", "--resolution", "2k", "--wait", "--json"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    try:
        j = json.loads(r.stdout)
    except Exception:
        print(f"{name}: parse fail {r.stderr[-200:]}"); return
    urls = []
    def walk(o):
        if isinstance(o, dict):
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
        elif isinstance(o, str) and re.match(r"https://.+\.(png|jpg|jpeg|webp)$", o):
            urls.append(o)
    walk(j)
    res = [u for u in urls if INPUT_REF_HOST not in u] or urls
    if res:
        urllib.request.urlretrieve(res[-1], dst); print(f"{name}: saved")
    else:
        print(f"{name}: no url")

if __name__ == "__main__":
    only = sys.argv[1:]          # regenerate specific names after a verify failure
    for n, p in PROMPTS.items():
        if only and n not in only:
            continue
        gen(n, p)
    print("baked done  — now READ every output and verify Korean text char-for-char")
