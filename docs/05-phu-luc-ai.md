# Phụ lục AI: bản ghi trung thực từ phiên làm việc (nhóm chuyển sang mẫu Tab 6)

**Tên nhóm:** Nhóm 9, SE1919. **Chủ đề:** 9. **Cam kết:** nhóm tự điền và chỉ ký khi đúng sự thật.

| Nhiệm vụ | Công cụ | Prompt chính | Kết quả AI | Kiểm chứng và sử dụng | Minh chứng |
|---|---|---|---|---|---|
| Đọc tài liệu môn học | Claude (model cấu hình `claude-opus-5-5`, Anthropic) | "Tìm giáo trình ở tab Link, đọc hiểu, tập trung phần nhóm 9, giữ lại link" | Ghi chú theo trang (`docs/02`), tóm tắt (`docs/01`) | [Nhóm điền: ai đã đối chiếu những trang nào] | https://claude.ai/code/session_01WXAvBWwoXd7CQFBHFUbUuf |
| Nghiên cứu số liệu | Claude, tìm kiếm web | "Nghiên cứu tài liệu bổ sung có trích dẫn, ưu tiên nguồn chính thống" | Bảng nguồn (`docs/03`), trong đó đánh dấu số dẫn lại | [Nhóm điền: đã mở lại link nào, có sửa số nào không] | như trên |
| Dựng slide web | Claude | "Làm trang web thiết kế thành slide thuyết trình, chấm theo tab Score, sáng tạo hơn nhóm 6" | Toàn bộ mã và bản nháp nội dung slide | [Nhóm điền: đã sửa gì, viết lại gì] | Lịch sử commit repo |
| AI phản biện | Claude | "Đóng vai nhóm phản biện, đặt câu hỏi 3C" | `docs/07-cau-hoi-phan-bien.md` | [Nhóm điền: câu nào đã luyện, trả lời ra sao] | như trên |

| Soạn kịch bản nói, câu Kahoot, sắp lại slide cho 5 người | Claude | "Làm script thuyết trình hoàn chỉnh, ghi rõ mỗi người từ slide nào đến slide nào" | `docs/06-kich-ban.md`, `docs/09-kahoot.md`, slide bản 2 | [Nhóm điền: đã đọc, sửa những gì] | như trên |
| Viết lại lời nói, rà câu chữ trên slide, đổi giao diện | Claude | "Rà lại từng câu từng chữ, script nói phải tự nhiên, tăng lên khoảng 20 phút, bỏ bộ đếm giờ, thêm số slide, đề xuất style khác" | `src/slides.part`, `docs/06-kich-ban.md`, giao diện mới | [Nhóm điền phần chỉnh sửa và kiểm chứng] | Commit 04/11/2026 |
| Đề xuất công nghệ, phong cách và làm thử hướng "Sợi chỉ xuyên suốt" | Claude | "Đưa vài mẫu, vài công nghệ để slide đẹp hơn, nhiều hoạt họa hơn, hợp nội dung"; nhóm chọn hướng A | Bản thử `soi-chi.html` (GSAP, sợi chỉ chạy qua slide, đường c/v trong mô phỏng) | [Nhóm điền: đã xem, chọn giữ hay bỏ gì] | Commit 04/11/2026 |
| Làm bản nháp B "Bản vẽ kỹ thuật động" | Claude | "Thử làm bản B, sáng tạo cả bố cục, cách trình bày, màu sắc, sơ đồ"; nhóm chọn hướng B | Bản nháp `ban-b.html`: khung bản vẽ, khung tên, nét kích thước, sơ đồ có nét nối, 3 kiểu màu mới; nội dung và số liệu giữ nguyên | [Nhóm điền: đã xem, chọn giữ hay bỏ gì] | Commit 04/11/2026 |
| Sửa khung tên và thêm hoạt ảnh cho bản B | Claude | "Phần này bị lỗi UI sao không sửa; tăng cường tiểu tiết, animation, hướng làm đẹp tiếp theo" | Sửa thanh tỉ lệ tràn khỏi khung tên; thêm nét bút quét khi chuyển slide, số câu hỏi lớn mờ phía sau, nét nối có dòng chảy, số "60–80 năm" đếm lên, thanh thời gian ở slide 4, nét đứt trong biểu đồ thác nước. Không thêm số liệu | [Nhóm điền: đã xem, giữ hay bỏ hiệu ứng nào] | Commit 04/11/2026 |
| Làm bản nháp C "Báo chí dữ liệu" | Claude | "Lưu bản này rồi làm option C. Báo chí dữ liệu: chữ lớn hiện ra theo từng cụm, biểu đồ tự chạy" | Bản nháp `ban-c.html`: giữ bố cục bản B, đổi sang kiểu mặt báo (chữ có chân Newsreader, dòng đầu trang, màu xám cho bối cảnh và một màu nhấn); tiêu đề hiện theo cụm; biểu đồ tự chạy; mục tiêu 2030 vẽ thành thanh đích. Không thêm số liệu | [Nhóm điền: đã xem, giữ hay bỏ gì] | Commit 04/11/2026 |
| Thêm đợt chi tiết 2 cho bản B | Claude | "Quay lại bố cục B, tiếp tục cải thiện, tăng cường animation và tiểu tiết, đề xuất thêm" | Ngòi bút chạy theo đầu nét đang vẽ; chấm leo bậc thang và chấm đi tắt (slide 3, 21); ngòi bút trên ba con đường (7); dấu khác tự vẽ (13); vạch chia sáng theo cung và dấu đích (18); mặt cắt gạch chéo quét; ô trống có viền chạy; tên tờ gõ ra từng chữ; đường dẫn từ con số ra ô nguồn khi bấm soi nguồn. Không thêm số liệu | [Nhóm điền: đã xem, giữ hay bỏ hiệu ứng nào] | Commit 04/11/2026 |
| Nhận xét độc lập | Codex | Yêu cầu rà soát repo | Báo cáo về nguồn, deploy, chỉ tiêu | Đã chọn lọc: nhận phần nguồn và nhãn; không giữ khảo sát | File review |
| Phản biện review Codex lần 2, cắt và sửa lời nói | Claude | "Đây là review của Codex, hãy phản biện lại rồi bắt đầu chỉnh sửa" | Danh sách điểm đồng ý, không đồng ý; sửa slide 9, 13–19, 21; lời nói từ khoảng 24 xuống khoảng 17–19 phút | [Nhóm điền: đã tự mở lại link nào; tự nói lại lời nói bằng lời của mình] | Commit 04/11/2026 |

**Quyết định do sinh viên đưa ra sau khi đọc và phản biện bản AI (04/11/2026):** bỏ khảo sát có nhập phiếu vì tốn thời gian của lớp, thay bằng hỏi một, hai bạn; yêu cầu hoạt ảnh tự chạy, giảm số lần bấm; thêm sơ đồ; sửa câu "Đi tắt nhưng vẫn phải đầu tư cho năng lực"; yêu cầu làm rõ "lợi ích" trong câu trả lời câu 2; cân thời lượng 25–30 phút gồm Kahoot.

**Góp ý của sinh viên cho bản AI (04/11/2026):** chỉ ra các từ lạ như "trên chuyền", "thoi bay"; nhận xét lời nói giống đọc lại slide, chuyển ý và chuyển người còn kém; yêu cầu viết lại cho tự nhiên.

**Ví dụ kiểm chứng đã có:**
0. Codex (04/11) dẫn số 67,1% từ một bài 700 lao động; mở bài đó không có số này, số đúng thuộc khảo sát 1.770 lao động. Codex đề xuất GDP/người Hàn Quốc 94 USD năm 1961; World Bank cho thấy năm 1960 là 159 USD, chênh do tỷ giá, nên nhóm không dùng một năm lẻ.
1. Bài bình luận trên VTV ghi kinh tế số khoảng 24% GDP năm 2025; Cục Thống kê ước tính 14,02%. Chọn Cục Thống kê.
2. Số 86%: một bài báo diễn đạt thành "lao động dệt may, da giày, điện tử bị robot thay thế đến 2050". Chọn cách ghi ở trang của ILO.
3. Tìm cụm "đi tắt đón đầu" trong Nghị quyết 57: công cụ đọc web báo không có; nằm ở giáo trình tr. 158. Nhóm nên tự tìm kiếm trong toàn văn để xác nhận.

**Tự kiểm tra Tab 6:** nhóm tự tích, không tích hộ.
