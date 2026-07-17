"""v4: reorder cold open so the 99%-give-up clip leads (matches thumbnail),
then re-concat + rebuild captions/SRT/chapters + re-burn. No segment re-render.
"""
import json, re, subprocess, sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corrections

EDIT = "<WORK>/edit"
FINAL = "<WORK>/final"
CLIPS = f"{EDIT}/clips_full"
INTRO_CARD = 4.5

VCODEC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
          "-pix_fmt", "yuv420p", "-r", "24", "-video_track_timescale", "90000"]

edl = json.load(open(f"{EDIT}/edl_full.json", encoding="utf-8"))
cuts = json.load(open(f"{EDIT}/filler_cuts.json", encoding="utf-8"))
data = json.load(open(f"{EDIT}/transcripts/recording.json", encoding="utf-8"))
WORDS = [w for w in data["words"] if w.get("type") == "word"]

# same range math as v3 (must match the rendered seg3_* files)
cut_iv = [(c["start"] - 0.02, c["end"] + 0.04) for c in cuts]
ranges = []
for r in edl["ranges"]:
    pieces_ = [(r["start"], r["end"])]
    for (ca, cb) in cut_iv:
        nxt = []
        for (a, b) in pieces_:
            if cb <= a or ca >= b:
                nxt.append((a, b))
            else:
                if ca - a >= 0.3:
                    nxt.append((a, ca))
                if b - cb >= 0.3:
                    nxt.append((cb, b))
        pieces_ = nxt
    ranges.extend(pieces_)
merged = [list(ranges[0])]
for a, b in ranges[1:]:
    if a - merged[-1][1] < 0.06:
        merged[-1][1] = b
    else:
        merged.append([a, b])
ranges = merged
assert len(ranges) == 101, f"range count changed: {len(ranges)}"

HL_SRC = {0: 2316.55, 1: 1080.08, 2: 1287.27, 3: 2496.18, 4: 3021.48}
HL_ORDER = [3, 0, 1, 2, 4]   # 99% first — thumbnail match

def dur_of(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout)

pieces = []
t = 0.0
for i in HL_ORDER:
    d = dur_of(f"{CLIPS}/hl_{i}.mp4")
    pieces.append((HL_SRC[i], HL_SRC[i] + d, t))
    t += d
HL_TOTAL = t
t += INTRO_CARD
for (a, b) in ranges:
    pieces.append((a, b, t))
    t += b - a
TOTAL = t
print(f"cold open reordered (99% first), {HL_TOTAL:.1f}s; total ~{TOTAL + 6.0:.1f}s")

with open(f"{CLIPS}/concat_v4.txt", "w", encoding="utf-8") as f:
    for i in HL_ORDER:
        f.write(f"file 'hl_{i}.mp4'\n")
    f.write("file 'card_intro.mp4'\n")
    for i in range(len(ranges)):
        f.write(f"file 'seg3_{i:03d}.mp4'\n")
    f.write("file 'card_outro.mp4'\n")
subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", f"{CLIPS}/concat_v4.txt", "-c", "copy", "-y",
                f"{EDIT}/full_v4_raw.mp4"], check=True)

def chunks_for_piece(a, b, off):
    ws = [w for w in WORDS if w["start"] >= a - 0.02 and w["end"] <= b + 0.02]
    out, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w)
        text = " ".join(x["text"] for x in cur)
        nxt = ws[i + 1] if i + 1 < len(ws) else None
        gap = (nxt["start"] - w["end"]) if nxt else 99
        if len(text) >= 26 or re.search(r"[.?!]$", w["text"]) or gap >= 0.7:
            st = off + (cur[0]["start"] - a)
            en = min(off + (cur[-1]["end"] - a) + 0.22, off + (b - a))
            text = corrections.apply(text)
            text = re.sub(r"\s*--\s*", " ", text).strip()
            if en > st and text:
                out.append((max(st, off), en, text))
            cur = []
    return out

cues = []
for (a, b, off) in pieces:
    cues.extend(chunks_for_piece(a, b, off))
cues.sort()
for i in range(len(cues) - 1):
    if cues[i][1] > cues[i + 1][0]:
        cues[i] = (cues[i][0], cues[i + 1][0] - 0.02, cues[i][2])

def ass_time(x):
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Noto Serif CJK KR,46,&H00F2F7FA,&H00FFFFFF,&H2017191C,&H2017191C,-1,0,0,0,100,100,0,0,3,9,0,2,60,60,42,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(f"{EDIT}/full_v4.ass", "w", encoding="utf-8-sig") as f:
    f.write(ASS_HEAD)
    for st, en, text in cues:
        f.write(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},Cap,,0,0,0,,{text}\n")

def srt_time(x):
    ms = int(round((x - int(x)) * 1000))
    return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{ms:03d}"

with open(f"{FINAL}/webinar-s02-full.srt", "w", encoding="utf-8") as f:
    for i, (st, en, text) in enumerate(cues, 1):
        f.write(f"{i}\n{srt_time(st)} --> {srt_time(en)}\n{text}\n\n")

def to_out(src):
    for a, b, off in pieces[5:]:
        if a - 0.02 <= src <= b + 0.02:
            return off + (src - a)
    return None

CHAPTERS = [
    (None, "하이라이트"), (858.44, "오프닝 — 지난주 리뷰 3가지"),
    (1046.59, "에이전트가 여는 시장"), (1454.42, "세상의 케이스 스터디"),
    (2038.21, "직접 만든 자동화 사례"), (2367.25, "시작 플레이북 5단계"),
    (2583.55, "챗GPT vs 클로드 vs 제미나이"), (3113.75, "키 메시지 — 사람 직원을 대하듯"),
    (3310.05, "퀴즈 타임"), (3871.20, "무료 상담 안내 & Q&A"),
    (4726.37, "마무리 & 다음 주 예고"),
]
with open(f"{FINAL}/webinar-s02-chapters.txt", "w", encoding="utf-8") as f:
    for src, label in CHAPTERS:
        o = 0.0 if src is None else to_out(src)
        f.write(f"{int(o // 60)}:{int(o % 60):02d} {label}\n")

print("burning subtitles (audio copy)...")
subprocess.run(["ffmpeg", "-v", "error", "-i", "full_v4_raw.mp4",
                "-vf", "subtitles=full_v4.ass:fontsdir=assets/fonts",
                *VCODEC, "-c:a", "copy", "-movflags", "+faststart",
                "-y", f"{FINAL}/webinar-s02-full-1080p.mp4"], check=True, cwd=EDIT)
r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", f"{FINAL}/webinar-s02-full-1080p.mp4"],
                   capture_output=True, text=True)
print(f"DONE v4  duration={float(r.stdout):.1f}s (expected ~{TOTAL + 6.0:.1f}s)")
