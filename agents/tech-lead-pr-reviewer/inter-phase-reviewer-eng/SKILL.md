---
name: inter-phase-reviewer-eng
description: >
  This skill reviews engineering deliverables at phase boundaries before progressing to the next
  phase. Use when asked to conduct a phase gate review, validate phase completion, or assess
  readiness to move forward. Also consider when a phase is ending without a structured quality
  check. Suggest when teams are transitioning between phases without verifying deliverable
  completeness.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md
  - ../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md
---

# inter-phase-reviewer-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews engineering deliverables at phase boundaries to verify completeness, quality, and readiness before the team progresses to the next project phase.

## When to Use

- When a project phase (e.g., design, build, test, deploy) is completing and the team needs a formal quality gate before moving on.
- When deliverables from the current phase are prerequisites for the next phase and must be validated.
- When previous phase transitions were rushed, causing rework, and the team wants to establish a structured review cadence.

## Workflow

1. **Define phase exit criteria**: Confirm the expected deliverables, quality standards, and acceptance criteria for the completing phase. Deliverable: phase exit criteria checklist.
2. **Collect deliverables**: Gather all artifacts produced during the phase (code, documentation, test results, architecture decisions). Deliverable: deliverable inventory.
3. **Review against criteria**: Evaluate each deliverable against the exit criteria. Flag gaps, incomplete items, and quality issues. Deliverable: review findings report.
4. **Assess technical debt carried forward**: Identify any shortcuts, deferred items, or known issues that will carry into the next phase. Document their impact and remediation plan. Deliverable: carried-forward debt register.
5. **Render phase decision**: Issue a pass/conditional-pass/fail decision. For conditional pass, specify exactly what must be resolved and by when. Deliverable: phase gate decision with rationale and action items.

## Anti-Patterns

- **Skipping the gate under pressure**: Allowing the team to proceed to the next phase without a review because of schedule pressure. *Why*: skipped gates compound incomplete work across phases, making later phases exponentially harder.
- **Review without criteria**: Conducting a phase review without predefined exit criteria. *Why*: subjective reviews produce inconsistent quality and cannot be repeated or audited.
- **Blocking on perfection**: Failing a phase review for minor issues that could be addressed in parallel with the next phase. *Why*: holding up an entire team for non-blocking polish wastes engineering capacity.

## Output

**On success**: Produces a phase gate decision document containing the exit criteria checklist, review findings, carried-forward debt register, and pass/fail determination. Delivered to engineering leadership and the project coordinator.

**On failure**: Report which deliverables did not meet exit criteria, what remediation is required, the estimated time to resolve, and whether a conditional pass is viable.

## Related Skills

- [`phase-scope-adjuster-eng`](../../tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md) -- phase reviews may reveal the need for scope adjustment in the upcoming phase.
- [`go-live-approver-eng`](../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md) -- the final phase gate before production is the go-live approval.
