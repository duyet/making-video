# molly-v2 library: fixes for failing refs

Source: `ratings/library.json` (52 refs incl. fallbacks; M01–M08 skipped). 38 pass, 14 fail (2 hard fails: F32, F12).

## Swaps (existing images, no generation needed)

| Line / slot | Now | Swap to | Why |
|---|---|---|---|
| a01 cue "tang lễ" | F31 | **B02** | Molly's portrait on a sunlit flower table; keeps the sunny funeral from N21 (N21 already has a portrait easel) and names whose funeral it is. F31 is heavy grey fog. |
| a01 fallback | F24 | **B01** | Sunny outdoor funeral with crowd (backyard, but only used if N21 is missing). |
| a02 cue "khiến ông phát điên" | X11 | **B03** (or keep X11 and drop fog) | Sunny, rueful Yalom at the funeral. Caveat: cardigan without overcoat. |
| b02 start | X02 | **B14** | Yalom lecturing to doctors, Alvin in the audience: literally "một bài nói chuyện của Yalom". (Yalom wears a white coat there, off-anchor but reads fine.) |
| b02 cue "bắt đầu" | F11 | **X02** | Hand at the lightbox fits "began thinking about…". |
| b02 cue "phía sau" | F32 | **B15** | Alvin facing a chest film with a ghostly human face in it: "the people behind the X-rays". |
| b04 fallback for M01 | F06 | **B16** | The tense family dinner, exactly the sheet beat. |
| b04 cue "mâu thuẫn" | F30 | **B17** (optional) | Alvin and Jason face to face in conflict; F30 is back views of Jason and an unanchored woman at night. Keep F30 if M01 already covers the conflict and you want the "Jason leaves" beat. |
| b05 fallback for M02 | F34 | **B18** | Alvin taking the phone call, shocked: the sheet beat. F34 stays at b07. |
| b09 start | F32 | **F14** | Alvin's clasped hands in the leather chair: therapy without the diploma. |
| b13 cue "ngay tại nhà" | X08 | **F17** | Alvin opening his front door to Yalom: the "his front door" hard cut, with faces. Daytime matches F12/N14 interiors. |
| c02 start | N15 | **B23** | Avoids N15 reused back to back from c01 (Ken Burns restart pop); Yalom in the hoard with a guilty look = "tự trách mình". |
| c05 fallback for M06 | F12 | **B22** | Molly walking into the hoard with workmen while Alvin waits: the exact sheet beat (F12 also hard-fails). |

After the swaps, F32 is still needed only at b12 start: use R01. X02 passes in its new cue role (beat 8 -> 8.7).

## Grade/fx changes (no new image)

- a01–a05: drop the `fog` fx on F22, F23, X10, X11, F31 (F24) and warm the grade. VO says "buổi chiều đầy nắng"; N21 is sunny, the rest are misty. With fog off, F22 (8.45) and X10/F20 read as hazy afternoon sun.
- b07 F11: lift exposure ~+0.4 EV or soften the `flicker` (0.3–0.45 is very dark). R04 below if you'd rather redraw.
- b08 F27: dim is intended (sheet: "lights dim"); keep, marginal 8.45. No redraw recommended.

## New redraws

All prompts: one line, anchors verbatim, even readable lighting, no text.

### R01 · Therapy two-shot, no diplomas (replaces F32 at b12, "Khi Yalom hỏi sâu hơn") · HARD FAIL fix

```
Medium-wide two-shot in a quiet 1982 Stanford office used as a therapy room, warm afternoon light through half-open blinds, bookshelves, a small lamp and a tissue box on a side table; plain bare walls with no framed certificates, no diplomas, no posters. Left, in a brown leather armchair, leaning slightly forward with gentle attention, hands loosely clasped: Dr. Yalom: man about 50, inspired by Zeke Yeager, short tousled dark-blond hair, full trimmed blond beard, round wire-rim glasses, calm intellectual face, kind tired eyes, medium build; brown knit cardigan over a shirt, dark trousers. Right, in a matching armchair, sitting stiffly, eyes lowered, hands resting on his knees: Alvin Cross: man mid-30s, inspired by Erwin Smith, tall, blond hair in a neat side part with silver-grey temples, strong angular jaw, heavy brows, blue eyes, commanding calm; white doctor coat with "Alvin Cross" embroidered in dark blue on the left chest, pale blue shirt, dark tie. Faces fully readable. Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, 1980s California, calm natural expressions, no captions, no watermark, no text except the embroidered name on the coat.
```

### R02 · Yalom stunned in the hoard, blank papers (replaces F12 at b14) · HARD FAIL fix

```
Medium-wide shot inside a 1980s California bungalow living room crammed with knee-high to shoulder-high stacks of plain folded newspapers, file boxes and books, only narrow walkways left between the piles, a buried sofa and lamp, daylight through dusty blinds keeping the room evenly lit. Right third, just inside the doorway, standing still in shock: Dr. Yalom: man about 50, inspired by Zeke Yeager, short tousled dark-blond hair, full trimmed blond beard, round wire-rim glasses, calm intellectual face, kind tired eyes, medium build; grey wool overcoat over a brown knit cardigan, dark trousers. Every newspaper, page and box completely blank: no headlines, no mastheads, no printed letters anywhere. Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, calm natural expressions, no text, no captions, no watermark.
```

### R03 · The narrow path (replaces F25 at b14 cue "chỉ còn")

```
Low-angle shot at knee height down a narrow walkway between tall leaning stacks of plain blank newspapers and cardboard boxes in a 1980s California bungalow, the path barely one person wide, dust motes in a shaft of daylight from a window at the end, an empty armchair visible at the far end, evenly lit. All paper completely blank: no headlines, no mastheads, no letters. Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, calm natural expressions, no text, no captions, no watermark.
```

### R04 · The handshake: Monica smiling, Yalom puzzled (replaces F23 at a04 cue "Người vợ")

F23 has Monica sad (hand on chest), Yalom not puzzled and the Panama hat gone. No existing image has this beat (B07 is the same composition).

```
Medium shot on a sunlit cemetery path, weeping willows behind, clear warm afternoon light, no fog. Left: Monica: woman early 30s, inspired by Historia Reiss, small and slender, long pale blonde hair, large blue eyes, gentle quiet face, soft smile; black funeral dress under a black wool coat, black leather gloves; smiling warmly and speaking, one gloved hand open toward Yalom. Centre: Alvin Cross: man about 40, inspired by Erwin Smith, tall, blond hair in a neat side part with silver-grey temples, strong angular jaw, heavy brows, blue eyes, quiet warmth; charcoal suit, white shirt, black tie, dark overcoat, a cream Panama hat with a black band; the Panama hat held against his chest in his left hand, his right hand shaking Yalom's hand, a polite grateful smile. Right: Dr. Yalom: man about 50, inspired by Zeke Yeager, short tousled dark-blond hair, full trimmed blond beard, round wire-rim glasses, calm intellectual face, kind tired eyes, medium build; grey wool overcoat over a brown knit cardigan, dark trousers; shaking Alvin's hand, polite but visibly puzzled, brows slightly raised, trying to place the face. Hands clean and simple, all headstones blank. Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, 1980s California, calm natural expressions, no text, no captions, no watermark.
```

### R05 (optional) · F11 brighter (b07 start), only if the grade lift isn't enough

```
Medium shot in a 1982 Stanford radiology reading room, Alvin Cross: man mid-30s, inspired by Erwin Smith, tall, blond hair in a neat side part with silver-grey temples, strong angular jaw, heavy brows, blue eyes, commanding calm; white doctor coat with "Alvin Cross" embroidered in dark blue on the left chest, pale blue shirt, dark tie; standing in profile before a wall-mounted X-ray lightbox showing a chest film, studying it with a fixed haunted stare, the lightbox glow plus a warm overhead fluorescent light keeping the whole room and his face clearly lit, film jackets and a beige rotary phone on a desk behind, both hands relaxed at his sides out of frame. Anime illustration in the style of Attack on Titan (Wit Studio era): bold clean line art, heavy black ink shadows, flat cel shading, muted earthy palette of olive, slate grey, brick and dusty gold, dramatic but restrained lighting, evenly lit and easy to read, never murky or underexposed, cinematic 16:9 widescreen framing, 1980s California, calm natural expressions, no captions, no watermark, no text except the embroidered name on the coat.
```

## Continuity flags

1. **Weather, a01–a05.** The VO says sunny; N21 is sunny, then F31/X11/F22/X10/F23/F15/F20 are misty grey, and the `fog` fx is on 6 of them. Fix: swaps above, plus fog off.
2. **Panama hat.** On in N03, held in X10, gone in F23 (hands empty). Fixed by R04.
3. **Location.** The B-series funeral is a backyard memorial, not a cemetery. Use only close shots that hide the location (B02, B03). Don't cut B01/B04/B05/B07 against N21, N03 or X12.
4. **Costume.** Yalom wears an overcoat at the funeral (N21, F20, F23) but only a cardigan in B03/B08. This only matters if B03 goes in.
5. **Repetition.** X04 appears 3 times in b09–b13. Fix: F14 at b09 start, X04 at its cue. Keep X04 at b11. At b13, X04 → F17 cue is fine, or start b13 on R01 if you want fewer repeats. F32 ×3 is resolved by the swaps and R01. N15 back to back across c01→c02 is resolved by B23. N18 at c04 and c06 has c05 between them, which is fine.
6. **Age, present day.** Yalom in the café (N16/N18) and at the funeral looks the same ~50 as in 1982, and present-day Alvin (X10, N16/N17, N19) looks ~40, not ~65. This follows the anchor sheet's convention, so it isn't penalised, but the sheet's "older Yalom" for c03 is not shown.
7. **Day/night, b13.** The sheet wants "front door at night", but the interiors F12/N14/F18/X09 are daytime, so keep the visit in daylight (F17/X08).
8. **Era.** The 1967 family conflict (B16/B17/F30) shows Alvin at about 20, which works. Everything else is in era.
