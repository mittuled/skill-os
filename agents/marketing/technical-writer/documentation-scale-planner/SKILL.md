---
name: documentation-scale-planner
description: >
  This skill plans how documentation structure and tooling will scale as the product grows.
  Use when asked to future-proof documentation, evaluate doc tooling, or plan for multi-product documentation.
  Also consider when documentation build times are increasing or content reuse is needed across products.
  Suggest when the user is about to add a second product's docs without a scalability plan.
department: marketing
agent: technical-writer
version: 1.0.0
complexity: medium
related-skills:
  - api-documentation-designer
  - documentation-writer
  - documentation-requirements-extractor
triggers:
  - "plan documentation at scale"
  - "docs scaling strategy"
  - "documentation team plan"
  - "scale technical writing"
  - "docs ops planning"
---

# documentation-scale-planner

## Agent: Technical Writer

L3 technical writer reporting to Developer Relations Lead, responsible for API documentation, developer guides, and documentation accuracy.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Plans how the documentation structure and tooling will scale as the product grows to prevent documentation becoming a bottleneck to product velocity.

## When to Use

- When the product is expanding to multiple APIs, SDKs, or platforms and documentation structure needs to accommodate growth.
- When documentation build times, search quality, or contributor workflows are degrading.
- When adding a second product line and needing to evaluate shared vs. separate documentation.
- When the documentation team is growing and needs standardized tooling and contribution workflows.

## Workflow

1. **Assess current state**: Evaluate the existing documentation stack using the six dimensions in [framework.md](references/framework.md) (authoring, build pipeline, hosting, search, analytics, contribution workflow). Identify warning signs for each dimension. Deliverable: current state assessment with pain points.
2. **Project growth trajectory**: Estimate documentation growth over the next 12–18 months based on product roadmap (new APIs, platforms, languages, products). Apply the maintenance burden formula from the framework to estimate team capacity requirements at projected scale. Deliverable: growth projection document.
3. **Identify scaling bottlenecks**: Use the bottleneck diagnosis criteria in the framework to identify which parts of the current stack will fail at projected scale. Deliverable: bottleneck analysis with severity ratings.
4. **Evaluate tooling options**: Score tooling options using the six evaluation criteria and comparison matrix from the framework. Deliverable: scored tooling comparison matrix.
5. **Design scale plan**: Select the appropriate IA pattern from the framework for the projected page count. Propose target architecture including tooling changes, content reuse strategy, and IA evolution. Deliverable: documentation scale plan.
6. **Define migration roadmap**: Use the phased migration model from the framework (PoC → parallel run → progressive migration → cutover → decommission). Include the 72-hour rollback gate. Deliverable: migration roadmap with milestones.

## Anti-Patterns

- **Premature optimization**: Investing in complex documentation infrastructure before the scale problems actually manifest. *Why*: Documentation tooling decisions made too early lock in technology choices before requirements are clear, creating migration costs that exceed the problems they prevent.
- **Tool-first planning**: Selecting documentation tooling before understanding the scaling requirements. *Why*: Tool selection should follow requirements analysis; leading with tools creates vendor lock-in and feature gaps that could have been avoided.
- **Ignoring contributor experience**: Planning for content scale without considering how writers and engineers will author, review, and publish. *Why*: A documentation system that is hard to contribute to will not scale regardless of its technical architecture; contributor friction is the primary scaling bottleneck.

## Output

**On success**: Produces a documentation scale plan containing current state assessment, growth projections, tooling evaluation, target architecture, and migration roadmap. Delivered to technical writing, developer relations, and engineering leadership.

**On failure**: Report which growth projections could not be made, what product roadmap information was unavailable, and recommend interim measures. Every error must be actionable.

## Related Skills

- [`api-documentation-designer`](../api-documentation-designer/SKILL.md) — Documentation architecture design must align with the scale plan's information architecture evolution.
- [`documentation-writer`](../documentation-writer/SKILL.md) — Writers are directly affected by tooling changes and must be consulted during scale planning.
- [`documentation-requirements-extractor`](../documentation-requirements-extractor/SKILL.md) — Requirements volume projections feed into the growth trajectory analysis.
