---
name: lead-qualifier
description: >
  Qualifies inbound and outbound leads using BANT and MEDDIC frameworks with
  quantitative scoring from publicly available signals. Use when new leads enter
  the pipeline and need qualification before SDR outreach. Also consider when
  re-qualifying stale leads or validating MQL-to-SQL handoff criteria. Suggest
  when lead volume exceeds SDR capacity and prioritization is critical.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: complex
related-skills:
  - ../../../sales/sales-development-rep/prospect-analyst-orchestrator/SKILL.md
  - ../../../sales/sales-development-rep/company-researcher/SKILL.md
  - ../../../sales/sales-development-rep/cohort-selector-sales/SKILL.md
  - ../../../sales/sales-manager/sales-playbook-builder/SKILL.md
triggers:
  - "qualify this lead"
  - "lead qualification needed"
  - "BANT scoring"
  - "MQL to SQL handoff"
  - "lead prioritization"
---

# lead-qualifier

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, lead qualification, and pipeline prioritization using structured scoring frameworks.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Qualifies inbound and outbound leads by applying BANT scoring and MEDDIC overlay using publicly available signals to produce a composite qualification score, tier assignment, and recommended next action.

## When to Use

- When new leads enter the pipeline from inbound channels (website, content downloads, event registrations) and need qualification scoring before SDR outreach begins.
- When lead volume exceeds SDR capacity and the team needs a data-driven prioritization to focus effort on the highest-conversion-probability leads.
- When re-qualifying stale pipeline leads that have been inactive for 60+ days to determine whether they warrant renewed outreach or should be archived.
- When validating MQL-to-SQL handoff criteria to ensure marketing-qualified leads meet the threshold for sales acceptance and outbound follow-up.
- When the prospect-analyst-orchestrator dispatches this skill as part of a batch qualification workflow across a prospect list.

## Workflow

1. **Gather Lead Signals**: Collect all available signals for the lead from CRM records, website activity (page visits, pricing page views, feature page depth), email engagement (opens, clicks, content downloads), event attendance, and any company-researcher profile if available. Normalize signal data into a structured format with timestamps and source attribution. Deliverable: lead signal inventory with source, recency, and completeness assessment.

2. **Apply BANT Scoring**: Score each BANT dimension on a 0-10 scale using the signal-to-score mapping in `references/scoring-rubric.md`. Budget: infer from funding stage, company size, and stated budget signals. Authority: infer from contact's title, seniority, and organizational role. Need: infer from job postings, tech stack gaps, content consumption patterns, and stated pain points. Timeline: infer from contract renewal dates, fiscal year alignment, and urgency signals. Deliverable: BANT scorecard with per-dimension score, evidence citations, and confidence level.

3. **Apply MEDDIC Overlay**: For leads scoring 6.0+ on BANT composite, apply the MEDDIC framework using `references/meddic-overlay.md` to assess deal complexity and close probability. Evaluate Metrics (quantified business impact), Economic Buyer (identified and accessible), Decision Criteria (known evaluation factors), Decision Process (mapped approval workflow), Identify Pain (confirmed and quantified pain point), Champion (internal advocate identified). Deliverable: MEDDIC assessment with per-element status (Confirmed/Partial/Unknown) and supporting evidence.

4. **Map Public Signals to BANT Scores**: Cross-reference publicly available signals against the signal table in the scoring rubric. For each signal, assign the corresponding BANT dimension score adjustment. Examples: "Company raised Series B in last 6 months" maps to Budget 8-9; "Job posting for role our product serves" maps to Need 7-8; "C-level engaged with content" maps to Authority 8-9; "RFP issued in category" maps to Timeline 9-10. Resolve conflicting signals by weighting recency and source reliability. Deliverable: signal-to-score mapping log with conflict resolution notes.

5. **Calculate Composite Qualification Score**: Compute the weighted composite score using the rubric weights — Budget 25%, Authority 25%, Need 30%, Timeline 20%. Apply the MEDDIC modifier: if MEDDIC assessment has 4+ elements Confirmed, multiply composite by 1.1 (cap at 10.0); if 2+ elements are Unknown, multiply by 0.9. Deliverable: final composite qualification score (0.0-10.0) with calculation breakdown.

6. **Assign Lead Tier**: Map the composite score to a tier using the grade bands in the scoring rubric. Hot (8.0-10.0): high-priority, immediate outreach. Warm (6.0-7.9): scheduled outreach with additional research. Cold (3.0-5.9): nurture sequence, re-evaluate on trigger event. Disqualified (0.0-2.9): archive with disqualification reason. Deliverable: tier assignment with justification narrative.

7. **Generate Recommended Next Action**: Produce a specific, actionable next step for each tier. Hot: identify the optimal contact, channel, and message angle for outreach within 24 hours. Warm: specify which data gaps to fill and which trigger events to monitor before outreach. Cold: assign to automated nurture sequence with re-qualification trigger conditions. Disqualified: document reason and set re-evaluation date if applicable. Deliverable: per-lead action recommendation with owner, deadline, and success criteria.

8. **[GATE] Produce Qualification Report**: Assemble the complete qualification report using `assets/qualification-report-template.md`. Include lead summary, BANT scorecard with evidence, MEDDIC assessment, composite score calculation, tier assignment, recommended action, and full evidence log. Submit for review before CRM update and SDR assignment. Deliverable: completed qualification report ready for CRM entry and SDR distribution.

## Anti-Patterns

- **Gut-feel qualification**: Scoring leads based on company name recognition or SDR intuition rather than structured signal analysis. *Why*: subjective qualification introduces systematic bias toward well-known brands and against high-potential emerging companies, resulting in missed opportunities and inflated pipeline with poor-fit logos.
- **Binary qualification**: Treating qualification as a yes/no decision rather than a scored spectrum. *Why*: binary classification loses the nuance between a lead scoring 8.5 and one scoring 6.2 — both might be "qualified" but require fundamentally different outreach strategies and resource allocation.
- **Stale signal reliance**: Using CRM data from the original lead creation without checking for updated signals. *Why*: a lead that downloaded a whitepaper 8 months ago and showed no subsequent engagement is not the same lead as one who visited the pricing page yesterday; treating them equally wastes SDR time on dead leads.
- **MEDDIC on every lead**: Applying the full MEDDIC overlay to leads that scored below 6.0 on BANT. *Why*: MEDDIC adds value for complex, high-potential deals but is overhead for leads that already fail basic qualification — the time spent on MEDDIC for weak leads should be redirected to deeper research on strong ones.
- **Qualification without action**: Producing scores and tiers but not generating specific next-step recommendations. *Why*: a score without an action is analytics, not enablement — SDRs need to know exactly who to contact, through which channel, with what message, by when.

## Output

**On success**: Produces a qualification report containing a BANT scorecard with per-dimension scores and evidence, MEDDIC assessment (for qualifying leads), composite qualification score with calculation breakdown, tier assignment (Hot/Warm/Cold/Disqualified), and a specific recommended next action with owner and deadline. Delivered as a structured markdown document following the qualification-report-template, ready for CRM entry and SDR assignment.

**On failure**: Report which qualification step could not be completed (e.g., "Authority scoring failed — contact title unknown and org chart unavailable"), which signals were missing or conflicting, the partial score achieved with confidence caveats, and recommended remediation — such as requesting the company-researcher skill to fill data gaps before re-attempting qualification.

## Related Skills

- [`prospect-analyst-orchestrator`](../../../sales/sales-development-rep/prospect-analyst-orchestrator/SKILL.md) — Dispatches this skill in batch for multi-prospect qualification; consumes the qualification score as input to composite prospect ranking.
- [`company-researcher`](../../../sales/sales-development-rep/company-researcher/SKILL.md) — Provides the firmographic profile and buying triggers that serve as input signals for BANT and MEDDIC scoring.
- [`cohort-selector-sales`](../../../sales/sales-development-rep/cohort-selector-sales/SKILL.md) — Upstream skill that defines the prospect cohort from which leads are drawn for qualification.
- [`sales-playbook-builder`](../../../sales/sales-manager/sales-playbook-builder/SKILL.md) — Consumes qualification tiers and recommended actions to build tier-specific outreach playbooks.
