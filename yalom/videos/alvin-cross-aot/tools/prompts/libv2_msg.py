"""Build one-line Flow agent messages for the molly-v2 library redraws and save per-candidate prompt files.
usage: libv2_msg.py [--noref] <round_json> <round_n> <R##>[:<round of that shot, prompt from library-v2-r<k>.json>] ..."""
import json, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STYLE = ("Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, "
         "flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, "
         "evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, calm natural expressions, "
         "cinematic anime film still, anamorphic widescreen composition, painterly backgrounds with atmospheric perspective, "
         "motivated dramatic lighting, shallow depth of field, film grain, no text, no letters, no captions, no logos, no watermark, "
         "no sparkle icon in any corner.")
noref = '--noref' in sys.argv
args = [a for a in sys.argv[1:] if a != '--noref']
src, n, shots = args[0], args[1], args[2:]
P = json.load(open(src))
for extra in ('library-v2-r1.json', 'library-v2-r2.json', 'library-v2-r3.json', 'library-v2-r4.json', 'library-v2-r5.json'):
    q = os.path.join(os.path.dirname(os.path.abspath(__file__)), extra)
    if os.path.exists(q):
        for k, v in json.load(open(q)).items():
            P.setdefault(k + ':' + extra[-6], v)
rounds = {s.split(':')[0]: (s.split(':')[1] if ':' in s else n) for s in shots}
items = []
for i, s0 in enumerate(shots, 1):
    p = P[s0]
    s = s0.split(':')[0]; n_s = rounds[s]
    items.append(f"{i}) {s}: {p['prompt']}" if noref else f"{i}) {s} (reference image {p['replaces']}-ref.jpg): {p['prompt']}")
    d = os.path.join(ROOT, 'assets/flow2k_raw/molly-v2', s); os.makedirs(d, exist_ok=True)
    for k in (1, 2):
        open(os.path.join(d, f'r{n_s}-{k}.prompt.txt'), 'w').write(
            f"[Flow agent batch message, round {n_s}, item {i}) {s} replaces {p['replaces']}; variation {k}; per-shot prompt:]\n{p['prompt']} {STYLE}\n")
names = ', '.join(f"{s}-r{r}a and {s}-r{r}b" for s, r in rounds.items())
msg = (f"Create {2*len(shots)} new images, 16:9: two separate variations of each of the {len(shots)} shots below, every image its own generation, no collage, no grid, no split screen. "
       + (f"Use the attached character sheet AOT-CAST-SHEET as the reference for every face and outfit; compose each frame exactly as described. " if noref else f"Use the attached character sheet AOT-CAST-SHEET as the reference for every face and outfit, and each shot's attached reference image only for its characters, set and art style: recompose it as a new, more cinematic film frame exactly as described, do not copy its framing. ")
       + f"Name the images {names}, in that order, and add them to the LIBV2 collection. Shared style for all: {STYLE} " + ' '.join(items))
print(msg.replace('\n', ' '))
