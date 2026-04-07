# Story Mapping Guide: JTBD to User Stories

## Purpose

A practical reference for translating Jobs-to-be-Done (JTBD) insights into well-formed user stories and design requirements that engineering and design teams can act on.

## The Translation Ladder

JTBD insights move from abstract to actionable through a structured translation:

```
Job (why) → Goal (what) → Task (how) → Story (build spec)
```

| Level | Format | Example |
|-------|--------|---------|
| Job | "When [trigger], I want to [motivation], so I can [outcome]" | "When I run my weekly status meeting, I want to see who is blocked without asking each person, so I can resolve blockers before they cause delays" |
| Goal | User needs to [capability] | User needs to see blocker status across all team members without manual collation |
| Task | User can [action] on [object] | User can view a blocker flag on each team member's task row |
| Story | As a [user], I want to [action], so that [benefit] | "As a project manager, I want to see a blocker indicator on each task row, so that I can identify and resolve issues before my status meeting" |

## User Story Format

### Standard Format
```
As a [user role],
I want to [action / capability],
So that [benefit / outcome].
```

### Acceptance Criteria Format (BDD)
```
Given [precondition / context],
When [user action],
Then [system response / outcome].
```

### Example

**Story**: As a project manager, I want to see blocked tasks highlighted in the project view, so that I can identify which team members need help without asking each individually.

**Acceptance Criteria**:
- Given a project has tasks with blockers flagged, when the manager opens the project view, then tasks with active blockers are visually distinguished from unblocked tasks.
- Given a task is flagged as blocked, when the manager clicks on the blocker indicator, then they see the blocker description and who flagged it.
- Given no tasks are blocked, when the manager opens the project view, then no blocker indicators are displayed.

## JTBD → Story Mapping Table

Use this to systematically translate job stages into stories:

| Job Stage | User Goal | Design Capability | User Story | Acceptance Criteria (summary) |
|-----------|-----------|------------------|-----------|-------------------------------|
| [Stage from JTBD map] | [What user needs to achieve at this stage] | [Feature / UI capability needed] | [As a... I want... So that...] | [Given/When/Then summary] |

## Story Quality Checklist (INVEST)

Before accepting a story into the backlog, validate against INVEST:

| Criterion | Description | Check |
|-----------|-------------|-------|
| **I**ndependent | Story can be built without dependency on another story | [ ] |
| **N**egotiable | Not a rigid contract — implementation details can be discussed | [ ] |
| **V**aluable | Delivers direct value to the user (traceable to a job) | [ ] |
| **E**stimable | Engineering can estimate the effort | [ ] |
| **S**mall | Can be completed in one sprint (max 5 days) | [ ] |
| **T**estable | Acceptance criteria are objectively verifiable | [ ] |

## Research-to-Story Traceability

Each story derived from research should be traceable to its source. Document the link:

| Story ID | JTBD Source | Research Evidence | Confidence |
|----------|------------|-------------------|-----------|
| [Story ID] | [Job statement it derives from] | [e.g. "8/12 interview participants described this pain; 3 rated it critical"] | [High/Med/Low] |

## Story Mapping Canvas Structure

Organise stories using the Jeff Patton story map structure:

```
Backbone (User Activities — top row)
└── Walking Skeleton (Minimum viable story per activity — 2nd row)
    └── Enhancements (Additional stories prioritised below skeleton)
```

| Activity | Walking Skeleton Story | Enhancement 1 | Enhancement 2 |
|----------|----------------------|---------------|---------------|
| [e.g. View project status] | [As a PM I want to see all tasks and their status] | [As a PM I want to filter by assignee] | [As a PM I want to export status to PDF] |

## Definition of Ready (Before Sprint Entry)

A story is ready for sprint planning when:
- [ ] Story follows As a / I want / So that format
- [ ] All acceptance criteria are written and understood
- [ ] Design mockup (wireframe or hi-fi) is linked and approved
- [ ] Story traces to a JTBD insight (evidence field populated)
- [ ] Engineering has confirmed the story is estimable
- [ ] No unresolved dependencies block starting the story
