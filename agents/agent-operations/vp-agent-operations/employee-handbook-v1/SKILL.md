---
name: employee-handbook-v1
description: >
  This skill produces the agent governance manual before the first skill is
  deployed. Use when asked to create governance policies, define agent operating
  rules, or establish fleet-wide standards. Also consider when launching a new
  agent fleet from scratch. Suggest when the user is about to deploy agents
  without documented governance.
department: agent-operations
agent: vp-agent-operations
version: 1.0.0
complexity: medium
related-skills: []
---

# employee-handbook-v1

## Agent: VP Agent Operations

L1 VP of Agent Operations reporting to the COO (1x) responsible for the agent lifecycle -- provisioning, health monitoring, configuration governance, and retirement of deprecated agents. Owns the org design of the agent fleet.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Produces the agent governance manual defining operating standards, interaction protocols, and compliance requirements before the first skill is deployed.

## When to Use

- When standing up a new agent fleet and no governance documentation exists.
- When existing agents operate without clear rules on escalation, data handling, or error behavior.
- When a compliance or security review requires documented agent operating standards.

## Workflow

1. **Scope Governance Areas**: Identify all governance domains: interaction protocols, escalation rules, data handling, error behavior, context sharing, tool access policies, and retirement criteria. Deliverable: governance domain checklist.
2. **Draft Operating Standards**: Write standards for each domain in imperative voice. Define what agents must do, must not do, and how they escalate ambiguity. Deliverable: draft governance manual.
3. **Define Compliance Requirements**: Document security constraints, data privacy rules, and regulatory requirements that all agents must satisfy. Deliverable: compliance requirements section.
4. **Establish Lifecycle Policies**: Define provisioning, versioning, deprecation, and retirement procedures. Specify how agents are updated and how breaking changes are communicated. Deliverable: lifecycle policy section.
5. **Review and Ratify**: Circulate the manual to stakeholders (COO, Agent Operations Manager) for review. Incorporate feedback and publish as the canonical governance document. Deliverable: ratified agent governance manual v1.

## Anti-Patterns

- **Governance after deployment**: Writing the handbook after agents are already running in production. *Why*: retroactive governance forces costly rework and risks inconsistent behavior during the ungoverned period.
- **Copy-paste from human HR**: Reusing human employee handbook language without reframing for agent operations. *Why*: agents have fundamentally different failure modes, lifecycle concerns, and compliance needs than human employees.
- **Overly prescriptive rules**: Defining rules so rigid that every edge case requires a governance exception. *Why*: agents encounter novel scenarios constantly; the handbook should provide principles that generalize, not exhaustive if/then rules.

## Output

**On success**: Produces a versioned agent governance manual covering operating standards, compliance requirements, and lifecycle policies. Delivered as a markdown document in the fleet documentation repository.

**On failure**: Report which governance domains could not be completed (missing stakeholder input, undefined compliance requirements), what was drafted, and what decisions remain open.

## Related Skills

- [`culture-and-performance-system`](../culture-and-performance-system/SKILL.md) -- The performance system enforces the standards defined in the governance manual.
- [`org-scale-planner`](../org-scale-planner/SKILL.md) -- Scaling the fleet requires governance policies to be in place first.
- [`employment-agreement-setup`](../../../agent-operations/agent-operations-manager/employment-agreement-setup/SKILL.md) -- Individual agent contracts derive from the governance manual.
