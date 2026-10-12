# Flow image worker brief (molly-v2), 2026-10-11 recovery

Paths are relative to `/Users/duet/project/make-video/yalom/videos/`. P1 is `alvin-cross-aot`, P3 is `alvin-cross-aot-3p`.

## Read first
- Skill `google-flow-images`. Load it before any Chrome call.
- `alvin-cross-aot/script-src/molly-v2/RUBRIC.md`: pass is ≥9.0 with no axis below 8. Hard fails are readable text, a watermark, a wrong face, or broken hands.
- `CINEMATIC.md`: shot language; the "Natural, not AI-looking" and "Expressions" rules (no smirks, no glaring in warm beats, nobody looks into the lens).
- `SHEET.md` and `BEATS.md`: what each line needs.
- `NEW-SHOTS-2026-10-11.md`, for S shots.
- Memory: `/Users/duet/.claude/projects/-Users-duet-project-make-video-yalom/memory/flow-outpaint-widen.md`.
- Your prompts, ratings and candidates from earlier rounds are in `ratings/*.json` and `alvin-cross-aot/assets/flow2k_raw/molly-v2/<SHOT>/`. Build on them.

## Loop for each shot
1. Generate in Flow (Nano Banana) in your OWN Chrome tab: call `tabs_context_mcp` with `createIfEmpty:true`, then make a new tab. Record its ID and use ONLY that tab ID; other workers share the same tab group.
   - Your asset names and prompts carry your prefix.
   - Don't attach the old shot as a reference, because Flow copies its framing.
   - Do attach the character and set references.
2. Download at 1K (the 2K upscale fails). Then run `python3 alvin-cross-aot/tools/flow_unsparkle.py <in> <out>`, which does the default crop and the interim upscale to 2752x1536.
3. **No visible Gemini sparkle, ever.** Run `--check`, and also look at the bottom-right corner at full resolution yourself.
4. **Edge content** (anything important in the right ~12% or the bottom): use the margin-then-crop method.
   - Scale the approved clean 1K image to 0.88 (1211x676) and place it at (0,41) on a flat-grey 1376x768 canvas.
   - Upload it and outpaint ONLY the grey margin.
   - Download, then apply the default crop. The whole picture survives.
5. Validate with a fresh sub-agent with model opus, named `opus-high-validate-<shot>`, and keep it short: one image set per call. If opus is unavailable (limit), use sonnet and name it `sonnet-high-validate-<shot>`. Give it RUBRIC.md, CINEMATIC.md and the beat text. It returns JSON scores.
6. Save only if the new score beats the incumbent. If the incumbent's winners.json score predates the current rubric or art review, re-score it in the same validator call and compare like with like. Saving means:
   - copy the PNG to `assets/redraw/<SHOT>.png` in BOTH P1 and P3;
   - update `ratings/winners.json` (shot, replaces, file, total, scores, minor). When you overwrite an entry, KEEP its existing `replaces` field. Dropping it silently removes the shot from the video;
   - add an entry to `ratings/pending-2k.json`.
7. Take up to 3 rounds per shot. If a shot still misses, save the best image with `"flag"` and move on.
8. **Disk:** convert only YOUR losing candidates to JPEG q90. Never touch other workers' folders.
9. **Report:** when the queue is done, message `main` (the lead) with a short table. Append one line per result to `TODO-molly-v2.md`.

Never run TTS or rendering.

## Save tokens in Chrome (user rule)
- Batch every click, type and wait into ONE `browser_batch` call. Never make one call per action.
- Prefer `find`, `get_page_text` or `javascript_tool`, which return short text, over screenshots and full `read_page` dumps.
- Take a screenshot only to judge a generated image. Never take one to find a button.
- Fetch images with JS (fetch the image URL, then save locally), then judge them from the local downsized file. Don't open large previews in the browser.
- Reuse one prompt template per shot and paste it in a single type action.
- Don't poll a generation every few seconds. Wait about 60 s in one `wait` action, then check once.
- Keep your own context lean: no page dumps in replies, and short reports to `main`.
