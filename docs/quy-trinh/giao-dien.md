# Quy tắc giao diện, công nghệ và UI/UX

Phiên bản quy tắc: QT-2026-11-04. Giao diện "Bản vẽ kỹ thuật động" đã được nhóm chốt ngày 04/11/2026. Mọi thay đổi phải trông như cùng một người vẽ cả 22 tờ.

## 1. Công nghệ: được dùng gì

| Thành phần | Dùng | Không dùng |
|---|---|---|
| Khung | Một file HTML, ghép từ `src/*.part` bằng `python3 scripts/build.py` | reveal.js, Slidev, Canva, PowerPoint, framework JS, bước build mới |
| Hoạt ảnh | GSAP lưu sẵn trong `vendor/gsap/` (gsap, DrawSVGPlugin, SplitText), CSS animation | Thư viện khác, CDN, Lottie, video nhúng, GIF |
| Hình | SVG vẽ bằng nét, biểu tượng nét 24×24 có sẵn (mục 6c trong `src/ban-ve.part`), canvas đã có | Ảnh chụp, ảnh stock, ảnh AI, emoji, bộ icon ngoài |
| Phông | Bricolage Grotesque (tiêu đề), Be Vietnam Pro (chữ thường), IBM Plex Mono (nhãn, số kỹ thuật), Newsreader (trích dẫn) trong `fonts/` | Phông khác, Google Fonts qua mạng |
| Mạng | Không cần mạng khi trình chiếu | Bất cứ tài nguyên nào tải từ Internet |

Muốn thêm công nghệ: đề xuất trong PR, nêu vì sao cái có sẵn không làm được.

## 2. File nào để làm gì

- `src/slides.part`: nội dung 22 slide và ghi chú lời nói. Thành viên sửa chủ yếu ở đây, **trong slide của mình**.
- `src/app.part`: `CONFIG` (tên, ngày), bảng nguồn `S`, dữ liệu biểu đồ, tương tác. Thêm nguồn ở bảng `S`.
- `src/ban-ve.part`: hoạt ảnh từng slide. Mỗi cảnh là một hàm gọi từ `enter(i)`.
- `src/ban-ve.css.part`, `src/deck.css.part`: màu, phông, bố cục chung. **Đã khóa.** CSS riêng cho một hình mới thì viết thêm ở cuối `ban-ve.css.part`, trước `</style>`, và chỉ chọn trong slide đó.
- `index.html`, `src/deck.html`, `docs/06-kich-ban.md`, `ban-c.html`, `src/deck-c.html`: file build, không sửa tay.
- `src/c/`, `ban-c.html`, `soi-chi.html`: bản cũ đã gác lại, không sửa.

## 3. Màu

- **Chỉ dùng biến CSS**, không viết mã màu (`#…`, `rgb(…)`, tên màu) ngoài các khối `:root`. Máy kiểm tra sẽ báo lỗi.
- Ba kiểu màu (phím D): `giay` giấy can sáng (mặc định), `reu` bản in xanh, `cham` bàn vẽ đêm. Hình mới phải đọc rõ ở cả ba.
- Nghĩa của màu, giữ đúng trên mọi slide:
  - `--son` (xanh cobalt ở kiểu mặc định): **công nghệ**, máy móc, dữ liệu.
  - `--nghe` (cam): **năng lực, con người**. Trong tiêu đề dùng `<em class="nl">`.
  - `--si` (xanh ngọc): nét bút giảng bài, ý phụ, cơ hội.
  - `--vai`, `--vai-2`, `--vai-3`: chữ chính, chữ phụ, nhãn mờ.
  - `--cham`, `--cham-2`, `--cham-3`: nền, mặt khối, đường lưới.
- Chữ trên nền màu dùng `--on-son`, `--on-nghe`, `--on-si`, `--on-vai`.

## 4. Bố cục và chữ

- Sân khấu 1600×900. Mỗi slide một hình chính. Ngoài tiêu đề, chữ trên slide khoảng 25 từ trở xuống; phần còn lại thuộc về lời nói.
- Tiêu đề là một câu khẳng định hoặc câu hỏi, không phải nhãn chủ đề.
- Dòng nhãn nhỏ trên tiêu đề (`.eb`) theo mẫu `CÂU HỎI n · <ý của slide>`.
- Chữ nhỏ nhất 15px ở cỡ 1600 (nhãn mono có thể 12–14px nếu chỉ là chú thích phụ).
- Dòng "Nguồn:" ở chân trái, góc phải dưới chỉ có tên người nói và số tờ. Không thêm khung viền ngoài, không làm to góc tờ.
- Sợi chỉ tiến độ chạy hết đáy slide; không đặt gì đè lên nó.
- Không chữ nào được đè lên chữ khác hay hình khác, ở mọi thời điểm của hoạt ảnh. Máy kiểm tra chụp 22 slide và báo chỗ đè.

## 5. Hoạt ảnh và tương tác

- **Slide tự chạy như video.** Người nói chỉ bấm mũi tên (hoặc bút trình chiếu) để sang nhịp. Không làm hình phải bấm, rê chuột, đoán rồi lật, câu đố trên slide.
- Hoạt ảnh phải nói đúng điều lời nói đang nói; không có chuyển động chỉ để trang trí.
- Mọi tween, timeline phải đưa vào mảng `live` để bị dừng khi chuyển slide. Tôn trọng `motion` (người xem chọn giảm chuyển động thì hiện ngay trạng thái cuối).
- Cảnh trên một slide xong trong khoảng 12 giây.
- Đã thử và **bị loại**, không làm lại: lật trang 3D, máy quay phóng gần (zoom) cả slide, các tương tác bấm để hiện.
- Hình ví von (bánh răng, con thoi, cầu thang…) không được mang số liệu mới. Số trên hình phải là số đã có nguồn.

## 6. Phím đã dùng

Mũi tên, Space: chuyển nhịp. N: ghi chú. P: cửa sổ người nói. K: soi nguồn. F: toàn màn hình. T: bấm đồng hồ. D: đổi kiểu màu. Không gán phím mới khi chưa hỏi trưởng nhóm.

## 7. Kiểm tra trước khi mở PR

1. `python3 scripts/build.py` và `python3 scripts/kiem-tra.py` qua hết.
2. Mở `index.html` trong trình duyệt, xem slide của mình ở cả ba kiểu màu (phím D), đợi hoạt ảnh chạy hết.
3. Trên GitHub, máy kiểm tra chụp lại 22 slide và đính kèm vào PR (mục Artifacts của lần chạy). Trưởng nhóm sẽ xem ảnh này khi duyệt.
