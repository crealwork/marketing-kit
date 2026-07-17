"""Silence-cut EDL from a word-level transcript.

Splits speech into segments at inter-word gaps > --gap, pads every edge, snaps
every boundary to a word edge, merges too-short neighbours. Optionally restricts
to keep-windows and subtracts disfluency cuts (scan_fillers.py output).

Usage:
  python gen_edl.py <transcript.json> --source <video> [-o edl.json]
      [--gap 1.75] [--windows windows.json] [--subtract filler_cuts.json]

windows.json: [[start, end], ...]  keep-windows on the source timeline (seconds).
Default is the whole file. Author these by READING the packed transcript.
"""
import argparse, json, sys

sys.stdout.reconfigure(encoding="utf-8")


def subtract_cuts(ranges, cuts, pad=0.03, min_piece=0.25):
    """Remove [cut.start-pad, cut.end+pad] intervals from ranges."""
    out = []
    for s, e in ranges:
        pieces = [(s, e)]
        for c in cuts:
            ca, cb = c["start"] - pad, c["end"] + pad
            nxt = []
            for a, b in pieces:
                if cb <= a or ca >= b:
                    nxt.append((a, b))
                    continue
                if ca > a:
                    nxt.append((a, ca))
                if cb < b:
                    nxt.append((cb, b))
            pieces = nxt
        out.extend(p for p in pieces if p[1] - p[0] >= min_piece)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--source", required=True, help="video path recorded into the EDL")
    ap.add_argument("-o", "--out", default="edl.json")
    ap.add_argument("--gap", type=float, default=1.75, help="split at inter-word silence > this")
    ap.add_argument("--head-pad", type=float, default=0.30)
    ap.add_argument("--tail-pad", type=float, default=0.35)
    ap.add_argument("--edge-head", type=float, default=0.15)
    ap.add_argument("--edge-tail", type=float, default=0.25)
    ap.add_argument("--min-seg", type=float, default=0.8, help="merge segments shorter than this")
    ap.add_argument("--windows", help="JSON [[start,end],...] keep-windows (default: whole file)")
    ap.add_argument("--subtract", help="filler_cuts.json from scan_fillers.py")
    args = ap.parse_args()

    data = json.load(open(args.transcript, encoding="utf-8"))
    words = [w for w in data["words"] if w.get("type") == "word"]
    if not words:
        sys.exit("no words in transcript")

    if args.windows:
        windows = [tuple(w) for w in json.load(open(args.windows, encoding="utf-8"))]
    else:
        windows = [(words[0]["start"], words[-1]["end"])]

    segments = []
    for wa, wb in windows:
        ws = [w for w in words if w["start"] >= wa - 0.05 and w["end"] <= wb + 0.35]
        if not ws:
            segments.append((max(0.0, wa), wb))
            continue
        runs = [[ws[0]]]
        for prev, cur in zip(ws, ws[1:]):
            if cur["start"] - prev["end"] > args.gap:
                runs.append([cur])
            else:
                runs[-1].append(cur)
        for i, run in enumerate(runs):
            s = run[0]["start"] - (args.edge_head if i == 0 else args.head_pad)
            e = run[-1]["end"] + (args.edge_tail if i == len(runs) - 1 else args.tail_pad)
            segments.append((max(0.0, max(wa - args.edge_head, s)), min(wb + args.edge_tail, e)))

    # merge too-short / overlapping neighbours
    merged = [list(segments[0])]
    for s, e in segments[1:]:
        if s <= merged[-1][1] + 0.05 or merged[-1][1] - merged[-1][0] < args.min_seg:
            merged[-1][1] = max(merged[-1][1], e)
        elif e - s < args.min_seg:
            merged[-1][1] = e  # absorb forward
        else:
            merged.append([s, e])
    ranges = [tuple(r) for r in merged]

    if args.subtract:
        cuts = json.load(open(args.subtract, encoding="utf-8"))
        ranges = subtract_cuts(ranges, cuts)

    total = sum(e - s for s, e in ranges)
    span = windows[-1][1] - windows[0][0]
    print(f"segments: {len(ranges)}")
    print(f"kept: {total / 60:.1f} min  (content span {span / 60:.1f} min, trimmed {(span - total) / 60:.1f} min)")

    edl = {"version": 1, "source": args.source,
           "ranges": [{"start": round(s, 3), "end": round(e, 3)} for s, e in ranges],
           "total_duration_s": round(total, 1)}
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(edl, f, indent=1)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
