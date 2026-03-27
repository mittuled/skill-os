---
name: sprint-reviewer-eng
description: >
  This skill runs engineering sprint reviews to assess completed work against acceptance
  criteria. Use when asked to review a sprint, evaluate sprint output, or conduct a sprint
  retrospective. Also consider when a sprint ends without a formal review. Suggest when the
  team is closing a sprint and no review session is scheduled.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md
  - ../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md
---

# sprint-reviewer-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Runs engineering sprint reviews to assess completed work against acceptance criteria, identify incomplete items, and capture lessons for future sprints.

## When to Use

- When a sprint ends and the team needs to formally assess which tasks met their acceptance criteria and which did not.
- When stakeholders want visibility into engineering progress and delivery velocity at regular intervals.
- When the team needs to identify patterns in incomplete work or recurring blockers across sprints.

## Workflow

1. **Prepare review materials**: Collect the sprint backlog, completed tasks, and their acceptance criteria. Pull velocity metrics and burn-down data. Deliverable: sprint review preparation package.
2. **Assess completion**: For each task, verify whether acceptance criteria are fully met, partially met, or not met. Collect evidence (test results, demos, PR links). Deliverable: task completion assessment.
3. **Identify carryover and blockers**: Document tasks that were not completed, the reasons why (scope creep, blockers, estimation errors), and their disposition (carry to next sprint, deprioritise, or split). Deliverable: carryover list with root causes.
4. **Capture velocity and trends**: Calculate sprint velocity and compare against recent sprints. Identify trends in estimation accuracy, blocker frequency, and throughput. Deliverable: velocity trend analysis.
5. **Document lessons and actions**: Record what went well, what did not, and specific action items for the next sprint. Assign owners to each action item. Deliverable: sprint review summary with action items.

## Anti-Patterns

- **Skipping the review**: Closing the sprint without reviewing completed work because the team is eager to start the next one. *Why*: unreviewed sprints hide incomplete work that compounds across iterations and degrades delivery predictability.
- **Review without data**: Conducting the review based on memory rather than metrics and evidence. *Why*: subjective assessments miss patterns and make it impossible to track improvement over time.
- **Blame-oriented review**: Focusing on who failed rather than what systemic issues caused incomplete work. *Why*: blame discourages transparency and prevents the team from surfacing the root causes that actually need fixing.

## Output

**On success**: Produces a sprint review summary containing task completion assessment, carryover list with root causes, velocity trend analysis, and action items with owners. Delivered to the project management tool and shared with product and engineering teams.

**On failure**: Report which tasks could not be assessed (e.g., missing acceptance criteria, unavailable test results), what information is needed, and when a follow-up review will occur.

## Related Skills

- [`backlog-groomer-eng`](../../tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md) -- sprint review carryover items feed back into backlog grooming for the next sprint.
- [`go-live-approver-eng`](../../tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md) -- sprint review completion evidence supports go-live approval decisions.
