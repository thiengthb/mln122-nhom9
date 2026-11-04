#!/usr/bin/env python3
"""Ghép các phần trong src/ thành src/deck.html và index.html.

src/deck.html: bản không có khung trang, để đăng làm Artifact.
index.html: bản đầy đủ, để GitHub Pages và Vercel phục vụ.
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "src"
parts = [(src / n).read_text(encoding="utf8") for n in ("deck.css.part", "slides.part", "app.part")]
body = "\n".join(parts)
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
RATE = 170  # tiếng mỗi phút
out = [
    "# Kịch bản thuyết trình 5 người\n\n"
    "Tự sinh từ ghi chú trong `src/slides.part`; sửa ở đó rồi chạy `python3 scripts/build.py`. "
    "Thời lượng ước tính theo tốc độ 170 tiếng mỗi phút, chưa tính nhịp dừng, nên phải bấm giờ khi tập.\n\n"
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
    words = sum(len(n.split()) for _, _, n in spoken)
    mins = words / RATE
    total += mins
    a, b = spoken[0][0], spoken[-1][0]
    table.append(f"| Người {w} | {a}–{b} | {spoken[0][1]} đến {spoken[-1][1]} | {mins:.1f} phút |\n")
    parts.append(f"\n## Người {w}: slide {a}–{b} (khoảng {mins:.1f} phút)\n")
    for i, title, n in spoken:
        parts.append(f"\n### Slide {i}. {title}\n\n{n}\n")
table.append(f"| **Tổng phần nói** | | | **{total:.1f} phút** |\n")
out += table + parts
out.append("\n## Slide dự phòng\n\nSlide 22 (Tài liệu tham khảo) không đọc, chỉ mở khi được hỏi. Phụ lục AI là file riêng, nộp qua email.\n")
(root / "docs" / "06-kich-ban.md").write_text("".join(out), encoding="utf8")
print("Kịch bản: %.1f phút" % total)

# Bản thử hướng "Sợi chỉ xuyên suốt": thêm GSAP (lưu sẵn trong vendor/, chạy được khi không có mạng) và src/soi-chi.part.
vend = "".join(
    "<script>\n" + (root / "vendor" / "gsap" / n).read_text(encoding="utf8") + "\n</script>\n"
    for n in ("gsap.min.js", "DrawSVGPlugin.min.js", "SplitText.min.js")
)
demo = body + "\n" + vend + (src / "soi-chi.part").read_text(encoding="utf8")
(src / "deck-soi-chi.html").write_text(demo, encoding="utf8")
(root / "soi-chi.html").write_text(page.replace(body, demo), encoding="utf8")
print("OK soi-chi", len(demo))

# Bản nháp B "Bản vẽ kỹ thuật động": bố cục riêng ở src/b/, lời nói lấy từ src/slides.part theo tên slide.
notes = dict(re.findall(r'data-title="([^"]+)".*?<aside class="notes">(.*?)</aside>', src_slides, re.S))
b_slides = (src / "b" / "slides.part").read_text(encoding="utf8")
def fill(m):
    return m.group(1) + notes.get(m.group(2), "") + m.group(3)
b_slides = re.sub(r'(<section[^>]*data-title="([^"]+)".*?<aside class="notes">)(</aside>)', fill, b_slides, flags=re.S)
b_body = "\n".join([(src / "deck.css.part").read_text(encoding="utf8"), (src / "b" / "b.css.part").read_text(encoding="utf8"), b_slides, (src / "app.part").read_text(encoding="utf8"), vend, (src / "b" / "b.part").read_text(encoding="utf8")])
(src / "deck-b.html").write_text(b_body, encoding="utf8")
(root / "ban-b.html").write_text(page.replace(body, b_body), encoding="utf8")
print("OK ban-b", len(b_body), "ghi chú:", len(re.findall(r'<aside class="notes">[^<]', b_slides)))

# Bản nháp C "Báo chí dữ liệu": dùng lại bố cục bản B (src/c/slides.part chép từ src/b/slides.part), giao diện và hoạt ảnh riêng ở src/c/.
c_slides = re.sub(r'(<section[^>]*data-title="([^"]+)".*?<aside class="notes">)(</aside>)', fill, (src / "c" / "slides.part").read_text(encoding="utf8"), flags=re.S)
c_body = "\n".join([(src / "deck.css.part").read_text(encoding="utf8"), (src / "b" / "b.css.part").read_text(encoding="utf8"), (src / "c" / "c.css.part").read_text(encoding="utf8"), c_slides, (src / "app.part").read_text(encoding="utf8"), vend, (src / "c" / "c.part").read_text(encoding="utf8")])
(src / "deck-c.html").write_text(c_body, encoding="utf8")
(root / "ban-c.html").write_text(page.replace(body, c_body), encoding="utf8")
print("OK ban-c", len(c_body), "ghi chú:", len(re.findall(r'<aside class="notes">[^<]', c_slides)))
