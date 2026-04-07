# Instrumentation Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | instrumentation-clarity-reviewer |
| Spec Reviewed | [Instrumentation spec name / link] |

## Executive Summary

[2-3 sentences with the overall verdict, composite score, and the top blocking finding.

GUIDANCE: Lead with approved/needs-revision. Example: "This instrumentation spec is approved for implementation with 4 required fixes. Composite score: 7.3 (grade B). The primary blocker is a journey coverage gap in the error-recovery flow, which must be addressed before implementation begins on those events."]

**Verdict:** [APPROVED / APPROVED WITH REQUIRED FIXES / NEEDS REVISION / REJECTED]
**Composite Score:** [X.X / 10]
**Grade:** [A+ / A / B / C / D / F]

## Event-Level Review

[Pass/fail status for every event in the spec with specific feedback.

GUIDANCE:
- Good: One row per event with pass/fail for each dimension (naming, properties, journey mapping, measurability) and specific remediation for each failure.
- Bad: "Most events look good." Every event must have an explicit status.
- Format: Table with a details section for each failed event below.]

| Event Name | Naming | Properties | Journey Step | Measurability | Overall | Issues |
|------------|--------|-----------|-------------|--------------|---------|--------|
| [event_name] | [PASS/FAIL] | [PASS/FAIL] | [PASS/FAIL] | [PASS/FAIL] | [PASS/FAIL] | [Issue count] |

### Failed Event Details

[For each FAIL row above, document the specific issue and remediation.

GUIDANCE: Be precise. "Property `plan_tier` is defined as string but should be enum with values: [free, pro, enterprise]" is correct. "Property needs fixing" is not.]

**[event_name]:**
- **Naming issue:** [Description] → **Fix:** [Exact correction]
- **Property issue:** [Property name] — [Description] → **Fix:** [Exact correction]

## Journey Coverage Assessment

[Visual or tabular map of the user journey with coverage status.

GUIDANCE:
- Good: Table listing every journey step with the event(s) that cover it; explicit marking of blind spots.
- Bad: Text saying "coverage looks adequate."
- Format: Table with Journey Step | Covering Event(s) | Coverage Status]

| Journey Step | Covering Event(s) | Status | Notes |
|-------------|------------------|--------|-------|
| [Step name] | [event_name, event_name] | [Covered / Blind Spot / Redundant] | [Any notes] |

## Measurability Assessment

[For each analytics goal, trace whether it is answerable from the proposed spec.

GUIDANCE:
- Good: "Goal: measure 7-day activation rate. Query path: `activation_completed` WHERE `days_since_signup <= 7` — MEASURABLE."
- Bad: "Goals are mostly covered."
- Format: Table.]

| Analytics Goal | Query Path | Measurable | Gap (if any) |
|---------------|-----------|-----------|-------------|
| [Goal statement] | [Event + property filter] | [YES / PARTIAL / NO] | [Missing event or property] |

## Privacy Review

[Summary of privacy compliance check.

GUIDANCE:
- Good: Explicit statement on PII status with list of any flagged properties.
- Bad: Omitting this section.
- Format: Short prose with a flagged-properties table if applicable.]

**PII Status:** [CLEAR / FLAGS IDENTIFIED]

| Property | Event | Issue | Required Action |
|---------|-------|-------|----------------|
| [property_name] | [event_name] | [PII type / indirect identifier] | [Remove / Hash / Add consent documentation] |

## Required Fixes Before Implementation

[Ordered list of all blocking issues.

GUIDANCE:
- P1: Must be fixed before any implementation begins.
- P2: Must be fixed before the affected events are implemented.
- P3: Should be fixed but does not block implementation.
- Format: Numbered list with priority, event reference, and exact remediation.]

1. **[P1]** [Event name] — [Specific fix required]
2. **[P2]** [Event name] — [Specific fix required]
3. **[P3]** [Event name] — [Suggested improvement]

## Recommendations

[Broader recommendations beyond line-item fixes.

GUIDANCE:
- Include structural improvements (e.g., "Add a global context schema to reduce property duplication across events").
- Note patterns that indicate the spec author needs coaching on naming conventions or privacy review.
- Recommend whether a re-review is needed after fixes or if fixes can be verified during implementation QA.]

## Appendices

### A. Methodology

[Document the review approach: journey map source, analytics goals source, naming convention reference, privacy framework used.]

### B. Supporting Data

[Instrumentation spec version reviewed, journey map used for coverage assessment, analytics goals document reference.]
