// Chụp đủ 22 slide sau khi hoạt ảnh chạy xong và tìm chỗ chữ đè lên chữ.
// Chạy: node scripts/chup-slide.js [thư mục ảnh] [kiểu màu, mặc định giay,cham]
// Cần Playwright (npm i playwright). Thoát mã 1 nếu có chỗ đè.
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const file = "file://" + path.resolve(__dirname, "..", "index.html");
const out = process.argv[2] || "anh-slide";
const looks = (process.argv[3] || "giay,cham").split(",");
const CHO = { 14: 11500 }; // slide 14 tự kéo thanh đến 100% trong khoảng 9 giây
fs.mkdirSync(out, { recursive: true });

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  const errs = [];
  p.on("pageerror", (e) => errs.push(e.message));
  const de = [];
  await p.goto(file);
  const n = await p.evaluate(() => document.querySelectorAll("section.s").length);
  for (const lk of looks) {
    for (let i = 1; i <= n; i++) {
      await p.goto(file + "#" + i);
      await p.evaluate((l) => setLook(l), lk);
      await p.reload();
      await p.waitForTimeout(CHO[i] || 7500);
      await p.screenshot({ path: `${out}/${lk}-${String(i).padStart(2, "0")}.png` });
      const r = await p.evaluate(() => {
        const S = document.querySelector(".s.on"), o = [];
        const vis = (e) => e.getClientRects().length && getComputedStyle(e).visibility != "hidden" && +getComputedStyle(e).opacity > 0;
        const tx = [...S.querySelectorAll("*")].filter((e) => [...e.childNodes].some((c) => c.nodeType == 3 && c.textContent.trim()) && vis(e) && !e.closest(".notes"));
        const R = tx.map((e) => { const g = document.createRange(); g.selectNodeContents(e); return [e, [...g.getClientRects()]]; });
        for (let a = 0; a < R.length; a++) for (let c = a + 1; c < R.length; c++) {
          const A = R[a][0], C = R[c][0];
          if (A.contains(C) || C.contains(A)) continue;
          const h = A.closest("h1,h2"); if (h && h === C.closest("h1,h2")) continue; // tiêu đề tách từng từ
          if (A.closest('[aria-hidden="true"]') || C.closest('[aria-hidden="true"]')) continue; // chữ trang trí (dấu ngoặc lớn, con dấu xoay) được phép nằm dưới chữ
          // Hộp chữ của trình duyệt cao hơn nét chữ (chừa chỗ cho dấu tiếng Việt), nên hai dòng xếp sát nhau
          // có thể chạm hộp mà chữ không chạm. Chỉ tính phần thân chữ: bỏ 22% trên và 22% dưới của mỗi hộp.
          const core = (r) => { const k = r.height * 0.22; return { left: r.left, right: r.right, top: r.top + k, bottom: r.bottom - k }; };
          let hit = null;
          for (const x0 of R[a][1]) for (const y0 of R[c][1]) {
            const x = core(x0), y = core(y0);
            const w = Math.min(x.right, y.right) - Math.max(x.left, y.left), hh = Math.min(x.bottom, y.bottom) - Math.max(x.top, y.top);
            if (w > 2 && hh > 2) hit = `${Math.round(w)}×${Math.round(hh)}px`;
          }
          if (hit) o.push(`"${A.textContent.trim().slice(0, 30)}" đè "${C.textContent.trim().slice(0, 30)}" (${hit})`);
        }
        return o;
      });
      r.forEach((x) => de.push(`${lk} slide ${i}: ${x}`));
      console.log(`${lk} ${i}: ${r.length ? r.length + " chỗ đè" : "OK"}`);
    }
  }
  await b.close();
  const rep = ["## Chụp slide và kiểm tra đè chữ", ""]
    .concat(de.length ? de.map((x) => "- ❌ " + x) : ["Không có chỗ chữ đè lên chữ."])
    .concat(errs.length ? ["", "**Lỗi JavaScript:**"].concat([...new Set(errs)].map((x) => "- ❌ " + x)) : [])
    .concat(["", `Ảnh: ${looks.length * n} tấm, tải ở mục Artifacts của lần chạy này (anh-22-slide).`]);
  console.log(rep.join("\n"));
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, rep.join("\n") + "\n");
  process.exit(de.length || errs.length ? 1 : 0);
})();
