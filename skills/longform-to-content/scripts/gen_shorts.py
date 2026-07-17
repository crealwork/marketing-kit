"""Build 6 vertical shorts (1080x1920) from the webinar recording.

Layout: cream paper canvas, serif header (wordmark + hook title),
slide card top, big serif captions middle, webcam card bottom.
Captions are burned LAST (after all overlays), per hard rule 1.
"""
import json, subprocess, sys, os, re
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corrections

EDIT = "<WORK>/edit"
SRC = "<WORK>/recording.mp4"
FONTS = f"{EDIT}/assets/fonts"
SERIF_VF = "<FONTS_DIR>/NotoSerifKR-VF.ttf"

CREAM = (250, 247, 242)
INK = (28, 25, 23)
BURGUNDY = (114, 10, 34)          # sampled from deck ("in Action" italic)
GRAY = (120, 114, 108)
BURGUNDY_ASS = "&H00220A72"       # BGR of 720A22
INK_ASS = "&H0017191C"

W, H = 1080, 1920
SLIDE_W, SLIDE_H, SLIDE_X, SLIDE_Y = 1040, 585, 20, 352
CAM_W, CAM_H, CAM_X, CAM_Y = 700, 394, 190, 1360
CAPTION_TOP = 1010  # ASS MarginV (alignment 8)

GAP_SPLIT = 0.9
TAIL_PAD, HEAD_PAD, EDGE_HEAD, EDGE_TAIL = 0.25, 0.20, 0.12, 0.30

SHORTS = [
    dict(id="s1_99percent", title=["|99%|는 여기서", "포기합니다"],
         ranges=[(2474.89, 2539.33)],
         keywords=["99%", "1%", "포기", "완성"]),
    dict(id="s2_document", title=["글로 못 쓰면", "|자동화|도 없습니다"],
         ranges=[(1254.20, 1274.32), (1287.42, 1305.64)],
         keywords=["문서화", "자동화", "구십", "글로써"]),
    dict(id="s3_voicemail", title=["고객 |93%|는 다시", "전화하지 않는다"],
         ranges=[(1561.70, 1581.72), (1598.18, 1633.16)],
         keywords=["93%", "삼십 분", "한시간", "뺏기는", "시스템"]),
    dict(id="s4_nocode", title=["노코드 툴,", "|배우지 마세요|"],
         ranges=[(2976.83, 3024.71)],
         keywords=["노코드", "코딩 에이전트", "버블", "메이크", "제이피어"]),
    dict(id="s5_claude_gpt", title=["$20라면,", "|클로드| vs 챗GPT?"],
         ranges=[(2729.53, 2786.15)],
         keywords=["클로드", "챗GPT", "$20", "마케팅"]),
    dict(id="s6_hallucination", title=["AI는 |거짓말|을", "합니다"],
         ranges=[(1376.78, 1386.84), (1396.76, 1433.06)],
         keywords=["거짓말", "할루시네이션", "인간", "워크플로우", "프로세스"]),
]

VCODEC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
          "-pix_fmt", "yuv420p", "-r", "24", "-video_track_timescale", "90000"]
ACODEC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


def serif(size, weight=700):
    f = ImageFont.truetype(SERIF_VF, size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def rounded_mask(w, h, r, path):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    m.save(path)


def draw_title(d, lines, y0):
    font = serif(64, 700)
    for i, line in enumerate(lines):
        # |word| marks burgundy spans
        parts = re.split(r"(\|[^|]+\|)", line)
        widths = []
        for p in parts:
            t = p.strip("|")
            widths.append(d.textlength(t, font=font))
        total = sum(widths)
        x = (W - total) / 2
        y = y0 + i * 88
        for p, wpx in zip(parts, widths):
            t = p.strip("|")
            color = BURGUNDY if p.startswith("|") else INK
            d.text((x, y), t, font=font, fill=color)
            x += wpx


def build_bg(short):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 96), "Sundayable.", font=serif(44, 600), fill=INK, anchor="mm")
    draw_title(d, short["title"], 158)
    # shadows under cards
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sh)
    ds.rounded_rectangle([SLIDE_X + 2, SLIDE_Y + 10, SLIDE_X + SLIDE_W + 2, SLIDE_Y + SLIDE_H + 10],
                         radius=18, fill=(30, 20, 20, 110))
    ds.rounded_rectangle([CAM_X + 2, CAM_Y + 10, CAM_X + CAM_W + 2, CAM_Y + CAM_H + 10],
                         radius=20, fill=(30, 20, 20, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img.convert("RGBA"), sh).convert("RGB")
    # footer kicker
    ImageDraw.Draw(img).text((W / 2, 1832), "AI 마케팅 웨비나  ·  SESSION 02",
                             font=serif(30, 500), fill=GRAY, anchor="mm")
    out = f"{EDIT}/assets/bg_{short['id']}.png"
    img.save(out)
    return out


def build_endcard():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 880), "Sundayable.", font=serif(96, 700), fill=INK, anchor="mm")
    d.text((W / 2, 1000), "AI 마케팅 웨비나 — 매주 목요일", font=serif(40, 500),
           fill=BURGUNDY, anchor="mm")
    out = f"{EDIT}/assets/endcard.png"
    img.save(out)
    return out


# ---------- word timeline ----------
data = json.load(open(f"{EDIT}/transcripts/recording.json", encoding="utf-8"))
WORDS = [w for w in data["words"] if w.get("type") == "word"]


def segments_for(ranges):
    segs = []
    for (a, b) in ranges:
        ws = [w for w in WORDS if w["start"] >= a - 0.05 and w["end"] <= b + 0.3]
        runs = [[ws[0]]]
        for prev, cur in zip(ws, ws[1:]):
            if cur["start"] - prev["end"] > GAP_SPLIT:
                runs.append([cur])
            else:
                runs[-1].append(cur)
        for i, run in enumerate(runs):
            s = run[0]["start"] - (EDGE_HEAD if i == 0 else HEAD_PAD)
            e = run[-1]["end"] + (EDGE_TAIL if i == len(runs) - 1 else TAIL_PAD)
            segs.append({"start": max(a - EDGE_HEAD, s), "end": min(b + EDGE_TAIL, e),
                         "words": run})
    # output offsets
    t = 0.0
    for s in segs:
        s["offset"] = t
        t += s["end"] - s["start"]
    return segs, t


# ---------- captions ----------
def chunk_words(words):
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        text = " ".join(x["text"] for x in cur)
        brk = (len(text) >= 12 or re.search(r"[.?!,]$", w["text"]))
        nxt = words[words.index(w) + 1] if words.index(w) + 1 < len(words) else None
        gap = (nxt["start"] - w["end"]) if nxt else 99
        if brk or gap >= 0.5:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    return chunks


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def build_ass(short, segs, out_dur):
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Noto Serif CJK KR,64,{INK_ASS},&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,1,0,0,8,50,50,{CAPTION_TOP},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    kw = short["keywords"]
    lines = []
    for seg in segs:
        seg_out_end = seg["offset"] + (seg["end"] - seg["start"])
        for ch in chunk_words(seg["words"]):
            st = ch[0]["start"] - seg["start"] + seg["offset"]
            en = ch[-1]["end"] - seg["start"] + seg["offset"] + 0.18
            en = min(en, seg_out_end)
            text = corrections.apply(" ".join(w["text"] for w in ch))
            text = re.sub(r"\s*--\s*", " ", text).strip()
            for k in kw:
                if k in text:
                    text = text.replace(
                        k, "{\\c" + BURGUNDY_ASS + "}" + k + "{\\c" + INK_ASS + "}")
            lines.append(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},Cap,,0,0,0,,{text}")
    path = f"{EDIT}/shorts/{short['id']}.ass"
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(header + "\n".join(lines) + "\n")
    return path


# ---------- render ----------
def render_short(short, endcard):
    sid = short["id"]
    segs, out_dur = segments_for(short["ranges"])
    bg = build_bg(short)
    clips = []
    for i, seg in enumerate(segs):
        dur = seg["end"] - seg["start"]
        out = f"{EDIT}/shorts/_{sid}_seg{i}.mp4"
        fc = (
            f"[1:v]scale={W}:{H}[bg];"
            f"[0:v]crop=1440:810:0:135,scale={SLIDE_W}:{SLIDE_H}:flags=lanczos[sl];"
            f"[sl][2:v]alphamerge[slr];"
            f"[0:v]crop=480:270:1440:405,scale={CAM_W}:{CAM_H}:flags=lanczos[cam];"
            f"[cam][3:v]alphamerge[camr];"
            f"[bg][slr]overlay={SLIDE_X}:{SLIDE_Y}[t1];"
            f"[t1][camr]overlay={CAM_X}:{CAM_Y}[v];"
            f"[0:a]afade=t=in:st=0:d=0.03,afade=t=out:st={dur - 0.03:.3f}:d=0.03[a]"
        )
        cmd = ["ffmpeg", "-v", "error", "-ss", f"{seg['start']:.3f}", "-t", f"{dur:.3f}",
               "-i", SRC, "-loop", "1", "-i", bg,
               "-loop", "1", "-i", f"{EDIT}/assets/mask_slide.png",
               "-loop", "1", "-i", f"{EDIT}/assets/mask_cam.png",
               "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
               *VCODEC, *ACODEC, "-shortest", "-y", out]
        subprocess.run(cmd, check=True, capture_output=True)
        clips.append(out)
    # end card (1.4s, silent)
    ec = f"{EDIT}/shorts/_{sid}_end.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-loop", "1", "-t", "1.4", "-i", endcard,
                    "-f", "lavfi", "-t", "1.4", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]fade=t=in:st=0:d=0.25:color=0xFAF7F2[v]",
                    "-map", "[v]", "-map", "1:a", *VCODEC, *ACODEC, "-y", ec],
                   check=True, capture_output=True)
    clips.append(ec)
    # concat
    lst = f"{EDIT}/shorts/_{sid}_concat.txt"
    with open(lst, "w", encoding="utf-8") as f:
        for c in clips:
            f.write(f"file '{os.path.basename(c)}'\n")
    raw = f"{EDIT}/shorts/_{sid}_raw.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", "-y", raw], check=True, capture_output=True)
    # captions LAST
    final = f"{EDIT}/shorts/{sid}.mp4"
    ass = build_ass(short, segs, out_dur)
    ass_f = os.path.basename(ass)
    subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.basename(raw),
                    "-vf", f"subtitles={ass_f}:fontsdir=../assets/fonts",
                    *VCODEC, *ACODEC, "-movflags", "+faststart",
                    "-y", os.path.basename(final)],
                   check=True, capture_output=True, cwd=f"{EDIT}/shorts")
    print(f"{sid}: {out_dur + 1.4:.1f}s  ({len(segs)} segs)")


def reburn_captions(short):
    """Rebuild corrected ASS and re-burn onto the existing _raw concat."""
    sid = short["id"]
    segs, out_dur = segments_for(short["ranges"])
    build_ass(short, segs, out_dur)
    subprocess.run(["ffmpeg", "-v", "error", "-i", f"_{sid}_raw.mp4",
                    "-vf", f"subtitles={sid}.ass:fontsdir=../assets/fonts",
                    *VCODEC, *ACODEC, "-movflags", "+faststart", "-y", f"{sid}.mp4"],
                   check=True, capture_output=True, cwd=f"{EDIT}/shorts")
    print(f"{sid}: captions re-burned")


if __name__ == "__main__":
    if "--captions-only" in sys.argv:
        for s in SHORTS:
            reburn_captions(s)
        print("shorts captions done")
        sys.exit(0)
    rounded_mask(SLIDE_W, SLIDE_H, 18, f"{EDIT}/assets/mask_slide.png")
    rounded_mask(CAM_W, CAM_H, 20, f"{EDIT}/assets/mask_cam.png")
    endcard = build_endcard()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for s in SHORTS:
        if only and s["id"] != only:
            continue
        render_short(s, endcard)
    print("shorts done")
