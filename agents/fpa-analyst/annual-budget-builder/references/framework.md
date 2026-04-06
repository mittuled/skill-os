# Framework: annual-budget-builder

Defines the process architecture, modelling standards, and scenario rules for building the annual operating budget.

## Budget Process Architecture

### Timeline (Working Backwards from Fiscal Year Start)

| Milestone | Timing Before FY Start | Owner |
|-----------|----------------------|-------|
| Revenue target set (board-aligned) | 10 weeks | CEO + CFO |
| Department budget templates distributed | 9 weeks | FP&A |
| Department requests submitted | 7 weeks | Dept Heads |
| Headcount plan finalized | 6 weeks | FP&A + People |
| P&L consolidation complete | 5 weeks | FP&A |
| Scenario analysis complete | 4 weeks | FP&A |
| CFO review and adjustment | 3 weeks | CFO |
| Board approval package submitted | 2 weeks | FP&A + CFO |
| Board approval | 1 week | Board |
| Budget loaded into financial system | FY Start | FP&A |

### Iteration Rounds

Expect 3 rounds of revision between initial department requests and board approval:
1. **Round 1**: Remove requests not backed by ROI rationale
2. **Round 2**: CFO alignment on P&L structure and key constraints (Rule of 40, burn multiple)
3. **Round 3**: Board-facing adjustments and narrative refinement

## Revenue Target Methodology

### Dual-Method Reconciliation

Run both methods and reconcile the gap — do not default to one approach:

**Bottoms-Up Method**
```
New ARR = (AE headcount at start) × (quota) × (attainment assumption) 
        + (planned new AE hires) × (quota) × (ramp-adjusted attainment)
        + (inbound leads) × (conversion rate) × (ACV)
Expansion ARR = Beginning ARR × expansion rate assumption
Ending ARR = Beginning ARR + New ARR + Expansion ARR - (Beginning ARR × gross churn rate)
```

**Top-Down Method**
```
Target ARR = Board/investor expectation for next fundraise milestone
           OR current ARR × target growth rate (benchmarked to Series stage)
```

Typical gap: 15-30%. The reconciliation discussion forces the team to decide whether the gap closes via more hires, higher quotas, better conversion, or accepting a lower target.

## Headcount Modelling Standards

### Fully-Loaded Cost Components

Never budget headcount at base salary only:

| Component | Typical % of Base | Notes |
|-----------|------------------|-------|
| Base salary | 100% | Source: approved offer letters or bands |
| Employer payroll taxes | 7–10% | Varies by jurisdiction |
| Benefits | 15–25% | Health, dental, vision, 401k match |
| Equity (annualized vest value) | 5–20% | Use Black-Scholes or 409A for options; market price for RSUs |
| Equipment and setup | $2–5K one-time | Allocated to hire month |
| Productivity tools | $1–3K annual | Seat licenses, SaaS tools |

### Ramp Assumption Rules

- AEs and SDRs: Model revenue attainment at 0% / 33% / 66% / 100% for quarters 1-4
- CSMs: Model full capacity at month 3 (90-day ramp)
- Engineers: Model full productivity at month 3 for senior ICs; month 6 for managers
- G&A: No ramp — budget at full cost from hire month

### Headcount Budget Template Per Department

```
Dept | Role | Level | Start Month | Base Salary | Fully Loaded | FY Cost | Revenue Impact
```

## P&L Consolidation Standards

### Cost Category Mapping

All budget items must map to a GAAP-aligned P&L category:

| Department Spend | GAAP Line | Notes |
|-----------------|-----------|-------|
| Product engineering salaries | R&D | Capitalize portion meeting ASC 350 criteria |
| Customer support | COGS | Allocated to cost of revenue |
| Implementation/onboarding | COGS | Allocated to cost of revenue |
| Sales headcount + commissions | S&M | Do not split across categories |
| Marketing (all) | S&M | Include events, content, and agency fees |
| HR, Finance, Legal, IT | G&A | Fully allocated |
| CEO office | G&A | Standard allocation |

### Top-Level Constraints

Apply these as final checks before board submission:

| Metric | Series A Target | Series B Target | Series C+ Target |
|--------|---------------|----------------|-----------------|
| Gross Margin | >65% | >70% | >75% |
| S&M as % of Revenue | <50% | <40% | <35% |
| Rule of 40 | >20 | >30 | >40 |
| Burn Multiple | <2.0x | <1.5x | <1.0x |
| Runway | >15 months | >12 months | >12 months |

If the consolidated budget fails any constraint, iterate before presenting to the board.

## Cash Flow Budget Rules

### Billings vs. Revenue Timing

Model cash separately from revenue — they are not the same:

```
Monthly Billings = (New annual customers × ACV) + (New monthly customers × MRR) 
                 + (Renewal customers × ACV, in their renewal month)
Cash Collections = Prior month billings × collection assumption (typically 85-90% in 30 days)
                 + Prior-prior month remaining balance
```

### Capex Treatment

For SaaS companies, major capex categories:
- Hardware / server infrastructure: capitalize and depreciate over 3-5 years
- Capitalized internal development: track hours for ASC 350 capitalization; depreciate over useful life
- Office buildout: capitalize and depreciate over lease term
- Software licenses (annual): expense directly; do not capitalize

## Scenario Trigger Thresholds

Define the conditions that shift the company from base to upside or downside mode:

| Scenario | Trigger | Action |
|---------|---------|--------|
| Upside | ARR 15%+ above quarterly plan for 2 consecutive quarters | Accelerate approved headcount; activate upside hiring plan |
| Base | ARR within ±10% of quarterly plan | Execute as budgeted |
| Downside | ARR >10% below quarterly plan for 1 quarter | Freeze discretionary spend; defer non-critical hires |
| Severe downside | ARR >20% below quarterly plan or runway drops below 9 months | Activate RIF plan; reduce burn to minimum viable runway |
