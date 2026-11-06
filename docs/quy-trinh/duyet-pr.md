# Dành cho trưởng nhóm: cài đặt `main` và duyệt PR

Phiên bản quy tắc: QT-2026-11-06.

## 1. Cài đặt GitHub (làm một lần, chỉ chủ repo làm được)

Repo đang công khai nên mọi tính năng dưới đây dùng được với tài khoản miễn phí.

**a. Mời thành viên:** Settings → Collaborators → Add people, mời 4 bạn. Họ có quyền tạo nhánh, mở PR.

**b. Bảo vệ `main`: đã nới từ 06/11/2026.** Thành viên được push thẳng lên `main`, không cần PR. Cách nới (chỉ chủ repo làm được):
- Settings → Rules → Rulesets → bấm ruleset `Bảo vệ main.` (link thẳng: https://github.com/thiengthb/mln122-nhom9/rules/26546650).
- **Bỏ tích** "Require a pull request before merging" và "Require status checks to pass".
- **Giữ tích** "Restrict deletions" và "Block force pushes", để không ai lỡ tay xóa `main` hay ghi đè lịch sử.
- Bấm **Save changes**.
- Settings → Branches: nếu còn "Branch protection rule" cho `main` (kiểu cũ) thì bấm **Delete**.
- Thử: một thành viên `git push` lên `main` phải đi qua.

Muốn gỡ hẳn thì trong ruleset kéo xuống cuối, bấm **Delete ruleset**. Muốn khóa lại (ví dụ trước giờ thuyết trình), tích lại "Require a pull request before merging".

**c. Gọn gàng PR:** Settings → General → Pull Requests: bỏ Allow merge commits và Allow rebase merging, giữ **Allow squash merging**; tích **Automatically delete head branches**.

**d. Quyền của máy kiểm tra:** Settings → Actions → General → Workflow permissions: **Read repository contents and packages permissions**.

## 2. Duyệt một PR

Mở PR → tab Checks và Files changed. Thứ tự đọc:

1. **Máy kiểm tra xanh.** Đỏ thì không đọc tiếp, nhờ thành viên sửa.
2. **Đúng phạm vi:** bản tóm tắt của máy kiểm tra (tab Checks → `quy-tac` → Summary) ghi PR sửa slide nào, của ai, có đụng file đã khóa không. Đụng slide người khác thì phải có "Đã hỏi ý <tên>".
3. **Phiếu phản biện** trong mô tả PR: có kết luận, có "phản biện mạnh nhất". Phiếu chỉ toàn khen là dấu hiệu AI chiều người dùng; hỏi lại.
4. **Số liệu mới:** bấm link nguồn, tìm đúng con số, đúng năm, đúng đơn vị. Kiểm tra đủ ba chỗ (docs/03, bảng `S`, `data-c`).
5. **Mạch chung:** đọc lời nói của slide trước và sau phần bị sửa trong `docs/06-kich-ban.md`. Câu chuyển còn khớp không, câu chốt còn về luận điểm không.
6. **Hình:** tải ảnh chụp ở Checks → `chup-slide` → Artifacts (`anh-22-slide`), xem slide bị sửa ở hai kiểu màu.
7. **Thời lượng:** tổng phần nói trong bản tóm tắt; quá 20 phút thì máy đã báo đỏ.
8. **Hỏi một câu** về nội dung vừa sửa trong phần bình luận. Thành viên trả lời bằng lời của mình (rubric: phải tự giải thích được).

Duyệt: Review changes → Approve → Squash and merge. Chưa được: Request changes, ghi rõ cần sửa gì.

**PR do chính bạn hoặc Claude mở:** khi ruleset còn bật "Require a pull request", GitHub không cho tác giả tự duyệt nên PR bị "blocked" dù đã xanh; đợi kiểm tra xanh, tích ô "bypass rules" rồi merge. Sau khi đã nới luật ở mục 1b thì merge bình thường.

## 3. Lịch khóa nội dung

**Buổi thuyết trình: thứ Ba 10/11/2026** (Slot 9). Lịch áp dụng:
- **Thứ Bảy 07/11/2026:** hạn chót mở và merge PR nội dung. Sau mốc này chỉ nhận PR sửa lỗi.
- **Thứ Hai 09/11/2026, trước giờ Slot 9:** nộp slide và Phụ lục AI qua email; `main` đóng đến sau buổi.
- **Thứ Tư 11/11/2026, trước giờ Slot 9:** nộp lại slide đã sửa theo góp ý của thầy, cùng quy trình PR.

Quy tắc chung (khi đổi ngày thì tính lại theo đây):

Khi có ngày thuyết trình (điền `CONFIG.ngay` trong `src/app.part`):
- **Hạn chót PR nội dung:** 72 giờ trước buổi. Sau mốc này chỉ nhận PR sửa lỗi (chính tả, số sai, đè chữ).
- **24 giờ trước buổi:** nộp slide và Phụ lục AI qua email theo `docs/00`. Sau mốc này `main` đóng, không merge gì cho đến sau buổi.
- **24 giờ sau buổi:** mở lại để sửa theo góp ý của thầy, cùng quy trình PR.

## 4. Khi cần đổi luật

Sửa file trong `docs/quy-trinh/`, `AGENTS.md`, `scripts/kiem-tra.py` qua PR như mọi thay đổi khác. Nếu đổi nội dung luật, tăng phiên bản (ví dụ `QT-2026-11-10`) ở **tất cả** các chỗ ghi phiên bản (`grep -rn "QT-2026" .`), kể cả hằng số `PHIEN_BAN` trong `scripts/kiem-tra.py`. PR mở sau đó phải ghi phiên bản mới, tức là AI của thành viên phải đọc lại luật.
