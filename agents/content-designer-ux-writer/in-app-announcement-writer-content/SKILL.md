---
name: in-app-announcement-writer-content
description: >
  This skill writes in-app announcement copy coordinated with content design standards. Use
  when asked to write an in-app banner, modal announcement, or feature release notification.
  Also consider when a product update needs in-context communication to users. Suggest when
  the user is about to ship a feature change without any in-app communication.
department: design
agent: content-designer-ux-writer
version: 1.0.0
complexity: simple
related-skills: []
---

# in-app-announcement-writer-content

## Agent: Content Designer UX Writer

L3 content designer and UX writer (Nx) responsible for support readiness, help content creation, in-app announcements, and training materials.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Writes in-app announcement copy coordinated with content design standards, ensuring users are informed of product changes in context without disrupting their workflow.

## When to Use

- When a new feature, product update, or breaking change needs to be communicated to users within the product interface.
- When a scheduled maintenance window, pricing change, or deprecation requires advance notice via in-app messaging.
- When product analytics show low adoption of a recently launched feature and in-app promotion could drive awareness.

## Workflow

1. **Announcement Brief**: Gather the announcement details: what changed, who it affects, when it takes effect, what action (if any) the user should take, and the announcement format (banner, modal, tooltip, toast). Deliverable: announcement brief.
2. **Copy Drafting**: Write the announcement copy following content design spec guidelines. Keep the headline under 8 words, the body under 40 words for banners or 80 words for modals. Include a clear CTA if action is required. Deliverable: draft copy with format annotations.
3. **Tone Calibration**: Verify the tone matches the announcement type: celebratory for new features, informational for updates, urgent for breaking changes, and empathetic for deprecations. Deliverable: tone-reviewed copy.
4. **Design & Engineering Review**: Review copy in the actual announcement component with the designer and engineer to verify fit, truncation behaviour, and dismissal logic. Deliverable: approved announcement copy.

## Anti-Patterns

- **Announcement overload**: Shipping multiple in-app announcements simultaneously or in rapid succession. *Why*: announcement fatigue causes users to dismiss all announcements without reading, including critical ones.
- **Vague CTAs**: Using generic call-to-action text like "Learn more" without indicating what the user will learn or do. *Why*: specific CTAs ("Set up your workspace" vs. "Learn more") drive higher engagement and set correct expectations.
- **Missing dismissal path**: Writing announcements without considering how users dismiss or revisit the information. *Why*: announcements that cannot be dismissed block users; announcements that disappear permanently lose users who were not ready to act.

## Output

**On success**: Produces approved in-app announcement copy with headline, body, CTA, format specification, and tone rationale. Delivered as a copy document or directly implemented in the announcement component.

**On failure**: Report which announcement elements could not be finalised (e.g., unclear product change details, undefined announcement format), what draft was produced, and recommend the product decisions needed to complete the copy.

## Related Skills

- [`content-design-spec`](../../content-design-lead/content-design-spec/SKILL.md) — All announcement copy must follow the content design spec voice and tone.
- [`launch-narrative-brand`](../../brand-designer/launch-narrative-brand/SKILL.md) — In-app announcements for major launches should align with the broader launch narrative.
- [`support-readiness-briefer`](../support-readiness-briefer/SKILL.md) — Announcements about changes should be coordinated with support readiness briefs.
