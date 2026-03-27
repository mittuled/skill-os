---
name: activation-signal-definer
description: >
  This skill defines the activation signal — the specific user behaviour indicating core value has been experienced. Use when asked to define the aha moment, set activation criteria, or identify the behaviour that separates retained from churned users. Also consider when onboarding redesigns need a target metric. Suggest when growth experiments lack a clear activation goal.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
  - activation-moment-validator
  - growth-model-designer
  - retention-model-hypothesiser
---

# activation-signal-definer

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The activation signal definer identifies and formalizes the specific user behaviour that indicates a new user has experienced the product's core value, producing a measurable activation metric with an event, threshold, and time window that the growth team can optimize toward.

## When to Use

- When the product lacks a defined activation metric and growth experiments have no clear target.
- When onboarding redesign is underway and the team needs to know what "activated" means quantitatively.
- When the product's value proposition changes and the existing activation signal may no longer represent the aha moment.
- When multiple teams define "active user" differently and need a canonical activation standard.

## Workflow

1. **Map the value moment**: Interview users who retained past Day 30 and users who churned within Day 7. Identify the action or outcome that retained users consistently completed and churned users did not.
2. **Generate candidate signals**: List 5-10 candidate behaviours (e.g., "created first dashboard," "invited a teammate," "completed first analysis"). Each must be instrumentable as an event.
3. **Analyse retention correlation**: For each candidate, compute retention rates for users who completed the action vs. those who did not. Rank by retention lift.
4. **Define threshold and window**: For the top candidate, determine the optimal threshold (how many times) and time window (within how many days of signup) by testing multiple combinations against retention.
5. **Formalize the definition**: Write the activation signal as a precise statement: "A user is activated when they [event] [threshold] times within [window] days of signup."
6. **Validate and publish**: Hand off to activation-moment-validator for statistical validation. Once validated, publish the definition to growth, product, and engineering teams.

## Anti-Patterns

- **Gut-feel activation**: Defining the aha moment based on intuition rather than retention data produces a metric the team optimizes toward without evidence it matters. *Why*: optimizing toward the wrong activation signal wastes experiment capacity on a non-causal lever.
- **Too-easy activation**: Setting the bar at a trivial action (e.g., "logged in") inflates activation rates without predicting retention. *Why*: everyone logs in at least once; the signal has no discriminative power.
- **Too-hard activation**: Setting the bar at a power-user action (e.g., "used advanced feature X") classifies most users as non-activated, making the metric useless for broad optimization. *Why*: the activation signal should capture the minimum viable value moment, not expert usage.

## Output

**Success:**
- A formalized activation signal definition with event name, threshold, time window, retention lift data, and publication to all relevant teams.

**Failure:**
- No candidate signal shows meaningful retention lift (>10 percentage points). Report the analysis, the candidates tested, and recommend deeper user research before re-attempting definition.

## Related Skills

- [`activation-moment-validator`](../activation-moment-validator/SKILL.md) -- validates the signal this skill defines.
- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the activation metric is a core input to the growth model.
- [`retention-model-hypothesiser`](../retention-model-hypothesiser/SKILL.md) -- the retention model builds on the activation signal as the entry point for retention mechanics.
