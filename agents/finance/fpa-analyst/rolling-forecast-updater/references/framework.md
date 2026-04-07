# Framework: rolling-forecast-updater

Defines the process and principles for updating the rolling forecast to maintain a continuously accurate financial outlook that replaces budget assumptions with reality.

## Rolling Forecast Architecture

### What a Rolling Forecast Is (and Is Not)

| Rolling Forecast | Annual Budget |
|-----------------|--------------|
| Updated monthly with actuals | Set once per year |
| Always shows the next 12 months | Shows the remaining fiscal year |
| Actuals replace projections as time passes | Actuals compared against a fixed plan |
| Designed to be accurate | Designed to set targets |
| Purpose: enable decisions | Purpose: establish accountability |

### Update Cadence

| Trigger | Type of Update | Scope | Timeline |
|--------|---------------|-------|---------|
| Monthly close complete | Regular update | Full P&L, cash flow, runway | Within 7 business days of close |
| Material business event | Ad hoc update | Affected revenue/cost lines + runway | Within 3 business days of event |
| CFO / board request | On-demand | Specific scenarios or KPIs | Within 2 business days of request |

### Material Events Requiring Ad Hoc Updates

- Signed or lost deal > 10% of monthly new ARR target
- Approved headcount change affecting > 2% of monthly OpEx
- Major contract renegotiation (customer expansion, vendor rate change)
- Market shift visible in pipeline quality (conversion rate drop > 15%)
- Fundraising close (updates runway and use-of-proceeds assumptions)

## Revenue Forecast Methodology

### Bottom-Up Revenue Build

```
Forecasted MRR = Beginning MRR
                 + Forecasted New MRR (from sales pipeline, weighted by stage)
                 + Forecasted Expansion MRR (from CS expansion pipeline)
                 − Forecasted Contraction MRR (based on at-risk accounts)
                 − Forecasted Churn MRR (based on renewal calendar × GRR assumption)
```

### Pipeline Weighting Convention

| Deal Stage | Weight Applied |
|-----------|---------------|
| Discovery | 10% |
| Demo / Qualification | 20% |
| Proposal / Evaluation | 40% |
| Negotiation / Legal | 70% |
| Verbal Commit | 90% |
| Closed-Won | 100% |

Adjust weights based on historical stage conversion rates — recalibrate every 6 months using actual close data.

### Revenue Forecast Reconciliation

Reconcile the bottom-up forecast against the top-down run-rate:
- **Run-rate check**: Current MRR × 12 = implied ARR; add expected net expansion
- **Pipeline check**: Weighted pipeline (next 90 days) should explain the difference between current ARR and forecasted ARR in the same period
- **Variance > 10%**: Investigate discrepancy; do not blend without explanation

## Expense Forecast Methodology

### Headcount-Driven Expenses (typically 60–75% of OpEx)

- Maintain a position-level headcount roster with actual start dates
- Use fully-loaded cost per employee: salary + benefits (1.15–1.20× base) + payroll taxes + equipment
- Apply ramp assumptions to quota-carrying roles: 50% productivity in month 1–3, 75% in month 4–6, 100% thereafter
- Update actual vs. planned start dates each month

### Non-Headcount Expenses

- Lock committed vendor contracts at the contracted rate
- Apply seasonality adjustments from prior-year actuals for variable marketing spend
- Flag any expense line with a month-over-month variance > 15% for investigation

## Cash Flow Update Protocol

| Component | Source | Update Frequency |
|-----------|--------|-----------------|
| Operating cash inflows | Billing forecast × collection timing (DSO) | Monthly |
| Operating cash outflows | Expense forecast × payment timing | Monthly |
| Capex | Approved capital projects | Monthly |
| Financing activities | Debt draws/repayments, equity | As events occur |

### Runway Calculation Standard

```
Ending Cash = Beginning Cash + Cash Inflows − Cash Outflows (per month)
Runway = Ending Cash / Average Monthly Net Burn (trailing 3 months)
```

Report runway as:
- **Base case**: current forecast assumptions
- **Upside case**: +15% revenue, no cost change
- **Downside case**: −20% revenue, no cost change
- **Extended runway**: −20% revenue, planned cost reduction actions

## Forecast Quality Gates

Before distributing the updated forecast, confirm:

- [ ] All actuals for closed months are final (GL period locked)
- [ ] Revenue forecast reconciles to weighted pipeline within 10%
- [ ] Headcount roster is updated with actual vs. planned starts
- [ ] Committed vendor contracts are at contracted rates, not estimates
- [ ] Cash flow runway is calculated for base + upside + downside
- [ ] Forecast-to-budget bridge is prepared with explanations for all variances > 5% or $50K
- [ ] CFO review completed before distribution to department heads
