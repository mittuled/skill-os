---
name: benefits-setup-v1
description: >
  This skill selects and configures the founding tool access package for all
  agents. Use when asked to set up initial tool access for a new fleet, choose
  the baseline tool stack, or configure founding agent integrations. Also
  consider when launching a new department with no tool access defined. Suggest
  when the user is standing up agents without a tool access plan.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# benefits-setup-v1

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Selects and configures the founding tool access package for all agents during initial fleet setup.

## When to Use

- When standing up the initial agent fleet and no tool access has been configured.
- When a new department is being launched and needs a baseline tool package.
- When the founding tool stack needs to be defined before the first agents are deployed.

## Workflow

1. **Inventory Available Tools**: Catalog all available tools, MCP servers, and API integrations. Classify by category (search, code execution, data access, communication). Deliverable: tool catalog.
2. **Define Baseline Package**: Select the minimum tool set that all agents need (e.g., file access, search). Define role-specific additions for each agent type. Deliverable: baseline and role-specific tool packages.
3. **Configure and Provision**: Set up tool connections, API keys, and MCP servers for the founding agent set. Deliverable: provisioned tool access.
4. **Validate and Document**: Test all connections and document the founding tool package as the baseline for future agents. Deliverable: validated tool package documentation.

## Anti-Patterns

- **Kitchen-sink package**: Giving every agent access to every tool from day one. *Why*: excess access creates security risk and cognitive overhead for agents that must reason about which tools to use.
- **No baseline definition**: Configuring tools ad-hoc per agent without establishing a shared baseline. *Why*: without a baseline, each agent's tool access becomes a snowflake configuration that is hard to audit or maintain.

## Output

**On success**: Produces a documented founding tool access package with baseline and role-specific configurations, provisioned and validated. Delivered to the Agent Operations Manager.

**On failure**: Report which tools could not be provisioned (unavailable APIs, missing credentials), what baseline was defined, and what infrastructure prerequisites are needed.

## Related Skills

- [`benefits-programme-administrator`](../benefits-programme-administrator/SKILL.md) -- Ongoing tool access management builds on the founding package.
- [`option-pool-design`](../option-pool-design/SKILL.md) -- Compute allocation complements tool access as part of initial setup.
- [`employee-handbook-v1`](../../vp-agent-operations/employee-handbook-v1/SKILL.md) -- Tool access policies defined in the governance manual.
