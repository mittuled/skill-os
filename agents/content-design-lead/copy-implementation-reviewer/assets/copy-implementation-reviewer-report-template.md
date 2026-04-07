# Copy Implementation Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Content Design Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | copy-implementation-reviewer |
| Feature / Release | [Name of feature or release reviewed] |
| Environment Reviewed | [Staging / Production] |
| Content Design Spec Version | [Link to spec version used as reference] |

## Executive Summary

[2-3 sentences stating the overall grade, the most significant finding (if any critical or major deviations), and whether the feature is clear to ship. Lead with the verdict.]

GUIDANCE: Example — "The onboarding flow implementation scores 7.2/10 (B — Good) and is clear to ship with 4 minor copy corrections filed as tickets. The most significant finding is that all validation error messages use the generic 'Invalid input' pattern instead of the spec's actionable format — this has been filed as a Major ticket to resolve in the next sprint. No critical deviations that would block the release were found."

## Review Scope

[Document exactly what was reviewed.

GUIDANCE: Be precise — "the full onboarding flow" is not precise enough. List screens or component types.]

| Surface | Screens / Components | Copy Types Reviewed | Access Method |
|---------|--------------------|--------------------|--------------|
| [e.g., Onboarding] | [Screen names or count] | [Labels, errors, empty states, etc.] | [Staging URL / Production] |
| [e.g., Settings] | | | |

## Composite Score

| Criterion | Weight | Score (0-10) | Weighted Score |
|-----------|--------|-------------|---------------|
| Voice and Tone Conformance | 30% | [Score] | [Weighted] |
| Terminology Accuracy | 25% | | |
| Copy Pattern Adherence | 25% | | |
| Accessibility Copy | 10% | | |
| Grammar and Mechanics | 10% | | |
| **Total** | **100%** | | **[X.X]** |
| **Grade** | | | **[A+/A/B/C/D/F]** |

## Deviation Log

[List every deviation found, sorted by severity (Critical first).

GUIDANCE: Each row must include the corrected copy — engineers should not have to interpret what "fix this" means. Severity: Critical = meaning change or blocks task; Major = tone violation, wrong pattern, missing empty state; Minor = capitalisation, punctuation, formatting.]

| # | Severity | Surface | Element | Current Copy | Corrected Copy | Criterion Affected | Ticket |
|---|---------|---------|---------|-------------|---------------|-------------------|--------|
| 1 | [Critical/Major/Minor] | [Screen name] | [Button/Error/Label/etc.] | "[current text]" | "[corrected text]" | [Criterion name] | [Ticket #] |
| 2 | | | | | | | |

**Summary**: [N] Critical | [N] Major | [N] Minor

## Recommendations

[Actions based on the review findings.]

| Priority | Recommendation | Owner | Deadline |
|----------|---------------|-------|---------|
| P1 | [e.g., Resolve all Major deviations before the next sprint ships the affected feature to external users] | [Engineering Lead] | [Date] |
| P2 | [e.g., Update copy review to be a step in the release checklist to prevent recurrence] | [Content Design Lead + PM] | [Date] |

## Appendices

### A. Methodology

[How the review was conducted: tool used to walk through the product, how copy was extracted, which sections of the spec were checked against each copy type.]

### B. Passed Items

[Summary of copy elements that were reviewed and found compliant — useful to confirm the review was comprehensive, not just failure-focused.]
