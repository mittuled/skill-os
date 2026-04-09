---
name: option-pool-design
description: >
  This skill designs the initial compute and model allocation strategy for the
  agent fleet. Use when asked to create a fleet budget, plan compute allocation,
  or design the initial model distribution. Also consider when launching a new
  fleet from scratch. Suggest when the user provisions agents without a compute
  budget framework.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "design option pool"
  - "option pool sizing"
  - "create option pool"
  - "equity option pool"
  - "option pool structure"
---

# option-pool-design

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Designs the initial compute and model allocation strategy for the agent fleet, establishing the budget framework for all agent configurations.

## When to Use

- When standing up the initial agent fleet and compute budgets need to be established.
- When a major fleet expansion requires a new allocation strategy that the existing framework cannot accommodate.
- When total compute budget has been set by leadership and needs to be distributed across the fleet.

## Workflow

1. **Define Total Budget**: Confirm the total compute budget available. Break down by cost categories: model API costs, tool access costs, infrastructure overhead. Deliverable: budget breakdown by category.
2. **Classify Agent Tiers**: Group agent roles into tiers based on compute requirements: high (complex reasoning, large context), medium (standard tasks), low (simple extraction, formatting). Deliverable: agent tier classification.
3. **Design Allocation Model**: Assign compute budget per tier. Include headroom for burst usage and new agent provisioning. Define how budget scales as the fleet grows. Deliverable: allocation model with per-tier budgets and scaling rules.
4. **Assign Per-Agent Budgets**: Translate tier budgets into specific per-agent allocations: model tier, max tokens per request, requests per day, and context window limits. Deliverable: per-agent budget assignments.
5. **Document and Communicate**: Publish the allocation strategy with clear rules for requesting budget increases and handling overages. Deliverable: allocation strategy document.

## Anti-Patterns

- **Equal distribution**: Splitting the budget equally across all agents regardless of role complexity. *Why*: simple agents receive budget they cannot use while complex agents are starved, degrading critical capabilities.
- **No growth headroom**: Allocating 100% of the budget to current agents with nothing reserved for new agents or burst usage. *Why*: fleet growth stalls when every new agent requires a budget renegotiation.
- **Budget without monitoring**: Setting budgets without tracking actual spend against allocation. *Why*: unmonitored budgets drift silently; overspending is discovered only when the bill arrives.

## Output

**On success**: Produces a compute allocation strategy containing budget breakdown, tier classifications, per-agent assignments, and scaling rules. Delivered to the VP Agent Operations and finance stakeholders.

**On failure**: Report what budget information was unavailable (unclear total budget, missing agent role list), what partial allocation was designed, and what decisions are needed to complete the strategy.

## Related Skills

- [`benefits-setup-v1`](../benefits-setup-v1/SKILL.md) -- Tool access setup complements compute allocation as part of initial fleet configuration.
- [`compensation-benchmarking`](../compensation-benchmarking/SKILL.md) -- Model benchmarking informs which tier each agent should occupy.
- [`equity-programme-manager`](../equity-programme-manager/SKILL.md) -- Premium resource allocation extends the initial allocation strategy.
