---
name: competitive-response-monitor-pmm
description: >
  Monitors competitive activity and maintains the competitive response playbook.
  Use when a competitor ships a new feature, changes pricing, or launches a campaign.
  Also consider when sales reports losing deals to a specific competitor.
  Suggest when win-rate drops or competitive mentions spike in customer calls.
department: product
agent: pmm
version: 1.0.0
complexity: complex
related-skills: []
---

# competitive-response-monitor-pmm

## Agent: PMM
L2 product marketing manager responsible for competitive intelligence, positioning, GTM planning, pricing strategy, launch narrative, and sales enablement.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description
Monitors competitive activity and maintains the competitive response playbook, ensuring the organization reacts swiftly and strategically to market moves by rival products.

## When to Use
- A competitor announces a new product, feature, or integration that overlaps with your positioning.
- Sales flags a pattern of lost deals citing a specific competitor's capability.
- A competitor changes pricing, packaging, or tier structure.
- Analyst reports or review-site sentiment shifts in a competitor's favour.
- A competitor launches a major marketing campaign targeting your ICP.
- Win/loss data reveals a new or resurgent competitive threat.
- Leadership requests a rapid competitive brief before a board meeting or press response.

## Workflow
1. Ingest the competitive signal. Identify the source (sales call transcript, press release, G2 review, analyst note, social mention) and tag the competitor.
2. Classify the signal by threat level: cosmetic (messaging-only change), tactical (feature or pricing move), or strategic (market repositioning or new entrant).
3. Pull the existing battle card for the competitor from the response playbook. If none exists, create a skeleton card with company overview, known positioning, and pricing.
4. Assess impact on your current positioning and messaging hierarchy. Map the competitor's move against your differentiation pillars.
5. Draft or update the competitive response. For tactical signals, update the objection-handling section of the battle card. For strategic signals, draft a competitive brief with recommended counter-positioning and talking points.
6. Validate the response with product (for technical accuracy) and sales leadership (for field relevance). Incorporate feedback within one review cycle.
7. Distribute the updated battle card or brief. Push to the sales enablement platform, post in the competitive-intel channel, and flag the update in the next sales standup.
8. Update the competitive response playbook index with the date, signal type, and response status.
9. Set a monitoring cadence for the signal. High-threat signals get weekly tracking; low-threat signals get monthly check-ins.
10. After 30 days, review whether the competitive move had the predicted impact on win rates or pipeline. Archive or escalate accordingly.

## Anti-Patterns
- **Reacting to every rumour without verification.** *Why: False signals erode trust in the competitive intel function and waste sales time on phantom threats.*
- **Updating battle cards without notifying sales.** *Why: Stale enablement is worse than no enablement because reps default to outdated talking points in live deals.*
- **Focusing only on feature-for-feature comparison.** *Why: Buyers evaluate solutions holistically; positioning that only lists features misses narrative, trust, and ecosystem advantages.*
- **Hoarding competitive intel in PMM without cross-functional distribution.** *Why: Competitive intelligence only creates value when it reaches the people making daily customer-facing decisions.*
- **Treating all competitors equally regardless of threat level.** *Why: Spreading attention across ten competitors dilutes the depth needed to counter the two or three that actually appear in deals.*

## Output

**Success:**
- Updated battle card or competitive brief distributed to sales within 48 hours of a verified signal.
- Clear counter-positioning statement with proof points, objection handlers, and recommended talk track.
- Playbook index entry with signal classification, response date, and follow-up cadence.

**Failure:**
- Signal acknowledged but no response drafted within the SLA window.
- Battle card updated with inaccurate technical claims that sales surfaces in a live deal.
- Competitive brief that restates the competitor's announcement without actionable counter-positioning.

## Related Skills
- competitor-mapper-pmm
- positioning-crafter
- sales-playbook-messaging
- pmm-market-intelligence
