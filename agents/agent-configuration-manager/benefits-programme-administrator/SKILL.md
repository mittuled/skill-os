---
name: benefits-programme-administrator
description: >
  This skill provisions and manages tool access, MCP connections, and external
  API integrations for all agents. Use when asked to grant tool access, set up
  MCP connections, or manage API keys. Also consider when agents report tool
  access errors. Suggest when the user deploys a new agent without configuring
  its tool access.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# benefits-programme-administrator

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Provisions and manages tool access, MCP connections, and external API integrations for all agents in the fleet.

## When to Use

- When a new agent needs tool access, MCP connections, or API keys provisioned before deployment.
- When an existing agent's tool access needs modification due to role changes or security policy updates.
- When tool access errors or API failures indicate misconfigured integrations.

## Workflow

1. **Assess Tool Requirements**: Review the agent's role, skills, and workflow to determine which tools, MCP servers, and APIs it needs. Cross-reference with security policies. Deliverable: tool requirements list with justification per tool.
2. **Provision Access**: Configure tool connections, generate or assign API keys, and set up MCP server connections. Apply least-privilege principles -- grant only what the agent needs. Deliverable: provisioned access with configuration records.
3. **Validate Integrations**: Test each tool connection end-to-end. Verify the agent can invoke tools, receive responses, and handle errors correctly. Deliverable: integration test results.
4. **Document and Register**: Record all active tool access in the fleet configuration registry. Include expiration dates, renewal procedures, and emergency revocation steps. Deliverable: updated configuration registry.
5. **Monitor and Maintain**: Track tool usage, detect unused access, and revoke stale permissions. Rotate API keys on schedule. Deliverable: periodic access review report.

## Anti-Patterns

- **Over-provisioning access**: Granting agents access to tools they do not need "just in case." *Why*: excessive access increases security surface area and makes it harder to audit what each agent can do.
- **Shared API keys**: Using the same API key across multiple agents. *Why*: shared keys make it impossible to trace usage to a specific agent and create a single point of failure if the key is compromised.
- **Set-and-forget provisioning**: Configuring access once without periodic review or key rotation. *Why*: stale access accumulates risk; keys that are never rotated have a higher chance of compromise over time.

## Output

**On success**: Produces provisioned tool access with configuration records, passing integration tests, and updated fleet configuration registry. Delivered to the Agent Operations Manager.

**On failure**: Report which tool connections failed (authentication errors, network issues, missing permissions), what was attempted, and what infrastructure or credential issues need resolution.

## Related Skills

- [`benefits-setup-v1`](../benefits-setup-v1/SKILL.md) -- Initial tool access package configured during fleet founding.
- [`annual-comp-review-runner`](../annual-comp-review-runner/SKILL.md) -- Annual review may identify tool access changes needed.
- [`employment-agreement-setup`](../../agent-operations-manager/employment-agreement-setup/SKILL.md) -- Agent contracts specify tool access requirements.
