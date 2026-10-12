# "Thank You, Molly" — shot map

Source: `script-src/thank-you-molly.csv` → `lines.molly.json` (40 lines, 850 words ≈ 5:27 VO at 2.6 w/s; the sheet's own timecodes assume 5:00, so expect ~30 s of overrun before pauses).

Legend: `F##` = existing `assets/redraw/F##.png`, `N##` = new shot (prompt in `new-shots.md`), `(opt)` = optional new shot with a reuse fallback. Motion = Ken Burns suggestion for `tools/motion.py`. When a line lists two shots, the second is a cue cut inside the line, same as the SHOTS tuples in `tools/build.py`.

## Act 1 — Cuộc hội ngộ bất ngờ

| Line | Shot(s) | Motion | Reason |
|---|---|---|---|
| m01 | F24 → F31 (cue "Yalom") | F24 slow push-in; F31 slow drift left | Funeral establishing + Yalom at the grave. Sheet says afternoon sun and a crowd; existing is fog and a few distant mourners. Reuse by default; N21 (opt) is the sunny version if the user wants the sheet honoured. |
| m02 | F33 | push-in on the headstone | Sheet asks for a push-in to Molly's photo among flowers. F33 already carries "MOLLY" and white flowers, so it reads as the same beat without a new image. Dissolve to N01 at the end. |
| m03 | N01 → N02 (cue "sửa chữa") | N01 pan right across the bills; N02 slow push-in | Molly running Yalom's household: no existing shot of Molly outside Alvin's house. N01 = bills and ledger at Yalom's kitchen table; N02 = tree-trimming crew. |
| m04 | N02 → F31 (cue "không thể thiếu bà") | N02 drift toward Yalom; F31 static | Yalom watching Molly direct the tree crew, helpless. The sheet's "cabinet door closes → funeral gate opens" match cut becomes a hard cut back to F31. |
| m05 | N03 | slow track right | The Panama hat is new, so the gate approach needs a new shot. Fog kept to match F24/F31. |
| m06 | F23 → F13 (cue "Vợ anh nói") | F23 slow push-in; F13 slow drift | Handshake + introduction. F23 has Monica mid-thank-you, Alvin nodding, Yalom puzzled; close enough. Note: no hat in F23/F13 (see conflicts). |
| m07 | F20 | very slow push-in | Yalom cannot remember. Exact match. |
| m08 | N04 | slow tilt down | Top shot of the file drawer. No existing archive shot. |
| m09 | N05 | push-in on the page | Open folder insert. Sheet's "page becomes the therapy door" match cut becomes a dissolve into F32. The same N05 image is reused for m32 and m33. |

## Act 2 — Ca trị liệu dang dở

| Line | Shot(s) | Motion | Reason |
|---|---|---|---|
| m10 | F01 → F10 (cue "Stanford") | F01 slow drift; F10 tilt up | Radiologist at Stanford: the embroidered coat establishes it. N20 (opt) is a Stanford exterior if the user wants the sheet's establishing shot. |
| m11 | F11 → F34 (cue "Không chỉ là hình ảnh") → F32 (cue "cuộc đời") | F11 push-in; F34 slow push-in; F32 slow drift | Alvin at the lightbox, the film, the therapy room. |
| m12 | N06 | slow push-in | Alvin lowers his eyes when Jason is named. Needs a therapy-room close-up of Alvin, which does not exist (F10 is the reading room). N06 is reused for m20 and m25. |
| m13 | F06 → F30 (cue "xung đột") | F06 slow push-in; F30 slow push-in | Family conflict, Jason leaves. The sheet says a tense dinner; F06 is a hallway argument, same beat. |
| m14 | F34 → N07 (cue "Alvin lập tức") | F34 push-in; N07 slow track forward | "Muốn Alvin xem phim chụp" gets the tumour film, then the drive to North Carolina. N07 can be dropped (hold F34) if the user wants fewer new shots. |
| m15 | N08 → N09 (cue "Jason qua đời") | N08 very slow push-in; N09 static | Brothers apart in the NC house, stone fireplace between them, then the empty chair. F05 puts Jason in the Stanford reading room, which contradicts this script. |
| m16 | F11 (+ F19 ghost dissolve at 30% opacity) | F11 static; F19 fades in and out | Alvin frozen at the lightbox, Jason flickering as memory. Done in HTML, no new image. |
| m17 | F32 → F14 (cue "những điều chưa kịp nói") | F32 slow pull-out; F14 slow push-in | Alvin head down, Yalom listening, slow pull-out exactly as the sheet asks. |
| m18 | F27 → F28 (cue "giữa bóng tối") | F27 slow push-in; F28 slow push-in | Nightmare raven in the bathroom mirror. The sheet's "bird crosses the mirror → light dims" is F27 with an opacity fade. |
| m19 | F26 → F35 (cue "mất mát") → N09 (cue "sâu xa hơn") | F26 push-in; F35 slow track; N09 static | Flash memory: parents' portrait, hospital corridor, empty chair. |
| m20 | N06 | static then slow push-in | Alvin opens his eyes in the therapy room, tense. |
| m21 | N10 → N11 (cue "cuối tuần") → N13 (cue "không có ai") | N10 slow push-in; N11 slow drift right; N13 push-in on the doorway | Cafeteria, kayak, coming home at dusk. All new locations. N13 doubles as the porch for m26/m27; here use a tight crop of the doorway with Alvin. |
| m22 | N12 → F32 (cue "không muốn tìm hiểu") | N12 static hold on the empty chair; F32 push-in on Alvin's chair | Dinner alone, empty chair opposite, match cut to the therapy chair. |
| m23 | F11 → F32 (cue "Anh nghĩ") | F11 slow drift; F32 slow push-in | "Brightening" montage: working calmly, then at ease in therapy. Grade both warmer in HTML. The "sleeping peacefully" beat is skipped; no existing shot, not worth a new one. |
| m24 | F32 (push-in on Alvin) | push-in to Alvin's side of the frame | Yalom leans in, Alvin defensive. F32 has Alvin upright with clasped hands; the push-in sells the guard going up. |
| m25 | N06 | slow drift left | Alvin silent, eyes away from Yalom. |
| m26 | N13 | slow track with the woman walking away | A woman leaves Alvin's porch at dusk; no interior shown, as the sheet demands. |
| m27 | F32 → N13 (cue "tại nhà Alvin") | F32 push-in; N13 tight crop on the dark door, static | Yalom proposes, Alvin freezes; hard cut to the front door at night (N13 cropped to the doorway, graded darker). |
| m28 | F12 → F25 (cue "Chỉ còn vài lối đi") | F12 slow track forward; F25 push-in | POV reveal of the hoard. |
| m29 | N14 | static, 2 s hold before VO | Alvin seated with his back to the camera at the window, Yalom far. New: F18 has Alvin facing the room. |
| m30 | N14 → F18 (cue "Nhưng anh không muốn") | N14 slow push-in; F18 static | Yalom moves closer, Alvin shakes his head; F18 already shows the refusal. Cut to black on the last word. |
| m31 | N15 | slow push-in | Phone rings in Yalom's 1982 office, his face falls. |
| m32 | N15 → N05 (cue "trong nhiều năm sau đó") | N15 slow drift; N05 slow pull-out, warm grade → cool grade crossfade | Yalom alone with the file. The young/old match cut is done with the same N05 insert and a colour-grade crossfade (see conflicts: no "old Yalom" design exists). |

## Act 3 — Thank you, Molly

| Line | Shot(s) | Motion | Reason |
|---|---|---|---|
| m33 | N05 → N16 (cue "tôi rất muốn biết") | N05 static; N16 slow push-in | File closes, Yalom in the café. The "Yalom enters the café" tracking shot is folded into the café two-shot. |
| m34 | N16 | push-in toward Alvin | Café two-shot, camera moves to Alvin as the question lands. |
| m35 | N17 → N18 (cue "chính tôi đã giới thiệu") | N17 slow push-in; N18 static | Alvin explains, Yalom surprised. |
| m36 | F12 → F16 (cue "sắp xếp") → F02 (cue "hơn ba mươi năm") | F12 slow drift; F16 push-in; F02 slow pull-out | Molly clears the house over time. Exact reuse of the existing B7 trio. |
| m37 | N19 → N18 (cue "khi chúng tôi chia tay") | N19 slow push-in on the frame; N18 slow push-in | Alvin and Monica with the family photo, dissolve to Yalom in the café. |
| m38 | N18 | very slow push-in | Yalom looks out of the café window, afternoon sun. |
| m39 | N01 | slow push-in on Molly | Molly at work in memory. Reuse of the Act 1 bills shot; F16 is the fallback if the user prefers her in Alvin's house. |
| m40 | black + HTML title "THANK YOU, MOLLY" | title fade-in, 2 s hold, fade to black | End title is HTML text, not an image. Piano outro. |

## Counts

- 40 lines.
- Existing shots reused: 24 of 36 (F01 F02 F06 F10 F11 F12 F13 F14 F16 F18 F19 F20 F23 F24 F25 F26 F27 F28 F30 F31 F32 F33 F34 F35). Not used: F03 F04 F05 F07 F08 F09 F15 F17 F21 F22 F29 F36.
- New shots: 19 core (N01–N19) + 2 optional (N20 Stanford exterior, N21 sunny funeral). N07 and N09 are the first to drop if the count must shrink.

## Conflicts and decisions for the user

1. **Thirty years.** The script says Yalom meets Alvin again "sau hơn ba mươi năm" (1982 → ~2013+) and asks for a "Yalom trẻ → Yalom lớn tuổi" match cut. The existing cast is Yalom ~50 and Alvin ~40 at the funeral, i.e. roughly a decade after 1982, and every funeral shot (F23, F13, F20, F31, F24) is drawn that way. Options: (a) keep the existing ages and let the number stay in the VO only (this plan; the m32 match cut is done with a grade shift on the same folder insert), or (b) introduce an "old Yalom, ~80, white hair and beard" and "Alvin ~65" and regenerate all present-day shots (funeral, café, family). (b) roughly doubles the new-shot count. Recommend (a), or soften the VO to "sau nhiều năm".
2. **Funeral weather.** Existing: foggy early-morning cemetery. Sheet: outdoor funeral, afternoon sun through trees, a crowd. Plan reuses the fog (F24/F31/F33 and all three Alvin/Monica shots live there). N21 is an optional sunny wide if the user wants it, but then F23/F13/F20 would clash with it.
3. **Panama hat.** The script names it; F23/F13/F03 have Alvin bareheaded. N03 gives him the hat at the gate; in m06 the hat is simply off (he can have taken it off to greet). If that bothers the user, F23 needs a regen with the hat.
4. **Where Jason was seen.** Existing story: Jason comes to Stanford, F05/F21/F19/F08 are in the hospital. New script: Jason phones, Alvin travels to North Carolina, the brothers sit by a stone fireplace. The plan follows the new script (N07/N08/N09) and does not use F05/F21/F08. F19 is used only as a memory ghost in m16.
5. **Cause of the family rift.** Existing VO: Alvin blocked Jason's teenage marriage, Jason left with the family money (F06/F30). New VO says only "một cuộc xung đột gia đình". F06/F30 are reused and stay compatible.
6. **Molly's photo (m02).** The sheet wants a framed photo among flowers. Plan uses the F33 headstone to avoid a new shot. If the user wants the photo, add a shot to batch BM1.
7. **Hoard contents.** New VO adds "phim X-quang" to the stacks; F12/F25 show newspapers and journals only. Minor; no regen proposed.
8. **"Mười hai giờ trị liệu" / "Năm 1982" (m08).** No text rule: the folder tab in N04/N05 is blank or blurred, the years are carried by the VO only.
9. **Running time.** 850 words ≈ 5:27 at 2.6 w/s, plus 2 s holds at m29 and the title, so plan for ~5:45–6:00 rather than the sheet's 5:00.
10. **Sleeping-peacefully beat (m23)** and the **"empty therapy chair" cut (m22)** are covered by grading and push-ins, not new images.
