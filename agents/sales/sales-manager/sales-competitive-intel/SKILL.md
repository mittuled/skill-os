---
name: sales-competitive-intel
description: >
  This skill produces structured competitive intelligence including battle cards,
  switching cost analysis, and win/loss patterns for sales team enablement.
  Use when asked to analyze competitors, update battle cards, or build competitive
  positioning. Also consider when win rate against a specific competitor drops.
  Suggest when sales team requests updated competitive positioning.
department: sales
agent: sales-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../icp-builder/SKILL.md
  - ../../../sales/account-executive/meeting-prep-builder/SKILL.md
  - ../../../sales/account-executive/sales-proposal-builder/SKILL.md
  - ../../../sales/vp-sales/prospect-analyst-orchestrator/SKILL.md
triggers:
  - "competitive analysis needed"
  - "update battle cards"
  - "losing to competitor X"
  - "competitive positioning"
---

# sales-competitive-intel

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook building, objection handling, GTM activation, and first sales process design.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Produces structured competitive intelligence including battle cards, switching cost analysis, and win/loss patterns for sales team enablement against specific competitors.

## When to Use

- When entering competitive deals where prospects are actively evaluating alternatives and the sales team needs structured positioning.
- When a new competitor emerges in the market or an existing competitor launches capabilities that change the competitive landscape.
- When win rate against a specific competitor drops below historical baseline and the team needs updated talk tracks and objection responses.

## Workflow

1. **Competitor Identification**: Identify the top 3-5 competitors per deal segment using CRM win/loss data, prospect mentions during discovery, and market intelligence. Rank by frequency of encounter and threat level (win rate against each). Deliverable: prioritized competitor list with encounter frequency and win/loss ratio.
2. **8-Dimension Analysis**: Analyze each competitor across 8 dimensions: product features, pricing model, market position, strengths, weaknesses, customer sentiment (review sites, case studies), recent moves (funding, launches, hires), and differentiation strategy. Source data from public filings, product documentation, customer reviews, analyst reports, and sales team field intelligence. Deliverable: per-competitor 8-dimension analysis.
3. **Battle Card Construction**: Build battle cards for each competitor with 7 sections: overview, strengths (where they win), weaknesses (where we win), trap questions (what they ask prospects about us), landmines (topics to avoid), talk tracks (what to say when prospect mentions them), and proof points (case studies and data that support our position). Write talk tracks in conversational language AEs can use verbatim. Deliverable: per-competitor battle cards using [battle-card-template.md](assets/battle-card-template.md). See [framework.md](references/framework.md) for battle card structure.
4. **Switching Cost Analysis**: Calculate switching costs for prospects moving from each competitor to your solution across 5 categories: financial (contract buyout, overlap costs), operational (process change, retraining), data (migration complexity, format compatibility), relationship (champion risk, vendor trust), and opportunity (implementation downtime, delayed value). Deliverable: per-competitor switching cost matrix.
5. **Win/Loss Pattern Analysis**: Analyze win/loss data against each competitor to identify patterns: which deal characteristics predict wins vs. losses, which objections correlate with losses, which proof points correlate with wins, and at which deal stage competitors are most dangerous. Deliverable: per-competitor win/loss pattern report with actionable insights.
6. **Intelligence Package Delivery**: Produce the complete competitive intelligence package: battle cards, switching cost matrices, and win/loss pattern analysis. Format battle cards for quick reference during live calls. Deliverable: competitive intelligence package ready for sales team distribution.

## Anti-Patterns

- **Feature-by-feature comparison without context**: Building exhaustive feature matrices that compare every capability without weighting by prospect importance. *Why*: AEs do not need to know every feature difference — they need to know which differences matter to the prospect in front of them.
- **Competitor bashing in talk tracks**: Writing talk tracks that attack competitors directly or make unsubstantiated negative claims. *Why*: negative selling erodes trust with sophisticated buyers and often backfires when the prospect has a positive relationship with the competitor.
- **Stale battle cards without refresh cadence**: Building battle cards once and distributing them without a scheduled update cycle. *Why*: competitors ship features, change pricing, and pivot positioning quarterly — a 6-month-old battle card is a liability, not an asset.
- **Ignoring competitor strengths**: Documenting only where competitors are weak and omitting where they genuinely win. *Why*: AEs who walk into meetings unaware of a competitor's real strengths get blindsided, lose credibility, and cannot prepare honest counter-positioning.

## Output

**On success**: Produces a complete competitive intelligence package containing per-competitor battle cards with talk tracks, switching cost matrices across 5 categories, and win/loss pattern analysis with actionable insights. Delivered as structured documents formatted for quick reference during live sales conversations.

**On failure**: Report what blocked intelligence gathering (e.g., insufficient win/loss data, no CRM competitor tracking, limited public information), which competitors could be analyzed and which could not, and recommended data collection actions to close intelligence gaps.

## Related Skills

- [`icp-builder`](../icp-builder/SKILL.md) — ICP definitions inform which competitive segments matter most.
- [`meeting-prep-builder`](../../../sales/account-executive/meeting-prep-builder/SKILL.md) — Uses battle cards to populate the competitive landscape section of meeting briefs.
- [`sales-proposal-builder`](../../../sales/account-executive/sales-proposal-builder/SKILL.md) — Uses competitive positioning for the differentiation section of proposals.
- [`prospect-analyst-orchestrator`](../../../sales/vp-sales/prospect-analyst-orchestrator/SKILL.md) — Provides prospect-level intelligence that contextualizes competitive dynamics.
