---
name: phase-scope-adjuster-eng
description: >
  This skill adjusts engineering scope mid-phase in response to new information or blockers.
  Use when asked to cut scope, re-scope a phase, or adjust deliverables due to changed
  constraints. Also consider when velocity data shows the current scope cannot be completed
  on time. Suggest when a phase is at risk and no scope conversation has happened.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/inter-phase-reviewer-eng/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/dependency-resolver/SKILL.md
  - ../../vp-engineering/scope-boundary-setter-eng/SKILL.md
---

# phase-scope-adjuster-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Adjusts engineering scope mid-phase when new information, blockers, or velocity data indicates the current plan cannot be delivered within constraints.

## When to Use

- When mid-phase velocity data or burn-down trends indicate the team will not complete the planned scope by the phase deadline.
- When a newly discovered technical blocker or dependency forces removal or deferral of planned work items.
- When business priorities shift mid-phase and the team needs to swap in urgent work while maintaining a viable delivery plan.

## Workflow

1. **Assess the gap**: Compare planned scope against current velocity, remaining capacity, and known blockers. Quantify the shortfall. Deliverable: scope gap analysis.
2. **Identify adjustment options**: Generate options: (a) cut low-priority items, (b) reduce feature depth (MVP subset), (c) extend the timeline, (d) add capacity. Document tradeoffs for each. Deliverable: adjustment options with tradeoff analysis.
3. **Evaluate impact on dependencies**: Check whether proposed cuts or deferrals affect downstream phases, other teams, or committed deliverables. Deliverable: dependency impact assessment.
4. **Negotiate with stakeholders**: Present options to product and engineering leadership. Align on the chosen adjustment, documenting what is cut, deferred, or reduced. Deliverable: approved scope adjustment decision.
5. **Update plans and communicate**: Update the backlog, phase plan, and dependency map to reflect the adjusted scope. Notify all affected teams. Deliverable: updated phase plan and stakeholder communication.

## Anti-Patterns

- **Scope silence**: Knowing the phase is at risk but not raising it until the deadline passes. *Why*: late disclosure eliminates options and forces emergency decisions with worse outcomes.
- **Cutting quality instead of scope**: Reducing test coverage, skipping code review, or dropping observability to fit the timeline. *Why*: quality cuts create production incidents that cost more than the time they saved.
- **Adjusting without stakeholder alignment**: Unilaterally cutting scope without product or leadership agreement. *Why*: unilateral cuts break trust and may remove items that stakeholders consider non-negotiable.

## Output

**On success**: Produces an approved scope adjustment decision with the updated phase plan, deferred items list, dependency impact assessment, and stakeholder communication. Delivered to the project management tool and all affected teams.

**On failure**: Report why scope adjustment could not be agreed upon (e.g., stakeholder disagreement, no viable cut options), what alternatives were considered, and recommended escalation path.

## Related Skills

- [`inter-phase-reviewer-eng`](../../../engineering/tech-lead-pr-reviewer/inter-phase-reviewer-eng/SKILL.md) -- phase reviews may trigger scope adjustments when deliverables fall short of exit criteria.
- [`dependency-resolver`](../../../engineering/tech-lead-pr-reviewer/dependency-resolver/SKILL.md) -- unresolved dependencies are a common trigger for mid-phase scope adjustment.
