"""Generate EDL for the Sundayable Webinar S02 full-length edit.

Keep-windows are hand-authored from takes_packed.md. Within each window,
silences > GAP_SPLIT between words are collapsed to a short breath by
splitting into separate segments (render adds 30ms afades at each edge).
All boundaries snap to Scribe word edges, then get edge padding.
"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")

EDIT = "<WORK>/edit"
SRC_JSON = f"{EDIT}/transcripts/recording.json"

GAP_SPLIT = 1.75     # split when inter-word silence exceeds this
TAIL_PAD = 0.35      # keep after last word of a segment
HEAD_PAD = 0.30      # keep before first word of a segment
EDGE_HEAD = 0.15     # pad at window start
EDGE_TAIL = 0.25     # pad at window end
MIN_SEG = 0.8        # merge segments shorter than this

# (start, end) keep-windows on the source timeline, in order.
WINDOWS = [
    (841.53, 843.63),     # "그럼 이제 슬슬 시작을 해보도록 하겠습니다"
    (858.44, 3307.23),    # main presentation (skips last-week meta talk)
    # --- quiz, heavily compressed ---
    (3310.05, 3324.54),   # quiz intro + QR
    (3326.00, 3348.10),   # gift card
    (3398.72, 3400.96),   # "시작을 하겠습니다. 시작."
    (3407.14, 3409.82),   # Q1
    (3439.96, 3446.74),   # Q1 result
    (3450.96, 3470.24),   # Q2
    (3473.62, 3480.98),   # Q2 result
    (3483.10, 3494.96),   # Q3
    (3510.44, 3530.08),   # Q3 result
    (3537.22, 3543.30),   # Q4
    (3549.78, 3561.62),   # Q4 options
    (3573.10, 3595.70),   # Q4 curveball + answer
    (3600.50, 3617.22),   # Q5
    (3626.70, 3635.08),   # Q5 result
    (3645.34, 3661.56),   # Q6
    (3665.90, 3680.98),   # Q6 result
    (3688.88, 3690.96),   # Q7
    (3697.70, 3707.08),   # Q7 result
    (3715.64, 3729.96),   # Q8
    (3745.58, 3753.16),   # Q8 result (joke answer)
    (3765.54, 3781.14),   # Q9
    (3792.36, 3814.68),   # Q9 answer
    (3827.20, 3843.52),   # Q10
    (3844.66, 3869.98),   # winner
    # --- consult offer + Q&A + closing (gap-trimmed) ---
    (3871.20, 4828.09),
]

with open(SRC_JSON, encoding="utf-8") as f:
    data = json.load(f)

words = [w for w in data["words"] if w.get("type") == "word"]

def words_in(a, b):
    return [w for w in words if w["start"] >= a - 0.05 and w["end"] <= b + 0.35]

segments = []
for (wa, wb) in WINDOWS:
    ws = words_in(wa, wb)
    if not ws:
        segments.append((wa, wb))
        continue
    runs = [[ws[0]]]
    for prev, cur in zip(ws, ws[1:]):
        if cur["start"] - prev["end"] > GAP_SPLIT:
            runs.append([cur])
        else:
            runs[-1].append(cur)
    for i, run in enumerate(runs):
        s = run[0]["start"] - (EDGE_HEAD if i == 0 else HEAD_PAD)
        e = run[-1]["end"] + (EDGE_TAIL if i == len(runs) - 1 else TAIL_PAD)
        segments.append((max(wa - EDGE_HEAD, s), min(wb + EDGE_TAIL, e)))

# merge too-short / overlapping neighbours
merged = [list(segments[0])]
for s, e in segments[1:]:
    if s <= merged[-1][1] + 0.05 or merged[-1][1] - merged[-1][0] < MIN_SEG:
        merged[-1][1] = max(merged[-1][1], e)
    elif e - s < MIN_SEG:
        merged[-1][1] = e  # absorb forward
    else:
        merged.append([s, e])

total = sum(e - s for s, e in merged)
removed = (WINDOWS[-1][1] - WINDOWS[0][0]) - total
print(f"segments: {len(merged)}")
print(f"kept: {total/60:.1f} min   (source content span {(WINDOWS[-1][1]-WINDOWS[0][0])/60:.1f} min, trimmed {removed/60:.1f} min)")

edl = {
    "version": 1,
    "source": "<WORK>/recording.mp4",
    "ranges": [{"start": round(s, 3), "end": round(e, 3)} for s, e in merged],
    "total_duration_s": round(total, 1),
}
with open(f"{EDIT}/edl_full.json", "w", encoding="utf-8") as f:
    json.dump(edl, f, indent=1)
print(f"wrote {EDIT}/edl_full.json")
