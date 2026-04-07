---
name: support-pre-briefer
description: >
  This skill briefs the support team on upcoming releases so they are ready for customer questions.
  Use before any customer-facing release to ensure support agents can handle inbound queries.
  Suggest when a release is shipping without a support enablement handoff.
department: product
agent: product-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# support-pre-briefer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Briefs the support team on upcoming releases so they are ready for customer questions.

## When to Use
- When a customer-facing release is scheduled and the support team has not yet been briefed on changes
- When a feature changes existing user workflows and support agents need updated talking points
- When a known-issues list exists for a release and support needs workaround scripts

## Workflow
1. **Compile release summary**: Gather release notes, feature descriptions, known limitations, and any changed workflows from the sprint review and release checklist. Deliverable: one-page release brief covering what changed, who it affects, and known issues.
2. **Draft support-facing materials**: Translate the release brief into support-friendly language — FAQs, troubleshooting steps, and escalation paths for edge cases. Deliverable: FAQ document and escalation guide.
3. **Deliver the briefing**: Share materials with the support team lead and walk through the key changes. Confirm the team understands new workflows and knows when to escalate. Deliverable: briefing delivered with acknowledgment from the support lead.

## Anti-Patterns
- **Briefing after release**: Sending the support brief after the feature is already live. *Why*: Support agents face customer questions unprepared, leading to incorrect answers and escalation spikes.
- **Developer-language briefs**: Sending raw engineering release notes without translating them into customer-facing language. *Why*: Support agents cannot interpret technical jargon and will misrepresent the change to customers.

## Output
**On success**: A support briefing package containing a release summary, FAQ with troubleshooting steps, and escalation guide — delivered to the support team before the release goes live.
**On failure**: Report what information is missing (incomplete release notes, undocumented known issues), and recommend actions to close the gap before release.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
