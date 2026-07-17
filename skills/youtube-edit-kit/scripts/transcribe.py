"""Word-level verbatim transcription via faster-whisper (free, local, no API key).

Every script in this kit reads the same JSON shape:
  {"language": "ko", "duration": 123.4,
   "words": [{"type": "word", "text": "hello", "start": 0.42, "end": 0.98}, ...]}

Also writes a packed phrase view (<name>.packed.md) — the reading view for humans
and agents. Cached per source: existing JSON is never overwritten (delete to redo).

Usage:
  python transcribe.py <video> [--edit-dir DIR] [--model large-v3] [--language ko]
"""
import argparse, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")


def pack(words, path):
    lines, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        gap = (nxt["start"] - w["end"]) if nxt else 99
        if gap >= 0.7 or w["text"].rstrip().endswith((".", "?", "!")):
            t = cur[0]["start"]
            stamp = f"[{int(t // 60):02d}:{int(t % 60):02d}]"
            lines.append(f"{stamp} " + " ".join(x["text"] for x in cur))
            cur = []
    if cur:
        t = cur[0]["start"]
        lines.append(f"[{int(t // 60):02d}:{int(t % 60):02d}] " + " ".join(x["text"] for x in cur))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--edit-dir", default=None, help="output dir (default: <video dir>/edit)")
    ap.add_argument("--model", default="large-v3",
                    help="faster-whisper model: large-v3 (CJK accuracy) | small (speed)")
    ap.add_argument("--language", default=None, help="ISO code; autodetect if omitted")
    args = ap.parse_args()

    edit = args.edit_dir or os.path.join(os.path.dirname(os.path.abspath(args.video)) or ".", "edit")
    tdir = os.path.join(edit, "transcripts")
    os.makedirs(tdir, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.video))[0]
    out_json = os.path.join(tdir, base + ".json")
    if os.path.exists(out_json):
        print(f"cached: {out_json}  (delete the file to re-transcribe)")
        return

    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, compute_type="auto")
    segments, info = model.transcribe(
        args.video, language=args.language,
        word_timestamps=True, condition_on_previous_text=False)

    words = []
    for seg in segments:
        for w in seg.words or []:
            t = w.word.strip()
            if t:
                words.append({"type": "word", "text": t,
                              "start": round(w.start, 3), "end": round(w.end, 3)})

    data = {"language": info.language, "duration": round(info.duration, 2), "words": words}
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    pack(words, os.path.join(tdir, base + ".packed.md"))
    print(f"{len(words)} words  lang={info.language}  -> {out_json}")


if __name__ == "__main__":
    main()
