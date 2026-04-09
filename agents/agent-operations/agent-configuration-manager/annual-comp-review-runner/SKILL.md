---
name: annual-comp-review-runner
description: >
  This skill reviews whether each agent's model, compute, and tool access are
  appropriately sized annually. Use when asked to run the annual configuration
  review, right-size agent resources, or audit tool access. Also consider when
  agent costs have drifted from budget. Suggest when a year has passed since
  the last configuration review.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run annual config review"
  - "right-size agent resources"
  - "audit tool access"
  - "annual configuration review"
  - "agent resource audit"
---

# annual-comp-review-runner

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Reviews whether each agent's model, compute budget, and tool access are appropriately sized through an annual configuration audit.

## When to Use

- When the annual configuration review cycle is due.
- When fleet compute costs have drifted significantly from the allocated budget.
- When new model tiers or tools have become available and existing agent configurations may be suboptimal.

## Workflow

1. **Gather Configuration Baselines**: Collect each agent's current configuration: model tier, compute allocation, context window size, tool access list, and API key scope. Deliverable: configuration inventory.
2. **Collect Performance and Cost Data**: Pull per-agent performance metrics and cost data from the past year. Include ROI assessments and health monitoring trends. Deliverable: annual performance and cost dataset.
3. **Assess Right-Sizing**: Compare each agent's configuration to its actual usage. Identify over-provisioned agents (paying for capacity not used) and under-provisioned agents (performance degraded by resource constraints). Deliverable: right-sizing assessment per agent.
4. **Propose Configuration Changes**: For each misaligned agent, propose specific changes -- model upgrade/downgrade, compute budget adjustment, tool access addition/removal. Include cost impact estimates. Deliverable: configuration change proposals with cost impact.
5. **Execute Approved Changes**: Implement approved configuration changes. Verify each change does not regress agent performance. Deliverable: updated configurations with post-change validation.

## Anti-Patterns

- **Review without data**: Making configuration decisions based on intuition rather than actual usage and performance data. *Why*: subjective assessments lead to either wasteful over-provisioning or harmful under-provisioning.
- **Annual-only reviews**: Treating the annual review as the only time configurations can change. *Why*: significant events (model releases, cost spikes, new tools) require mid-cycle adjustments.
- **Blanket changes**: Applying the same configuration adjustment to all agents without per-agent analysis. *Why*: each agent has different workload patterns and performance requirements; uniform changes inevitably misfit some agents.

## Output

**On success**: Produces an annual configuration review report containing right-sizing assessments, approved configuration changes, and post-change validation results. Delivered to the VP Agent Operations.

**On failure**: Report which agents could not be reviewed (missing data, unavailable metrics), what partial assessment was completed, and what data gaps need to be closed.

## Related Skills

- [`409a-valuation-commissioner`](../409a-valuation-commissioner/SKILL.md) -- ROI data feeds into annual right-sizing decisions.
- [`compensation-benchmarking`](../compensation-benchmarking/SKILL.md) -- Model benchmarking informs upgrade/downgrade recommendations.
- [`benefits-programme-administrator`](../benefits-programme-administrator/SKILL.md) -- Tool access changes are executed through the benefits programme.
