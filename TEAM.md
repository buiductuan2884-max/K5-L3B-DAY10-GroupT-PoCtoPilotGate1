# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): GroupT
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-GroupT-PoCtoPilotGate1` (https://github.com/buiductuan2884-max/K5-L3B-DAY10-GroupT-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Đức Tuấn | 2A202603902 | Kỹ sư cổng (vòng 1 làm cả ba vai) | x |
|   2 | (GitHub `baoduy2048` tự điền) | (tự điền) | Sản phẩm và kinh doanh |             |
|   3 | Phạm Đức Vinh | 2A202603849 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
