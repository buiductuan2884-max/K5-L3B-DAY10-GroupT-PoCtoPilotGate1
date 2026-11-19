# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): GroupT
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-GroupT-PoCtoPilotGate1` (https://github.com/buiductuan2884-max/K5-L3B-DAY10-GroupT-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): S2

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Đức Tuấn | 2A202603902 | Kỹ sư cổng (vòng 1 làm cả ba vai) | x |
|   2 | Nguyễn Bảo Duy | 2A202603890 | Sản phẩm và kinh doanh |             |
|   3 | Phạm Đức Vinh | 2A202603849 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## BuiDucTuan-2A202603902

### Phần việc phụ trách

Trưởng nhóm, vai **Kỹ sư cổng**. Vòng 1 làm bản đầu của cả ba vai: Phiếu A (A1–A5, ký tiêu chí), Phiếu B (B0–B8, quyết định v1),
`lab10/guards.py`, `config/operating_gates.json`, chốt cổng vòng 1. Vòng 2: `lab10/guards.py`, `lab10/monitors.py`, Phiếu C
mục C0, C1, C2, C7 dòng [1]–[2], C8; gộp bài của hai bạn, soát và hoàn thiện C12, nộp bài.

### Đóng góp cụ thể

- Ký tiêu chí trước lần chạy đầu tiên (ký 09:15:39, chạy base 09:15:50), dựng 3 cổng vòng 1: tiền theo tracking DB và phê duyệt
  hợp lệ, lỗi hãng theo DB, ghim chính sách theo ngày hiệu lực; thêm danh sách trắng cho `notify_carrier`.
- Vòng 2 (thẻ S2): đổi cổng tiền từ "bên trả ≠ LOGIX thì chuyển người" sang "sửa bên trả về LOGIX, số tiền về quyền lợi theo DB",
  thêm luật vượt `auto_limit_vnd` mà không có phê duyệt thì chờ NV-HANH. Chi phí S2 từ 8.027đ xuống 5.273đ/ticket, ROI
  0,25 → 0,9, hoàn sai và trừ shop vẫn 0.
- Thêm 2 monitor `injected_directive_rate`, `non_logix_payer_rate` (bộ nền 0, S2 0,4667 / 0,4).
- Gộp nhánh của Vinh và Duy; soát C12 với `decision_rule` đã ký, cả bàn chốt giữ Thu hẹp vì kho "?" vẫn đắt hơn làm tay.

### Bằng chứng

Commit `fed7d1c` (ký tiêu chí), `65d20ab` (vòng 1), `b85207b` (code vòng 2), `4dc1652` (Phiếu C phần Kỹ sư cổng). Lần chạy
`R-base-before-20261119-091550-bde05c`, `R-base-prepared-20261119-091801-87645a`, `R-S2-after-20261119-163934-a2e13d`,
`R-S2-grade-20261119-163942-a2e13d` (PASS-VISIBLE). Phiếu C mục C2, C7, C8, C12.

### Exit ticket

Học được: cùng chặn được tác hại, nhưng chuyển người mọi ca nghi ngờ đẩy chi phí S2 lên 8.027đ/ticket, còn sửa lệnh ghi
theo tracking DB thì vẫn an toàn mà chỉ tốn 5.273đ. Chưa chắc: trần theo khách lách được bằng nhiều mã khách, và bộ thử ẩn
có thể có kiểu lệnh cài mà cổng chưa gặp.

## PhamDucVinh-2A202603849

### Phần việc phụ trách

Vai **Vận hành và pháp lý**. Câu 2.4 (Phiếu B mục B4 phần ngoài kỹ thuật, B5), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm),
câu 3.1 phần riêng theo thẻ (Phiếu C mục C3), câu 3.3 (C5), nhánh con người/vận hành của fault tree (C6, C9), câu 3.7
(C10 risk register, C11 checklist và runbook 4–5), `config/operating_gates.json` mục `operations` và `legal` ở vòng 2,
`submission/submission.json`.

### Đóng góp cụ thể

- Soát phần vận hành và pháp lý vòng 1 (bản demo của trưởng nhóm) với `data/world.json` (`staff`, `ops_limits`, `ops_facts`,
  `staff_behavior`) và Bản tiêu chí đã ký; sửa chỗ runbook lệch config: mốc gọi người trực thứ hai (60 phút / > 6 ca, khớp
  `operations.stop_conditions`), thêm điều kiện dừng 2.000.000đ đã ký vào Runbook 3, hạ ngưỡng vàng chi phí xuống dưới
  7.000đ đã ký, chuẩn hoá trạng thái checklist B5 (Xong / Chưa), tính thêm tải kiểm mẫu 10% vào giờ cao điểm.
- Viết trước Risk register (C10) từ các dòng "Chưa" của checklist B5 và Runbook 5 (ba kịch bản tuần đầu pilot).
- Vòng 2: (điền sau khi bốc thẻ) phần riêng theo thẻ, giả định môi trường, runbook 4, cổng `operations`/`legal` nếu có sửa.

### Bằng chứng

Phiếu B mục B5, B7.5, B7.6; Phiếu C mục C10, C11. Mã commit và mã lần chạy: (điền sau khi push và chạy lệnh 6).

### Exit ticket

(Tự viết cuối buổi: một điều học được, một điều còn chưa chắc.)
