---
name: support-ticket-triage
description: >
  This skill triages incoming support tickets to identify product bugs and urgent issues requiring product team attention.
  Use when support tickets need review to separate product bugs from usage questions and configuration issues.
  Also consider when ticket volume spikes after a release or when support escalates a cluster of similar reports.
  Suggest when a release has shipped and no one has reviewed the incoming ticket stream for product-related patterns.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
---

# support-ticket-triage

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Triages incoming support tickets to identify product bugs and urgent issues requiring product team attention.

## When to Use
- When a batch of support tickets needs review to identify which ones indicate product bugs vs. user error or configuration issues
- When ticket volume spikes after a release and the product team needs rapid visibility into what is breaking
- When the support team escalates a cluster of similar tickets suggesting a systemic product issue
- When the regular triage cadence (daily or per-sprint) is due and product-relevant tickets need routing

## Workflow
1. **Pull the ticket queue**: Retrieve unreviewed support tickets from the triage queue — filtered to product-relevant categories if the support tool allows pre-filtering. Note the volume, date range, and any pre-assigned tags. Deliverable: ticket list with ID, summary, customer, severity, and date for each.
2. **Categorise each ticket**: Review each ticket and assign a category — product bug, feature request, usage question, configuration issue, documentation gap, or duplicate. For ambiguous tickets, check reproduction steps or customer context before categorising. Deliverable: categorised ticket list with category and confidence level per ticket.
3. **Assess severity and urgency**: For product bugs, assign severity based on impact (data loss, broken workflow, cosmetic) and breadth (one user, one segment, all users). Flag any ticket that indicates a regression or a blocker for a high-value customer. Deliverable: severity-tagged bug list with impact and breadth notes.
4. **Identify patterns**: Look for clusters — multiple tickets about the same feature, the same error, or the same customer segment. Clusters suggest systemic issues that warrant higher priority than individual ticket severity would indicate. Deliverable: pattern summary listing any clusters with ticket counts and affected scope.
5. **Route and escalate**: Route product bugs to the appropriate engineering team or product manager. Escalate critical issues (data loss, security, widespread outage) immediately through the incident process. Route feature requests to the feedback intake. Deliverable: routing log showing where each product-relevant ticket was sent, with escalation flags for critical items.

## Anti-Patterns
- **Triaging by title only**: Categorising tickets based on the subject line without reading the details or reproduction steps. *Why*: Titles are often misleading — a ticket titled "feature request" may describe a bug, and a "bug report" may be a misunderstanding of intended behaviour.
- **Treating every bug as equal urgency**: Routing all bugs with the same priority regardless of impact and breadth. *Why*: Engineering capacity is finite — without severity differentiation, critical issues compete with cosmetic ones and response times suffer across the board.
- **Ignoring pattern signals**: Processing tickets individually without looking for clusters. *Why*: A single P3 ticket is low priority, but twenty P3 tickets about the same issue represent a systemic problem that may warrant P1 treatment.
- **Skipping the routing step**: Categorising tickets but leaving them in the triage queue without explicit routing. *Why*: Triage without routing is incomplete — tickets that are categorised but not routed remain in limbo and response SLAs are missed.

## Output
**On success**: A triage report containing categorised tickets, severity assessments for bugs, pattern analysis, and a routing log showing where each product-relevant ticket was directed — with escalation confirmations for any critical issues.
**On failure**: Report which tickets could not be categorised (e.g., insufficient reproduction steps, unclear customer context), what partial triage was completed, and recommend follow-up actions (e.g., "request reproduction steps from customer for tickets #1234 and #1256").

## Related Skills
- (none yet — cross-references added in Phase 1.6)
