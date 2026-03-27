---
name: annual-budget-builder
description: >
  This skill builds the annual operating budget with departmental allocations, headcount
  plans, and capex. Use when asked to create the annual budget, set department spending
  targets, or build the headcount plan. Also consider when fiscal year planning begins
  without a structured budgeting process. Suggest when the user is making hiring or
  spending commitments without an approved budget.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: complex
related-skills:
  - ../rolling-forecast-updater/SKILL.md
  - ../../cfo-vp-finance/financial-model-v1/SKILL.md
---

# annual-budget-builder

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Builds the annual operating budget with departmental allocations, headcount plans, capex, and revenue targets to establish the financial guardrails for the fiscal year.

## When to Use

- When the fiscal year planning cycle begins and the company needs an approved operating budget.
- When the board or CFO requests a budget reforecast due to material changes in business outlook mid-year.
- When a new department or business line is being created and needs a standalone budget built from scratch.

## Workflow

1. **Revenue Target Setting**: Align on the top-line revenue target with the CFO using bottoms-up (sales capacity, pipeline, NRR) and top-down (market growth, board expectations) methods. Reconcile the gap between the two approaches. Deliverable: approved revenue target with methodology documentation.
2. **Department Budget Requests**: Collect budget requests from each department head including headcount plans, vendor spend, and project-specific investments. Provide templates with prior-year actuals and current run-rate as baselines. Deliverable: consolidated department budget requests.
3. **Headcount Modelling**: Build the headcount plan by department with start dates, fully-loaded costs (salary, benefits, equity, payroll taxes), and ramp assumptions for quota-carrying roles. Model the difference between approved headcount and expected attainment. Deliverable: headcount budget model with phased costs.
4. **OpEx Consolidation**: Consolidate all operating expenses into a company-wide P&L budget. Categorize by GAAP line item (R&D, S&M, G&A) and by department. Apply the Rule of 40 or burn multiple as a top-level constraint. Deliverable: consolidated P&L budget with department-level detail.
5. **Cash Flow Budget**: Translate the P&L budget into a cash flow budget accounting for billing mix (monthly vs. annual), collections timing, vendor payment terms, and capex. Calculate ending cash and runway for each month. Deliverable: cash flow budget with monthly runway.
6. **Scenario Modelling**: Build upside (+15% revenue, +10% headcount) and downside (-20% revenue, hiring freeze) scenarios. Define the trigger criteria for moving between scenarios. Deliverable: scenario matrix with trigger thresholds.
7. **Board Approval Package**: Package the budget into a board-ready format with an executive summary, key assumptions, risks, and comparison to prior year. Deliverable: board budget presentation and supporting detail.

## Anti-Patterns

- **Peanut-butter spreading**: Distributing budget increases or cuts evenly across departments without considering strategic priority. *Why*: equal distribution ignores that some departments drive disproportionate ROI; budgets should reflect strategic bets.
- **Budgeting from last year plus a percentage**: Using prior-year actuals as the starting point and applying a blanket growth rate. *Why*: this perpetuates historical inefficiencies and prevents zero-based evaluation of whether each spend category earns its place.
- **Headcount without ramp modelling**: Budgeting for new hires at full-year cost without modelling start dates and ramp time. *Why*: a hire starting in Q3 costs half what a Q1 hire costs; failing to phase costs creates misleading OpEx projections.
- **Missing the cash dimension**: Building a P&L budget without a corresponding cash flow budget. *Why*: profitable budgets can still produce cash shortfalls if the billing mix or collections timing is unfavorable.

## Output

**On success**: Produces the annual operating budget containing the consolidated P&L, headcount plan, cash flow budget, scenario analysis, and board approval package. Delivered as a version-controlled model with supporting documentation.

**On failure**: Report which department budgets are incomplete, what preliminary consolidation exists, and what decisions or inputs are needed to finalize. Provide a timeline to completion with dependencies mapped.

## Related Skills

- [`rolling-forecast-updater`](../rolling-forecast-updater/SKILL.md) -- Updates the budget assumptions monthly as actuals replace projections.
- [`financial-model-v1`](../../cfo-vp-finance/financial-model-v1/SKILL.md) -- Provides the financial model framework that the budget builds upon.
