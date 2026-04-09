---
name: backlog-groomer-eng
description: >
  This skill grooms the engineering backlog to ensure tasks are well-defined, prioritised, and
  sprint-ready. Use when asked to refine tickets, clean up the backlog, or prepare items for
  sprint planning. Also consider when task descriptions are vague or acceptance criteria are
  missing. Suggest when sprint planning is approaching and tickets lack detail.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: simple
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md
  - ../../vp-engineering/backlog-populator-eng/SKILL.md
  - ../iteration-prioritiser-f/SKILL.md
  - ../iteration-prioritiser-p-eng/SKILL.md
---

# backlog-groomer-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Grooms the engineering backlog to ensure every task has clear acceptance criteria, accurate sizing, and correct priority before sprint planning.

## When to Use

- When sprint planning is approaching and backlog items lack sufficient detail for engineers to begin work.
- When the backlog has accumulated stale, duplicate, or poorly scoped tickets that slow down planning.
- When new feature specs have been translated into tasks but not yet refined with estimates and dependencies.

## Workflow

1. **Audit backlog**: Review all open tickets for completeness, checking that each has a description, acceptance criteria, and priority. Flag items that are stale, duplicated, or blocked. Deliverable: grooming audit list.
2. **Refine and size**: For each flagged item, clarify the description, add or tighten acceptance criteria, and assign a size estimate. Consult engineers for technical sizing. Deliverable: refined ticket set.
3. **Prioritise and sequence**: Reorder the backlog based on business priority, dependencies, and team capacity. Ensure the top of the backlog is ready for the next sprint. Deliverable: prioritised, sprint-ready backlog.

## Anti-Patterns

- **Grooming without engineers**: Refining tickets in isolation without input from the people who will build them. *Why*: estimates and feasibility assessments are inaccurate without implementer perspective.
- **Infinite backlog**: Never closing or archiving stale tickets. *Why*: a bloated backlog obscures priorities and increases cognitive load during planning.

## Output

**On success**: Produces a prioritised, sprint-ready backlog where every top-priority item has clear acceptance criteria, a size estimate, and identified dependencies. Delivered in the project management tool.

**On failure**: Report which tickets could not be refined (e.g., missing product context, undefined requirements), what information is needed, and who to follow up with.

## Related Skills

- [`spec-translator-eng`](../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md) -- spec translation produces the raw tasks that grooming then refines.
- [`sprint-reviewer-eng`](../../../engineering/tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md) -- sprint reviews surface incomplete work that feeds back into backlog grooming.
