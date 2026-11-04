#!/usr/bin/env python3
"""Ghép các phần trong src/ thành src/deck.html và index.html.

Giao diện chính là "Bản vẽ kỹ thuật động" (trước gọi là bản B): deck.css.part là nền chung,
ban-ve.css.part là giao diện, slides.part là nội dung kèm ghi chú, app.part là dữ liệu và tương tác,
GSAP lưu sẵn trong vendor/, ban-ve.part là hoạt ảnh.

src/deck.html: bản không có khung trang, để đăng làm Artifact.
index.html: bản đầy đủ, để GitHub Pages và Vercel phục vụ.
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "src"
vend = "".join(
    "<script>\n" + (root / "vendor" / "gsap" / n).read_text(encoding="utf8") + "\n</script>\n"
    for n in ("gsap.min.js", "DrawSVGPlugin.min.js", "SplitText.min.js")
)
rd = lambda n: (src / n).read_text(encoding="utf8")
body = "\n".join([rd("deck.css.part"), rd("ban-ve.css.part"), rd("slides.part"), rd("app.part"), vend, rd("ban-ve.part")])
(src / "deck.html").write_text(body, encoding="utf8")
page = (
    '<!doctype html>\n<html lang="vi"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<meta name="description" content="Thuyết trình MLN122, Nhóm 9: Công nghiệp hóa, hiện đại hóa ở Việt Nam trong Cách mạng công nghiệp lần thứ tư.">'
    "</head><body>\n" + body + "\n</body></html>\n"
)
(root / "index.html").write_text(page, encoding="utf8")
print("OK", len(body))

# Sinh kịch bản nói từ ghi chú trong slide, để slide và lời nói luôn khớp nhau.
import re

src_slides = (src / "slides.part").read_text(encoding="utf8")
items = re.findall(
    r'<section[^>]*data-who="(\d)"[^>]*data-title="([^"]+)".*?<aside class="notes">(.*?)</aside>',
    src_slides,
    re.S,
)
RATE = 150  # âm tiết mỗi phút: tốc độ nói chậm, có dừng; 170 là tốc độ nói nhanh
CUE = re.compile(r"\[(?!Người)[^\]]*\]")  # bỏ chỉ dẫn trong ngoặc vuông khi đếm, giữ [Người N]
out = [
    "# Kịch bản thuyết trình 5 người\n\n"
    "Tự sinh từ ghi chú trong `src/slides.part`; sửa ở đó rồi chạy `python3 scripts/build.py`. "
    "Thời lượng ước tính theo tốc độ 150 âm tiết mỗi phút (nói chậm, có dừng), không đếm chỉ dẫn trong ngoặc vuông; ở 170 âm tiết mỗi phút thì nhân với 0,88. Phải bấm giờ khi tập.\n\n"
    "Phím: mũi tên phải hoặc bút trình chiếu. `[Bấm một lần.]` là nhịp bấm trong cùng slide. "
    "Hết mỗi đoạn thì bấm sang slide sau.\n"
]
who = {}
for i, (w, title, note) in enumerate(items, 1):
    who.setdefault(w, []).append((i, title, note.strip()))
total = 0
table = ["\n| Người | Slide | Nội dung | Ước tính |\n|---|---|---|---|\n"]
parts = []
for w, rows in sorted(who.items()):
    spoken = [r for r in rows if r[1] != "Tài liệu tham khảo"]
    words = sum(len(CUE.sub("", n).split()) for _, _, n in spoken)
    mins = words / RATE
    total += mins
    a, b = spoken[0][0], spoken[-1][0]
    table.append(f"| Người {w} | {a}–{b} | {spoken[0][1]} đến {spoken[-1][1]} | {mins:.1f} phút |\n")
    parts.append(f"\n## Người {w}: slide {a}–{b} (khoảng {mins:.1f} phút)\n")
    for i, title, n in spoken:
        parts.append(f"\n### Slide {i}. {title}\n\n{n}\n")
table.append(f"| **Tổng phần nói** | | | **{total:.1f} phút** (nói nhanh 170: {total*150/170:.1f} phút) |\n")
out += table + parts
out.append("\n## Slide dự phòng\n\nSlide 22 (Tài liệu tham khảo) không đọc, chỉ mở khi được hỏi. Phụ lục AI là file riêng, nộp qua email.\n")
(root / "docs" / "06-kich-ban.md").write_text("".join(out), encoding="utf8")
print("Kịch bản: %.1f phút" % total)

# Các bản thử cũ: soi-chi.html (hướng "Sợi chỉ xuyên suốt") giữ nguyên file đã sinh, không build lại.
# ban-b.html chỉ còn chuyển hướng sang index.html vì bản B đã thành bản chính (04/11/2026).
(root / "ban-b.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=./"><title>Chuyển sang slide chính</title><a href="./">Slide chính</a>\n', encoding="utf8")
(src / "deck-b.html").unlink(missing_ok=True)

notes = dict(re.findall(r'data-title="([^"]+)".*?<aside class="notes">(.*?)</aside>', src_slides, re.S))
def fill(m):
    return m.group(1) + notes.get(m.group(2), "") + m.group(3)

# Bản nháp C "Báo chí dữ liệu" (đã gác lại): dùng lại bố cục bản chính (src/c/slides.part là bản chép), giao diện và hoạt ảnh riêng ở src/c/.
c_slides = re.sub(r'(<section[^>]*data-title="([^"]+)".*?<aside class="notes">)(</aside>)', fill, (src / "c" / "slides.part").read_text(encoding="utf8"), flags=re.S)
c_body = "\n".join([(src / "deck.css.part").read_text(encoding="utf8"), (src / "ban-ve.css.part").read_text(encoding="utf8"), (src / "c" / "c.css.part").read_text(encoding="utf8"), c_slides, (src / "app.part").read_text(encoding="utf8"), vend, (src / "c" / "c.part").read_text(encoding="utf8")])
(src / "deck-c.html").write_text(c_body, encoding="utf8")
(root / "ban-c.html").write_text(page.replace(body, c_body), encoding="utf8")
print("OK ban-c", len(c_body), "ghi chú:", len(re.findall(r'<aside class="notes">[^<]', c_slides)))
