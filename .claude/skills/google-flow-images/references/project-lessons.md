# Project lessons — running Flow at scale for the Yalom videos

Hard-won from the molly-v2 run (Oct 2026). Read before launching a multi-worker image loop.

## Parallel workers
- One Chrome tab per worker, same Flow project. **Flow chat sessions are shared per project** → each worker uses its own titled chat session and an asset-name prefix (e.g. `ag-` aged, `ms-` mshots, `lb-` library) so downloads/matching never collide.
- Each worker spawns its own independent validator per round; the worker never grades its own images.
- On a session/usage-limit death, workers resume by re-checking disk + their own Chrome tab, not by restarting.

## Quality loop
generate → validator scores (RUBRIC.md: pass ≥ 9.0, no axis < 8) → revised prompt (keep anchors verbatim, change only the defects) → regenerate, ≤ 5 rounds → save winners; log `winners.json` (with `"replaces"` for library swaps). Flagged best-available images are saved but marked, then retried later.

## Failure modes seen
- **2K upscaling fails** ("Upscaling failed!"): validate at 1K, save an interim Lanczos 2752×1536, log in `ratings/pending-2k.json`, retry 2K at most once per 20 min, one worker at a time. Final render needs that file empty (or accept softer frames on Ken Burns ≥ 1.15).
- **Flow 2K has a sparkle/watermark mark**: run `tools/flow_unsparkle.py` (crop) and its `--check` before accepting; `--check` can false-alarm on dark coats.
- **Agent quota exhausted** → switch to manual prompting (works, same quality); don't spin.
- **Vimium in Chrome** swallows stray keys — disable it on labs.google or keys typed into the prompt box misfire.
- **Old shot as reference** makes Flow copy its flat framing — describe the new composition in words instead.
- Sending while the agent is busy silently loses the message — always idle-gate (see `automation.md`).
- Style drift to scowls/smirks and glossy "AI" lighting — see the Natural and Expressions rules in the repo's `CINEMATIC.md`.
