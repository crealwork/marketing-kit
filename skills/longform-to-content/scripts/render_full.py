"""Render the full-length horizontal edit.

Per-segment extract from source with the relayout transform
(slide region -> full frame, webcam -> rounded PIP bottom-right),
30ms audio fades at every boundary, then lossless concat with
pre-rendered intro/outro cards (BGM).
"""
import json, subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")

EDIT = "<WORK>/edit"
BGM = "<BGM_FILE>.mp3"
CLIPS = f"{EDIT}/clips_full"
os.makedirs(CLIPS, exist_ok=True)

edl = json.load(open(f"{EDIT}/edl_full.json", encoding="utf-8"))
SRC = edl["source"]

VCODEC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
          "-pix_fmt", "yuv420p", "-r", "24", "-video_track_timescale", "90000"]
ACODEC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

def render_seg(i, start, end):
    dur = end - start
    out = f"{CLIPS}/seg_{i:03d}.mp4"
    fc = (
        "[0:v]crop=1440:810:0:135,scale=1920:1080:flags=lanczos[bg];"
        "[0:v]crop=480:270:1440:405,scale=432:243[cam];"
        "[cam][2:v]alphamerge[camr];"
        "[bg][3:v]overlay=0:0[bgs];"
        "[bgs][camr]overlay=1460:809[v];"
        f"[0:a]afade=t=in:st=0:d=0.03,afade=t=out:st={dur - 0.03:.3f}:d=0.03[a]"
    )
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", SRC,
           "-f", "lavfi", "-i", "anullsrc",  # placeholder to keep input indexes stable
           "-loop", "1", "-i", f"{EDIT}/assets/pip_mask.png",
           "-loop", "1", "-i", f"{EDIT}/assets/pip_shadow.png",
           "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
           *VCODEC, *ACODEC, "-shortest", "-y", out]
    subprocess.run(cmd, check=True, capture_output=True)
    return i

def render_card(img, out, dur, fade_in, fade_out, bgm_start=0.0, end_fade_to_white=False):
    vf = f"fade=t=in:st=0:d={fade_in}:color=0xFAF7F2"
    if end_fade_to_white:
        vf += f",fade=t=out:st={dur - fade_out:.2f}:d={fade_out}:color=0xFAF7F2"
    af = (f"atrim=start={bgm_start}:end={bgm_start + dur},asetpts=PTS-STARTPTS,"
          f"afade=t=in:st=0:d=1.0,afade=t=out:st={dur - 1.4:.2f}:d=1.4,volume=0.9")
    cmd = ["ffmpeg", "-v", "error", "-loop", "1", "-t", str(dur), "-i", img,
           "-i", BGM, "-filter_complex", f"[0:v]{vf}[v];[1:a]{af}[a]",
           "-map", "[v]", "-map", "[a]", *VCODEC, *ACODEC, "-y", out]
    subprocess.run(cmd, check=True, capture_output=True)

print("rendering intro/outro cards...")
render_card(f"{EDIT}/assets/intro_card.png", f"{CLIPS}/card_intro.mp4", 4.5, 0.9, 1.0)
render_card(f"{EDIT}/assets/outro_card.png", f"{CLIPS}/card_outro.mp4", 6.0, 0.6, 0.9,
            bgm_start=8.0, end_fade_to_white=True)

print(f"rendering {len(edl['ranges'])} segments (4 workers)...")
with ThreadPoolExecutor(max_workers=4) as ex:
    futs = [ex.submit(render_seg, i, r["start"], r["end"])
            for i, r in enumerate(edl["ranges"])]
    done = 0
    for f in futs:
        f.result()
        done += 1
        if done % 10 == 0:
            print(f"  {done}/{len(futs)}", flush=True)

with open(f"{CLIPS}/concat.txt", "w", encoding="utf-8") as f:
    f.write(f"file 'card_intro.mp4'\n")
    for i in range(len(edl["ranges"])):
        f.write(f"file 'seg_{i:03d}.mp4'\n")
    f.write(f"file 'card_outro.mp4'\n")

print("concatenating...")
subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", f"{CLIPS}/concat.txt", "-c", "copy", "-movflags", "+faststart",
                "-y", f"{EDIT}/full_horizontal.mp4"], check=True)
r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", f"{EDIT}/full_horizontal.mp4"],
                   capture_output=True, text=True)
print(f"DONE  full_horizontal.mp4  duration={float(r.stdout):.1f}s "
      f"(expected ~{edl['total_duration_s'] + 10.5:.1f}s)")
