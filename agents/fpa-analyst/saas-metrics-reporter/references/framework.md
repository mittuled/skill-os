# Framework: saas-metrics-reporter

Defines the standardized calculation methodologies, definitions, and reporting structure for SaaS metrics to ensure consistency across internal reporting, board communications, and investor materials.

## Canonical Metric Definitions

All metrics must use these definitions consistently. Any deviation requires a footnote explaining the change and the reason.

### ARR and MRR

| Metric | Definition | What to Include | What to Exclude |
|--------|-----------|----------------|----------------|
| ARR | Annualized Committed Recurring Revenue | Subscription fees, committed minimum contracts (annualized) | One-time setup fees, professional services, usage above minimums |
| MRR | Monthly Recurring Revenue | ARR ÷ 12 OR sum of monthly subscription charges | Same exclusions as ARR |
| New ARR | ARR from customers who had $0 ARR in the prior period | Net new logo ARR | Expansion from existing customers |
| Expansion ARR | ARR increase from existing customers | Upsells, seat additions, usage upgrades | New logo ARR |
| Contraction ARR | ARR decrease from existing customers who are still customers | Downgrades, seat reductions | Churn |
| Churned ARR | ARR lost from customers who fully cancelled | Full cancellations, non-renewals | Contractions |

### Net Revenue Retention (NRR)

```
NRR = (Beginning MRR + Expansion MRR − Contraction MRR − Churned MRR) / Beginning MRR × 100%
```

- **Calculation window**: Rolling 12-month cohort (measure NRR for customers who existed 12 months ago)
- **Benchmark (growth stage)**: >100% = net expansion; >120% = best-in-class; <90% = concerning
- **Variants**: Report both trailing-12-month NRR and trailing-3-month annualized NRR; explain any gap

### Gross Revenue Retention (GRR)

```
GRR = (Beginning MRR − Contraction MRR − Churned MRR) / Beginning MRR × 100%
```

- GRR measures the floor of retention — what you keep before any expansion
- GRR ≤ NRR always (expansion can only add to NRR)
- **Benchmark**: >85% acceptable; >90% strong; <80% requires investigation

### Quick Ratio

```
Quick Ratio = (New MRR + Expansion MRR) / (Contraction MRR + Churned MRR)
```

- Measures growth efficiency: how much new revenue for every dollar lost
- **Benchmark**: >4 = high-growth SaaS; 1–4 = sustainable growth; <1 = more revenue lost than gained

## Data Sourcing Requirements

| Data Element | Primary Source | Secondary Validation |
|-------------|---------------|---------------------|
| Subscription bookings | Billing system (Stripe, Chargebee, Zuora) | CRM closed-won stage |
| Expansion revenue | Billing system | CS platform (account expansion events) |
| Churn and contraction | Billing system | CS churn log |
| Revenue recognized | GL (GAAP accounting) | Billing system deferred revenue rollforward |

**Reconciliation gate**: Billing system MRR and GL-recognized revenue must be reconciled before publishing any report. Maximum acceptable variance: ±0.5% or $5K, whichever is smaller.

## Cohort Analysis Structure

| Cohort Dimension | Purpose | Minimum Cohort Size |
|-----------------|---------|-------------------|
| Signup month | Measure retention decay curves | 5 customers |
| Acquisition segment (SMB/MM/ENT) | Identify which segments retain best | 10 customers |
| Plan tier | Identify price-point retention patterns | 5 customers |
| Acquisition channel | Connect CAC efficiency with LTV | 10 customers |
| Industry vertical | Surface vertical-specific retention | 5 customers |

## Industry Benchmarks by ARR Scale

| Metric | $1M–$10M ARR | $10M–$50M ARR | $50M+ ARR |
|--------|-------------|--------------|----------|
| NRR | 90–105% | 100–115% | 110–130% |
| GRR | 80–90% | 85–92% | 88–95% |
| Quick Ratio | 2–4 | 3–5 | 3–6 |
| Monthly growth rate | 10–20% MoM | 5–10% MoM | 3–6% MoM |

Source: Bessemer Venture Partners State of the Cloud; OpenView SaaS benchmarks. Update annually.

## Reporting Output Checklist

Before publishing any SaaS metrics report, confirm:

- [ ] All metrics use the canonical definitions above
- [ ] Billing system and GL are reconciled within the acceptable variance
- [ ] All metrics have trailing 6-month trend lines (not just point-in-time)
- [ ] Benchmark overlays are from the correct ARR scale band
- [ ] Any metric definition change is footnoted and explained
- [ ] Cohort breakdowns are included for NRR (minimum: by segment)
- [ ] Quick ratio is included to contextualize gross churn vs. expansion
