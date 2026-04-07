# Payroll Register and Reconciliation

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Controller / Payroll Coordinator name] |
| Pay Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Pay Date | [YYYY-MM-DD] |
| Frequency | [Bi-weekly / Semi-monthly] |
| Total Headcount | [N employees] |
| Total Gross Pay | [$XXX,XXX] |
| Total Net Pay (direct deposit) | [$XXX,XXX] |
| Skill | payroll-processor |

## Input Changes This Period

[Document all changes that affect this payroll run.]

| Change Type | Employee | Effective Date | Prior Value | New Value | Approval Reference |
|-------------|---------|---------------|------------|----------|------------------|
| [New hire] | [Name] | [YYYY-MM-DD] | — | [$XXX,XXX base, $XXX equity] | [Offer letter — [date]] |
| [Termination] | [Name] | [YYYY-MM-DD] | [$XXX,XXX base] | — | [Termination approval — [date]] |
| [Salary change] | [Name] | [YYYY-MM-DD] | [$XXX,XXX] | [$XXX,XXX] | [Board/manager approval — [date]] |
| [Bonus payment] | [Name] | [YYYY-MM-DD] | — | [$X,XXX gross] | [Manager approval — [date]] |
| [Equity event: NSO exercise] | [Name] | [YYYY-MM-DD] | — | [N shares at $X.XX] | [Option exercise notice — [date]] |

## Equity Compensation Tax Treatment

[Document required for any equity events in this period.]

| Employee | Event Type | Shares | Exercise/Grant Price | FMV per Share | Taxable Income | Withholding Required |
|----------|-----------|--------|---------------------|--------------|----------------|---------------------|
| [Name] | [NSO Exercise] | [N] | [$X.XX] | [$X.XX] | [(FMV - Exercise) × Shares = $X,XXX] | [Federal: $X,XXX / State: $X,XXX / FICA: $X,XXX] |
| [Name] | [RSU Vesting] | [N] | — | [$X.XX] | [FMV × Shares = $X,XXX] | [Federal: $X,XXX / State: $X,XXX / FICA: $X,XXX] |

**ISO exercise note**: ISOs exercised below FMV are not subject to regular withholding but create an AMT preference item. Notify employee and document for 3921 reporting.

## Payroll Register Summary

| Department | Headcount | Gross Salaries | Gross Bonuses | Equity Income | Total Gross | Employer FICA | Benefits Employer | Total Cost |
|------------|----------|--------------|--------------|--------------|------------|--------------|------------------|------------|
| Engineering | [N] | [$XX,XXX] | [$X,XXX] | [$X,XXX] | [$XX,XXX] | [$X,XXX] | [$X,XXX] | [$XX,XXX] |
| Sales | [N] | [$XX,XXX] | [$X,XXX] | — | [$XX,XXX] | [$X,XXX] | [$X,XXX] | [$XX,XXX] |
| Marketing | [N] | [$XX,XXX] | — | — | [$XX,XXX] | [$X,XXX] | [$X,XXX] | [$XX,XXX] |
| G&A | [N] | [$XX,XXX] | — | — | [$XX,XXX] | [$X,XXX] | [$X,XXX] | [$XX,XXX] |
| **Total** | **[N]** | **[$XXX,XXX]** | **[$X,XXX]** | **[$X,XXX]** | **[$XXX,XXX]** | **[$X,XXX]** | **[$X,XXX]** | **[$XXX,XXX]** |

## Employee Deduction Summary

| Deduction Type | Employee Contribution | Employer Contribution | Total |
|---------------|----------------------|----------------------|-------|
| Federal income tax (withheld) | [$XX,XXX] | — | [$XX,XXX] |
| State income tax (withheld) | [$X,XXX] | — | [$X,XXX] |
| Employee FICA (6.2% SS + 1.45% Medicare) | [$X,XXX] | [$X,XXX] (match) | [$X,XXX] |
| 401(k) employee contribution | [$X,XXX] | [$X,XXX] (match) | [$X,XXX] |
| Health insurance premiums | [$X,XXX] | [$X,XXX] | [$X,XXX] |
| FSA / HSA contributions | [$X,XXX] | — | [$X,XXX] |
| Other garnishments | [$X,XXX] | — | [$X,XXX] |

## Tax Deposits and Filings

| Tax | Amount | Deposit Deadline | Method | Status |
|-----|--------|----------------|--------|--------|
| Federal payroll taxes (941) | [$X,XXX] | [YYYY-MM-DD — next business day for semi-weekly depositor] | [EFTPS] | [Scheduled / Complete] |
| State income tax withholding | [$X,XXX] | [YYYY-MM-DD] | [State portal] | [Scheduled / Complete] |
| State unemployment (SUTA) | [$X,XXX] | [Quarterly — [YYYY-MM-DD]] | [State portal] | [N/A this period / Scheduled] |

## Prior Period Comparison

| Metric | Current Period | Prior Period | Change | Flag? |
|--------|--------------|-------------|--------|-------|
| Total gross pay | [$XXX,XXX] | [$XXX,XXX] | [+/-$X,XXX (+/-X%)] | [Yes if >10% without explanation] |
| Headcount | [N] | [N] | [+/- N] | — |
| Average gross pay per employee | [$X,XXX] | [$X,XXX] | [+/-$X,XXX] | — |
| Employer FICA | [$X,XXX] | [$X,XXX] | [+/-$X,XXX] | — |

**Anomalies investigated**: [List any variances >10% and the explanation, e.g., "Gross pay +$15K due to new hire starting mid-period and bonus payment approved by [Name]."]

## GL Journal Entry

| Account | Debit | Credit |
|---------|-------|--------|
| 8010 — Salaries Expense — G&A | [$XX,XXX] | — |
| 7010 — Salaries Expense — R&D | [$XX,XXX] | — |
| 6010 — Salaries Expense — Sales | [$XX,XXX] | — |
| 5010 — Salaries Expense — COGS | [$XX,XXX] | — |
| 2300 — Accrued Salaries Payable | — | [$XXX,XXX] |
| 2310 — Federal Payroll Tax Payable | — | [$X,XXX] |
| 2320 — State Payroll Tax Payable | — | [$X,XXX] |
| 2330 — Benefits Payable | — | [$X,XXX] |

## Approval Sign-Off

| Reviewer | Role | Status | Date |
|----------|------|--------|------|
| [Name] | Controller | [Approved] | [YYYY-MM-DD] |
| [Name] | CFO | [Approved] | [YYYY-MM-DD] |
