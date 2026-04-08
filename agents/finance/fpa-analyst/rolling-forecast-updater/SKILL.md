---
name: rolling-forecast-updater
description: >
  This skill updates the rolling forecast monthly based on actual performance and pipeline
  changes. Use when asked to refresh the forecast, update projections with latest actuals,
  or reforecast based on changed assumptions. Also consider when material business changes
  occur mid-month that invalidate current projections. Suggest when the user is making
  resource decisions based on a stale forecast.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-variance-analyser/SKILL.md
  - ../annual-budget-builder/SKILL.md
triggers:
  - "revenue forecast"
  - "financial forecast"
  - "revenue-forecaster"
  - "update forecast"
---

# rolling-forecast-updater

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Updates the rolling forecast monthly by replacing projections with actuals, incorporating pipeline changes, and adjusting assumptions to maintain a continuously accurate financial outlook.

## When to Use

- When the monthly close is complete and the rolling forecast needs to be refreshed with actuals.
- When a material event (large deal signed/lost, headcount change, market shift) requires an interim forecast update.
- When the CFO needs an updated runway calculation or cash flow projection for board communication.

## Workflow

1. **Actuals Integration**: Replace forecast months with finalized actuals. Recalculate year-to-date performance and remaining-period projections. Update the baseline for all forward-looking assumptions. Deliverable: forecast model with actuals integrated.
2. **Revenue Reforecast**: Update the revenue forecast using latest pipeline data (weighted pipeline by stage), bookings run-rate, churn actuals, and expansion trends. Reconcile with sales team's bottom-up commit. Deliverable: updated revenue forecast with pipeline support.
3. **Expense Reforecast**: Update expense projections based on actual hiring pace vs. plan, vendor commitments, and any approved spend changes. Adjust for timing differences identified in variance analysis. Deliverable: updated expense forecast by department.
4. **Cash Flow Update**: Recalculate the cash flow forecast with updated billing mix, collections performance (DSO trend), and payment timing. Update runway calculation. Deliverable: updated cash flow forecast with runway.
5. **Forecast vs. Budget Reconciliation**: Document the delta between the updated forecast and the annual budget. Explain the drivers of deviation and flag whether budget reallocation is needed. Deliverable: forecast-to-budget bridge with commentary.

## Anti-Patterns

- **Forecast anchoring**: Keeping the forecast close to the original budget even when actuals clearly indicate a different trajectory. *Why*: anchored forecasts give leadership false confidence and delay necessary course corrections.
- **Single-point forecasting**: Updating only the base case without refreshing best/worst scenarios. *Why*: leadership needs the range of outcomes to make informed decisions, especially as the year progresses and uncertainty resolves.
- **Ignoring pipeline quality**: Updating the revenue forecast using pipeline totals without adjusting for stage conversion rates and deal age. *Why*: a pipeline full of stale or early-stage deals overstates the revenue outlook.

## Output

**On success**: Produces an updated rolling forecast containing revenue, expense, and cash flow projections with a forecast-to-budget bridge and scenario updates. Delivered to the CFO within 7 business days of close.

**On failure**: Report which inputs are pending (e.g., pipeline data not updated by sales, close not finalized), what partial update is possible, and the expected timeline for a complete forecast. Flag any data quality issues.

## Related Skills

- [`monthly-variance-analyser`](../monthly-variance-analyser/SKILL.md) -- Provides the variance insights that inform forecast adjustments.
- [`annual-budget-builder`](../annual-budget-builder/SKILL.md) -- Establishes the annual budget that the rolling forecast is compared against.
