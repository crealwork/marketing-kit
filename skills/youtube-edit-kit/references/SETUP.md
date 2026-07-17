# SETUP — required tools (verify ALL before editing)

Run every VERIFY command. If any fails, give the user the matching INSTALL
instructions and stop until it passes. Do not substitute alternatives.

## 1. ffmpeg + ffprobe
- VERIFY: `ffmpeg -version && ffprobe -version`
- INSTALL: https://ffmpeg.org/download.html
  - Windows: `winget install Gyan.FFmpeg` (restart shell)
  - macOS: `brew install ffmpeg`

## 2. Python 3.11+ with faster-whisper
- VERIFY: `python -c "import faster_whisper; print('ok')"`
- INSTALL: https://www.python.org/downloads/ then `pip install faster-whisper`
- First transcription downloads the model (~1.5GB for large-v3). `--model small`
  is faster but degrades on CJK — use large-v3 for Korean/Japanese/Chinese.
- Windows rule (mandatory): run scripts under `PYTHONUTF8=1`; every kit script
  already starts with `sys.stdout.reconfigure(encoding="utf-8")`.

## 3. Caption font
Priority: (1) the user's brand font IF it has a real Bold weight → use it.
(2) Otherwise language defaults:
- Korean: **Pretendard** — https://github.com/orioncactus/pretendard (static Bold)
- Pan-CJK fallback: Noto CJK — https://github.com/notofonts/noto-cjk
- Latin: Inter — https://rsms.me/inter/
Mechanics: libass needs a STATIC bold file, referenced via a RELATIVE `fontsdir`
(`gen_shorts.py --fontsdir fonts`). Windows absolute `C:` paths break the
`subtitles=` filter at the colon. Variable fonts render at default weight in
libass — don't use them for burns.
VERIFY: burn a 3s test clip → glyphs render (not boxes) at target size.

## 4. Optional upgrades (NOT required for the basic pipeline)
- **whisper.cpp** (https://github.com/ggml-org/whisper.cpp) — alternative free
  backend; **ElevenLabs Scribe** (paid) — multi-speaker diarization + better
  verbatim fillers. Key via env `ELEVENLABS_API_KEY` only; never write the value
  into any file.
- **yt-dlp** — only if the source arrives as a URL instead of a file.

## 5. API-call rule (Windows)
Emoji-bearing API responses crash subprocess+curl under cp1252. Use Python
`urllib.request` + `.read().decode("utf-8")` for every API call. No exceptions.

## 6. OS portability
Scripts are OS-neutral (forward slashes, no Windows-only APIs). `PYTHONUTF8=1`
and the stdout reconfigure are Windows-critical and harmless elsewhere — keep them.
