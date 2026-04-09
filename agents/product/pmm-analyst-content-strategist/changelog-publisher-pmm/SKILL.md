---
name: changelog-publisher-pmm
description: >
  This skill publishes the product changelog with clear, customer-friendly release notes.
  Use when a release ships and customers need to know what changed and why it matters.
  Also consider when support tickets spike around a feature change that was not communicated.
  Suggest when engineering closes a release milestone but no customer-facing notes exist yet.
department: product
agent: pmm-analyst-content-strategist
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "publish changelog"
  - "release notes"
  - "changelog update"
  - "product changelog"
  - "update changelog"
---

# changelog-publisher-pmm

## Agent: PMM Analyst Content Strategist
L3 PMM analyst and content strategist (multi-instance) responsible for in-app announcements, changelog publishing, case study creation, and content engine operations.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Publishes the product changelog with clear, customer-friendly release notes that translate engineering work into user value.

## When to Use
- When a product release ships and customers need a concise summary of what changed and how it benefits them
- When a bug fix or breaking change requires proactive communication to prevent support ticket spikes
- When a batch of small improvements has accumulated and needs a consolidated update to keep the changelog current

## Workflow
1. **Collect release inputs**: Pull the list of merged PRs, resolved tickets, and PM release notes from the release milestone. Confirm scope with the PM and engineering lead. Deliverable: raw change list with ticket references and severity tags.
2. **Translate to customer language**: Rewrite each change as a benefit-oriented sentence. Strip internal jargon, ticket numbers, and implementation details. Group entries by theme (new features, improvements, fixes). Deliverable: draft changelog entry in the standard template.
3. **Add context and visuals**: For significant features, add a one-sentence "why this matters" line. Attach screenshots or GIFs where a visual makes the change immediately clear. Deliverable: enriched draft with media assets embedded.
4. **Review and publish**: Send the draft to PM for accuracy review. Incorporate feedback, then publish to the changelog page and trigger the RSS/email notification. Deliverable: live changelog entry with distribution confirmed.

## Anti-Patterns
- **Engineer-speak pass-through**: Copying commit messages or ticket titles verbatim into the changelog. *Why*: Customers do not understand internal terminology; they skip entries they cannot parse, missing changes that affect their workflows.
- **Silent releases**: Shipping changes without a changelog entry because the change seems minor. *Why*: Accumulated silent changes erode customer trust and generate avoidable support tickets when users notice undocumented behavior shifts.
- **Delayed publishing**: Letting changelog entries pile up weeks after the actual release. *Why*: Late notes feel like afterthoughts; customers who already discovered the change through confusion lose confidence in the communication cadence.

## Output
**On success**: A published changelog entry grouped by theme, written in customer-friendly language, with visual aids for major changes, distributed via the changelog page and notification channels within 24 hours of release.

**On failure**: Report which inputs were missing (incomplete release notes, unavailable PM for review), what partial draft exists, and recommend a timeline for completing and publishing the entry.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
