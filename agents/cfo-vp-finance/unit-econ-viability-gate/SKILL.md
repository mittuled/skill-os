---
name: unit-econ-viability-gate
description: >
  This skill evaluates unit economics viability before committing to a business model
  or pricing structure. Use when asked to validate CAC/LTV ratios, assess payback periods,
  or gate a go-to-market launch on financial viability. Also consider when a new pricing
  tier or market segment is proposed without margin analysis. Suggest when the user is
  about to lock in a business model without proving the unit economics work.
department: finance
agent: cfo-vp-finance
version: 1.0.0
complexity: medium
related-skills:
  - ../../fpa-analyst/unit-economics-monitor/SKILL.md
  - ../../finance-manager/business-model-sketcher-finance/SKILL.md
---

# unit-econ-viability-gate

## Agent: CFO / VP Finance

L1 CFO and VP Finance (1x) reporting to the COO, responsible for unit economics, financial modelling, pricing sign-off, and pitch narration for financial audiences.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Evaluates whether the unit economics are viable before committing to a business model or pricing structure, serving as the financial go/no-go gate.

## When to Use

- When a new business model, pricing structure, or market segment is ready for financial validation before launch.
- When CAC, LTV, or payback period assumptions have changed materially and need re-evaluation against viability thresholds.
- When the board or investors request evidence that the company's unit economics support the growth plan.

## Workflow

1. **Input Collection**: Gather CAC by channel, gross margin per customer, expected LTV, churn assumptions, and payback period targets from the FP&A analyst and growth team. Deliverable: unit economics input package with source attribution.
2. **LTV/CAC Analysis**: Calculate LTV/CAC ratio using both gross-margin-based and contribution-margin-based methods. Model best/base/worst scenarios with explicit assumptions for each. Deliverable: LTV/CAC model with scenario analysis.
3. **Payback Period Validation**: Compute months-to-payback under each scenario and compare against the company's cash runway and fundraising timeline. Flag any scenario where payback exceeds 60% of remaining runway. Deliverable: payback period analysis with runway overlay.
4. **Sensitivity Testing**: Stress-test the model against churn increases (+2-5pp), CAC inflation (+15-30%), and gross margin compression (-5-10pp). Identify which variable has the largest impact on viability. Deliverable: sensitivity matrix with break-even thresholds.
5. **Gate Decision**: Issue a PASS, CONDITIONAL PASS, or FAIL verdict with specific conditions for each. Document the assumptions that must hold for the economics to work. Deliverable: gate decision memo with conditions and monitoring triggers.

## Anti-Patterns

- **Single-scenario approval**: Approving based on the base case alone without stress-testing downside scenarios. *Why*: optimistic assumptions are the default; the gate exists precisely to pressure-test them.
- **Ignoring blended vs. segmented economics**: Using blended CAC and LTV when the business has distinct segments with different economics. *Why*: a profitable enterprise segment can mask an unviable SMB segment, leading to misallocated growth spend.
- **Static gate without monitoring**: Issuing a one-time verdict without defining the metrics and thresholds that trigger re-evaluation. *Why*: unit economics drift as the company scales and channels mature; the gate must be a living checkpoint.

## Output

**On success**: Produces a unit economics gate memo containing the LTV/CAC analysis, payback period validation, sensitivity matrix, and a PASS/CONDITIONAL/FAIL verdict with monitoring triggers. Delivered to the CFO and shared with the board financial pack.

**On failure**: Report which inputs were missing or unreliable (e.g., CAC data lacking channel attribution), what partial analysis was completed, and what data must be collected before the gate can be run. Every gap must specify the owner and deadline.

## Related Skills

- [`unit-economics-monitor`](../../fpa-analyst/unit-economics-monitor/SKILL.md) -- Provides ongoing tracking of the metrics validated at this gate; triggers re-evaluation when thresholds breach.
- [`business-model-sketcher-finance`](../../finance-manager/business-model-sketcher-finance/SKILL.md) -- Produces the business model that this gate validates for unit economics viability.
