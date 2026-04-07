---
name: growth-loop-optimiser
description: >
  This skill identifies and optimises the highest-leverage growth loops based on data. Use when asked to improve viral coefficients, optimize referral mechanics, or strengthen content-driven acquisition loops. Also consider when growth flattens despite stable acquisition spend. Suggest when the growth model shows a loop with declining throughput.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: complex
related-skills:
  - growth-model-designer
  - growth-loop-activator
  - activation-moment-validator
  - funnel-analyser-growth
---

# growth-loop-optimiser

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth loop optimiser analyses active growth loops — viral, content, paid, and product-led — to identify friction points, measure loop throughput (users in vs. users generated), and design experiments that increase the loop's compounding rate.

## When to Use

- When a growth loop is active but throughput (viral coefficient, content amplification factor, or referral rate) is declining.
- When the growth model shows that optimizing an existing loop yields higher ROI than opening a new channel.
- When a referral or sharing mechanic is live but underperforming the benchmark for the product category.
- When the team needs to decide which loop to prioritize for the next experiment cycle.

## Workflow

1. **Map active loops**: Document each active growth loop as a cycle: trigger action, user output, distribution mechanism, new user input, and activation step. Quantify the throughput at each node.
2. **Measure loop metrics**: For viral loops, calculate the viral coefficient (k = invites sent * conversion rate) and cycle time. For content loops, measure content creation rate, SEO impressions, CTR, and signup conversion. For paid loops, measure ROAS and reinvestment rate.
3. **Identify bottleneck node**: Find the node in each loop with the largest drop-off. Rank loops by the potential throughput gain from fixing the bottleneck.
4. **Design experiments**: For the top bottleneck, design 2-3 experiments with clear hypotheses, success metrics, and minimum detectable effect. Prioritize by expected impact and implementation effort.
5. **Model compounding impact**: Project the long-term user growth impact of each experiment assuming success. A 10% improvement in viral coefficient compounds over each cycle — model the 6-month trajectory.
6. **Execute and measure**: Run experiments with proper A/B testing and statistical significance tracking. After conclusion, update the loop metrics and re-rank bottlenecks.

## Anti-Patterns

- **Optimizing a broken loop**: Spending experiment cycles on a loop whose fundamental mechanic does not work (k < 0.1 for viral) before fixing structural issues. *Why*: optimizing a 0.05 viral coefficient to 0.07 is meaningless; the loop needs a mechanic redesign, not conversion optimization.
- **Ignoring cycle time**: Focusing only on conversion rates without reducing the time between loop iterations underestimates the compounding effect of speed. *Why*: a loop with k=0.5 and a 2-day cycle time outperforms k=0.7 with a 30-day cycle time over 6 months.
- **Single-loop dependency**: Optimizing only one loop creates fragility. *Why*: if the primary loop degrades (platform change, competitive response), growth stalls without a fallback.
- **No compounding model**: Evaluating loop improvements as linear gains instead of compound growth understates the value of small improvements. *Why*: a 5% improvement per loop cycle compounds to 50%+ over 10 cycles.

## Output

**Success:**
- A loop optimization report containing loop maps with node-level metrics, bottleneck ranking, experiment designs with projected compound impact, and a prioritized experiment roadmap.

**Failure:**
- No active loop has a throughput above the minimum viable threshold. Report the loop analysis, recommend structural changes to loop mechanics, and flag whether a new loop type should be explored.

## Related Skills

- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model provides the framework within which loops operate.
- [`growth-loop-activator`](../../../data-growth/growth-engineer/growth-loop-activator/SKILL.md) -- implements the loop mechanics that this skill optimizes.
- [`activation-moment-validator`](../activation-moment-validator/SKILL.md) -- the activation step within each loop must be validated as a retention predictor.
- [`funnel-analyser-growth`](../../../data-growth/growth-engineer/funnel-analyser-growth/SKILL.md) -- funnel analysis within each loop node reveals specific conversion bottlenecks.
