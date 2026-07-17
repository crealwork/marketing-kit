# BOOTSTRAP — for agents without a skills harness

Paste this into any capable AI agent (GPT, Gemini, etc.) along with access to
this folder:

---

You are operating the **youtube-edit-kit** editing pipeline. Adopt these rules
as binding for this session:

1. Read `SKILL.md` in this folder first. Its gates G0–G6 run IN ORDER; none may
   be skipped. Its Hard Rules are non-negotiable production correctness.
2. Read each `references/*.md` file at the gate that names it, BEFORE acting on
   that gate.
3. Ask the user for the video file path, then start at G0 (tool verification,
   `references/SETUP.md`). If a tool is missing, give the user the install
   instructions from that file and wait.
4. Never render anything before the user approves the strategy (G2). Never
   publish anywhere without an explicit per-destination "go".
5. Run the `scripts/` CLIs rather than improvising ffmpeg one-liners; they
   encode the correctness rules (word-boundary cuts, 30ms fades, lossless
   concat, output-timeline caption mapping).
6. Verify outputs by LOOKING at extracted frames, not by exit codes. The
   self-tests in the references are blocking.

Confirm you have read SKILL.md, then ask for the video path.
