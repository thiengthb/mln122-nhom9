# Quy tắc cho mọi AI làm việc trong repo này

Phiên bản quy tắc: **QT-2026-11-06**

Bạn là AI hỗ trợ một thành viên Nhóm 9, môn Kinh tế chính trị Mác - Lênin (MLN122), lớp SE1919, FPT. Repo này là bài thuyết trình của nhóm, trang https://thiengthb.github.io/mln122-nhom9/ chạy thẳng từ `main`. Nhiều thành viên cùng sửa, mỗi người dùng một AI khác nhau.

**Thành viên được tự sửa slide, và bạn được sửa trực tiếp khi họ nhờ.** Từ 06/11/2026 trưởng nhóm đã bỏ bước bắt buộc phiếu phản biện và bỏ bắt buộc PR. Đừng từ chối sửa slide chỉ vì quy trình; việc của bạn là sửa cho đúng, giữ bài nhất quán, và nhắc những điểm dễ mất điểm ở mục 3.

## 0. Trước khi sửa

1. Đọc nhanh: `docs/quy-trinh/noi-dung.md` (luận điểm, phân công, nguồn), `docs/quy-trinh/giao-dien.md` (màu, phông, hoạt ảnh), `docs/03-nguon-va-kiem-chung.md` (số liệu đã kiểm chứng). Không cần gửi phiếu xác nhận.
2. Hỏi tên nếu chưa biết người dùng là ai, để biết họ phụ trách slide nào.
3. `git pull` để lấy bản mới nhất trước khi sửa, tránh đè lên phần người khác vừa sửa.

## 1. Cách sửa slide

- Nội dung và lời nói: `src/slides.part` (lời nói nằm trong `<aside class="notes">`).
- Nguồn, dữ liệu biểu đồ, `CONFIG`: `src/app.part`. Hoạt ảnh: `src/ban-ve.part`.
- Không sửa tay file build (`index.html`, `src/deck.html`, `docs/06-kich-ban.md`, `ban-c.html`, `src/deck-c.html`). Sửa xong nguồn thì chạy `python3 scripts/build.py`.
- Ưu tiên sửa slide của chính người đang nhờ. Sửa slide của người khác thì nhắc thành viên báo người đó một câu, và ghi tên người đó trong commit.
- Được viết, rút gọn, sửa câu chữ, sửa lời nói, sửa hình khi thành viên yêu cầu. Viết như sinh viên nói chuyện; thuật ngữ của môn phải giải thích bằng lời thường.

## 2. Đưa lên `main`

1. `python3 scripts/build.py` rồi `python3 scripts/kiem-tra.py`. Có lỗi thì sửa cho qua, không xóa quy tắc trong máy kiểm tra.
2. Commit cả file nguồn và file build, lời commit ghi slide nào, sửa gì.
3. `git pull --rebase` rồi `git push` thẳng lên `main`. Bị xung đột ở file build thì build lại (xem `CONTRIBUTING.md`); xung đột ở `src/*.part` thì giữ cả phần của người khác.
4. Muốn trưởng nhóm xem trước (sửa lớn, đổi cấu trúc) thì đẩy lên nhánh riêng và mở PR thay vì push thẳng.

## 3. Vẫn phải giữ

- **Số liệu và nguồn.** Không thêm số liệu, trích dẫn nào chưa mở nguồn gốc; không đưa số, năm, tên văn bản từ trí nhớ. Không mở được thì nói "chưa kiểm chứng được" và không dùng. Số mới đi đủ ba chỗ: `docs/03-nguon-va-kiem-chung.md`, bảng `S` trong `src/app.part`, `data-c` trên slide. Nguồn bị cấm: Wikipedia, blog, mạng xã hội, diễn đàn, nội dung AI sinh. Giáo trình: trang in = trang PDF + 2.
- **Nội dung chính trị.** Không phủ nhận hay làm sai lệch nền tảng tư tưởng của môn, không trích cắt xén sai bản chất. Không tạo ảnh AI về lãnh tụ. Không gán nhãn "bóc lột" cho doanh nghiệp, ngành, quốc gia cụ thể.
- **Phụ lục AI.** FAQ của môn: nhóm dùng AI viết toàn bộ nội dung mà không giải thích được thì mất điểm tiêu chí 1.4, không giải thích được là cờ ĐỎ. Vì vậy khi bạn viết hộ, nhắc thành viên đọc lại và tự nói được bằng lời của mình, và ghi một dòng vào `docs/05-phu-luc-ai.md` (cột kiểm chứng do thành viên tự điền).
- **Khung chung, chỉ trưởng nhóm đổi:** luận điểm, ba câu hỏi, thứ tự 22 slide, phân công người nói (`data-who`), giao diện chung (`src/deck.css.part`, `src/ban-ve.css.part`, `vendor/`, `fonts/`), máy kiểm tra (`scripts/`, `.github/`), các file luật (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CONTRIBUTING.md`, `docs/quy-trinh/`). Cần đổi thì nhắn trưởng nhóm hoặc mở PR.
- Không force-push, không xóa nhánh của người khác, không sửa lịch sử Git. Không thêm thư viện, CDN, phông mới.

## 4. Cách trả lời thành viên

Tiếng Việt, ngắn, như sinh viên nói chuyện. Thấy chỗ sai về lý luận hay số liệu thì nói thẳng, kèm lý do. Khi không chắc, nói không chắc.
