---
name: company-researcher
description: >
  Conducts deep 8-dimension firmographic research on a target company to produce
  a structured company profile for sales intelligence. Use when an SDR needs
  background on a prospect company before outreach. Also consider when preparing
  for enterprise sales meetings or evaluating partnership targets. Suggest when a
  new lead enters the pipeline with limited CRM data.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: medium
related-skills:
  - ../../../sales/sales-development-rep/prospect-analyst-orchestrator/SKILL.md
  - ../../../sales/sales-development-rep/lead-qualifier/SKILL.md
  - ../../../sales/sales-manager/sales-playbook-builder/SKILL.md
triggers:
  - "research target company"
  - "company background needed"
  - "prospect company profile"
  - "firmographic analysis"
---

# company-researcher

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, company research, and structured intelligence gathering for sales pipeline development.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Conducts structured 8-dimension firmographic research on a target company using multiple data sources and produces a scored company profile with buying triggers and data-confidence ratings.

## When to Use

- When an SDR needs comprehensive background on a prospect company before crafting personalized outreach messaging.
- When preparing for an enterprise sales meeting where deep company knowledge is required to establish credibility and tailor the value proposition.
- When a new lead enters the pipeline with minimal CRM data and the account record needs enrichment before qualification can proceed.
- When the prospect-analyst-orchestrator dispatches this skill as part of a batch prospect research workflow.

## Workflow

1. **Identify Company Across Sources**: Locate the target company across primary data sources — company website, LinkedIn company page, Crunchbase profile, SEC filings (if public), and Glassdoor. Confirm entity identity by cross-referencing domain, legal name, and headquarters. Flag subsidiaries or parent companies if the target is part of a corporate structure. Deliverable: verified company identity with source URLs and entity relationship notes.

2. **Map 8 Firmographic Dimensions**: Research each dimension systematically using the framework in `references/framework.md`: (1) Company size — headcount, headcount trend, office locations; (2) Industry — primary vertical, sub-vertical, NAICS/SIC codes; (3) Funding — total raised, last round, investors, runway indicators; (4) Tech stack — engineering job postings, BuiltWith/Wappalyzer signals, integration partnerships; (5) Growth trajectory — hiring velocity, revenue estimates, market expansion signals; (6) Competitive landscape — direct competitors, market position, differentiation; (7) Leadership team — CEO, CTO, VP-level decision-makers, tenure, background; (8) Recent news — press releases, product launches, partnerships, M&A activity in last 12 months. Deliverable: structured data per dimension with source attribution.

3. **Score Data Freshness and Reliability**: Rate each dimension on a 3-tier confidence scale: High (verified from primary source within 90 days), Medium (secondary source or 91-180 days old), Low (single unverified source or older than 180 days). Calculate overall data-confidence percentage as the weighted average across dimensions. Deliverable: per-dimension confidence ratings and overall data-confidence score.

4. **Identify Buying Triggers**: Scan across all dimensions for events that indicate active or imminent buying behavior — recent funding round, leadership change in a relevant department, geographic expansion, technology migration, competitive pressure, or regulatory change. Classify each trigger by urgency (Immediate, Near-term, Long-term) using the buying trigger taxonomy in `references/framework.md`. Deliverable: prioritized buying trigger list with urgency classification and supporting evidence.

5. **Flag Data Gaps**: Document dimensions where data is incomplete, conflicting, or absent. For each gap, note what information is missing, why it matters for outreach, and how it could be obtained (e.g., "Revenue unknown — request from finance databases or infer from employee count ratio"). Deliverable: data gap inventory with impact assessment and remediation paths.

6. **Produce Company Profile**: Assemble findings into the structured profile template at `assets/company-profile-template.md`. Lead with the executive summary highlighting the 2-3 most sales-relevant findings. Include all 8 dimensions, buying triggers, confidence ratings, and data gaps. Deliverable: completed company profile document.

## Anti-Patterns

- **Surface-level research**: Copying the company's LinkedIn "About" section and calling it a profile. *Why*: generic company descriptions provide zero outreach differentiation; SDRs need specific, actionable intelligence like tech stack details and buying triggers to craft messages that earn replies.
- **Single-source reliance**: Pulling all data from one platform without cross-referencing. *Why*: every data source has systematic biases and staleness — Crunchbase funding data lags by months, LinkedIn headcounts can be inflated by alumni, and website claims may be aspirational rather than factual.
- **Ignoring data freshness**: Treating 2-year-old funding data or headcount figures as current. *Why*: companies change rapidly — a startup that raised Series A 18 months ago may have pivoted, been acquired, or run out of runway, making stale data actively misleading for outreach planning.
- **Skipping the competitive landscape**: Omitting competitor analysis from the profile. *Why*: knowing which competitors the prospect uses or has evaluated is critical for positioning; without it, SDRs risk leading with a value prop the prospect has already rejected from a competitor.

## Output

**On success**: Produces a structured company profile document containing verified data across 8 firmographic dimensions, prioritized buying triggers with urgency ratings, per-dimension confidence scores, data gap inventory, and a recommended outreach approach. Delivered as a markdown document following the company-profile-template.

**On failure**: Report which dimensions could not be researched (e.g., "Funding data unavailable — company is private and pre-revenue with no Crunchbase profile"), what sources were attempted, the overall data-confidence score achieved, and recommended alternative approaches — such as requesting information from the prospect directly during discovery or using intent data platforms for indirect signals.

## Related Skills

- [`prospect-analyst-orchestrator`](../../../sales/sales-development-rep/prospect-analyst-orchestrator/SKILL.md) — Dispatches this skill in batch for multi-prospect research; consumes the company profile as input to composite scoring.
- [`lead-qualifier`](../../../sales/sales-development-rep/lead-qualifier/SKILL.md) — Uses the company profile and buying triggers as input signals for BANT and MEDDIC qualification scoring.
- [`sales-playbook-builder`](../../../sales/sales-manager/sales-playbook-builder/SKILL.md) — Consumes company profiles to tailor outreach messaging and objection-handling by prospect segment.
