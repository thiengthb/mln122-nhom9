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
