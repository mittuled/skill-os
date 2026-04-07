# Framework: Signal Synthesis

## Core Model

Signal synthesis converts raw data from multiple sources into a ranked list of actionable product insights, distinguishing confirmed trends from noise and flagging where sources conflict or a single source is over-amplifying a concern.

## Signal Source Inventory

| Source | Signal Type | Reliability | Frequency |
|--------|------------|------------|-----------|
| Usage analytics | Behavioural truth | High (quantitative) | Continuous |
| Support tickets | Friction and bugs | Medium (biased toward reactive users) | Continuous |
| NPS/CSAT verbatims | Sentiment themes | Medium (biased toward extremes) | Monthly |
| Sales call recordings/notes | Objections, feature gaps | Medium (biased toward prospects) | Weekly |
| CS check-in notes | Adoption blockers, churn risk | High (direct customer relationship) | Bi-weekly |
| In-app feedback | Feature-specific friction | Medium (self-selected) | Continuous |
| Community / social | Public sentiment | Low (vocal minority) | Weekly |

## Signal Strength Classification

Classify each signal before synthesis:

| Strength | Criteria | Action |
|----------|---------|--------|
| Confirmed | 3+ independent sources; supported by quantitative data | Include in synthesis; flag as high-confidence |
| Emerging | 2 sources; qualitative only | Include with confidence caveat |
| Noise | Single source; contradicted by data | Log but do not synthesise; monitor for recurrence |
| Conflicting | Multiple sources disagree directionally | Surface as an open question; do not synthesise to a conclusion |

## Synthesis Process

1. **Collect**: Gather raw signals from all active sources for the period
2. **Tag**: Apply type, severity, segment, and source tags to each signal item
3. **Cluster**: Group items by theme (e.g., "export friction", "onboarding drop-off")
4. **Score**: Apply signal strength classification to each cluster
5. **Rank**: Order confirmed clusters by frequency × severity × strategic importance
6. **Conflict-flag**: Surface any clusters where sources point in opposite directions
7. **Recommend**: For each top-3 confirmed cluster, propose a specific action

## Theme Naming Convention

Name themes in plain language that describes the user experience, not the technical cause:
- "Users cannot export to CSV without errors" (good)
- "Export bug in data pipeline" (bad — engineering framing, not user framing)

## Conflicting Signal Protocol

When two sources disagree (e.g., usage data shows feature is used heavily, but NPS verbatims call it confusing):
1. Do not reconcile by averaging — surface both findings explicitly
2. Propose a resolution question ("Are the heavy users a segment that has adapted to the friction, while new users struggle?")
3. Recommend a targeted investigation (session replay, user interview, cohort split analysis)

## Output Quality Standard

A synthesis output is complete when:
- [ ] All active signal sources have been reviewed
- [ ] Every claim is tagged with source and strength
- [ ] Top 3 themes are ranked with rationale
- [ ] Conflicting signals are explicitly called out
- [ ] Each theme has a recommended action (or explicitly states "more data needed")
