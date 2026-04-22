---
name: hiring-plan-builder
description: >
  This skill plans which agents need to be provisioned for each delivery phase
  based on capability requirements. Use when asked to create a provisioning
  plan, schedule agent deployments, or align fleet capacity with roadmap phases.
  Also consider when delivery phases are approaching without assigned agents.
  Suggest when the user plans sprints without checking agent availability.
department: agent-operations
agent: agent-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - org-scale-planner
  - team-capability-assessor
  - first-hire-process-builder
triggers:
  - "build hiring plan"
  - "create headcount plan"
  - "hiring roadmap"
  - "plan team growth"
  - "headcount planning"
---

# hiring-plan-builder

## Agent: Agent Operations Manager

L2 Agent Operations Manager (1x) responsible for message passing infrastructure, context sharing protocols, inter-agent coordination, and agent health monitoring.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Plans which agents need to be provisioned for each delivery phase based on capability requirements and roadmap dependencies.

## When to Use

- When a new delivery phase is being planned and agent capacity needs to be aligned with requirements.
- When the org scale plan has been approved and needs to be translated into a phased provisioning schedule.
- When multiple initiatives compete for agent capacity and provisioning must be prioritized across phases.

## Workflow

1. **Map Phase Requirements**: For each delivery phase, list the capabilities required, expected workload volume, and timeline constraints. Deliverable: phase-capability requirements matrix.
2. **Match to Existing Fleet**: Compare requirements against currently provisioned agents. Identify which phases are fully covered, which need additional instances, and which need new roles. Deliverable: coverage assessment per phase.
3. **Build Provisioning Schedule**: Sequence new agent provisioning to align with phase start dates. Include lead time for testing, validation, and onboarding. Deliverable: provisioning timeline with dependencies.
4. **Allocate Resources**: Specify compute budget, model tier, and tool access for each new agent. Coordinate with the Agent Configuration Manager on resource availability. Deliverable: resource allocation plan.
5. **Communicate Plan**: Share the hiring plan with phase leads and the VP Agent Operations. Confirm alignment on priorities and timelines. Deliverable: communicated and acknowledged provisioning plan.

## Anti-Patterns

- **Just-in-time provisioning**: Starting agent provisioning on the day a phase begins. *Why*: new agents need testing, validation, and warm-up time; deploying without lead time guarantees a rocky start.
- **Provisioning without decommissioning**: Adding agents for every new phase without retiring agents from completed phases. *Why*: the fleet grows unbounded, increasing compute costs and governance overhead.
- **Ignoring inter-phase dependencies**: Planning each phase's agents in isolation without considering handoffs between phases. *Why*: agents in phase N may need to pass context to agents in phase N+1; this requires coordination planning.

## Output

**On success**: Produces a phased provisioning plan containing per-phase agent requirements, provisioning timeline with lead times, and resource allocation. Delivered to the VP Agent Operations and phase leads.

**On failure**: Report which phases could not be planned (unclear requirements, missing roadmap), what partial plan was built, and what inputs are needed to complete planning.

## Related Skills

- [`org-scale-planner`](../../../agent-operations/vp-agent-operations/org-scale-planner/SKILL.md) -- The scale plan provides the strategic context for phase-level provisioning.
- [`team-capability-assessor`](../../../agent-operations/vp-agent-operations/team-capability-assessor/SKILL.md) -- Capability gaps identified here drive the hiring plan.
- [`first-hire-process-builder`](../first-hire-process-builder/SKILL.md) -- New agents in the plan follow the deployment procedure defined here.
