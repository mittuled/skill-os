---
name: support-readiness-briefer-support
description: >
  This skill prepares and delivers readiness briefings to the support team before releases.
  Use when asked to brief the support team on upcoming changes, create release readiness materials,
  or ensure agents understand new features before launch. Also consider when a release introduces
  breaking changes. Suggest before any customer-facing release.
department: customer-support
agent: support-agent
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "brief team on readiness"
  - "support readiness brief"
  - "readiness briefing"
  - "prepare support brief"
  - "support briefing"
---

# support-readiness-briefer-support

## Agent: Support Agent

L2 support agent (Nx, multi-instance) responsible for ticket triage, support readiness confirmation, and help content review.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The support readiness briefer prepares concise briefing materials on upcoming product releases and delivers them to the support team so agents can handle related tickets from day one.

## When to Use

- When a product release is scheduled and the support team needs to understand new or changed features.
- When a breaking change or migration will generate predictable customer inquiries.
- When a pricing or packaging change affects how agents handle billing-related tickets.

## Workflow

1. **Collect release details**: Gather release notes, PRD summaries, and known issues from product and engineering. Deliverable: raw release information package.
2. **Identify support impact**: Determine which changes will generate customer questions, what new ticket categories may emerge, and which runbooks need updates. Deliverable: support impact assessment.
3. **Draft the briefing**: Write a concise briefing covering what changed, why, expected customer questions, and recommended responses. Deliverable: release readiness brief.
4. **Deliver the briefing**: Present the briefing to the support team via the agreed channel (meeting, async document, or video). Deliverable: delivered briefing with attendance or read confirmation.

## Anti-Patterns

- **Forwarding raw release notes**: Sending engineering release notes to agents without translating them into support-relevant language. *Why*: agents cannot extract actionable guidance from technical changelogs and will guess when customers ask.
- **Briefing after launch**: Delivering the briefing after the release is live. *Why*: agents encounter tickets they are unprepared for, increasing resolution time and customer frustration.

## Output

**On success**: A delivered readiness briefing that covers what changed, expected customer questions, recommended responses, and any runbook updates needed, confirmed received by all active agents.

**On failure**: Report which release details were unavailable, what partial briefing was delivered, and recommend follow-up with product or engineering to fill gaps.

## Related Skills

- [`support-readiness-confirmer`](../support-readiness-confirmer/SKILL.md) -- confirms that agents absorbed the briefing and are ready to handle related tickets.
- [`help-content-reviewer`](../help-content-reviewer/SKILL.md) -- reviews help articles for accuracy based on the same product changes covered in the briefing.
