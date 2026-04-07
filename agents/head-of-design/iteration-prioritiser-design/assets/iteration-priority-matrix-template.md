# Design Iteration Priority Matrix

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Head of Design] |
| Cycle / Sprint | [e.g. Q2 Sprint 3] |
| Input Sources | [Session analysis, usability test findings, accessibility audit, user feedback] |
| Version | [1.0] |
| Status | [Draft / Approved] |

## Priority Decision Summary

[1-2 sentences stating how many items were evaluated, how many are approved for the current cycle, and the primary prioritisation rationale. GUIDANCE: e.g. "14 iteration candidates were evaluated; 4 are approved for Sprint 3. Priority weighted toward task-completion blockers found in session analysis over cosmetic improvements."]

## Scoring Model

Items are scored on four dimensions. Each dimension is rated 1–5.

| Dimension | Weight | Description |
|-----------|--------|-------------|
| User Impact | 35% | Degree to which the issue blocks or significantly impairs user task completion |
| Business Value | 25% | Alignment with active OKRs, conversion or retention impact |
| Design Effort | 20% | Inverse of effort — lower effort scores higher (1=weeks, 5=hours) |
| Accessibility Severity | 20% | WCAG severity level if applicable; non-A11y issues score 3 (neutral) |

**Composite Score** = (User Impact × 0.35) + (Business Value × 0.25) + (Design Effort × 0.20) + (Accessibility Severity × 0.20)

## Iteration Backlog

[List all candidates evaluated in this cycle. Add rows as needed.]

| ID | Item Description | Source | User Impact (1-5) | Business Value (1-5) | Design Effort (1-5) | A11y Severity (1-5) | Composite | Recommendation |
|----|-----------------|--------|------------------|---------------------|--------------------|--------------------|-----------|----------------|
| I-01 | [e.g. Cart quantity stepper has no keyboard focus state] | [Accessibility audit] | 4 | 3 | 5 | 5 | [4.15] | Approve — Sprint 3 |
| I-02 | [e.g. Empty state copy on dashboard is unclear] | [Session analysis] | 3 | 4 | 4 | 3 | [3.45] | Approve — Sprint 3 |
| I-03 | [e.g. Improve visual hierarchy on settings page] | [Design debt] | 2 | 2 | 2 | 3 | [2.25] | Defer — Q3 |
| I-04 | [e.g. Add skeleton loading state to feed] | [User feedback] | 4 | 4 | 3 | 3 | [3.60] | Approve — Sprint 3 |
| I-05 | [Description] | [Source] | | | | | | |
| I-06 | [Description] | [Source] | | | | | | |

## Approved Items — Current Cycle

| ID | Item | Owner | Effort Estimate | Sprint |
|----|------|-------|----------------|--------|
| I-01 | [e.g. Fix keyboard focus state on cart quantity stepper] | [Designer name] | 0.5 days | Sprint 3 |
| I-02 | [e.g. Rewrite empty state copy for dashboard] | [Content Designer] | 0.5 days | Sprint 3 |
| I-04 | [e.g. Design skeleton loading state for feed] | [Designer name] | 1 day | Sprint 3 |

## Deferred Items

| ID | Item | Defer Reason | Revisit Date |
|----|------|-------------|--------------|
| I-03 | [e.g. Settings page visual hierarchy] | [Low impact + limited sprint capacity] | [Q3 cycle 1] |

## Dropped Items

| ID | Item | Drop Reason |
|----|------|------------|
| [ID] | [Description] | [e.g. Superseded by upcoming settings redesign initiative] |

## Notes & Constraints

[Document any capacity constraints, dependencies, or sequencing requirements that affected prioritisation decisions.]

- [e.g. Designer A is at 80% allocated this sprint — only one medium-effort item assigned]
- [e.g. Accessibility items prioritised over design debt per Q2 OKR commitment to WCAG AA compliance]
- [e.g. I-04 skeleton loader depends on engineering API response structure confirmation before design can finalise]
