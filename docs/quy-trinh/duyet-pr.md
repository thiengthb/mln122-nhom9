# Dành cho trưởng nhóm: bật bảo vệ `main` và duyệt PR

Phiên bản quy tắc: QT-2026-11-04.

## 1. Cài đặt GitHub (làm một lần, chỉ chủ repo làm được)

Repo đang công khai nên mọi tính năng dưới đây dùng được với tài khoản miễn phí.

**a. Mời thành viên:** Settings → Collaborators → Add people, mời 4 bạn. Họ có quyền tạo nhánh, mở PR.

**b. Luật bảo vệ `main`:** Settings → Rules → Rulesets → New ruleset → New branch ruleset.
- Ruleset name: `Bảo vệ main`. Enforcement status: **Active**.
- Bypass list → Add bypass → **Repository admin** → chọn **For pull requests only**. Nghĩa là: chính bạn cũng phải đi qua PR (không push thẳng), nhưng được merge PR của mình mà không cần người khác duyệt. GitHub không cho tác giả tự duyệt PR của mình, nên không có dòng này thì PR của bạn (và của Claude trong các phiên của bạn) sẽ kẹt.
- Target branches → Add target → **Include default branch**.
- Tích các luật:
  - **Restrict deletions**
  - **Block force pushes**
  - **Require a pull request before merging**, trong đó: Required approvals `1`; Dismiss stale pull request approvals when new commits are pushed; Require review from Code Owners; Require approval of the most recent reviewable push; Require conversation resolution before merging; Allowed merge methods: chỉ **Squash**.
  - **Require status checks to pass**, thêm hai kiểm tra `quy-tac` và `chup-slide` (chúng hiện trong danh sách sau khi máy kiểm tra chạy lần đầu trên một PR).
- Create.

**c. Gọn gàng PR:** Settings → General → Pull Requests: bỏ Allow merge commits và Allow rebase merging, giữ **Allow squash merging**; tích **Automatically delete head branches**.

**d. Quyền của máy kiểm tra:** Settings → Actions → General → Workflow permissions: **Read repository contents and packages permissions**.

Sau khi bật, thử: một thành viên push thẳng lên `main` phải bị từ chối.

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
