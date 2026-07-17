"""Mine ASR-correction candidates: proper nouns, jargon, acronyms, spelled-out
numbers, inconsistent spellings. Mechanical narrowing only — JUDGMENT stays with
the operating agent (the AI running this skill), who reviews every candidate
with its own knowledge and asks the user for canonical spellings it can't verify.

The corrections pass is BLOCKING: captions never burn without a reviewed
corrections.json (an empty [] is valid only after this review actually happened).

Usage:
  python scan_terms.py <transcript.json> [-o corrections_todo.md]
"""
import argparse, json, re, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

KR_NUM = re.compile(r"^[일이삼사오육륙칠팔구십백천만억조]{2,}$")
EN_NUM = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve", "twenty", "thirty", "forty", "fifty",
          "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "million",
          "billion", "percent"}
REPEAT_SYL = re.compile(r"^(..?)\1+$")  # onomatopoeia-ish: 쿵쿵, 하하하, boom-boom


def norm(t):
    return re.sub(r"[,.?!]+$", "", t.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("-o", "--out", default="corrections_todo.md")
    args = ap.parse_args()

    data = json.load(open(args.transcript, encoding="utf-8"))
    words = [w for w in data["words"] if w.get("type") == "word"]

    def ctx(i, span=3):
        return " ".join(x["text"] for x in words[max(0, i - span):i + span + 1])

    # A. latin-bearing tokens, grouped by latin core -> catches brand/tech terms
    #    and flags inconsistent spellings (GPT를 / gpt / Gpt = one group, 3 forms)
    latin_groups = defaultdict(list)  # core -> [(i, surface)]
    for i, w in enumerate(words):
        cores = re.findall(r"[A-Za-z][A-Za-z0-9.\-]*", w["text"])
        for core in cores:
            latin_groups[core.lower()].append((i, norm(w["text"])))

    # B. spelled-out numbers
    numbers = []
    for i, w in enumerate(words):
        t = norm(w["text"])
        if KR_NUM.match(t) or t.lower() in EN_NUM:
            numbers.append(i)
    # collapse adjacent indices into one report line ("ninety three percent")
    num_runs = []
    for i in numbers:
        if num_runs and i - num_runs[-1][-1] == 1:
            num_runs[-1].append(i)
        else:
            num_runs.append([i])

    # C. acronym runs: >=2 consecutive single-latin-letter tokens ("C R M")
    acro_runs, run = [], []
    for i, w in enumerate(words):
        if re.fullmatch(r"[A-Za-z][,.?!]?", w["text"].strip()):
            if run and i - run[-1] != 1:
                run = []
            run.append(i)
            if len(run) == 2:
                acro_runs.append(run)
        else:
            run = []

    # D. onomatopoeia / interjection-ish repeated syllables
    onomat = [i for i, w in enumerate(words)
              if len(norm(w["text"])) >= 2 and REPEAT_SYL.match(norm(w["text"]))]

    lines = ["# Correction candidates — review EVERY line with your own knowledge",
             "",
             "For each candidate decide: correct as-is / needs a corrections.json",
             "pair / ask the user for the canonical spelling. Candidates are hints;",
             "pure-hangul ASR errors (챗 피티, 크램) only surface by READING the",
             "packed transcript — this scan does not replace that read.", ""]

    lines.append("## A. Latin/brand terms (jargon, proper nouns)")
    for core, hits in sorted(latin_groups.items(), key=lambda kv: -len(kv[1])):
        forms = sorted({s for _, s in hits})
        flag = "  <-- INCONSISTENT SPELLING, unify" if len(forms) > 1 else ""
        i = hits[0][0]
        lines.append(f"- `{core}` x{len(hits)} forms={forms}{flag}  e.g. [{words[i]['start']:.1f}s] ...{ctx(i)}...")

    lines.append("\n## B. Spelled-out numbers (convert via explicit pairs only)")
    for r in num_runs:
        i = r[0]
        phrase = " ".join(norm(words[j]["text"]) for j in r)
        lines.append(f"- `{phrase}`  [{words[i]['start']:.1f}s] ...{ctx(i)}...")

    lines.append("\n## C. Possible spelled acronyms")
    for r in acro_runs:
        i = r[0]
        lines.append(f"- `{' '.join(words[j]['text'] for j in r)}`  [{words[i]['start']:.1f}s] ...{ctx(i)}...")

    lines.append("\n## D. Onomatopoeia / repeated syllables (check spelling + styling)")
    for i in onomat:
        lines.append(f"- `{norm(words[i]['text'])}`  [{words[i]['start']:.1f}s] ...{ctx(i)}...")

    counts = {"latin": len(latin_groups), "numbers": len(num_runs),
              "acronyms": len(acro_runs), "onomatopoeia": len(onomat)}
    with open(args.out, "w", encoding="utf-8-sig") as f:  # BOM: Windows console-safe
        f.write("\n".join(lines) + "\n")
    print(f"candidates: {counts}  -> {args.out}")
    print("NEXT (blocking, in order):")
    print("  1. READ every candidate above + the FULL packed transcript (CAPTIONS.md §4).")
    print("  2. Resolve with your own knowledge; ASK THE USER for spellings you can't verify.")
    print("  3. Write corrections.json (ordered [[wrong, right], ...], longest-first).")
    print("  4. Smoke-test on 15-20 transcript lines, THEN pass --corrections to gen_srt/gen_shorts.")


if __name__ == "__main__":
    main()
