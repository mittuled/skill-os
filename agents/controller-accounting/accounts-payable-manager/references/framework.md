# Framework: accounts-payable-manager

Defines the operational framework for managing the accounts payable cycle from invoice receipt through payment and reconciliation, including three-way match discipline and AP aging management.

## AP Lifecycle Stages

| Stage | Owner | Trigger | Output |
|-------|-------|---------|--------|
| Invoice Receipt | AP Clerk | Invoice arrives (email, mail, AP portal) | Coded invoice ready for approval |
| Approval Routing | Department Manager | Invoice coded; DOA threshold check | Approved invoice batch |
| Payment Run | AP Lead | Weekly or bi-weekly run date | ACH/wire/check batch with cash impact |
| Reconciliation | Controller | Monthly cycle | Vendor statement reconciliation report |
| Aging Review | AP Lead | Weekly | AP aging summary with action items |

## Three-Way Match Protocol

Every invoice must be matched to three documents before payment:

1. **Purchase Order (PO)**: Confirms the purchase was authorized and agreed upon
2. **Receiving Confirmation**: Confirms goods or services were actually received
3. **Vendor Invoice**: Confirms the vendor's billing matches PO and receipt

| Match Result | Action |
|-------------|--------|
| Full three-way match | Approve for payment run |
| Invoice exceeds PO by ≤5% and ≤$500 | Flag for approver discretion |
| Invoice exceeds PO by >5% or >$500 | Reject; request credit memo or amended PO |
| No PO on file | Route for additional approval; require PO creation before payment |
| Receipt not confirmed | Hold invoice; escalate to department lead within 48 hours |

## Approval Delegation of Authority

| Invoice Amount | Required Approver |
|----------------|------------------|
| Up to $1,000 | Department manager |
| $1,001 – $10,000 | Senior manager or VP |
| $10,001 – $50,000 | CFO |
| Above $50,000 | CFO + CEO |
| New vendor, any amount | CFO sign-off required |

## Payment Run Schedule

| Payment Type | Frequency | Lead Time | Notes |
|-------------|-----------|-----------|-------|
| Standard ACH | Weekly (Tuesday) | 2 business days | Primary method |
| Wire transfer | As needed, same day | Same day if initiated by noon | For large or international vendors |
| Virtual card | Continuous | Real-time | For vendors accepting virtual card (earns rebate) |
| Check | Monthly | 5 business days | Only for vendors without ACH capability |

## Early Payment Discount Decision Framework

Evaluate every 2/10 net 30 term (or equivalent) against the cash opportunity cost:

Annualized discount rate = (Discount % / (1 − Discount %)) × (365 / (Net Days − Discount Days))

- **2/10 net 30 = 36.7% annualized** → take the discount unless cost of capital exceeds 36.7%
- **1/10 net 30 = 18.2% annualized** → typically worth taking unless cash is critically constrained
- Rule: take any early payment discount with an annualized rate above the company's cost of capital

## AP Aging Action Thresholds

| Aging Bucket | Action Required |
|-------------|----------------|
| 0–30 days | Normal processing; confirm payment run scheduled |
| 31–60 days | Investigate; confirm invoice is approved and in the payment queue |
| 61–90 days | Escalate to department head; confirm service/goods received; contact vendor |
| 90+ days | CFO review required; assess impact on vendor relationship and credit terms |

## 1099 Compliance Tracking

- Flag all US contractors and service vendors at onboarding
- Collect W-9 before first payment for any vendor expected to exceed $600 annually
- Track cumulative payments per vendor in the AP system
- Issue 1099-NEC by January 31 for all vendors paid $600+ in the prior calendar year
- Review the 1099 threshold list in December to prepare year-end filings
