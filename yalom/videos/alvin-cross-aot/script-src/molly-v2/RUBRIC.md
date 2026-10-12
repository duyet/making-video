# molly-v2 image rubric (validator agents)

Score each candidate 0–10 on each axis, then a weighted total (out of 10).

| Axis | Weight | 10 means |
|---|---|---|
| Beat match | 25% | Shows exactly the sheet beat for its line (who, where, action, era 1960s/1982/present). |
| Character consistency | 20% | Faces, hair, glasses and outfits match the cast anchors / AOT-CAST-SHEET and the existing redraws; age right for the era (present day: Yalom ≈80, Alvin ≈70, Monica ≈60). |
| Cinematic artistry | 20% | Reads as a frame from a feature film, not an illustration: deliberate shot size and lens (see CINEMATIC.md), layered depth (foreground framing, midground subject, background), motivated light with shape (rim/back light, window shafts, practicals, silhouettes), strong composition (thirds, leading lines, negative space), mood that serves the beat; natural and candid, not "AI-looking" (see CINEMATIC.md, "Natural"). |
| Style consistency | 10% | Same AOT (Wit Studio) cel look, palette and line weight as the existing `assets/redraw` set; it would not stand out in a cut. |
| Technical quality | 15% | No extra or melted fingers/limbs, no warped faces or eyes, clean perspective, sharp at 1920×1080, no artifacts. |
| Readability & clean frame | 10% | Subject readable even in low-key light, room for a slow Ken Burns move (subject not at the very edge), **no text, letters, logos or watermark/sparkle** (except the embroidered "Alvin Cross" where asked). |

**Pass:** total ≥ 9.0 and no axis below 8 (bar raised by the user, 2026-10-11). **Hard fail** (score 0 overall): readable text or a watermark, a wrong-gender or clearly wrong-person face, or a broken hand/face in the focal area.

For every candidate below the pass bar, write a **revised prompt**: keep the anchors verbatim, then change only what fixes the listed defects (be concrete: "both hands hidden in pockets", "camera at eye level, face fills the left third", "remove the wall calendar").

Output per round: `script-src/molly-v2/ratings/round-<n>.json`:
`[{"shot":"M01","file":"…","scores":{"beat":8,"character":7,"cinematic":8,"style":9,"technical":6,"readability":9},"total":7.6,"pass":false,"defects":["…"],"revised_prompt":"…"}]`
