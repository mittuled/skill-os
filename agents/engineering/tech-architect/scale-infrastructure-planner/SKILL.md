---
name: scale-infrastructure-planner
description: >
  This skill plans infrastructure changes required to support projected user and
  data scale. Use when asked to plan for scaling, capacity planning, or
  infrastructure growth. Also consider when traffic projections exceed current
  capacity or a major launch is approaching. Suggest when the team is planning
  a feature that will significantly increase load.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: complex
related-skills:
  - technical-feasibility-check
  - design-feasibility-reviewer
  - tech-scaffolder
triggers:
  - "plan infrastructure scaling"
  - "scale infra plan"
  - "infrastructure growth plan"
  - "scaling roadmap"
  - "capacity planning"
---

# scale-infrastructure-planner

## Agent: Tech Architect
L2 technical architect responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description
Plans the infrastructure changes required to support projected user, traffic, and data scale over a defined time horizon.

## When to Use
- When projected growth (users, requests, data volume) will exceed current infrastructure capacity within the next 3-6 months.
- When a major product launch or marketing campaign is expected to cause a step-change in traffic.
- When post-mortem analysis reveals the current architecture hit scaling limits during a traffic spike.

## Workflow
1. **Quantify scale targets**: Gather projected metrics — concurrent users, requests per second, data storage growth, peak-to-average ratios. Define the time horizon (3/6/12 months). Deliverable: scale requirements document with numeric targets.
2. **Audit current capacity**: Map existing infrastructure against scale targets. Identify bottlenecks — database connections, compute limits, network bandwidth, storage IOPS. Deliverable: capacity gap analysis.
3. **Design scaling strategy**: For each bottleneck, evaluate options — vertical scaling, horizontal scaling, caching layers, read replicas, sharding, CDN offload, queue-based decoupling. Deliverable: scaling strategy per component.
4. **Estimate costs**: Project infrastructure cost at target scale. Compare against budget. Identify cost-optimisation opportunities (reserved instances, spot capacity, tiered storage). Deliverable: cost projection with options.
5. **Define migration path**: Sequence the infrastructure changes to avoid downtime. Identify which changes can be done incrementally vs. which require maintenance windows. Deliverable: phased migration plan with rollback procedures.
6. **Set monitoring thresholds**: Define capacity alerts that trigger before limits are reached — 70% utilisation warnings, 85% critical alerts. Deliverable: monitoring configuration document.
7. **Document decisions**: Record the scaling strategy in an ADR. Link to cost projections, migration plan, and monitoring dashboards. Deliverable: published scaling ADR.

## Anti-Patterns
- **Scaling without measuring**: Adding capacity based on intuition rather than measured bottlenecks wastes money and may not address the actual constraint. *Why*: the bottleneck is often not where you think — databases hit connection limits before CPU limits, networks saturate before compute does.
- **Big-bang migration**: Attempting all infrastructure changes in a single deployment creates high risk of cascading failures. *Why*: phased rollouts with rollback procedures let you validate each change before proceeding.
- **Ignoring cost at scale**: Designing for unlimited horizontal scaling without cost modelling can produce architectures that are technically sound but financially unsustainable. *Why*: infrastructure cost grows non-linearly — a 10x traffic increase rarely costs exactly 10x more.
- **Planning without a time horizon**: "Scale for growth" without a specific target (e.g., 100K concurrent users by Q4) produces vague plans that can't be prioritised. *Why*: engineering needs concrete numbers to make architecture decisions, not directional intent.

## Output
**On success**: A scaling plan containing: scale requirements with numeric targets, capacity gap analysis, per-component scaling strategy, cost projection, phased migration plan with rollback procedures, and monitoring thresholds. Published as an ADR with linked dashboards.

**On failure**: Report which scale dimensions could not be planned (unclear growth projections, missing baseline metrics, budget constraints that make required scaling infeasible). Recommend specific data collection, load testing, or budget discussions needed before the plan can be completed.

## Related Skills
- [`technical-feasibility-check`](../technical-feasibility-check/SKILL.md) — sibling skill under the same agent — combine with technical-feasibility-check for end-to-end coverage
- [`design-feasibility-reviewer`](../design-feasibility-reviewer/SKILL.md) — sibling skill under the same agent — combine with design-feasibility-reviewer for end-to-end coverage
- [`tech-scaffolder`](../tech-scaffolder/SKILL.md) — sibling skill under the same agent — combine with tech-scaffolder for end-to-end coverage
