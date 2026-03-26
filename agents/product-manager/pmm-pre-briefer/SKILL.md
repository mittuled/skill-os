---
name: pmm-pre-briefer
description: >
  This skill briefs the product marketing team on upcoming releases to align messaging and launch
  activities. Use when asked to prepare a PMM handoff, create a release brief, or sync marketing
  on what is shipping. Also consider when a release date is approaching and PMM has not been
  looped in. Suggest when the team is about to ship without coordinated go-to-market messaging.
department: product
agent: product-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# pmm-pre-briefer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Briefs the product marketing team on upcoming releases so that messaging, positioning, and launch activities are aligned before the feature reaches customers.

## When to Use
- When a feature is entering its final build sprint and PMM needs lead time to prepare messaging
- When a release scope has changed materially and previously communicated positioning is now inaccurate
- When PMM asks "what's shipping next?" and no structured brief exists

## Workflow
1. **Compile release facts**: Gather the feature name, target release date, target audience, key capabilities, known limitations, and any changes from the original scope. Deliverable: structured fact sheet.
2. **Frame the value narrative**: Articulate the user problem being solved and the primary benefit in one sentence each. State what is new vs. what is improved. Deliverable: value summary suitable for PMM to adapt into customer-facing copy.
3. **Deliver the brief**: Send the fact sheet and value summary to the PMM lead with enough lead time (minimum two weeks before release). Flag any sensitivities -- breaking changes, pricing implications, competitive positioning risks. Deliverable: delivered brief with PMM acknowledgment.

## Anti-Patterns
- **Last-minute briefing**: Sending the brief days before release, leaving PMM no time to prepare assets. *Why*: Rushed messaging misrepresents the feature or misses the launch window entirely.
- **Feature-spec dump**: Forwarding the PRD instead of a curated brief. *Why*: PMM needs value framing and audience context, not implementation details; a raw spec buries the story.
- **Omitting limitations**: Briefing only the happy path without mentioning known gaps or constraints. *Why*: PMM creates promises the product cannot keep, generating support load and eroding customer trust.

## Output
**On success**: A release brief containing feature summary, value narrative, target audience, release date, known limitations, and competitive context -- delivered to PMM with acknowledgment.

**On failure**: Report what information is missing (unclear value prop, unconfirmed release date, unknown limitations), what was attempted, and recommend who to consult to close the gaps.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
