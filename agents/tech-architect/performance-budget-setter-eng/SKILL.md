---
name: performance-budget-setter-eng
description: >
  This skill defines quantitative performance budgets for latency, throughput, and
  memory that engineering builds against. Use when asked to set performance targets,
  define SLOs, or establish non-functional requirements. Also consider when a new
  service is being designed or an existing one is scaling. Suggest when the team is
  about to begin implementation without explicit performance constraints.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills: []
---

# performance-budget-setter-eng

## Agent: Tech Architect
L2 technical architect responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description
Sets quantitative performance budgets for latency, throughput, and memory that engineering teams build and test against.

## When to Use
- When a new service or feature requires explicit performance targets before implementation begins.
- When an existing system is being re-architected and current performance baselines need updating.
- When product requirements include user-facing latency or throughput expectations that must be translated into engineering constraints.

## Workflow
1. **Gather context**: Identify the service, feature, or endpoint requiring performance budgets. Collect current baselines if they exist. Deliverable: context summary with existing metrics.
2. **Define budget categories**: Establish which dimensions matter — p50/p95/p99 latency, requests per second, memory ceiling, cold start time, payload size. Deliverable: budget category list.
3. **Set targets**: Define specific numeric targets per category based on user expectations, infrastructure constraints, and business requirements. Deliverable: performance budget table.
4. **Validate feasibility**: Review targets with engineering leads to confirm they are achievable within the current architecture and timeline. Deliverable: feasibility assessment with any flagged risks.
5. **Document and publish**: Record the performance budget in the service's ADR or design doc. Link to monitoring dashboards that will track adherence. Deliverable: published performance budget document.

## Anti-Patterns
- **Setting aspirational targets without baselines**: Defining "sub-100ms p99" without measuring current performance first leads to unrealistic expectations. *Why*: teams either ignore unachievable targets or waste cycles optimising prematurely.
- **Budgeting only happy-path latency**: Ignoring error paths, cold starts, and degraded-mode performance creates blind spots. *Why*: production incidents happen on the edges, not the median.
- **One-time budgets with no monitoring**: Setting targets without dashboards means no one knows when budgets are breached. *Why*: a performance budget without observability is a wish, not a constraint.

## Output
**On success**: A published performance budget document containing numeric targets per category (latency percentiles, throughput, memory), linked to monitoring dashboards and referenced in the service's design doc.

**On failure**: Report which budget categories could not be defined and why (missing baselines, unclear product requirements, architectural uncertainty). Recommend specific data collection or spikes needed before budgets can be set.

## Related Skills
- (none yet — cross-references added in validation pass)
