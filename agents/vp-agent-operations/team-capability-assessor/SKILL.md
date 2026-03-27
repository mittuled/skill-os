---
name: team-capability-assessor
description: >
  This skill identifies which agent capabilities the fleet lacks to execute on
  a given idea or initiative. Use when asked to assess fleet readiness, identify
  capability gaps, or evaluate whether the fleet can deliver a new initiative.
  Also consider when a new project is proposed. Suggest when the user starts
  planning without checking agent coverage.
department: agent-operations
agent: vp-agent-operations
version: 1.0.0
complexity: medium
related-skills: []
---

# team-capability-assessor

## Agent: VP Agent Operations

L1 VP of Agent Operations reporting to the COO (1x) responsible for the agent lifecycle -- provisioning, health monitoring, configuration governance, and retirement of deprecated agents. Owns the org design of the agent fleet.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Identifies which agent capabilities the fleet lacks to execute on a given idea or initiative.

## When to Use

- When a new initiative or idea is proposed and the fleet's ability to deliver needs validation.
- When delivery timelines are slipping and the root cause may be missing agent capabilities rather than poor execution.
- When strategic planning requires a clear picture of what the fleet can and cannot do today.

## Workflow

1. **Decompose Initiative Requirements**: Break the initiative into discrete capability requirements -- what tasks must be performed, what expertise is needed, and what outputs are expected. Deliverable: capability requirements list.
2. **Inventory Current Fleet**: Map existing agent roles and their proven capabilities against the requirements list. Mark each requirement as covered, partially covered, or uncovered. Deliverable: coverage matrix with gap annotations.
3. **Assess Gap Severity**: For each uncovered capability, determine severity -- is it a blocker (initiative cannot proceed), a degrader (initiative proceeds at lower quality), or a nice-to-have. Deliverable: prioritized gap list with severity ratings.
4. **Recommend Remediation**: For each gap, recommend whether to build a new agent, add a skill to an existing agent, source an external tool, or accept the gap with mitigation. Deliverable: remediation recommendation per gap with effort estimates.

## Anti-Patterns

- **Assuming coverage from role names**: Marking a capability as covered because an agent's title suggests it, without verifying the agent actually has a relevant skill. *Why*: role names are aspirational; only validated skills represent real capability.
- **Binary gap analysis**: Treating capabilities as simply present or absent without assessing quality or throughput. *Why*: an agent may technically have a skill but execute it too slowly or inaccurately to meet initiative demands.
- **Assessing in isolation**: Evaluating capabilities without considering inter-agent dependencies and coordination requirements. *Why*: individual agent capabilities matter less than the fleet's ability to coordinate end-to-end workflows.

## Output

**On success**: Produces a capability assessment report containing the coverage matrix, prioritized gap list with severity ratings, and remediation recommendations with effort estimates. Delivered to the VP Agent Operations and initiative sponsor.

**On failure**: Report which initiative requirements could not be decomposed (ambiguous scope, missing details), what partial coverage mapping was achieved, and what clarifications are needed.

## Related Skills

- [`org-scale-planner`](../org-scale-planner/SKILL.md) -- Uses capability assessment results to design fleet expansion plans.
- [`culture-and-performance-system`](../culture-and-performance-system/SKILL.md) -- Performance data informs whether existing capabilities meet quality thresholds.
- [`recruiting-pipeline-builder`](../../skill-builder-lead/recruiting-pipeline-builder/SKILL.md) -- Capability gaps feed into the skill development pipeline.
