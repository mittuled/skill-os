---
name: manager-development-programme
description: >
  This skill trains orchestration agents on delegation, context management,
  and multi-agent coordination. Use when asked to improve orchestrator
  performance, design coordination training, or optimize multi-agent workflows.
  Also consider when orchestration agents produce poor delegation decisions.
  Suggest when the user adds new agents without updating orchestrator training.
department: agent-operations
agent: agent-trainer-skill-optimizer
version: 1.0.0
complexity: medium
related-skills: []
---

# manager-development-programme

## Agent: Agent Trainer & Skill Optimizer

L2 Agent Trainer and Skill Optimizer (1x) responsible for evaluating existing skills, running evals, optimising prompts, improving agent performance, and training new agent configurations.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Trains orchestration agents on delegation, context management, and multi-agent coordination to improve fleet-wide workflow execution.

## When to Use

- When orchestration agents are making poor delegation decisions, routing tasks to wrong agents or overloading specific agents.
- When new agents have been added to the fleet and orchestrators need updated awareness of available capabilities.
- When multi-agent workflows are failing due to context loss during handoffs between agents.

## Workflow

1. **Assess Orchestrator Performance**: Evaluate current orchestration agents on delegation accuracy, context preservation during handoffs, and coordination efficiency. Deliverable: orchestrator performance baseline.
2. **Identify Training Gaps**: Analyze delegation errors, context loss incidents, and coordination failures to determine specific training needs. Deliverable: training gap analysis.
3. **Design Training Programme**: Create training scenarios covering delegation logic (which agent for which task), context packaging (what to include in handoffs), and coordination patterns (sequential, parallel, fan-out). Deliverable: training programme with scenario sets.
4. **Execute Training**: Run orchestration agents through training scenarios. Evaluate outputs against expected delegation decisions and context handling. Iterate on prompt updates and configuration changes. Deliverable: training results with before/after comparison.
5. **Validate and Deploy**: Confirm improved orchestration performance meets thresholds. Deploy updated configurations to production orchestrators. Deliverable: validated orchestrator configurations.

## Anti-Patterns

- **Training on happy paths only**: Practicing delegation with clear-cut scenarios but never with ambiguous or multi-valid-answer tasks. *Why*: production orchestration frequently involves ambiguous routing where multiple agents could handle the task; training must cover these cases.
- **Ignoring context window budgets**: Training orchestrators to pass full context without considering downstream agents' context window limits. *Why*: oversized context causes truncation or overflow, leading to lost information at the worst possible moment.
- **Static training**: Training once and never refreshing as the fleet evolves. *Why*: the orchestrator's knowledge of available agents and their capabilities becomes stale, leading to misroutes.

## Output

**On success**: Produces updated orchestrator configurations with improved delegation logic, context management, and coordination patterns. Delivered as deployed configurations with performance improvement metrics.

**On failure**: Report which training scenarios the orchestrator still fails, what prompt or configuration changes were attempted, and what additional training data or scenarios are needed.

## Related Skills

- [`onboarding-programme-builder`](../onboarding-programme-builder/SKILL.md) -- New agent onboarding feeds into orchestrator awareness updates.
- [`skills-gap-analyser`](../skills-gap-analyser/SKILL.md) -- Skill gaps in orchestrators are a specific case of the broader gap analysis.
- [`team-health-monitor`](../../agent-operations-manager/team-health-monitor/SKILL.md) -- Coordination failures surface as health monitoring anomalies.
