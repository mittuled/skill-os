# Tax Compliance Calendar

## Metadata

| Field | Value |
|-------|-------|
| Tax Year | [YYYY] |
| Author | [Controller name] |
| External Tax Advisor | [Firm name] |
| Last Updated | [YYYY-MM-DD] |
| Skill | tax-compliance-manager |

## Federal Tax Calendar

### Income Tax

| Filing / Payment | Due Date | Extended Due Date | Owner | Status | Notes |
|-----------------|---------|------------------|-------|--------|-------|
| Q1 Estimated Tax Payment (Form 1120-W) | April 15, [YYYY] | N/A | Controller + Tax Advisor | [ ] | — |
| Q2 Estimated Tax Payment | June 15, [YYYY] | N/A | Controller + Tax Advisor | [ ] | — |
| Q3 Estimated Tax Payment | September 15, [YYYY] | N/A | Controller + Tax Advisor | [ ] | — |
| Q4 Estimated Tax Payment | December 15, [YYYY] | N/A | Controller + Tax Advisor | [ ] | — |
| Corporate Income Tax Return (Form 1120) | April 15, [YYYY] for prior year | October 15 with extension | Controller + Tax Advisor | [ ] | — |

### Payroll Tax

| Filing / Payment | Frequency | Owner | Notes |
|-----------------|-----------|-------|-------|
| Federal tax deposits (Form 941 schedule) | [Semi-weekly / Monthly — based on lookback period] | Controller | Via EFTPS |
| Form 941 quarterly return | Quarterly — April 30, July 31, Oct 31, Jan 31 | Controller | — |
| Form 940 FUTA annual return | January 31 following year | Controller | — |
| W-2 and W-3 filing | January 31 following year | Controller | SSA electronic filing |
| 1099-NEC (for contractor payments ≥$600) | January 31 following year | Controller | IRS FIRE system |

### Information Returns

| Form | Purpose | Due Date | Threshold | Owner |
|------|---------|---------|-----------|-------|
| 1099-NEC | Contractor payments | Jan 31 | $600+ | Controller |
| 1099-MISC | Rents, royalties, prizes | Jan 31 | $600+ | Controller |
| 1099-K | Payment card transactions | Jan 31 | $5,000 (2024+) | Controller |
| 3921 | ISO exercises | Jan 31 | All exercises | Controller |
| 3922 | ESPP transfers | Jan 31 | All transfers | Controller |

## State Income Tax Calendar

| State | Filing Type | Due Date | Extended Due Date | Nexus Basis | Status |
|-------|------------|---------|------------------|------------|--------|
| [Delaware] | Annual corporate return | [March 1] | — | [State of incorporation] | [ ] |
| [California] | Annual franchise tax + return | [March 15 for S-Corps / April 15 for C-Corps] | [September 15 with extension] | [Employees / revenue] | [ ] |
| [New York] | Annual corporate tax | [April 15] | [October 15] | [Employees] | [ ] |
| [Texas] | Franchise tax (no income tax) | [May 15] | [November 15] | [Revenue nexus] | [ ] |

## Sales Tax Calendar

| State | Nexus Basis | Filing Frequency | Next Due Date | Monthly Sales | Status |
|-------|------------|----------------|--------------|--------------|--------|
| [California] | [Economic nexus — $500K+ revenue] | [Monthly] | [YYYY-MM-DD] | [$XX,XXX] | [ ] |
| [New York] | [Economic nexus — $500K+] | [Quarterly] | [YYYY-MM-DD] | [$XX,XXX] | [ ] |
| [Texas] | [Economic nexus — $500K+] | [Monthly] | [YYYY-MM-DD] | [$XX,XXX] | [ ] |

**SaaS taxability note**: SaaS is taxable in [list states where taxable]. Verify taxability by state before collecting/remitting. [States where SaaS is exempt: list].

## Nexus Tracking Matrix

| State | Nexus Trigger | Threshold | Current Status | Income Tax Nexus | Sales Tax Nexus | Action Required |
|-------|-------------|-----------|---------------|-----------------|-----------------|----------------|
| [California] | Employees + revenue | >$600K revenue or 25% apportionment | [Active nexus] | [Yes] | [Yes] | [Filed and compliant] |
| [New York] | Employees + revenue | >$1M revenue | [Active nexus] | [Yes] | [Yes] | [Filed and compliant] |
| [Florida] | Revenue | >$100K | [Approaching — $80K YTD] | [No income tax] | [MONITOR — approaching] | [Set up sales tax account when threshold hit] |
| [Washington] | Revenue | >$100K | [Not reached] | [No income tax] | [Not yet] | [Monitor monthly] |

**Wayfair economic nexus thresholds** (default if state-specific not listed): $100,000 in sales OR 200 transactions.

## Year-End Tax Compliance Checklist

### By November 30
- [ ] Confirm all 1099 vendor information (W-9s on file for all vendors paid $600+)
- [ ] Run preliminary nexus analysis for new states entered during the year
- [ ] Provide year-end tax provision data package to external tax advisors
- [ ] Review Q4 estimated payment calculation

### By January 15
- [ ] Complete payroll year-end reconciliation (gross wages, withholdings, employer FICA)
- [ ] Prepare W-2 data for payroll provider
- [ ] Prepare 1099 data for all qualifying vendors
- [ ] Complete 3921 data for all ISO exercises during the year

### By January 31
- [ ] File/distribute W-2s
- [ ] File/distribute 1099-NECs
- [ ] File 3921 forms
- [ ] File Q4 Form 941

### By March 15 / April 15 (per entity type)
- [ ] Corporate income tax return filed (or extension filed)
- [ ] All state returns filed (or extensions filed)
- [ ] Prior-year tax provision finalized and audited
