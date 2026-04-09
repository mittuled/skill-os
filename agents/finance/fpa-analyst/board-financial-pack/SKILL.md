---
name: board-financial-pack
description: >
  This skill prepares the financial section of the board pack including KPIs, budget vs.
  actuals, and outlook. Use when asked to build the finance slides for a board meeting,
  prepare the financial summary for board review, or compile KPI dashboards for directors.
  Also consider when board meetings are approaching without a finance section drafted.
  Suggest when the user is preparing board materials without finance-validated numbers.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-variance-analyser/SKILL.md
  - ../../../finance/investor-relations-manager/board-materials-coordinator/SKILL.md
  - ../saas-metrics-reporter/SKILL.md
triggers:
  - "build board financial pack"
  - "board finance slides"
  - "board financial report"
  - "prepare board financials"
  - "board pack financials"
---

# board-financial-pack

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Prepares the financial section of the board pack including KPIs, budget vs. actuals, variance commentary, and forward-looking outlook for board-level decision-making.

## When to Use

- When a board meeting is scheduled and the financial section of the board pack needs preparation.
- When the CFO requests an ad-hoc financial summary for investor or board communication.
- When quarterly results are finalized and need to be packaged for board consumption.

## Workflow

1. **Data Collection**: Pull finalized monthly or quarterly actuals from the accounting system. Confirm the close is complete and numbers are final. Collect non-financial KPIs from department leads. Deliverable: verified data package with source confirmation.
2. **Budget vs. Actuals Analysis**: Compare actuals against budget and prior year for revenue, gross margin, OpEx by category, EBITDA, and cash. Calculate variances as both absolute dollars and percentages. Deliverable: budget vs. actuals table with variance columns.
3. **Variance Commentary**: Write narrative explanations for all material variances (>5% or >$50K). Answer "what happened" and "so what" for each. Distinguish between timing variances and permanent variances. Deliverable: variance commentary document.
4. **KPI Dashboard Assembly**: Compile the SaaS metrics dashboard (ARR, MRR growth, NRR, gross churn, LTV/CAC, burn multiple, runway) with trend lines showing 6-month trajectory. Deliverable: KPI dashboard with trend visualizations.
5. **Outlook and Risks**: Update the forward-looking outlook including revised forecast, key risks, and any asks of the board (budget approval, strategic decisions). Deliverable: outlook section with risk flags and decision requests.

## Anti-Patterns

- **Data dump without narrative**: Presenting tables of numbers without explaining what they mean for the business. *Why*: board members need insight, not data; numbers without context waste board time and erode confidence in the finance team.
- **Hiding bad news in footnotes**: Burying unfavorable variances in dense tables rather than leading with them. *Why*: boards that discover bad news buried in materials lose trust in management; proactive transparency builds credibility.
- **Stale metrics**: Using metric definitions or benchmarks that have not been updated as the company evolved (e.g., still reporting on user count when the model shifted to usage-based). *Why*: outdated metrics obscure the real story and signal that finance is not keeping up with the business.

## Output

**On success**: Produces the financial section of the board pack containing the budget vs. actuals analysis, variance commentary, KPI dashboard, and outlook. Delivered as slide-ready content and a supporting data appendix.

**On failure**: Report which data is not yet finalized (e.g., close not complete for the period), what preliminary analysis is available, and the expected timeline for final numbers. Provide a draft with clearly marked provisional figures.

## Related Skills

- [`monthly-variance-analyser`](../monthly-variance-analyser/SKILL.md) -- Provides the detailed variance analysis that feeds the board pack commentary.
- [`board-materials-coordinator`](../../../finance/investor-relations-manager/board-materials-coordinator/SKILL.md) -- Coordinates the overall board pack that this financial section integrates into.
