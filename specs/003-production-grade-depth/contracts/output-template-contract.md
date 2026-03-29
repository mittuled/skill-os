# Contract: Output Template Format

**Version**: 1.0.0 | **Date**: 2026-03-28

## Location

`<skill>/assets/<output-name>-template.md`

## Required For

Every skill that produces a report, document, plan, brief, proposal, or any structured output artifact.

## Structure

```markdown
# <Output Name>

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | [skill-slug that produced this] |

## Executive Summary

[2-3 sentences summarizing the key findings/content of this document.
GUIDANCE: Lead with the most important conclusion or recommendation.
Do not restate the methodology — focus on outcomes.]

## <Section 1: Domain-Specific>

[Section content placeholder.

GUIDANCE:
- Good: [Example of what good content looks like in this section]
- Bad: [Example of what to avoid]
- Format: [Tables/lists/prose — specify expected format]]

## <Section 2: Domain-Specific>

[Repeat with section-specific guidance]

## <Section N: Domain-Specific>

[As many sections as the output type requires]

## Recommendations

[Prioritized list of recommendations based on findings.
GUIDANCE: Each recommendation should be:
- Specific (not "improve X" but "implement Y to achieve Z")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3 or High/Medium/Low)]

## Appendices

### A. Methodology

[How this output was produced — frameworks used, data sources, time period]

### B. Supporting Data

[Raw data, detailed tables, or evidence that supports the main content]
```

## Validation Rules

1. Must have a Metadata section with Date, Author, Version, Status, Skill fields
2. Must have an Executive Summary with guidance annotation
3. Must have at least 3 domain-specific content sections
4. Each content section must include placeholder text AND guidance (good/bad examples or format notes)
5. Must have a Recommendations section (even if the output is informational — recommendations can be "next steps")
6. Template must be specific to the skill's output type — a PRD template is not a design doc template

## Naming Convention

`<output-type>-template.md`

Examples:
- `threat-model-report-template.md`
- `prd-template.md`
- `competitive-analysis-template.md`
- `nda-template.md`
- `audit-report-template.md`

## Anti-Patterns

- **Headings only**: A template with just headings and no placeholder content or guidance is a table of contents, not a template
- **Generic sections**: "Analysis", "Results", "Conclusion" — use domain-specific section names
- **Missing guidance**: Every section needs at least one guidance annotation (good/bad example or format note)
- **One-size-fits-all**: Don't create a "universal report template" — each skill's output has different sections
