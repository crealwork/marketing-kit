# SETUP — Required tools (ALL mandatory before Gate 2)

Run every VERIFY command. If any fails, give the user the matching INSTALL instructions
and stop until it passes. Do not substitute alternatives.

## 1. ffmpeg + ffprobe
- VERIFY: `ffmpeg -version && ffprobe -version`
- INSTALL: https://ffmpeg.org/download.html
  - Windows: `winget install Gyan.FFmpeg` (restart shell)
  - macOS: `brew install ffmpeg`

## 2. Python 3.11+ with Pillow (+ numpy, librosa for BGM analysis)
- VERIFY: `python -c "import PIL, numpy; print('ok')"`
- INSTALL: https://www.python.org/downloads/ then `pip install pillow numpy librosa`
- Windows rule (mandatory): every script starts with
  `sys.stdout.reconfigure(encoding="utf-8")` and runs under `PYTHONUTF8=1`.

## 3. video-use (transcription + edit helpers)
- REPO: https://github.com/browser-use/video-use
- INSTALL: `git clone https://github.com/browser-use/video-use && cd video-use && uv sync`
  (uv: https://docs.astral.sh/uv/getting-started/installation/)
- VERIFY: `uv run python helpers/transcribe.py --help`
- Used for: ElevenLabs Scribe word-level transcription (`helpers/transcribe.py`),
  packed transcripts (`helpers/pack_transcripts.py`). Its SKILL.md hard rules
  (word-boundary cuts, 30ms afades, captions last, cache transcripts) apply here too.

## 4. Transcription backend
DEFAULT (free, local): **whisper.cpp**
- INSTALL: https://github.com/ggml-org/whisper.cpp (release binaries or build);
  download a model — `ggml-large-v3-turbo` for CJK accuracy, `ggml-small` for speed.
- video-use ships `helpers/transcribe_whispercpp.py` which outputs the SAME JSON shape
  as the paid backend, so the whole pipeline is backend-agnostic. Point it via
  `WHISPER_CLI_PATH` / `WHISPER_MODEL_PATH` env vars.
- VERIFY: transcribe a 10s clip → JSON has per-word start/end.
- Limits: no speaker diarization; small models degrade on CJK — use large-v3 for KR.

OPTIONAL UPGRADE (paid): **ElevenLabs Scribe** (`helpers/transcribe.py`)
- Use when the recording has MULTIPLE speakers (Q&A, guests — diarization) or the free
  pass produces heavy ASR errors on domain terms.
- GET: https://elevenlabs.io → Profile → API Keys → store as env `ELEVENLABS_API_KEY`
  (docs reference the NAME only; never write the value anywhere).
- NOTE: ElevenLabs here = speech-to-text ONLY. BGM does NOT come from ElevenLabs —
  it comes from royalty-free libraries (PIPELINE.md §6: Mixkit first).

## 5. Caption fonts (brand-driven — see BRAND.md selection rule)
Priority: (1) the brand's own font IF it has a real Bold weight and passes the 22px
readability floor → use it. (2) Otherwise language defaults:
- Korean: **Pretendard** — https://github.com/orioncactus/pretendard (static Bold for libass)
- Pan-CJK / Japanese / Chinese fallback: Noto CJK — https://github.com/notofonts/noto-cjk
- Latin: Inter — https://rsms.me/inter/
Mechanics (all fonts): libass gets a STATIC bold file in `<work>/edit/assets/fonts/`
referenced with a RELATIVE fontsdir; PIL may use variable fonts with axis weights.
VERIFY: 3s test burn renders glyphs (not boxes) at the target size.

## 6. Image generation (thumbnail base images) — Higgsfield CLI only
- ALL generation goes through the **Higgsfield CLI** (`npm i -g @higgsfield/cli`,
  `higgsfield auth login`). Default model **gpt_image_2**; real-face reference via
  `--image photo.png`. VERIFY BEFORE SPENDING: `higgsfield account status`
  (account email + credits — wrong-account spend is unrecoverable).
- Command pattern + download snippets: the `image-gen` skill in this kit.
- NO FALLBACK to any other route/service — on failure, report to the user.
- Windows: call via full path `%APPDATA%\npm\higgsfield.cmd`.
- Background removal (cutouts for compositing): local `rembg` with the
  `birefnet-portrait` model (`pip install rembg`).

## 7. Zernio (publishing) — verify at Gate 4, see PUBLISHING.md
- VERIFY: `GET https://zernio.com/api/v1/profiles` with `Authorization: Bearer $ZERNIO_API_KEY`
  returns profiles, and `GET /v1/accounts` lists the target platforms.
- No account / key / connected platforms → run the user onboarding in PUBLISHING.md.

## 8. API-call rule (all of the above, Windows)
Emoji-bearing API responses crash subprocess+curl under cp1252. Use Python
`urllib.request` + `.read().decode("utf-8")` for every API call. No exceptions.

## 9. OS portability notes

- The reference scripts were proven on Windows; on macOS/Linux they run as-is once the
  placeholder paths are filled (forward slashes everywhere, no Windows-only APIs).
- `PYTHONUTF8=1` + `sys.stdout.reconfigure` are Windows-critical and harmless elsewhere — keep them.
- Font locations differ per OS (see scripts/README.md legend). libass `fontsdir` stays
  RELATIVE on every OS.
- The `subtitles=` filter colon trap is Windows-drive-letter specific, but relative
  paths are the rule everywhere anyway.
