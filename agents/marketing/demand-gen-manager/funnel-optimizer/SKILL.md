---
name: funnel-optimizer
description: >
  This skill diagnoses conversion drop-offs across TOFU, MOFU, and BOFU stages by
  mapping funnel metrics against benchmarks, identifying friction points at each stage
  transition, and producing a prioritised optimisation roadmap. Use when pipeline
  velocity is slowing, MQL-to-SQL conversion is degrading, or top-of-funnel volume
  is not translating to closed revenue. Suggest when a paid campaign is generating
  impressions but no pipeline.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../../../marketing/demand-gen-manager/ad-campaign-builder/SKILL.md
  - ../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
  - ../../../marketing/marketing-operations-manager/marketing-attribution-modeller/SKILL.md
triggers:
  - "optimise the funnel"
  - "diagnose conversion drop-off"
  - "MQL to SQL conversion is low"
  - "pipeline is not converting"
  - "audit funnel performance"
---

# funnel-optimizer

## Agent: Demand Gen Manager

L2 Demand Gen Manager (1x) responsible for channel strategy, paid and organic demand generation, content distribution, and pipeline contribution from marketing programmes.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Diagnoses conversion performance across the full TOFU/MOFU/BOFU funnel by comparing stage metrics against benchmarks, identifying friction points at each transition, and producing a prioritised optimisation roadmap with specific interventions for each stage.

## When to Use

- When paid spend is increasing but pipeline generated is flat or declining.
- When MQL-to-SQL conversion rate drops below 15% for two or more consecutive weeks.
- When a new campaign has launched and early metrics show high impressions but low click-to-lead conversion.
- When the sales team reports that inbound leads are low quality or not converting to opportunities.
- When preparing a quarterly demand review and a full-funnel performance analysis is required.
- When post-launch metrics for a product or feature reveal that awareness is high but trial or demo requests are not materialising.

## Workflow

1. **Define funnel stages and metrics**: Map the specific funnel stages for this business — TOFU (impressions → sessions → leads), MOFU (leads → MQLs → SQLs), BOFU (SQLs → opportunities → closed-won). Confirm the definitions of each stage transition with the team. Reference `references/framework.md` for stage definitions and benchmark ranges. Deliverable: funnel stage map with metric definitions and owners.

2. **Pull current performance data**: Extract conversion rate data for each stage transition for the trailing 30, 60, and 90 days. Segment by channel, campaign, and content type where possible. Identify trend direction (improving, flat, declining) per stage. Deliverable: funnel performance snapshot table with trend indicators.

3. **Benchmark comparison**: Compare each stage conversion rate against the benchmarks in `references/framework.md` for the relevant industry and business model. Classify each stage as healthy (within benchmark), underperforming (10-25% below benchmark), or critical (more than 25% below benchmark). Deliverable: benchmark comparison table with RAG (Red/Amber/Green) status per stage.

4. **Friction identification at each stage**: For each underperforming or critical stage, apply the friction identification frameworks in `references/framework.md` to diagnose root causes. Distinguish between volume problems (not enough input at the top), conversion problems (leakage at a specific stage), and quality problems (wrong audience entering the funnel). Deliverable: friction diagnosis per stage with root cause hypotheses ranked by confidence.

5. **[GATE] Channel and content attribution**: Break down funnel performance by channel source. Identify which channels are contributing healthy-quality leads that convert through the funnel versus channels generating volume that stalls at MOFU or BOFU. Present attribution findings and confirm with stakeholders which channels should be scaled, held, or cut before proceeding. Deliverable: channel attribution heatmap showing conversion rate by channel at each stage.

6. **Intervention design**: For each friction point, design specific interventions. TOFU interventions: audience targeting adjustment, channel reallocation, messaging refinement. MOFU interventions: nurture sequence improvement, lead scoring recalibration, content gap filling. BOFU interventions: sales enablement content, follow-up sequence optimisation, offer or pricing adjustments. Each intervention must include a measurable success metric and an estimated effort level (low/medium/high). Deliverable: intervention list with stage, friction point, action, success metric, and effort rating.

7. **Prioritisation and roadmap**: Rank interventions using the impact/effort matrix — high impact, low effort interventions are immediate priorities. Group into a 30/60/90-day roadmap. Flag any interventions that require cross-functional coordination (e.g., sales process changes, product changes). Deliverable: prioritised 90-day optimisation roadmap.

8. **Report generation**: Compile all findings into the funnel optimisation report using `assets/funnel-optimization-report-template.md`. Include current state, benchmark gaps, friction diagnoses, intervention plan, and roadmap. Deliverable: funnel optimisation report ready for stakeholder review.

## Anti-Patterns

- **Optimising TOFU while ignoring BOFU leakage**: Increasing top-of-funnel volume when BOFU conversion is broken amplifies waste. *Why*: More leads entering a broken funnel generates more cost without more revenue.
- **Blaming volume for quality problems**: Attributing MOFU stall to insufficient lead volume when the real issue is audience targeting. *Why*: Adding volume that matches the wrong ICP compounds the problem instead of solving it.
- **Measuring conversion rate without segmenting by channel**: Reporting a single blended conversion rate that masks high-performing and low-performing channels. *Why*: Blended rates hide the truth; segmented rates reveal where to invest and where to cut.
- **Optimising for MQL volume over MQL quality**: Setting lead scoring thresholds low to inflate MQL counts reported to leadership. *Why*: High MQL volume with low SQL conversion destroys sales team trust in marketing and eventually leads to marketing budget cuts.
- **Making funnel changes without a control period**: Simultaneously changing multiple funnel variables (ad creative, landing page, lead form, nurture sequence) and then attributing improvement or decline to the wrong change. *Why*: Without a control period and single-variable testing, it is impossible to know what worked.

## Output

**On success**: Produces a funnel optimisation report (using `assets/funnel-optimization-report-template.md`) containing the current-state funnel snapshot, benchmark gap analysis, friction diagnoses by stage, channel attribution heatmap, intervention list, and 90-day roadmap. Delivered as a document ready for stakeholder review and programme execution.

**On failure**: Report which funnel stages could not be analysed and why (missing data, undefined stage transitions, no attribution tracking), what was attempted, and what data or tooling is required to complete the analysis. Every gap must be described as a specific ask.

## Related Skills

- [`ad-campaign-builder`](../../../marketing/demand-gen-manager/ad-campaign-builder/SKILL.md) — Campaign structure and targeting directly determine TOFU input quality; funnel analysis informs campaign adjustments.
- [`landing-page-auditor`](../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md) — Landing page friction is a primary cause of TOFU-to-MOFU conversion failure; audit findings feed directly into funnel interventions.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Analytics reporting provides the performance data inputs required for funnel diagnosis.
- [`marketing-attribution-modeller`](../../../marketing/marketing-operations-manager/marketing-attribution-modeller/SKILL.md) — Attribution models determine which channels receive credit for funnel conversions; model accuracy affects optimisation decisions.
