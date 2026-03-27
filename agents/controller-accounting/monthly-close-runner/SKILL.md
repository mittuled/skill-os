---
name: monthly-close-runner
description: >
  This skill runs the monthly financial close process including reconciliations, accruals,
  and financial statement preparation. Use when asked to close the books, prepare month-end
  financials, or run the close checklist. Also consider when the close deadline is
  approaching and reconciliations are incomplete. Suggest when the user needs financial
  statements but the books have not been closed.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: complex
related-skills:
  - ../accounts-payable-manager/SKILL.md
  - ../accounts-receivable-manager/SKILL.md
---

# monthly-close-runner

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Runs the monthly financial close process including GL reconciliations, accruals, revenue recognition, and financial statement preparation to produce GAAP-compliant financials on a consistent timeline.

## When to Use

- When the calendar month ends and the close process needs to begin per the close calendar.
- When interim financial statements are needed for a board meeting, investor request, or audit.
- When the close process needs to be established or improved for a company that has been operating without a structured close.

## Workflow

1. **Pre-Close Preparation**: Confirm all sub-ledgers are current (AP, AR, payroll, bank feeds). Send close reminders to department leads for expense submissions and accrual inputs. Review the close checklist for any new items. Deliverable: pre-close readiness confirmation.
2. **Revenue Recognition**: Apply ASC 606 five-step model to all revenue transactions. Recognize subscription revenue ratably, professional services on delivery, and usage revenue based on consumption. Reconcile deferred revenue schedule. Deliverable: revenue recognition workpaper with ASC 606 documentation.
3. **Expense Accruals**: Record accruals for incurred but unpaid expenses (payroll, benefits, vendors with delayed invoicing, SaaS tools billed in arrears). Reverse prior-month accruals and record new ones. Deliverable: accrual journal entries with supporting documentation.
4. **Bank and Account Reconciliations**: Reconcile all bank accounts, credit cards, and intercompany accounts. Investigate and clear all reconciling items older than 30 days. Deliverable: reconciliation workpapers with cleared items.
5. **Financial Statement Preparation**: Prepare the income statement, balance sheet, and cash flow statement. Run a trial balance and verify that debits equal credits, balance sheet balances, and cash flow reconciles to bank. Deliverable: draft financial statements with trial balance.
6. **Analytical Review**: Perform flux analysis comparing current month to prior month and budget. Investigate any variance greater than 10% or $25K. Document explanations for all material movements. Deliverable: flux analysis with explanations.
7. **Close Certification**: Certify that all close tasks are complete, all reconciling items are resolved, and the financials are ready for review. Lock the period in the GL. Deliverable: close certification with locked period confirmation.

## Anti-Patterns

- **Perpetually late close**: Allowing the close to extend beyond the target (typically day 10-15 for startups) without a remediation plan. *Why*: a late close delays variance analysis, forecast updates, and board reporting, creating a cascading bottleneck across finance.
- **Skipping reconciliations for speed**: Closing the books without completing all account reconciliations to meet a deadline. *Why*: unreconciled accounts accumulate errors that compound over time and create audit findings.
- **Manual revenue recognition**: Applying ASC 606 through manual journal entries without a documented methodology or systematic process. *Why*: manual rev rec is the single highest audit risk for SaaS companies; inconsistent application creates material misstatement risk.
- **No close checklist**: Running the close from memory without a standardized, version-controlled checklist. *Why*: checklists ensure completeness and enable delegation; without them, close quality depends entirely on individual knowledge.

## Output

**On success**: Produces GAAP-compliant financial statements (income statement, balance sheet, cash flow), reconciliation workpapers, accrual documentation, and close certification. Delivered within the target close timeline.

**On failure**: Report which close tasks are incomplete, what preliminary financials are available, and the expected completion timeline. Flag any reconciling items or data quality issues that may affect financial statement accuracy.

## Related Skills

- [`accounts-payable-manager`](../accounts-payable-manager/SKILL.md) -- AP must be current for accurate expense recording during close.
- [`accounts-receivable-manager`](../accounts-receivable-manager/SKILL.md) -- AR must be reconciled for accurate revenue and cash reporting during close.
