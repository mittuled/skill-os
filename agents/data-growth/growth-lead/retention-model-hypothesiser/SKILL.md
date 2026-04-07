---
name: retention-model-hypothesiser
description: >
  This skill hypothesises the retention model including habit loops, re-engagement triggers, and churn levers. Use when asked to design retention mechanics, model churn drivers, or hypothesize habit loops. Also consider when retention curves flatten prematurely. Suggest when the growth model treats retention as a static constant.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: complex
related-skills:
  - activation-signal-definer
  - activation-moment-validator
  - growth-model-designer
  - growth-loop-optimiser
---

# retention-model-hypothesiser

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The retention model hypothesiser constructs a hypothesis-driven model of why users stay, identifying the habit loops that drive recurring usage, the re-engagement triggers that recover lapsing users, and the churn levers that cause permanent departure, so the growth team can design experiments that improve long-term retention.

## When to Use

- When retention curves show premature flattening (e.g., Day 30 retention below 20% for a daily-use product).
- When the growth model treats retention as a fixed percentage rather than a system of interacting loops.
- When the team needs to prioritize retention experiments but lacks a structured model of churn drivers.
- When a product change (feature launch, UX redesign, pricing change) is expected to affect retention and the team needs to predict the direction and magnitude.

## Workflow

1. **Map the retention landscape**: Plot Day 1, 7, 14, 30, 60, and 90 retention curves by cohort. Identify the inflection points where the curve drops steepest and where it stabilizes.
2. **Identify habit loops**: Hypothesize the recurring usage patterns that drive retention. For each habit loop, define the trigger (internal or external), the action, the variable reward, and the investment that increases switching cost.
3. **Map re-engagement triggers**: List the mechanisms (email, push notification, in-product prompt, social trigger) that can recover lapsing users. For each trigger, hypothesize the timing window (how many days after last activity) and the expected reactivation rate.
4. **Identify churn levers**: Interview churned users or analyse churn survey data to list the top reasons for departure. Categorize as preventable (UX friction, missing feature, support failure) vs. structural (no longer needs the product, competitor switch, budget cut).
5. **Build the retention model**: Construct a quantitative model linking habit loop frequency, re-engagement trigger effectiveness, and churn lever severity to predicted Day 30/60/90 retention. Include sensitivity analysis for each lever.
6. **Prioritize experiments**: Rank retention interventions by expected impact on the retention curve and implementation cost. Focus on the steepest drop-off point first.
7. **Publish hypotheses**: Document each hypothesis with the expected retention impact, the experiment design to validate it, and the success criteria.

## Anti-Patterns

- **Retention as re-engagement only**: Equating retention with email/push campaigns ignores the product-level habit loops that drive organic return. *Why*: push-driven retention is fragile and decays as users develop notification fatigue; product-driven retention compounds.
- **Aggregate retention curves**: Analysing a single retention curve for all users hides that different segments retain for different reasons. *Why*: power users retain because of workflow integration; casual users retain because of content freshness — the interventions differ entirely.
- **Ignoring structural churn**: Spending experiment capacity trying to retain users who have a structural reason to leave (graduated from the product, company went out of business) wastes resources. *Why*: structural churn is unpreventable; experiments should target preventable churn only.
- **No habit loop mapping**: Designing retention experiments without first understanding the habit loops that drive recurring usage produces random interventions. *Why*: effective retention experiments strengthen an existing habit loop or create a new one; without the map, you cannot target the right loop.

## Output

**Success:**
- A retention model document containing cohort retention curves, habit loop hypotheses, re-engagement trigger designs, churn lever taxonomy, a quantitative retention model with sensitivity analysis, and a prioritized list of retention experiments.

**Failure:**
- Insufficient churn data exists to build the model. Report the data gap, recommend churn survey implementation and instrumentation for lapsing behaviour, and provide a placeholder model based on category benchmarks.

## Related Skills

- [`activation-signal-definer`](../activation-signal-definer/SKILL.md) -- the activation signal marks the entry point into the retention model.
- [`activation-moment-validator`](../activation-moment-validator/SKILL.md) -- validates that the activation moment predicts retention, which is a foundational assumption of the retention model.
- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the retention model feeds the retention stage of the growth model.
- [`growth-loop-optimiser`](../growth-loop-optimiser/SKILL.md) -- retention loops are a subset of growth loops that this skill analyses.
