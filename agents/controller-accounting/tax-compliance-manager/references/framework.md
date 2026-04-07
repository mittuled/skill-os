# Framework: tax-compliance-manager

Defines the operational framework for managing the company's tax compliance obligations including federal, state, and local filings, nexus monitoring, and tax planning coordination.

## Tax Compliance Architecture

### Filing Calendar by Obligation Type

| Obligation | Filing / Payment | Frequency | Key Deadline |
|------------|-----------------|-----------|--------------|
| Federal income tax | Form 1120 (C-Corp) | Annual | April 15 (Oct 15 with extension) |
| Federal estimated tax | Form 1120-W | Quarterly | Apr 15, Jun 15, Sep 15, Dec 15 |
| Federal payroll taxes | Form 941 | Quarterly | Last day of month following quarter |
| Federal W-2 / W-3 | Form W-2, W-3 | Annual | January 31 |
| Federal 1099-NEC | Form 1099-NEC | Annual | January 31 |
| State income tax | State return | Annual | Varies by state (typically April–May) |
| State payroll taxes | State withholding return | Varies | Monthly, quarterly, or annual by state |
| Sales tax | State sales tax return | Varies | Monthly, quarterly, or annual by state |
| R&D tax credit | Section 41 study | Annual | With income tax return |

### Alert Protocol

Set automated reminders at:
- **30 days before**: Begin preparation; collect required data
- **14 days before**: Draft filing complete; ready for review
- **7 days before**: Final review; extension decision if needed
- **Day of deadline**: Confirm filing or extension is submitted

## Nexus Monitoring Framework

### Nexus-Creating Activities by Type

| Activity Type | Creates Income Tax Nexus? | Creates Sales Tax Nexus? | Notes |
|--------------|--------------------------|--------------------------|-------|
| Employee physically present | Yes | Yes | Any state with a full-time or part-time employee |
| Remote employee | Yes (many states) | Yes | Work-from-home creates nexus in employee's state |
| Revenue threshold crossed | Varies | Yes (post-Wayfair) | Economic nexus: typically $100K revenue or 200 transactions |
| Physical inventory | Yes | Yes | Warehouse, fulfillment center, or co-location |
| Independent contractor | Maybe | Maybe | Check state-specific standards (agency test) |
| Trade show or conference | Maybe | Maybe | Temporary presence rules vary by state |

### Nexus Tracking Matrix

Maintain a tracking matrix updated quarterly with:
- All states where employees reside
- All states where revenue exceeds $100K or 200 transactions (12-month rolling)
- Filing status per state (registered, filing, not yet required)
- Next threshold review date

## Income Tax Compliance Process

| Step | Activity | Owner | Timeline |
|------|---------|-------|---------|
| 1 | Provide trial balance and financial statements to tax advisor | Controller | Within 30 days of year-end close |
| 2 | Provide schedule of M-1 adjustment items (meals, stock comp, depreciation timing) | Controller | With financial package |
| 3 | Review draft federal return with tax advisor | CFO | 30 days before filing deadline |
| 4 | Review state apportionment methodology | CFO | With federal return review |
| 5 | Sign and file or file extension request | CEO/CFO | By deadline |
| 6 | Reconcile tax provision to return; adjust deferred tax balances | Controller | Within 60 days of filing |

## Sales Tax Management Process

| Step | Activity | Frequency |
|------|---------|-----------|
| 1 | Reconcile sales made into each nexus state against collected sales tax | Monthly |
| 2 | Prepare and file sales tax returns in each registration state | Monthly or quarterly per state |
| 3 | Remit collected tax to the applicable state revenue authority | Per return schedule |
| 4 | Review exemption certificates for business customers claiming exemption | Quarterly |
| 5 | Audit the product taxability matrix against any new product launches | At product launch |
| 6 | Review new states approaching economic nexus thresholds | Monthly |

## Tax Planning Opportunities

### R&D Tax Credit (Section 41)

- Qualifying activities: developing or improving products, internal-use software, processes
- Qualifying expenses: wages (employees performing QREs), contractor costs (65% of payments), supplies
- Credit rate: 20% of qualifying expenses above the base amount (simplified credit: 14% of average excess)
- Federal benefit: reduces tax liability dollar-for-dollar; startup election allows offset against payroll tax
- Action: engage a qualified R&D credit study firm annually; document qualifying activities contemporaneously

### Section 174 R&D Capitalization

- Post-2022 tax law requires domestic R&D expenses to be capitalized and amortized over 5 years (15 years for foreign)
- Identify all R&D-related wages, contractors, and overhead subject to Section 174
- Model the cash tax impact of 174 capitalization on estimated tax payments

### QSBS (Qualified Small Business Stock, Section 1202)

- Gain exclusion up to $10M (or 10x basis) for C-Corp stock held for 5+ years
- Confirm the company qualifies: C-Corp, aggregate gross assets under $50M at issuance, active business
- Issue QSBS eligibility letters to investors at funding close; maintain documentation

### Section 382 NOL Limitation

- Ownership changes greater than 50% over a 3-year period trigger Section 382 limits on NOL carryforwards
- Model the impact of fundraising rounds on ownership change percentages
- Coordinate with tax advisor before rounds that may trigger a Section 382 ownership change
