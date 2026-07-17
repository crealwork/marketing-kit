"""Master SRT on the OUTPUT timeline of full_horizontal.mp4 + YouTube chapters."""
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

EDIT = "<WORK>/edit"
INTRO = 4.5

edl = json.load(open(f"{EDIT}/edl_full.json", encoding="utf-8"))
data = json.load(open(f"{EDIT}/transcripts/recording.json", encoding="utf-8"))
words = [w for w in data["words"] if w.get("type") == "word"]

# source->output map per range
ranges = []
t = INTRO
for r in edl["ranges"]:
    ranges.append((r["start"], r["end"], t))
    t += r["end"] - r["start"]

def to_out(src):
    for a, b, off in ranges:
        if a <= src <= b:
            return off + (src - a)
    return None

def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = int(x % 60)
    ms = int(round((x - int(x)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# chunk words into subtitle lines (only words inside kept ranges)
kept = []
for a, b, off in ranges:
    kept.extend([w for w in words if w["start"] >= a - 0.02 and w["end"] <= b + 0.02])

subs, cur = [], []
for i, w in enumerate(kept):
    cur.append(w)
    text = " ".join(x["text"] for x in cur)
    nxt = kept[i + 1] if i + 1 < len(kept) else None
    gap = (nxt["start"] - w["end"]) if nxt else 99
    if len(text) >= 26 or re.search(r"[.?!]$", w["text"]) or gap >= 0.7:
        st, en = to_out(cur[0]["start"]), to_out(cur[-1]["end"])
        if st is not None and en is not None and en > st:
            subs.append((st, min(en + 0.25, st + 7.0), text))
        cur = []

with open(f"{EDIT}/full_horizontal.srt", "w", encoding="utf-8") as f:
    for i, (st, en, text) in enumerate(subs, 1):
        f.write(f"{i}\n{srt_time(st)} --> {srt_time(en)}\n{text}\n\n")
print(f"SRT: {len(subs)} cues -> full_horizontal.srt")

CHAPTERS = [
    (0.0, "인트로"),
    (858.44, "오프닝 — 지난주 리뷰 3가지"),
    (1046.59, "에이전트가 여는 시장"),
    (1454.42, "세상의 케이스 스터디"),
    (2038.21, "직접 만든 자동화 사례"),
    (2367.25, "시작 플레이북 5단계"),
    (2583.55, "챗GPT vs 클로드 vs 제미나이"),
    (3113.75, "키 메시지 — 사람 직원을 대하듯"),
    (3310.05, "퀴즈 타임"),
    (3871.20, "무료 상담 안내 & Q&A"),
    (4726.37, "마무리 & 다음 주 예고"),
]
def yt(x):
    m, s = int(x // 60), int(x % 60)
    return f"{m}:{s:02d}"

with open(f"{EDIT}/chapters.txt", "w", encoding="utf-8") as f:
    for src, label in CHAPTERS:
        o = 0.0 if src == 0 else to_out(src)
        if o is None:
            o = min((abs(src - a), off + max(0, src - a)) for a, b, off in ranges)[1]
        f.write(f"{yt(o)} {label}\n")
        print(f"{yt(o):>6}  {label}")
print("chapters.txt written")
