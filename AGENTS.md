# AGENTS.md

Guidance for coding agents (Claude Code, Codex, …) working in this repo. `CLAUDE.md` imports this file.

## What this repo is

Narrated, image-driven videos (Vietnamese VO) built with **HyperFrames** (HTML → MP4), **ElevenLabs** TTS and **Google Flow** (Nano Banana) stills. Current work: `yalom/` — "Thank You, Molly" (Yalom / Alvin Cross), script id `molly-v2`.

```
yalom/videos/
  alvin-cross/           original version      ┐ each is a standalone HyperFrames project
  alvin-cross-aot/       1p (first-person) AOT │ (index.html, hyperframes.json, package.json,
  alvin-cross-aot-3p/    3p (third-person) AOT ┘  narration/, tools/, assets/, renders/)
  tools/cost.py          Claude-token + ElevenLabs credit snapshot
  TODO-molly-v2.md       running log — read the tail before continuing work
yalom/ref/               reference images (book pages, redraw refs), local only
.claude/skills/          project skills (see below)
```

Per project, per script: `script-src/<script>/` holds `SHEET.md` (source of truth), `RUBRIC.md`, `CINEMATIC.md`, `BOOK-FACTS.md`, `ratings/`; `narration/scripts/<script>/` holds `lines.json`, `shots.json`, `script.json`, `slots.json`.

## Before you do anything — load skills

Skills live in `.claude/skills/` (project-local; do not move them back to `~/.claude`). **Invoke the relevant skill before writing or changing anything:**

| Task | Skill |
|---|---|
| Any video / composition / render / preview | `hyperframes` (router) → `hyperframes-core`, `-animation`, `-keyframes`, `-creative`, `-cli`, `-audio`, `-registry`, `-studio` |
| Longer / multi-scene custom piece | `general-video` · short motion graphic → `motion-graphics` · footage/images treatment → `media-use` |
| Voice-over, TTS, line timing | `vo-narration` |
| Quality bar, storyboard, shot language, review | `make-good-video` |
| Stills / Veo clips from Google Flow (Chrome automation) | `google-flow-images`, `google-flow-video` |

Never write composition HTML from generic web knowledge — HyperFrames has its own rules (`window.__timelines`, `data-*` timing, seek-safe motion).

## Commands

Run inside a video project dir (`yalom/videos/alvin-cross-aot-3p`, …). `npm install` once per project.

```bash
npm run check                         # lint + runtime + layout + motion + contrast — must be clean before render
npx hyperframes preview --background  # Studio preview (agent-safe); --status / --stop. Never `npm run dev` in a tool shell
python3 narration/tts.py <script> <voice>   # ElevenLabs takes (spends credits — see rules)
python3 narration/fit.py <script>           # fit VO to shared slots + cues
QUALITY=standard sh tools/rebuild.sh <script> visuals   # build + picture render
sh tools/rebuild.sh <script> mux all                    # mux each voice → renders/
python3 ../tools/cost.py                     # token + credit snapshot (needs ELEVENLABS_API_KEY)
```

Pipeline: `tts.py → fit.py → build.py → hyperframes render → mux.py`. `hyperframes@0.8.143` is pinned in each `package.json`; upgrade with `npx hyperframes@latest upgrade --project . --check`, don't hand-edit pins.

## Rules

- **Credits & quota:** never run TTS or Flow generation in bulk without the user saying the script/storyboard is final. ElevenLabs/Flow quota is limited; on exhaustion stop, log the reset date + exact resume command in `TODO-<script>.md`.
- **Secrets:** `ELEVENLABS_API_KEY` etc. come from the environment. Never print, write or commit them.
- **Source of truth order:** user's `SHEET.md` > `BOOK-FACTS.md` (the book) > agent ideas. A user choice that differs from the book is kept, not "fixed".
- **Keep the log:** append dated one-liners (decision · why · next step) to `yalom/videos/TODO-molly-v2.md`. Don't rewrite history.
- **Don't rebuild what exists:** reuse library shots/redraws (`assets/redraw`, `winners.json` `replaces` map) before generating new images. Old scripts must stay byte-identical when changing `build.py` / `motion.py` / `fit.py`.
- **Parallel agents:** Chrome/Flow workers each use their own tab, chat session and asset prefix. Never run builds/renders concurrently in parallel sub-agents (OOM); verify once after merge.
- **Done means verified:** `npm run check` clean, length on target, no black gaps, cues land, loudness matches earlier renders (full list in `make-good-video`). Say what was skipped.

## Git

- Remote: `git@github.com:duyet/making-video.git`, branch `main`.
- Semantic commits (`feat(yalom): …`, `fix(vo): …`, `chore(skills): …`), simple English, one logical change each. No `Claude-Session` trailer.
- **Large media is gitignored** (~9 GB: mp4/mov/png/jpg/webp/heic/mp3/wav, `renders/`, `node_modules/`, `snapshots/`, caches, `narration/**/raw/`). Only source, scripts, JSON, docs, fonts and skills are tracked — images and renders exist **only on the author's machine**; don't assume a fresh clone can render. Never `git add -f` media.
