# Cinematic shot language for molly-v2 prompts

Every Flow prompt names the **shot size, lens/camera, composition, light and depth** explicitly, then the beat, anchors and [STYLE]. Append to [STYLE]: "cinematic anime film still, anamorphic widescreen composition, painterly backgrounds with atmospheric perspective, motivated dramatic lighting, shallow depth of field, film grain".

## Vocabulary to pick from
- **Size:** extreme wide (figure small in a big world) · wide · medium-wide · medium · medium close-up · close-up · extreme close-up (eyes, hands, an object) · insert.
- **Camera:** low angle (power, dread) · high angle / top shot (smallness, isolation) · eye level (intimacy) · over-the-shoulder · POV · dutch tilt (unease, dream only) · through a doorway / window / between objects (voyeur, distance).
- **Lens feel:** 24mm wide with deep focus for rooms and the hoard · 50mm natural for two-shots · 85–135mm telephoto compression with creamy bokeh for faces and lonely figures.
- **Composition:** rule of thirds · strong leading lines (paths, shelves, film rows) · frame-within-frame (door, window, mirror) · negative space around a lonely figure · foreground silhouette or out-of-focus object for depth.
- **Light:** golden-hour backlight and lens flare (funeral, café) · window shafts with dust in the air (therapy room, hoard) · cold lightbox glow on a face (reading room) · single practical lamp in darkness (study, phone call) · moonlight blue vs warm interior (night) · silhouette against a bright window (Alvin's back, b15).

## Mood map by act
- **Act 1 (present, sunny):** setting per the book = a memorial in the spacious sunny BACKYARD of Molly's son's house (garden chairs, flower table with her portrait, Stanford colleagues among guests), Yalom leaving through the garden GATE onto the street — never a cemetery, headstones or graves. warm golden-hour, long shadows, lens flare, wide lonely compositions for Yalom; close telephoto faces for the encounter.
- **Act 2 (1982):** cooler, contrasty, institutional greens and slate; lightbox glow; the dream goes near-monochrome with a dutch tilt; the hoard is claustrophobic, deep-focus wide with towering foreground stacks.
- **Act 3 (present + memory):** soft warm afternoon; memory shots (Molly) slightly hazy and glowing; the last shots breathe — wide, quiet, negative space.

## Variety rule (storyboard)
No two adjacent shots with the same size and angle; each line mixes at least two sizes when it has 2+ shots; every act has at least one extreme wide, one extreme close-up/insert, and one frame-within-frame.

## Natural, not "AI-looking" (user feedback 2026-10-11, on R92)
Avoid the AI tells: posed, symmetrical "portrait" staging; everyone facing camera; glossy rim light on every edge; god rays + floating dust motes + bloom haze stacked together; airbrushed, ageless, glamour-smooth faces; hands placed "decoratively" on shoulders/tables; spotless props; a photo-within-photo drawn in the same glossy style.
Prefer: a candid, in-between moment (mid-gesture, looking at each other or at an object, not at the lens); one motivated light source, matte shading, restrained atmosphere; faces with real age, asymmetry and lines; lived-in props (worn edges, clutter, creases); photos-within-photos that look like real snapshots (faded colour, film grain, slight blur, white border).
Validators: dock the cinematic and style axes when an image shows two or more of these tells.

## Expressions (user feedback 2026-10-11, on R91)
The AOT style defaults to scowls (heavy furrowed brows, clenched jaws, hard stares). Always name the emotion in the prompt with concrete facial cues (brows, eyes, mouth, jaw) that fit the beat in the book, e.g. moved = brows lifted at the inner corners, soft eyes, lips parted. Validators fail a face whose emotion doesn't match the beat.
Hard fails (face audit 2026-10-11): the heavy-lidded, one-sided, closed-mouth smirk; glaring at another character when the beat is warm/shocked/ashamed; staring dead into the lens. Per-image briefs: ratings/face-audit.md.
