# Checklist: backlog-groomer-eng

Ensures every backlog item is well-defined, accurately sized, and prioritized before sprint planning begins.

## Pre-Grooming Audit

Before the grooming session, run this audit to identify which tickets require attention:

- [ ] **Export the full backlog**: Pull all open tickets from the project management tool, sorted by priority
- [ ] **Flag stale tickets**: Mark tickets with no activity in > 30 days as stale candidates for archiving or deprioritization
- [ ] **Flag duplicate tickets**: Identify tickets describing the same work; note the canonical ticket to keep
- [ ] **Flag missing acceptance criteria**: Mark every ticket without at least one testable AC statement
- [ ] **Flag oversized tickets**: Mark tickets estimated > 8 story points as candidates for decomposition
- [ ] **Flag dependency gaps**: Mark tickets that depend on other work but have no dependency annotation

## Per-Ticket Grooming Checklist

Apply to every ticket in the top 2 sprints' worth of backlog:

### Description
- [ ] Title is a verb + noun (action + subject): "Add pagination to /users" not "Pagination"
- [ ] Description explains what, why, and any constraints in 2–5 sentences
- [ ] No ambiguous terms ("improve", "fix", "update") without specific criteria

### Acceptance Criteria
- [ ] At least one testable AC statement in given/when/then or equivalent format
- [ ] Each AC is independently verifiable (one thing to check per statement)
- [ ] Edge cases and error states are covered, not just the happy path
- [ ] AC does not describe implementation details (what to build, not how)

### Sizing
- [ ] Ticket has a size estimate (story points or t-shirt size)
- [ ] Estimate was provided by an engineer who will work on it, not just the tech lead
- [ ] Tickets sized > 8 points are flagged for decomposition before sprint entry
- [ ] Sizing accounts for testing effort, not just implementation

### Priority and Dependencies
- [ ] Priority label is assigned (P1 / P2 / P3 or equivalent scale)
- [ ] All upstream blocking tasks are annotated with `DEPENDS-ON: [ticket-id]`
- [ ] All downstream tasks that this blocks are annotated with `BLOCKS: [ticket-id]`
- [ ] External dependencies (other teams, vendors) are annotated with `EXT-DEP: [team/date]`

### Readiness Gate
A ticket is "sprint-ready" only when ALL of the following are true:
- [ ] Description is complete
- [ ] At least one AC statement exists and is testable
- [ ] Estimate is assigned
- [ ] Priority is set
- [ ] All blocking dependencies are identified

## Backlog Pruning

At the end of each grooming session:
- [ ] Archive tickets not touched in > 60 days that are not explicitly planned
- [ ] Merge all identified duplicates into the canonical ticket
- [ ] Close tickets for features that have been descoped or superseded
- [ ] Confirm the top of the backlog (next 2 sprints) is 100% sprint-ready per the readiness gate above

## Grooming Session Standards

- [ ] Engineering is represented: at least one implementer per workstream (BE, FE, infra) attends
- [ ] Product is represented: PO can answer AC questions and resolve priority conflicts
- [ ] Session is time-boxed: 1 hour maximum per sprint of backlog reviewed; split across multiple sessions if needed
- [ ] Decisions are recorded: any AC changes, re-sizing decisions, and priority changes made in session are committed to the ticket in real time — not after

## Output Quality Gate

Before the grooming session is closed:
- [ ] Top [2 × sprint velocity] points of backlog are sprint-ready
- [ ] No sprint-ready ticket has an unresolved blocking dependency that would prevent work from starting in the next sprint
- [ ] Backlog size is reasonable: remove or archive if total open tickets > [team size × 40]
