# Kiểm tra kịch bản 1p với sách

- Kịch bản được kiểm tra: `alvin-cross-aot/narration/scripts/original/lines.json`, bản trước khi sửa.
- Bản đã sửa: `original-1p.lines.json` và `original-3p.lines.json`.
- Kết luận: OK = đúng sách; WRONG = sai sách; UNSUPPORTED = sách không nói, hoặc là lời diễn giải không có căn cứ; MISSING-IMPORTANT = thiếu một dữ kiện quan trọng; STYLE = mô tả ngoại hình, đã chuyển sang `image-details.md`.

| Dòng | Câu trong kịch bản | Sách nói (trang) | Kết luận | Sửa |
|---|---|---|---|---|
| s01 | "Năm 1980, tôi thuê bà Molly" | Thuê năm 1980 (69) | OK | giữ |
| s01 | "người phụ nữ chất phác, kiên nhẫn" | Molly là người không gì ngăn được, tự quyết mọi việc (69) | UNSUPPORTED | bỏ |
| s01 | "giúp vợ chồng tôi quản lý những hóa đơn ngập đầu" | Gom thư và trả hóa đơn khi Yalom vắng nhà cả một năm; sau đó bà thâu tóm tài chính và nhà cửa (69) | WRONG | "trả hóa đơn khi tôi vắng nhà. Rồi bà dần quản lý mọi việc nhà tôi" |
| s01 | "Tôi từng vài lần cho bà nghỉ việc" | Ông nổi nóng với bà (vụ cây sồi và ít nhất ba lần khác), bà coi như không; không hề đuổi việc (70) | WRONG | "Tôi từng nhiều lần nổi nóng với bà" |
| s01 | "vẫn không thể thiếu bà" | "người không thể thiếu được" (70) | OK | giữ |
| s01/02 | (không có) Molly mất vì ung thư | (70) | MISSING-IMPORTANT | thêm "Bà mất vì ung thư" (s02) |
| s02 | "một bất ngờ đang chờ tôi" | Chiều nắng, sân sau nhà con trai Molly (70) | OK | thêm "Chiều nắng hôm ấy"; bối cảnh sân sau ghi trong image-details |
| s03 | "Một người phụ nữ tên Monica bước đến, xúc động cảm ơn tôi" (Monica nói trước) | Alvin gọi tên Yalom ở cổng, tự giới thiệu mình và Monica trước; Monica nói sau (70–71) | WRONG | Alvin nói trước, Monica nói sau |
| s03 | "vì đã thay đổi cuộc đời chồng cô" | Monica: "tôi nợ ông về cuộc hôn nhân của chúng tôi và cả hai đứa con" (71) | WRONG | dùng lời Monica theo sách |
| s03 | "người chồng đĩnh đạc chỉ lặng im" | Alvin là người nói nhiều nhất: tự giới thiệu, nhắc ký ức, đưa danh thiếp (70–71) | WRONG | bỏ |
| s03 | "Tôi không tài nào nhớ ra anh" | Không nhận ra vì kém nhận diện khuôn mặt (71) | OK, MISSING lý do | thêm "Vốn kém nhớ mặt" |
| s03 | (không có) ở cổng, đang vội ra sân bay | (70) | MISSING-IMPORTANT | "Ra đến cổng, tôi nghe gọi tên mình" |
| s04 | "Tôi hẹn gặp lại họ" | Hẹn cà phê với Alvin trong tuần; Alvin đưa danh thiếp (71) | OK, thiếu chi tiết | "Tôi nhận danh thiếp, hẹn anh uống cà phê" |
| s04 | "rồi về lục tìm hồ sơ bệnh án cũ" | Ngay tối đó (72) | OK | giữ |
| s05 | "Hồ sơ năm 1982, mười hai giờ trị liệu" | (72) | OK | thêm "dày cộp ghi chép" (hồ sơ dày, 72) |
| s05 | "chuyên gia X-quang tại Stanford" | (71–72) | OK | giữ |
| s05 | "Ngoài ba mươi, tự tin" | (73) | OK | Theo quyết định của người dùng (không nhấn mạnh tuổi), đổi thành "Anh rất tự tin."; chi tiết tuổi chuyển sang image-details |
| s05 | "tóc điểm bạc, mặc áo blouse trắng thêu tên mình bằng chỉ xanh sẫm" | Đúng sách (73) nhưng chỉ là ngoại hình | STYLE | bỏ khỏi lời kể, chuyển sang image-details |
| s05 | (không có) tìm đến sau bài nói ở hội nghị y khoa | (73) | MISSING-IMPORTANT | "Anh tìm đến sau khi nghe tôi nói ở một hội nghị y khoa" |
| s06 | "ngay sau cái chết của em trai, Jason" | "tới gặp ông ngay sau khi em trai tôi mất" (71) | OK | giữ ý |
| s06 | "Mười lăm năm hai anh em không nói" | Hơn 15 năm (75) | WRONG (nhẹ) | "Suốt hơn mười lăm năm" |
| s06 | "Jason tìm đến, nhờ anh xem tấm phim phổi" | Jason **gọi điện** từ Bắc Carolina: "Em đã bị ung thư phổi" (77) | WRONG (nhẹ) | "Jason gọi từ Bắc Carolina: em bị ung thư phổi, nhờ anh xem phim" |
| s07 | "Mỗi ngày, Alvin đọc cái chết trên phim X-quang" | Năm năm viết báo cáo "chết người" (74) | OK | bỏ để giữ độ dài; ý sợ đi làm chuyển sang s12 |
| s07 | "lá phổi của chính em trai mình, không thể cứu vãn" | Khối u ăn hết phổi trái, di căn xương và não, "không còn hi vọng" (79) | OK | "Khối u đã lan vào xương và não, không thể cứu vãn" |
| s07 | "qua làn khói thuốc, ánh mắt Jason vẫn đầy thách thức" | (79) | OK | giữ; thêm "Alvin bay ngay đến" (79) |
| s08 | "lớn lên dưới cái bóng của người anh xuất sắc, chán học rồi sa vào nghiện ngập" | (75–76) | OK | thêm "kém anh hai tuổi" (75) |
| s08 | "bị Alvin gay gắt ngăn cản chuyện cưới vội" | Cha mẹ nhờ Alvin cảnh báo và bắt anh hứa giữ kín; sách không nói "gay gắt" hay "cưới vội", chỉ là đính hôn (76) | WRONG / MISSING-IMPORTANT | "Jason đính hôn. Cha mẹ bí mật nhờ Alvin can ngăn" |
| s08 | "Jason ôm hết tiền nhà bỏ đi biệt xứ" | Sáng hôm sau, biến mất cùng toàn bộ tiền trong nhà, không bao giờ liên lạc (76) | OK | thêm "Sáng hôm sau" |
| s08 | "Giờ thì những điều chưa nói sẽ mãi mãi không được nói ra" | Yalom: quan hệ "đóng băng thành một trạng thái chưa hoàn thành" (85–86) | OK (diễn giải) | bỏ để giữ độ dài |
| s10 | "đêm nào Alvin cũng mơ" | Lặp lại "vài lần trong cả tháng qua" (83) | WRONG | "Alvin gặp một ác mộng lặp lại" |
| s10 | "một con quạ đen khổng lồ… lao thẳng vào anh trong bóng tối" | Trong phòng tắm, đang soi gương, một con chim đen rất to lao vào phòng; đèn yếu dần rồi tắt; anh chạy, nghe tiếng cánh đập sau lưng (83) | WRONG (nhẹ) | "con chim đen khổng lồ lao thẳng vào phòng tắm, đèn tắt dần, anh bỏ chạy trong bóng tối" |
| s10 | "như bước ra từ thơ Edgar Allan Poe" | Liên tưởng của chính Alvin: con quạ của Poe (84) | OK | ghi rõ là lời Alvin: "anh nói" |
| s10 | "Con quạ của những điều dang dở, không thể vãn hồi" | Alvin: giấc mơ "về cái chết", "cuộc sống đang dần biến mất" (84) | UNSUPPORTED | "Giấc mơ về cái chết" |
| s12 | "tấm phim nào cũng làm anh nhớ đến Jason" | Nhất là phim ngực (82) | OK | "tấm phim ngực nào cũng gợi nhớ Jason" |
| s12 | "mối quan hệ nào cũng cần nỗ lực từ hai phía" | "Là một người anh tốt cần có sự hợp tác nào đó từ phía người em" (86) | OK | bỏ để giữ độ dài |
| s12 | "ăn một mình, đi về một mình, chưa mối tình nào kéo dài" | Ăn một mình, cuối tuần một mình, không ai trụ lâu (82–83) | OK | "cuối tuần một mình" |
| s14 | "chú chó nhỏ mà người cha bác sĩ không cứu nổi" | Chó Max bị xe đâm; cha (bác sĩ gia đình) lắc đầu (90); kích cỡ chó không được nêu | OK, "nhỏ" UNSUPPORTED | "chú chó Max" |
| s14 | "người cha bác sĩ" | Bác sĩ gia đình ở nông thôn Virginia (82) | OK | giữ |
| s14 | "người bạn Ralph bất động trong lồng phổi sắt" | Ralph chết vì viêm tủy xám (bại liệt); không có phổi sắt; Alvin không thân với Ralph (91) | WRONG | "người bạn Ralph chết vì bệnh bại liệt" |
| s14 | "Với Alvin, cái chết là chấm hết vĩnh viễn" | Đó là quan điểm của **người cha** ("thoát ra"); Alvin không thể chấp nhận ý nghĩ mọi thứ kết thúc với mình (91–92) | WRONG (gán sai người) | "Ý nghĩ mọi thứ sẽ chấm hết với chính mình làm anh kinh hãi" |
| s14 | (không có) cha mẹ chết trong tai nạn mười năm trước, anh thành mồ côi | (81, 89) | MISSING-IMPORTANT | thêm "cha mẹ mất trong tai nạn mười năm trước" |
| s16 | "Ác mộng thưa dần" | "Không còn những cơn ác mộng nữa" (93) | WRONG (nhẹ) | "Ác mộng dứt hẳn" |
| s16 | "Alvin càng muốn kết thúc trị liệu" | Alvin hỏi đã kết thúc được chưa (93) | OK | giữ ý |
| s16 | "anh vẫn đang che giấu điều gì đó" | Yalom nhận ra sự kháng cự (95–96) | OK | giữ |
| s17 | "người phụ nữ nào cũng rời bỏ anh, ngay sau lần đầu bước vào nhà anh" | (99) | OK | giữ ý |
| s17 | "Sau nhiều lần nài nỉ, anh miễn cưỡng để tôi đến" | Yalom đề nghị đến nhà; Alvin gọi 7:01 xin dừng; Yalom thuyết phục; hẹn 7:30 tối cùng ngày (99–101) | OK, thiếu chi tiết | "Tôi xin đến nhà anh. Anh định bỏ cuộc, rồi anh miễn cưỡng để tôi đến" |
| s18 | "Hàng trăm chồng báo cũ chất kín chân tường" | Danh bạ, sách, catalogue, báo ố vàng, tạp chí, phim X quang, bệnh án phủ sàn; lối đi khoảng 10 inch (102); không có con số "hàng trăm" | UNSUPPORTED (nhẹ) | "Sách, báo cũ, tạp chí, phim X-quang phủ kín sàn nhà" |
| s18 | "Một tâm trí đã đóng băng suốt mười năm, kể từ ngày cha mẹ anh qua đời" | Sách không nối việc tích trữ với cái chết của cha mẹ. Năm 1982, chính Yalom cũng chưa hiểu chứng này (102–103) | UNSUPPORTED | bỏ; thay bằng "Căn nhà nhỏ ở Sunnyvale" và "Alvin ngồi quay lưng về phía tôi, im lặng" (101–102) |
| s20 | "Anh chết lặng vì xấu hổ" | Alvin im lặng, quay lưng; Yalom đã gọi tên nỗi xấu hổ từ trước (100, 102–103) | OK (diễn giải) | thay bằng hành động trong sách |
| s20 | "lịch sự mà dứt khoát mời tôi ra về" | Yalom cảm ơn và xin lỗi; Alvin lắc đầu "Không phải bây giờ"; Yalom ngồi im vài phút rồi tự ra về (103–104) | WRONG | "Tôi cảm ơn anh, xin lỗi vì đã thúc ép. Anh chỉ lắc đầu: 'Không phải bây giờ.'" |
| s20 | "Sáng hôm sau, anh gọi điện chấm dứt trị liệu" | (104) | OK | giữ |
| s21 | "Suốt nhiều năm, tôi tin mình đã thúc ép anh quá sớm, và đã thất bại" | Yalom đóng hồ sơ; từng hỏi ý một người bạn về khủng hoảng của mình quanh ca này (104–105) | OK (diễn giải hợp lý) | "Tôi đóng hồ sơ, tin rằng mình đã thất bại" |
| s21 | "buổi gặp lại sau tang lễ" | Quán cà phê gần bệnh viện (105) | OK | giữ |
| s22 | "Alvin mỉm cười" | Alvin sững sờ: "Ông không nhớ sao?" (105) | WRONG | "Alvin sững sờ" |
| s22 | "Chính ông đã giới thiệu bà Molly cho tôi" | Yalom gọi điện cho anh tên Molly 1–2 ngày sau buổi cuối (106) | OK | giữ |
| s22 | "dọn sạch căn nhà đóng băng ấy" | Dọn sạch trong vài ngày (106) | OK, "đóng băng" bỏ vì gắn với ý s18 không có căn cứ | "Bà ấy dọn sạch căn nhà" |
| s22 | "lo liệu mọi việc cho tôi suốt nhiều năm" | Ba mươi năm, mỗi tuần (106) | OK, thiếu số | "suốt ba mươi năm" |
| s22 | "để tôi mở lòng đón nhận Monica" | Sách không nói Molly là nguyên nhân hôn nhân; Alvin nói: "ông đã tặng cho tôi Molly", điều tốt nhất đời anh **sau** Monica và hai con (106) | UNSUPPORTED | "Trên hết, ông đã tặng tôi Molly. Bà là điều tốt nhất đời tôi, sau Monica và hai đứa con" |
| s23 | "Tôi hoàn toàn không nhớ chuyện đó" | (106) | OK | giữ |
| s23 | "mọi lý thuyết trị liệu không bằng một sự giúp đỡ cụ thể" | Yalom: nhà trị liệu không thể "chính xác"; môi trường chân thành giúp bệnh nhân tự tìm điều họ cần (107). Câu "không bằng" là phóng đại | UNSUPPORTED (nhẹ) | "Trị liệu hiếm khi chính xác như sách vở. Đôi khi, điều cứu người ta là một sự giúp đỡ cụ thể, đời thường" |
| s23 | "Đủ chân thành, con người sẽ tự biết nắm lấy điều họ cần" | (107) | OK | giữ ý |
| s23 | "Cảm ơn bà, Molly." | (107) | OK | giữ |

## Những điểm được yêu cầu kiểm tra

- **Người cha là bác sĩ:** đúng. Ông là bác sĩ gia đình ở nông thôn Virginia (82), cầm túi đen chạy ra xem Max (90).
- **"Nhà đóng băng mười năm từ khi cha mẹ mất":** không có căn cứ. Đã bỏ.
- **Phổi sắt:** không có trong sách. Đã bỏ.
- **Molly làm việc khoảng 30 năm và do Yalom giới thiệu:** đúng (106).
- **Ác mộng:** đúng là chim đen và đèn tắt. "Đêm nào cũng mơ" thì sai. Đã sửa.
- **Chi tiết tình dục:** cả bản cũ lẫn bản mới đều không có. Chủ đề nỗi sợ cái chết vẫn giữ.

## Đếm

- WRONG: 15 (s01 ×2, s03 ×3, s06 ×2, s08, s10 ×2, s14 ×2, s16, s20, s22)
- UNSUPPORTED: 8 (s01, s10, s14 "nhỏ", s18 ×2, s22 "mở lòng", s22 "đóng băng", s23)
- Tất cả 23 mục WRONG/UNSUPPORTED đều đã sửa hoặc bỏ. 6 mục MISSING-IMPORTANT đã được thêm vào. 1 mục STYLE (ngoại hình ở s05) đã chuyển sang image-details.
