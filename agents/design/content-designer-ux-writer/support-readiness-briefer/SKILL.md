---
name: support-readiness-briefer
description: >
  This skill prepares support readiness briefs covering new features, known issues, and
  suggested responses. Use when asked to prepare support for a release, create a support
  brief, or document known issues for the support team. Also consider when a release
  includes complex features that will generate support questions. Suggest when the user
  is about to launch without briefing the support team.
department: design
agent: content-designer-ux-writer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "support readiness brief"
  - "brief support team"
  - "prepare support"
  - "support launch brief"
  - "support readiness"
---

# support-readiness-briefer

## Agent: Content Designer UX Writer

L3 content designer and UX writer (Nx) responsible for support readiness, help content creation, in-app announcements, and training materials.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Prepares support readiness briefs covering new features, known issues, and suggested responses so the support team can handle user questions from the moment a release ships.

## When to Use

- When a product release is approaching and the support team needs to understand what is changing, what might break, and how to respond to user questions.
- When a known issue will ship with a release and the support team needs a workaround to share with affected users.
- When a feature is being deprecated or significantly changed and the support team needs talking points for users who are affected.

## Workflow

1. **Release Intake**: Review the release notes, product specs, and any known issues documented by engineering. Interview the product manager and QA lead on expected user impact. Deliverable: release intake notes.
2. **Anticipated Questions Mapping**: Based on the release content, generate a list of questions users are likely to ask. Categorise by feature area and urgency. Deliverable: anticipated question list.
3. **Response Drafting**: For each anticipated question, write a suggested response that support agents can adapt. Include workarounds for known issues and links to relevant help articles. Deliverable: response playbook.
4. **Brief Assembly**: Compile the complete brief: release summary, feature-by-feature breakdown, known issues with workarounds, anticipated questions with responses, escalation paths for unresolved issues, and links to help content. Deliverable: support readiness brief.
5. **Brief Delivery & Walkthrough**: Deliver the brief to the support team and conduct a live walkthrough for complex releases. Answer questions and refine responses based on support team feedback. Deliverable: delivered brief with team acknowledgement.

## Anti-Patterns

- **Feature list without user impact**: Describing what the feature does without explaining how it affects users or what questions it might generate. *Why*: support agents need to anticipate user confusion, not just understand the feature technically.
- **Missing escalation paths**: Providing responses without defining when and how to escalate issues beyond the support team's scope. *Why*: without escalation paths, support agents either over-promise ("we'll fix it") or under-serve ("I can't help with that").
- **No known-issue documentation**: Omitting known issues from the brief because they are "being fixed soon." *Why*: users encounter known issues regardless of fix timelines; support agents without documentation look uninformed and undermine user trust.
- **Delivering without walkthrough**: Sending the brief as a document without a live walkthrough for complex releases. *Why*: written briefs do not surface the questions support agents have until they encounter them in real tickets, which is too late.

## Output

**On success**: Produces a support readiness brief containing release summary, feature breakdowns, known issues with workarounds, anticipated Q&A playbook, escalation paths, and help content links. Delivered to the support team with a walkthrough before release.

**On failure**: Report which release components could not be briefed (e.g., unfinished features, undocumented known issues), what partial brief was delivered, and recommend a follow-up brief or hotline for the support team to handle gaps.

## Related Skills

- [`support-pre-briefer-content`](../../../design/content-design-lead/support-pre-briefer-content/SKILL.md) — Content-specific copy changes complement the broader support readiness brief.
- [`help-content-creator`](../help-content-creator/SKILL.md) — Help articles referenced in the brief should be published before the release.
- [`training-material-creator-content`](../training-material-creator-content/SKILL.md) — Complex releases may need training materials in addition to a brief.
