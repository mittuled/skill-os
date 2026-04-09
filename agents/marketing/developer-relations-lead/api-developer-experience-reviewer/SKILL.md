---
name: api-developer-experience-reviewer
description: >
  This skill reviews the API developer experience including design, documentation, and error handling.
  Use when asked to audit an API's usability, evaluate error messages, or assess API documentation quality.
  Also consider when developer onboarding drop-off rates are high at the API integration step.
  Suggest when the user is about to ship a new API version without a developer experience review.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "review API developer experience"
  - "audit API DX"
  - "developer experience review"
  - "API usability audit"
  - "DX improvement review"
---

# api-developer-experience-reviewer

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Reviews the API developer experience including endpoint design, documentation clarity, error handling, and time-to-first-call to identify friction points.

## When to Use

- When a new API or major API version is approaching release and needs a developer experience audit.
- When developer support tickets disproportionately involve API integration issues.
- When onboarding funnel data shows drop-off at the API integration step.
- When competitive analysis reveals developers prefer a rival API for usability reasons.

## Workflow

1. **Define review scope**: Identify which API endpoints, SDKs, and documentation pages are in scope. Deliverable: review scope document with endpoint inventory.
2. **Attempt first integration**: Walk through the API as a new developer would, from reading docs to making the first successful call. Record every friction point, confusion, and workaround in the first-call experience log section of [api-dx-review-report-template.md](assets/api-dx-review-report-template.md). Deliverable: first-call experience log with timestamps.
3. **Audit error handling**: Trigger common and edge-case errors to evaluate error message clarity, HTTP status code correctness, and recovery guidance. Score each scenario using the error handling audit table in the report template. Deliverable: error handling audit table.
4. **Review documentation**: Assess completeness, accuracy, code sample quality, and navigation structure of API reference docs. Deliverable: documentation gap analysis.
5. **Benchmark against standards**: Compare the experience against API design best practices using the standards compliance checklist in the report template and the scoring rubric in [references/scoring-rubric.md](references/scoring-rubric.md). Deliverable: scored standards compliance checklist.
6. **Compile recommendations**: Score each criterion per the rubric, compute composite grade, and prioritize P1/P2/P3 findings by developer impact and implementation effort. Deliverable: completed API DX review report.

## Anti-Patterns

- **Expert-blind review**: Reviewing as an experienced internal developer rather than simulating a new external developer's perspective. *Why*: Internal familiarity masks the confusion and missing context that real developers encounter.
- **Documentation-only review**: Evaluating docs in isolation without actually calling the API. *Why*: Documentation can appear complete but fail to match actual API behaviour, and only hands-on testing reveals runtime friction.
- **Ignoring error paths**: Focusing only on happy-path flows and skipping error scenario testing. *Why*: Developers spend more time debugging errors than writing happy-path code; poor error messages multiply support burden.

## Output

**On success**: Produces an API DX review report containing first-call experience log, error handling audit, documentation gaps, and prioritized recommendations. Delivered to engineering and product teams.

**On failure**: Report which endpoints could not be tested, what access or environment issues blocked the review, and recommend how to unblock. Every error must be actionable.

## Related Skills

- [`developer-experience-reviewer`](../developer-experience-reviewer/SKILL.md) — Broader developer experience review that includes but is not limited to API-specific concerns.
- [`developer-feedback-synthesiser`](../developer-feedback-synthesiser/SKILL.md) — Developer feedback often surfaces API pain points that should inform the review scope.
- [`api-documentation-designer`](../../../marketing/technical-writer/api-documentation-designer/SKILL.md) — Documentation issues found here feed directly into API documentation redesign.
