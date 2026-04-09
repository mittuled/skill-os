---
name: performance-budget-setter
description: >
  This skill sets the performance budget that a product must meet across load time, API latency,
  and resource consumption. Use when asked to define acceptable performance thresholds, set SLOs
  for user-facing interactions, or establish non-functional requirements. Also consider when users
  report sluggishness but engineering has no target to optimize against. Suggest when the team is
  about to ship a feature without quantified performance expectations.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "set performance budget"
  - "performance budget"
  - "define performance targets"
  - "perf budget"
  - "performance constraints"
---

# performance-budget-setter

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Sets the performance budget -- load time, API latency, payload size, and resource consumption thresholds -- that the product must meet to deliver an acceptable user experience.

## When to Use
- When a new feature or product increment needs explicit non-functional requirements before engineering begins implementation
- When user research or support tickets reveal performance complaints but no defined budget exists to measure against
- When infrastructure costs are growing and the team needs performance guardrails to constrain resource consumption per interaction

## Workflow
1. **Identify critical user paths**: Map the 3-5 user interactions that most affect perceived performance (e.g., initial page load, search query, dashboard render). Rank by frequency and business impact. Deliverable: prioritized list of critical paths with usage volume estimates.
2. **Benchmark current performance**: Collect p50, p95, and p99 latency measurements for each critical path. Pull data from APM tools, synthetic monitoring, or manual profiling. Deliverable: baseline performance table with percentile breakdowns.
3. **Set budget thresholds**: Define target values for each critical path at p50 and p95. Ground targets in user research (perceived speed thresholds), competitive benchmarks, or business constraints (e.g., conversion drop-off curves). Deliverable: performance budget table with metric, current baseline, target, and rationale per row.
4. **Define enforcement policy**: Specify how the budget is monitored (synthetic tests, CI checks, production alerts) and what happens when a threshold is breached (block deploy, alert on-call, create tech-debt ticket). Deliverable: enforcement rules document.
5. **Align with engineering**: Review the budget with the engineering lead and SRE team. Confirm that targets are achievable within the planned architecture and that monitoring instrumentation exists. Deliverable: signed-off performance budget or documented trade-off decisions.

## Anti-Patterns
- **Aspirational budgets**: Setting targets based on what would be ideal rather than what the architecture can deliver. *Why*: Unrealistic budgets get ignored by engineering, making the entire performance framework performative rather than protective.
- **Single-percentile thinking**: Defining only p50 targets and ignoring tail latency. *Why*: p50 hides the experience of the worst-affected users, who are often the most valuable (complex queries, large accounts, mobile networks).
- **Budget without enforcement**: Setting thresholds that no CI pipeline or alert actually checks. *Why*: Unenforced budgets decay silently as features accumulate; by the time someone notices, the regression is too entangled to isolate.
- **One-size-fits-all thresholds**: Applying the same latency target to a dashboard load and a batch export. *Why*: Different interactions have different user expectations; uniform budgets either over-constrain cheap operations or under-constrain expensive ones.

## Output
**On success**: A performance budget document containing critical path inventory, baseline measurements, target thresholds at p50 and p95, enforcement policy, and engineering sign-off -- formatted for embedding in a PRD or technical requirements spec.

**On failure**: Report which paths could not be baselined (missing instrumentation, insufficient traffic volume), which targets could not be agreed upon (architectural constraints, cost trade-offs), what was attempted, and recommend specific instrumentation work or architecture reviews to unblock.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
