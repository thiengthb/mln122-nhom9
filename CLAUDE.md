# MLN122 - Nhóm 9: hướng dẫn cho Claude

@AGENTS.md

Quy tắc ở `AGENTS.md` (nạp ở trên) áp dụng cho **mọi** phiên Claude, kể cả phiên của trưởng nhóm. Trả lời bằng tiếng Việt, viết dễ hiểu. Sau `AGENTS.md`, đọc thêm: `docs/08-ra-soat-va-ke-hoach-v2.md`, `docs/HISTORY.md`.

## Bạn đang làm việc với ai

- Hỏi tên nếu chưa rõ. Trưởng nhóm là **Trần Ngọc Thiên** (GitHub `thiengthb`), người duyệt và merge mọi PR.
- Với thành viên khác: theo đúng `AGENTS.md`, phản biện, không viết hộ, chỉ sửa slide của họ.
- Với trưởng nhóm: vẫn đi qua nhánh riêng và PR (không push thẳng `main`), vẫn chạy máy kiểm tra. Trưởng nhóm được đổi phần đã khóa; khi đổi luật thì tăng phiên bản quy tắc theo `docs/quy-trinh/duyet-pr.md` mục 4.

## Bối cảnh
Môn Kinh tế chính trị Mác - Lênin (MLN122), lớp SE1919, FPT, giảng viên BinhNV26. Nhóm 9, Slot 9, chủ đề 9 (CNH, HĐH trong CMCN 4.0, AI, chuyển đổi số, nhân lực). Nhóm phản biện: 10, 4, 5. Nhóm 6 cùng lớp đạt 10/10: https://presentation-group6-mln-122.vercel.app/

## Ưu tiên của trưởng nhóm
1. Nội dung giáo trình và thực tiễn có trích dẫn. 2. Hệ thống, logic, quy chuẩn. 3. Thiết kế, chuyển động, sơ đồ.

## Cấu trúc
- Giao diện chính là "Bản vẽ kỹ thuật động" (bản B, nhóm chốt 04/11/2026). Nguồn slide: `src/deck.css.part` (nền chung), `src/ban-ve.css.part` (giao diện bản vẽ), `src/slides.part` (nội dung và ghi chú), `src/app.part` (dữ liệu nguồn, tương tác), `src/ban-ve.part` (hoạt ảnh, dùng GSAP lưu sẵn trong `vendor/`). `src/deck.html` và `index.html` là bản build: chạy `python3 scripts/build.py` rồi commit. Slide 18 vẽ mặt đồng hồ trong `src/ban-ve.part` từ mảng `G` của `app.part`. Bản C (`src/c/`, `ban-c.html`) đã gác lại; `soi-chi.html` là bản thử cũ, không build lại.
- Kiểm tra: `python3 scripts/kiem-tra.py` (quy tắc) và `node scripts/chup-slide.js <thư mục> giay,reu,cham` (chụp 22 slide, tìm chỗ đè). Trên GitHub hai việc này tự chạy cho mỗi PR.
- Đầu `src/app.part` có `CONFIG`: tên thành viên theo thứ tự nói, MSSV, ngày.
- Kịch bản `docs/06` tự sinh từ ghi chú trong `src/slides.part`.
- Câu chữ: viết như sinh viên nói chuyện, không dùng từ người nghe chưa biết; thuật ngữ của môn phải giải thích trong lời nói.

## Liên kết
- Sheet lớp: https://docs.google.com/spreadsheets/d/1EbCKDjwmWwk-oDGSOQbBcpIg0JYxn-2vS0e0khU8ucE
- Assignment: https://docs.google.com/spreadsheets/d/1hVFAJjzrrHz5ZyfjXJsZ1Y7Q0DwHswIhdqLsvmlNmBg
- Giáo trình: https://drive.google.com/file/d/1kD4-FWb8MXoen6B_DhxJTahx38bnqibN/view (PDF scan, không đưa vào repo)
Sheet cần đăng nhập, đọc bằng trình duyệt; đường dẫn `.../gviz/tq?tqx=out:html&sheet=<tên tab>` cho ra văn bản thuần.
