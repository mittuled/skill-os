---
name: support-pre-briefer-content
description: >
  This skill briefs the support team on new UX copy and terminology changes before release.
  Use when asked to prepare support for copy changes, brief the support team on new
  terminology, or create a pre-release content changelist for support. Also consider when a
  release includes renamed features or changed UI labels. Suggest when the user is about to
  ship terminology changes without notifying support.
department: design
agent: content-design-lead
version: 1.0.0
complexity: simple
related-skills: []
---

# support-pre-briefer-content

## Agent: Content Design Lead

L2 content design lead (1x) (moved from Product, now reports to Head of Design) responsible for microcopy, voice standards, UX copy, and help content architecture.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Briefs the support team on new UX copy and terminology changes before release, ensuring support agents use consistent language and can guide users through updated interfaces.

## When to Use

- When a release includes new or changed terminology, renamed features, or significantly revised UX copy that support agents need to know about.
- When a content design spec update introduces new voice/tone guidelines that affect how support communicates with users.
- When help centre content is being updated in parallel with a product release and support needs to know what changed and why.

## Workflow

1. **Change Inventory**: Compile all UX copy and terminology changes included in the upcoming release. For each change, note the old term/copy, the new term/copy, and the rationale. Deliverable: copy changelist.
2. **Support Impact Assessment**: Identify which changes affect support workflows: new terms users will ask about, renamed features that will confuse users referencing old names, and copy changes that alter how users describe their problems. Deliverable: support impact notes.
3. **Brief Document Creation**: Write a pre-release brief containing the changelist, impact assessment, suggested responses for anticipated user questions, and links to updated help articles. Deliverable: support pre-release brief.
4. **Brief Delivery**: Share the brief with the support team lead and conduct a walkthrough if changes are significant. Deliverable: delivered and acknowledged brief.

## Anti-Patterns

- **Post-release briefing**: Sending the brief after the release ships instead of before. *Why*: support agents encounter confused users immediately after release; a late brief means the first wave of tickets gets inconsistent responses.
- **Change-only, no context**: Listing what changed without explaining why or how users might react. *Why*: support agents who understand the rationale can explain changes to users confidently rather than just acknowledging them.
- **Omitting deprecated terms**: Not documenting old terminology that users will still use when contacting support. *Why*: users do not read changelogs; support agents need a mapping from old terms to new terms to understand what users are describing.

## Output

**On success**: Produces a support pre-release brief containing a copy changelist with old/new mappings, support impact assessment, suggested responses, and help article links. Delivered to the support team before the release ships.

**On failure**: Report which changes could not be fully documented (e.g., copy still in flux at brief deadline), what partial brief was delivered, and recommend a follow-up brief once the remaining changes are finalised.

## Related Skills

- [`content-design-spec`](../content-design-spec/SKILL.md) — Spec changes that affect terminology trigger support briefings.
- [`copy-implementation-reviewer`](../copy-implementation-reviewer/SKILL.md) — Implementation review may surface unexpected copy changes that need support briefing.
- [`support-readiness-briefer`](../../../design/content-designer-ux-writer/support-readiness-briefer/SKILL.md) — Broader support readiness briefs complement the content-specific focus of this skill.
