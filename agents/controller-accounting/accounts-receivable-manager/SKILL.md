---
name: accounts-receivable-manager
description: >
  This skill manages the accounts receivable process including invoicing, collections,
  and cash application. Use when asked to track outstanding receivables, improve collections,
  or reconcile AR aging. Also consider when DSO is increasing or cash collection is
  lagging revenue recognition. Suggest when the user is growing revenue without a
  collections process.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-close-runner/SKILL.md
  - ../../fpa-analyst/saas-metrics-reporter/SKILL.md
---

# accounts-receivable-manager

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Manages the accounts receivable process including customer invoicing, collections outreach, cash application, and AR aging analysis to maximize cash collection and minimize DSO.

## When to Use

- When customer invoices need to be generated and delivered per contract billing schedules.
- When AR aging shows receivables past due and collections outreach is needed.
- When DSO is trending upward and the company needs to accelerate cash collection.

## Workflow

1. **Invoice Generation**: Generate customer invoices per contract terms (monthly, quarterly, annual). Verify invoice accuracy against contract pricing, usage data, and any credits or adjustments. Deliverable: issued invoices with delivery confirmation.
2. **Collections Cadence**: Execute the collections cadence: reminder at 7 days past due, follow-up at 15 days, escalation to account manager at 30 days, and CFO escalation at 60 days. Deliverable: collections activity log with status.
3. **Cash Application**: Match incoming payments to outstanding invoices. Investigate and resolve unapplied cash, short payments, and overpayments. Deliverable: cash application report with cleared items.
4. **AR Aging Analysis**: Review the AR aging report weekly. Segment by customer, geography, and contract type to identify patterns. Calculate DSO and compare against target (e.g., <45 days). Deliverable: AR aging summary with DSO calculation.
5. **Bad Debt Assessment**: Review receivables older than 90 days for collectibility. Recommend write-offs or allowance adjustments per GAAP (ASC 326). Coordinate with legal on any disputed amounts. Deliverable: bad debt assessment with reserve recommendation.

## Anti-Patterns

- **Invoicing lag**: Delaying invoice generation after the billing trigger (month-end, usage threshold, milestone). *Why*: every day of invoicing delay adds a day to DSO; chronic lag compounds into a material cash flow problem.
- **Collections without segmentation**: Applying the same collections cadence to all customers regardless of size, relationship, or payment history. *Why*: enterprise customers with net-60 terms need different handling than SMBs on credit card billing; one-size-fits-all wastes effort and damages relationships.
- **Write-offs without root cause analysis**: Writing off bad debt without investigating why it became uncollectable (billing errors, disputed deliverables, customer financial distress). *Why*: write-offs without root cause analysis guarantee the same losses will recur.

## Output

**On success**: Produces issued invoices, collections activity log, cash application report, AR aging summary, and bad debt assessment. Delivered weekly (aging, collections) and monthly (full AR report).

**On failure**: Report which invoices could not be generated (e.g., missing contract data, usage data unavailable), what collection attempts were made, and what escalation is needed. Flag any customers approaching write-off threshold.

## Related Skills

- [`monthly-close-runner`](../monthly-close-runner/SKILL.md) -- AR must be reconciled for accurate revenue and cash reporting during close.
- [`saas-metrics-reporter`](../../fpa-analyst/saas-metrics-reporter/SKILL.md) -- AR data feeds into ARR and cash collection metrics.
