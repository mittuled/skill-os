# Framework: board-financial-pack

Defines the structure, narrative standards, and presentation rules for the financial section of the board pack.

## Board Financial Pack Architecture

### Section Order

The financial section follows this order in the board pack:

1. **KPI Dashboard** — one-page visual summary of the metrics directors track across every meeting
2. **Budget vs. Actuals** — financial performance for the period vs. plan
3. **Variance Commentary** — narrative explanations for material variances
4. **Cash and Runway** — cash position and burn trajectory
5. **Outlook and Risks** — revised full-year forecast, key risks, and board asks

### Section Depth by Board Type

| Board Type | KPI Dashboard | BvA Detail | Commentary | Cash | Outlook |
|-----------|---------------|------------|------------|------|---------|
| Quarterly board meeting | Full | Full P&L | All material variances | Full | Full-year + 2-quarter look-ahead |
| Monthly update | Summary metrics only | Revenue + burn summary | Top 3 variances | Runway update | Current quarter |
| Special session | Focused on session topic | Relevant lines only | Issue-specific | If relevant | Decision-focused |

## SaaS KPI Dashboard Standards

### Required Metrics

Every board pack must include these metrics with trend lines (6-month minimum):

| Metric | Definition | Threshold Alert |
|--------|-----------|-----------------|
| ARR | Annualized run-rate recurring revenue | Flag if MoM growth decelerates >5 points |
| MRR Growth (MoM%) | Month-over-month MRR change | Flag if below 3-month average by >20% |
| NRR (Net Revenue Retention) | (Starting MRR + expansion - contraction - churn) / starting MRR | Flag if <100% for 2+ consecutive months |
| Gross Churn (%) | Churned MRR / beginning MRR | Flag if exceeds internal target |
| LTV/CAC Ratio | Gross-margin LTV / fully-loaded CAC | Flag if below 3x |
| Burn Multiple | Net burn / net new ARR | Flag if above 1.5x for Series A; above 1.0x for Series B+ |
| Runway (months) | Ending cash / monthly net burn | Flag if below 12 months |
| Rule of 40 | ARR growth % + EBITDA margin % | Flag if below 40 at Series B+ |

### Metric Consistency Rule

Never change a metric definition between board meetings without explicit board notification. If a definition change is required (e.g., shifting from gross revenue to net revenue), include a one-time reconciliation slide showing both the old and new calculation for the most recent 6 months.

## Budget vs. Actuals Structure

### P&L Comparison Table Format

```
                Budget    Actual    Var ($)    Var (%)    Prior Period
Revenue
  New ARR
  Expansion MRR
  Churn
  ─────────────────────────────────────────────
  Total Revenue
COGS
  ─────────────────────────────────────────────
  Gross Profit
  Gross Margin %
Operating Expenses
  R&D
  S&M
  G&A
  ─────────────────────────────────────────────
  Total OpEx
  ─────────────────────────────────────────────
  EBITDA
  EBITDA Margin %
Cash
  Beginning Cash
  Net Burn
  Ending Cash
  Runway (months)
```

### Prior Period Column

Always include a prior-period column (prior month for monthly boards; prior quarter for quarterly boards; prior year for YTD). Board members track trends, not snapshots.

## Narrative Standards

### Variance Commentary Rules

1. Lead with the dollar amount and direction before the explanation
2. Classify every material variance as permanent or timing — never leave it ambiguous
3. Include a "so what" — the business implication, not just the accounting fact
4. Keep each commentary block under 40 words
5. Never use passive voice — "we over-spent on S&M" not "S&M spending was elevated"

### Bad News Protocol

Board members must not discover material bad news by reading tables. The narrative must lead with bad news:
- If EBITDA miss exceeds 10% of budget, open the variance commentary section with it
- If cash runway has declined by more than 2 months vs. last meeting, open the cash section with it
- If a key metric crossed a threshold (e.g., NRR dropped below 100%), flag it in the KPI dashboard callout box

## Outlook Section Standards

### Forward-Looking Format

The outlook section must contain:

1. **Revised full-year forecast** — updated based on YTD actuals and trend adjustments
2. **Variance to original budget** — the gap between the original board-approved budget and the revised forecast
3. **Key risks** — maximum 5 risks, each with likelihood (H/M/L) and impact ($)
4. **Board asks** — specific decisions or approvals requested, not informational updates

### Board Ask Format

Each board ask must follow this structure:
- **What**: The specific decision or approval requested
- **Why now**: Why this requires board action at this meeting
- **Recommendation**: Management's recommended course of action
- **Alternatives considered**: What other options were evaluated
