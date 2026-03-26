---
name: documentation-accuracy-auditor
description: >
  This skill audits documentation for technical accuracy against the current product implementation.
  Use when asked to verify docs are up to date, check code samples work, or find stale documentation.
  Also consider after a major release when documentation may have drifted from the implementation.
  Suggest when the user is about to publish docs that have not been verified against the latest build.
department: marketing
agent: technical-writer
version: 1.0.0
complexity: medium
related-skills: []
---

# documentation-accuracy-auditor

## Agent: Technical Writer

L3 technical writer reporting to Developer Relations Lead, responsible for API documentation, developer guides, and documentation accuracy.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Audits documentation for technical accuracy against the current product implementation to prevent developer confusion from stale or incorrect content.

## When to Use

- When a major product release has shipped and documentation may have drifted from the implementation.
- When developer support tickets cite incorrect or outdated documentation as the source of confusion.
- When onboarding a new technical writer who needs to understand the current accuracy baseline.
- When establishing a recurring accuracy audit cadence for the first time.

## Workflow

1. **Scope the audit**: Define which documentation sections, API versions, and platforms are in scope. Prioritize by traffic, recency of product changes, and known issue reports. Deliverable: audit scope with prioritized section list.
2. **Test code samples**: Execute every code sample in the scoped documentation against the current product version. Record pass/fail for each. Deliverable: code sample test results.
3. **Verify API references**: Compare documented endpoint signatures, parameters, response schemas, and error codes against the actual API behaviour. Deliverable: API reference accuracy report.
4. **Check procedural steps**: Walk through every tutorial and guide step-by-step to verify the instructions produce the stated outcome. Deliverable: procedure verification log.
5. **Flag inaccuracies**: Log each inaccuracy with the documentation location, expected vs. actual behaviour, severity (misleading vs. broken vs. cosmetic), and suggested fix. Deliverable: inaccuracy log with severity ratings.
6. **Prioritize and remediate**: Rank inaccuracies by developer impact and assign fixes to writers or engineers. Deliverable: remediation plan with owners and deadlines.

## Anti-Patterns

- **Skimming instead of testing**: Reading documentation for plausibility instead of actually executing the described steps. *Why*: Documentation that reads correctly can still be wrong; only execution against the live product catches runtime discrepancies.
- **Auditing without versioning**: Testing docs against "the latest" without pinning to a specific product version. *Why*: Version drift between audit time and publication creates false positives and false negatives that undermine audit credibility.
- **Audit without remediation**: Producing an inaccuracy report but not tracking fixes to completion. *Why*: An audit that does not result in corrected documentation is wasted effort; the same inaccuracies will be reported again next cycle.

## Output

**On success**: Produces a documentation accuracy report containing code sample test results, API reference verification, procedure checks, and a prioritized remediation plan. Delivered to technical writing and engineering teams.

**On failure**: Report which sections could not be audited, what environment or access issues blocked testing, and recommend how to unblock. Every error must be actionable.

## Related Skills

- [`documentation-writer`](../documentation-writer/SKILL.md) — Writers remediate the inaccuracies found by the audit.
- [`documentation-requirements-extractor`](../documentation-requirements-extractor/SKILL.md) — Requirements extraction surfaces changes that should trigger accuracy audits.
- [`api-developer-experience-reviewer`](../../developer-relations-lead/api-developer-experience-reviewer/SKILL.md) — API experience reviews complement accuracy audits by catching usability issues beyond correctness.
