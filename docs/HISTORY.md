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
- Người dùng xem bản mềm và yêu cầu quay lại như cũ: đã hoàn tác, bản B giữ khung bản vẽ và khung tên như lần đăng đầu.
- Sau đó người dùng yêu cầu chỉ bỏ khung viền ngoài: đã bỏ viền đôi và ô tọa độ, giữ khung tên (thêm viền đủ 4 cạnh), giữ màu và mọi thứ khác của bản B.
- Rà lỗi giao diện bản B (quét tự động chữ đè chữ + xem ảnh 22 slide): sửa nhãn đè hình ở slide 3 và 21; slide 13 xếp lại số, lưới và lời giải thích để không tràn xuống câu dưới; slide 18 bỏ vòng vạch chia bị vẽ lệch; slide 19 bỏ khoảng trống quá lớn; slide 20 thu gọn ba khối.
- Sửa khung tên bị tràn (thanh tỉ lệ 22 ô lọt ra ngoài viền vì khung cao cố định 46px): bỏ chiều cao cố định, ô nhỏ lại, viền đủ 4 cạnh.
- Thêm tiểu tiết và hoạt ảnh cho bản B, không thêm số liệu: chuyển slide bằng nét bút quét ngang (đi lùi thì quét ngược); số câu hỏi 1, 2, 3 rất lớn, nét viền mờ ở góc phải trên, tự ẩn khi tiêu đề dài chạm tới; nét nối nhấn có dòng chảy sau khi kẻ xong; bong bóng số bật ra; "60–80 năm", "20–30 năm" đếm lên; slide 4 có thanh thời gian chạy theo từng giai đoạn; slide 16 có nét đứt nối đỉnh các cột; slide 12 ô kết luận nháy vòng sóng; ô đang đứng ở thanh tỉ lệ nhấp nháy nhẹ. Tắt hết khi máy bật giảm chuyển động.

## 04/11/2026: Bản nháp C "Báo chí dữ liệu"
- Bản B được giữ nguyên (đường dẫn cũ). Bản C là bản riêng: `src/c/slides.part` chép từ bố cục bản B, giao diện ở `src/c/c.css.part` (nạp sau `deck.css.part` và `src/b/b.css.part`), hoạt ảnh ở `src/c/c.part`. Build ra `ban-c.html` và `src/deck-c.html`.
- Kiểu mặt báo: tiêu đề dùng chữ có chân Newsreader (giấy phép OFL, lưu ở `fonts/`), dòng đầu trang ghi phần đang nói, người nói, số trang và vạch đỏ tiến độ; khối nội dung dùng gạch đầu thay cho hộp; biểu đồ dùng màu xám cho bối cảnh, một màu nhấn cho Việt Nam.
- Tiêu đề hiện theo từng cụm (đến dấu phẩy, hai chấm, chấm hỏi, xuống dòng hoặc phần in màu), rồi phần in màu được tô dần như bút dạ quang.
- Biểu đồ tự chạy: thanh mọc dần và số đếm lên (slide 9, 15), ô vuông hiện lần lượt (11, 13), thác nước (16), nét kích thước (6), nét nối sơ đồ (5, 10, 12, 17, 19). Slide 18 đổi từ đồng hồ sang thanh đích: mỗi chỉ tiêu một thang riêng, phần gạch chéo là chặng còn lại.
- Ba kiểu màu (phím D): Giấy báo, Bản tối, Xanh đêm. Không thêm số liệu mới.

## 04/11/2026: Quay lại bản B, đợt chi tiết 2
- Người dùng chọn quay lại bố cục B (bản C vẫn giữ ở đường dẫn riêng, không sửa thêm). Thêm cho B, không thêm số liệu:
  - Ngòi bút (chấm tròn có viền) chạy theo đầu mọi nét đang được vẽ: bậc thang, nét kích thước, nét nối sơ đồ.
  - Slide 3: chấm "đi tắt" bay theo đường đứt, rồi chấm "năng lực" leo từng bậc, lặp lại. Slide 21: chấm leo bậc.
  - Slide 7: ngòi bút chạy trên ba con đường đúng nhịp nét đang vẽ, đến đích thì có vòng sóng.
  - Slide 13: dấu khác tự vẽ (hai gạch ngang rồi nét chéo). Slide 18: vạch chia sáng dần theo cung, có dấu đích ở đỉnh vòng.
  - Mặt cắt gạch chéo quét từ trái sang sau khi viền kẻ xong. Ô để trống ở slide 2 có viền đứt chạy vòng. Tên tờ trong khung tên gõ ra từng chữ.
  - Bấm vào con số để soi nguồn: có đường dẫn kẻ từ con số sang ô nguồn, như chú thích trên bản vẽ.

## 04/11/2026: phản biện review Codex lần 2, sửa nội dung (nhánh claude/project-thread-rshvkc)
- Kiểm lại từng điểm bằng nguồn gốc, ghi ở cuối `docs/03`. Nhận phần lớn; không nhận: Kahoot tính trong 20 phút (người dùng đã xác nhận Kahoot riêng), tốc độ "135–150 từ" (tiếng Việt tính theo âm tiết), nguồn 67,1% Codex dẫn sai, số Hàn Quốc 94 USD (năm tỷ giá tụt), đưa slide 14 vào phụ lục.
- Lời nói: cắt từ khoảng 4.050 xuống khoảng 2.850 âm tiết; build giờ không đếm chỉ dẫn trong ngoặc vuông và tính ở 150 âm tiết/phút (khoảng 19 phút; ở 170 là khoảng 17 phút). Thêm chỉ dẫn nhấn, dừng, thao tác trong ngoặc vuông ở các slide chính. Bàn giao theo nội dung, bỏ "Cảm ơn [Người X]".
- Phân vai: slide 13 (86% hay dưới 2%) chuyển sang Người 3.
- Sửa: định nghĩa CNH, HĐH ở slide 10; slide 9 dùng R&D World Bank 2023 cho cả ba nước; slide 14 ghi giới hạn mô hình; slide 15 bỏ 90,5% và 5–7%, ghi mẫu Bangladesh và 67,1%; slide 16 nói rõ WEF không riêng AI, thêm số riêng AI, thêm bốn tác nhân; slide 17 "nhóm gom thành năm cụm"; slide 18 bỏ vòng tiến độ, thành thẻ "hiện tại, mốc 2030"; slide 19, 20, 21 sửa câu chữ. Đổi nguồn NQ57, Luật AI, GII sang trang chính thức.
- Bản B (nhánh khác) lấy lời nói từ `src/slides.part` theo tên slide nên tự nhận lời mới; chữ trên slide của bản B ở `src/b/slides.part` phải chép lại các sửa đổi này khi gộp. `#gauges` giữ id, đổi cách vẽ trong `src/app.part`.
- Nhóm phải tự nói lại lời nói bằng lời của mình (FAQ: AI viết toàn bộ script là vi phạm).

## 04/11/2026: Bản B đợt 3
- Gộp main (PR #3 sửa nội dung) vào nhánh bản B và chép các sửa chữ trên slide sang `src/b/slides.part` (slide 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 21). Slide 18 bỏ mặt đồng hồ, dùng thẻ như bản chính, vì bốn chỉ tiêu khác đơn vị và không tính phần trăm hoàn thành. Bản C cũng chép chữ mới và tắt thanh đích ở slide 18 vì cùng lý do.
- `src/app.part`: thời gian mỗi giai đoạn ở slide 4 đọc từ `window.N9_STAGE` nếu có (bản chính vẫn 13,5 giây). Bản B đặt 6,75 giây.
- Slide 4 bản B: chụp lại hình ở cuối mỗi giai đoạn; khi đến giai đoạn 4, hình lớn thu nhỏ vào ô 4, rồi ô 1, 2, 3 hiện lần lượt với mũi tên 1 → 2, đường nối từ 2 vòng xuống 3, rồi 3 → 4.
- Khung tên mới: ô PHẦN (Mở đầu, Câu hỏi 1–3, Kết luận), tên tờ, người nói có 5 chấm, số tờ; hàng dưới là thanh tiến độ chia theo phần, phần đang nói được tô nền.
- Tiêu đề hiện theo từng cụm (như bản C) nhưng giữ chữ và màu bản B.
- Khi đi tới phần câu hỏi mới (slide 4, 13, 17) có tờ bìa phụ: số câu hỏi lớn được kẻ nét, câu hỏi hiện theo cụm, nét kích thước, tên người nói; khoảng 1,5 giây. Đi lùi thì không có tờ bìa phụ.

## 04/11/2026: Bản B, sửa theo nhận xét sau đợt 3
- Slide 18 bản B quay lại mặt đồng hồ (vòng, vạch chia sáng dần, tam giác đích) theo ý người dùng; dữ liệu lấy từ mảng `G` mới của bản chính, chữ "Mốc 2030", "Mốc theo" như bản chính, thêm ghi chú g[11]. Bản chính vẫn dùng thẻ. Lưu ý: vòng tô màu dễ làm người xem hiểu là phần trăm hoàn thành, trong khi chú thích dưới slide ghi "không tính phần trăm hoàn thành"; nhóm cần nói rõ điều này khi trình bày hoặc sửa câu chú thích.
- Khung tên thu gọn: chỉ còn "Người n", số tờ "NN / 22" và dãy 22 ô nhỏ ở góc phải dưới; không khung, không nền, chữ mờ. Bỏ ô PHẦN, tên tờ, chấm người nói, thanh chia phần.
- Chỗ đè chữ: slide 14 khi kéo mức tự động hóa lên 100% thì ba khung cao hơn hàng, đè lên dòng "Giả định". Thu lưới chấm (390 → 340px) và đường c/v (cao 150px). Đã chụp lại 22 slide ở ba giao diện và chạy kiểm tra đè chữ.
- Góc tờ (sau nhận xét "hơi nhạt và nhỏ"): cùng cỡ chữ 15px, cùng phông và màu với dòng Nguồn, cùng đường chân chữ và lề phải 70px đối xứng với lề trái; bỏ độ mờ.

## 04/11/2026: Chốt bản B làm bản chính
- Người dùng chốt "Bản vẽ kỹ thuật động" (bản B) là giao diện chính. `index.html` và `src/deck.html` giờ giống hệt bản B đã đăng (đã so từng byte).
- Cấu trúc: `src/b/slides.part` thay `src/slides.part` (đã ghép lại ghi chú của 22 slide, kịch bản `docs/06` không đổi); `src/b/b.css.part` → `src/ban-ve.css.part`; `src/b/b.part` → `src/ban-ve.part`. `scripts/build.py` build bản chính từ các file này.
- `ban-b.html` chỉ còn chuyển hướng sang trang chính. `soi-chi.html` giữ nguyên, không build lại. Bản C vẫn build được nhưng đã gác lại.
- Từ nay sửa chữ trên slide chỉ cần sửa `src/slides.part` (không còn bản chép riêng cho B).
- Còn treo: câu chú thích slide 18 "không tính phần trăm hoàn thành" trong khi slide dùng vòng tròn; chưa có bản PDF để nộp.

