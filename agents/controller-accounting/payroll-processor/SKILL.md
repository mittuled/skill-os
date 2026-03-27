---
name: payroll-processor
description: >
  This skill processes payroll accurately and on time including deductions, equity
  compensation, and compliance filings. Use when asked to run payroll, set up a new
  employee in the payroll system, or handle payroll tax filings. Also consider when
  equity events (exercises, RSU vesting) create payroll tax implications. Suggest when
  the user is hiring without a payroll process in place.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-close-runner/SKILL.md
  - ../tax-compliance-manager/SKILL.md
---

# payroll-processor

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Processes payroll accurately and on time including salary, deductions, equity compensation tax treatment, benefits withholding, and federal/state compliance filings.

## When to Use

- When the regular payroll cycle (bi-weekly or semi-monthly) needs to be processed.
- When new hires, terminations, or compensation changes need to be reflected in the next payroll run.
- When equity events (option exercises, RSU vesting, ESPP purchases) create payroll tax withholding requirements.

## Workflow

1. **Payroll Input Collection**: Gather all inputs for the pay period: new hire data, terminations, salary changes, bonus approvals, commission calculations, expense reimbursements, and equity event notifications. Deliverable: verified payroll input package.
2. **Payroll Calculation**: Calculate gross pay, federal and state tax withholdings, benefits deductions (health, 401k, FSA), garnishments, and equity compensation tax treatment (ISO vs. NSO, RSU income recognition). Deliverable: payroll register draft.
3. **Review and Approval**: Review the payroll register for accuracy. Compare against prior period to identify anomalies. Obtain manager approval for any off-cycle payments or unusual items. Deliverable: approved payroll register.
4. **Payroll Submission**: Submit payroll to the payroll provider by the processing deadline. Confirm direct deposit initiation and check generation for any manual payments. Deliverable: payroll submission confirmation with payment dates.
5. **Post-Payroll Reconciliation**: Reconcile the payroll GL entries against the payroll register. Verify tax deposits were made accurately and on time. File any required state new-hire reports. Deliverable: payroll reconciliation workpaper.

## Anti-Patterns

- **Skipping equity tax treatment review**: Processing payroll with equity events without verifying the correct tax treatment (e.g., ISO AMT implications, NSO ordinary income). *Why*: incorrect equity tax withholding creates personal tax liability for employees and compliance exposure for the company.
- **Manual payroll calculations**: Calculating payroll manually in spreadsheets rather than using a payroll system with built-in tax tables. *Why*: manual calculations are error-prone and cannot keep up with changing tax rates, thresholds, and filing requirements.
- **Processing without reconciliation**: Running payroll without reconciling against the prior period or the GL. *Why*: unreconciled payroll accumulates errors in the largest expense category, creating material misstatements.

## Output

**On success**: Produces the approved payroll register, payment confirmations, tax filing confirmations, and payroll reconciliation workpaper. Delivered per the payroll calendar (bi-weekly or semi-monthly).

**On failure**: Report which payroll inputs are missing or incorrect, what partial processing was completed, and the impact on the payment deadline. Escalate immediately if the delay affects employee pay dates.

## Related Skills

- [`monthly-close-runner`](../monthly-close-runner/SKILL.md) -- Payroll accruals and GL entries are a key close input.
- [`tax-compliance-manager`](../tax-compliance-manager/SKILL.md) -- Coordinates payroll tax filings and compliance obligations.
