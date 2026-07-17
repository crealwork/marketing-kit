# BOOTSTRAP — paste this into any agent without a skills harness

For agents (Hermes/GPT, Gemini, custom) that don't auto-load SKILL.md. Paste verbatim
as the task prompt, filling the two blanks:

---

You are executing the `longform-to-content` pipeline from this repository:
https://github.com/crealwork/longform-to-content (clone it locally first).

INPUT RECORDING: `<absolute path to the video file>`
USER'S GOAL: `<e.g. "full edit + shorts + thumbnails, then schedule to YouTube/IG">`

Operating rules — these override your defaults:
1. Read `SKILL.md` first. Execute gates G0→G4 IN ORDER. Every rule marked mandatory
   is mandatory — a skipped self-test is a failed task, not a shortcut.
2. Before each gate, read its reference file completely
   (references/SETUP → BRAND → PIPELINE + CAPTIONS + SHORTS → THUMBNAILS + YOUTUBE → PUBLISHING).
3. Adapt scripts/ reference implementations by replacing the `<PLACEHOLDER>` constants
   (legend in scripts/README.md). Never run them unmodified; never rewrite from
   scratch what a script already implements.
4. At the strategy-confirmation step (PIPELINE.md §2) STOP and present the plan to the
   user; do not render before their OK. Never publish or schedule anything without
   explicit per-destination approval.
5. Every visual self-test says READ the image — actually load and look at the extracted
   frames. If you cannot view images in this environment, you MUST NOT skip the gate:
   extract the specified frames, send them to the user, and ask the exact yes/no
   questions from the checklist instead.
6. When a number in the skill conflicts with your instinct, the number wins. When the
   user's explicit instruction conflicts with the skill, the user wins — note the
   deviation in the project log.
7. Keep a running `edit/project.md` log: strategy, decisions, reasoning, outstanding.

Start with Gate 0 now: run every VERIFY command in references/SETUP.md and report a
pass/fail table before touching the recording.

---

## Agent capability requirements (check before assigning this task)

| capability | needed for | if missing |
|---|---|---|
| shell + ffmpeg/Python execution | everything | cannot run this skill |
| image viewing (multimodal input) | all visual self-tests, thumbnail checks | fallback per rule 5 above — user becomes the eyes; slower but valid |
| long-running processes (5–15 min renders) | render + burn passes | run steps sequentially with progress prints; no step needs >20 min |
| internet | tool installs, Zernio/gpt-image-2/Nano Banana API APIs | offline: edit-only mode, manual publish handoff |
