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

## NguyenBaoDuy-2A202603890

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**. Phiếu A: câu 1.1–1.6 (mục tiêu, thước đo và tiêu chí chấp nhận); Phiếu B: câu 2.3 (B3, bản đồ dữ liệu/drift) và câu 2.9 (B7.4, cổng kinh doanh); `config/acceptance_criteria.json`, mục `business` trong `config/operating_gates.json`; Phiếu C: C5 (specification và giả định môi trường), C7 (lý do kinh doanh cho phương án sửa) và C12 (quyết định Gate 1 v2).

### Đóng góp cụ thể

- Xác định mục tiêu kinh doanh đi cùng ngưỡng an toàn: hoàn sai, lỗi hãng oan và lộ dữ liệu tối đa 0; `pass_rate` tối thiểu 0,97, `pass_k` tối thiểu 0,9; chi phí tối đa 7.000đ/ticket, ROI tối thiểu 0,3 và không có ca ùn. Đặt `escalation_rate` tối đa 0,25 là ngưỡng mong muốn.
- Ghi lý do cho các cổng kinh doanh: trần hoàn tự động 1.500.000đ/ngày (trong ngân sách Finance 2.000.000đ), chi phí LLM tối đa 1.500đ/ticket, ROI tối thiểu 0,3; giữ phạm vi `all` ở lần đo để có số so sánh theo kho trước khi quyết định phạm vi pilot.
- Đối chiếu kết quả S2 trước và sau sửa. Mốc prepared còn chi phí 8.027đ/ticket và ROI 0,25 do 8/15 ca chuyển người; mốc after giảm còn 5.273đ/ticket, ROI 0,9 và 3 ca cần người. Cùng kết quả bộ nền không regression, dùng các bằng chứng này để ghi quyết định v2 **Tiếp tục** theo tiêu chí đã ký; nêu rõ cần xác nhận lại số kinh doanh trong pilot thật vì dữ liệu lab là mock.

### Bằng chứng

Phiếu A mục A1–A5; Phiếu B mục B3, B7.4, B8; Phiếu C mục C5, C7, C12; `config/acceptance_criteria.json` và `config/operating_gates.json` mục `business`. Mã lần chạy: `R-S2-prepared-20261119-163834-87645a`, `R-S2-after-20261119-163934-a2e13d`, `R-S2-grade-20261119-163942-a2e13d`, `R-base-after-20261119-163935-a2e13d`. (Bổ sung mã commit cá nhân nếu có.)

### Exit ticket

Điều học được: cổng an toàn phải cân bằng với chi phí vận hành; chuyển nhiều ca sang người có thể làm chi phí vượt ngưỡng dù tác hại đã được chặn. Điều còn chưa chắc: các con số chi phí, ROI và tải người duyệt trong dữ liệu mock có phản ánh pilot thật hay không; cần đo lại theo kho và trong giờ cao điểm.

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
