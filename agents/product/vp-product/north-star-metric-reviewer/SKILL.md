---
name: north-star-metric-reviewer
description: >
  This skill reviews whether the north-star metric still accurately reflects product and business
  goals, recommending adjustments when the metric drifts from value delivery. Use when a quarterly
  planning cycle begins and the team needs to validate metric alignment. Also consider when a major
  pivot, new product line, or pricing model change makes the current metric suspect. Suggest when
  teams are optimizing for the north star but user outcomes or revenue are not improving.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills:
  - business-model-sketcher
  - competitive-response-monitor
  - goal-framer
triggers:
  - "review north star metric"
  - "north star review"
  - "nsm review"
  - "evaluate north star"
  - "north star metric"
---

# north-star-metric-reviewer

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Reviews whether the north-star metric still accurately reflects product and business goals, and recommends recalibration when alignment has degraded.

## When to Use
- When entering a new planning cycle and the current north-star metric needs validation
- When product strategy has shifted (new persona, new market segment, pricing change) and the metric may no longer capture value delivery
- When the north star is trending positively but downstream business metrics (revenue, retention, NPS) are flat or declining
- When multiple teams are Goodharting the metric -- optimizing the number without improving actual user outcomes

## Workflow
1. **Retrieve current metric definition**: Document the existing north-star metric, its formula, data source, measurement cadence, and the strategic rationale from when it was adopted. Deliverable: metric definition card.
2. **Assess strategic alignment**: Compare the metric against current company objectives, product vision, and ICP definition. Identify any drift between what the metric measures and what the business now values. Deliverable: alignment gap analysis.
3. **Analyze leading and lagging indicators**: Check whether movements in the north star reliably predict improvements in retention, revenue, and customer satisfaction. Deliverable: correlation analysis summary with directional confidence.
4. **Evaluate Goodhart risk**: Look for evidence that teams are gaming the metric -- e.g., inflating activation counts without genuine engagement, or boosting usage through notifications rather than product value. Deliverable: Goodhart risk assessment with specific examples.
5. **Propose recommendation**: Either reaffirm the current metric with rationale, recommend a revised metric with migration plan, or suggest a composite indicator. Deliverable: recommendation memo with proposed metric, measurement plan, and transition timeline.
6. **Socialize and ratify**: Present findings to leadership and team leads. Incorporate feedback, resolve objections, and lock the metric for the upcoming cycle. Deliverable: ratified metric decision record.

## Anti-Patterns
- **Metric inertia**: Keeping a north-star metric simply because it was chosen at founding without re-evaluating fit. *Why*: Products evolve; a metric that captured early traction (e.g., sign-ups) may be meaningless at scale when retention matters more.
- **Vanity north star**: Choosing a metric that always goes up (e.g., cumulative users) rather than one that reflects ongoing value delivery. *Why*: Vanity metrics mask churn, mask engagement decay, and give false confidence to leadership.
- **Metric churn**: Changing the north star every quarter, preventing teams from building intuition or establishing baselines. *Why*: Frequent changes destroy longitudinal comparability and erode team trust in the planning process.
- **Ignoring input metrics**: Reviewing only the north star without examining the input metrics that drive it. *Why*: A healthy top-line number can hide compensating failures in underlying drivers.

## Output
**On success**: A ratified metric decision record confirming or updating the north-star metric, including formula, data source, measurement cadence, target range, and transition plan if the metric changed.
**On failure**: Report which data was unavailable for correlation analysis, what strategic ambiguities prevented alignment assessment, and recommend specific clarifications needed from leadership before the review can be completed.

## Related Skills
- [`business-model-sketcher`](../business-model-sketcher/SKILL.md) — sibling skill under the same agent — combine with business-model-sketcher for end-to-end coverage
- [`competitive-response-monitor`](../competitive-response-monitor/SKILL.md) — sibling skill under the same agent — combine with competitive-response-monitor for end-to-end coverage
- [`goal-framer`](../goal-framer/SKILL.md) — sibling skill under the same agent — combine with goal-framer for end-to-end coverage
