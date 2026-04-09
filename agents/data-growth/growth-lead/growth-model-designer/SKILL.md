---
name: growth-model-designer
description: >
  This skill designs the growth model mapping acquisition, activation, retention, revenue, and referral mechanics. Use when asked to build a growth model, map the AARRR funnel, or create a quantitative user growth framework. Also consider at company formation or major pivots. Suggest when growth decisions are made without a unifying model.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: complex
related-skills:
triggers:
  - "design growth model"
  - "build growth framework"
  - "growth model architecture"
  - "create growth equation"
  - "model growth levers"
---

# growth-model-designer

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth model designer builds a quantitative framework mapping the full user lifecycle — acquisition, activation, retention, revenue, and referral (AARRR) — with conversion rates, loop mechanics, and unit economics at each stage, enabling the team to identify the highest-leverage growth levers and forecast user growth trajectories.

## When to Use

- When a product is preparing for launch and needs a growth framework before acquisition begins.
- When the team lacks a unified model and makes growth decisions based on isolated metrics.
- When a pivot changes the value proposition, acquisition channels, or revenue model and the growth model needs redesign.
- When the team needs to forecast user growth for fundraising, board presentations, or capacity planning.

## Workflow

1. **Define lifecycle stages**: Map each AARRR stage to the specific user actions in the product. Define the event and threshold that marks transition between stages.
2. **Quantify conversion rates**: Estimate or measure the conversion rate between each stage. Use existing data where available; use category benchmarks for pre-launch products. Document confidence levels.
3. **Map growth loops**: Identify each growth loop (viral, content, paid, product-led). For each loop, document the cycle mechanics, throughput metrics, and cycle time.
4. **Model unit economics**: Calculate CAC per channel, LTV per segment, LTV:CAC ratio, and payback period. Model how these change at 2x, 5x, and 10x current volume.
5. **Build the forecast**: Create a spreadsheet model that takes acquisition volume as input and projects active users, revenue, and churn over 12-24 months. Include scenario toggles for key assumptions.
6. **Identify leverage points**: Rank each conversion rate and loop metric by sensitivity — a 10% improvement in which metric produces the largest impact on 12-month active users? This identifies the priority for growth experiments.
7. **Publish and socialize**: Present the growth model to leadership, product, and engineering. Align on which leverage points to prioritize in the next quarter.

## Anti-Patterns

- **Static model**: Building the growth model once and never updating it with actuals turns it into fiction. *Why*: assumptions drift from reality within weeks; the model must be a living document fed by real data.
- **Acquisition-only focus**: Modelling only the top of funnel while treating retention as a constant underestimates churn's compounding drag on growth. *Why*: a 5% monthly churn rate eliminates 46% of acquired users within a year.
- **No sensitivity analysis**: Presenting a single growth trajectory without varying assumptions gives false precision. *Why*: stakeholders plan resources against the forecast; a single scenario hides the range of possible outcomes.
- **Ignoring negative loops**: Omitting churn loops, support cost loops, or negative word-of-mouth from the model produces systematically optimistic forecasts. *Why*: negative loops counteract positive loops and can dominate at scale.

## Output

**Success:**
- A growth model document and spreadsheet containing AARRR stage definitions, conversion rates, loop maps, unit economics, a 12-24 month forecast with sensitivity analysis, and a ranked list of leverage points.

**Failure:**
- Key conversion rates cannot be estimated due to lack of data or instrumentation. Report the data gaps, the assumptions used as placeholders, and the validation plan to replace assumptions with actuals.

## Related Skills

- [`activation-signal-definer`](../activation-signal-definer/SKILL.md) -- the activation signal is the transition metric between acquisition and activation stages in the model.
- [`retention-model-hypothesiser`](../retention-model-hypothesiser/SKILL.md) -- the retention model feeds the retention stage of the growth model.
- [`distribution-viability-check`](../distribution-viability-check/SKILL.md) -- channel viability informs the acquisition inputs to the model.
- [`growth-loop-optimiser`](../growth-loop-optimiser/SKILL.md) -- loop optimization targets the leverage points identified by the model.
