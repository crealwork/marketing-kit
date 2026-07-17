"""Measure the recording's layout geometry (PIPELINE.md §2) — run BEFORE any render.

Extracts frames at 3 spread timestamps, finds bright-region runs per axis, and
reports the content-share crop + webcam tile crop. The three frames must agree
within ±4px or the script exits nonzero (layout changes mid-recording → split
geometry per section).

Usage: PYTHONUTF8=1 python measure_layout.py <recording.mp4> [t1 t2 t3]
"""
import sys, subprocess, tempfile, os
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
import numpy as np


def grab(video, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video,
                    "-frames:v", "1", "-y", out], check=True)


def runs(arr, minv, min_len=20):
    out, inrun, start = [], False, 0
    for i, v in enumerate(arr):
        if v > minv and not inrun:
            start, inrun = i, True
        elif v <= minv and inrun:
            out.append((start, i)); inrun = False
    if inrun:
        out.append((start, len(arr)))
    return [(a, b) for a, b in out if b - a > min_len]


def measure(path, thresh=60):
    img = np.asarray(Image.open(path).convert("L"))
    bright = img > thresh
    col = runs(bright.sum(axis=0), 100)
    row = runs(bright.sum(axis=1), 100)
    if not col or not row:
        return None
    # largest column run = content share; anything to its right = webcam strip
    share = max(col, key=lambda r: r[1] - r[0])
    x0, x1 = share
    y0, y1 = max(row, key=lambda r: r[1] - r[0])
    cam = None
    strip = img[:, x1 + 2:] if x1 + 2 < img.shape[1] else None
    if strip is not None and strip.size and (strip > 25).sum() > 500:
        ys = np.where((strip > 25).sum(axis=1) > 50)[0]
        if len(ys):
            cam = (x1 + 2, int(ys.min()), img.shape[1] - (x1 + 2), int(ys.max() - ys.min()))
    return {"share": (x0, y0, x1 - x0, y1 - y0), "cam": cam}


def main():
    video = sys.argv[1]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration", "-of", "csv=p=0", video],
                               capture_output=True, text=True).stdout)
    ts = [float(x) for x in sys.argv[2:5]] or [dur * 0.3, dur * 0.55, dur * 0.8]
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, t in enumerate(ts):
            f = os.path.join(tmp, f"m{i}.png")
            grab(video, t, f)
            m = measure(f)
            print(f"t={t:7.1f}s  share={m['share'] if m else None}  cam={m['cam'] if m else None}")
            results.append(m)
    shares = [m["share"] for m in results if m]
    if len(shares) < 3:
        sys.exit("FAIL: could not measure 3 frames — inspect frames manually")
    for k in range(4):
        vals = [s[k] for s in shares]
        if max(vals) - min(vals) > 4:
            sys.exit(f"FAIL: share bounds disagree >4px across sections ({vals}) — "
                     "layout changes mid-recording; split geometry per section")
    s = shares[0]
    print(f"\nOK  share crop: crop={s[2]}:{s[3]}:{s[0]}:{s[1]}")
    cams = [m["cam"] for m in results if m and m["cam"]]
    if cams:
        c = cams[0]
        print(f"OK  webcam crop (verify visually): crop={c[2]}:{c[3]}:{c[0]}:{c[1]}")
    else:
        print("NO WEBCAM detected — use the no-webcam layout variants "
              "(PIPELINE.md §5, SHORTS.md §2)")


if __name__ == "__main__":
    main()
