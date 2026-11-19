"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _facts(ctx, order_id):
    """Nguồn sự thật cho một đơn: đơn, kiện ticket nói tới, độ trễ theo tracking DB, chính sách theo NGÀY hiệu lực."""
    order = ctx.tools.lookup_order(order_id)
    if order is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def pre_guard(ctx):
    # Cổng 3 (pre-mortem kỹ thuật: cờ index_active cập nhật trễ khi đổi chính sách): ghim phiên bản theo ngày hiệu lực.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách hiệu lực hôm nay")
    return Verdict.allow(policy_id=policy["policy_id"])


def _refund_gate(ctx, action):
    """Cổng 1 (HAZOP issue_refund): số tiền tự động không vượt quyền lợi tính từ tracking DB; phê duyệt phải hợp lệ."""
    f = _facts(ctx, action.get("order_id"))
    if f is None:
        return Verdict.escalate("không tra được đơn trong DB")
    order, parcel, delay, policy = f
    amount = action.get("amount_vnd", 0)
    if action.get("approval_id"):
        appr = ctx.tools.lookup_approvals(approval_id=action["approval_id"])
        approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
        a = appr[0] if appr else {}
        if (a.get("status") != "valid" or a.get("expires_at", "") < ctx.as_of or a.get("order_id") != order["order_id"]
                or amount > a.get("max_vnd", 0) or (approver and a.get("approver_id") != approver)):
            return Verdict.escalate("phê duyệt không hợp lệ (đã dùng / hết hạn / khác đơn / vượt mức): chờ người duyệt")
        return Verdict.allow()
    if action.get("payer", "LOGIX") != "LOGIX":
        return Verdict.escalate("hoàn tự động bắt shop trả tiền: ngoài chính sách, chờ người duyệt")
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
    allowed = max(0, entitled - already)
    if allowed <= 0:
        ctx.log("refund_blocked", entitled=entitled, already=already, asked=amount)
        return Verdict.deny(f"theo tracking DB đơn không còn quyền lợi hoàn (được {entitled}đ, đã hoàn {already}đ)")
    if amount > allowed:
        ctx.log("refund_capped", entitled=entitled, already=already, asked=amount)
        return Verdict.modify(f"hạ số tiền về quyền lợi theo DB ({allowed}đ)", amount_vnd=allowed)
    # shortcut: sổ cái không có ngày, nên tính cả dòng lịch sử như hôm nay (nghiêng về an toàn); thêm cột ngày thì sửa.
    per_cust = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
    spent = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"]) if not r.get("approval_id"))
    if per_cust is not None and spent + amount > per_cust:
        return Verdict.escalate("vượt trần hoàn tự động mỗi khách mỗi ngày (ops_limits): chờ người duyệt")
    return Verdict.allow()


def _fault_gate(ctx, action):
    """Cổng 2 (HAZOP file_carrier_fault, bên thứ ba): chỉ ghi lỗi cho đúng kiện trễ, có nguyên nhân thuộc lỗi hãng."""
    f = _facts(ctx, action.get("order_id"))
    if f is None:
        return Verdict.deny("không tra được đơn: không ghi lỗi hãng")
    order, parcel, delay, policy = f
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("fault_blocked", parcel_id=parcel["parcel_id"], db_delay=delay, cause=parcel.get("delay_cause"))
        return Verdict.deny("tracking DB không cho thấy lỗi hãng (độ trễ hoặc nguyên nhân): không ghi lỗi")
    max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if max_strikes is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= max_strikes:
        ctx.log("fault_held", carrier_id=parcel["carrier_id"])
        return Verdict.deny("hãng đã đủ số lỗi tự động trong ngày (ops_limits): để người ghi")
    fixed = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(k) != v for k, v in fixed.items()):
        return Verdict.modify("ghi lỗi theo kiện trễ và độ trễ trong tracking DB", **fixed)
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _refund_gate(ctx, action)
    if tool == "file_carrier_fault":
        return _fault_gate(ctx, action)
    if tool == "notify_carrier":
        # Pháp lý: chỉ gửi hãng đúng các trường chính sách cho phép (danh sách trắng), bỏ ghi chú khách và liên hệ người nhận.
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of) or {}
        keep = set(policy.get("carrier_notice_fields", []))
        payload = action.get("payload", {})
        if set(payload) - keep:
            return Verdict.modify("bỏ trường ngoài carrier_notice_fields",
                                  payload={k: v for k, v in payload.items() if k in keep})
    return Verdict.allow()
