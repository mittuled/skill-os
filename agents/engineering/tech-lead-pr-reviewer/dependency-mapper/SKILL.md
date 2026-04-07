---
name: dependency-mapper
description: >
  This skill maps inter-task and inter-service dependencies to identify blockers and sequencing
  constraints. Use when asked to find blockers, visualize task dependencies, or determine the
  critical path. Also consider when sprint planning reveals unclear task ordering. Suggest when
  a team is about to start parallel work streams without verifying they are independent.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/dependency-resolver/SKILL.md
  - ../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md
---

# dependency-mapper

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Maps inter-task and inter-service dependencies across engineering work streams to identify blockers, sequencing constraints, and the critical path.

## When to Use

- When a multi-sprint project begins and the team needs to understand which tasks must complete before others can start.
- When engineers report being blocked and the root cause is unclear or involves cross-team dependencies.
- When sprint planning reveals tasks that appear independent but may share hidden data, API, or infrastructure dependencies.

## Workflow

1. **Inventory tasks and services**: Collect all tasks from the backlog and all services involved in the current initiative. Document ownership and team boundaries. Deliverable: task and service inventory.
2. **Identify dependency edges**: For each task, determine what it depends on (data, API, infrastructure, other tasks) and what depends on it. Mark each edge as hard (blocking) or soft (preferred but not required). Deliverable: dependency edge list.
3. **Build dependency graph**: Visualize the dependencies as a directed acyclic graph (DAG). Highlight cycles, which indicate design issues that must be resolved. Deliverable: dependency graph diagram.
4. **Identify critical path**: Calculate the longest chain of hard dependencies to determine the minimum timeline. Flag tasks on the critical path for priority attention. Deliverable: critical path analysis.
5. **Flag cross-team blockers**: Identify dependencies that cross team boundaries and require coordination. Assign owners to each cross-team dependency. Deliverable: cross-team blocker register with assigned owners.
6. **Communicate and update**: Share the dependency map with all affected teams. Establish a cadence for updating the map as work progresses. Deliverable: published dependency map with update schedule.

## Anti-Patterns

- **Mapping once and forgetting**: Creating the dependency map at project kickoff and never updating it. *Why*: dependencies change as work progresses; a stale map gives false confidence about sequencing.
- **Ignoring soft dependencies**: Only tracking hard blockers and dismissing preferred ordering. *Why*: soft dependencies become hard blockers when violated, causing rework and merge conflicts.
- **Assuming independence**: Treating tasks as independent by default without verifying. *Why*: hidden dependencies discovered mid-sprint cause context switching and delay delivery.

## Output

**On success**: Produces a dependency graph (DAG) with critical path analysis, cross-team blocker register, and update schedule. Delivered to the project management tool and shared with all affected engineering teams.

**On failure**: Report which dependencies could not be mapped (e.g., undefined APIs, unclear task scope), what information is missing, and recommended steps to complete the mapping.

## Related Skills

- [`dependency-resolver`](../../../engineering/tech-lead-pr-reviewer/dependency-resolver/SKILL.md) -- once dependencies are mapped, the resolver unblocks tasks when blockers arise.
- [`spec-translator-eng`](../../../engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md) -- spec translation produces the task breakdown that dependency mapping operates on.
