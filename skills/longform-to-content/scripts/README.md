# scripts/ — reference implementations (S02 webinar, 2026-07-10)

These are WORKING scripts from the proven run, not generic templates. To reuse:
copy into `<work>/edit/`, then adapt ONLY the constants at the top of each file —
absolute paths, layout geometry (measure per recording! PIPELINE.md §2), brand tokens
(from the project DESIGN.md), and the keep-window timestamps.

| Script | Stage | Adapt |
|---|---|---|
| measure_layout.py | Layout geometry (READY TO RUN, no adaptation) | — |
| scan_slides.py | Slide-change timeline (READY TO RUN) | crop string from measure_layout |
| gen_edl.py | EDL: keep-windows + silence splits | paths, WINDOWS list, thresholds rarely |
| scan_fillers.py | Disfluency cut candidates | FILLERS/EMPHASIS sets per language |
| corrections.py | ASR fix dictionary (worked KR example) | rebuild per brand/domain — scan the transcript |
| build_assets.py | PIP mask/shadow, intro/outro cards | crop coords, erase box |
| render_full.py | Relayout render + concat + cards | paths, crop/PIP geometry, BGM |
| gen_final_v4.py | Cold open (thumbnail-matched order) + captions + burn | HL clips, ASS style line |
| gen_srt.py | SRT + YouTube chapters on output timeline | chapter list |
| gen_shorts.py | 6 verticals + endcard + `--captions-only` | SHORTS list (ranges/titles/keywords), brand tokens |
| compose_thumbs.py | (legacy) illustration+PIL thumbnails | prefer THUMBNAILS.md full-generation route |
| publish.py | Zernio upload + publish/schedule | account IDs, copy, dates; keep the safety rules |

Do not run any of these unmodified against a new recording — the hardcoded timestamps
belong to the S02 source. The PIPELINE.md steps tell you which values to re-derive.

## Placeholder legend (replace before running)

- `<WORK>` — absolute path to the project work dir (contains recording.mp4, edit/, final/)
- `<FONTS_DIR>` — where your .ttf/.otf layout fonts live (Windows user fonts:
  `%LOCALAPPDATA%\Microsoft\Windows\Fonts`; macOS: `~/Library/Fonts`; Linux: `~/.fonts`)
- `<BGM_FILE>` — your intro/outro music track (see PIPELINE.md §6 for selection metric)
