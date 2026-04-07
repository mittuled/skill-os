---
name: copy-implementation-reviewer
description: >
  This skill reviews implemented copy in the product for accuracy and consistency with design
  specifications. Use when asked to review shipped copy, audit UX writing quality, or check
  copy against the content design spec. Also consider when a release is about to ship and
  no copy review has been performed. Suggest when the user notices copy inconsistencies in
  a recently deployed feature.
department: design
agent: content-design-lead
version: 1.0.0
complexity: simple
related-skills: []
---

# copy-implementation-reviewer

## Agent: Content Design Lead

L2 content design lead (1x) (moved from Product, now reports to Head of Design) responsible for microcopy, voice standards, UX copy, and help content architecture.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Reviews implemented copy in the product for accuracy, voice consistency, and conformance with the content design specification.

## When to Use

- When a feature has been implemented and needs a copy review before or shortly after release to verify the approved copy was implemented correctly.
- When a periodic copy audit is scheduled to catch drift from content design standards across the product.
- When support tickets or user feedback indicate confusion caused by unclear or inconsistent product copy.

## Workflow

1. **Scope Definition**: Identify the screens, flows, or product areas to review. Prioritise high-traffic surfaces and recently changed areas. Deliverable: review scope document.
2. **Copy Extraction**: Walk through the defined scope in the product (staging or production), capturing all visible copy including labels, placeholders, tooltips, error messages, empty states, and notifications. Deliverable: extracted copy inventory.
3. **Spec Comparison**: Compare each copy string against the content design spec: voice and tone, terminology glossary, copy patterns, grammar rules, and accessibility standards. Flag deviations. Deliverable: deviation log with severity (critical: meaning change, major: tone/terminology violation, minor: formatting inconsistency).
4. **Recommendation & Filing**: For each deviation, write the corrected copy and file it as a bug or task for the engineering team. Deliverable: copy correction tickets.

## Anti-Patterns

- **Review without spec reference**: Reviewing copy based on personal preference rather than the documented content design spec. *Why*: subjective reviews produce inconsistent feedback and undermine the authority of the spec.
- **Batch-only reviews**: Only reviewing copy in large periodic audits rather than incorporating review into the release process. *Why*: copy drift compounds between audits; catching issues at release is cheaper than retroactive fixes.
- **Flagging without fixes**: Identifying copy deviations without providing the corrected copy string. *Why*: engineers should not have to guess the correct copy; providing the fix ensures accuracy and speeds resolution.

## Output

**On success**: Produces a copy deviation log with severity ratings and corrected copy strings, filed as actionable tickets for the engineering team. Delivered as a structured list or directly as tickets in the project management tool.

**On failure**: Report which product areas could not be reviewed (e.g., access restrictions, feature flags hiding content), what partial review was completed, and recommend access or environment setup needed to complete the audit.

## Related Skills

- [`content-design-spec`](../content-design-spec/SKILL.md) — The spec is the standard against which implementation is reviewed.
- [`ux-copy-writer`](../ux-copy-writer/SKILL.md) — Original copy authored by UX writing is what implementation should match.
- [`support-pre-briefer-content`](../support-pre-briefer-content/SKILL.md) — Copy changes found in review may require support team notification.
