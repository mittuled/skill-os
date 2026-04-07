# First Sales Process Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Sales Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | first-sales-process-builder |

## Executive Summary

[2-3 sentences summarizing the sales process: number of stages, qualification framework used, expected cycle time, and the motion type it supports.
GUIDANCE: Lead with "This defines a [N]-stage sales process for [motion type] targeting [segment]." Include expected cycle time.]

## Current State Deal Flow Map

[Analysis of how deals currently flow from first touch to close.

GUIDANCE:
- Good: Visual flow showing common paths (e.g., "Inbound lead → SDR qualify → AE discovery → Demo → Proposal → Negotiation → Close"), with variance analysis showing where deals diverge, stall, or skip steps. Include sample size (N deals analyzed).
- Bad: "Deals go through several stages"
- Format: Step-by-step flow with branching paths noted, plus a variance table showing which steps are skipped and how often]

## Pipeline Stage Definitions

[5-7 stages aligned to buyer milestones.

GUIDANCE:
- Good: Table with Stage Name, Buyer Milestone, Entry Criteria, Required Activities, Exit Criteria, Expected Duration, and Probability Weight. Stages named for buyer state ("Evaluating Options") not seller action ("Sent Proposal").
- Bad: "Stage 1: Prospecting, Stage 2: Qualification..."
- Format: Detailed table with one row per stage, ordered sequentially]

## Qualification Scorecard

[Scoring framework applied at each stage gate.

GUIDANCE:
- Good: MEDDIC-based scorecard with each element (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion) scored 0-3 per stage, with minimum score to advance. Include "what good looks like" and "red flags" per element.
- Bad: "Qualify deals using MEDDIC"
- Format: Matrix with MEDDIC elements as rows and stages as columns, showing minimum score per cell. Reference: `references/framework.md`]

## Stage-Activity Matrix

[Required seller activities mapped to each stage.

GUIDANCE:
- Good: Table mapping each stage to required activities (emails, calls, meetings, demos, proposals), cadence expectations (e.g., "follow up within 24 hours of demo"), and SLAs (e.g., "proposal delivered within 3 business days of verbal agreement")
- Bad: "Reps should follow up regularly"
- Format: Table with Stage, Activity Type, Cadence, SLA, and Owner columns]

## Handoff Protocols

[Information transfer at each role transition.

GUIDANCE:
- Good: For each handoff (SDR→AE, AE→SE, AE→CS), specify: trigger event, required information fields, transfer format (CRM fields, document, meeting), SLA for handoff completion, and acceptance criteria
- Bad: "SDRs hand off to AEs"
- Format: One subsection per handoff with structured field list]

## CRM Configuration Specification

[Technical requirements for CRM implementation.

GUIDANCE:
- Good: Stage picklist values matching stage definitions, required fields per stage (with field type and validation rules), automation rules (stage advancement triggers, alert conditions), and reporting views (pipeline by stage, conversion rates, velocity)
- Bad: "Update the CRM"
- Format: Three tables -- fields, automations, and reports]

## Recommendations

[90-day rollout plan with success metrics.

GUIDANCE: Each recommendation should be:
- Specific (not "train the team" but "conduct 2-hour process walkthrough with pilot group of 3 AEs by [date]")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)
- Include: pilot group selection, training plan, feedback cadence (weekly for first month), iteration schedule, and success metrics (stage compliance rate, forecast accuracy improvement)]

## Appendices

### A. Methodology

[Deal audit scope: N closed-won and N closed-lost deals reviewed, time period, rep interviews conducted, frameworks referenced (MEDDIC/BANT).]

### B. Supporting Data

[Deal flow data, stage duration distributions, conversion rate baselines, and rep interview notes that informed the process design.]
