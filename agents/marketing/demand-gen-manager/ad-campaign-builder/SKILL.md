---
name: ad-campaign-builder
description: >
  This skill builds structured paid advertising campaigns across Google, Meta,
  LinkedIn, and TikTok with platform-specific targeting, bidding, creative specs,
  and retargeting sequences. Use when asked to plan a paid campaign, build ad
  account structure, or design a multi-platform media plan. Also consider when
  budget allocation across paid channels needs optimisation. Suggest when a
  product launch lacks a paid distribution plan.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md
  - ../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
  - ../../../marketing/demand-gen-manager/channel-signal-analyst/SKILL.md
triggers:
  - "ad campaign"
  - "paid campaign"
  - "build campaign"
  - "demand gen campaign"
---

# ad-campaign-builder

## Agent: Demand Gen Manager

L2 Demand Gen Manager (1x) responsible for channel strategy, paid and organic demand generation, content distribution, and pipeline contribution from marketing programmes.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds structured paid advertising campaigns across Google, Meta, LinkedIn, and TikTok with platform-specific account architecture, targeting strategies, bidding configurations, creative specifications, and retargeting sequences, outputting a deployable campaign plan.

## When to Use

- When launching a new product or feature that requires paid distribution to reach the target audience.
- When restructuring ad accounts that have grown organically without clear campaign hierarchy.
- When expanding into a new paid channel and platform-specific best practices are needed.
- When paid CAC is rising and campaign structure or targeting needs diagnosis and rebuilding.
- When building a retargeting funnel to re-engage site visitors who did not convert.

## Workflow

1. **Objective and ICP alignment**: Define the campaign objective (awareness, consideration, conversion), confirm the ICP profile, and identify which funnel stage each platform will serve. Deliverable: campaign brief with objective, ICP, platform-to-funnel mapping.
2. **Platform selection and budget allocation**: Select platforms based on ICP channel behaviour (not marketer preference). Allocate budget using the 70/20/10 framework — 70% to proven channels, 20% to scaling channels, 10% to experiments. Reference `references/framework.md` for platform-specific benchmarks. Deliverable: budget allocation table by platform and campaign type.
3. **Account structure design**: Design the campaign hierarchy for each platform — campaigns, ad groups/ad sets, and ads — following platform-specific naming conventions and structure best practices. Deliverable: account structure diagram per platform.
4. **Targeting configuration**: Build audience targeting for each platform — keywords (Google), interests and lookalikes (Meta), job titles and company attributes (LinkedIn), interest categories and creator audiences (TikTok). Include exclusion lists to prevent wasted spend. Deliverable: targeting specification per platform with audience sizes.
5. **Bidding strategy selection**: Choose bidding strategies aligned with campaign objectives and maturity — manual CPC for new campaigns, target CPA for optimised campaigns, maximise conversions for scaled campaigns. Document bid caps and daily budgets. Deliverable: bidding configuration per campaign.
6. **Creative specifications**: Define ad format requirements, character limits, image/video dimensions, and copy guidelines for each platform. Specify how many creative variants are needed for statistical significance in testing. Deliverable: creative brief per platform with specs.
7. **[GATE] Retargeting sequence design**: Build the retargeting funnel — define audience segments by recency and behaviour (visited pricing page, started trial, abandoned cart), assign frequency caps, and sequence creative to match funnel stage. Present retargeting plan for approval before launch. Deliverable: retargeting sequence map with audience definitions, creative assignments, and frequency caps.
8. **Campaign plan generation**: Run `scripts/generate.py` to compile all specifications into a unified campaign plan using `assets/campaign-plan-template.md`. Deliverable: deployable campaign plan document.

## Anti-Patterns

- **Platform-first thinking**: Choosing Google or Meta because the team knows them, not because the ICP is there. *Why*: Budget spent on platforms where the audience is absent generates impressions but not pipeline.
- **Single ad per ad group**: Running one ad variant per ad group eliminates the ability to test and optimise creative. *Why*: Platform algorithms need 3-5 variants to find winners; single-ad groups guarantee suboptimal performance.
- **Broad match without negative keywords**: Running broad match keywords on Google without negative keyword lists. *Why*: Broad match without negatives burns budget on irrelevant queries that inflate impressions but destroy ROAS.
- **Retargeting without frequency caps**: Showing the same ad to the same person indefinitely. *Why*: Ad fatigue increases CPMs and damages brand perception; frequency caps protect both budget and brand.
- **Vanity budget allocation**: Spending most budget on awareness campaigns because they produce the best impression numbers. *Why*: Impressions do not pay for pipeline; budget must be weighted toward campaigns that generate attributable pipeline and revenue.

## Output

**On success**: Produces a campaign plan document (using `assets/campaign-plan-template.md`) containing platform-specific account structures, targeting configurations, bidding strategies, creative specifications, retargeting sequences, and budget allocation. Delivered as a file or inline document ready for implementation.

**On failure**: Report which platforms could not be planned and why (missing ICP data, unknown benchmarks, insufficient budget for platform minimums), what was attempted, and what inputs are needed to complete the plan. Every error must be actionable.

## Related Skills

- [`funnel-optimizer`](../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md) — Campaign performance data feeds funnel analysis; funnel insights inform campaign targeting adjustments.
- [`landing-page-auditor`](../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md) — Ad campaigns drive traffic to landing pages; page quality directly impacts campaign ROAS.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Ongoing campaign performance reporting informs budget reallocation and structure changes.
- [`channel-signal-analyst`](../../../marketing/demand-gen-manager/channel-signal-analyst/SKILL.md) — Channel signals inform platform selection and budget allocation decisions.
