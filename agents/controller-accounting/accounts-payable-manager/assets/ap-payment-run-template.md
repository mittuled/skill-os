# Accounts Payable Payment Run Summary

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Controller / AP Coordinator name] |
| Pay Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Payment Method(s) | [ACH / Wire / Check / Virtual Card] |
| Total Payment Amount | [$XXX,XXX] |
| Invoice Count | [N invoices] |
| Skill | accounts-payable-manager |

## Payment Run Summary

| Payment Method | Invoice Count | Total Amount | Processing Date | Expected Delivery |
|---------------|--------------|-------------|-----------------|------------------|
| ACH | [N] | [$XX,XXX] | [YYYY-MM-DD] | [YYYY-MM-DD +1 business day] |
| Wire | [N] | [$XX,XXX] | [YYYY-MM-DD] | [YYYY-MM-DD same day] |
| Check | [N] | [$XX,XXX] | [YYYY-MM-DD] | [YYYY-MM-DD +5 days] |
| Virtual Card | [N] | [$XX,XXX] | [YYYY-MM-DD] | [Immediate] |
| **Total** | **[N]** | **[$XXX,XXX]** | — | — |

## Invoice Batch

| Vendor | Invoice # | Invoice Date | Due Date | GL Account | Department | Amount | Payment Method | Early Pay Discount |
|--------|----------|-------------|---------|------------|------------|--------|---------------|-------------------|
| [Vendor A] | [INV-001] | [YYYY-MM-DD] | [YYYY-MM-DD] | [6000 - SaaS Tools] | [Engineering] | [$X,XXX] | [ACH] | [N/A] |
| [Vendor B] | [INV-002] | [YYYY-MM-DD] | [YYYY-MM-DD] | [7000 - Marketing] | [Marketing] | [$X,XXX] | [ACH] | [2% - $XX saved] |
| [Vendor C] | [INV-003] | [YYYY-MM-DD] | [YYYY-MM-DD] | [5000 - COGS] | [Engineering] | [$XX,XXX] | [Wire] | [N/A] |

## Three-Way Match Status

| Invoice | PO Match | Receiving Confirmation | Three-Way Match |
|---------|---------|----------------------|-----------------|
| [INV-001] | [Yes — PO-0045] | [Yes] | [PASS] |
| [INV-002] | [No PO — approved by [Name] per DOA] | [N/A — services] | [APPROVED — services exception] |
| [INV-003] | [Yes — PO-0046] | [Yes] | [PASS] |

## Invoices on Hold

| Vendor | Invoice # | Amount | Reason on Hold | Owner | Expected Resolution |
|--------|----------|--------|----------------|-------|-------------------|
| [Vendor D] | [INV-004] | [$X,XXX] | [Missing W-9 — vendor not set up as US taxpayer] | [AP Coordinator] | [YYYY-MM-DD] |
| [Vendor E] | [INV-005] | [$X,XXX] | [Amount exceeds PO by 15% — approval pending] | [Department Head] | [YYYY-MM-DD] |

## Early Payment Discount Summary

| Vendor | Invoice Amount | Discount Terms | Discount Amount | Pay-By Date | Decision |
|--------|--------------|---------------|----------------|-------------|---------|
| [Vendor B] | [$X,XXX] | [2/10 Net 30] | [$XX] | [YYYY-MM-DD] | [Capture] |

Annualized return on early payment discounts this run: [X% — accept/decline guidance: >15% annualized = capture]

## Cash Impact

| Item | Amount |
|------|--------|
| Opening cash balance | [$X,XXX,XXX] |
| Less: this payment run | [-$XXX,XXX] |
| Less: other disbursements pending | [-$XX,XXX] |
| Projected cash balance after run | [$X,XXX,XXX] |
| Minimum cash threshold | [$XXX,XXX] |
| Cash cushion above threshold | [$X,XXX,XXX] |

## 1099 Tracking

| Vendor | YTD Payments | 1099 Required (>$600)? | W-9 on File? | Action |
|--------|-------------|----------------------|-------------|--------|
| [Vendor F] | [$X,XXX] | [Yes] | [Yes] | [No action] |
| [Vendor G] | [$X,XXX] | [Yes] | [NO] | [Request W-9 before payment] |

## Approval

| Approver | Role | Amount Authority | Status |
|----------|------|----------------|--------|
| [Name] | [Controller] | [Up to $25K per invoice] | [Approved] |
| [Name] | [CFO] | [$25K+ per invoice] | [Approved] |
