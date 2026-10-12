# Prompt design — Nano Banana / Imagen / Veo

Write prompts as **full descriptive sentences** (Nano Banana is a Gemini model: it reads prose better than tag
soup), but keep a fixed slot order so nothing is forgotten. Every prompt must stand alone.

## Slot order

1. **Shot id + format** — `[S07] 16:9 cinematic still,`
2. **Art style tokens** — e.g. `hand-drawn anime, clean cel-shading, soft ink linework, muted watercolor
   backgrounds` / `Chinese ink-wash (shuimo), dry-brush texture, rice-paper grain` / `1950s Kodachrome photo, film grain`.
   Same string in every prompt of a project.
3. **Subject + identity anchors** — the character bible line, verbatim (see below).
4. **Action, pose, expression** — one action; restrained expression ("eyes lowered, lips pressed, a quiet
   stillness" beats "sad"). Name hands explicitly when visible.
5. **Setting + period details** — place, era, 2–4 concrete props.
6. **Shot size & camera** — wide / medium / medium close-up / close-up / extreme close-up / insert (object) /
   over-the-shoulder (OTS) / POV; angle (eye level, low, high, top-down, Dutch); lens (24mm wide, 50mm natural,
   85mm portrait shallow DoF, 135mm compressed).
7. **Lighting** — source + quality + direction: "late-afternoon window light from left, soft shadows", "single
   tungsten desk lamp, warm pool of light, dark surroundings", "overcast diffuse".
8. **Palette** — 3–4 colors: "desaturated teal, ochre, ivory, charcoal".
9. **Composition** — subject placement + negative space; for 16:9 video with Ken Burns: "subject in the right third,
   generous headroom and margins on all sides, nothing important within 10% of the edges" (pan/zoom crops 10–20%).
10. **Negatives** — always: "no text, no captions, no letters, no watermark, no logo, no signature, no borders,
    no split panels". Add shot-specific ones ("no modern objects", "no extra people").

Length: 60–140 words. Longer prompts drift; shorter ones lose identity.

## Character bible (2–3 characters, 30+ shots)

Write one anchor line per character and paste it **verbatim** into every prompt that includes them:

> MAYA: a 34-year-old Vietnamese woman, shoulder-length straight black hair tucked behind her left ear, thin oval
> face, small mole under right eye, round tortoiseshell glasses, cream cable-knit sweater, dark grey wool trousers.

Rules:
- Use fixed **age as a number**, hair (length/color/part), face shape, 1–2 unique marks, glasses/jewelry, and a
  **locked wardrobe** per scene/day. Change wardrobe only deliberately and update the bible.
- Same name every time; never paraphrase ("her hair" ≠ re-stating it).
- Make a **reference sheet** first: "character turnaround sheet of MAYA: front, three-quarter, profile, full body,
  neutral grey background, same style tokens". Then attach it as an ingredient / "Add to prompt" for later shots, or
  put it in Agent Instructions with the bible text.
- Two characters in frame: give positions ("MAYA on the left, seated; DR. LEE on the right, standing") and keep each
  anchor complete. Three in frame is the practical limit — prefer OTS or split coverage.
- Re-check identity every batch; when it drifts, generate the next shot as an **edit** of a good shot rather than new.
- Keep style tokens and palette identical project-wide; varying them is the #1 cause of "different character".

## Batch phrasing (agent chat)

One line: `Generate 4 separate 16:9 images (one generation each, no collage), in this order — [S01] <prompt>;
[S02] <prompt>; [S03] <prompt>; [S04] <prompt>. Shared for all: <style tokens>; no text, no captions, no watermark.`
Even with "shared" clauses, put the character anchors inside each shot's prompt.

## Edits vs new images

- **Edit** (keeps composition/identity): select/open the image or reference it ("edit image S07"), then state only the
  change + what to preserve: "Edit S07: change the window light to blue dusk; keep MAYA's face, pose, framing and
  everything else identical; no text." In the editor, lasso the region first for local changes.
- **New** when composition, shot size or camera angle must change — edits rarely move the camera.
- Fix one thing per edit; chained multi-change edits degrade faces.

## Accuracy pitfalls

- **Iron lung (tank respirator)**: patient lies **on their back, face UP**, body sealed inside a horizontal metal
  cylinder; **only the head** protrudes through a **rubber neck collar** at one end; head rests on a small
  padded shelf/pillow; an **angled mirror above the face** lets them see the room; portholes on the tank side, bellows
  beneath/at the foot end. Not sitting, not face-down, no arms outside, no glass dome.
- Hands: specify count and action ("both hands wrapped around a teacup"); avoid hands in extreme close-up.
- Period: name decade + 3 concrete era props; add "no modern objects, no smartphones, no plastic".
- Medical/clinical: real equipment shapes, correct uniforms per era; ask for "historically accurate".
- Text in scene (signs, books): generate blank ("blank spines", "unlabeled sign") — add text later.
- Mirrors/reflections and crowds produce artifacts; keep them simple.

## Veo (video) prompts

subject + one action + setting + camera move (static / slow push-in / pan left / orbit) + lighting + style + duration
feel ("over 8 seconds") + audio cue if wanted + "no text". For animating a still: describe only motion and camera
("gentle steam rising from the cup, slight hair movement, slow push-in; keep the face unchanged").

## Worked examples

**1 — Establishing wide (anime style)**
`[S01] 16:9 cinematic still, hand-drawn anime, clean cel-shading, soft ink linework, muted watercolor backgrounds.
A narrow 1970s San Francisco street on a foggy morning, Victorian row houses, a lone streetcar, wet cobblestones.
Wide shot, eye level, 24mm lens. Soft overcast light, fog diffusing distant buildings. Palette: desaturated teal,
ochre, ivory, charcoal. Streetcar in the left third, open sky and fog in the upper half, generous margins for slow
pan. No people in focus, no modern cars, no text, no captions, no letters, no watermark, no logo, no borders.`

**2 — Two-character medium (consistency)**
`[S14] 16:9 cinematic still, hand-drawn anime, clean cel-shading, soft ink linework, muted watercolor backgrounds.
DR. LEE: a 62-year-old man, thinning grey hair combed back, deep forehead lines, wire-rimmed glasses, brown corduroy
jacket over a pale blue shirt, sits in a worn leather armchair on the right, listening, hands folded. MAYA: a
34-year-old Vietnamese woman, shoulder-length straight black hair tucked behind her left ear, thin oval face, small
mole under right eye, round tortoiseshell glasses, cream cable-knit sweater, dark grey wool trousers, sits on a sofa
on the left, eyes lowered, a quiet stillness. 1970s therapy office, bookshelves with blank spines, a fern, a low
table with a box of tissues. Medium two-shot, slightly high angle, 50mm. Late-afternoon window light from the left,
warm. Palette: ochre, olive, ivory, charcoal. Headroom and side margins for Ken Burns. No text, no captions, no
letters, no watermark, no logo, no extra people.`

**3 — Period-accurate medical (iron lung)**
`[S22] 16:9 cinematic still, hand-drawn anime, clean cel-shading, soft ink linework, muted watercolor backgrounds.
A 1950s polio ward: a 10-year-old boy with short brown hair lies on his back, face up, his whole body sealed inside
a large horizontal cream-colored metal iron lung respirator; only his head protrudes through a snug rubber neck
collar at the end of the tank, resting on a small padded headrest; an angled rectangular mirror mounted above his
face reflects the room; round portholes along the tank side. A nurse in a 1950s white uniform and cap stands beside
him. Medium-wide shot, eye level from the head end at a three-quarter angle, 35mm. Soft cool daylight from tall
windows. Palette: pale mint, cream, steel grey. Boy and tank in the center-right, room space on the left. Historically
accurate; the boy is not sitting, not face down, no arms outside the tank, no glass dome; no text, no captions, no
watermark, no logo.`
