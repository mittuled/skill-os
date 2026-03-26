---
name: developer-experience-reviewer
description: >
  This skill reviews the developer experience including onboarding, documentation, and SDK usability.
  Use when asked to audit the developer journey, evaluate SDK ergonomics, or assess onboarding friction.
  Also consider when developer activation rates are below target or time-to-first-value is too high.
  Suggest when the user is about to ship developer-facing changes without an experience review.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# developer-experience-reviewer

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Reviews the end-to-end developer experience including signup, onboarding, documentation, SDK usability, and time-to-first-value to identify and prioritize friction points.

## When to Use

- When developer activation or retention metrics are below target and the cause is unclear.
- When a major developer-facing release is approaching and needs a pre-ship experience audit.
- When developer support ticket volume is rising and root cause analysis points to experience issues.
- When expanding to a new developer segment (e.g., mobile developers) and needing to validate the experience for that audience.

## Workflow

1. **Define review scope and persona**: Select the developer persona and journey stages to review (signup, quickstart, first integration, production deployment). Deliverable: review scope with persona definition.
2. **Walk the journey**: Complete the full developer journey from scratch using only public resources. Record every step, time spent, confusion, and workaround. Deliverable: journey walkthrough log with timestamps and screenshots.
3. **Evaluate SDK and tooling**: Test SDK installation, configuration, IDE integration, debugging experience, and upgrade path. Deliverable: SDK usability assessment.
4. **Assess documentation**: Review guides, tutorials, and reference docs for accuracy, completeness, discoverability, and code sample quality. Deliverable: documentation assessment.
5. **Score and prioritize**: Rate each journey stage on a friction scale, identify the highest-impact improvement opportunities, and estimate effort. Deliverable: DX scorecard with prioritized recommendations.
6. **Present findings**: Share the review with product, engineering, and documentation teams with concrete next steps. Deliverable: DX review presentation.

## Anti-Patterns

- **Internal network review**: Reviewing from inside the company network where authentication, access, and services behave differently than for external developers. *Why*: Internal environments mask real-world friction like signup flows, rate limits, and permission errors.
- **Single-language review**: Testing only one SDK language when the product supports multiple. *Why*: Developer experience varies dramatically across language ecosystems; Python developers and Java developers have different ergonomic expectations.
- **Ignoring the middle journey**: Focusing only on first-call experience while skipping the path from prototype to production. *Why*: Many developers succeed with quickstart but churn at production deployment; the middle journey is where long-term retention is won or lost.

## Output

**On success**: Produces a DX review report containing journey walkthrough, SDK assessment, documentation evaluation, and a prioritized improvement roadmap. Delivered to product, engineering, and developer relations leadership.

**On failure**: Report which journey stages could not be completed, what environment or access issues blocked the review, and recommend unblocking steps. Every error must be actionable.

## Related Skills

- [`api-developer-experience-reviewer`](../api-developer-experience-reviewer/SKILL.md) — API-specific subset of the broader developer experience review.
- [`developer-feedback-synthesiser`](../developer-feedback-synthesiser/SKILL.md) — Synthesised developer feedback identifies which experience areas need the most urgent review.
- [`developer-community-signal-extractor`](../developer-community-signal-extractor/SKILL.md) — Community signals surface real-world experience friction that the review should validate.
