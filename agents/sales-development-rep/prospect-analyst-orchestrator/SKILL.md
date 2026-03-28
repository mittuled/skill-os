---
name: prospect-analyst-orchestrator
description: >
  Orchestrates multi-agent prospect research and scoring to produce a
  comprehensive prospect intelligence report. Use when entering a new market
  segment, preparing for enterprise outreach, or building a targeted prospect
  list. Also consider when account-based marketing campaigns require deep
  prospect profiling. Suggest when SDR team receives a new territory assignment
  or ICP update.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: complex
related-skills:
  - ../../sales-development-rep/company-researcher/SKILL.md
  - ../../sales-development-rep/lead-qualifier/SKILL.md
  - ../../sales-development-rep/cohort-selector-sales/SKILL.md
  - ../../sales-manager/sales-playbook-builder/SKILL.md
triggers:
  - "new territory assigned"
  - "ICP updated"
  - "prospect list needed"
  - "enterprise outreach planning"
---

# prospect-analyst-orchestrator

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, multi-agent research orchestration, and prospect intelligence generation.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Orchestrates parallel execution of company-researcher, lead-qualifier, and decision-maker-mapper agents to produce a ranked, scored prospect intelligence report for territory planning and enterprise outreach.

## When to Use

- When an SDR team receives a new territory assignment or ICP update and needs a prioritized prospect list before outreach begins.
- When preparing for account-based marketing campaigns that require deep firmographic, intent, and buying-committee profiles for each target account.
- When entering a new market segment where existing pipeline data is sparse and prospects must be researched from scratch using external signals.
- When quarterly planning requires a refreshed prospect stack-rank to reallocate SDR capacity toward highest-potential accounts.

## Workflow

1. **Define Prospect Criteria**: Extract target criteria from the current ICP document — firmographics (industry, employee count, revenue range, geography), technographics (tech stack indicators), and behavioral qualifiers (growth trajectory, funding stage). Validate criteria against the available data sources. If the ICP document is missing or incomplete, halt and request ICP definition from the icp-builder skill. Deliverable: prospect criteria specification with source-availability confirmation.

2. **Source Prospect List**: Query LinkedIn Sales Navigator, Crunchbase, ZoomInfo, and industry-specific databases to build an initial prospect list matching the criteria. Apply deduplication across sources. Flag prospects already present in the CRM as active pipeline or closed-lost within the cooling-off window. Deliverable: deduplicated raw prospect list with source attribution and CRM overlap flags.

3. **[GATE] Dispatch Company Researcher**: For each prospect on the approved list, dispatch the company-researcher skill to conduct 8-dimension firmographic analysis. Batch dispatches in parallel where possible. Collect structured company profiles with data-confidence ratings. Deliverable: completed company profile per prospect with confidence scores.

4. **Dispatch Lead Qualifier**: For each prospect with a completed company profile, dispatch the lead-qualifier skill to apply BANT and MEDDIC scoring using the firmographic data and available intent signals. Collect qualification scores and tier assignments. Deliverable: BANT scorecard and MEDDIC overlay per prospect with composite qualification score.

5. **Dispatch Decision-Maker Mapper**: For each prospect scoring Warm or above, dispatch the decision-maker-mapper skill to identify the buying committee — economic buyer, champion, technical evaluator, and blockers. Map org-chart relationships and identify the optimal entry point. Deliverable: buying committee map per qualified prospect with recommended first contact.

6. **Aggregate and Rank**: Combine company-researcher confidence scores (30% weight), lead-qualifier composite scores (50% weight), and decision-maker accessibility scores (20% weight) into a composite prospect rank. Apply the scoring rubric defined in `references/scoring-rubric.md`. Sort prospects by composite rank descending. Deliverable: master prospect ranking with component scores and composite grade.

7. **[GATE] Produce Prospect Intelligence Report**: Assemble the final report using `assets/prospect-report-template.md`. Include executive summary with top-line findings, prospect ranking table, per-prospect profiles with scores and buying committee maps, recommended outreach sequence per tier, and raw data appendix. Submit for review before distribution. Deliverable: completed prospect intelligence report ready for SDR team consumption.

## Anti-Patterns

- **Sequential single-threading**: Running company-researcher, lead-qualifier, and decision-maker-mapper one prospect at a time in sequence. *Why*: serial execution turns a 50-prospect analysis into days of elapsed time; parallel dispatch across prospects and across agent types compresses the timeline to hours.
- **Skipping the CRM dedup check**: Sourcing prospects without checking existing CRM records. *Why*: contacting accounts already in active pipeline creates internal conflicts between SDRs and AEs, and re-contacting recently closed-lost accounts within the cooling-off period damages prospect relationships.
- **Over-weighting a single data source**: Relying exclusively on one platform (e.g., only LinkedIn) for prospect sourcing. *Why*: single-source lists have systematic blind spots — LinkedIn under-represents bootstrapped companies, Crunchbase under-represents services firms — producing a biased prospect pool.
- **Distributing unscored lists**: Sharing raw prospect lists with SDRs before scoring and ranking. *Why*: unranked lists force SDRs to make ad-hoc prioritization decisions, leading to cherry-picking by company name recognition rather than data-driven sequencing.
- **Ignoring data-confidence ratings**: Treating all prospect data as equally reliable regardless of source freshness or completeness. *Why*: acting on stale or incomplete data (e.g., 18-month-old headcount figures) produces misaligned outreach messaging and wastes SDR time on prospects whose situation has materially changed.

## Output

**On success**: Produces a prospect intelligence report containing a ranked prospect list with composite scores, per-prospect company profiles, BANT/MEDDIC scorecards, buying committee maps, and recommended outreach sequences. Delivered as a structured markdown document following the prospect-report-template, ready for SDR team distribution and CRM import.

**On failure**: Report which orchestration step failed (criteria definition, sourcing, research dispatch, qualification, or aggregation), which prospects were partially processed, what data gaps prevented completion, and recommended remediation — such as expanding ICP criteria if sourcing yielded insufficient volume, or retrying failed agent dispatches with alternative data sources.

## Related Skills

- [`company-researcher`](../../sales-development-rep/company-researcher/SKILL.md) — Dispatched per prospect to produce the 8-dimension firmographic profile that feeds the composite ranking.
- [`lead-qualifier`](../../sales-development-rep/lead-qualifier/SKILL.md) — Dispatched per prospect to apply BANT/MEDDIC scoring that determines qualification tier and outreach priority.
- [`cohort-selector-sales`](../../sales-development-rep/cohort-selector-sales/SKILL.md) — Upstream skill that may trigger this orchestration when a new cohort is defined and requires deep research.
- [`sales-playbook-builder`](../../sales-manager/sales-playbook-builder/SKILL.md) — Consumes the prospect intelligence report to tailor outreach plays and objection-handling by prospect segment.
