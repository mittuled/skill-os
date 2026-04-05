# Framework: Accounts Receivable Management

This framework defines the AR process, DSO targets, collections cadence, and aging management for a SaaS company.

## AR Metrics and Targets

| Metric | Formula | Early-Stage Target | Growth-Stage Target |
|--------|---------|-------------------|---------------------|
| Days Sales Outstanding (DSO) | (Ending AR Balance / Revenue) × Days in Period | <45 days | <30 days |
| Collection Rate | Cash Collected / Invoices Issued in Period | >95% | >98% |
| % AR Current (<30 days) | Current AR / Total AR | >80% | >90% |
| Bad Debt as % of Revenue | Write-offs / Revenue | <1% | <0.5% |

## Collections Cadence by Days Past Due

| DPD | Action | Channel | Owner | Escalation |
|-----|--------|---------|-------|------------|
| Day 0 (Invoice date) | Send invoice with payment link and due date | Email/billing portal | AR System | — |
| 7 DPD | Polite payment reminder | Email | AR System / Controller | — |
| 15 DPD | Personal follow-up; confirm invoice received and not disputed | Email + Phone | Controller | — |
| 30 DPD | Escalation to Account Manager; flag for Customer Success | Email + Phone | Account Manager | VP Sales |
| 45 DPD | Formal collection notice; suspend new orders if policy allows | Formal letter | Controller + CFO | CFO |
| 60 DPD | CFO escalation; assess creditworthiness; consider payment plan | Phone + Formal notice | CFO | Legal review |
| 90+ DPD | Legal or collection agency referral; review for write-off | Legal notice | CFO + Legal | Write-off assessment |

## Customer Segmentation for Collections

Not all customers receive the same collections treatment. Segment before acting:

| Segment | Characteristics | Collections Approach |
|---------|----------------|---------------------|
| Enterprise (net-60 terms) | >$100K ACV, contractual net-60 | Aggressive reminders only after day 60; work through CSM |
| Mid-Market (net-30 terms) | $10K-$100K ACV | Standard cadence; escalate at 30 DPD |
| SMB (credit card / annual upfront) | <$10K ACV | Auto-retry failed charges; cancel subscription at 15 DPD |
| At-risk (history of late payment) | 2+ late payments in prior 12 months | Shorten to annual upfront billing at renewal |

## AR Aging Report Structure

The AR aging report is the primary management tool. It must show:

| Column | Definition |
|--------|------------|
| Customer Name | Exact billing entity name |
| Invoice Number | Each open invoice separately |
| Invoice Date | Date issued |
| Due Date | Contractual due date |
| 0-30 DPD | Amount in current bucket |
| 31-60 DPD | Amount in 31-60 bucket |
| 61-90 DPD | Amount in 61-90 bucket |
| 91-120 DPD | Amount in 91-120 bucket |
| 120+ DPD | Amount in 120+ bucket |
| Total Outstanding | Sum of all open buckets |
| Dispute Flag | Y/N — is any amount formally disputed |
| Next Action | Specific next step and date |

## GAAP: Bad Debt Allowance (ASC 326)

Under ASC 326 (Current Expected Credit Loss), the company must estimate expected credit losses on all outstanding receivables:

```
Allowance for Credit Losses = Σ (Outstanding Balance × Probability of Default by Age Bucket)

Typical PD estimates by age:
  0-30 DPD: 0.5-1%
  31-60 DPD: 3-5%
  61-90 DPD: 10-15%
  91-120 DPD: 25-35%
  120+ DPD: 50-75%
  Disputed amounts: 40-80% (case-specific)
```

Review and update the allowance at each month-end close.

## DSO Calculation and Interpretation

```
DSO = (Ending AR Balance / Revenue) × Number of Days in Period

Example: AR Balance $500K, Monthly Revenue $400K
DSO = ($500K / $400K) × 30 = 37.5 days

Interpretation:
  <30 days: Collection ahead of billing terms
  30-45 days: Healthy for net-30 terms
  45-60 days: Review collections cadence; may indicate process issues
  >60 days: Material issue — escalate to CFO
```

## Cash Application Process

When payments are received, they must be matched within 1 business day:

1. **Automatic match**: Amount exactly matches one open invoice → auto-apply
2. **Partial payment**: Amount is less than invoice → create partial payment, flag the remainder for collections
3. **Overpayment**: Amount exceeds invoice → create credit memo, notify AR
4. **Unapplied cash**: Cannot match to any open invoice → flag as unapplied, investigate within 3 business days
5. **Customer-applied**: Payment references a specific invoice number → apply to that invoice; validate it matches
