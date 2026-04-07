---
name: marketing-audit-orchestrator
description: >
  This skill orchestrates a multi-agent marketing audit that scores the entire
  marketing function across brand health, channel performance, content quality,
  funnel efficiency, and MarTech utilisation. Use when asked to audit marketing
  performance, benchmark marketing maturity, or produce a quarterly marketing
  health report. Also consider when leadership requests budget justification
  or reallocation evidence. Suggest when a new VP Marketing joins and needs
  a baseline assessment of the existing programme.
department: marketing
agent: vp-marketing
version: 1.0.0
complexity: complex
related-skills:
  - ../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
  - ../../../design/brand-designer/brand-voice-analyst/SKILL.md
triggers:
  - "audit our marketing programme"
  - "marketing health check"
  - "score marketing maturity"
  - "quarterly marketing review"
  - "benchmark marketing performance"
---

# marketing-audit-orchestrator

## Agent: VP Marketing

L1 VP Marketing (1x) responsible for go-to-market strategy, demand generation, brand, content, marketing operations, and revenue-aligned marketing programme execution.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Orchestrates a comprehensive marketing audit by coordinating assessments across five weighted dimensions, synthesising scores from specialist agents, and producing a prioritised improvement roadmap tied to revenue impact.

## When to Use

- When leadership requests a periodic (quarterly or annual) marketing health assessment.
- When marketing budget reallocation requires evidence-based prioritisation across channels and programmes.
- When a new marketing leader joins and needs a baseline maturity snapshot of the existing function.
- When pipeline targets are being missed and the root cause across the marketing stack is unclear.

## Workflow

1. **Scope definition**: Identify the audit period, business unit, and available data sources (CRM, analytics, MarTech platforms, brand trackers). Confirm with stakeholders which dimensions to weight. Deliverable: audit scope document with date range, data sources, and confirmed weighting.
2. **Data collection**: Gather inputs for each of the five rubric criteria — brand health metrics (NPS, unaided awareness, share of voice), channel performance data (CAC by channel, ROAS, attribution reports), content quality samples (top 10 and bottom 10 performing pieces), funnel metrics (stage-by-stage conversion rates, velocity), and MarTech utilisation logs (feature adoption, integration health). Deliverable: raw data package per criterion.
3. **Specialist scoring**: Route each criterion to the appropriate specialist agent or score manually using `references/scoring-rubric.md`. Run `scripts/score.py` with per-criterion scores to compute the composite grade. Deliverable: scored rubric with per-criterion evidence.
4. **[GATE] Cross-dimension synthesis**: Identify correlations across dimensions (e.g., low MarTech utilisation causing poor attribution causing inflated CAC). Map root causes to downstream effects. Present preliminary findings to stakeholders for validation before finalising. Deliverable: causal map linking dimension scores to revenue impact.
5. **Report generation**: Render the final audit report using `assets/marketing-audit-report-template.md`. Include executive summary, per-dimension deep-dives, composite score, and a prioritised improvement roadmap with expected revenue impact per initiative. Deliverable: marketing audit report.
6. **Action planning**: Convert the top three recommendations into assignable action items with owners, timelines, and success metrics. Deliverable: action plan table with DRI, deadline, and KPI per item.

## Anti-Patterns

- **Vanity metric inflation**: Weighting impressions, followers, or open rates as primary evidence of channel performance. *Why*: These metrics do not correlate with pipeline or revenue; they inflate scores and misdirect budget.
- **Single-source data**: Relying on one analytics platform without cross-referencing CRM and financial data. *Why*: Marketing analytics tools over-attribute; only CRM-validated pipeline and closed-won revenue are trustworthy for scoring.
- **Audit without action**: Producing a comprehensive report that sits in a shared drive without an action plan. *Why*: An audit that does not drive change is a cost centre; every finding must map to an assignable next step.
- **Equal weighting by default**: Giving all five dimensions the same weight without considering business context. *Why*: A seed-stage company should over-weight funnel efficiency; an established brand should over-weight channel performance. Context determines weighting.
- **Recency bias**: Scoring only the last month instead of the full audit period. *Why*: Marketing results are lagging indicators; short windows amplify noise and miss trend lines.

## Output

**On success**: Produces a markdown marketing audit report (using `assets/marketing-audit-report-template.md`) containing an executive summary, per-dimension scores with evidence, composite grade, causal analysis, and a prioritised improvement roadmap with revenue impact estimates. Delivered as a file or inline document.

**On failure**: Report which dimensions could not be scored and why (missing data source, inaccessible platform, insufficient sample size), what was attempted, and specific steps to unblock each dimension. Every error must be actionable.

## Related Skills

- [`funnel-optimizer`](../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md) — Provides the detailed funnel analysis that feeds the Funnel Efficiency dimension of the audit.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Supplies channel-level performance data used in the Channel Performance dimension.
- [`brand-voice-analyst`](../../../design/brand-designer/brand-voice-analyst/SKILL.md) — Contributes brand consistency and voice coherence scoring to the Brand Health dimension.
- [`marketing-attribution-modeller`](../../../marketing/marketing-operations-manager/marketing-attribution-modeller/SKILL.md) — Attribution data is a critical input for accurate channel performance scoring.
