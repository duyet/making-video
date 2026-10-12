# Thay đổi cue (shots.json)

Áp dụng cho cả hai dự án: `alvin-cross-aot` (1p) và `alvin-cross-aot-3p` (3p). Mỗi cue mới đã được kiểm tra bằng script: nó là chuỗi con chính xác của dòng tương ứng và chỉ xuất hiện đúng một lần, trong cả hai bản. Mọi cue không có trong bảng dưới đây vẫn khớp, nên giữ nguyên (gồm cả cue riêng của 3p ở s03, `"Yalom bối rối"`).

Tổng: **8 cue thay đổi cho mỗi dự án**, giống hệt nhau ở 1p và 3p. Tổng cộng là 16 lần sửa.

| Dòng | Ref | Cue cũ | Cue mới | Lý do |
|---|---|---|---|---|
| s05 | F01 | `thêu tên mình` | `Anh tìm đến` | Đã bỏ mô tả áo blouse khỏi lời kể |
| s05 | F10 | `Ngoài ba mươi` | `rất tự tin` | Quyết định của người dùng: lời kể không nhấn mạnh tuổi nhân vật |
| s06 | F21 | `Mười lăm năm` | `hơn mười lăm năm` | Sách ghi "hơn 15 năm" |
| s14 | F07 | `lồng phổi` | `bệnh bại liệt` | Sách không có chi tiết phổi sắt |
| s18 | F25 | `Một tâm trí` | `phủ kín sàn nhà` | Đã bỏ câu "tâm trí đóng băng", vì không có căn cứ |
| s18 | F26 | `kể từ ngày` | `Alvin ngồi quay lưng` | Như trên |
| s20 | F18 | `lịch sự mà` | `Anh chỉ lắc đầu` | Alvin không mời Yalom về |
| s22 | F02 | `để tôi mở lòng` | `rồi suốt ba mươi năm` | Đã bỏ quan hệ nhân quả "mở lòng" vì không có căn cứ |

Áp dụng: `{"ref": "F01", "cue": "Anh tìm đến"}`, v.v. Giữ nguyên `box`/`ink`/`fallback` hiện có.

## Ảnh nên làm lại hoặc đổi (nội dung ảnh mâu thuẫn với sách)

- **F18** "Man asking doctor to leave": Alvin không đuổi Yalom. Nên làm lại thành Alvin ngồi ghế lớn quay mặt ra cửa sổ, lắc đầu, còn Yalom ngồi phía sau.
- **F07** "Child peering into iron lung": sách không có phổi sắt. Nên đổi thành chân dung cậu bé Ralph với đôi mắt nâu sáng, hoặc một lớp học có ghế trống.
- **F26** "Photograph of parents smiling", cue mới là Alvin ngồi quay lưng: nên thay bằng cảnh Alvin trong ghế lớn giữa đống đồ tích trữ. Ảnh cha mẹ hợp hơn với s14 ("cha mẹ mất trong tai nạn mười năm trước").
- **F23 / F24 / F31 / F33 / F22** (nghĩa trang, bia mộ): tang lễ trong sách diễn ra ở **sân sau nhà con trai Molly**, vào buổi chiều nắng, không phải ở nghĩa trang. F33 (hoa trên bia đá) và F24 nên làm lại thành sân vườn nắng có ghế xếp và di ảnh.
