# Cách đóng góp vào bài thuyết trình Nhóm 9

Phiên bản quy tắc: QT-2026-11-06. Trưởng nhóm: **Trần Ngọc Thiên** (`thiengthb`).

**Thuyết trình thứ Ba 10/11/2026.**

`main` là bản thuyết trình thật: trang https://thiengthb.github.io/mln122-nhom9/ chạy thẳng từ `main`. Từ 06/11/2026 thành viên **được push thẳng lên `main`** để sửa slide cho nhanh. Vì vậy trước khi push phải build và chạy máy kiểm tra, để không làm hỏng bản đang chạy.

## Lần đầu (làm một lần)

1. Nhận lời mời cộng tác trong email GitHub, bấm Accept.
2. Cài Git và Python 3. Clone repo:
   ```
   git clone https://github.com/thiengthb/mln122-nhom9.git
   cd mln122-nhom9
   ```
3. Đọc `AGENTS.md` và `docs/quy-trinh/noi-dung.md` (luận điểm, phân công, nguồn).
4. Nếu dùng AI:
   - Claude Code, Codex, Cursor, Copilot, Gemini CLI mở trong thư mục repo sẽ tự đọc `AGENTS.md` (hoặc `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, đều trỏ về `AGENTS.md`).
   - ChatGPT, Gemini, Claude trên web không đọc được repo: dán nội dung `AGENTS.md` và `docs/quy-trinh/ai-phan-bien.md` vào đầu cuộc trò chuyện.

## Mỗi lần sửa

1. **Lấy bản mới nhất:**
   ```
   git switch main
   git pull
   ```
2. **Sửa đúng chỗ:** nội dung và lời nói ở `src/slides.part`, nguồn ở `src/app.part` và `docs/03`. Không sửa file build bằng tay. Sửa slide của người khác thì báo người đó một câu.
3. **Build và tự kiểm tra:**
   ```
   python3 scripts/build.py
   python3 scripts/kiem-tra.py
   ```
   Mở `index.html` bằng trình duyệt, xem slide vừa sửa ở cả ba kiểu màu (phím D).
4. **Ghi Phụ lục AI** vào `docs/05-phu-luc-ai.md` nếu có dùng AI (tự viết cột kiểm chứng).
5. **Commit cả file nguồn và file build, rồi push:**
   ```
   git add -A
   git commit -m "Slide 15: rút gọn lời nói, thêm câu chuyển sang slide 16"
   git pull --rebase
   git push
   ```
6. **Xem máy kiểm tra trên GitHub** (tab Actions). Đỏ thì sửa ngay và push lại, vì trang thuyết trình đang chạy từ `main`.

Sửa lớn hoặc muốn trưởng nhóm xem trước: tạo nhánh riêng (`git switch -c <ten>/<viec>`), push nhánh đó và mở PR vào `main`.

## Khi bị xung đột (conflict)

Vì file build (`index.html`, `src/deck.html`, `docs/06-kich-ban.md`…) thay đổi mỗi lần build, hai người cùng sửa thường xung đột ở các file này. Cách gỡ:
```
git pull --rebase
# Nếu chỉ xung đột ở file build: lấy bản nào cũng được, rồi build lại
git checkout --theirs index.html src/deck.html docs/06-kich-ban.md ban-c.html src/deck-c.html
python3 scripts/build.py
git add -A
git rebase --continue
git push
```
Nếu xung đột ở `src/slides.part`, `src/app.part` hay `docs/…`: mở file, giữ cả phần của mình lẫn phần người khác, hỏi người kia nếu không chắc. Không xóa phần của người khác cho xong.

## Những điều không được làm

- Force-push, xóa nhánh người khác, sửa lịch sử Git.
- Push khi `python3 scripts/kiem-tra.py` còn báo lỗi.
- Sửa khung chung (luận điểm, ba câu hỏi, thứ tự slide, phân công, giao diện chung, `scripts/`, `.github/`, file luật). Muốn đổi thì nhắn trưởng nhóm.
- Thêm số liệu chưa mở nguồn gốc. Dùng nguồn bị cấm.
- Để AI viết hộ mà mình không tự giải thích được.
