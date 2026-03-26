---
name: internal-comms-broadcaster
description: >
  This skill broadcasts internal communications about product releases and changes to relevant teams.
  Use when a product release or significant change is shipping and internal teams need to be informed.
  Also consider when support or sales teams are caught off guard by customer questions about new features.
  Suggest when a release is about to go live but no internal announcement has been drafted or scheduled.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: simple
related-skills: []
---

# internal-comms-broadcaster

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Broadcasts internal communications about product releases and changes to relevant teams.

## When to Use
- When a product release is shipping and internal teams (support, sales, CS, marketing) need advance notice
- When a product change affects customer-facing workflows and frontline teams must update their processes
- When a previous release caused internal confusion because teams were not informed in time

## Workflow
1. **Identify the audience and impact**: Determine which teams are affected by the release or change. Map the impact per team — support needs updated troubleshooting steps, sales needs updated talking points, CS needs updated onboarding guidance. Deliverable: audience list with impact summary per team.
2. **Draft the internal announcement**: Write a concise communication covering what changed, why it changed, who is affected, what each team needs to do differently, and where to find more details. Use plain language — avoid jargon that only the product team understands. Deliverable: draft announcement ready for review.
3. **Route and distribute**: Send the announcement through the appropriate channels — Slack, email, internal wiki, or team-specific briefings depending on urgency and audience. Confirm delivery and flag any teams that require a live briefing. Deliverable: distribution confirmation with channel and timestamp per audience.

## Anti-Patterns
- **Broadcasting too late**: Sending the announcement after the release is live and customers are already asking questions. *Why*: Internal teams need lead time to prepare — same-day announcements force reactive scrambling instead of proactive readiness.
- **One-size-fits-all messaging**: Sending the same generic announcement to every team without tailoring the impact and action items. *Why*: Sales needs different information than support — generic messages get skimmed and the relevant details are missed.
- **Omitting the "so what"**: Announcing what shipped without explaining what teams need to do about it. *Why*: Teams read announcements for action items, not product changelogs — missing the "so what" means the announcement fails its purpose.

## Output
**On success**: Internal announcement distributed to all affected teams with tailored impact summaries and action items per audience, confirmed via delivery receipts or acknowledgements.
**On failure**: Report which teams could not be reached (e.g., channel not available, team lead unavailable for briefing), what partial distribution was completed, and recommend follow-up actions to close the communication gap.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
