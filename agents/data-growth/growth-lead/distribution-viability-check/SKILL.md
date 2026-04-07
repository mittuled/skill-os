---
name: distribution-viability-check
description: >
  This skill assesses whether proposed distribution channels can reach the target customer at acceptable CAC. Use when asked to evaluate channel feasibility, assess acquisition economics, or validate go-to-market distribution. Also consider before committing budget to a new channel. Suggest when the growth model assumes channel performance without validation.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
  - growth-model-designer
  - demand-gen-planner-growth
  - search-demand-validator
---

# distribution-viability-check

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The distribution viability check evaluates whether each proposed acquisition channel can reach the target customer segment at a CAC that sustains a healthy LTV:CAC ratio, producing a go/no-go verdict per channel before budget is committed.

## When to Use

- When the growth model proposes acquisition channels that have not been tested or validated.
- When a new market segment is targeted and existing channel assumptions may not transfer.
- When CAC on an existing channel degrades and the team evaluates alternatives.
- When a GTM strategy includes partner or marketplace distribution that needs feasibility assessment.

## Workflow

1. **Define target customer**: Specify the ICP (ideal customer profile) including demographics, behaviour patterns, and the platforms/channels where they spend time.
2. **List candidate channels**: Enumerate all proposed channels — paid search, paid social, content/SEO, partnerships, marketplaces, product-led/viral, community, events.
3. **Estimate unit economics per channel**: For each channel, estimate CPC/CPM, expected CTR, landing page conversion rate, and resulting CAC. Use industry benchmarks where first-party data is unavailable.
4. **Assess volume ceiling**: Estimate the maximum monthly volume each channel can deliver before audience saturation degrades economics. Cross-reference with search volume and audience size data.
5. **Calculate LTV:CAC ratio**: For each channel, compute the expected LTV:CAC ratio and payback period. Flag channels where LTV:CAC falls below 3:1 or payback exceeds 12 months.
6. **Produce viability scorecard**: Rate each channel on reach (can it hit the ICP?), economics (CAC within budget?), scalability (volume ceiling sufficient?), and timeline (how quickly can it be activated?). Deliver a go/caution/no-go per channel.

## Anti-Patterns

- **Benchmark-only analysis**: Relying entirely on industry benchmarks without running a small-scale test overestimates confidence in channel economics. *Why*: your product, ICP, and messaging produce different results than the average.
- **Ignoring payback period**: Focusing on LTV:CAC ratio without considering payback period strains cash flow for early-stage companies. *Why*: a 5:1 ratio with a 24-month payback is worse than 3:1 with a 3-month payback when capital is limited.
- **Single-channel dependency**: Approving only one channel creates concentration risk. *Why*: platform algorithm changes, policy updates, or cost inflation can eliminate a single channel overnight.

## Output

**Success:**
- A distribution viability scorecard rating each channel on reach, economics, scalability, and timeline, with a go/caution/no-go verdict and supporting data.

**Failure:**
- No viable channel achieves LTV:CAC above 3:1. Report the analysis, the closest channels, and recommend whether to adjust pricing (increase LTV), reduce CAC through product-led growth, or narrow the ICP.

## Related Skills

- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model assumes channel performance that this skill validates.
- [`demand-gen-planner-growth`](../demand-gen-planner-growth/SKILL.md) -- the demand gen plan is built using channels approved by this viability check.
- [`search-demand-validator`](../../../data-growth/analytics-lead/search-demand-validator/SKILL.md) -- search demand data informs volume ceiling estimates for organic and paid search channels.
