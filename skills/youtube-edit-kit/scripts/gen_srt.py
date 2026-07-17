"""Master SRT on the OUTPUT timeline of the cut + YouTube chapters.

Timing always comes from the ORIGINAL source transcript mapped through the EDL
piece table (out = t - piece.src_start + piece.out_offset). Never re-transcribe
an edited file. Corrections apply AFTER chunking, to every surface.

Usage:
  python gen_srt.py <transcript.json> --edl <edl.json> [-o cut.srt]
      [--offset 0.0]            # leading content (intro card) before segment 1
      [--chunk-chars N]         # cue close length; default 26 CJK / 42 Latin
      [--corrections corr.json] # ordered [["wrong","right"], ...] longest-first
      [--chapters chapters_src.txt]  # lines: "<src_seconds> <label>" -> chapters.txt
"""
import argparse, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")


def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = int(x % 60)
    ms = int(round((x - int(x)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--edl", required=True)
    ap.add_argument("-o", "--out", default="cut.srt")
    ap.add_argument("--offset", type=float, default=0.0)
    ap.add_argument("--chunk-chars", type=int, default=None)
    ap.add_argument("--corrections", default=None)
    ap.add_argument("--chapters", default=None)
    args = ap.parse_args()

    edl = json.load(open(args.edl, encoding="utf-8"))
    data = json.load(open(args.transcript, encoding="utf-8"))
    words = [w for w in data["words"] if w.get("type") == "word"]

    chunk_chars = args.chunk_chars or (26 if data.get("language") in ("ko", "ja", "zh") else 42)

    corrections = []
    if args.corrections:
        corrections = json.load(open(args.corrections, encoding="utf-8"))

    def correct(text):
        for wrong, right in corrections:
            text = text.replace(wrong, right)
        return text

    # source -> output piece table, from FINAL concat order
    pieces = []
    t = args.offset
    for r in edl["ranges"]:
        pieces.append((r["start"], r["end"], t))
        t += r["end"] - r["start"]

    def to_out(src):
        for a, b, off in pieces:
            if a <= src <= b:
                return off + (src - a)
        return None

    def piece_out_end(src):
        for a, b, off in pieces:
            if a <= src <= b:
                return off + (b - a)
        return None

    # words inside kept pieces only — cut words vanish from captions too
    kept = []
    for a, b, off in pieces:
        kept.extend(w for w in words if w["start"] >= a - 0.02 and w["end"] <= b + 0.02)

    subs, cur = [], []
    for i, w in enumerate(kept):
        cur.append(w)
        text = " ".join(x["text"] for x in cur)
        nxt = kept[i + 1] if i + 1 < len(kept) else None
        gap = (nxt["start"] - w["end"]) if nxt else 99
        if len(text) >= chunk_chars or re.search(r"[.?!]$", w["text"]) or gap >= 0.7:
            st = to_out(cur[0]["start"])
            en = to_out(cur[-1]["end"])
            if st is not None and en is not None and en > st:
                # +0.25s reading tail, clamped inside the piece (never cross a cut)
                pe = piece_out_end(cur[-1]["end"]) or en
                subs.append([st, min(en + 0.25, st + 7.0, pe), correct(text)])
            cur = []

    # overlap clamping
    for i in range(len(subs) - 1):
        subs[i][1] = min(subs[i][1], subs[i + 1][0] - 0.02)

    with open(args.out, "w", encoding="utf-8") as f:
        for i, (st, en, text) in enumerate(subs, 1):
            f.write(f"{i}\n{srt_time(st)} --> {srt_time(en)}\n{text}\n\n")
    print(f"SRT: {len(subs)} cues -> {args.out}")

    if args.chapters:
        out_ch = os.path.join(os.path.dirname(os.path.abspath(args.out)) or ".", "chapters.txt")
        with open(args.chapters, encoding="utf-8") as f:
            rows = [ln.strip().split(" ", 1) for ln in f if ln.strip()]
        with open(out_ch, "w", encoding="utf-8") as f:
            for src_s, label in rows:
                src = float(src_s)
                o = 0.0 if src == 0 else to_out(src)
                if o is None:  # chapter mark fell in a cut — snap to nearest piece start
                    o = min((abs(src - a), off + max(0.0, src - a)) for a, b, off in pieces)[1]
                f.write(f"{int(o // 60)}:{int(o % 60):02d} {label}\n")
        print(f"chapters -> {out_ch}")


if __name__ == "__main__":
    main()
