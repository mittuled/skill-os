# Framework: Revenue Funnel Analysis

Defines the metrics model, benchmarks, and analysis methodology for the full MQL → SQL → SQO → Closed-Won revenue funnel.

## Funnel Stage Definitions

| Stage | Definition | Conversion Event |
|-------|-----------|-----------------|
| MQL | Marketing Qualified Lead — meets ICP fit threshold and has met minimum engagement score | Lead score ≥ threshold; auto-promoted in CRM |
| SAL | Sales Accepted Lead — SDR reviewed and accepted; basic ICP confirmed | SDR updates status to "Accepted" |
| SQL | Sales Qualified Lead — discovery call completed; BANT partially confirmed | SDR converts to Opportunity or advances stage |
| SQO | Sales Qualified Opportunity — formal demo or proposal delivered; active evaluation | AE advances stage in CRM |
| Closed-Won | Contract signed; deal revenue recognised | Opportunity stage = "Closed-Won" |
| Closed-Lost | Evaluated but did not purchase; reason code recorded | Opportunity stage = "Closed-Lost" |

## Benchmark Conversion Rates (B2B SaaS)

| Stage Transition | Benchmark Conversion | Warning Signal |
|-----------------|---------------------|----------------|
| MQL → SAL | 60 – 75% | < 50% suggests ICP criteria misconfigured or lead quality low |
| SAL → SQL | 40 – 60% | < 30% suggests SDRs not qualifying effectively |
| SQL → SQO | 50 – 70% | < 40% suggests poor product-market fit messaging at demo |
| SQO → Closed-Won | 20 – 35% | < 15% suggests competitive, pricing, or timing issues |
| MQL → Closed-Won (end-to-end) | 5 – 15% | < 3% suggests systemic funnel failure |

## Velocity Metrics

| Stage | Benchmark Days in Stage | Warning Signal |
|-------|------------------------|----------------|
| MQL → SQL | 5 – 14 days | > 21 days: SDR follow-up lag or backlog |
| SQL → SQO | 7 – 21 days | > 30 days: sales cycle drag, demo scheduling delays |
| SQO → Closed-Won | 14 – 60 days | > 90 days: deal stall, legal or procurement bottleneck |

## Segmentation Dimensions

Segment every funnel analysis across all of the following dimensions before drawing conclusions:

| Dimension | Why It Matters |
|-----------|----------------|
| Deal size (SMB / Mid-Market / Enterprise) | Enterprise deals have longer cycles; aggregate metrics mask segment health |
| Lead source / channel | Channel quality varies; poor channels inflate volume without improving outcomes |
| Sales rep | Rep performance variation identifies coaching needs |
| Product / tier | Different products convert differently |
| Geography / territory | Regional variation may indicate market fit or competitive differences |
| Cohort (month of MQL creation) | Cohort analysis reveals whether recent performance is improving or declining |

## Bottleneck Severity Classification

| Conversion Gap vs. Benchmark | Severity | Recommended Action |
|------------------------------|----------|--------------------|
| Within 5% of benchmark | Normal | Monitor; no action required |
| 5 – 15% below benchmark | Watch | Investigate; look for segment-specific causes |
| 15 – 30% below benchmark | Warning | Prioritise root cause analysis; present findings to sales/marketing lead |
| > 30% below benchmark | Critical | Escalate to VP level; halt pipeline expansion until root cause resolved |
