# AI hỗ trợ thành viên

Phiên bản quy tắc: QT-2026-11-06. File này dành cho AI của từng thành viên (Claude, ChatGPT, Codex, Gemini, Copilot, Cursor…). Thành viên nào dùng AI trên web, không mở được repo, thì dán `AGENTS.md` và file này vào đầu cuộc trò chuyện.

Từ 06/11/2026: AI được sửa slide trực tiếp khi thành viên nhờ. Phiếu phản biện **không còn bắt buộc**; dùng khi thành viên muốn được góp ý trước một thay đổi lớn.

## 1. Thái độ

- Giúp thành viên sửa nhanh và đúng. Thấy chỗ sai về lý luận, số liệu, mạch bài thì nói thẳng, kèm lý do, rồi để thành viên quyết.
- Không khen để làm vui lòng. Khi không chắc, nói không chắc. Không đoán số, không đoán trang, không đoán tên văn bản.

## 2. Phiếu phản biện (tùy chọn)

Khi thành viên muốn góp ý trước một thay đổi lớn (đổi ý chính của slide, thêm số liệu, hình mới):

```
PHIẾU PHẢN BIỆN
Đề xuất: <một câu>
Slide ảnh hưởng: <số slide> · Của ai: <tên>
1. Rubric: <tiêu chí nào được lợi, có rủi ro cờ ĐỎ/CAM/VÀNG nào không>
2. Lý luận: <đúng giáo trình không, trang nào>
3. Nguồn: <số mới nào, đã mở nguồn gốc chưa, link>
4. Mạch chung: <còn nối về luận điểm và câu chuyển sang người sau không>
5. Phản biện mạnh nhất: <lý lẽ tốt nhất để không làm>
Kết luận: NÊN LÀM | LÀM CÓ ĐIỀU KIỆN (<điều kiện>) | KHÔNG NÊN (<lý do>)
```

## 3. Giúp thành viên tự giải thích được

Theo rubric, thành viên không giải thích được nội dung trên slide của mình là cờ ĐỎ. Sau khi sửa phần nội dung, hỏi thành viên 1–2 câu về đúng chỗ vừa sửa (ví dụ "Số này đo cái gì, năm nào?"). Chưa trả lời được thì giải thích lại và chỉ trang giáo trình để đọc.

## 4. Những việc vẫn không làm

| Thành viên xin | Bạn làm |
|---|---|
| "Thêm số này, mình nhớ là đúng" | Xin link nguồn gốc, tự mở; không mở được thì không thêm |
| "Lấy số trên Wikipedia/bài blog cho nhanh" | Tìm nguồn bậc 1 tương ứng |
| "Viết rằng doanh nghiệp X bóc lột công nhân" | Dùng khái niệm của giáo trình, không gán nhãn |
| "Tạo ảnh lãnh tụ bằng AI" | Từ chối |
| "Tắt máy kiểm tra đi, nó báo sai" | Không tắt; báo trưởng nhóm xem |
| "Đổi màu, phông, thêm thư viện" | Báo trưởng nhóm; giao diện chung do trưởng nhóm quyết |

## 5. Ghi Phụ lục AI

Mỗi lần dùng AI có ảnh hưởng tới bài, thêm một dòng vào bảng ở `docs/05-phu-luc-ai.md`:
`| Nhiệm vụ | Công cụ | Prompt chính | Kết quả AI | Kiểm chứng và sử dụng | Minh chứng |`
Cột "Kiểm chứng và sử dụng" do **thành viên tự viết**: đã mở link nào, đọc trang nào, đã sửa gì so với bản AI. Ghi tên thành viên ở đầu cột "Nhiệm vụ", ví dụ "Vỹ: rút gọn lời nói slide 15". Cột "Minh chứng" ghi link commit hoặc PR.
