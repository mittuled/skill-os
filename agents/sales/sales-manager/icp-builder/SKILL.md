---
name: icp-builder
description: >
  This skill defines and scores Ideal Customer Profiles across 6 dimensions
  using a 100-point scoring rubric to focus sales team on highest-value segments.
  Use when asked to define an ICP, build a customer profile, or prioritize
  segments. Also consider when marketing and sales disagree on lead quality.
  Suggest when pipeline analysis shows low conversion in specific segments.
department: sales
agent: sales-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../../sdr/lead-qualifier/SKILL.md
  - ../sales-competitive-intel/SKILL.md
triggers:
  - "define ICP"
  - "ideal customer profile needed"
  - "segment prioritization"
  - "who should we target"
---

# icp-builder

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook building, objection handling, GTM activation, and first sales process design.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Defines and scores Ideal Customer Profiles across 6 dimensions using a weighted scoring rubric to focus the sales team on highest-value segments with the strongest win-rate correlation.

## When to Use

- When entering a new market or launching a new product and the sales team needs clarity on which segments to prioritize.
- When win rates drop below target and pipeline analysis suggests the team is pursuing low-fit accounts that consume resources without converting.
- When marketing and sales disagree on lead quality and a shared, data-driven definition of "ideal customer" is needed to align both teams.

## Workflow

1. **Closed-Won Analysis**: Analyze closed-won deals from the last 12 months (or all available if fewer) for common patterns across firmographic, technographic, and behavioral dimensions. Pull deal data from CRM including company size, industry, technology stack, deal cycle length, ACV, and expansion rate. Identify the attributes that correlate most strongly with wins, short sales cycles, high ACV, and low churn. Deliverable: closed-won pattern analysis with attribute frequency and correlation data.
2. **Dimension Definition**: Define the 6 ICP dimensions: Company Size, Industry Fit, Technology Stack, Growth Stage, Pain Intensity, and Budget Authority. For each dimension, establish the specific attributes that indicate fit within your market context. Reference [scoring-rubric.md](references/scoring-rubric.md) for dimension definitions and scoring criteria. Deliverable: 6-dimension ICP framework with attribute definitions.
3. **Dimension Weighting**: Weight each dimension based on its correlation with win rate, deal velocity, and customer lifetime value. Validate weights against closed-won analysis — the dimension most predictive of wins should carry the highest weight. Adjust weights if backtesting against historical data shows misalignment. Deliverable: weighted dimension model with correlation evidence. [GATE]
4. **Scoring Rubric Construction**: Build the scoring rubric with a 0-10 scale per criterion and composite score calculation. Define fit tiers: Tier 1 (8.0-10.0), Tier 2 (6.0-7.9), Tier 3 (4.0-5.9), Deprioritize (0-3.9). Document specific, observable signals for each score range in each dimension. Deliverable: complete scoring rubric with signal tables.
5. **Pipeline Scoring**: Score the existing pipeline against the ICP rubric. Calculate composite scores for every active opportunity. Segment the pipeline by tier and identify distribution patterns: what percentage of pipeline is Tier 1 vs. Tier 2 vs. Deprioritize. Deliverable: scored pipeline with tier distribution analysis.
6. **Gap and Segment Analysis**: Identify highest-fit segments with insufficient pipeline coverage (opportunity gaps) and lowest-fit segments consuming disproportionate sales resources (resource drains). Calculate the revenue-weighted conversion rate per tier to validate the rubric's predictive power. Deliverable: segment prioritization matrix with gap analysis.
7. **ICP Document Production**: Produce the complete ICP definition document using [icp-profile-template.md](assets/icp-profile-template.md). Include executive summary, methodology, 6-dimension analysis, scoring rubric summary, segment prioritization, pipeline fit analysis, and actionable recommendations for sales and marketing alignment. Deliverable: ICP definition document ready for leadership review.

## Anti-Patterns

- **Building ICP from assumptions instead of data**: Defining the ideal customer based on who the team wants to sell to rather than analyzing who actually buys and retains. *Why*: aspiration-based ICPs lead teams to pursue segments where they have no evidence of fit, wasting pipeline resources on low-probability deals.
- **Over-weighting company size**: Giving company size 40%+ weight because large companies have bigger budgets. *Why*: company size correlates with deal size but not necessarily with win rate or retention — a mid-market company with acute pain and fast decision-making may be a better ICP than an enterprise account with 18-month procurement cycles.
- **Static ICP without refresh cadence**: Defining the ICP once and never revisiting it as the product, market, and competitive landscape evolve. *Why*: ICPs decay as markets shift — a profile built on last year's wins may not predict next year's wins if the product has expanded into new use cases or competitors have changed positioning.
- **Ignoring negative signals**: Defining ICP only by positive attributes without documenting disqualifying signals. *Why*: knowing who not to sell to is as valuable as knowing who to sell to — without disqualification criteria, SDRs waste time on accounts that look good on paper but consistently fail to close.
- **ICP without sales-marketing alignment**: Building the ICP as a sales-only exercise without marketing input or buy-in. *Why*: if marketing does not use the same ICP to target campaigns and score leads, the two teams will continue arguing about lead quality because they are operating from different definitions.

## Output

**On success**: Produces a complete ICP definition document containing executive summary, methodology, 6-dimension analysis with scoring rubric, segment prioritization matrix, pipeline fit analysis, and recommendations for sales and marketing alignment. Includes the scored pipeline data as an appendix. Delivered as a structured document for leadership review and cross-functional alignment.

**On failure**: Report what blocked ICP construction (e.g., insufficient closed-won data, missing CRM fields, no win/loss tracking), what dimensions could be scored and which could not, and recommended data collection actions to enable a future ICP build.

## Related Skills

- [`lead-qualifier`](../../sdr/lead-qualifier/SKILL.md) — Uses the ICP scoring rubric to qualify inbound leads against the defined profile.
- [`prospect-analyst-orchestrator`](../../../sales/vp-sales/prospect-analyst-orchestrator/SKILL.md) — Orchestrates prospect research that feeds firmographic and technographic data into ICP scoring.
- [`company-researcher`](../../../sales/vp-sales/company-researcher/SKILL.md) — Provides company intelligence for firmographic and technographic dimension scoring.
- [`sales-competitive-intel`](../sales-competitive-intel/SKILL.md) — Provides competitive landscape context that influences ICP dimension weighting.
