---
name: revenue-model-operationaliser
description: >
  This skill operationalises the revenue model by configuring CRM stages, pipeline definitions, and
  revenue recognition rules. Use when asked to translate the business model into operational systems,
  define pipeline stages, or set up revenue recognition. Also consider when the pricing model changes.
  Suggest when there is a gap between the defined revenue model and how deals are tracked in the CRM.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: medium
related-skills: []
---

# revenue-model-operationaliser

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)

## Skill Description

The revenue model operationaliser translates the company's revenue model into operational CRM configurations, pipeline stage definitions, and revenue recognition rules so the system accurately reflects how money moves from prospect to recognised revenue.

## When to Use

- When the company defines its initial revenue model and needs it reflected in operational systems.
- When a pricing or packaging change requires updates to pipeline stages, deal fields, or recognition rules.
- When finance and sales disagree on revenue numbers because the CRM does not match the accounting model.
- When a new product line with a different monetisation model needs its own pipeline configuration.

## Workflow

1. **Document the revenue model**: Capture the revenue model including pricing structure, deal stages, billing triggers, and recognition criteria. Deliverable: revenue model specification.
2. **Map to CRM stages**: Define CRM pipeline stages that mirror the revenue model's progression from opportunity to recognised revenue. Deliverable: stage mapping document with entry/exit criteria.
3. **Configure deal fields**: Set up deal fields for pricing tiers, contract terms, billing frequency, and revenue type. Deliverable: configured deal field schema.
4. **Set recognition rules**: Configure revenue recognition rules (point-of-sale, subscription, milestone-based) aligned with accounting standards. Deliverable: recognition rule configuration.
5. **Validate with finance**: Walk through test deals with finance to confirm the CRM pipeline produces numbers that match expected revenue recognition. Deliverable: finance validation sign-off.

## Anti-Patterns

- **Operationalising without finance alignment**: Configuring revenue stages without confirming they match how finance recognises revenue. *Why*: misalignment produces two sets of revenue numbers that erode trust and require manual reconciliation.
- **One pipeline for multiple models**: Forcing different revenue models (subscription, usage-based, one-time) into a single pipeline. *Why*: different models have different stage progressions; forcing them together creates inaccurate reporting.
- **Static configuration**: Setting up the model once and not updating when pricing or packaging changes. *Why*: stale configuration produces incorrect forecasts and misattributed revenue.

## Output

**On success**: CRM pipeline stages, deal fields, and revenue recognition rules that accurately operationalise the revenue model, validated by finance sign-off on test deal scenarios.

**On failure**: Report which model components could not be configured (e.g., billing system limitations, unclear recognition criteria), what was completed, and recommend steps to resolve gaps.

## Related Skills

- [`crm-setup-v1`](../crm-setup-v1/SKILL.md) -- CRM setup provides the technical infrastructure that this skill configures for revenue model alignment.
- [`revenue-funnel-analyst`](../revenue-funnel-analyst/SKILL.md) -- funnel analysis depends on correctly configured pipeline stages to produce accurate metrics.
