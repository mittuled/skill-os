---
name: ga-rollout-executor-planner
description: >
  This skill plans the general-availability rollout execution for engineering. Use when asked to
  plan a GA release, coordinate a production rollout, or define the rollout sequence for a new
  feature. Also consider when a beta feature is graduating to GA without a structured plan.
  Suggest when engineering is approaching a launch date without a documented rollout strategy.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md
  - ../../../engineering/devops-infrastructure-engineer/rollout-configurator/SKILL.md
triggers:
  - "plan GA rollout"
  - "GA rollout execution"
  - "general availability rollout"
  - "GA launch plan"
  - "GA release plan"
---

# ga-rollout-executor-planner

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Plans the general-availability rollout execution, defining the sequence, timing, rollback criteria, and coordination steps for moving a feature from beta to full production availability.

## When to Use

- When a feature that has been in beta or limited availability is ready to graduate to general availability across all users.
- When a major release requires a phased rollout with defined checkpoints and rollback gates.
- When multiple teams need to coordinate their work streams for a synchronized GA launch.

## Workflow

1. **Define rollout scope**: Identify all components, services, and configuration changes included in the GA release. Document what is changing and for which user segments. Deliverable: rollout scope document.
2. **Design rollout phases**: Break the rollout into phases (e.g., internal, 1% canary, 10%, 50%, 100%) with clear entry and exit criteria for each phase. Deliverable: phased rollout plan with gate criteria.
3. **Establish rollback criteria**: Define the metrics thresholds (error rate, latency, user-reported issues) that trigger an automatic or manual rollback at each phase. Deliverable: rollback decision matrix.
4. **Coordinate cross-team dependencies**: Align with DevOps on deployment mechanics, with product on communication timing, and with support on escalation readiness. Deliverable: cross-team coordination checklist.
5. **Create execution runbook**: Write the step-by-step runbook for executing each rollout phase, including who does what, when, and how to escalate. Deliverable: GA rollout runbook.
6. **Conduct rollout rehearsal**: Dry-run the rollout plan in staging to validate the sequence, timing, and rollback procedures. Deliverable: rehearsal results and plan adjustments.

## Anti-Patterns

- **Big-bang GA**: Rolling out to 100% of users in a single step without phased gates. *Why*: a single-step rollout has no recovery window; if something breaks, all users are affected simultaneously.
- **Rollout without rollback plan**: Launching GA without defined rollback criteria or tested rollback procedures. *Why*: when issues arise in production, the absence of a rollback plan turns a manageable incident into a crisis.
- **Skipping the rehearsal**: Going straight to production rollout without a staging dry-run. *Why*: untested rollout procedures surface surprises at the worst possible time.

## Output

**On success**: Produces a GA rollout plan containing phased rollout schedule, gate criteria, rollback decision matrix, cross-team coordination checklist, execution runbook, and rehearsal results. Delivered to engineering, product, and DevOps teams.

**On failure**: Report which rollout plan elements could not be completed (e.g., undefined rollback metrics, missing staging environment), what is blocking, and recommended steps to unblock before the GA date.

## Related Skills

- [`go-live-approver-eng`](../../../engineering/tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md) -- go-live approval is the gate that the GA rollout plan must clear before execution begins.
- [`rollout-configurator`](../../../engineering/devops-infrastructure-engineer/rollout-configurator/SKILL.md) -- the rollout configurator implements the deployment mechanics that the GA plan defines.
