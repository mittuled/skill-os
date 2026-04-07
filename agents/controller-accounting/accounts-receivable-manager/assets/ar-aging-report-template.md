# AR Aging Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Controller / AR Coordinator name] |
| Report As Of | [YYYY-MM-DD] |
| Total AR Balance | [$XXX,XXX] |
| DSO | [N days] |
| DSO Target | [<45 days] |
| Skill | accounts-receivable-manager |

## DSO Calculation

| Metric | Value |
|--------|-------|
| Total AR balance | [$XXX,XXX] |
| Revenue (trailing 90 days) | [$X,XXX,XXX] |
| Average daily revenue (90-day) | [$X,XXX/day] |
| DSO | [AR ÷ Daily Revenue] = [N days] |
| Prior month DSO | [N days] |
| DSO trend | [Improving / Stable / DETERIORATING — +N days MoM] |

## AR Aging Summary

| Aging Bucket | Amount | % of Total AR | Invoice Count |
|-------------|--------|--------------|--------------|
| Current (not yet due) | [$XXX,XXX] | [X%] | [N] |
| 1-30 days past due | [$XX,XXX] | [X%] | [N] |
| 31-60 days past due | [$XX,XXX] | [X%] | [N] |
| 61-90 days past due | [$X,XXX] | [X%] | [N] |
| 91-120 days past due | [$X,XXX] | [X%] | [N] |
| 120+ days past due | [$X,XXX] | [X%] | [N] |
| **Total** | **[$XXX,XXX]** | **100%** | **[N]** |

## Customer-Level Aging Detail

| Customer | Total Balance | Current | 1-30 DPD | 31-60 DPD | 61-90 DPD | 90+ DPD | Collections Status |
|----------|--------------|---------|----------|-----------|-----------|---------|-------------------|
| [Customer A] | [$XX,XXX] | [$XX,XXX] | — | — | — | — | [Current] |
| [Customer B] | [$X,XXX] | — | [$X,XXX] | — | — | — | [Reminder sent YYYY-MM-DD] |
| [Customer C] | [$X,XXX] | — | — | [$X,XXX] | — | — | [Follow-up sent YYYY-MM-DD] |
| [Customer D] | [$X,XXX] | — | — | — | [$X,XXX] | — | [Escalated to AM YYYY-MM-DD] |
| [Customer E] | [$X,XXX] | — | — | — | — | [$X,XXX] | [CFO escalation — dispute pending] |

## Collections Activity Log

| Customer | Invoice # | Amount | Action | Date | Outcome |
|----------|----------|--------|--------|------|---------|
| [Customer B] | [INV-0234] | [$X,XXX] | [7-day reminder email sent] | [YYYY-MM-DD] | [Awaiting response] |
| [Customer C] | [INV-0198] | [$X,XXX] | [15-day follow-up — spoke to AP contact] | [YYYY-MM-DD] | [Payment promised by YYYY-MM-DD] |
| [Customer D] | [INV-0167] | [$X,XXX] | [30-day escalation to Account Manager] | [YYYY-MM-DD] | [AM engaged — account at risk flag raised] |

## Disputed Invoices

| Customer | Invoice # | Amount | Dispute Reason | Internal Owner | Status | Expected Resolution |
|----------|----------|--------|----------------|---------------|--------|-------------------|
| [Customer E] | [INV-0145] | [$X,XXX] | [Disputed delivery of milestone 3] | [Account Manager Name] | [Under review] | [YYYY-MM-DD] |

## Cash Application Summary

| Period | Payments Received | Invoices Cleared | Unapplied Cash | Short Payments | Overpayments |
|--------|-----------------|----------------|---------------|----------------|-------------|
| [This week] | [$XX,XXX] | [N invoices] | [$X,XXX] | [$X,XXX] | [$X,XXX] |

**Unapplied cash action**: [Description of unapplied amounts and resolution plan]

## Bad Debt Assessment

| Customer | Balance | Aging | Collectibility | Recommended Action |
|----------|---------|-------|---------------|-------------------|
| [Customer F] | [$X,XXX] | [120+ days] | [Unlikely — customer unresponsive] | [Write-off recommendation — see allowance note] |

Allowance for doubtful accounts (current): [$X,XXX]
Recommended adjustment: [+/- $X,XXX to [$X,XXX]]

## Action Items

| Action | Owner | Due Date | Priority |
|--------|-------|----------|---------|
| [Send 7-day reminder to Customer B — INV-0234] | [AR Coordinator] | [YYYY-MM-DD] | [Medium] |
| [Escalate Customer D to CFO — 90+ DPD] | [Controller] | [YYYY-MM-DD] | [High] |
| [Obtain W-9 from Customer G before credit approval] | [AR Coordinator] | [YYYY-MM-DD] | [Medium] |
| [Write-off Customer F — $X,XXX — pending CFO approval] | [Controller] | [YYYY-MM-DD] | [High] |
