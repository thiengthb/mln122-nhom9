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

## 04/11/2026: bản thử hướng "Sợi chỉ xuyên suốt"
- Đề xuất 4 công nghệ (giữ khung cũ + GSAP và View Transitions; reveal.js; Slidev; Motion) và 3 phong cách. Người dùng chọn hướng A.
- GSAP 3.13 lưu trong `vendor/gsap` (chạy được khi không có mạng). Phần mới ở `src/soi-chi.part`, không sửa `app.part`; build ra `soi-chi.html` và `src/deck-soi-chi.html`. `index.html` chưa đổi.
- Làm kỹ 3 slide: bìa (sợi chỉ gạch dưới tiêu đề rồi chạy vào đáy khung dệt), bốn cuộc cách mạng (trục thời gian vẽ dần theo 4 giai đoạn, nét đổi kiểu, cuối tỏa nhánh vào mạng lưới), c/v (đường cong c/v vẽ theo thanh trượt, số từ mô hình giả định sẵn có). Các slide khác: sợi chỉ gạch dưới tiêu đề, chuyển cảnh sợi chỉ rút ra. Chưa dùng View Transitions.
- Link artifact cũ 7go3S9km... không đọc được từ phiên này. Bản thử đăng ở https://claude.ai/artifact/GHAYsKUXMt3XGWue1rbVNH

## 04/11/2026: bản nháp B "Bản vẽ kỹ thuật động"
- Người dùng chọn thử hướng B, cho phép đổi cả bố cục, màu, sơ đồ. Bản nháp riêng, chưa đưa về bản chính.
- Nguồn: `src/b/slides.part` (bố cục mới, ghi chú để trống, lúc build tự lấy lời nói từ `src/slides.part` theo tên slide), `src/b/b.css.part`, `src/b/b.part`. Build ra `ban-b.html` và `src/deck-b.html`.
- Ý tưởng: mỗi slide là một tờ bản vẽ (viền đôi, ô tọa độ 1–8, A–D, khung tên có số tờ và thanh tỉ lệ thay thanh tiến độ); số liệu dùng nét ghi kích thước (slide 6); khối quan trọng là mặt cắt gạch chéo; sơ đồ tự lắp bằng nét nối (slide 5, 10, 12, 17, 19); bánh răng ở tâm (10, 17); bậc thang và cú nhảy cho luận điểm (3, 21); đường c/v (14); số đếm lên.
- Ba kiểu màu mới (phím D): Giấy can, Bản in xanh, Bàn vẽ đêm. Không thêm số liệu mới.
- Góp ý của người dùng: thích sơ đồ của bản B nhưng bỏ khung viền ngoài, muốn mềm mại như bản cũ. Đã bỏ khung bản vẽ và khung tên, quay lại 3 kiểu màu cũ, nền lưới, số slide và sợi chỉ tiến độ; khối bo tròn có nền, nét nối màu nhạt. Phần "B mềm" nằm cuối `src/b/b.css.part`.
