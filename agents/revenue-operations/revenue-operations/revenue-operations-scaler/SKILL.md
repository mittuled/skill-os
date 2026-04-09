---
name: revenue-operations-scaler
description: >
  This skill scales revenue operations infrastructure to support growing pipeline and customer volume.
  Use when asked to handle RevOps growing pains, optimise workflows for higher volume, or plan
  infrastructure capacity. Also consider when manual processes are breaking under increased deal flow.
  Suggest when pipeline volume doubles and existing processes show strain.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "scale revenue operations"
  - "grow RevOps capacity"
  - "rev ops scaling plan"
  - "revenue ops maturity"
  - "scale GTM operations"
---

# revenue-operations-scaler

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)

## Skill Description

The revenue operations scaler identifies and resolves infrastructure, process, and tooling bottlenecks in the revenue operations stack so the organisation can handle growing deal volume and customer count without manual process breakdown.

## When to Use

- When pipeline volume grows and manual processes (data entry, reporting, handoffs) cannot keep pace.
- When the sales team expands and existing CRM workflows need to support more users and territories.
- When reporting latency increases because data volume exceeds current tooling capacity.
- When customer onboarding volume strains the handoff between sales and post-sales systems.

## Workflow

1. **Audit current capacity**: Assess current RevOps processes, tools, and workflows against projected volume growth. Deliverable: capacity audit with bottleneck identification.
2. **Prioritise bottlenecks**: Rank bottlenecks by business impact (revenue at risk, team productivity loss, data quality degradation). Deliverable: prioritised bottleneck list.
3. **Design scaling solutions**: For each bottleneck, design a solution: automation, tool upgrade, process redesign, or additional tooling. Deliverable: scaling solution proposals.
4. **Implement changes**: Execute the scaling improvements in priority order with rollback plans. Deliverable: implemented changes with before/after metrics.
5. **Monitor and iterate**: Track the impact of scaling changes on throughput, data quality, and team productivity. Deliverable: post-implementation monitoring report.

## Anti-Patterns

- **Scaling by adding headcount first**: Hiring more people before automating manual processes. *Why*: manual processes do not scale linearly; doubling people does not double throughput and increases error rates.
- **Big-bang platform migration**: Replacing the entire RevOps stack at once during a high-growth period. *Why*: migrations disrupt operations at the worst possible time; incremental improvements deliver value faster with less risk.
- **Scaling without data quality**: Automating processes on top of dirty data. *Why*: automation amplifies data quality problems; garbage in, garbage out at scale is worse than garbage at low volume.

## Output

**On success**: A RevOps infrastructure that handles projected volume growth with identified bottlenecks resolved, implemented automation, and monitoring dashboards tracking throughput and data quality.

**On failure**: Report which bottlenecks could not be resolved (e.g., vendor limitations, budget constraints), what was implemented, and recommend interim workarounds and timeline for permanent fixes.

## Related Skills

- [`crm-setup-v1`](../crm-setup-v1/SKILL.md) -- CRM setup builds the initial infrastructure that this skill scales.
- [`revenue-tooling-readiness`](../revenue-tooling-readiness/SKILL.md) -- tooling readiness ensures new or upgraded tools are ready before deployment.
