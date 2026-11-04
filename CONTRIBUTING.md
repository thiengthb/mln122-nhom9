# Cách đóng góp vào bài thuyết trình Nhóm 9

Phiên bản quy tắc: QT-2026-11-04. Trưởng nhóm, người duyệt và merge: **Trần Ngọc Thiên** (`thiengthb`).

**Thuyết trình thứ Ba 10/11/2026. Hạn chót PR nội dung: thứ Bảy 07/11/2026**, sau đó chỉ nhận PR sửa lỗi.

`main` là bản thuyết trình thật: trang https://thiengthb.github.io/mln122-nhom9/ chạy thẳng từ `main`. Vì vậy **không ai push thẳng lên `main`**. Mọi thay đổi đi qua nhánh riêng và Pull Request (PR), trưởng nhóm duyệt rồi mới vào.

## Lần đầu (làm một lần)

1. Nhận lời mời cộng tác trong email GitHub, bấm Accept.
2. Cài Git và Python 3. Clone repo:
   ```
   git clone https://github.com/thiengthb/mln122-nhom9.git
   cd mln122-nhom9
   ```
3. Đọc lần lượt: `AGENTS.md`, `docs/quy-trinh/noi-dung.md`, `docs/quy-trinh/giao-dien.md`, `docs/quy-trinh/ai-phan-bien.md`.
4. Nếu dùng AI:
   - Claude Code, Codex, Cursor, Copilot, Gemini CLI mở trong thư mục repo sẽ tự đọc `AGENTS.md` (hoặc `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, đều trỏ về `AGENTS.md`). Câu đầu tiên vẫn nên là: *"Đọc AGENTS.md và các file nó yêu cầu, rồi gửi phiếu xác nhận."*
   - ChatGPT, Gemini, Claude trên web không đọc được repo: dán nội dung `AGENTS.md` và `docs/quy-trinh/ai-phan-bien.md` vào đầu cuộc trò chuyện.
   - AI chưa gửi phiếu xác nhận (mẫu ở `AGENTS.md` mục 0) thì chưa làm gì cả.

## Mỗi lần sửa

1. **Lấy bản mới nhất và tạo nhánh riêng:**
   ```
   git switch main
   git pull
   git switch -c <ten>/<viec>
   ```
   Tên nhánh: tên gọi không dấu, gạch chéo, việc ngắn. Ví dụ `vy/slide-15-loi-noi`, `nghia/slide-19-nguon-luat-ai`.
2. **Một nhánh một việc.** Sửa lời nói và thêm số liệu là hai việc thì nên hai PR. PR nhỏ duyệt nhanh, ít xung đột.
3. **Sửa đúng chỗ:** nội dung và lời nói ở `src/slides.part` (chỉ slide của mình), nguồn ở `src/app.part` và `docs/03`. Không sửa file build bằng tay.
4. **Build và tự kiểm tra:**
   ```
   python3 scripts/build.py
   python3 scripts/kiem-tra.py
   ```
   Mở `index.html` bằng trình duyệt, xem slide của mình ở cả ba kiểu màu (phím D).
5. **Ghi Phụ lục AI** vào `docs/05-phu-luc-ai.md` nếu có dùng AI (tự viết cột kiểm chứng).
6. **Commit cả file nguồn và file build, rồi push nhánh:**
   ```
   git add -A
   git commit -m "Slide 15: rút gọn lời nói, thêm câu chuyển sang slide 16"
   git push -u origin <ten>/<viec>
   ```
7. **Mở PR** vào `main` trên GitHub. Điền đủ mẫu, ghi phiên bản quy tắc `QT-2026-11-04` (máy kiểm tra sẽ báo lỗi nếu thiếu).
8. **Đợi máy kiểm tra** (dấu tích xanh). Đỏ thì bấm vào xem lỗi, sửa trên cùng nhánh, push lại.
9. **Trưởng nhóm duyệt.** Có góp ý thì sửa trên cùng nhánh, push lại, trả lời góp ý. Trưởng nhóm bấm merge; thành viên không tự merge.

## Khi bị xung đột (conflict)

Vì file build (`index.html`, `src/deck.html`, `docs/06-kich-ban.md`…) thay đổi mỗi lần build, hai PR cùng mở thường xung đột ở các file này. Cách gỡ:
```
git switch <nhanh-cua-ban>
git fetch origin
git merge origin/main
# Nếu chỉ xung đột ở file build: lấy bản nào cũng được, rồi build lại
git checkout --theirs index.html src/deck.html docs/06-kich-ban.md ban-c.html src/deck-c.html
python3 scripts/build.py
git add -A
git commit
git push
```
Nếu xung đột ở `src/slides.part`, `src/app.part` hay `docs/…`: mở file, giữ cả phần của mình lẫn phần người khác, hỏi người kia nếu không chắc. Không xóa phần của người khác cho xong.

## Những điều không được làm

- Push lên `main`, force-push, xóa nhánh người khác.
- Sửa slide người khác khi họ chưa đồng ý.
- Sửa các file đã khóa: `src/deck.css.part`, `src/ban-ve.css.part`, `scripts/`, `vendor/`, `fonts/`, `.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CONTRIBUTING.md`, `docs/quy-trinh/`. Muốn đổi thì đề xuất trong PR hoặc issue.
- Thêm số liệu chưa mở nguồn gốc. Dùng nguồn bị cấm.
- Để AI viết hộ toàn bộ lời nói.

## Trưởng nhóm duyệt theo gì

Xem `docs/quy-trinh/duyet-pr.md`. Tóm lại: máy kiểm tra xanh; phiếu phản biện có trong PR; nguồn mở được và đúng số; slide vẫn nằm trong mạch chung; ảnh chụp 22 slide không có chỗ đè; người sửa tự giải thích được.
