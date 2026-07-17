"""Build one vertical Short (1080x1920) from a source moment.

Center-crops the source to 9:16 (talking-head framing), tightens internal pauses
(0.9s gap-split — shorts pacing dies on 1s pauses), burns a 2-line hook title
(visible from frame #1 — the platform uses it as the cover) and word-timed
captions LAST. Keeps <out>_raw.mp4 so caption fixes re-burn in seconds.

Usage:
  python gen_shorts.py <source.mp4> --transcript t.json --start 841.5 --end 897.2 \
      --title "99% quit\\nright *here*" -o short_01.mp4
      [--accent "#FFD24A"] [--gap 0.9] [--crop-x -1 (center)] [--font "Pretendard"]
      [--fontsdir fonts] [--corrections corr.json] [--accent-words 99%,here]
      [--captions-only]

Title accent: wrap ONE span in *asterisks* — the number or the verb, never a line.
"""
import argparse, json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

W, H = 1080, 1920


def ass_color(hex_rgb):
    r, g, b = hex_rgb.lstrip("#")[0:2], hex_rgb.lstrip("#")[2:4], hex_rgb.lstrip("#")[4:6]
    return f"&H00{b}{g}{r}".upper()


def ass_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--transcript", required=True)
    ap.add_argument("--start", type=float, required=True)
    ap.add_argument("--end", type=float, required=True)
    ap.add_argument("--title", required=True, help=r"2 lines max, \n separated, ONE *accent* span")
    ap.add_argument("-o", "--out", default="short.mp4")
    ap.add_argument("--accent", default="#FFD24A")
    ap.add_argument("--gap", type=float, default=0.9)
    ap.add_argument("--crop-x", type=int, default=-1, help="source-px left edge of 9:16 crop; -1 = center")
    ap.add_argument("--font", default="Pretendard")
    ap.add_argument("--fontsdir", default=None, help="RELATIVE dir with a static bold font file")
    ap.add_argument("--corrections", default=None)
    ap.add_argument("--accent-words", default=None, help="comma list of caption tokens to color")
    ap.add_argument("--crf", default="18")
    ap.add_argument("--captions-only", action="store_true", help="re-burn onto existing _raw")
    args = ap.parse_args()

    base, _ = os.path.splitext(args.out)
    raw = base + "_raw.mp4"
    data = json.load(open(args.transcript, encoding="utf-8"))
    words = [w for w in data["words"] if w.get("type") == "word"
             and w["start"] >= args.start - 0.05 and w["end"] <= args.end + 0.35]
    if not words:
        sys.exit("no words in the given window")

    # word-snapped segments, tight internal gap-split
    runs = [[words[0]]]
    for prev, cur in zip(words, words[1:]):
        (runs.append([cur]) if cur["start"] - prev["end"] > args.gap else runs[-1].append(cur))
    segs = []
    for i, run in enumerate(runs):
        s = run[0]["start"] - 0.20
        e = run[-1]["end"] + (0.25 if i == len(runs) - 1 else 0.20)
        segs.append((max(args.start, s), min(args.end + 0.30, e)))

    if not (args.captions_only and os.path.exists(raw)):
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                            "-show_entries", "stream=height,avg_frame_rate", "-of", "json", args.source],
                           capture_output=True, text=True, check=True)
        st = json.loads(r.stdout)["streams"][0]
        num, den = st["avg_frame_rate"].split("/")
        fps = str(round(int(num) / int(den), 3))
        crop_w = f"floor(ih*9/16/2)*2"
        crop_x = "(iw-ow)/2" if args.crop_x < 0 else str(args.crop_x)

        vcodec = ["-c:v", "libx264", "-crf", args.crf, "-preset", "veryfast",
                  "-pix_fmt", "yuv420p", "-r", fps, "-video_track_timescale", "90000"]
        acodec = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]
        clips = base + "_clips"
        os.makedirs(clips, exist_ok=True)
        for i, (s, e) in enumerate(segs):
            dur = e - s
            fc = (f"[0:v]crop={crop_w}:ih:{crop_x}:0,scale={W}:{H}:flags=lanczos[v];"
                  f"[0:a]afade=t=in:st=0:d=0.03,afade=t=out:st={dur - 0.03:.3f}:d=0.03[a]")
            subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{s:.3f}", "-t", f"{dur:.3f}",
                            "-i", args.source, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                            *vcodec, *acodec, "-y", os.path.join(clips, f"s{i:02d}.mp4")],
                           check=True, capture_output=True)
        with open(os.path.join(clips, "concat.txt"), "w", encoding="utf-8") as f:
            for i in range(len(segs)):
                f.write(f"file 's{i:02d}.mp4'\n")
        subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                        "-i", os.path.join(clips, "concat.txt"), "-c", "copy",
                        "-movflags", "+faststart", "-y", raw], check=True)

    # ---- captions + title (ASS, burned LAST) ----
    corrections = json.load(open(args.corrections, encoding="utf-8")) if args.corrections else []

    def correct(text):
        for wrong, right in corrections:
            text = text.replace(wrong, right)
        return text

    accent = ass_color(args.accent)
    ink = "&H00FFFFFF"
    accent_words = [w.strip() for w in (args.accent_words or "").split(",") if w.strip()]

    # output-timeline piece table for this short
    pieces, t = [], 0.0
    for s, e in segs:
        pieces.append((s, e, t))
        t += e - s
    total = t

    def to_out(src):
        for a, b, off in pieces:
            if a <= src <= b:
                return off + (src - a)
        return None

    kept = []
    for a, b, off in pieces:
        kept.extend(w for w in words if w["start"] >= a - 0.02 and w["end"] <= b + 0.02)

    chunk_chars = 13 if data.get("language") in ("ko", "ja", "zh") else 26
    cues, cur = [], []
    for i, w in enumerate(kept):
        cur.append(w)
        text = " ".join(x["text"] for x in cur)
        nxt = kept[i + 1] if i + 1 < len(kept) else None
        gap = (nxt["start"] - w["end"]) if nxt else 99
        if len(text) >= chunk_chars or re.search(r"[.?!]$", w["text"]) or gap >= 0.5:
            st, en = to_out(cur[0]["start"]), to_out(cur[-1]["end"])
            if st is not None and en is not None and en > st:
                cues.append([st, min(en + 0.22, total), correct(text)])
            cur = []
    for i in range(len(cues) - 1):
        cues[i][1] = min(cues[i][1], cues[i + 1][0] - 0.02)

    def accentize(text):
        for aw in accent_words:
            text = text.replace(aw, "{\\c" + accent + "&}" + aw + "{\\c" + ink + "&}")
        return text

    # title: \n line break, *span* -> accent color
    title = args.title.replace("\\n", "\\N")
    title = re.sub(r"\*([^*]+)\*",
                   lambda m: "{\\c" + accent + "&}" + m.group(1) + "{\\c" + ink + "&}", title)

    ass = base + ".ass"
    with open(ass, "w", encoding="utf-8-sig") as f:
        f.write(f"""[Script Info]
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Title,{args.font},76,{ink},{ink},&H00101010,&H00101010,-1,0,0,0,100,100,0,0,1,5,0,8,60,60,150,1
Style: Cap,{args.font},58,{ink},{ink},&H00101010,&H00101010,-1,0,0,0,100,100,0,0,1,4,0,2,60,60,620,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,{ass_time(0)},{ass_time(total)},Title,,0,0,0,,{title}
""")
        for st, en, text in cues:
            f.write(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},Cap,,0,0,0,,{accentize(text)}\n")

    sub = f"subtitles={os.path.basename(ass)}"
    if args.fontsdir:
        sub += f":fontsdir={args.fontsdir}"
    # relative paths only — Windows drive-letter colons break the subtitles filter
    subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.basename(raw), "-vf", sub,
                    "-c:v", "libx264", "-crf", args.crf, "-preset", "veryfast",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart",
                    "-y", os.path.basename(args.out)],
                   check=True, cwd=os.path.dirname(os.path.abspath(args.out)) or ".")

    flag = "" if 20 <= total <= 90 else "  <-- outside 40-90s envelope, reselect or retighten"
    print(f"DONE  {args.out}  {total:.1f}s  {len(cues)} cues{flag}")
    print("SELF-TEST: extract frame t=0.04 and READ it — full layout + title must be visible.")


if __name__ == "__main__":
    main()
