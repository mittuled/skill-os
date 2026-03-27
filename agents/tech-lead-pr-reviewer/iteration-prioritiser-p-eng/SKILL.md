---
name: iteration-prioritiser-p-eng
description: >
  This skill prioritises engineering iterations in the post-launch phase. Use when asked to
  rank post-launch work, prioritise production improvements, or decide what to address after
  GA. Also consider when production metrics reveal issues competing for engineering attention.
  Suggest when post-launch work is accumulating without a clear priority order.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../tech-lead-pr-reviewer/iteration-prioritiser-f/SKILL.md
  - ../../tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md
---

# iteration-prioritiser-p-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Prioritises engineering iterations during the post-launch phase by ranking production issues, performance improvements, and feature enhancements based on production data and business impact.

## When to Use

- When a product has launched to GA and production data reveals bugs, performance bottlenecks, and enhancement requests competing for engineering time.
- When the post-launch backlog is growing and the team needs a data-driven approach to decide what to fix or improve next.
- When stakeholders are requesting post-launch changes and engineering needs to set expectations on sequencing.

## Workflow

1. **Aggregate post-launch signals**: Collect production metrics, error logs, support tickets, customer feedback, and monitoring alerts. Deliverable: post-launch signal inventory.
2. **Categorize and deduplicate**: Group related issues, merge duplicates, and categorize as production bug, performance issue, tech debt, or feature enhancement. Deliverable: categorized issue list.
3. **Score by production impact**: Assess each item by user-facing impact (affected users, revenue risk, SLA violation potential) and engineering effort. Weight production stability issues higher than enhancements. Deliverable: impact-effort scoring matrix.
4. **Prioritise with stakeholder input**: Present the scored list to product and engineering leadership. Incorporate business priorities (e.g., customer commitments, retention risk) into the final ranking. Deliverable: prioritised post-launch iteration backlog.
5. **Scope the iteration**: Select items that fit the iteration capacity. Ensure at least one production stability item is included per iteration. Deliverable: scoped iteration plan with acceptance criteria.

## Anti-Patterns

- **Feature-first post-launch**: Prioritising new features over production stability issues after launch. *Why*: unresolved production issues erode user trust and generate escalating support load that eventually blocks all feature work.
- **Ignoring production data**: Prioritising based on stakeholder requests alone without consulting metrics. *Why*: the loudest stakeholder may not represent the highest-impact issue; production data provides objective severity.
- **Deferring tech debt indefinitely**: Always deprioritising tech debt in favor of user-visible work. *Why*: accumulated tech debt slows every subsequent iteration, creating a compounding tax on engineering velocity.

## Output

**On success**: Produces a prioritised post-launch iteration backlog with production-data-backed scoring, a scoped iteration plan, and stakeholder alignment. Delivered to the project management tool and communicated to product and engineering teams.

**On failure**: Report which items could not be scored (e.g., insufficient production data, unclear business impact), what data is needed, and recommended steps to complete prioritisation.

## Related Skills

- [`iteration-prioritiser-f`](../../tech-lead-pr-reviewer/iteration-prioritiser-f/SKILL.md) -- feedback-phase prioritisation uses similar methods but operates on beta feedback rather than production data.
- [`backlog-groomer-eng`](../../tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md) -- prioritised post-launch items feed into the backlog for grooming and sprint planning.
