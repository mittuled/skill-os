---
name: signal-synthesiser-data-p
description: >
  This skill synthesises post-launch data signals to inform the iteration backlog. Use when asked to analyse post-launch metrics, extract learnings from a release, or prioritize iteration work based on data. Also consider after a feature ships and the team needs data-backed next steps. Suggest when a post-launch review is scheduled without data preparation.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
  - signal-synthesiser-data
  - funnel-analyser
  - adoption-tracker-data
  - signal-synthesiser
---

# signal-synthesiser-data-p

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The post-launch signal synthesiser aggregates quantitative signals from the first 7-30 days after a feature release — adoption curves, funnel conversion, error rates, support ticket spikes — and distils them into a prioritized list of iteration candidates for the product backlog.

## When to Use

- When a feature has been live for 7-30 days and the team needs a data-backed assessment of its performance.
- When a post-launch review meeting is scheduled and requires prepared data synthesis.
- When the product team is deciding whether to iterate, scale, or sunset a recently launched feature.
- When support ticket volume spikes after a release and the team needs to correlate with behavioural data.

## Workflow

1. **Collect signals**: Pull adoption metrics, funnel conversion rates, error logs, latency data, support ticket counts, and NPS/CSAT scores for the launch period.
2. **Compare to targets**: Measure each signal against the pre-defined success criteria from the goal framework. Flag metrics that miss targets by more than 20%.
3. **Segment analysis**: Break key metrics by user cohort, platform, and acquisition channel. Identify segments where the feature performs well vs. poorly.
4. **Correlate with qualitative data**: Cross-reference quantitative signals with support tickets, user feedback, and session recordings to hypothesize root causes for underperformance.
5. **Prioritize iterations**: Rank potential improvements by expected metric impact and implementation effort. Produce a prioritized iteration backlog with data justification for each item.
6. **Deliver synthesis**: Present a one-page signal synthesis with key findings, metric performance vs. targets, root cause hypotheses, and the prioritized iteration list.

## Anti-Patterns

- **Premature synthesis**: Drawing conclusions from 48 hours of post-launch data before cohorts mature. *Why*: early adopters behave differently from mainstream users; patterns stabilize after 7-14 days.
- **Metrics without context**: Presenting numbers without qualitative context (user quotes, support themes) makes it hard to identify actionable improvements. *Why*: data tells you what happened; qualitative signals tell you why.
- **Ignoring null results**: Omitting metrics that met targets and reporting only failures biases the iteration backlog toward fixes instead of scaling what works. *Why*: doubling down on successful elements can be higher-leverage than fixing marginal ones.

## Output

**Success:**
- A post-launch signal synthesis containing metric performance vs. targets, cohort breakdowns, root cause hypotheses, and a prioritized iteration backlog with data justification per item.

**Failure:**
- Key post-launch metrics cannot be computed because instrumentation was incomplete. Report the gaps and recommend interim proxy metrics while instrumentation is remediated.

## Related Skills

- [`signal-synthesiser-data`](../signal-synthesiser-data/SKILL.md) -- the general signal synthesiser provides ongoing product health views; this skill focuses specifically on post-launch windows.
- [`funnel-analyser`](../funnel-analyser/SKILL.md) -- funnel analysis is a key input to post-launch synthesis.
- [`adoption-tracker-data`](../adoption-tracker-data/SKILL.md) -- adoption curves are a primary post-launch signal.
- [`signal-synthesiser`](../../product-operations-analyst/signal-synthesiser/SKILL.md) -- the product ops signal synthesiser incorporates operational signals alongside the data signals this skill produces.
