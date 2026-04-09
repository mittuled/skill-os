---
name: demand-gen-planner-growth
description: >
  This skill plans demand generation activities aligned to the growth model. Use when asked to design acquisition campaigns, plan top-of-funnel activities, or allocate demand generation budget. Also consider when CAC is rising without corresponding LTV improvement. Suggest when the growth model shows an acquisition bottleneck.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
  - growth-model-designer
  - distribution-viability-check
  - search-demand-validator
triggers:
  - "plan demand gen growth"
  - "growth demand generation plan"
  - "demand acquisition strategy"
  - "build growth demand plan"
  - "growth pipeline planning"
---

# demand-gen-planner-growth

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The demand gen planner designs acquisition activities — paid, organic, and partner-driven — that feed the growth model's top-of-funnel targets while maintaining CAC within the acceptable ratio to LTV.

## When to Use

- When the growth model identifies an acquisition bottleneck requiring planned demand generation.
- When CAC trends upward and the team needs to diversify or optimize acquisition channels.
- When a new product or feature launch requires a coordinated demand generation push.
- When quarterly planning requires budget allocation across acquisition channels.

## Workflow

1. **Set acquisition targets**: Derive monthly acquisition volume and CAC targets from the growth model. Calculate the maximum allowable CAC based on LTV and target payback period.
2. **Audit current channels**: Review performance of existing channels — paid search, paid social, organic SEO, content marketing, partnerships, product-led growth. Rank by CAC efficiency and volume capacity.
3. **Identify new channels**: Based on the distribution viability check and search demand data, propose 1-2 new channels to test. Define the minimum viable experiment for each.
4. **Allocate budget**: Distribute budget across channels based on historical CAC, projected volume capacity, and strategic priority. Reserve 15-20% for experimentation on new channels.
5. **Define campaigns**: For each channel, outline the campaign — target audience, messaging, landing pages, conversion events, and success metrics.
6. **Set measurement plan**: Define how each campaign will be tracked (UTM parameters, attribution model, conversion events) and the reporting cadence.

## Anti-Patterns

- **Scaling unvalidated channels**: Pouring budget into a channel before proving CAC sustainability at small scale wastes capital. *Why*: channel economics often degrade as spend increases due to audience saturation.
- **Ignoring organic in favour of paid**: Defaulting to paid acquisition without investing in organic and product-led growth creates permanent cost dependency. *Why*: paid channels have linear cost curves while organic compounds over time.
- **No attribution discipline**: Running campaigns without proper UTM tagging and attribution makes it impossible to measure channel-level CAC. *Why*: unattributed conversions prevent budget optimization.

## Output

**Success:**
- A demand generation plan with channel allocations, budget per channel, campaign briefs, CAC targets, measurement plan, and a timeline.

**Failure:**
- No channel can deliver the required volume at acceptable CAC. Report the channel analysis, the volume-CAC trade-off curve, and recommend adjusting the growth model's acquisition targets or exploring new channels.

## Related Skills

- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model sets the acquisition targets this plan fulfils.
- [`distribution-viability-check`](../distribution-viability-check/SKILL.md) -- channel viability assessment informs which channels to include in the plan.
- [`search-demand-validator`](../../../data-growth/analytics-lead/search-demand-validator/SKILL.md) -- search demand data informs organic and paid search channel sizing.
