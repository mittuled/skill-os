---
name: dependency-resolver
description: >
  This skill resolves dependency conflicts and unblocks engineering tasks when blockers arise.
  Use when asked to unblock a team, resolve a dependency conflict, or find workarounds for
  blocked tasks. Also consider when a cross-team dependency is stalling the critical path.
  Suggest when engineers have been blocked for more than one day without a resolution plan.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/dependency-mapper/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md
---

# dependency-resolver

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Resolves dependency conflicts and unblocks engineering tasks by negotiating with blocking teams, finding workarounds, or restructuring task sequencing.

## When to Use

- When an engineering task is blocked by an upstream dependency that is not delivering on the expected timeline.
- When two or more teams have conflicting requirements on a shared resource, API, or data model.
- When the critical path is stalling because a cross-team or third-party dependency has no clear owner or resolution plan.

## Workflow

1. **Diagnose the blocker**: Identify the exact dependency causing the block, its owner, and the reason it is delayed or conflicting. Deliverable: blocker diagnosis with root cause.
2. **Assess impact**: Determine what downstream work is affected, how many teams are impacted, and the timeline cost of inaction. Deliverable: impact assessment.
3. **Identify resolution options**: Generate at least two options: (a) accelerate the blocking dependency, (b) find a workaround (stub, mock, interface contract), (c) resequence work to pull in non-blocked tasks. Deliverable: resolution options with tradeoffs.
4. **Negotiate and decide**: Coordinate with the blocking team or vendor. Present options to stakeholders and select the resolution path. Deliverable: agreed resolution plan with owner and timeline.
5. **Execute and verify**: Implement the chosen resolution, update the dependency map, and confirm the previously blocked task can now proceed. Deliverable: updated task status and dependency map.

## Anti-Patterns

- **Waiting silently**: Leaving a blocked task in "blocked" status without actively pursuing resolution. *Why*: blockers do not resolve themselves; passive waiting compounds schedule delay.
- **Heroic workarounds**: Implementing complex workarounds without updating the dependency map or informing stakeholders. *Why*: undocumented workarounds create hidden technical debt and surprise failures later.
- **Escalation as first resort**: Immediately escalating to leadership instead of first attempting direct resolution with the blocking team. *Why*: premature escalation damages cross-team trust and slows resolution by adding layers.

## Output

**On success**: Produces an executed resolution plan with the blocker removed, updated dependency map, and confirmation that downstream work is unblocked. Delivered to the project management tool and communicated to affected teams.

**On failure**: Report the blocker that could not be resolved, what options were attempted, why they failed, and a recommended escalation path with specific asks for leadership.

## Related Skills

- [`dependency-mapper`](../../../engineering/tech-lead-pr-reviewer/dependency-mapper/SKILL.md) -- dependency mapping identifies the blockers that this skill resolves.
- [`phase-scope-adjuster-eng`](../../../engineering/tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md) -- when a dependency cannot be resolved, scope adjustment may be needed to keep the phase on track.
