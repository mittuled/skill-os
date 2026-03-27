---
name: mvp-definer-growth
description: >
  This skill defines MVP growth experiments to validate acquisition and activation hypotheses. Use when asked to design a growth experiment, define a minimum viable test, or scope the first growth sprint. Also consider when the growth model has untested assumptions. Suggest when the team wants to scale a channel before running a validation experiment.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
  - growth-model-designer
  - activation-signal-definer
  - statistical-significance-tracker
---

# mvp-definer-growth

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The MVP growth definer scopes the smallest possible experiments that can validate or invalidate the growth model's key assumptions — channel CAC, activation rate, viral coefficient — before committing resources to full-scale execution.

## When to Use

- When the growth model contains untested assumptions about channel economics or activation rates.
- When a new acquisition channel is proposed and needs a minimum viable test before budget allocation.
- When the team plans the first growth sprint and needs to prioritize which hypotheses to test.
- When a growth initiative has been running without clear experiment structure or success criteria.

## Workflow

1. **Extract assumptions**: List the top 5 assumptions in the growth model ranked by uncertainty and impact. Each assumption becomes a candidate experiment.
2. **Define hypotheses**: For each assumption, write a falsifiable hypothesis: "We believe [channel/mechanic] will produce [metric] at [threshold] because [rationale]."
3. **Scope minimum viable test**: Design the smallest experiment that can validate the hypothesis. Define the sample size, duration, budget cap, and success/failure threshold.
4. **Calculate required sample**: Use power analysis to determine the minimum sample size for the target MDE (minimum detectable effect) at 80% power and 95% confidence.
5. **Prioritize experiments**: Rank by learning value (which assumption, if wrong, most endangers the growth model) divided by cost (time + budget). Run the highest-value experiments first.
6. **Deliver experiment briefs**: Produce a one-page brief per experiment with hypothesis, test design, success criteria, sample size, budget, timeline, and kill criteria.

## Anti-Patterns

- **Over-scoping the MVP test**: Running a full campaign instead of a minimum viable test consumes budget that could validate three other assumptions. *Why*: the goal is learning, not performance; keep tests as small as statistical validity allows.
- **No kill criteria**: Running experiments without pre-defined failure thresholds leads to indefinite continuation of losing tests. *Why*: sunk cost bias keeps bad experiments running; kill criteria enforce disciplined capital allocation.
- **Testing everything at once**: Running all experiments simultaneously makes it impossible to attribute results when they interact. *Why*: concurrent experiments on overlapping audiences produce confounded results.

## Output

**Success:**
- A set of experiment briefs (1 per hypothesis) with falsifiable hypotheses, test designs, sample size calculations, budgets, timelines, and kill criteria.

**Failure:**
- The hypothesis cannot be tested at minimum viable scale due to insufficient traffic or budget. Report the constraint, the minimum required scale, and recommend a proxy test or qualitative validation approach.

## Related Skills

- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model's assumptions generate the hypotheses this skill tests.
- [`activation-signal-definer`](../activation-signal-definer/SKILL.md) -- activation rate is a common hypothesis requiring MVP validation.
- [`statistical-significance-tracker`](../../analytics-lead/statistical-significance-tracker/SKILL.md) -- tracks significance of the experiments this skill defines.
