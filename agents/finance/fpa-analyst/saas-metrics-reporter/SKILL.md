---
name: saas-metrics-reporter
description: >
  This skill reports on SaaS-specific metrics including ARR, NRR, churn, and expansion
  revenue. Use when asked to produce the SaaS metrics report, calculate net revenue
  retention, or compile metrics for investor communications. Also consider when key
  SaaS metrics are being cited without a standardized calculation methodology. Suggest
  when the user is reporting SaaS metrics using inconsistent definitions.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../unit-economics-monitor/SKILL.md
  - ../board-financial-pack/SKILL.md
  - ../../investor-relations-manager/monthly-investor-update/SKILL.md
  - ../../finance-manager/north-star-metric-reviewer-finance/SKILL.md
  - ../../controller-accounting/accounts-receivable-manager/SKILL.md
---

# saas-metrics-reporter

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Reports on SaaS-specific metrics including ARR, MRR, net revenue retention, gross churn, and expansion revenue using standardized definitions and calculation methodologies.

## When to Use

- When the monthly or quarterly SaaS metrics report is due for leadership, board, or investor consumption.
- When a new metric needs to be added to the reporting suite with a standardized definition and calculation methodology.
- When discrepancies arise between different teams' calculations of the same metric (e.g., sales vs. finance ARR).

## Workflow

1. **Data Sourcing**: Extract subscription data from the billing system including new bookings, renewals, expansions, contractions, and churns. Reconcile against recognized revenue in the GL to ensure consistency. Deliverable: verified subscription data set with GL reconciliation.
2. **Metric Calculation**: Calculate each metric using documented, standardized formulas: ARR (annualized committed recurring revenue), MRR (monthly recurring), NRR (net revenue retention = (beginning MRR + expansion - contraction - churn) / beginning MRR), gross churn rate, expansion rate, and quick ratio (new + expansion / contraction + churn). Deliverable: calculated metrics with formula documentation.
3. **Cohort Analysis**: Break down retention and expansion metrics by customer cohort (signup month, segment, plan tier) to identify patterns masked by aggregate numbers. Deliverable: cohort-level metric breakdown.
4. **Trend and Benchmark Comparison**: Plot each metric against trailing 6-12 months to show trajectory. Compare against industry benchmarks (e.g., median NRR for SaaS at similar ARR scale). Deliverable: trend charts with benchmark overlays.
5. **Narrative Summary**: Write a concise summary highlighting metric movements, the drivers behind them, and implications for the business. Flag any metric that crossed a threshold (e.g., NRR dropped below 100%, churn exceeded target). Deliverable: SaaS metrics narrative.

## Anti-Patterns

- **Inconsistent ARR definitions**: Calculating ARR differently across reports (e.g., including one-time fees in one report but not another). *Why*: inconsistency destroys credibility with investors and makes internal trend analysis meaningless.
- **Aggregate-only reporting**: Reporting only company-level metrics without segment or cohort breakdowns. *Why*: aggregate NRR can mask a segment where retention is deteriorating rapidly, delaying intervention until the problem is material.
- **Reporting without context**: Presenting metrics without trend lines or benchmarks. *Why*: a 110% NRR means very different things depending on whether it is improving, stable, or declining, and whether peers are at 90% or 130%.

## Output

**On success**: Produces a SaaS metrics report containing calculated metrics, cohort analysis, trend charts, benchmark comparisons, and narrative summary. Delivered to the CFO, board pack, and investor update.

**On failure**: Report which data sources could not be reconciled, what metrics are reportable with available data, and what system or process fixes are needed for complete reporting. Include timeline for remediation.

## Related Skills

- [`unit-economics-monitor`](../unit-economics-monitor/SKILL.md) -- Provides the customer-level economics that complement these subscription metrics.
- [`board-financial-pack`](../board-financial-pack/SKILL.md) -- Consumes the SaaS metrics report as a key component of the board financial section.
