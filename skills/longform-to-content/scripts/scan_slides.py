"""Slide/scene-change timeline for the content region (PIPELINE.md §2).

ffmpeg scene-detect misses light-on-light slide changes; this uses 5s-interval
thumbnails + PIL grayscale diff (change = >1% of pixels differ by >30 levels).

Usage: PYTHONUTF8=1 python scan_slides.py <recording.mp4> <crop W:H:X:Y> [out.txt]
  (crop string comes from measure_layout.py)
"""
import sys, subprocess, tempfile, glob, os
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
import numpy as np


def main():
    video, crop = sys.argv[1], sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else "slide_changes.txt"
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["ffmpeg", "-v", "error", "-i", video,
                        "-vf", f"fps=1/5,crop={crop},scale=178:-1",
                        "-y", os.path.join(tmp, "f_%05d.png")], check=True)
        files = sorted(glob.glob(os.path.join(tmp, "f_*.png")))
        prev, changes = None, []
        for i, f in enumerate(files):
            img = np.asarray(Image.open(f).convert("L"), dtype=np.int16)
            if prev is not None and (np.abs(img - prev) > 30).mean() > 0.01:
                changes.append(i * 5)
            prev = img
    with open(out_path, "w", encoding="utf-8") as f:
        for t in changes:
            f.write(f"{t}\n")
    print(f"{len(changes)} changes -> {out_path}")
    for t in changes[:40]:
        print(f"  {t:6d}s  ({t//60:02d}:{t%60:02d})")
    if len(changes) > 40:
        print(f"  ... +{len(changes)-40} more")


if __name__ == "__main__":
    main()
