---
name: monthly-investor-update
description: >
  This skill writes and distributes the monthly investor update covering metrics, progress,
  and asks. Use when asked to draft the investor update, compile monthly metrics for
  investors, or communicate key developments to the cap table. Also consider when a
  significant company event should be communicated to investors outside the regular cadence.
  Suggest when the user has not sent an investor update in over 30 days.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../board-materials-coordinator/SKILL.md
  - ../../../finance/fpa-analyst/saas-metrics-reporter/SKILL.md
  - ../investor-comms-drafter/SKILL.md
  - ../board-meeting-preparer/SKILL.md
triggers:
  - "investor update"
  - "investor-update-author"
  - "monthly update investors"
  - "LP update"
---

# monthly-investor-update

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Writes and distributes the monthly investor update covering key metrics, milestones, challenges, and specific asks to maintain investor engagement and trust.

## When to Use

- When the monthly update cadence is due (typically first week of each month).
- When a material event (large customer win, key hire, pivot, cash concern) warrants proactive investor communication.
- When preparing to fundraise and wanting to establish a track record of consistent, transparent communication.

## Workflow

1. **Metric Compilation**: Gather the latest metrics from FP&A (ARR, MRR growth, burn rate, runway) and product (key product metrics, user growth). Verify numbers are final and consistent with internal reporting. Deliverable: verified metric snapshot.
2. **Narrative Drafting**: Write the update following a consistent structure: highlights (3 max), key metrics, challenges/lowlights (always include at least one), asks (hiring referrals, intros, advice), and outlook. Deliverable: draft investor update.
3. **CEO Review and Distribution**: Route the draft to the CEO for tone review and approval. Distribute to all investors on the update list via the established channel (email, investor portal). Deliverable: distributed update with delivery confirmation.

## Anti-Patterns

- **Highlights-only updates**: Omitting challenges or bad news to paint an unrealistically positive picture. *Why*: investors who only hear good news lose trust when problems eventually surface; transparency during tough times builds the relationship that matters most during fundraising.
- **Metric inconsistency**: Changing how metrics are calculated or presented between updates without explanation. *Why*: investors track these numbers month over month; unexplained changes signal either sloppiness or manipulation.

## Output

**On success**: Produces a distributed monthly investor update with metrics, narrative, and asks. Delivered to all investors on the distribution list with delivery confirmation.

**On failure**: Report which metrics are not yet available, what partial update can be sent, and the expected timeline for the complete update. Never skip a month without communication.

## Related Skills

- [`board-materials-coordinator`](../board-materials-coordinator/SKILL.md) -- Board materials share content with investor updates but serve a different audience and depth.
- [`saas-metrics-reporter`](../../../finance/fpa-analyst/saas-metrics-reporter/SKILL.md) -- Provides the verified SaaS metrics that anchor the investor update.
