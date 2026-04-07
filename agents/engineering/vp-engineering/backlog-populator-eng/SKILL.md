---
name: backlog-populator-eng
description: >
  This skill populates the engineering backlog with well-defined tasks from approved specifications.
  Use when asked to break a spec into backlog items, seed a project backlog, or create engineering
  work items from a PRD. Also consider when a phase plan is finalized but no tasks exist yet.
  Suggest when an approved spec has no corresponding engineering backlog entries.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md
---

# backlog-populator-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Populates the engineering backlog with well-defined tasks derived from approved specifications and phase plans.

## When to Use

- When an approved specification or PRD needs to be decomposed into actionable engineering work items.
- When a new delivery phase begins and the backlog for that phase is empty.
- When a scope change introduces new requirements that must be tracked as discrete tasks.

## Workflow

1. **Ingest approved spec**: Read the approved specification, phase plan, and any architecture decisions. Identify all deliverables, acceptance criteria, and non-functional requirements. Deliverable: a requirements inventory list.
2. **Decompose into tasks**: Break each deliverable into tasks small enough to complete in one sprint. Each task must have a clear definition of done, size estimate (T-shirt or story points), and dependency tags. Deliverable: draft task list with metadata.
3. **Assign priority and sequencing**: Order tasks by dependency graph and business priority. Tag critical-path items. Deliverable: prioritized, sequenced backlog.
4. **Cross-reference dependencies**: Link tasks that depend on other teams, services, or infrastructure changes. Flag external blockers. Deliverable: dependency-annotated backlog.
5. **Load into tracker**: Create the tasks in the project management tool with all metadata, links to the source spec, and acceptance criteria. Deliverable: populated backlog ready for sprint planning.

## Anti-Patterns

- **Vague tasks**: Creating backlog items like "implement feature X" without acceptance criteria or definition of done. *Why*: ambiguous tasks cause scope disagreements during sprint review and inflate cycle time.
- **Premature decomposition**: Breaking tasks down to sub-day granularity before architecture is settled. *Why*: over-decomposition creates churn when designs change, wasting planning effort.
- **Orphaned tasks**: Populating tasks without linking them to the source spec or phase plan. *Why*: traceability loss makes it impossible to verify coverage or manage scope changes.

## Output

**On success**: Produces a fully populated engineering backlog with each task containing a title, description, acceptance criteria, size estimate, priority, dependency links, and source spec reference. Delivered in the project management tool.

**On failure**: Report which spec sections could not be decomposed (e.g., ambiguous requirements, missing acceptance criteria), what clarification is needed, and a recommended path to unblock.

## Related Skills

- [`spec-translator-eng`](../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md) -- translates specs into engineering tasks at the tech lead level; backlog population builds on this output.
- [`backlog-groomer-eng`](../../../engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md) -- grooms the backlog after it has been populated to keep tasks sprint-ready.
