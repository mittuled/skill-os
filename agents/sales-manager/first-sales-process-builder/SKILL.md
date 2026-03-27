---
name: first-sales-process-builder
description: >
  This skill designs and documents the first repeatable sales process from
  prospecting through close. Use when asked to build an initial sales process,
  define pipeline stages, or create the first sales methodology. Also consider
  when the team is closing deals ad hoc with no documented process.
  Suggest when reps are using inconsistent approaches across deals.
department: sales
agent: sales-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../sales-playbook-builder/SKILL.md
  - ../gtm-activation-sales/SKILL.md
  - ../../vp-sales/opportunity-framer-sales/SKILL.md
---

# first-sales-process-builder

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook development, objection handling, GTM activation for sales, and building the first sales process.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Designs and documents the first repeatable sales process from prospecting through close, establishing pipeline stages, qualification gates, and handoff protocols that the team executes consistently.

## When to Use

- When the company is pre-revenue or early-revenue and no formal sales process exists.
- When deals are closing through ad hoc heroics rather than a repeatable motion and leadership needs to scale the team.
- When a new product line or market segment requires a distinct sales process separate from the existing one.

## Workflow

1. **Current State Audit**: Interview existing reps and review the last 10 closed-won and 5 closed-lost deals. Map the actual steps each deal followed from first touch to signature. Identify common patterns and divergences. Deliverable: current state deal flow map with variance analysis.
2. **Stage Definition**: Define 5-7 pipeline stages aligned to buyer milestones (not seller activities). Each stage must have a clear entry criterion, required activities, and exit criterion. Use MEDDIC or BANT as the qualification backbone. Deliverable: pipeline stage definitions with entry/exit criteria.
3. **Qualification Framework**: Build the qualification scorecard applied at each stage gate. Define minimum thresholds for advancement: identified pain, quantified impact, access to economic buyer, defined decision process, and confirmed timeline. Deliverable: qualification scorecard template.
4. **Activity Mapping**: Map required seller activities to each stage: emails, calls, meetings, demos, proposals, references. Define cadence expectations and SLA for follow-up. Deliverable: stage-activity matrix with cadence guidelines.
5. **Handoff Protocols**: Define handoffs between SDR-to-AE, AE-to-SE, and AE-to-CS. Specify what information transfers at each handoff, the format, and the SLA. Deliverable: handoff protocol documents for each transition.
6. **CRM Configuration Spec**: Translate the process into CRM requirements: stage picklist values, required fields per stage, automation rules for stage advancement, and reporting views. Deliverable: CRM configuration specification.
7. **Rollout Plan**: Define the training plan, pilot group, feedback cadence, and iteration schedule for the first 90 days. Deliverable: 90-day rollout plan with success metrics.

## Anti-Patterns

- **Seller-centric stages**: Defining pipeline stages around what the seller does ("sent proposal") rather than where the buyer is ("evaluating options"). *Why*: seller-centric stages create false pipeline confidence because a sent proposal says nothing about buyer intent or readiness to decide.
- **Too many stages**: Creating 10+ pipeline stages that add administrative burden without decision value. *Why*: over-granular stages reduce CRM compliance because reps skip updates, and the extra stages don't correlate with meaningful buyer state changes.
- **No exit criteria**: Defining stages without clear criteria for what must be true before a deal advances. *Why*: without exit criteria, deals accumulate in mid-pipeline stages, forecasts become unreliable, and pipeline reviews devolve into storytelling.
- **Copying a process from a different motion**: Importing an enterprise sales process for a PLG motion or vice versa. *Why*: motion-process mismatch creates friction; an enterprise process applied to a velocity deal adds steps that kill conversion rate.

## Output

**On success**: Produces a complete first sales process package containing deal flow map, pipeline stage definitions, qualification scorecard, stage-activity matrix, handoff protocols, CRM configuration spec, and 90-day rollout plan. Delivered to VP Sales for approval and to RevOps for CRM implementation.

**On failure**: Report which process component could not be defined (e.g., insufficient deal history for pattern analysis, unclear buyer journey), what was attempted, and recommended steps to gather the missing inputs.

## Related Skills

- [`sales-playbook-builder`](../sales-playbook-builder/SKILL.md) -- Builds the playbook content that reps use to execute within this process.
- [`gtm-activation-sales`](../gtm-activation-sales/SKILL.md) -- Activates the process as part of a broader GTM launch with pipeline targets.
- [`opportunity-framer-sales`](../../vp-sales/opportunity-framer-sales/SKILL.md) -- Provides the opportunity frame and motion blueprint this process operationalizes.
