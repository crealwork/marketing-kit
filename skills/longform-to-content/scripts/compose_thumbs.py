"""Compose 3 YouTube thumbnails: gpt-image-2/Nano Banana API base + PIL Korean hook overlay."""
import sys, json, re, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageFont

WORK = "<WORK>"
SERIF = "<FONTS_DIR>/NotoSerifKR-VF.ttf"
SANS = "<FONTS_DIR>/InstrumentSans-SemiBold.ttf"

CREAM = (250, 247, 242)
INK = (28, 25, 23)
BURGUNDY = (114, 10, 34)
GRAY = (120, 114, 108)

THUMBS = [
    dict(n=1, lines=["이 웨비나,", "|AI가| 만들었습니다"], max_w=700),
    dict(n=2, lines=["|99%|는 여기서", "포기합니다"], max_w=700),
    dict(n=3, lines=["$20라면,", "|클로드| vs 챗GPT"], max_w=530),  # keep clear of storefront awning
]

def serif(size, weight=700):
    f = ImageFont.truetype(SERIF, size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f

def url_from_json(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    urls = re.findall(r"https://[^\s\"']+", raw)
    urls = [u.rstrip(",}]") for u in urls if re.search(r"\.(png|jpe?g|webp)", u) or "media" in u]
    if not urls:
        raise SystemExit(f"no result URL in {path}:\n{raw[:400]}")
    return urls[0]

def spaced_text(d, xy, text, font, fill, tracking=4):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking

def fitted_size(d, lines, max_w=700, cap=120, floor=68):
    size = cap
    while size > floor:
        f = serif(size, 700)
        if all(d.textlength(l.replace("|", ""), font=f) <= max_w for l in lines):
            break
        size -= 4
    return size

def draw_hook(d, lines, size):
    f = serif(size, 700)
    lh = int(size * 1.32)
    y = 170
    for line in lines:
        x = 64
        for part in re.split(r"(\|[^|]+\|)", line):
            t = part.strip("|")
            color = BURGUNDY if part.startswith("|") else INK
            d.text((x, y), t, font=f, fill=color)
            x += d.textlength(t, font=f)
        y += lh
    return y

for t in THUMBS:
    url = url_from_json(f"{WORK}/edit/thumbs_work/t{t['n']}.json")
    raw_path = f"{WORK}/edit/thumbs_work/base{t['n']}.png"
    urllib.request.urlretrieve(url, raw_path)
    img = Image.open(raw_path).convert("RGB").resize((1280, 720), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    spaced_text(d, (64, 106), "SUNDAYABLE WEBINAR — SESSION 02",
                ImageFont.truetype(SANS, 26), GRAY, tracking=4)
    size = fitted_size(d, t["lines"], max_w=t.get("max_w", 700))
    draw_hook(d, t["lines"], size)
    d.text((64, 636), "Sundayable.", font=serif(36, 600), fill=INK)
    out = f"{WORK}/final/thumbs/thumb{t['n']}.png"
    img.save(out)
    # legibility preview at YouTube list size
    img.resize((168, 95), Image.LANCZOS).save(f"{WORK}/edit/verify/thumb{t['n']}_tiny.png")
    print(f"thumb{t['n']}: hook {size}px -> {out}")
print("thumbnails composed")
