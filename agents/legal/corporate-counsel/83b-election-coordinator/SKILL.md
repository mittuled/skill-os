---
name: 83b-election-coordinator
description: >
  This skill coordinates 83(b) election filings for founders and early employees
  receiving restricted stock. Use when asked to file an 83(b) election, prepare
  election paperwork, or track the 30-day filing deadline. Also consider when
  restricted stock is being issued and the recipient needs tax election guidance.
  Suggest when the user is issuing restricted stock without mentioning 83(b) elections.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../founder-equity-issuance/SKILL.md
  - ../entity-formation/SKILL.md
  - ../../general-counsel/stock-plan-setup/SKILL.md
triggers:
  - "file 83b election"
  - "83b election"
  - "submit 83(b) form"
  - "83b tax election"
  - "founder 83b filing"
---

# 83b-election-coordinator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Coordinates the preparation, filing, and tracking of 83(b) elections for founders and early employees receiving restricted stock to ensure timely IRS submission within the 30-day deadline.

## When to Use

- When a founder or early employee receives restricted stock subject to vesting and needs to make an 83(b) election to minimize future tax liability.
- When the company issues restricted stock awards and must ensure recipients are informed of the 83(b) filing option and deadline.
- When a stock purchase agreement is being executed and the 30-day filing clock is about to start.

## Workflow

1. **Eligibility Assessment**: Determine whether the stock grant qualifies for an 83(b) election per IRC Section 83(a) — property transferred in connection with performance of services subject to substantial risk of forfeiture. Verify grant type qualifies (restricted stock YES, unexercised options NO, RSUs NO) per the eligibility verification section of `references/checklist.md`. Calculate the absolute 30-day deadline per IRC 83(b)(2). Deliverable: eligibility memo with deadline date.
2. **Election Preparation**: Draft the 83(b) election letter per Treasury Regulation 1.83(b)-1(d) requirements: taxpayer information, property description, fair market value at transfer (per most recent 409A valuation), amount paid, and nature of restrictions. Prepare IRS filing copy, company copy, and personal copy per `references/checklist.md`. Deliverable: completed 83(b) election form package.
3. **Filing Coordination**: File the election with the IRS Service Center via USPS Certified Mail with Return Receipt Requested (PS Form 3800) within 30 days of the grant date. Deliver copy to the company within 30 days. Notify recipient to attach copy to personal tax return for the taxable year of transfer per Reg 1.83(b)-1(b). Deliverable: proof of mailing with certified mail receipt and tracking number.
4. **Record Keeping**: File the return receipt and copies in the corporate minute book. Update the equity tracking system to reflect 83(b) election status per the post-filing record keeping section of `references/checklist.md`. Notify the CFO and payroll of the election for tax reporting (income recognized at grant date, no withholding at vesting). Deliverable: updated legal records and payroll notification.
5. **Deadline Monitoring**: Track all outstanding restricted stock grants and their 83(b) filing deadlines per the deadline monitoring system in `references/checklist.md`. Send reminders at grant date (Day 0), Day 15, Day 25, and Day 28. Escalate any at-risk deadlines to General Counsel immediately. Deliverable: deadline tracking log with reminder confirmations.

## Anti-Patterns

- **Missing the 30-day deadline**: Allowing the filing window to lapse due to administrative delay or lack of tracking. *Why*: the 30-day deadline is absolute and cannot be extended; missing it forces the recipient to pay ordinary income tax on the spread at each vesting milestone rather than at grant.
- **Filing without legal review**: Submitting the 83(b) election without verifying the grant terms, fair market value, or taxpayer details. *Why*: errors in the election form can render it invalid, and the IRS does not provide confirmation of acceptance.
- **Assuming all grants qualify**: Applying 83(b) elections to stock options or other instruments that do not qualify. *Why*: 83(b) elections apply only to property transferred in connection with performance of services; ISOs and NSOs at exercise are different situations requiring separate analysis.

## Output

**On success**: Produces a completed 83(b) election package with IRS filing confirmation (certified mail receipt), updated equity records, and payroll notification. Delivered within 30 days of the grant date.

**On failure**: Report which filing could not be completed (e.g., missing grant details, unsigned stock purchase agreement), the current deadline status, and immediate next steps. Escalate to General Counsel if the deadline is at risk.

## Related Skills

- [`founder-equity-issuance`](../founder-equity-issuance/SKILL.md) -- Founder equity issuance creates the restricted stock grants that trigger 83(b) election eligibility.
- [`entity-formation`](../entity-formation/SKILL.md) -- Entity formation establishes the corporate structure under which stock can be issued.
