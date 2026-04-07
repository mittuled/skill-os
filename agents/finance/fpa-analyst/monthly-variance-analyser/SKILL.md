---
name: monthly-variance-analyser
description: >
  This skill analyses monthly actuals vs. budget and forecast, identifying and explaining
  key variances. Use when asked to run the monthly variance analysis, explain why actuals
  diverged from plan, or prepare variance commentary for leadership. Also consider when
  the monthly close completes without variance analysis. Suggest when the user is reviewing
  financials without understanding why numbers moved.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../rolling-forecast-updater/SKILL.md
  - ../board-financial-pack/SKILL.md
---

# monthly-variance-analyser

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Analyses monthly actuals against budget and forecast, identifying material variances, attributing root causes, and producing actionable commentary for leadership.

## When to Use

- When the monthly close is complete and actuals are available for comparison against budget and forecast.
- When leadership asks why a specific P&L line item or KPI deviated from plan.
- When preparing the financial narrative for the board pack or investor update.

## Workflow

1. **Data Extraction**: Pull finalized actuals from the GL and compare against the approved budget and latest rolling forecast. Calculate variances as absolute dollars, percentages, and year-to-date cumulative. Deliverable: variance waterfall by P&L line item.
2. **Materiality Filtering**: Apply materiality thresholds (>5% variance AND >$10K for early-stage, adjusted for company size) to focus analysis on variances that matter. Deliverable: prioritized variance list.
3. **Root Cause Attribution**: For each material variance, identify the root cause: volume (more/fewer customers), price (ACV changes), timing (revenue recognition, expense accruals), or one-time items. Classify as permanent or timing. Deliverable: root cause analysis with classification.
4. **Commentary Writing**: Write concise variance commentary that answers three questions: what happened, why it happened, and what it means for the full-year outlook. Use the "so what" test -- every variance explanation must include a business implication. Deliverable: variance commentary document.
5. **Forecast Impact Assessment**: Determine whether each material variance should change the rolling forecast. Flag variances that represent trend shifts vs. one-time events. Deliverable: forecast adjustment recommendations.

## Anti-Patterns

- **Explaining every line item**: Writing commentary on immaterial variances that fall within normal operating noise. *Why*: exhaustive variance reports dilute attention from the few variances that actually matter and waste leadership's time.
- **Describing the variance without the "so what"**: Stating "travel was $20K over budget" without explaining the business impact or whether it will recur. *Why*: variance analysis without implications is bookkeeping, not strategic finance.
- **Treating all variances as permanent**: Adjusting the forecast for every variance without distinguishing between timing (invoice timing, accrual catch-ups) and permanent (structural cost increases, demand shifts). *Why*: over-adjusting the forecast based on timing variances creates unnecessary volatility in projections.

## Output

**On success**: Produces a monthly variance report containing the variance waterfall, root cause analysis, commentary, and forecast adjustment recommendations. Delivered to the CFO and department heads within 5 business days of close.

**On failure**: Report which actuals are not yet finalized, what preliminary variance analysis is possible with available data, and the expected timeline for final numbers. Flag any data quality issues discovered during extraction.

## Related Skills

- [`rolling-forecast-updater`](../rolling-forecast-updater/SKILL.md) -- Consumes the variance insights to update the rolling forecast.
- [`board-financial-pack`](../board-financial-pack/SKILL.md) -- Uses the variance commentary as a key input to the board financial section.
