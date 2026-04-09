---
name: dependency-mapper-review
description: >
  This skill identifies, documents, and reviews cross-team and cross-system dependencies that could block or delay product delivery. Use when planning a multi-team initiative, entering a new sprint cycle with upstream or downstream handoffs, or when a blocked ticket traces back to an external dependency. Also consider when an epic spans more than one squad or requires a third-party integration. Suggest when sprint burndown shows repeated carry-over of the same stories.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "map dependencies review"
  - "review dependencies"
  - "dependency review"
  - "dependency mapping"
  - "dep map review"
---

# dependency-mapper-review

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
The dependency mapper review identifies, catalogues, and assesses cross-team, cross-system, and third-party dependencies that threaten delivery timelines. It produces a dependency map -- a directed graph of blocking and non-blocking relationships between work items, teams, APIs, and external vendors -- and reviews that map at planning boundaries to surface risks before they become sprint blockers.

## When to Use
- A new epic or initiative spans more than one squad and requires coordinated delivery across teams.
- Sprint planning is approaching and stories in the candidate set reference APIs, services, or data owned by another team.
- A blocked ticket in the current sprint traces its root cause to a dependency that was not identified at planning time.
- A third-party vendor integration is on the critical path and its delivery timeline is uncertain.
- Sprint burndown charts show the same stories carrying over for two or more sprints, suggesting hidden dependencies.
- A phase plan or milestone definition requires a clear view of which teams must deliver what and in which order.

## Workflow
1. Collect the set of epics, stories, or enablers under review -- typically the upcoming sprint candidate list or a multi-sprint initiative plan.
2. For each item, identify inbound dependencies (what this item needs from others) and outbound dependencies (what others need from this item).
3. Classify each dependency by type: **team-to-team** (another squad must deliver first), **system-to-system** (an API, data pipeline, or infrastructure component), or **external** (vendor, partner, regulatory body).
4. Classify each dependency by severity: **blocking** (work cannot start or finish without it) or **non-blocking** (work can proceed with a workaround but the final deliverable requires resolution).
5. Build the dependency map as a directed graph with nodes (work items or systems) and edges (dependency relationships annotated with type and severity).
6. Review the map for critical-path risks: chains of blocking dependencies longer than one sprint, single points of failure, and circular dependencies.
7. For each critical-path risk, document the risk, the owning team, the current status, and a proposed mitigation (escalate to `dependency-resolver`, negotiate scope with `scope-boundary-setter`, or re-sequence with `sprint-planner`).
8. Publish the reviewed dependency map and risk register to stakeholders; attach it to the relevant epic or initiative in the project tracker.

## Anti-Patterns
- **Mapping dependencies only at project kickoff.** Dependencies evolve as scope changes; a stale map gives false confidence. *Why: new stories, API changes, and vendor delays introduce dependencies mid-flight that the kickoff map cannot reflect.*
- **Treating all dependencies as blocking.** Over-classifying non-blocking dependencies as blockers inflates risk perception and paralyses planning. *Why: the distinction between blocking and non-blocking determines whether a story can enter a sprint or must wait.*
- **Mapping without ownership assignment.** A dependency without a named owner is a dependency no one is tracking. *Why: unowned dependencies surface as surprises during sprint review, not during planning where mitigation is still possible.*
- **Ignoring internal platform dependencies.** Focusing only on external vendors while assuming internal platform teams will deliver on time is a common blind spot. *Why: internal teams have their own backlogs and priorities; their capacity is not automatically allocated to your initiative.*

## Output

**Success:**
- A dependency map (directed graph) covering all items in the review scope, with each dependency classified by type and severity and assigned an owner.
- A risk register listing critical-path dependencies, their status, and proposed mitigations routed to the appropriate resolver.

**Failure:**
- Dependencies are identified but not classified by severity, leaving sprint planners unable to distinguish blockers from nice-to-haves.
- The map is published without ownership, resulting in untracked dependencies that surface as sprint blockers.

## Related Skills
- `dependency-resolver` -- acts on the blocking dependencies this skill surfaces, negotiating resolution across teams.
- `sprint-planner` -- uses the dependency map to sequence stories and avoid blocked work entering the sprint.
- `backlog-groomer` -- flags potential dependencies during refinement for this skill to formally map.
- `phase-planner` -- consumes the dependency map when building multi-phase delivery plans.
