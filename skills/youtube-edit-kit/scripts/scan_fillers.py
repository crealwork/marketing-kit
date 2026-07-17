"""Scan disfluency cut candidates inside kept EDL ranges (conservative rules).

Rules: (1) standalone fillers, (2) abandoned false starts ('--' / trailing '-'),
(3) immediate unigram restart "X, X" (cut first), (4) bigram restart "A B, A B".
Emphasis words are never cut. Output is REVIEW-FIRST: read the printed context
lines before feeding filler_cuts.json into gen_edl.py --subtract.

Expected removal is small (5-30s per hour of speech). Far outside that range
means the rules misfired on this material — stop and inspect, don't apply.

Usage:
  python scan_fillers.py <transcript.json> --edl <edl.json> [-o filler_cuts.json]
"""
import argparse, json, re, sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

FILLERS = {"어", "음", "아", "에", "어어", "으", "엄",           # Korean
           "uh", "um", "erm", "uhm", "mm", "hmm"}                # English
EMPHASIS = {"정말", "너무", "진짜", "계속", "점점", "조금씩", "충분히", "훨씬",
            "very", "really", "so", "just", "more"}


def norm(t):
    return re.sub(r"[,.?!]+$", "", t.strip()).lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--edl", required=True)
    ap.add_argument("-o", "--out", default="filler_cuts.json")
    args = ap.parse_args()

    edl = json.load(open(args.edl, encoding="utf-8"))
    data = json.load(open(args.transcript, encoding="utf-8"))
    words = [w for w in data["words"] if w.get("type") == "word"]

    def in_ranges(w):
        return any(r["start"] - 0.02 <= w["start"] and w["end"] <= r["end"] + 0.02
                   for r in edl["ranges"])

    kept = [w for w in words if in_ranges(w)]
    cuts = []  # (start, end, kind, text, context)

    for i, w in enumerate(kept):
        t = norm(w["text"])
        prev = kept[i - 1] if i > 0 else None
        nxt = kept[i + 1] if i + 1 < len(kept) else None
        gap_b = (w["start"] - prev["end"]) if prev else 9
        gap_a = (nxt["start"] - w["end"]) if nxt else 9
        ctx = " ".join(x["text"] for x in kept[max(0, i - 3):i + 4])

        if t in FILLERS and (w["end"] - w["start"]) >= 0.12 and gap_b >= 0.10 and gap_a >= 0.08:
            cuts.append((w["start"], w["end"], "filler", w["text"], ctx))
            continue
        if ("--" in w["text"] or w["text"].rstrip(",.").endswith("-")) and gap_a >= 0.03:
            cuts.append((w["start"], w["end"], "false-start", w["text"], ctx))
            continue
        if (nxt and norm(nxt["text"]) == t and t not in EMPHASIS and len(t) >= 1
                and w["text"].rstrip().endswith(",") and gap_a < 1.2):
            cuts.append((w["start"], w["end"], "restart-1", w["text"], ctx))

    for i in range(len(kept) - 3):
        a, b, c, d = kept[i:i + 4]
        if (norm(a["text"]) == norm(c["text"]) and norm(b["text"]) == norm(d["text"])
                and b["text"].rstrip().endswith(",")
                and norm(a["text"]) not in EMPHASIS and len(norm(a["text"])) >= 1):
            ctx = " ".join(x["text"] for x in kept[max(0, i - 2):i + 6])
            cuts.append((a["start"], b["end"], "restart-2", a["text"] + " " + b["text"], ctx))

    cuts.sort()
    ded = []
    for c in cuts:
        if ded and c[0] < ded[-1][1]:
            continue
        ded.append(c)

    total = sum(c[1] - c[0] for c in ded)
    print(Counter(c[2] for c in ded))
    print(f"{len(ded)} cuts, {total:.1f}s removed\n")
    for c in ded[:80]:
        print(f"[{c[0]:8.2f}] {c[2]:<12} '{c[3]}'   ...{c[4]}...")
    json.dump([{"start": c[0], "end": c[1], "kind": c[2], "text": c[3]} for c in ded],
              open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nwrote {args.out} — REVIEW the lines above, then re-run gen_edl.py --subtract {args.out}")


if __name__ == "__main__":
    main()
