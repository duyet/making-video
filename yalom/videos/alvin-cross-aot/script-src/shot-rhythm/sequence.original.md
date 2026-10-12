# Sequence — script "original" (shared by 1p and 3p)

Line → shots. Cue = exact substring of the line text in `narration/scripts/original/lines.json` (first shot of a line has no cue, it starts with the line). Motion is the suggestion for `tools/motion.py` `CAM` (push-in = scale up, pull-out = scale down, pan = xPercent, tilt = yPercent, static = equal scales, no x/y). `ink` = act-boundary dissolve, unchanged from `shots.json`. N05 and N19 are reused from the Molly plan; if they are not generated, use the fallback in brackets.

| Line | # | Shot | Size | Cue | Motion |
|---|---|---|---|---|---|
| s01 | 1 | F24 | toàn | — | slow pan left→right (as now) |
| | 2 | X13 | insert | `quản lý` | static, micro push-in |
| | 3 | F31 | trung-toàn | `Hôm nay` | slow push-in |
| s02 | 1 | F33 | cận | — | slow push-in, tilt up (as now) |
| s03 | 1 | F23 | trung | — | slow pan |
| | 2 | F13 | trung | `Bên cạnh` | slow push-in |
| | 3 | X10 | cận | `ánh mắt đầy cảm kích` | static hold |
| | 4 | F20 | cận | `Tôi bối rối` | very slow push-in |
| s04 | 1 | F15 | insert | — | micro push-in |
| | 2 | X03 | toàn | `để lục lại` | slow push-in toward the cabinet |
| s05 | 1 | X01 | toàn | — | very slow pan right, hold wide |
| | 2 | F11 | trung | `Bác sĩ Alvin Cross` | slow pan (as now) |
| | 3 | F10 | cận | `Ngoài ba mươi` | tilt up (as now) |
| | 4 | F01 | insert | `có thêu tên` | push-in (as now) |
| s06 | 1 | F05 (ink) | toàn | — | slow pull-out (as now) |
| | 2 | F21 | trung | `Mười lăm năm` | slow push-in |
| | 3 | X02 | insert | `nhờ anh xem` | static, micro push-in |
| s07 | 1 | F34 | insert | — | push-in on the tumour (as now) |
| | 2 | X07 | cận | `Không thể cứu vãn` | static hold |
| | 3 | F08 | insert | `Vậy mà` | micro push-in |
| | 4 | F19 | cận | `ánh mắt Jason` | slow push-in, tilt down (as now) |
| s08 | 1 | F06 | trung | — | slow pan (as now) |
| | 2 | X06 | insert | `ôm sạch tiền` | static, micro push-in |
| | 3 | F30 | toàn | `bỏ đi biệt xứ` | slow pan (as now) |
| s10 | 1 | F27 | toàn | — | push-in (as now) |
| | 2 | F28 | đặc tả | `lao thẳng` | fast push-in power2.in (as now) |
| | 3 | F29 | đặc tả | `Con quạ của` | pull-out (as now) |
| s12 | 1 | F32 (ink) | toàn | — | slow pan (as now) |
| | 2 | X04 | cận | `Nhưng sâu bên dưới` | very slow push-in |
| | 3 | F14 | insert | `sự tự cô lập` | slow push-in (as now) |
| s14 | 1 | F04 | trung-toàn | — | pull-out (as now) |
| | 2 | F35 | toàn | `người bạn Ralph` | slow pan (as now) |
| | 3 | F07 | trung | `lồng phổi` | push-in (as now) |
| | 4 | F36 | cận | `chấm hết` | slow push-in (as now) |
| s16 | 1 | X05 | trung | — | slow push-in |
| | 2 | X04 | cận | `Nhưng trực giác` | static hold |
| s17 | 1 | X08 | toàn | — | very slow push-in toward the porch |
| | 2 | F17 | trung | `anh miễn cưỡng` | push-in (as now) |
| s18 | 1 | F12 (ink) | toàn | — | slow pan (as now) |
| | 2 | F25 | insert | `Một tâm trí` | push-in (as now) |
| | 3 | F26 | insert | `kể từ ngày` | slow push-in (as now) |
| s20 | 1 | X09 | cận | — | static hold, then micro push-in |
| | 2 | F18 | trung | `lịch thiệp` | slow push-in (as now), hold through "chấm dứt liệu trình" |
| s21 | 1 | N05 [fallback X03] | insert | — | slow pull-out |
| | 2 | X11 | cận | `cho đến hôm nay` | static hold |
| s22 | 1 | X10 | cận | — | very slow push-in |
| | 2 | F16 | trung | `Bà ấy` | push-in (as now) |
| | 3 | F02 | toàn | `để tôi mở lòng` | slow pan (as now) |
| | 4 | N19 [fallback F09] | trung | `và hai đứa con` | slow push-in on the photo |
| s23 | 1 | F03 | trung | — | slow push-in (as now) |
| | 2 | X13 | insert | `một sự quan tâm cụ thể` | static hold (callback to s01) |
| | 3 | F22 | toàn | `Đủ chân thành` | push-in (as now) |
| | 4 | X12 | toàn (aerial) | `để tiếp tục sống` | slow pull-out, hold to the fade |

## Size rhythm, before → after

Before: toàn tr-toàn · cận · trung trung cận · insert · trung insert cận · toàn trung · insert insert cận · trung toàn · toàn đt đt · toàn insert · tr-toàn toàn trung cận · insert · trung · toàn insert · trung · trung · trung toàn toàn · toàn

After: toàn insert tr-toàn · cận · trung trung cận cận · insert toàn · toàn trung cận insert · toàn trung insert · insert cận insert cận · trung insert toàn · toàn đt đt · toàn cận insert · tr-toàn toàn trung cận · trung cận · toàn trung · toàn insert insert · cận trung · insert cận · cận trung toàn trung · trung insert toàn toàn(aerial)

## What changed and why

- **s01** the bills insert gives Molly a presence in the first ten seconds and sets up the s23 callback.
- **s03** shot/reverse-shot: Alvin's grateful close-up answers Yalom's puzzled one.
- **s04 → s05** study wide, then the Stanford dawn exterior: two establishing shots in a row is deliberate, one closes the present, the other opens 1982.
- **s07** stays tight on purpose (insert cận insert cận); the stopped hand gives "Không thể cứu vãn" a human beat between the film and the cigarette.
- **s12 / s16** Yalom finally has a 1982 face; X05 shows Alvin at ease and ready to leave instead of the parents' portrait, which moves to s18 where the text names the parents.
- **s17** exterior before the door.
- **s20** shame on a face first, then the polite refusal on the two-shot.
- **s21** F16 (Molly clearing) no longer spoils the reveal; the "cho đến hôm nay" return gets its own close-up.
- **s22–s23** the reveal is a close-up, the ending steps cận → trung → toàn → insert → toàn → aerial instead of three wides.

## Cue words (all verified as exact substrings)

s01 `quản lý`, `Hôm nay` · s03 `Bên cạnh`, `ánh mắt đầy cảm kích`, `Tôi bối rối` · s04 `để lục lại` · s05 `Bác sĩ Alvin Cross`, `Ngoài ba mươi`, `có thêu tên` · s06 `Mười lăm năm`, `nhờ anh xem` · s07 `Không thể cứu vãn`, `Vậy mà`, `ánh mắt Jason` · s08 `ôm sạch tiền`, `bỏ đi biệt xứ` · s10 `lao thẳng`, `Con quạ của` · s12 `Nhưng sâu bên dưới`, `sự tự cô lập` · s14 `người bạn Ralph`, `lồng phổi`, `chấm hết` · s16 `Nhưng trực giác` · s17 `anh miễn cưỡng` · s18 `Một tâm trí`, `kể từ ngày` · s20 `lịch thiệp` · s21 `cho đến hôm nay` · s22 `Bà ấy`, `để tôi mở lòng`, `và hai đứa con` · s23 `một sự quan tâm cụ thể`, `Đủ chân thành`, `để tiếp tục sống`.

Note for `tools/build.py`: `slots.json` `cues` must gain entries for the new phrases (it is produced by `narration/fit.py` from the VO alignment); the phrase set above is what to feed it.

## shots.json draft

```json
{
 "s01": [{"ref": "F24"}, {"ref": "X13", "cue": "quản lý"}, {"ref": "F31", "cue": "Hôm nay"}],
 "s02": [{"ref": "F33"}],
 "s03": [{"ref": "F23"}, {"ref": "F13", "cue": "Bên cạnh"}, {"ref": "X10", "cue": "ánh mắt đầy cảm kích"}, {"ref": "F20", "cue": "Tôi bối rối"}],
 "s04": [{"ref": "F15"}, {"ref": "X03", "cue": "để lục lại"}],
 "s05": [{"ref": "X01"}, {"ref": "F11", "cue": "Bác sĩ Alvin Cross"}, {"ref": "F10", "cue": "Ngoài ba mươi"}, {"ref": "F01", "cue": "có thêu tên"}],
 "s06": [{"ref": "F05", "ink": true}, {"ref": "F21", "cue": "Mười lăm năm"}, {"ref": "X02", "cue": "nhờ anh xem"}],
 "s07": [{"ref": "F34"}, {"ref": "X07", "cue": "Không thể cứu vãn"}, {"ref": "F08", "cue": "Vậy mà"}, {"ref": "F19", "cue": "ánh mắt Jason"}],
 "s08": [{"ref": "F06"}, {"ref": "X06", "cue": "ôm sạch tiền"}, {"ref": "F30", "cue": "bỏ đi biệt xứ"}],
 "s10": [{"ref": "F27"}, {"ref": "F28", "cue": "lao thẳng"}, {"ref": "F29", "cue": "Con quạ của"}],
 "s12": [{"ref": "F32", "ink": true}, {"ref": "X04", "cue": "Nhưng sâu bên dưới"}, {"ref": "F14", "cue": "sự tự cô lập"}],
 "s14": [{"ref": "F04"}, {"ref": "F35", "cue": "người bạn Ralph"}, {"ref": "F07", "cue": "lồng phổi"}, {"ref": "F36", "cue": "chấm hết"}],
 "s16": [{"ref": "X05"}, {"ref": "X04", "cue": "Nhưng trực giác"}],
 "s17": [{"ref": "X08"}, {"ref": "F17", "cue": "anh miễn cưỡng"}],
 "s18": [{"ref": "F12", "ink": true}, {"ref": "F25", "cue": "Một tâm trí"}, {"ref": "F26", "cue": "kể từ ngày"}],
 "s20": [{"ref": "X09"}, {"ref": "F18", "cue": "lịch thiệp", "box": [0.05, 0.05, 0.95, 0.86]}],
 "s21": [{"ref": "N05"}, {"ref": "X11", "cue": "cho đến hôm nay"}],
 "s22": [{"ref": "X10"}, {"ref": "F16", "cue": "Bà ấy"}, {"ref": "F02", "cue": "để tôi mở lòng"}, {"ref": "N19", "cue": "và hai đứa con"}],
 "s23": [{"ref": "F03"}, {"ref": "X13", "cue": "một sự quan tâm cụ thể"}, {"ref": "F22", "cue": "Đủ chân thành"}, {"ref": "X12", "cue": "để tiếp tục sống"}]
}
```

Suggested `CAM` entries for the X shots (scale0, scale1, x0, x1, y0, y1, ease), all within the edge rule `|x|,|y| <= (scale-1)*50`:

```python
'X01': (1.12, 1.12, -5, 5, 0, 0, N),   'X02': (1.06, 1.12, 0, 0, 0, 0, P),
'X03': (1.08, 1.20, 0, -4, 0, 0, P),   'X04': (1.06, 1.16, 0, 0, 0, 0, P),
'X05': (1.06, 1.16, 0, 0, 0, 0, P),    'X06': (1.06, 1.12, 0, 0, 0, 0, P),
'X07': (1.10, 1.10, 0, 0, 0, 0, N),    'X08': (1.06, 1.18, 0, 0, 0, 2, P),
'X09': (1.10, 1.14, 0, 0, 0, 0, P),    'X10': (1.06, 1.14, 0, 0, 0, 0, P),
'X11': (1.10, 1.10, 0, 0, 0, 0, N),    'X12': (1.30, 1.06, 0, 0, 0, 0, P),
'X13': (1.08, 1.08, 0, 0, 0, 0, N),
```
