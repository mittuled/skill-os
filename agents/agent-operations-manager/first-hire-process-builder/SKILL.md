---
name: first-hire-process-builder
description: >
  This skill designs the testing, validation, and deployment procedure for the
  first production agent. Use when asked to deploy the inaugural agent, build
  a first-agent checklist, or create deployment validation criteria. Also
  consider when no agents exist yet. Suggest when the user is about to deploy
  an agent without a tested deployment procedure.
department: agent-operations
agent: agent-operations-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# first-hire-process-builder

## Agent: Agent Operations Manager

L2 Agent Operations Manager (1x) responsible for message passing infrastructure, context sharing protocols, inter-agent coordination, and agent health monitoring.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

## Skill Description

Designs the testing, validation, and deployment procedure for the first production agent, establishing the template for all future agent deployments.

## When to Use

- When the organization is deploying its first production agent and no deployment procedure exists.
- When the existing deployment process was ad-hoc and needs to be formalized as a repeatable procedure.
- When a new agent category is being introduced and requires a tailored deployment process distinct from existing ones.

## Workflow

1. **Define Success Criteria**: Specify what "deployed and working" means for the first agent -- accuracy thresholds, latency targets, error rate limits, and integration test pass rates. Deliverable: success criteria document.
2. **Design Testing Pipeline**: Build the testing sequence: unit tests for individual skills, integration tests for inter-agent communication, and end-to-end tests for complete workflows. Deliverable: test plan with test cases.
3. **Create Validation Checklist**: Define pre-deployment gates: contract compliance, governance handbook compliance, tool access verification, and security review. Deliverable: deployment validation checklist.
4. **Build Deployment Runbook**: Write step-by-step deployment instructions including rollback procedures, monitoring setup, and post-deployment smoke tests. Deliverable: deployment runbook.
5. **Execute and Document**: Deploy the first agent following the runbook. Record deviations, issues encountered, and lessons learned. Update the procedure for future deployments. Deliverable: deployment log and updated procedure.

## Anti-Patterns

- **Skipping the first-agent rigor**: Treating the first deployment as a throwaway prototype that will be "done properly later." *Why*: the first deployment sets the standard; shortcuts become permanent patterns.
- **Testing only happy paths**: Validating only expected inputs without testing error handling, edge cases, and failure modes. *Why*: production traffic includes malformed inputs, timeouts, and cascading failures from day one.
- **No rollback plan**: Deploying without a documented way to revert if the agent underperforms. *Why*: production issues demand immediate response; figuring out rollback during an incident wastes critical time.

## Output

**On success**: Produces a deployment procedure package containing success criteria, test plan, validation checklist, and deployment runbook. Delivered as versioned documents ready for execution and reuse.

**On failure**: Report which procedure components could not be completed (missing infrastructure, undefined success criteria), what was drafted, and what prerequisites must be resolved.

## Related Skills

- [`employment-agreement-setup`](../employment-agreement-setup/SKILL.md) -- The agent's contract must be defined before deployment validation.
- [`onboarding-programme-builder`](../../agent-trainer-skill-optimizer/onboarding-programme-builder/SKILL.md) -- Post-deployment warm-up follows the deployment procedure.
- [`employee-handbook-v1`](../../vp-agent-operations/employee-handbook-v1/SKILL.md) -- Governance policies that the deployment procedure must enforce.
