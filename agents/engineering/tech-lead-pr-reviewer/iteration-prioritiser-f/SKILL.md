---
name: iteration-prioritiser-f
description: >
  This skill prioritises engineering iterations in the feedback phase based on impact and effort.
  Use when asked to prioritise feedback-driven work, rank iteration items, or decide what to
  fix next after user feedback. Also consider when the team has more feedback items than capacity.
  Suggest when feedback is piling up without a clear prioritisation framework.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/iteration-prioritiser-p-eng/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md
triggers:
  - "prioritize iteration"
  - "iteration prioritization"
  - "sprint prioritization"
  - "rank iteration tasks"
  - "iteration backlog prioritization"
---

# iteration-prioritiser-f

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Prioritises engineering iterations during the feedback phase by ranking items based on user impact, engineering effort, and alignment with product goals.

## When to Use

- When user feedback, beta testing, or internal demos have generated a list of issues and enhancements that exceeds the team's capacity.
- When the feedback phase begins and the team needs a structured approach to decide which items to address first.
- When stakeholders disagree on feedback priority and the tech lead needs to provide an objective ranking framework.

## Workflow

1. **Collect and categorize feedback**: Aggregate all feedback items from user testing, demos, and bug reports. Categorize each as bug, usability issue, missing feature, or enhancement. Deliverable: categorized feedback inventory.
2. **Score impact and effort**: For each item, assess user impact (severity, frequency, user segment affected) and engineering effort (complexity, risk, dependencies). Deliverable: impact-effort scoring matrix.
3. **Apply prioritisation framework**: Rank items using impact-effort analysis, placing high-impact/low-effort items first. Factor in product goals and upcoming milestones. Deliverable: prioritised iteration backlog.
4. **Communicate priorities**: Share the prioritised list with product, design, and engineering. Explain the rationale for top-priority items and what was deprioritised and why. Deliverable: published priority list with rationale.
5. **Plan iteration scope**: Select items that fit within the iteration's capacity. Define acceptance criteria for each selected item. Deliverable: scoped iteration plan.

## Anti-Patterns

- **Recency bias**: Prioritising the most recently reported feedback over older, higher-impact items. *Why*: recency bias leads to thrashing and leaves systemic issues unaddressed.
- **Treating all feedback equally**: Working through feedback items in the order received without scoring impact. *Why*: first-in-first-out prioritisation ignores severity and wastes capacity on low-impact items.
- **Ignoring engineering effort**: Prioritising purely on user impact without considering implementation cost. *Why*: high-impact items that require disproportionate effort may not be the best use of a short iteration cycle.

## Output

**On success**: Produces a prioritised iteration backlog with impact-effort scores, a scoped iteration plan, and published rationale. Delivered to the project management tool and communicated to product and engineering teams.

**On failure**: Report which feedback items could not be scored (e.g., unclear reproduction steps, unknown user impact), what information is missing, and recommended steps to complete prioritisation.

## Related Skills

- [`iteration-prioritiser-p-eng`](../../../engineering/tech-lead-pr-reviewer/iteration-prioritiser-p-eng/SKILL.md) -- post-launch iteration prioritisation uses similar methods but operates on production data rather than beta feedback.
- [`backlog-groomer-eng`](../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md) -- prioritised feedback items feed into the backlog for grooming and sprint planning.
