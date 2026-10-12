---
name: make-good-video
description: >-
  The quality playbook for the narrated, image-driven videos in this repo (HyperFrames + Google Flow stills +
  ElevenLabs VO): storyboard-first process, shot language, scoring rubric (pass bar), natural-not-AI-looking
  rules, expression/face rules, pacing and QA. Use WHENEVER planning, reviewing, scoring or improving a video,
  its storyboard or its images — "make it better", "more cinematic", "review the storyboard", "why does it look AI".
---

# How to make a good video here

Order of work: **sheet (source of truth) → script/VO text → shots plan → images → storyboard score → TTS → build → render → QA.** Do not spend VO credits or render time before the storyboard passes.

## 1. Source of truth first
- Each video has a `script-src/<script>/SHEET.md` (the user's beat sheet) — scoring and edits are measured against it, not against taste. Facts come from the source book (`BOOK-FACTS.md`); a user choice that differs from the book is **kept** and noted, not "fixed".
- Keep a running log in `yalom/videos/TODO-<script>.md` (dated lines: decision, why, next step, resume command). Append, don't rewrite.

## 2. Storyboard
- One line per VO line; each line lists its shots, cues, camera move, transition (`cut` 0 / `dissolve` ~1.0–1.6 s / seconds), `hold_after`.
- **Variety rule:** no two adjacent shots with the same size and angle; any line with 2+ shots mixes ≥2 sizes; every act has an extreme wide, an extreme close-up/insert, and a frame-within-frame.
- Score the storyboard per line 0–10 (coverage 30, VO fit 20, image 20, cut logic 15, continuity 15). **Pass ≥ 9.0.** Re-score after every image or script change.

## 3. Images (Google Flow stills → see `google-flow-images`)
- Pass bar per image: weighted total **≥ 9.0 and no axis < 8** (beat 25, character 20, cinematic 20, style 10, technical 15, readability 10). Hard fail (0): readable text/watermark/sparkle, wrong-person face, broken hands/face in the focal area.
- Name shot size, lens, composition, light and depth in every prompt; repeat full character anchors every time (the agent doesn't carry identity).
- **Natural, not AI-looking:** candid in-between moments, one motivated light, matte shading, real age/asymmetry on faces, lived-in props. Avoid posed symmetry, everyone facing camera, rim light on every edge, god-rays + dust + bloom stacked, ageless glamour faces, decorative hands.
- **Faces:** name the emotion with concrete cues (brows/eyes/mouth/jaw). The AOT style defaults to scowls and smirks — hard fails: heavy-lidded closed-mouth smirk, glaring when the beat is warm/shocked/ashamed, staring into the lens.
- Leave room for a slow Ken Burns move (subject not on the edge). Don't attach the old shot as a reference when redrawing (Flow copies its flat framing).
- Independent validator scores each round (≤5 rounds); save ratings under `script-src/<script>/ratings/`.

## 4. Pacing & motion
- Motion is seek-safe HyperFrames (see `hyperframes-animation`, `hyperframes-keyframes`): still / push / drift / pull / rise-fall mix per `MOTION.json`; avoid the same move twice in a row.
- Cuts land on the cue word (`LEADIN` ≈ 0.25 s before it). Let key emotional beats breathe with a silent `hold_after` (3–6 s) instead of more VO.
- Real footage/image look changes go through `media-use` → `references/media-treatments.md`, never ad-hoc CSS filters.

## 5. QA before calling it done
`npx hyperframes check` clean · target length met (e.g. ≈3:00–3:30) · no black gaps · cues land · loudness matches earlier renders · contact sheet reviewed · no pending 1K→2K upscales left in `ratings/pending-2k.json` (soft frames on zooms ≥1.15) · outputs only in `renders/` (gitignored).
