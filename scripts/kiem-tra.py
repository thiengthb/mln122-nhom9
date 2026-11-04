#!/usr/bin/env python3
"""Máy kiểm tra quy tắc của Nhóm 9. Chạy: python3 scripts/kiem-tra.py

Kiểm tra những quy tắc đo được bằng máy (xem docs/quy-trinh/). Các quy tắc về ý nghĩa
(lý luận, mạch chung, phản biện) do trưởng nhóm duyệt trên PR.

Tùy chọn cho máy kiểm tra trên GitHub:
  --base <ref>          so với nhánh gốc để báo slide nào bị sửa, file khóa nào bị đụng
  --pr-body <file>      kiểm tra mô tả PR có ghi phiên bản quy tắc

Thoát với mã 1 nếu có lỗi. Cảnh báo không làm hỏng kiểm tra.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

PHIEN_BAN = "QT-2026-11-04"

# Phân công đã khóa: data-who của slide 1..22 (1 Huy, 2 Thiên, 3 Phương, 4 Vỹ, 5 Nghĩa)
PHAN_CONG = [1] * 5 + [2] * 4 + [3] * 4 + [4] * 3 + [5] * 6
SO_SLIDE = len(PHAN_CONG)
TOI_DA_PHUT = 20.0

TEN_MIEN_CAM = [
    "wikipedia.org", "wikiwand.com", "facebook.com", "fb.com", "tiktok.com", "youtube.com", "youtu.be",
    "instagram.com", "twitter.com", "x.com", "threads.net", "reddit.com", "quora.com", "medium.com",
    "blogspot.com", "wordpress.com", "substack.com", "voz.vn", "tinhte.vn", "chatgpt.com", "chat.openai.com",
    "gemini.google.com", "claude.ai", "perplexity.ai", "studocu.com", "123doc.net", "luanvan.co",
]

FILE_KHOA = [
    "src/deck.css.part", "src/ban-ve.css.part", "scripts/", "vendor/", "fonts/", ".github/",
    "AGENTS.md", "CLAUDE.md", "GEMINI.md", "CONTRIBUTING.md", "docs/quy-trinh/",
]
FILE_BUILD = ["index.html", "src/deck.html", "docs/06-kich-ban.md", "ban-c.html", "src/deck-c.html"]

ROOT = Path(os.environ.get("N9_ROOT") or Path(__file__).resolve().parent.parent).resolve()
loi, canh_bao, tom_tat = [], [], []


def doc(p):
    return (ROOT / p).read_text(encoding="utf8")


def cac_slide(text):
    """Trả về danh sách (thuộc tính, nội dung) của từng <section class="s ...">."""
    return re.findall(r'<section([^>]*class="s[ "][^>]*)>(.*?)</section>', text, re.S)


def thuoc_tinh(attrs, ten):
    m = re.search(ten + r'="([^"]*)"', attrs)
    return m.group(1) if m else None


def ten_mien_cam(url):
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in TEN_MIEN_CAM)


# 1. File build phải khớp với nguồn ---------------------------------------------------------
def kiem_build():
    truoc = {f: (ROOT / f).read_bytes() if (ROOT / f).exists() else b"" for f in FILE_BUILD}
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py")], cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        loi.append("build.py chạy lỗi:\n" + r.stderr[-1500:])
        return
    lech = [f for f in FILE_BUILD if (ROOT / f).exists() and (ROOT / f).read_bytes() != truoc[f]]
    if lech:
        loi.append("Chưa build lại sau khi sửa (hoặc sửa tay file build): " + ", ".join(lech)
                   + ". Chạy `python3 scripts/build.py` rồi commit cả các file này.")


# 2. Cấu trúc slide, phân công, ghi chú ------------------------------------------------------
def kiem_slide(slides_text):
    ss = cac_slide(slides_text)
    if len(ss) != SO_SLIDE:
        loi.append(f"Có {len(ss)} slide, phải là {SO_SLIDE}. Thêm, bớt slide là việc của trưởng nhóm.")
    who = []
    for i, (a, body) in enumerate(ss, 1):
        w, act, title = thuoc_tinh(a, "data-who"), thuoc_tinh(a, "data-act"), thuoc_tinh(a, "data-title")
        if not (w and act is not None and title):
            loi.append(f"Slide {i}: thiếu data-who, data-act hoặc data-title.")
        who.append(int(w) if w and w.isdigit() else 0)
        note = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
        if not note or len(re.sub(r"<[^>]+>|\s", "", note.group(1))) < 40:
            loi.append(f"Slide {i} ({title}): thiếu ghi chú lời nói hoặc quá ngắn.")
    if len(ss) == SO_SLIDE and who != PHAN_CONG:
        sai = [f"slide {i+1}: {w} (đúng là {p})" for i, (w, p) in enumerate(zip(who, PHAN_CONG)) if w != p]
        loi.append("Phân công người nói (data-who) bị đổi: " + "; ".join(sai) + ". Đổi phân công là việc của trưởng nhóm.")
    if re.search(r"\[Người \d\]", slides_text):
        loi.append("Còn chỗ giữ chỗ [Người N] trong ghi chú; thay bằng tên người nói.")
    return ss


# 3. Nguồn: mọi khóa dùng trên slide phải có trong bảng S, không dùng nguồn bị cấm --------------
def bang_nguon(app):
    a = app.index("const S = {")
    b = app.index("\n};", a)
    khoi = app[a:b]
    S = {}
    for m in re.finditer(r'^\s{2}(\w+):\{(.*)\},?\s*$', khoi, re.M):
        S[m.group(1)] = m.group(2)
    da_xoa = set(re.findall(r"delete S\.(\w+)", app))
    return S, da_xoa


def kiem_nguon(slides_text, app):
    S, da_xoa = bang_nguon(app)
    for k, v in S.items():
        for f in ("short", "kind", "url", "apa"):
            if not re.search(f + r":", v):
                loi.append(f"Nguồn `{k}` thiếu trường `{f}` trong bảng S (src/app.part).")
        m = re.search(r'url:"([^"]+)"', v)
        if m and not m.group(1).startswith("https://"):
            loi.append(f"Nguồn `{k}`: link phải bắt đầu bằng https://")
        if m and ten_mien_cam(m.group(1)):
            loi.append(f"Nguồn `{k}` dùng trang bị cấm: {m.group(1)}")
    dung = set(re.findall(r'data-c="([^"]+)"', slides_text))
    for refs in re.findall(r'data-refs="([^"]+)"', slides_text):
        dung |= {x.split("|")[0].strip() for x in refs.split(";") if x.strip()}
    for k in sorted(dung):
        if k not in S or k in da_xoa:
            loi.append(f"Slide dùng nguồn `{k}` nhưng bảng S (src/app.part) không có. Thêm nguồn theo docs/quy-trinh/noi-dung.md mục 4.")
    # link bị cấm ở bất cứ đâu trong nội dung và bảng nguồn
    for f in ["src/slides.part", "src/app.part", "docs/03-nguon-va-kiem-chung.md"]:
        for u in re.findall(r'https?://[^\s"\'<>)\]|]+', doc(f)):
            if ten_mien_cam(u):
                loi.append(f"{f}: link tới trang bị cấm làm nguồn: {u}")


# 4. Màu chỉ lấy từ biến CSS; không tải gì từ Internet ----------------------------------------
MAU = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?)\(")


def bo_root(t):
    return re.sub(r":root(?:\[[^\]]*\])?(?::not\([^)]*\))?\s*\{[^}]*\}", lambda m: "\n" * m.group(0).count("\n"), t)


def kiem_mau():
    for f in ["src/deck.css.part", "src/ban-ve.css.part", "src/slides.part", "src/app.part", "src/ban-ve.part"]:
        t = bo_root(doc(f))
        # bỏ thực thể HTML &#...; và mã màu trắng/đen trong mặt nạ SVG (mặt nạ bắt buộc dùng trắng/đen)
        for n, line in enumerate(t.split("\n"), 1):
            line2 = re.sub(r"&#x?[0-9a-fA-F]+;", "", line)
            line2 = re.sub(r'(stroke|fill):"#(fff|000)"', "", line2)
            for m in MAU.finditer(line2):
                s = m.group(0)
                if s.startswith("#") and len(s) - 1 not in (3, 4, 6, 8):
                    continue
                loi.append(f"{f}:{n}: mã màu viết cứng `{s}`. Dùng biến CSS (var(--son), var(--nghe)…), xem giao-dien.md mục 3.")


def kiem_mang():
    for f in ["src/deck.css.part", "src/ban-ve.css.part", "src/slides.part", "src/app.part", "src/ban-ve.part"]:
        t = doc(f)
        for pat, ten in [(r"<script[^>]+src=\"https?:", "script tải từ mạng"),
                         (r"<link[^>]+href=\"https?:", "stylesheet tải từ mạng"),
                         (r"@import", "@import"),
                         (r"url\(\s*['\"]?https?:", "url() tải từ mạng"),
                         (r"<img[^>]+src=\"https?:", "ảnh tải từ mạng"),
                         (r"<iframe", "iframe")]:
            if re.search(pat, t):
                loi.append(f"{f}: có {ten}. Slide phải chạy không cần mạng, xem giao-dien.md mục 1.")


# 5. Thời lượng phần nói ---------------------------------------------------------------------
def kiem_thoi_luong():
    m = re.search(r"\*\*Tổng phần nói\*\*.*?\*\*([\d.]+) phút\*\*", doc("docs/06-kich-ban.md"))
    if not m:
        canh_bao.append("Không đọc được tổng thời lượng trong docs/06-kich-ban.md.")
        return
    phut = float(m.group(1))
    tom_tat.append(f"Tổng phần nói ước tính: **{phut} phút** (giới hạn {TOI_DA_PHUT}).")
    if phut > TOI_DA_PHUT:
        loi.append(f"Kịch bản ước tính {phut} phút, quá {TOI_DA_PHUT} phút của rubric. Bớt lời nói trước khi thêm.")
    for row in re.findall(r"^\| (Người \d[^|]*) \| ([\d–]+) \|[^|]*\| ([\d.]+) phút \|", doc("docs/06-kich-ban.md"), re.M):
        tom_tat.append(f"- {row[0]}, slide {row[1]}: {row[2]} phút")


# 6. Lời lẽ cần cẩn thận ---------------------------------------------------------------------
def kiem_loi_le(slides_text):
    for i, (a, body) in enumerate(cac_slide(slides_text), 1):
        if re.search(r"bóc lột", body, re.I):
            canh_bao.append(f"Slide {i} có chữ \"bóc lột\". Chỉ dùng như khái niệm giáo trình, không gán cho doanh nghiệp hay ngành cụ thể.")


# 7. So với nhánh gốc: slide nào bị sửa, file khóa nào bị đụng --------------------------------
def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


def so_voi_base(base, slides_text):
    ten = re.findall(r'"([^"]+)"', re.search(r"thanhVien:\s*\[([^\]]*)\]", doc("src/app.part")).group(1))
    doi = [f for f in git("diff", "--name-only", f"{base}...HEAD").split("\n") if f]
    if not doi:
        return
    cu = git("show", f"{base}:src/slides.part")
    a, b = cac_slide(cu), cac_slide(slides_text)
    sua = [i + 1 for i in range(max(len(a), len(b))) if i >= len(a) or i >= len(b) or a[i] != b[i]]
    tom_tat.append("")
    tom_tat.append("**File thay đổi:** " + ", ".join(f"`{f}`" for f in doi))
    if sua:
        chu = sorted({PHAN_CONG[i - 1] for i in sua if i <= SO_SLIDE})
        tom_tat.append("**Slide bị sửa:** " + ", ".join(map(str, sua)) + " · thuộc phần của: "
                       + ", ".join(ten[c - 1] if c - 1 < len(ten) else f"Người {c}" for c in chu))
        if len(chu) > 1:
            canh_bao.append("PR sửa slide của nhiều người. Mô tả PR phải ghi \"Đã hỏi ý <tên>\" cho từng người.")
    khoa = [f for f in doi if any(f == k or f.startswith(k) for k in FILE_KHOA)]
    if khoa:
        canh_bao.append("PR đụng file đã khóa: " + ", ".join(khoa) + ". Chỉ trưởng nhóm được đổi; người duyệt xem kỹ.")
    if any(f.startswith("src/") and f.endswith(".part") for f in doi) and "docs/05-phu-luc-ai.md" not in doi:
        canh_bao.append("PR sửa nội dung slide nhưng không thêm dòng nào vào docs/05-phu-luc-ai.md. Nếu có dùng AI thì phải ghi.")
    if "src/app.part" in doi:
        S_cu, _ = bang_nguon(git("show", f"{base}:src/app.part"))
        S_moi, _ = bang_nguon(doc("src/app.part"))
        moi = [k for k in S_moi if k not in S_cu]
        doi_nguon = [k for k in S_moi if k in S_cu and S_moi[k] != S_cu[k]]
        if moi or doi_nguon:
            tom_tat.append("**Nguồn mới:** " + (", ".join(moi) or "không") + " · **Nguồn bị sửa:** " + (", ".join(doi_nguon) or "không"))
            if moi and "docs/03-nguon-va-kiem-chung.md" not in doi:
                loi.append("Thêm nguồn mới (" + ", ".join(moi) + ") nhưng không ghi vào docs/03-nguon-va-kiem-chung.md.")


def kiem_pr(body_file):
    body = Path(body_file).read_text(encoding="utf8") if body_file and Path(body_file).exists() else ""
    if PHIEN_BAN not in body:
        loi.append(f"Mô tả PR chưa ghi phiên bản quy tắc `{PHIEN_BAN}`. Nghĩa là AI và người sửa chưa đọc bản quy tắc hiện hành (AGENTS.md).")
    if "Kết luận" not in body:
        canh_bao.append("Mô tả PR chưa có tóm tắt phiếu phản biện (dòng \"Kết luận\").")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--pr-body")
    ap.add_argument("--bo-build", action="store_true", help="không chạy lại build (dùng khi đã kiểm build ở bước khác)")
    o = ap.parse_args()

    if not o.bo_build:
        kiem_build()
    slides_text, app = doc("src/slides.part"), doc("src/app.part")
    kiem_slide(slides_text)
    kiem_nguon(slides_text, app)
    kiem_mau()
    kiem_mang()
    kiem_thoi_luong()
    kiem_loi_le(slides_text)
    if o.base:
        so_voi_base(o.base, slides_text)
    if o.pr_body is not None:
        kiem_pr(o.pr_body)

    out = [f"## Kiểm tra quy tắc {PHIEN_BAN}", ""]
    out += [f"**{len(loi)} lỗi, {len(canh_bao)} cảnh báo**", ""]
    out += [f"- ❌ {x}" for x in loi] + [f"- ⚠️ {x}" for x in canh_bao]
    out += [""] + tom_tat
    text = "\n".join(out)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf8") as f:
            f.write(text + "\n")
    sys.exit(1 if loi else 0)


if __name__ == "__main__":
    main()
