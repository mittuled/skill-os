---
name: help-content-reviewer
description: >
  This skill reviews help centre content for accuracy and completeness after product changes.
  Use when asked to audit help articles, verify documentation accuracy, or update support content
  post-release. Also consider when customer tickets reference outdated help articles.
  Suggest when a product release changes existing workflows documented in the help centre.
department: customer-support
agent: support-agent
version: 1.0.0
complexity: simple
related-skills:
  - help-centre-builder-support
  - support-readiness-briefer-support
triggers:
  - "review help content"
  - "audit help articles"
  - "help content review"
  - "check support docs"
  - "help centre review"
---

# help-content-reviewer

## Agent: Support Agent

L2 support agent (Nx, multi-instance) responsible for ticket triage, support readiness confirmation, and help content review.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The help content reviewer audits existing help centre articles against the current product state, flags inaccuracies introduced by product changes, and recommends updates to keep self-service content reliable.

## When to Use

- When a product release changes UI flows, feature behaviour, or configuration options documented in the help centre.
- When customers submit tickets citing help articles that gave them incorrect instructions.
- When a scheduled content audit is due (quarterly or post-major-release).

## Workflow

1. **Gather change scope**: Collect release notes and changelog entries to identify which product areas changed. Deliverable: affected-area list.
2. **Map articles to changes**: Cross-reference affected product areas with existing help centre articles. Deliverable: article review queue.
3. **Review each article**: Walk through every step in the article against the live product to verify accuracy of screenshots, instructions, and terminology. Deliverable: per-article accuracy report.
4. **Flag and fix**: Mark inaccurate articles, draft corrections, and submit updates for publishing. Deliverable: updated article drafts.
5. **Confirm publication**: Verify corrected articles are live and test search discoverability. Deliverable: publication confirmation log.

## Anti-Patterns

- **Reviewing without using the product**: Checking article text without actually performing the steps in the live product. *Why*: subtle UI changes and edge cases are only caught by hands-on verification.
- **Batch-delaying reviews**: Waiting to review all articles at once instead of reviewing as releases ship. *Why*: customers encounter stale content in the gap, generating avoidable tickets.

## Output

**On success**: An updated set of help centre articles verified against the current product state, with an accuracy report documenting what changed and why.

**On failure**: Report which articles could not be verified (e.g., feature not accessible, environment unavailable), what was reviewed, and recommend next steps to complete the audit.

## Related Skills

- [`help-centre-builder-support`](../../../customer-support/support-manager/help-centre-builder-support/SKILL.md) -- builds the initial help centre that this skill maintains over time.
- [`support-readiness-briefer-support`](../support-readiness-briefer-support/SKILL.md) -- readiness briefings surface the product changes that trigger content review.
