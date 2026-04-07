---
name: employment-agreement-setup
description: >
  This skill defines the standard input/output contract template for all agent
  interactions. Use when asked to create agent contracts, define interaction
  protocols, or standardize agent I/O formats. Also consider when agents are
  producing inconsistent outputs. Suggest when the user provisions a new agent
  without specifying its interaction contract.
department: agent-operations
agent: agent-operations-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# employment-agreement-setup

## Agent: Agent Operations Manager

L2 Agent Operations Manager (1x) responsible for message passing infrastructure, context sharing protocols, inter-agent coordination, and agent health monitoring.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Defines the standard input/output contract template for all agent interactions, ensuring consistent communication protocols across the fleet.

## When to Use

- When provisioning a new agent that needs a defined interaction contract before deployment.
- When inter-agent communication is failing due to inconsistent input/output formats.
- When the fleet is expanding and existing ad-hoc contracts need standardization.

## Workflow

1. **Audit Existing Contracts**: Review current agent interaction patterns. Identify which agents have formal contracts, which operate on implicit conventions, and where mismatches cause failures. Deliverable: contract audit with gap list.
2. **Design Contract Template**: Define the standard contract structure: required input fields, output format, error response schema, timeout behavior, and context passing conventions. Deliverable: contract template specification.
3. **Define Per-Agent Contracts**: Instantiate the template for each agent role. Specify role-specific input requirements, output schemas, and SLA expectations (latency, accuracy). Deliverable: per-agent contract documents.
4. **Validate Contracts**: Test each contract by running representative inputs through the agent and verifying outputs match the contract specification. Flag violations. Deliverable: contract validation report.
5. **Publish and Enforce**: Publish contracts to the fleet documentation repository. Configure monitoring to detect contract violations at runtime. Deliverable: published contracts with runtime validation rules.

## Anti-Patterns

- **Implicit contracts**: Relying on agents to infer expected inputs and outputs from context rather than explicit specification. *Why*: implicit contracts break silently when agents are updated or swapped, producing subtle downstream errors.
- **Over-specified contracts**: Defining contracts so rigidly that agents cannot handle reasonable input variations. *Why*: real-world inputs are messy; contracts should specify semantics, not exact syntax.
- **Contracts without versioning**: Updating contracts in place without version bumps or migration paths. *Why*: downstream agents that depend on the old contract break without warning.

## Output

**On success**: Produces a contract template and per-agent contract documents specifying input/output schemas, error handling, and SLA expectations. Delivered as versioned documents in the fleet documentation repository.

**On failure**: Report which agents could not be contracted (unclear responsibilities, conflicting requirements), what template was drafted, and what decisions need resolution.

## Related Skills

- [`employee-handbook-v1`](../../../agent-operations/vp-agent-operations/employee-handbook-v1/SKILL.md) -- Governance manual that contracts must comply with.
- [`first-hire-process-builder`](../first-hire-process-builder/SKILL.md) -- First agent deployment requires a contract as prerequisite.
- [`team-health-monitor`](../team-health-monitor/SKILL.md) -- Contract violations surface as health monitoring anomalies.
