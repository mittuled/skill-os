# User Story

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | story-writer |

## Executive Summary

[2-3 sentences summarizing the user story, the persona it serves, and the business outcome.
GUIDANCE: Lead with what the user can do after this story is delivered.]

## Story Statement

[As a / I want / So that format.

GUIDANCE:
- Good: "As a workspace admin who manages a team of 15+, I want to create custom roles with specific permission sets, so that I can grant team members exactly the access they need without over-permissioning."
- Bad: "As a user, I want RBAC, so that permissions work."
- Format: Single sentence in standard story format with specific persona, atomic goal, measurable outcome]

## Context

[Background information for engineering and design.

GUIDANCE:
- Good: "Discovery finding: 8/10 interviewed admins reported creating workaround processes (shared accounts, manual permission requests) because the binary admin/member model does not match their team structure. Most common request: 'I want a role that can manage billing but not see user data.' Design reference: [Figma link]. API dependency: User Service v2 permission catalogue (available Q1)."
- Bad: "Users want this"
- Format: Discovery evidence, design references, API/technical dependencies, related stories]

## Acceptance Criteria

[Given/When/Then format, 3-7 criteria.

GUIDANCE:
- Good:
  "1. Given an admin is on the Roles settings page, When they click 'Create Role', Then a modal displays with a name field (max 50 chars) and a permission checklist grouped by category.
  2. Given the admin enters a valid name and selects 1+ permissions, When they click 'Save', Then the role is created and appears in the roles list within 2 seconds.
  3. [Edge case] Given the admin enters a name that already exists, When they click 'Save', Then an inline error displays below the name field: 'A role with this name already exists.'
  4. [Error state] Given the admin has no network connection, When they click 'Save', Then a toast error displays: 'Unable to save. Check your connection and try again.'
  5. [Accessibility] Given a screen reader user, When they navigate the permission checklist, Then each checkbox is labeled with the permission name and category."
- Bad: "Role creation works correctly"
- Format: Numbered list, each criterion in Given/When/Then, labeled as edge case or error state where applicable]

## Technical Constraints

[Implementation constraints and dependencies.

GUIDANCE:
- Good: "API: POST /api/v2/roles (new endpoint). DB: roles table with name (VARCHAR 50, UNIQUE per workspace), permissions (JSONB). Rate limit: 10 role creations per minute per workspace. Backwards compatibility: existing admin/member roles must remain as built-in, non-deletable roles."
- Bad: "Normal constraints"
- Format: Bulleted list with specific technical details]

## Recommendations

[Actions to finalise the story for sprint commitment.
GUIDANCE: Each recommendation should be:
- Specific (not "refine story" but "validate permission checklist grouping with 2 target admins before sprint commitment")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Story writing approach: persona-specific, atomic goals, Given/When/Then acceptance criteria with edge and error cases per framework.]

### B. Supporting Data

[Discovery interview excerpts, support ticket references, analytics data on current permission usage patterns.]
