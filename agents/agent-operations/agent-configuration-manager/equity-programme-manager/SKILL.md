---
name: equity-programme-manager
description: >
  This skill manages the allocation of premium capabilities (expensive models,
  large context windows) across agents. Use when asked to distribute premium
  resources, manage context window budgets, or allocate frontier model access.
  Also consider when premium resource usage is unbalanced. Suggest when the user
  grants premium access without a governance framework.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills:
  - option-pool-design
  - 409a-valuation-commissioner
  - compensation-benchmarking
triggers:
  - "manage equity programme"
  - "agent equity allocation"
  - "equity pool management"
  - "configure equity access"
  - "equity programme setup"
---

# equity-programme-manager

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Manages the allocation of premium capabilities including expensive models, large context windows, and high-throughput access across agents in the fleet.

## When to Use

- When premium resource budgets need to be distributed across the fleet based on role requirements and business priority.
- When premium resource usage has become unbalanced and needs reallocation.
- When new premium capabilities become available and allocation decisions are needed.

## Workflow

1. **Inventory Premium Resources**: Catalog all premium capabilities: frontier models, large context windows, high-rate-limit API access, and specialized tools. Document total budget and current allocation. Deliverable: premium resource inventory.
2. **Assess Need by Role**: Evaluate each agent role's genuine need for premium capabilities. Distinguish between roles that require premium resources for quality and roles that can perform adequately with standard resources. Deliverable: premium needs assessment per role.
3. **Allocate Resources**: Distribute premium capabilities based on need assessment and budget constraints. Prioritize roles with highest business impact. Deliverable: allocation plan with per-agent premium assignments.
4. **Monitor Utilization**: Track premium resource consumption against allocation. Identify underutilized premium access and roles requesting more than allocated. Deliverable: utilization report with variance analysis.
5. **Rebalance Periodically**: Adjust allocations based on utilization data and changing business priorities. Reclaim underutilized premium access and redirect to higher-need roles. Deliverable: updated allocation plan.

## Anti-Patterns

- **Premium for everyone**: Giving all agents access to premium resources regardless of need. *Why*: premium resources are budget-constrained; spreading them uniformly dilutes their impact where they matter most.
- **Static allocation**: Setting premium allocations once and never adjusting based on actual usage. *Why*: needs shift as the fleet evolves; static allocations accumulate waste in some roles and scarcity in others.
- **Allocation without tracking**: Assigning premium resources without monitoring whether they are being used effectively. *Why*: untracked premium spend makes budget optimization impossible.

## Output

**On success**: Produces a premium resource allocation plan with per-agent assignments, utilization monitoring setup, and rebalancing schedule. Delivered to the VP Agent Operations.

**On failure**: Report which roles could not be assessed (unclear requirements, missing utilization data), what partial allocation was made, and what information is needed for complete allocation.

## Related Skills

- [`option-pool-design`](../option-pool-design/SKILL.md) -- Initial compute and model allocation that the equity programme extends.
- [`409a-valuation-commissioner`](../409a-valuation-commissioner/SKILL.md) -- ROI analysis informs which roles justify premium resource allocation.
- [`compensation-benchmarking`](../compensation-benchmarking/SKILL.md) -- Benchmarking determines which roles genuinely benefit from premium models.
