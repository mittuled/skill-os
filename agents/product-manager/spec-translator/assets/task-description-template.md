# Engineering Task Description

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | spec-translator |

## Executive Summary

[2-3 sentences summarizing total tasks produced, the spec they trace to, and estimation readiness.
GUIDANCE: Lead with the number of tasks and whether they are ready for sprint commitment.]

## Source Specification

[Reference to the PRD or spec being translated.

GUIDANCE:
- Good: "Source: PRD-2026-Q2-RBAC v2.1 (approved 2026-03-01). Sections translated: 2.1 (Role Creation), 2.2 (Permission Assignment), 2.3 (Role Inheritance). Open questions: Section 2.4 (Audit Log) deferred — not translatable until design complete."
- Bad: "From the RBAC PRD"
- Format: Source document with version, sections covered, and sections not yet translatable]

## Task List

[Decomposed tasks with acceptance criteria and technical context.

GUIDANCE:
- Good: Per-task subsection with: Task ID, Title, Description (1 paragraph), Spec Traceability (section reference), Acceptance Criteria (Given/When/Then, 2-5 per task including edge case and error state), Technical Context (affected APIs, data model changes, integration points, constraints), Cross-Team Dependencies, Estimate
- Bad: "Implement roles"
- Format: Repeated subsection per task. Example:

**T-001: Create custom role with named permission set**
Description: Allow workspace admins to create a new role by selecting a name and checking desired permissions from the permission catalogue.
Spec: PRD Section 2.1
Acceptance Criteria:
1. Given an admin is on the Roles page, When they click "Create Role", Then a form displays with name field and permission checkboxes.
2. Given the admin submits a valid role name and 1+ permissions, When they click Save, Then the role appears in the roles list within 2 seconds.
3. Given the admin submits a duplicate role name, When they click Save, Then an inline error displays: "A role with this name already exists."
4. Given the admin submits with no permissions selected, When they click Save, Then an inline error displays: "Select at least one permission."
Technical Context: POST /api/v2/roles endpoint (new). roles table migration (add name, permissions JSONB column). Depends on permission catalogue from User Service v2.
Cross-Team: User Service team (permission catalogue API must be available).
Estimate: 5 SP]

## Traceability Matrix

[Mapping from spec sections to tasks.

GUIDANCE:
- Good: Table with Spec Section, Task IDs, Coverage Status (fully covered / partially covered / not covered)
- Bad: "Tasks map to the spec"
- Format: Markdown table confirming every spec behaviour has a corresponding task]

## Recommendations

[Actions before tasks are sprint-ready.
GUIDANCE: Each recommendation should be:
- Specific (not "review tasks" but "schedule 30-min task walkthrough with backend lead to validate T-001 through T-004 estimates")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Decomposition approach: single-responsibility tasks, Given/When/Then acceptance criteria, technical context annotation per task.]

### B. Supporting Data

[Source PRD, design mockups, API documentation, data model diagrams.]
