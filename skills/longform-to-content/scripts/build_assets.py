"""Build static assets: PIP rounded mask + shadow plate, intro/outro cards."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageFilter
import subprocess, os

EDIT = "<WORK>/edit"
SRC = "<WORK>/recording.mp4"
os.makedirs(f"{EDIT}/assets", exist_ok=True)

PIP_W, PIP_H, PIP_R = 432, 243, 14
PIP_X, PIP_Y = 1460, 809  # bottom-right, 28px margin

# --- rounded-rect alpha mask (grayscale, white=opaque) ---
mask = Image.new("L", (PIP_W, PIP_H), 0)
d = ImageDraw.Draw(mask)
d.rounded_rectangle([0, 0, PIP_W - 1, PIP_H - 1], radius=PIP_R, fill=255)
mask.save(f"{EDIT}/assets/pip_mask.png")

# --- full-canvas shadow plate under the PIP ---
plate = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
sh = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
ds = ImageDraw.Draw(sh)
ds.rounded_rectangle([PIP_X + 4, PIP_Y + 10, PIP_X + PIP_W + 4, PIP_Y + PIP_H + 10],
                     radius=PIP_R, fill=(10, 8, 8, 150))
sh = sh.filter(ImageFilter.GaussianBlur(14))
plate = Image.alpha_composite(plate, sh)
plate.save(f"{EDIT}/assets/pip_shadow.png")

# --- intro / outro slide stills (crop share region, upscale to 1920x1080) ---
def grab(t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", SRC,
                    "-frames:v", "1", "-y", out], check=True)

grab(300, f"{EDIT}/assets/_intro_raw.png")
grab(4505, f"{EDIT}/assets/_outro_raw.png")

def slide_card(raw, out, erase=None):
    img = Image.open(raw).convert("RGB").crop((0, 135, 1440, 945))
    if erase:
        # sample bg color just left of the erase box, paint over
        x0, y0, x1, y1 = erase
        bg = img.getpixel((x0 - 12, (y0 + y1) // 2))
        ImageDraw.Draw(img).rectangle(erase, fill=bg)
    img = img.resize((1920, 1080), Image.LANCZOS)
    img.save(out)

# erase "6:30 PM PT에 시작합니다." line on the title slide (coords in 1440x810 crop space)
slide_card(f"{EDIT}/assets/_intro_raw.png", f"{EDIT}/assets/intro_card.png",
           erase=(80, 560, 380, 612))
slide_card(f"{EDIT}/assets/_outro_raw.png", f"{EDIT}/assets/outro_card.png")
print("assets done")
