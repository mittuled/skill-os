# Equity Incentive Plan Framework

Reference framework for designing and implementing employee stock option plans covering IRC compliance, plan structure, and administration.

## Governing Law

### Federal
- **IRC Section 409A**: Deferred compensation rules; stock options must be granted at fair market value to avoid penalties. Requires independent 409A valuation (safe harbor: qualified appraisal, formula-based for startups under $10M revenue).
- **IRC Section 422**: Incentive Stock Option (ISO) requirements — $100K annual vesting limit, employment requirement, holding period (2 years from grant, 1 year from exercise), AMT implications on exercise.
- **IRC Section 83**: Taxation of property transferred in connection with services; governs restricted stock (83(a) income at vesting, 83(b) election to accelerate to grant).
- **Rule 701**: Securities exemption for compensatory equity grants by non-reporting companies. Limits: $1M or 15% of assets in any 12-month period; above threshold requires enhanced disclosure.
- **Section 4(a)(2)**: Private placement exemption for sophisticated/accredited participants.

### State
- **California**: Section 25102(o) exemption — requires plan adoption by board within 10 years of earlier of board/stockholder approval; stockholder approval within 12 months. California has an additional securities notice filing requirement.
- **New York**: Martin Act considerations for equity compensation. Blue sky filings required in certain circumstances.
- **State Blue Sky Laws**: Vary by state; some require notice filings or registration for compensatory securities.

## Pool Sizing Model

### Inputs
1. **Hiring plan**: Number of hires by role level for next 18-24 months
2. **Grant ranges by level**: Industry benchmarks (e.g., VP: 0.5-1.5%, Director: 0.25-0.5%, Senior IC: 0.1-0.25%, IC: 0.05-0.1%)
3. **Advisor grants**: Typically 0.25-1.0% per advisor
4. **Buffer**: 15-25% unallocated reserve for opportunistic hires and retention grants
5. **Investor expectations**: Post-money pool typically 10-15% for Series A, 15-20% for Series B

### Calculation
```
Total Pool = Σ(planned hires × midpoint grant %) + advisor grants + buffer
Pool % = Total Pool / Fully Diluted Shares
```

### Scenario Analysis
Model three scenarios: conservative (minimum hires, low grants), base case, aggressive (maximum hires, high grants). Present pool size that covers base case with buffer for aggressive.

## Plan Terms Decision Matrix

| Term | Standard | Aggressive (Employee-Friendly) | Conservative (Company-Friendly) |
|------|----------|-------------------------------|-------------------------------|
| Vesting | 4-year, 1-year cliff | 3-year, 6-month cliff | 4-year, 1-year cliff, back-weighted |
| Exercise Window | 90 days post-termination | 7-10 years post-termination | 90 days post-termination |
| Early Exercise | Not permitted | Permitted for all grants | Not permitted |
| Acceleration | Double-trigger only | Single-trigger on CoC | Double-trigger, board discretion |
| Grant Types | ISO + NSO | ISO + NSO + RSU + RSA | ISO + NSO only |
| Repurchase | Right of first refusal | No repurchase | ROFR + call option on termination |

## Document Package

1. **Equity Incentive Plan**: Master plan document defining all terms, share reserve, administration provisions
2. **Stock Option Agreement (ISO)**: Individual grant agreement for incentive stock options
3. **Stock Option Agreement (NSO)**: Individual grant agreement for non-qualified stock options
4. **Option Exercise Agreement**: Form for exercising vested options
5. **Restricted Stock Purchase Agreement**: For early exercise or restricted stock grants
6. **Board Resolution**: Adopting the plan and authorizing the share reserve
7. **Stockholder Consent**: Approving the plan (required within 12 months for ISO eligibility)
8. **409A Valuation Report**: Independent fair market value determination
9. **Plan Administration Guide**: Ongoing grant, exercise, and reporting procedures

## Administration Checklist

- [ ] 409A valuation obtained before first grant (and updated annually or upon material event)
- [ ] Board resolution adopted with share reserve specified
- [ ] Stockholder approval obtained within 12 months of board adoption
- [ ] Grant approval workflow established (board or committee authorization per grant)
- [ ] ISO $100K annual vesting limit tracked per employee
- [ ] Exercise procedures documented (cashless exercise, same-day sale options)
- [ ] Tax withholding procedures established (NSO: withhold at exercise; ISO: no withholding at exercise, AMT reporting)
- [ ] State securities filings completed (e.g., CA 25102(o) notice)
- [ ] Cap table updated with each grant, exercise, and cancellation
- [ ] Quarterly reconciliation of outstanding grants vs. available pool
