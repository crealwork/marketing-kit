"""Render the cut: per-segment extract + 30ms audio fades + lossless concat.

Footage is untouched (no relayout) — each EDL range is re-encoded once with
identical codec params, then concatenated with -c copy. 30ms afade in/out at
every boundary prevents audible pops.

Usage:
  python render_cut.py <edl.json> [-o cut.mp4] [--crf 18] [--workers 4]
"""
import argparse, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")


def src_fps(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=avg_frame_rate", "-of", "csv=p=0", path],
                       capture_output=True, text=True, check=True)
    num, den = r.stdout.strip().split("/")
    return str(round(int(num) / int(den), 3)) if int(den) else num


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edl")
    ap.add_argument("-o", "--out", default="cut.mp4")
    ap.add_argument("--crf", default="18")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    edl = json.load(open(args.edl, encoding="utf-8"))
    src = edl["source"]
    fps = src_fps(src)
    clips = os.path.join(os.path.dirname(os.path.abspath(args.out)) or ".", "clips")
    os.makedirs(clips, exist_ok=True)

    # identical codec params on every clip or the -c copy concat breaks
    vcodec = ["-c:v", "libx264", "-crf", args.crf, "-preset", "veryfast",
              "-pix_fmt", "yuv420p", "-r", fps, "-video_track_timescale", "90000"]
    acodec = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

    def render_seg(i, start, end):
        dur = end - start
        out = os.path.join(clips, f"seg_{i:03d}.mp4")
        af = f"afade=t=in:st=0:d=0.03,afade=t=out:st={dur - 0.03:.3f}:d=0.03"
        cmd = ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}",
               "-i", src, "-af", af, *vcodec, *acodec, "-y", out]
        subprocess.run(cmd, check=True, capture_output=True)
        return i

    n = len(edl["ranges"])
    print(f"rendering {n} segments ({args.workers} workers)...")
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(render_seg, i, r["start"], r["end"])
                for i, r in enumerate(edl["ranges"])]
        for done, f in enumerate(futs, 1):
            f.result()
            if done % 10 == 0:
                print(f"  {done}/{n}", flush=True)

    concat_txt = os.path.join(clips, "concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for i in range(n):
            f.write(f"file 'seg_{i:03d}.mp4'\n")

    print("concatenating...")
    subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", concat_txt, "-c", "copy", "-movflags", "+faststart",
                    "-y", args.out], check=True)

    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", args.out], capture_output=True, text=True)
    got = float(r.stdout)
    exp = edl["total_duration_s"]
    flag = "" if abs(got - exp) <= 1.0 else "  <-- MISMATCH >1s, inspect before shipping"
    print(f"DONE  {args.out}  duration={got:.1f}s (EDL expects ~{exp:.1f}s){flag}")


if __name__ == "__main__":
    main()
