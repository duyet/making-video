# Revised VO scripts: changes

Files in this folder:
- `original-1p.lines.json`: A, the original story, 1st person (Yalom narrates)
- `original-3p.lines.json`: B, the same content in 3rd person
- `molly.lines.json`: C, "Thank You, Molly", `{id,text}` only, same schema as A
- `molly.visual.json`: C's `act / beat / timecode / visual`, keyed by line id

Sources used: `alvin-cross-aot/narration/scripts/original/lines.json`, `alvin-cross-aot-3p/narration/scripts/original/lines.json`, `script-src/molly-plan/lines.molly.json`. Cue tables: `narration/scripts/original/shots.json` in both projects. These replaced the `SHOTS` dict that used to live in `tools/build.py`, and the cues are identical.

## Word counts and duration

There are two rate estimates:
- **Brief rate**: 3.4 words/s at 1.3x.
- **Measured rate**: 594 words took 208.4 s of VO at 1.0x (`durations.json`). That is 2.85 w/s, so about 3.7 w/s at 1.3x.

Durations below are VO only. Inter-line gaps, lead and tail add roughly 4–8 s.

| Script | Lines | Words before | Words after | @1.3x, brief rate | @1.3x, measured rate |
|---|---|---|---|---|---|
| A, original 1p | 18 | 594 | 669 (+13%) | 3:17 | 3:01 |
| B, original 3p | 18 | 598 | 675 (+13%) | 3:19 | 3:02 |
| C, molly | 40 | 850 | 938 (+10%) | 4:36 | 4:14 |

For reference, the old A at 1.3x is 2:55 at the brief rate, or 2:40 measured.

A note on the target: at the brief rate, a 2:45–3:00 window is 561–612 words, which is about what A already had. So I sized A and B against the measured rate and landed at the 3:00 ceiling. If the goal is to fill the whole 25% freed by 1.3x, so the runtime stays the same as the 1.0x cut (about 3:30), A and B have room for about 770 words. In that case, the cut content listed at the end can go back in.

C meets 4:15–4:45 at the brief rate. At the measured rate it lands at 4:14 before gaps. With 40 lines × 0.12 s plus lead and tail, that is about 4:20 on the timeline.

## A / B: per-line changes

B is A with `tôi` → `ông` / `Yalom`, and `chúng tôi` → `hai người`. The only exception is Alvin's direct speech in s22, which keeps `tôi` on purpose. Word counts are for A, before → after.

| id | words | change |
|---|---|---|
| s01 | 41→48 | Removed "giữa một buổi chiều California mờ sương". Added that Yalom fired Molly several times yet could not do without her. The last sentence is now "Hôm nay, tôi đến dự tang lễ của bà." B adds "nhà trị liệu tâm lý" before Irvin Yalom. |
| s02 | 15→15 | Removed the ellipsis. "đã đợi" → "đang chờ". |
| s03 | 48→47 | "cứu rỗi" (religious register) → "thay đổi cuộc đời". "người đàn ông" → "người chồng", "cảm kích" → "biết ơn". Removed the ellipsis and split it into two short sentences. |
| s04 | 15→14 | "đành hẹn họ một dịp khác, để lục lại" → "hẹn gặp lại họ, rồi về lục tìm". |
| s05 | 39→37 | Added "mười hai giờ trị liệu". Tightened the description of the embroidered coat. |
| s06 | 35→36 | "bặt vô âm tín" → "hai anh em không nói với nhau một lời", which is plainer and makes the estrangement mutual. |
| s07 | 34→36 | "phổi" → "lá phổi của chính em trai mình". Merged the fragment "Không thể cứu vãn." into the sentence before it. |
| s08 | 52→53 | Made the marriage clause clear: it was Jason who wanted to marry in a hurry. Replaced the clumsy idiom "Nói ra thì dở, mà không nói cũng chẳng xong" with the line about things never said. |
| s10 | 41→42 | "con quạ của Edgar Allan Poe" → "như bước ra từ thơ Edgar Allan Poe". "một cái chết dang dở" → "những điều dang dở". |
| s12 | 37→50 | **New:** every film now reminds Alvin of Jason. **New:** his loneliness, eating alone, living alone, no relationship that lasts. Replaced the jargon "cơ chế phòng vệ / khỏa lấp nỗi sợ hư vô" with "tự cô lập". |
| s14 | 38→49 | **New:** what Alvin fears most is his own death, which is the existential core of the case. |
| s16 | 24→28 | **New:** "Ác mộng thưa dần", which motivates his wish to stop therapy. |
| s17 | 28→32 | Made the confession specific: every woman left after her first visit to his home. |
| s18 | 28→36 | Added the narrow paths through the newspaper stacks. Clarified that it was his parents' deaths ("cha mẹ anh"). |
| s20 | 23→25 | **New:** the next morning he phoned to end therapy. "Ngay sau đó, anh chấm dứt liệu trình" was vague. |
| s21 | 16→26 | **New:** Yalom's own sense that he had pushed too fast. Removed the ellipsis. Fixed the timeline: the reveal happens at the later meeting, not at the grave. |
| s22 | 37→50 | **New:** "Bác sĩ quên rồi sao?" **New:** Molly stayed on and managed his affairs for many years, not only one clean-out. |
| s23 | 43→45 | "mô hình trị liệu" → "lý thuyết trị liệu", and "Đủ chân thành..." is tightened. **New:** the closing line "Cảm ơn bà, Molly." |

Numbers follow the existing convention: years stay as digits (1980, 1982), and every other number is in words (mười hai, mười lăm, ba mươi, mười năm).

## A / B: shots.json cue edits

**None needed: 0 changes.** I checked every cue string by substring against the new text, and all 26 (A) + 26 (B) are present:
- `Hôm nay`, `Bên cạnh`, `Tôi bối rối` / `Yalom bối rối`
- `Ngoài ba mươi`, `mặc áo`, `Jason tìm đến`, `Vậy mà`, `ánh mắt Jason`, `Jason ôm`
- `lao thẳng`, `Con quạ của`, `Nhưng sâu`, `người bạn Ralph`, `lồng phổi`, `chấm hết`
- `Một tâm trí`, `Bà ấy`, `để tôi mở lòng`

No line ids were added or renamed. Shot proportions change where text was added before a cue. For example, F24 holds longer in s01, F14 carries the loneliness sentence in s12, and F36 carries the fear-of-death sentence in s14.

## C (molly): per-line changes

All 40 ids are kept, and none were merged or split. "hơn ba mươi năm" (m33, m36) → "nhiều năm". "nhiều thập kỷ" (m01) → "nhiều năm", for consistency. Ellipses are removed from m07 and m34.

| id | change |
|---|---|
| m01 | "làm việc cùng tôi suốt nhiều thập kỷ" → "làm việc cho gia đình tôi suốt nhiều năm" |
| m03 | Smoother list: "từ hóa đơn, giấy tờ đến những lần sửa chữa" |
| m04 | "đuổi việc" → "cho bà nghỉ việc" (softer, closer to the tone) |
| m05 | "rời tang lễ" → "ra về", to avoid repeating "tang lễ" |
| m07 | Removed the ellipsis. "Tôi mỉm cười cảm ơn, nhưng thật lòng..." |
| m08 | Fragments merged: "Alvin Cross, năm 1982, mười hai giờ trị liệu." |
| m09 | Reworded more naturally, and gave the sheet's page-turn something to land on |
| m10 | **+** age and manner ("ngoài ba mươi tuổi, giỏi giang và tự tin"), consistent with A |
| m11 | Clarified that Alvin had heard Yalom speak. "con người" → "con người thật" |
| m12 | "Sự thay đổi ấy còn đến từ" (illogical) → "điều đưa anh đến phòng trị liệu của tôi là" |
| m13 | **+** Jason took the family money and left, from A. This matches F30, which is already cued here. |
| m14 | Split into clear subjects. "Anh mắc ung thư" was ambiguous between the brothers, so it is now "Cậu mắc" |
| m16 | "Mỗi tấm phim" → "Tấm phim nào trên bảng đèn" |
| m17 | "đã mãi biến mất" → "đã vĩnh viễn khép lại" |
| m18 | "thường xuyên" → "Đêm nào...", and "đuổi theo" → "lao theo" |
| m19 | **+** the early deaths, the dog the doctor father could not save and Ralph in the iron lung, from A. They sit on F35, the hospital corridor. |
| m20–m25 | Tightened: "Lạ thay", "Phải chăng ... chưa thực sự được sống?" as a real question |
| m26 | "Mọi phụ nữ" → "Người phụ nữ nào ... cũng" (natural Vietnamese) |
| m27 | **+** Alvin agreed only after repeated persuasion, from A |
| m28 | **+** "đóng băng từ ngày cha mẹ anh qua đời, mười năm trước", from A |
| m31 | Removed a filler "để" |
| m32 | "trong nhiều năm sau đó" → "suốt bao năm sau đó", so it does not echo m33's new "sau nhiều năm" |
| m33 | "sau hơn ba mươi năm" → "sau nhiều năm". "thay đổi" → "đổi thay" |
| m34 | Removed the ellipsis and made it a statement |
| m35 | "điều tôi đã hoàn toàn quên mất" → "chuyện tôi đã hoàn toàn quên" |
| m36 | "thu xếp" → "sắp xếp", which now matches the shotmap cue. **+** "dọn đi từng chồng báo cũ". "suốt hơn ba mươi năm" → "suốt nhiều năm" |
| m37 | **+** "Căn nhà dần có chỗ cho người khác bước vào.", the bridge from the cleared house to Monica |
| m39 | "sự quan tâm chân thành" → "một sự quan tâm chân thành, cụ thể, đời thường", which echoes A's ending |

Unchanged apart from punctuation: m02, m06, m15, m29, m30, m38, m40.

## C (molly): shotmap cue edits (`script-src/molly-plan/shotmap.md`)

I checked every cue in the shotmap against the new text. Three need editing:

| line | shot | old cue | new cue | why |
|---|---|---|---|---|
| m01 | F24 → F31 | `"Yalom"` | `"người đã làm việc"` | Already broken before this revision. The 1st-person text never contains "Yalom". |
| m32 | N15 → N05 | `"trong nhiều năm sau đó"` | `"suốt bao năm sau đó"` | Reworded to avoid repeating m33's "sau nhiều năm". |
| m36 | F16 → F02 | `"hơn ba mươi năm"` | `"suốt nhiều năm"` | Required by the "nhiều năm" change. |

Also fixed by a text edit, with no cue change: m36 `"sắp xếp"` used to fail because the source said "thu xếp", and the text now says "sắp xếp".

All other cues match the new text, and each first occurrence comes in the right order:
- `sửa chữa`, `không thể thiếu bà`, `Vợ anh nói`, `Stanford`
- `Không chỉ là hình ảnh` / `cuộc đời`, `xung đột`, `Alvin lập tức`, `Jason qua đời`
- `những điều chưa kịp nói`, `giữa bóng tối`, `mất mát` / `sâu xa hơn`
- `cuối tuần` / `không có ai`, `không muốn tìm hiểu`, `Anh nghĩ`
- `tại nhà Alvin`, `Chỉ còn vài lối đi`, `Nhưng anh không muốn`
- `tôi rất muốn biết`, `chính tôi đã giới thiệu`, `khi chúng tôi chia tay`

No new line ids.

## Content cut from A/B to stay under 3:00

These can be restored if the target moves toward about 3:30:
- s07: "Alvin cố hàn gắn, nhưng khoảng cách giữa hai người đã quá xa."
- s03: Alvin introducing himself as "bệnh nhân cũ của tôi"
- s12: Alvin's guilt at not reconciling in time
- s17: Yalom proposing the session at Alvin's home
- s20: Yalom trying to stay with Alvin in his shame
