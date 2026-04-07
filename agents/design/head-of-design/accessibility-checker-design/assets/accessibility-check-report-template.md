# Accessibility Check Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Head of Design / reviewer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | accessibility-checker-design |

## Executive Summary

[2-3 sentences summarizing the check outcome and verdict (pass/conditional-pass/fail).
GUIDANCE: Lead with the verdict. State the number of blocking vs advisory findings. Reference the WCAG conformance target.]

## Contrast & Sizing Matrix

[All text/background combinations checked against WCAG 2.1 AA.

GUIDANCE:
- Good: Table with foreground colour, background colour, contrast ratio, pass/fail, and WCAG criterion
- Bad: "Colours look okay"
- Format: Table with columns: Element | Foreground | Background | Ratio | Required | Pass/Fail]

## Interaction State Coverage

[Checklist of interactive elements and their documented states.

GUIDANCE:
- Good: Matrix with rows per element, columns per state (focus, hover, active, disabled, error), cells as documented/missing
- Bad: "Most states are there"
- Format: Matrix table with pass/gap indicators]

## Content Accessibility Notes

[Alt text, ARIA labels, heading hierarchy, and error message findings.

GUIDANCE:
- Good: Each finding with the specific element, what is missing, and the recommended specification
- Bad: "Need more ARIA labels"
- Format: Table with columns: Element | Issue | WCAG Criterion | Recommendation]

## Recommendations

[Prioritised fixes required before dev handoff.
GUIDANCE: Each recommendation should be:
- Specific (exact token value to change, exact ARIA attribute to add)
- Actionable (assignable to the designer)
- Prioritised (blocking vs advisory)]

## Appendices

### A. Methodology

[Tools used for contrast checking, how interaction states were verified, Figma inspection approach]

### B. Supporting Data

[Screenshots of contrast checker results, Figma layer structure inspection notes]
