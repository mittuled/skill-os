---
name: revenue-funnel-analyst
description: >
  This skill analyses the full revenue funnel from lead to renewal to identify conversion bottlenecks.
  Use when asked to diagnose pipeline health, identify conversion drops, or forecast revenue.
  Also consider when win rates decline without a clear cause.
  Suggest when quarterly planning needs data-driven pipeline insights.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "analyze revenue funnel"
  - "funnel conversion analysis"
  - "diagnose funnel drop-off"
  - "pipeline stage analysis"
  - "revenue funnel report"
---

# revenue-funnel-analyst

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)

## Skill Description

The revenue funnel analyst examines conversion rates, velocity, and deal progression across every stage of the revenue funnel from lead to renewal to identify bottlenecks, forecast revenue, and recommend operational improvements.

## When to Use

- When win rates decline and leadership needs to understand where deals are stalling.
- When quarterly planning requires a data-driven view of pipeline health and revenue forecast.
- When a new sales motion or pricing change needs post-launch funnel impact analysis.
- When marketing and sales alignment meetings need shared funnel metrics as a foundation.

## Workflow

1. **Extract funnel data**: Pull deal-level data from the CRM covering all pipeline stages, conversion timestamps, deal values, and outcomes. Deliverable: raw funnel dataset.
2. **Calculate stage metrics**: Compute conversion rates, average time-in-stage, and deal velocity for each pipeline stage. Deliverable: stage-level metrics table.
3. **Identify bottlenecks**: Flag stages with below-benchmark conversion rates or abnormal time-in-stage. Deliverable: bottleneck analysis with severity ranking.
4. **Segment the analysis**: Break down funnel performance by segment (deal size, source, rep, product) to isolate root causes. Deliverable: segmented funnel analysis.
5. **Recommend improvements**: Propose specific operational changes to address each bottleneck (e.g., better qualification criteria, faster legal review). Deliverable: improvement recommendation report.

## Anti-Patterns

- **Analysing without segmentation**: Looking at aggregate funnel metrics without slicing by segment. *Why*: aggregate metrics hide segment-specific problems; a healthy overall conversion rate can mask a failing product line.
- **Funnel analysis without time context**: Comparing current funnel metrics to no baseline. *Why*: without historical comparison, it is impossible to determine whether current performance is improving or declining.
- **Treating symptoms as causes**: Recommending "more leads" when the real bottleneck is mid-funnel conversion. *Why*: pouring more volume into a leaky funnel wastes acquisition spend without improving revenue.

## Output

**On success**: A funnel analysis report with stage-level conversion rates, identified bottlenecks with severity, segmented analysis, and specific improvement recommendations with expected impact.

**On failure**: Report which data gaps prevented full analysis (e.g., missing stage timestamps, inconsistent deal categorisation), what partial analysis was completed, and recommend data hygiene improvements.

## Related Skills

- [`revenue-attribution-monitor`](../revenue-attribution-monitor/SKILL.md) -- attribution data enriches funnel analysis by showing which channels drive the best-converting leads.
- [`revenue-model-operationaliser`](../revenue-model-operationaliser/SKILL.md) -- the revenue model defines the funnel stages that this skill analyses.
