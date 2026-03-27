---
name: tax-compliance-manager
description: >
  This skill manages tax compliance obligations including filings, payments, and nexus
  tracking. Use when asked to file tax returns, manage sales tax obligations, or assess
  nexus exposure. Also consider when the company expands to new states or countries that
  may create tax obligations. Suggest when the user is selling into new jurisdictions
  without tax compliance review.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: medium
related-skills:
  - ../payroll-processor/SKILL.md
  - ../financial-audit-preparer/SKILL.md
---

# tax-compliance-manager

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Manages tax compliance obligations including income tax filings, sales tax collection and remittance, nexus tracking, and coordination with external tax advisors to avoid penalties and optimize the tax position.

## When to Use

- When tax filing deadlines are approaching (quarterly estimates, annual returns, sales tax remittance).
- When the company expands operations, hires employees, or generates revenue in new jurisdictions that may create nexus.
- When an R&D tax credit study, transfer pricing review, or other tax planning opportunity needs coordination.

## Workflow

1. **Tax Calendar Management**: Maintain a comprehensive tax calendar with all filing deadlines (federal, state, local, international), estimated payment dates, and information return due dates (1099s, W-2s). Set alerts at 30 and 7 days before each deadline. Deliverable: updated tax calendar with owner assignments.
2. **Nexus Monitoring**: Track nexus-creating activities by jurisdiction: employee presence, revenue thresholds (economic nexus), physical inventory, and contractor activity. Assess whether new nexus obligations have been triggered. Deliverable: nexus tracking matrix with status.
3. **Income Tax Compliance**: Coordinate the preparation and filing of federal and state income tax returns with external tax advisors. Provide required financial data, reconcile tax provision to return, and review draft returns for accuracy. Deliverable: filed tax returns with review documentation.
4. **Sales Tax Management**: Ensure sales tax is collected on taxable transactions in nexus jurisdictions. Reconcile collections against remittance filings. Monitor for exemption certificate validity. Deliverable: sales tax reconciliation and filed returns.
5. **Tax Provision and Planning**: Coordinate the quarterly and annual tax provision (ASC 740) with external advisors. Identify tax planning opportunities (R&D credits, Section 174 capitalization, qualified small business stock). Deliverable: tax provision workpaper and planning memo.

## Anti-Patterns

- **Ignoring economic nexus**: Assuming no tax obligation exists because the company has no physical presence in a jurisdiction. *Why*: post-Wayfair, economic nexus thresholds (typically $100K revenue or 200 transactions) create sales tax obligations regardless of physical presence.
- **Reactive compliance only**: Filing returns and paying taxes without proactive planning for credits, deductions, and structural optimization. *Why*: reactive-only compliance leaves money on the table; R&D credits alone can offset hundreds of thousands in early-stage tax liability.
- **Missing the 1099 threshold**: Failing to issue 1099s to contractors and service providers who exceed the $600 threshold. *Why*: missing 1099s create IRS penalty exposure and audit triggers.

## Output

**On success**: Produces filed tax returns, sales tax remittance confirmations, nexus tracking matrix, tax provision workpapers, and tax planning memo. Delivered per the tax calendar.

**On failure**: Report which filings could not be completed on time, what extensions were filed, and what information is needed from other teams. Quantify penalty exposure for any missed deadlines. Escalate to CFO immediately.

## Related Skills

- [`payroll-processor`](../payroll-processor/SKILL.md) -- Coordinates on payroll tax withholding, filings, and year-end W-2 preparation.
- [`financial-audit-preparer`](../financial-audit-preparer/SKILL.md) -- Tax provision and compliance documentation are key audit deliverables.
