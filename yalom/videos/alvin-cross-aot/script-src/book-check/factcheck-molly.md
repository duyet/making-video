# Kiểm tra lời bình "Thank you Molly" (`thank-you-molly/lines.json`)

Tôi chỉ ghi chú ở đây, không sửa văn bản. Các dòng không có trong bảng đều khớp với sách.

| Dòng | Câu | Sách nói (trang) | Kết luận | Đề xuất |
|---|---|---|---|---|
| m04 | "Tôi từng đuổi việc bà vài lần" | Yalom **nổi nóng** với Molly (vụ cây sồi và ít nhất ba lần khác), bà coi như không; ông không đuổi việc bà (70) | WRONG | "Tôi từng nổi nóng với bà không ít lần, nhưng rồi phải thừa nhận rằng mình không thể thiếu bà." |
| m05 | "một người đàn ông đội mũ Panama" | Sách chỉ nói "người đàn ông luống tuổi", không nhắc tới mũ. Ông gặp Alvin ở cổng ra đường, khi đang vội đưa bạn ra sân bay (70) | UNSUPPORTED | Bỏ chi tiết mũ Panama, hoặc chỉ giữ trong hình ảnh. Có thể thêm "Khi tôi vội ra cổng…" |
| m03 | "từ hóa đơn đến giấy tờ, sửa chữa" | Tài chính, hóa đơn, giao thiệp, giấy tờ, hợp đồng, làm vườn, tạp vụ; việc nhỏ thì bà tự làm (69) | OK (chữ "sửa chữa" hơi lỏng) | Không bắt buộc sửa |
| m06 | "một phần là nhờ tôi" | Monica: "tôi nợ ông về cuộc hôn nhân… và cả hai đứa con" (71) | OK (diễn đạt mềm hơn) | — |
| m18 | "Alvin thường xuyên gặp ác mộng" | Ác mộng lặp lại "vài lần trong cả tháng qua" (83) | OK (chữ "thường xuyên" hơi mạnh) | Không bắt buộc sửa |
| m27 | Buổi trị liệu tại nhà Alvin | Lịch ban đầu là một tuần sau; sau đó dời thành tối cùng ngày, sau cuộc gọi 7:01 (99–101) | OK | — |
| m35 | "Ngay sau buổi gặp cuối" | Một hai ngày sau buổi trị liệu cuối (106) | OK | — |

Tóm lại có 1 lỗi sai (m04: đuổi việc) và 1 chi tiết không có trong sách (m05: mũ Panama). Phần còn lại khớp với sách.

## Các thay đổi đã áp dụng (`molly.lines.json`)

Người dùng yêu cầu bám theo sách, chỉ sửa ở mức tối thiểu và giữ nguyên câu chữ của sheet ở mọi chỗ khác. Chỉ hai dòng thay đổi; 38 dòng còn lại giữ nguyên từng chữ. Các cue trong `thank-you-molly/shots.json` vẫn khớp: m04 vẫn dùng cue "không thể thiếu bà", và m05 không có cue.

| Dòng | Cũ | Mới | Lý do |
|---|---|---|---|
| m04 | "Tôi từng **đuổi việc** bà vài lần, …" | "Tôi từng **nổi nóng với** bà vài lần, …" | Tr. 70: Yalom nổi nóng với Molly, chứ không đuổi việc bà |
| m05 | "một người đàn ông **đội mũ Panama** tiến đến cùng vợ" | "một người đàn ông tiến đến cùng vợ" | Sách không nhắc tới mũ Panama. Tôi cũng không thêm "luống tuổi", theo quyết định không nhấn mạnh tuổi nhân vật |

Các mục chỉ hơi lỏng (m03 "sửa chữa", m18 "thường xuyên") không sai so với sách, nên giữ nguyên.
