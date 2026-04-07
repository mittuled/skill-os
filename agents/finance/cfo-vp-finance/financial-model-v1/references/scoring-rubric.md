# Scoring Rubric: Financial Model V1

Evaluates the completeness, accuracy, and defensibility of the initial financial model across revenue architecture, cost modelling, cash flow construction, and scenario analysis.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Revenue Architecture | 25% | Quality of revenue model structure: driver definitions, bottoms-up build, cohort modelling |
| 2 | Cost Structure Accuracy | 20% | Completeness of COGS and OpEx modelling: headcount-driven costs, gross margin derivation |
| 3 | Cash Flow Construction | 20% | Accuracy of cash conversion modelling: billing mix, DSO, payment timing, runway calculation |
| 4 | SaaS Metrics Integration | 15% | Correctness of derived metrics: ARR, NRR, LTV/CAC, burn multiple with documented methodology |
| 5 | Scenario Framework | 20% | Quality of scenario analysis: driver sensitivity, trigger definitions, management actions |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Model has complete bottoms-up revenue build, accurate cash flow, integrated SaaS metrics, and multi-scenario framework with trigger definitions | Approve for investor distribution and board reporting |
| A | 8.0 – 8.9 | Strong | Comprehensive model with minor gaps in scenario triggers or metric documentation | Approve with follow-up documentation within one week |
| B | 7.0 – 7.9 | Good | Solid revenue and cost modelling but cash flow timing or scenario analysis needs strengthening | Approve for internal use; remediate before investor distribution |
| C | 5.0 – 6.9 | Adequate | Core P&L model exists but missing cohort-level detail, cash flow model, or scenario framework | Revise model; not suitable for fundraising or board-level decisions |
| D | 3.0 – 4.9 | Weak | Incomplete model with top-down-only revenue, missing cost categories, or no cash flow | Rework from revenue architecture stage with FP&A support |
| F | 0.0 – 2.9 | Failing | No structured financial model or only a single-tab spreadsheet with hardcoded numbers | Commission a full model build before any financial decisions |

## Signal Tables

### Revenue Architecture
| Score | Evidence |
|-------|----------|
| 9-10 | Revenue streams mapped to specific drivers (customers x ACV, seats x price); monthly cohorts for 24 months with quarterly extension to month 60; expansion and contraction modelled separately |
| 7-8 | Bottoms-up build with driver definitions; cohort model present but missing expansion/contraction detail |
| 5-6 | Revenue forecast exists but uses top-down TAM percentages without bottoms-up validation |
| 3-4 | Single revenue line with growth rate assumption; no driver decomposition or cohort structure |
| 0-2 | No revenue model or only a single annual number without monthly granularity |

### Cost Structure Accuracy
| Score | Evidence |
|-------|----------|
| 9-10 | COGS itemized (hosting, support, APIs); OpEx by department with headcount-driven and non-headcount lines; SBC separated; gross margin derived correctly |
| 7-8 | Cost structure modelled by category with headcount plan; minor gaps in COGS detail or SBC treatment |
| 5-6 | OpEx modelled at department level but COGS is a single percentage assumption; headcount not phased |
| 3-4 | Costs modelled as a percentage of revenue without underlying driver analysis |
| 0-2 | No cost model or only total OpEx as a single line |

### Cash Flow Construction
| Score | Evidence |
|-------|----------|
| 9-10 | Cash flow accounts for billing frequency mix, DSO assumptions, vendor payment terms, and capex; monthly granularity for 24 months; cash conversion cycle documented |
| 7-8 | Cash flow model present with billing and collections timing; minor gaps in vendor payment or capex modelling |
| 5-6 | Basic cash flow statement exists but assumes cash equals revenue recognition timing |
| 3-4 | Cash position calculated as cumulative P&L without timing adjustments |
| 0-2 | No cash flow model; runway calculated from bank balance divided by monthly burn |

### SaaS Metrics Integration
| Score | Evidence |
|-------|----------|
| 9-10 | ARR, MRR, NRR, gross churn, LTV/CAC, CAC payback, burn multiple all calculated with documented formulas; methodology aligned with industry standards |
| 7-8 | Key SaaS metrics calculated correctly; minor gaps in documentation or one metric missing |
| 5-6 | Some metrics present but formulas not documented or inconsistent with industry definitions |
| 3-4 | Only ARR and burn rate calculated; no unit economics integration |
| 0-2 | No SaaS metrics derived from the model |

### Scenario Framework
| Score | Evidence |
|-------|----------|
| 9-10 | Best/base/worst scenarios with 3-5 varied drivers; explicit trigger definitions for scenario transitions; management action plans documented for each |
| 7-8 | Three scenarios with varied drivers; triggers partially defined; management actions noted but not detailed |
| 5-6 | Multiple scenarios exist but only vary growth rate; no trigger definitions or management actions |
| 3-4 | Only a base case with one sensitivity toggle |
| 0-2 | No scenario analysis; single-point forecast only |
