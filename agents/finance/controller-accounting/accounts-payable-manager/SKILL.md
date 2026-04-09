---
name: accounts-payable-manager
description: >
  This skill manages the accounts payable process including invoice approval, payment
  runs, and vendor reconciliation. Use when asked to process vendor invoices, run payments,
  or reconcile AP aging. Also consider when vendor payments are overdue or approval
  workflows are breaking down. Suggest when the user is onboarding new vendors without
  an AP process.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-close-runner/SKILL.md
  - ../financial-systems-setup/SKILL.md
triggers:
  - "manage accounts payable"
  - "pay vendor invoices"
  - "AP management"
  - "process bills"
  - "accounts payable"
---

# accounts-payable-manager

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Manages the accounts payable process including invoice receipt, approval workflows, payment runs, vendor reconciliation, and 1099 compliance to ensure accurate and timely vendor payments.

## When to Use

- When vendor invoices need processing through the approval and payment workflow.
- When the payment run cycle (weekly or bi-weekly) is due and pending invoices need to be batched.
- When AP aging shows overdue balances that need investigation or vendor relationships are at risk.

## Workflow

1. **Invoice Receipt and Coding**: Receive invoices, match against purchase orders or contracts, and code to the correct GL account, department, and cost center. Flag any invoice without a PO or contract for additional approval. Deliverable: coded invoices ready for approval.
2. **Approval Routing**: Route invoices through the approval workflow based on delegation-of-authority limits. Escalate invoices above threshold and any unrecognized vendors. Track approval status and follow up on stale approvals. Deliverable: approved invoice batch.
3. **Payment Run Execution**: Batch approved invoices for payment by method (ACH, wire, check, virtual card). Optimize payment timing to capture early-payment discounts while preserving cash. Deliverable: payment run summary with cash impact.
4. **Vendor Reconciliation**: Reconcile vendor statements against AP sub-ledger monthly. Investigate and resolve discrepancies (missing invoices, duplicate payments, credit memos). Deliverable: vendor reconciliation report.
5. **AP Aging Review**: Review the AP aging report weekly. Flag invoices approaching or past due dates. Identify systematic issues (e.g., recurring late approvals from a specific department). Deliverable: AP aging summary with action items.

## Anti-Patterns

- **Paying without three-way match**: Processing payments without matching invoice to PO and receiving confirmation. *Why*: skipping the three-way match creates fraud risk and leads to paying for goods or services not received.
- **Inconsistent GL coding**: Allowing different people to code similar expenses to different accounts. *Why*: inconsistent coding makes expense analysis unreliable and creates reclassification work during close and audit.
- **Ignoring early-payment discounts**: Letting invoices with 2/10 net 30 terms pay at net 30 without evaluating the discount opportunity. *Why*: a 2% ten-day discount annualizes to 36% return on cash; ignoring it is expensive.

## Output

**On success**: Produces a payment run summary, vendor reconciliation report, and AP aging summary. Delivered weekly (payment run) and monthly (reconciliation, aging).

**On failure**: Report which invoices could not be processed (e.g., missing approval, coding unclear), what payments were completed, and what vendor follow-up is needed. Flag any compliance issues (missing W-9s, 1099 threshold vendors).

## Related Skills

- [`monthly-close-runner`](../monthly-close-runner/SKILL.md) -- AP must be current and reconciled for accurate month-end close.
- [`financial-systems-setup`](../financial-systems-setup/SKILL.md) -- Configures the AP automation tools and approval workflows.
