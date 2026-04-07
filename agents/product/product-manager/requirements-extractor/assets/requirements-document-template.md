# Requirements Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | requirements-extractor |

## Executive Summary

[2-3 sentences summarizing total requirements extracted, priority distribution, and key gaps identified.
GUIDANCE: Lead with the most critical requirement or the primary user need driving this extraction.]

## Input Inventory

[Sources used for requirement extraction with metadata.

GUIDANCE:
- Good: Table with Source ID, Source Type (interview/ticket/PRD/competitive), Origin (customer name, ticket #), Date, Key Themes
- Bad: "We looked at some interviews"
- Format: Markdown table, one row per source]

## Requirements Table

[Structured requirements with ID, category, statement, priority, and traceability.

GUIDANCE:
- Good: "FR-001 | Functional | The system shall allow workspace admins to create custom roles with named permission sets | Must (RICE: 84) | Interview #3, Support tickets #1201-#1205 | Given an admin is on the Roles page, When they click Create Role, Then a role creation form is displayed with permission checkboxes"
- Bad: "Add roles feature"
- Format: Table with columns: Req ID, Category, Statement, MoSCoW (RICE Score), Source Traceability, Acceptance Criteria]

## Priority Distribution

[Summary of requirement distribution across MoSCoW categories.

GUIDANCE:
- Good: "Must: 8 requirements (40%). Should: 6 requirements (30%). Could: 4 requirements (20%). Won't: 2 requirements (10%). Total RICE score range: 12-84."
- Bad: "Most things are important"
- Format: Summary table with MoSCoW category, count, percentage, RICE range]

## Gap Analysis

[Requirements that are incomplete or have conflicts.

GUIDANCE:
- Good: Table with Req ID, Gap Type (missing acceptance criteria / conflicting sources / unclear scope), Description, Resolution Action, Owner
- Bad: "Some requirements need work"
- Format: Markdown table, one row per gap]

## Recommendations

[Actions to finalise the requirements set.
GUIDANCE: Each recommendation should be:
- Specific (not "clarify requirements" but "schedule follow-up interview with Customer X to resolve conflict between FR-003 and FR-007")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Extraction approach: source collection, RICE scoring parameters, MoSCoW classification thresholds, stakeholder validation process.]

### B. Supporting Data

[Raw interview notes, support ticket exports, competitive feature matrices, RICE scoring calculations.]
