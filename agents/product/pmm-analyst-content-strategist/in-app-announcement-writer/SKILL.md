---
name: in-app-announcement-writer
description: >
  This skill writes in-app announcement copy for new feature releases and product updates.
  Use when a feature ships and users need to discover it inside the product. Also consider when
  adoption metrics for a recently launched feature are below target and a nudge could help.
  Suggest when a release is planned but no in-app communication has been drafted yet.
department: product
agent: pmm-analyst-content-strategist
version: 1.0.0
complexity: simple
related-skills:
  - case-study-extractor-pmm
  - changelog-publisher-pmm
  - content-engine-builder-pmm
  - ga-announcement
  - partner-activation-planner-pmm
triggers:
  - "write in-app announcement pmm"
  - "in-app release note"
  - "product announcement"
  - "feature announcement copy"
  - "in-app message pmm"
---

# in-app-announcement-writer

## Agent: PMM Analyst Content Strategist
L3 PMM analyst and content strategist (multi-instance) responsible for in-app announcements, changelog publishing, case study creation, and content engine operations.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Writes in-app announcement copy for new feature releases and product updates, optimizing for discovery and activation within the product experience.

## When to Use
- When a new feature or significant improvement ships and users need to discover it within the product interface
- When adoption of a recently launched feature is below target and an in-app nudge could drive awareness
- When a breaking change or workflow shift requires proactive in-app communication to reduce confusion

## Workflow
1. **Gather feature context**: Review the PM release brief, feature documentation, and target user segment. Confirm the announcement type (banner, modal, tooltip, slideout) and placement with the product and design teams. Deliverable: context brief with feature summary, target audience, and agreed announcement format.
2. **Write the copy**: Draft headline, body, and CTA in the character limits set by the announcement component. Lead with the user benefit, not the feature name. Keep body copy under 40 words. Deliverable: draft copy with variants for A/B testing if applicable.
3. **Review and approve**: Send to PM for accuracy and to design for visual fit. Confirm that the CTA links to the correct destination. Deliverable: approved copy ready for implementation.
4. **Coordinate publish and sunset**: Confirm the publish date and auto-dismiss or expiration rules with engineering. Verify the announcement renders correctly in staging. Deliverable: live in-app announcement with confirmed expiration date.

## Anti-Patterns
- **Feature-name headlines**: Leading with the internal feature name instead of the benefit the user gets. *Why*: Users scan for relevance to their workflow; a jargon headline gets dismissed instantly, wasting the impression.
- **Wall of text**: Writing multi-paragraph in-app messages that block the user's workflow. *Why*: Users are mid-task when they encounter in-app announcements; long copy triggers immediate dismissal and trains users to ignore future announcements.
- **Zombie announcements**: Leaving announcements live indefinitely after the feature is no longer new. *Why*: Stale announcements clutter the interface, reduce trust in the communication channel, and annoy users who have already seen the message.

## Output
**On success**: A live in-app announcement with benefit-led copy under 40 words, a clear CTA linking to the correct destination, confirmed publish and expiration dates, and variant copy for A/B testing if requested.

**On failure**: Report what blocked publication (missing design approval, broken CTA link, staging render issue), what draft copy exists, and recommend a revised timeline.

## Related Skills
- [`case-study-extractor-pmm`](../case-study-extractor-pmm/SKILL.md) — sibling skill under the same agent — combine with case-study-extractor-pmm for end-to-end coverage
- [`changelog-publisher-pmm`](../changelog-publisher-pmm/SKILL.md) — sibling skill under the same agent — combine with changelog-publisher-pmm for end-to-end coverage
- [`content-engine-builder-pmm`](../content-engine-builder-pmm/SKILL.md) — sibling skill under the same agent — combine with content-engine-builder-pmm for end-to-end coverage
- [`ga-announcement`](../ga-announcement/SKILL.md) — sibling skill under the same agent — combine with ga-announcement for end-to-end coverage
- [`partner-activation-planner-pmm`](../partner-activation-planner-pmm/SKILL.md) — sibling skill under the same agent — combine with partner-activation-planner-pmm for end-to-end coverage
