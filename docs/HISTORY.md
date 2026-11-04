# Nhật ký dự án

## 02/11/2026: phiên đầu (Claude)
- Đọc sheet lớp, file Assignment, Slot 0, giáo trình mục 6.1 và 3.1.3, 3.2.3, mục lục toàn cuốn; 18 slide của nhóm 6.
- Nghiên cứu nguồn ngoài, lập bảng kiểm chứng.
- Quyết định của người dùng: repo công khai; thành viên, ngày điền sau; khảo sát cả lớp theo kiểu giơ tay, nhập tay.
- Quyết định thiết kế: mạch "sợi chỉ" từ ngành dệt (CMCN 1) đến AI; bấm số ra nguồn; khảo sát đầu và cuối bài; mô phỏng c/v.

## 04/11/2026: nhận review Codex và góp ý của người dùng
Xem `docs/08-ra-soat-va-ke-hoach-v2.md`. Chưa sửa slide, đang chờ người dùng chốt và chờ trình duyệt.

## 04/11/2026: bản 2
Dựng lại hoạt ảnh, sơ đồ, một phím một nhịp; bỏ khảo sát; thêm Nhật Bản, Hàn Quốc và NQ57 nguyên văn; sửa câu chữ; kịch bản 5 người; Kahoot.

## 04/11/2026: bỏ slide Minh bạch AI
Người dùng phản biện, thống nhất: slide không bắt buộc. Phụ lục AI là file riêng theo Tab 6, nộp email cùng slide trước 24h. Deck còn 22 slide. GitHub Pages do người dùng bật.

## Việc còn lại của nhóm
Xem mục "Việc nhóm phải làm" trong README.

## 02/11/2026: slide bản đầu
- 21 slide, tự kiểm tra: không lỗi JavaScript, không tràn khung, mô phỏng ra đúng 3,50 và 80 ở mức 100%.
- Chưa bật được GitHub Pages từ phiên Claude (bị chặn); người dùng bật trong Settings hoặc nối Vercel.
- Chưa thử trên máy chiếu thật.

## 04/11/2026: viết lại lời nói, giao diện mới
- Viết lại toàn bộ ghi chú người nói; thay từ lạ trên slide (trên chuyền, thoi bay, xe kéo sợi, hậu kiểm, NICs, ròng). Trích dẫn nguyên văn giữ nguyên, giải thích ở lời nói.
- Lời nói khoảng 24 phút ở tốc độ 170 tiếng mỗi phút, chưa bấm giờ thật.
- Bỏ bộ đếm giờ trên slide (cửa sổ người nói vẫn có đồng hồ), thêm số slide.
- Ba giao diện, đổi bằng phím D: Giấy kỹ thuật (mặc định), Rừng rêu, Chàm cũ.
- Sửa slide 22: danh mục tràn khung, ba mục cuối bị khuất.
- Còn chờ: thứ tự 5 người, ngày thuyết trình, kiểm chứng của nhóm cho Phụ lục AI.

## 04/11/2026: bàn giao sang chat mới
Người dùng đã chốt: giữ câu "nhóm dùng AI hỗ trợ" ở slide 19; không đọc câu mời phản biện và Kahoot ở cuối slide 21.
Việc tiếp theo:
1. Người dùng chọn kiểu màu (mặc định Giấy kỹ thuật) và góp ý lời nói.
2. Sau 22h 04/11: nhận thứ tự 5 người, ngày thuyết trình. Thay `[Người 1]`...`[Người 5]` trong `src/slides.part`, điền `CONFIG.ngay` và phân công trong `src/app.part`.
3. Tạo file Word Phụ lục AI theo mẫu Tab 6 từ `docs/05`; cột kiểm chứng phải là thông tin thật do nhóm cung cấp, không tự điền.
4. Soạn mẫu Biên bản nhóm theo Tab 7.
5. Tập nói, bấm giờ thật, thử trên máy chiếu; kiểm tra lại link GitHub Pages: https://thiengthb.github.io/mln122-nhom9/
Bản đăng trang slide: https://claude.ai/artifact/7go3S9kmCDnw2bBwPx3iyL (đăng lại `src/deck.html` với `url` này, chat mới phải đọc artifact trước khi đăng).

## 04/11/2026: phản biện review Codex lần 2, sửa nội dung (nhánh claude/project-thread-rshvkc)
- Kiểm lại từng điểm bằng nguồn gốc, ghi ở cuối `docs/03`. Nhận phần lớn; không nhận: Kahoot tính trong 20 phút (người dùng đã xác nhận Kahoot riêng), tốc độ "135–150 từ" (tiếng Việt tính theo âm tiết), nguồn 67,1% Codex dẫn sai, số Hàn Quốc 94 USD (năm tỷ giá tụt), đưa slide 14 vào phụ lục.
- Lời nói: cắt từ khoảng 4.050 xuống khoảng 2.850 âm tiết; build giờ không đếm chỉ dẫn trong ngoặc vuông và tính ở 150 âm tiết/phút (khoảng 19 phút; ở 170 là khoảng 17 phút). Thêm chỉ dẫn nhấn, dừng, thao tác trong ngoặc vuông ở các slide chính. Bàn giao theo nội dung, bỏ "Cảm ơn [Người X]".
- Phân vai: slide 13 (86% hay dưới 2%) chuyển sang Người 3.
- Sửa: định nghĩa CNH, HĐH ở slide 10; slide 9 dùng R&D World Bank 2023 cho cả ba nước; slide 14 ghi giới hạn mô hình; slide 15 bỏ 90,5% và 5–7%, ghi mẫu Bangladesh và 67,1%; slide 16 nói rõ WEF không riêng AI, thêm số riêng AI, thêm bốn tác nhân; slide 17 "nhóm gom thành năm cụm"; slide 18 bỏ vòng tiến độ, thành thẻ "hiện tại, mốc 2030"; slide 19, 20, 21 sửa câu chữ. Đổi nguồn NQ57, Luật AI, GII sang trang chính thức.
- Bản B (nhánh khác) lấy lời nói từ `src/slides.part` theo tên slide nên tự nhận lời mới; chữ trên slide của bản B ở `src/b/slides.part` phải chép lại các sửa đổi này khi gộp. `#gauges` giữ id, đổi cách vẽ trong `src/app.part`.
- Nhóm phải tự nói lại lời nói bằng lời của mình (FAQ: AI viết toàn bộ script là vi phạm).
