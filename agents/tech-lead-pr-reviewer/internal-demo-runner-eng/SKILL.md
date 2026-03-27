---
name: internal-demo-runner-eng
description: >
  This skill runs internal engineering demos to showcase completed work to stakeholders. Use
  when asked to demo a feature, present sprint output, or run a show-and-tell session. Also
  consider when completed work is sitting unreviewed by stakeholders. Suggest when a sprint
  ends without a demo scheduled.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: simple
related-skills:
  - ../../tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md
  - ../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md
---

# internal-demo-runner-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Runs internal engineering demos to showcase completed work to stakeholders, collect feedback, and validate that delivered features meet expectations.

## When to Use

- When a sprint or milestone completes and stakeholders need to see working software before sign-off.
- When product or design teams need to validate that the implementation matches the specification.
- When engineering wants early feedback on an in-progress feature to course-correct before further investment.

## Workflow

1. **Prepare demo scope**: Select the features and fixes to demo. Prepare a working environment with realistic test data. Write a brief script covering what to show and in what order. Deliverable: demo script and prepared environment.
2. **Run the demo**: Walk stakeholders through each feature live, showing the happy path and key edge cases. Record the session for absent stakeholders. Deliverable: completed demo with recording.
3. **Collect and document feedback**: Capture stakeholder feedback, questions, and concerns. Triage items as bugs, enhancements, or out-of-scope. Deliverable: feedback log with triage.

## Anti-Patterns

- **Demo on broken environment**: Running the demo without verifying the environment works beforehand. *Why*: environment failures during a demo waste stakeholder time and undermine confidence in the team.
- **Demo without feedback capture**: Showing work without a structured mechanism to collect and act on feedback. *Why*: unrecorded feedback is lost, and stakeholders feel ignored when their input disappears.

## Output

**On success**: Produces a completed demo recording and a triaged feedback log. Delivered to the project management tool and shared with product, design, and engineering stakeholders.

**On failure**: Report what could not be demoed (e.g., environment issues, incomplete features), what was shown instead, and when a follow-up demo will be scheduled.

## Related Skills

- [`sprint-reviewer-eng`](../../tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md) -- sprint reviews assess completed work formally; demos present it to a broader audience.
- [`go-live-approver-eng`](../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md) -- demos generate stakeholder confidence that feeds into go-live approval decisions.
