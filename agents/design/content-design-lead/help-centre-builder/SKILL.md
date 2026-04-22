---
name: help-centre-builder
description: >
  This skill architects and writes the initial help centre content structure. Use when asked
  to build a help centre, create a knowledge base architecture, or design the information
  architecture for self-service support content. Also consider when a product is approaching
  launch with no self-service support content. Suggest when the user is about to launch
  without help documentation.
department: design
agent: content-design-lead
version: 1.0.0
complexity: medium
related-skills:
  - content-design-spec
  - help-content-creator
  - support-pre-briefer-content
triggers:
  - "build help centre"
  - "help center content"
  - "create help docs"
  - "help centre"
  - "support content"
---

# help-centre-builder

## Agent: Content Design Lead

L2 content design lead (1x) (moved from Product, now reports to Head of Design) responsible for microcopy, voice standards, UX copy, and help content architecture.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Architects and writes the initial help centre content structure, creating an information architecture that enables users to find answers through self-service before contacting support.

## When to Use

- When a product is approaching its first public launch and needs a help centre built from scratch.
- When an existing help centre has grown organically without information architecture and needs restructuring.
- When support ticket volume indicates users cannot find answers to common questions, suggesting the help centre structure is failing.

## Workflow

1. **Content Needs Analysis**: Review the product feature set, common support ticket categories, onboarding friction points, and user research findings to identify what content the help centre must cover. Deliverable: content needs inventory.
2. **Information Architecture Design**: Design the help centre taxonomy: top-level categories, subcategories, and article groupings. Use card sorting principles (open or closed sort with representative users if possible) to validate the structure matches user mental models. Deliverable: help centre IA diagram.
3. **Article Planning**: Create an article plan listing every article needed, its category placement, target audience (new user, admin, power user), and priority (launch-critical vs. post-launch). Deliverable: article plan with priority tiers.
4. **Template & Style Definition**: Define article templates for different content types (how-to guide, troubleshooting article, conceptual explainer, FAQ) with structural conventions, voice/tone rules per template, and screenshot/media guidelines. Deliverable: help content style guide.
5. **Launch-Critical Content Writing**: Write the highest-priority articles covering getting started, core workflows, account management, and billing/payment. Apply the content design spec voice and tone. Deliverable: launch-ready article set.
6. **Review & Publishing**: Review articles with product and support teams for accuracy. Publish to the help centre platform and verify navigation, search, and cross-linking. Deliverable: published help centre.

## Anti-Patterns

- **Product-structure mirroring**: Organising help content by product feature names rather than by user tasks or questions. *Why*: users search for help based on what they are trying to do, not which feature they are in; product-structured help centres have poor findability.
- **Writing without templates**: Authoring articles without standardised templates for different content types. *Why*: inconsistent article structure forces users to relearn how to read each article, increasing cognitive load and time-to-answer.
- **Launch without search verification**: Publishing the help centre without testing that common user queries return relevant results. *Why*: many users navigate help centres via search; if search fails, the content may as well not exist.
- **Ignoring support team input**: Building the help centre without consulting the support team on actual ticket patterns. *Why*: the support team knows what users actually ask; without their input, the help centre addresses assumed questions rather than real ones.

## Output

**On success**: Produces a published help centre containing information architecture, article templates, style guide, and launch-critical articles. Delivered as a live help centre with verified navigation and search.

**On failure**: Report which content areas could not be completed (e.g., product documentation gaps, unresolved feature questions), what partial structure was built, and recommend a post-launch content plan to fill gaps.

## Related Skills

- [`content-design-spec`](../content-design-spec/SKILL.md) — Voice, tone, and copy standards apply to all help centre content.
- [`help-content-creator`](../../../design/content-designer-ux-writer/help-content-creator/SKILL.md) — Creates individual help articles within the architecture built here.
- [`support-pre-briefer-content`](../support-pre-briefer-content/SKILL.md) — Help centre content updates should be coordinated with support briefings.
