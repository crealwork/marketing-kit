"""PREFERRED real-face thumbnails: rembg CUTOUTS as the gpt_image_2 reference, model bakes
the WHOLE thumbnail (scene + Korean text + logos) around the real faces.

Cutout reference (clean subject on white) preserves the real current look better than the
original messy-background photo, and the model composites + renders text cohesively —
better than a PIL paste. VERIFY every Korean line char-for-char; regenerate garbled.
Fill in the constants + PROMPTS for your project (paths marked <WORK>).
"""
import subprocess, sys, os, json, urllib.request, re
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
import numpy as np

HF = os.path.expandvars(r"%APPDATA%\npm\higgsfield.cmd")
R = r"<WORK>/edit\assets\thumbs\real"
OUT = r"<WORK>/edit\assets\thumbs"
REF = rf"{R}\ref_cut.png"

# ---- build clean cutout collage reference (burned subtitle killed) ----
def clean_cut(name, kill_below=None):
    im = Image.open(rf"{R}\{name}.png").convert("RGBA")
    if kill_below is not None:
        a = np.array(im); a[kill_below:, :, 3] = 0; im = Image.fromarray(a, "RGBA")
    return im.crop(im.getchannel("A").getbbox())

if not os.path.exists(REF):
    dan = clean_cut("dan_real_cut", kill_below=676)
    kay = clean_cut("kay_real_cut")
    H = 1100
    fit = lambda im: im.resize((int(im.width * H / im.height), H), Image.LANCZOS)
    dan, kay = fit(dan), fit(kay)
    ref = Image.new("RGBA", (dan.width + kay.width + 80, H), (255, 255, 255, 255))
    ref.alpha_composite(dan, (0, 0)); ref.alpha_composite(kay, (dan.width + 80, 0))
    ref.convert("RGB").save(REF)
    print("ref_cut.png", ref.size)

FACES = ("Use the TWO real people from the reference cutouts and preserve their EXACT faces and "
         "likeness — LEFT a Korean man in a white shirt, RIGHT a Korean woman with a chin-length "
         "dark bob and round glasses. ")
TXT = ("Render every Korean character EXACTLY as written, spelled perfectly, thick bold gothic "
       "sans-serif, crisp and legible. No other text, no watermark. ")
DRAMA = ("YouTube thumbnail, 16:9, high-CTR Korean tech channel. " + FACES +
         "Chest-up, dramatic bright rim lighting, vivid, extreme contrast. ")
FEED = ("Photoreal YouTube thumbnail, 16:9, warm authentic Korean podcast channel style, NOT neon. "
        + FACES + "Warm wooden podcast desk with studio microphones, cozy bookshelf + plants softly "
        "blurred behind, natural warm lighting, a laptop. Editorial documentary look. ")

PROMPTS = {
 "real1-disbelief": DRAMA + ("The man confident, the woman shocked and wide-eyed. Two glowing app icons "
   "between them: OpenAI blossom + Anthropic Claude sunburst. Burgundy-to-orange gradient background. "
   "At the TOP, first line yellow reads exactly \"AI가 유튜브 편집을?\", second line white reads exactly "
   "\"진짜 믿기지가 않네\". " + TXT),
 "real2-vs": DRAMA + ("Split-screen face-off, the man on a teal LEFT with a glowing OpenAI blossom logo, "
   "the woman on an orange RIGHT with a glowing Claude sunburst logo, a bright center light divider and "
   "a huge white \"VS\". Across the BOTTOM a bold white line reads exactly \"코덱스 vs 클로드, 승자는?\". " + TXT),
 "real3-nogada": FEED + ("The man points at a glowing laptop, the woman amazed. At the TOP, first line "
   "white bold reads exactly \"AI한테 편집 맡겼더니\"; second line inside a rounded YELLOW highlight box "
   "with dark text reads exactly \"'노가다'가 사라졌다\". " + TXT),
 "real4-clean": DRAMA + ("Both confident, premium clean cream studio background with a soft burgundy accent, "
   "large glowing OpenAI blossom and Claude sunburst logos. At the TOP, first line dark ink reads exactly "
   "\"유튜브 편집 자동화\", second line inside a rounded BURGUNDY box with white text reads exactly "
   "\"이걸로 끝냅니다\". " + TXT),
 "real5-instead": DRAMA + ("The woman points at the viewer shocked, the man confident behind, saturated "
   "teal-to-blue tech gradient, glowing OpenAI and Claude icons. On the LEFT a giant bold white three-line "
   "title reads exactly \"이 영상,\" then \"전부 AI가\" (with \"AI가\" in yellow) then \"편집했어요\". " + TXT),
}

def gen(name, prompt):
    dst = rf"{OUT}\baked_{name}.png"
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
    res = [u for u in urls if "d2ol7oe51mr4n9" not in u] or urls
    if res:
        urllib.request.urlretrieve(res[-1], dst); print(f"{name}: saved")
    else:
        print(f"{name}: no url")

if __name__ == "__main__":
    only = sys.argv[1:]
    for n, p in PROMPTS.items():
        if only and n not in only:
            continue
        gen(n, p)
    print("real baked done — READ each, verify Korean text")
