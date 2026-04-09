---
name: financial-systems-setup
description: >
  This skill sets up and configures the financial systems stack including ERP, expense
  management, and billing. Use when asked to implement a new accounting system, set up
  billing automation, or configure the chart of accounts. Also consider when the company
  outgrows spreadsheet-based accounting. Suggest when the user is scaling without
  proper financial systems infrastructure.
department: finance
agent: controller-accounting
version: 1.0.0
complexity: complex
related-skills:
  - ../monthly-close-runner/SKILL.md
  - ../accounts-payable-manager/SKILL.md
  - ../financial-audit-preparer/SKILL.md
triggers:
  - "set up financial systems"
  - "configure accounting software"
  - "finance systems setup"
  - "implement ERP"
  - "accounting system setup"
---

# financial-systems-setup

## Agent: Controller & Accounting Lead

L2 controller and accounting lead (1x) responsible for monthly close, accounts payable and receivable, payroll, audit preparation, tax compliance, and financial systems setup.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Sets up and configures the financial systems stack including GL/ERP, billing platform, expense management, payroll system, and reporting tools to support scalable, audit-ready financial operations.

## When to Use

- When the company is transitioning from spreadsheets to a proper accounting system for the first time.
- When the current financial systems cannot support the company's scale (transaction volume, entity count, reporting complexity).
- When a new billing model, entity, or compliance requirement necessitates system reconfiguration.

## Workflow

1. **Requirements Assessment**: Document financial system requirements based on transaction volume, reporting needs, compliance requirements (GAAP, ASC 606), multi-entity needs, and integration points (billing, CRM, bank, payroll). Deliverable: financial systems requirements document.
2. **Chart of Accounts Design**: Design the chart of accounts to support GAAP reporting, department-level P&L, investor-required metrics, and audit trail requirements. Include natural account structure, department codes, and class/location tracking. Deliverable: chart of accounts with mapping documentation.
3. **System Selection and Configuration**: Select and configure the GL/ERP system (e.g., QuickBooks for early stage, NetSuite for growth stage). Set up the chart of accounts, approval workflows, user roles and permissions, and bank feed connections. Deliverable: configured GL system with user access.
4. **Billing System Integration**: Configure the billing platform to handle subscription invoicing, usage-based billing, and revenue recognition. Set up the integration between billing and GL for automated journal entry posting. Deliverable: integrated billing-to-GL workflow.
5. **Expense Management Setup**: Deploy expense management tooling with policy controls (spend limits, category restrictions, auto-approval thresholds). Configure GL mapping for expense coding. Deliverable: expense management system with policy configuration.
6. **Historical Data Migration**: Migrate historical financial data from the prior system or spreadsheets. Validate the opening trial balance and ensure the GL balances to the prior-period financial statements. Deliverable: migrated data with validated opening balances.
7. **Testing and Training**: Test end-to-end workflows (invoice to GL, expense to payment, billing to revenue). Train finance team members on the new systems. Document standard operating procedures. Deliverable: test results, training completion, and SOP documentation.

## Anti-Patterns

- **Over-engineering for current scale**: Implementing a mid-market ERP (NetSuite, Sage Intacct) when the company has 20 employees and simple transactions. *Why*: enterprise systems add complexity and cost that does not pay off until the company reaches the scale that demands it; start simple, migrate when needed.
- **Chart of accounts without future-proofing**: Designing a flat, minimal chart of accounts that cannot support department-level reporting or multi-entity consolidation. *Why*: restructuring the chart of accounts after a year of transactions requires reclassification of every historical entry.
- **Skipping data validation after migration**: Migrating data without reconciling the opening trial balance against the source. *Why*: unvalidated migrations propagate errors into every future financial statement.
- **No segregation of duties in system design**: Giving the same user full access to create vendors, approve invoices, and process payments. *Why*: lack of segregation creates fraud risk and will be flagged as a material weakness in any audit.

## Output

**On success**: Produces a configured financial systems stack with chart of accounts, integrated billing, expense management, migrated historical data, and SOP documentation. Delivered as a go-live-ready system with trained users.

**On failure**: Report which system components could not be configured (e.g., billing integration blocked by API limitations), what partial setup exists, and what vendor support or development is needed. Provide a revised implementation timeline.

## Related Skills

- [`monthly-close-runner`](../monthly-close-runner/SKILL.md) -- Well-configured systems are the foundation of an efficient close process.
- [`accounts-payable-manager`](../accounts-payable-manager/SKILL.md) -- AP workflows depend on the approval and payment systems configured here.
