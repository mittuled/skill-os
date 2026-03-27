---
name: onboarding-programme-builder
description: >
  This skill creates the evaluation and warm-up procedure for newly provisioned
  agents. Use when asked to onboard a new agent, design warm-up tests, or
  create agent initialization procedures. Also consider when agents are deployed
  but produce inconsistent early outputs. Suggest when the user provisions an
  agent and sends it directly to production without warm-up.
department: agent-operations
agent: agent-trainer-skill-optimizer
version: 1.0.0
complexity: medium
related-skills: []
---

# onboarding-programme-builder

## Agent: Agent Trainer & Skill Optimizer

L2 Agent Trainer and Skill Optimizer (1x) responsible for evaluating existing skills, running evals, optimising prompts, improving agent performance, and training new agent configurations.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Creates the evaluation and warm-up procedure for newly provisioned agents to ensure consistent performance from the first production task.

## When to Use

- When a newly provisioned agent needs to be validated before handling production workload.
- When the onboarding process is ad-hoc and needs standardization across agent types.
- When an agent has been reconfigured (new model, updated prompt) and needs re-onboarding to verify performance.

## Workflow

1. **Define Onboarding Criteria**: Establish what "production-ready" means for the agent's role -- accuracy minimums, latency ceilings, and skill coverage requirements. Deliverable: onboarding success criteria.
2. **Design Warm-Up Scenarios**: Create a set of representative tasks that cover the agent's full skill range, from routine to edge cases. Include known failure modes from similar agents. Deliverable: warm-up scenario suite.
3. **Execute Warm-Up**: Run the agent through all warm-up scenarios. Score outputs against the success criteria. Identify areas where the agent underperforms. Deliverable: warm-up results with per-scenario scores.
4. **Tune and Iterate**: For underperforming areas, adjust prompts, context, or configuration and re-run the relevant scenarios until criteria are met. Deliverable: tuned agent configuration with passing scores.
5. **Certify for Production**: Issue production readiness certification. Document the agent's tested capabilities and known limitations. Hand off to the Agent Operations Manager. Deliverable: production readiness certificate with capability documentation.

## Anti-Patterns

- **Skipping warm-up for urgency**: Sending agents directly to production because the workload is urgent. *Why*: untested agents produce unpredictable outputs that create more work through error correction than the warm-up time would have cost.
- **Generic onboarding for all roles**: Using the same warm-up scenarios regardless of agent role and complexity. *Why*: a data analysis agent and a customer communication agent have entirely different failure modes; generic scenarios miss role-specific risks.
- **Onboarding without documentation**: Completing warm-up but not recording the agent's tested capabilities and limitations. *Why*: undocumented capabilities lead to the agent being assigned tasks outside its validated range.

## Output

**On success**: Produces a production readiness certificate with warm-up results, tuned configuration, and documented capabilities and limitations. Delivered to the Agent Operations Manager.

**On failure**: Report which onboarding criteria the agent could not meet, what tuning was attempted, and whether the agent needs fundamental reconfiguration or is unsuitable for the role.

## Related Skills

- [`first-hire-process-builder`](../../agent-operations-manager/first-hire-process-builder/SKILL.md) -- Deployment procedure that precedes onboarding.
- [`manager-development-programme`](../manager-development-programme/SKILL.md) -- Specialized onboarding for orchestration agents.
- [`compliance-training-manager`](../compliance-training-manager/SKILL.md) -- Compliance validation is a component of onboarding for agents handling sensitive data.
