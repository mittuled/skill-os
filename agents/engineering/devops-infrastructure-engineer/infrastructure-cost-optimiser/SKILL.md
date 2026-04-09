---
name: infrastructure-cost-optimiser
description: Finds and eliminates wasted cloud spend without sacrificing reliability or performance. Use when asked to infrastructure cost optimiser. Suggest when relevant.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "cloud costs"
  - "cost optimisation"
  - "reduce AWS bill"
  - "infrastructure savings"
---

# infrastructure-cost-optimiser

## Agent: Social Media Manager

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer identifies and implements infrastructure cost optimisation opportunities.

## When to Use

- Cloud costs have increased significantly without a corresponding increase in traffic or services.
- A cost review cadence has been established and it is time for the periodic assessment.
- The team is preparing budget forecasts and needs to right-size current spend.
- A new pricing model or reserved instance opportunity has become available.

## Workflow

1. Pull the current cost breakdown by service, team, environment, and resource type.
2. Identify underutilized resources: low-CPU instances, oversized databases, idle load balancers.
3. Identify waste: orphaned resources, unattached volumes, unused IP addresses.
4. Evaluate reserved instance or savings plan opportunities based on steady-state usage patterns.
5. Propose right-sizing recommendations with projected savings and any performance risk.
6. Implement quick wins (delete orphaned resources, schedule non-production shutdowns).
7. Plan and execute right-sizing changes with monitoring to confirm no performance impact.
8. Report the total savings achieved and remaining optimization opportunities.
   - **Deliverable**: Cost optimization report with findings, implemented savings, and remaining recommendations.

## Anti-Patterns

- **Optimizing cost without monitoring performance impact.** *Why*: Right-sizing that causes latency spikes or outages costs more than the savings it generates.
- **Treating cost optimization as a one-time project.** *Why*: Cloud usage patterns change continuously; optimization must be a recurring process.
- **Focusing only on compute while ignoring data transfer and storage.** *Why*: Data transfer and storage costs often grow faster than compute and are easier to overlook.

## Output

**Success**: A cost optimization report showing implemented savings, performance validation, and a backlog of future opportunities.

**Failure**: A cost analysis identifying optimization opportunities that could not be implemented, with blockers and a plan to address them.

## Related Skills

*None defined yet.*
