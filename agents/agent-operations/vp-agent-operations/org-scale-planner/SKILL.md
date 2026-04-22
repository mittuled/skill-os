---
name: org-scale-planner
description: >
  This skill designs the agent topology, role definitions, and provisioning plan
  for the scale phase. Use when asked to plan fleet expansion, define new agent
  roles, or restructure the agent org. Also consider when workload exceeds
  current fleet capacity. Suggest when the user is scaling product scope without
  reviewing agent capacity.
department: agent-operations
agent: vp-agent-operations
version: 1.0.0
complexity: complex
related-skills:
  - team-capability-assessor
  - employee-handbook-v1
  - hiring-plan-builder
triggers:
  - "plan org scale"
  - "org growth planning"
  - "scale org structure"
  - "headcount scale plan"
  - "organisational scaling"
---

# org-scale-planner

## Agent: VP Agent Operations

L1 VP of Agent Operations reporting to the COO (1x) responsible for the agent lifecycle -- provisioning, health monitoring, configuration governance, and retirement of deprecated agents. Owns the org design of the agent fleet.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Designs the agent topology, role definitions, and provisioning plan for scaling the agent fleet to meet growing capability demands.

## When to Use

- When the product roadmap requires capabilities that exceed the current agent fleet's capacity.
- When the organization is transitioning from founding phase to scale phase and needs a structured fleet expansion plan.
- When agent utilization metrics show consistent overload across multiple roles, signaling the need for fleet redesign.

## Workflow

1. **Demand Assessment**: Inventory all capability requirements from the product roadmap, active initiatives, and backlog. Map each requirement to an existing agent role or flag as a gap. Deliverable: capability demand matrix with gap annotations.
2. **Current State Audit**: Document the existing agent topology -- roles, instance counts, dependencies, and utilization rates. Identify bottlenecks where single-instance agents block parallel work. Deliverable: current-state topology map with utilization data.
3. **Topology Design**: Design the target-state topology including new roles, multi-instance scaling decisions (1x vs Nx), reporting lines, and inter-agent coordination patterns. Define clear role boundaries to avoid overlap. Deliverable: target-state topology diagram with role definitions.
4. **Provisioning Plan**: Sequence the rollout of new agents and role changes. Prioritize by business impact and dependency order. Specify model tier, compute budget, and tool access for each new role. Deliverable: phased provisioning plan with resource requirements.
5. **Migration Strategy**: Plan how existing agents transition to the new topology -- role splits, responsibility transfers, and deprecation of redundant agents. Define rollback criteria if new agents underperform. Deliverable: migration runbook with rollback triggers.
6. **Stakeholder Alignment**: Present the scale plan to COO and department leads. Incorporate feedback on priorities and constraints. Deliverable: approved scale plan with stakeholder sign-off.

## Anti-Patterns

- **Scaling by cloning**: Creating duplicate agents with identical roles instead of designing specialized sub-roles. *Why*: cloned agents produce redundant outputs and create coordination overhead without improving capability coverage.
- **Big-bang deployment**: Provisioning all new agents simultaneously without phased rollout. *Why*: simultaneous deployment makes it impossible to isolate failures or measure the impact of individual additions.
- **Ignoring retirement**: Adding new agents without deprecating roles that are no longer needed. *Why*: accumulated unused agents waste compute budget and create governance surface area with no business value.

## Output

**On success**: Produces a scale plan document containing the target topology, phased provisioning schedule, resource requirements, and migration runbook. Delivered to the COO and Agent Operations Manager for execution.

**On failure**: Report which parts of the plan could not be completed (unclear roadmap inputs, missing utilization data), what was designed so far, and what information is needed to finish.

## Related Skills

- [`team-capability-assessor`](../team-capability-assessor/SKILL.md) -- Provides the capability gap analysis that informs scaling decisions.
- [`employee-handbook-v1`](../employee-handbook-v1/SKILL.md) -- Governance policies that new agents must comply with.
- [`hiring-plan-builder`](../../../agent-operations/agent-operations-manager/hiring-plan-builder/SKILL.md) -- Translates the scale plan into operational provisioning tasks.
