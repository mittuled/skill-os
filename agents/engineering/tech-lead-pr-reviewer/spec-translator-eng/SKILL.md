---
name: spec-translator-eng
description: >
  This skill translates product specifications into concrete engineering tasks and acceptance
  criteria. Use when asked to break down a spec, create engineering tickets, or convert
  requirements into tasks. Also consider when a product spec has been approved but no
  engineering tasks exist yet. Suggest when engineers are about to start building without
  a formal task breakdown.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/dependency-mapper/SKILL.md
---

# spec-translator-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Translates product specifications into concrete engineering tasks with clear acceptance criteria, size estimates, and dependency annotations.

## When to Use

- When a product specification has been approved and engineering needs a task breakdown before sprint planning can begin.
- When a large feature needs to be decomposed into independently deliverable, testable units of work.
- When product and engineering are misaligned on what "done" means for a feature, and explicit acceptance criteria are needed.

## Workflow

1. **Parse the specification**: Read the product spec end-to-end. Identify functional requirements, non-functional requirements, edge cases, and open questions. Deliverable: annotated spec with requirement tags and open questions list.
2. **Decompose into tasks**: Break the spec into engineering tasks, each representing a single deployable or testable unit. Include frontend, backend, infrastructure, and testing tasks. Deliverable: task list with brief descriptions.
3. **Write acceptance criteria**: For each task, define clear, testable acceptance criteria that specify when the task is done. Use the given/when/then format where applicable. Deliverable: tasks with acceptance criteria.
4. **Estimate and annotate dependencies**: Size each task (story points or t-shirt sizes) and annotate cross-task dependencies. Flag tasks that require input from other teams. Deliverable: sized and dependency-annotated task set.
5. **Review with product**: Walk through the task breakdown with the product owner to verify completeness and alignment with the original spec. Resolve any gaps. Deliverable: approved engineering task breakdown.

## Anti-Patterns

- **One-to-one spec-to-task mapping**: Creating a single engineering task per spec section without decomposing further. *Why*: overly large tasks hide complexity, resist estimation, and delay feedback loops.
- **Missing acceptance criteria**: Creating tasks with descriptions but no definition of done. *Why*: ambiguous tasks cause rework when engineers and product disagree on completion.
- **Translating without questioning**: Converting the spec mechanically without challenging assumptions or flagging gaps. *Why*: specs often contain implicit assumptions that, if left unchallenged, surface as bugs during implementation.

## Output

**On success**: Produces a complete engineering task breakdown with descriptions, acceptance criteria, size estimates, and dependency annotations. Delivered to the project management tool and shared with product and engineering teams.

**On failure**: Report which spec sections could not be translated (e.g., ambiguous requirements, missing design decisions), what clarifications are needed, and who to follow up with.

## Related Skills

- [`backlog-groomer-eng`](../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md) -- translated tasks feed into backlog grooming for refinement and sprint readiness.
- [`dependency-mapper`](../../../engineering/tech-lead-pr-reviewer/dependency-mapper/SKILL.md) -- the dependency annotations from translation are inputs to full dependency mapping.
