"""Screenshot the 36 demo frames with headless Edge and assemble the 6 README GIFs."""
import pathlib, shutil, subprocess, sys, tempfile, time

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LANGS = ["en", "zh", "es", "pt", "ja", "ko"]
N = 6

from PIL import Image

def shoot(html, png):
    for attempt in range(4):
        png.unlink(missing_ok=True)
        tmp = tempfile.mkdtemp(prefix="edge_gif_")
        try:
            subprocess.run(
                [EDGE, "--headless", "--disable-gpu", f"--screenshot={png}",
                 "--window-size=800,420", "--virtual-time-budget=15000",
                 "--hide-scrollbars", f"--user-data-dir={tmp}", str(html)],
                capture_output=True, timeout=90)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        if png.exists() and png.stat().st_size > 5000:
            return
        time.sleep(1)
    raise SystemExit(f"screenshot failed: {html.name}")

for lang in LANGS:
    frames = []
    for i in range(N):
        html = HERE / f"frame_{lang}_{i}.html"
        png = HERE / f"frame_{lang}_{i}.png"
        shoot(html, png)
        frames.append(Image.open(png).convert("P", palette=Image.ADAPTIVE, colors=128))
    out = HERE / (f"demo.{lang}.gif")
    frames[0].save(out, save_all=True, append_images=frames[1:],
                   duration=1400, loop=0, optimize=True)
    print(f"{out.name}: {out.stat().st_size // 1024} KB")

for p in HERE.glob("frame_*_*.png"):
    p.unlink()
for p in HERE.glob("frame_*_*.html"):
    p.unlink()
print("done")
