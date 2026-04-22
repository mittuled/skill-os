---
name: goal-framer
description: >
  This skill defines measurable product goals aligned to business outcomes for a given initiative.
  Use when a new initiative needs explicit success criteria before work begins.
  Also consider when existing goals feel vague, lack baselines, or don't connect to revenue/retention metrics.
  Suggest when a team is about to kick off discovery or planning without articulated OKRs or North Star metrics.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills:
  - assumption-mapper
  - business-model-sketcher
  - competitive-response-monitor
  - design-partner-programme-builder
  - gate-12-evaluator
  - prd-assembler
  - idea-critic
  - launch-coordinator
  - moat-analyzer
  - mvp-definer
  - north-star-metric-reviewer
  - opportunity-framer
  - packaging-designer
  - pitch-narrator
  - pricing-v1-setter
  - product-feedback-ingestion
  - sla-definer
triggers:
  - "frame product goals"
  - "goal framing"
  - "define product goals"
  - "product goal setting"
  - "frame goals"
---

# goal-framer

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Defines measurable product goals aligned to business outcomes for a given initiative.

## When to Use
- When a new initiative enters the roadmap and needs quantified success criteria before discovery begins
- When stakeholders disagree on what "success" looks like and the team needs a shared goal framework
- When post-launch metrics are missing or disconnected from company-level KPIs and need realignment

## Workflow
1. **Identify business context**: Review the company strategy, quarterly OKRs, and the initiative brief to understand which business lever the initiative targets. Deliverable: one-paragraph context summary linking the initiative to a top-level company objective.
2. **Define the North Star metric**: Select a single leading indicator that captures the core value the initiative delivers to users. Validate it passes the "can we move this in 90 days?" test. Deliverable: named metric with current baseline and measurement method.
3. **Set supporting metrics**: Choose 2-4 input metrics that drive the North Star — e.g., activation rate, time-to-value, retention at day-7. Assign directional targets (increase/decrease) and numeric thresholds. Deliverable: metric table with name, baseline, target, owner, and cadence.
4. **Define guardrail metrics**: Identify 1-2 metrics that must not degrade as a side effect — e.g., support ticket volume, page load time. Set acceptable bounds. Deliverable: guardrail list appended to the metric table.
5. **Validate with stakeholders**: Walk engineering, design, and business leads through the goal framework. Confirm feasibility of measurement and alignment on targets. Deliverable: sign-off record or revision notes.

## Anti-Patterns
- **Vanity metrics as goals**: Setting targets on page views or raw signups without tying them to retention or revenue. *Why*: These inflate perceived progress while masking real product health.
- **Goal overload**: Defining 8+ metrics so every outcome looks like a win. *Why*: Diffuses team focus and makes trade-off decisions impossible.
- **Missing baselines**: Setting a target of "20% improvement" without knowing the current number. *Why*: Makes the goal unmeasurable and impossible to track progress against.

## Output
**On success**: A goal framework document containing the North Star metric, 2-4 supporting metrics with baselines and targets, guardrail metrics, and stakeholder sign-off — formatted as a table suitable for embedding in a PRD or initiative brief.
**On failure**: Report which elements are incomplete (missing baselines, unvalidated measurement method, lack of stakeholder alignment), what was attempted, and recommend specific data pulls or stakeholder conversations needed to close the gaps.

## Related Skills
- [`assumption-mapper`](../assumption-mapper/SKILL.md) — sibling skill under the same agent — combine with assumption-mapper for end-to-end coverage
- [`business-model-sketcher`](../business-model-sketcher/SKILL.md) — sibling skill under the same agent — combine with business-model-sketcher for end-to-end coverage
- [`competitive-response-monitor`](../competitive-response-monitor/SKILL.md) — sibling skill under the same agent — combine with competitive-response-monitor for end-to-end coverage
- [`design-partner-programme-builder`](../design-partner-programme-builder/SKILL.md) — sibling skill under the same agent — combine with design-partner-programme-builder for end-to-end coverage
- [`gate-12-evaluator`](../gate-12-evaluator/SKILL.md) — sibling skill under the same agent — combine with gate-12-evaluator for end-to-end coverage
- [`prd-assembler`](../prd-assembler/SKILL.md) — sibling skill under the same agent — combine with prd-assembler for end-to-end coverage
- [`idea-critic`](../idea-critic/SKILL.md) — sibling skill under the same agent — combine with idea-critic for end-to-end coverage
- [`launch-coordinator`](../launch-coordinator/SKILL.md) — sibling skill under the same agent — combine with launch-coordinator for end-to-end coverage
- [`moat-analyzer`](../moat-analyzer/SKILL.md) — sibling skill under the same agent — combine with moat-analyzer for end-to-end coverage
- [`mvp-definer`](../mvp-definer/SKILL.md) — sibling skill under the same agent — combine with mvp-definer for end-to-end coverage
- [`north-star-metric-reviewer`](../north-star-metric-reviewer/SKILL.md) — sibling skill under the same agent — combine with north-star-metric-reviewer for end-to-end coverage
- [`opportunity-framer`](../opportunity-framer/SKILL.md) — sibling skill under the same agent — combine with opportunity-framer for end-to-end coverage
- [`packaging-designer`](../packaging-designer/SKILL.md) — sibling skill under the same agent — combine with packaging-designer for end-to-end coverage
- [`pitch-narrator`](../pitch-narrator/SKILL.md) — sibling skill under the same agent — combine with pitch-narrator for end-to-end coverage
- [`pricing-v1-setter`](../pricing-v1-setter/SKILL.md) — sibling skill under the same agent — combine with pricing-v1-setter for end-to-end coverage
- [`product-feedback-ingestion`](../product-feedback-ingestion/SKILL.md) — sibling skill under the same agent — combine with product-feedback-ingestion for end-to-end coverage
- [`sla-definer`](../sla-definer/SKILL.md) — sibling skill under the same agent — combine with sla-definer for end-to-end coverage
