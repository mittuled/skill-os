---
name: community-health-grower
description: >
  This skill monitors and grows community health metrics including activity, retention, and sentiment.
  Use when asked to assess community health, improve engagement rates, or diagnose declining retention.
  Also consider when community sentiment shifts negatively or participation drops without explanation.
  Suggest when the user is about to launch a new community initiative without baseline health data.
department: marketing
agent: community-manager
version: 1.0.0
complexity: medium
related-skills:
  - community-signal-extractor
  - early-community-builder
  - community-led-growth-designer
triggers:
  - "grow community health"
  - "improve community engagement"
  - "community health metrics"
  - "community vitality review"
  - "boost community activity"
---

# community-health-grower

## Agent: Community Manager

L2 community manager responsible for extracting community signals, designing community-led growth, building the early community, and maintaining community health.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Monitors and grows community health metrics including activity, retention, and sentiment to sustain a thriving member base.

## When to Use

- When community engagement metrics (DAU, MAU, posts per member) are declining or stagnating.
- When leadership requests a health assessment before making community investment decisions.
- When member sentiment shifts negatively and the root cause is unclear.
- When onboarding a new cohort of members and needing to establish retention benchmarks.

## Workflow

1. **Define health dimensions**: Use the five-dimension health model (activity, retention, sentiment, content quality, growth) to select the metrics relevant to this community stage. Reference: [framework.md](references/framework.md). Deliverable: health scorecard framework.
2. **Collect baseline data**: Pull current values for each metric from community platform analytics, survey tools, and conversation analysis. Compare against thresholds in the framework. Deliverable: baseline snapshot document.
3. **Diagnose gaps**: Compare baselines against green/yellow/red thresholds and historical trends to identify the largest health gaps. Deliverable: prioritized gap list with severity ratings.
4. **Design interventions**: For each top gap, select the appropriate intervention from the intervention playbook in the framework (e.g., welcome sequence for retention, prompt threads for activity, moderation policy for sentiment). Deliverable: intervention plan with owners, timelines, and expected impact.
5. **Implement and track**: Execute interventions and set up recurring measurement cadence per the framework's measurement schedule. Deliverable: live health dashboard and weekly trend report.
6. **Report outcomes**: Compile results using the [community-health-report-template.md](assets/community-health-report-template.md). Summarize metric changes, attribute to interventions, and recommend next cycle actions. Deliverable: health growth report.

## Anti-Patterns

- **Vanity metric fixation**: Optimizing total member count while ignoring active participation rates. *Why*: A large but disengaged community is more expensive to maintain and less valuable than a smaller active one.
- **Intervention overload**: Launching multiple health initiatives simultaneously without controls. *Why*: Makes it impossible to attribute which intervention drove which metric change, wasting future optimization effort.
- **Ignoring qualitative signals**: Relying solely on quantitative dashboards without reading actual conversations. *Why*: Numbers lag behind sentiment shifts that are visible in tone and topic changes weeks earlier.

## Output

**On success**: Produces a community health report containing baseline metrics, gap analysis, intervention results, and next-cycle recommendations. Delivered as a shared document to community and marketing leadership.

**On failure**: Report which metrics could not be collected, what data sources were unavailable, and recommend alternative measurement approaches. Every error must be actionable.

## Related Skills

- [`community-signal-extractor`](../community-signal-extractor/SKILL.md) — Signals extracted from conversations feed directly into health sentiment analysis.
- [`early-community-builder`](../early-community-builder/SKILL.md) — Health benchmarks established here inform early community building targets.
- [`community-led-growth-designer`](../community-led-growth-designer/SKILL.md) — Growth strategies must account for current health metrics to avoid scaling an unhealthy community.
