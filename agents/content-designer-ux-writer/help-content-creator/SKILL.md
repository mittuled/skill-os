---
name: help-content-creator
description: >
  This skill creates help articles, FAQs, and how-to guides for the help centre. Use when
  asked to write a help article, create a how-to guide, or add FAQ content. Also consider
  when a new feature launches without documentation or when support tickets indicate users
  cannot find answers. Suggest when the user ships a feature without corresponding help
  content.
department: design
agent: content-designer-ux-writer
version: 1.0.0
complexity: simple
related-skills: []
---

# help-content-creator

## Agent: Content Designer UX Writer

L3 content designer and UX writer (Nx) responsible for support readiness, help content creation, in-app announcements, and training materials.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Creates help articles, FAQs, and how-to guides for the help centre, following the established information architecture and content design standards.

## When to Use

- When a new feature or product update requires help documentation before or at launch.
- When support ticket analysis identifies a topic that users frequently ask about but no help article exists.
- When existing help articles need to be rewritten due to product changes, outdated screenshots, or unclear instructions.

## Workflow

1. **Topic Research**: Review the feature documentation, product release notes, and any support ticket patterns related to the topic. Identify the user's goal and common confusion points. Deliverable: article brief with topic scope and target audience.
2. **Article Drafting**: Write the article using the appropriate template (how-to, troubleshooting, conceptual explainer, or FAQ) from the help content style guide. Use task-oriented headings, numbered steps for procedures, and screenshots for complex UI interactions. Deliverable: draft article.
3. **Accuracy Review**: Share the draft with the product or engineering team to verify technical accuracy. Deliverable: accuracy-reviewed draft.
4. **Publishing & Cross-Linking**: Publish the article in the correct help centre category, add cross-links to related articles, and verify the article appears in search results for relevant queries. Deliverable: published and cross-linked article.

## Anti-Patterns

- **Feature-description articles**: Writing articles that describe what a feature does instead of how to accomplish a task with it. *Why*: users visit help centres with a goal, not to learn about features; task-oriented content resolves their problem faster.
- **Wall-of-text formatting**: Writing long paragraphs without headings, numbered steps, or visual breaks. *Why*: users scan help articles for relevant sections; dense text forces them to read everything to find their answer.
- **Stale screenshots**: Including screenshots that do not match the current product UI. *Why*: outdated screenshots confuse users who cannot match what they see in the article to what they see in the product.

## Output

**On success**: Produces a published help article in the correct category with cross-links, accurate screenshots, and verified search discoverability. Delivered as a live article in the help centre.

**On failure**: Report which article elements could not be completed (e.g., feature not yet stable for screenshots, unresolved technical questions), what draft was produced, and recommend a timeline for completing the article.

## Related Skills

- [`help-centre-builder`](../../content-design-lead/help-centre-builder/SKILL.md) — Provides the IA and templates this skill operates within.
- [`ux-copy-writer`](../../content-design-lead/ux-copy-writer/SKILL.md) — Help articles may reference or expand on UX copy for feature context.
- [`support-readiness-briefer`](../support-readiness-briefer/SKILL.md) — New help articles should be included in support readiness briefs.
