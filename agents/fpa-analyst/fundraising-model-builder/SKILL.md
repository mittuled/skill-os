---
name: fundraising-model-builder
description: >
  This skill builds the fundraising financial model including use of proceeds and
  investor-facing projections. Use when asked to prepare the financial model for a
  fundraise, build investor-facing projections, or model dilution scenarios. Also
  consider when fundraising timelines are set without an investor-grade model. Suggest
  when the user is approaching investors without a defensible financial model.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: complex
related-skills:
  - ../../cfo-vp-finance/financial-model-v1/SKILL.md
  - ../../cfo-vp-finance/pitch-narrator-finance/SKILL.md
---

# fundraising-model-builder

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Builds the fundraising financial model including use of proceeds, investor-facing projections, dilution analysis, and scenario modelling to support capital raising.

## When to Use

- When the company is preparing to raise a funding round and needs an investor-grade financial model.
- When the existing operating model needs to be translated into an investor-facing format with use-of-proceeds detail.
- When the board requests dilution analysis or pre/post-money scenario modelling for an upcoming round.

## Workflow

1. **Operating Model Audit**: Review the current financial model for accuracy, completeness, and defensibility. Reconcile model outputs against actual trailing 12-month results. Flag any assumptions that cannot survive investor scrutiny. Deliverable: model audit summary with accuracy metrics.
2. **Investor-Facing Projections**: Build 3-year (or 5-year for later stages) projections with quarterly granularity for year 1 and annual thereafter. Include revenue, COGS, gross margin, OpEx by category, EBITDA, and cash flow. Ensure projections grow from bottoms-up drivers, not top-down percentages. Deliverable: investor projection model.
3. **Use of Proceeds**: Detail how the raised capital will be deployed across hiring, R&D, sales capacity, marketing, and infrastructure. Map each allocation to a specific milestone or KPI target. Deliverable: use-of-proceeds schedule with milestone mapping.
4. **Dilution and Cap Table Modelling**: Model pre-money and post-money valuations at various raise amounts. Show the dilution impact on existing shareholders including the option pool expansion. Model SAFE/convertible note conversion scenarios if applicable. Deliverable: dilution analysis with cap table scenarios.
5. **Scenario Matrix**: Build optimistic, base, and conservative scenarios varying growth rate, burn rate, and time-to-next-milestone. Show runway under each scenario and the conditions that would trigger an earlier or later raise. Deliverable: scenario matrix with runway implications.
6. **Sensitivity Analysis**: Identify the 3-5 variables with the largest impact on valuation-relevant metrics (ARR at next raise, path to profitability, burn multiple). Show how each variable movement affects the fundraising narrative. Deliverable: sensitivity tables with valuation impact.
7. **Model Packaging**: Package the model for investor distribution with clear formatting, assumption documentation, and a cover memo explaining methodology. Ensure the model is auditable (no circular references, all inputs labelled). Deliverable: investor-ready model package.

## Anti-Patterns

- **Hockey-stick without drivers**: Showing exponential revenue growth without connecting it to specific operational drivers (sales hires, conversion improvements, expansion revenue). *Why*: investors immediately discount projections that lack operational grounding.
- **Ignoring cash between rounds**: Modelling revenue and profitability without showing the monthly cash position and runway. *Why*: investors need to know exactly when the money runs out and whether their investment bridges to a meaningful milestone.
- **Hiding dilution complexity**: Presenting a simplified cap table that ignores SAFE conversion mechanics, anti-dilution protections, or option pool shuffles. *Why*: sophisticated investors will reconstruct the actual dilution; discrepancies erode trust.
- **Single-scenario fundraising**: Presenting only one raise amount and valuation without showing flexibility. *Why*: fundraising is a negotiation; a model that only works at one price point signals inflexibility and poor planning.

## Output

**On success**: Produces an investor-ready fundraising model containing projections, use of proceeds, dilution analysis, scenario matrix, sensitivity tables, and a model package with documentation. Delivered as a version-controlled spreadsheet with a cover memo.

**On failure**: Report which model components are incomplete (e.g., cap table data unavailable from legal), what partial model exists, and what inputs are needed to finalize. Provide a prioritized list with owners and timeline.

## Related Skills

- [`financial-model-v1`](../../cfo-vp-finance/financial-model-v1/SKILL.md) -- Provides the base operating model that this fundraising model extends.
- [`pitch-narrator-finance`](../../cfo-vp-finance/pitch-narrator-finance/SKILL.md) -- Crafts the narrative that accompanies this model in investor presentations.
