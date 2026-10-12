---
name: vo-narration
description: >-
  Write, generate and fit Vietnamese voice-over (VO) for the narrated videos in this repo with ElevenLabs
  (eleven_v3) — lines.json, tts.py, fit.py, voices, tempo, sfx, loudness, credit/quota rules. Use WHENEVER the
  task touches narration, VO, TTS, voices, line timing, "naturalise the script", retakes, or running
  tts.py / fit.py / mux.py — even if the user only says "re-record", "voice" or "narration".
---

# VO narration (ElevenLabs, Vietnamese)

Pipeline per video project (e.g. `yalom/videos/alvin-cross-aot-3p/`):
`tts.py` → `fit.py` → `build.py` → `hyperframes render` → `mux.py`. Run from the project dir.

| Step | Command | What it does |
|---|---|---|
| TTS | `python3 narration/tts.py <script> <voice> [id,id]` | Raw 1x takes into `narration/scripts/<script>/<voice>/raw/`. Only lines with no take or changed text are generated; listed ids are always retaken. |
| Fit | `python3 narration/fit.py <script>` | Shared slot timeline across voices (`slots.json`), per-voice fitted mp3 + alignment, shot cues placed at the median cue time. |
| Build/render/mux | `QUALITY=standard sh tools/rebuild.sh <script> visuals` then `sh tools/rebuild.sh <script> mux all` | Picture render, then mux each voice onto it → `renders/`. |

## Rules

- **Credits are real money.** `ELEVENLABS_API_KEY` comes from the environment; never print or commit it. Check the balance with `python3 yalom/videos/tools/cost.py` before a batch. **Never run TTS until the user says the script/storyboard is final** — every text edit re-spends credits for that line.
- Voices live in `narration/voices.json` (`thanh` tempo 1.15, `duc-huy` tempo 1.3, model `eleven_v3`, `language_code: vi`). Change voices/tempo there, not inline.
- `lines.json` is the source of truth: `{id, text}` per line; ids (`a01`…`c08`) are stable and shared with `shots.json` cues and `script.json`. Edit text → only that line is retaken.
- **Write for the ear, in natural Vietnamese**: short spoken sentences, no written-style clauses. Names and loanwords (e.g. "X-quang", "Panama", "Molly") must be listen-checked after TTS — retake with respelled text if wrong.
- Stay faithful to the source material (the book). Facts changed in VO must be re-checked against `BOOK-FACTS.md` / `book-fixes.md` in `script-src/<script>/`.
- Word budget ≈ 2.7–3 words/s at tempo; a line that is too long for its sheet slot stretches the timeline (fit.py) — shorten the text rather than speeding the voice past `HI=1.12`.
- 429 from ElevenLabs = concurrency limit; `tts.py` already backs off. Quota exhausted → stop, log it in the TODO file with the reset date and the exact resume command; do not switch voices silently.
- After fitting: verify total length vs. the target, no black/silent gaps, cues land on their words, loudness matches earlier renders.
