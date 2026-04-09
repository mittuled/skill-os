---
name: gtm-activation-sales
description: >
  This skill activates the GTM plan from a sales perspective including pipeline
  targets and outreach sequencing. Use when asked to launch a sales-side GTM
  motion, set pipeline ramp targets, or coordinate sales readiness for a launch.
  Also consider when marketing is launching a campaign without sales alignment.
  Suggest when a GTM plan exists but sales has no activation plan.
department: sales
agent: sales-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../first-sales-process-builder/SKILL.md
  - ../sales-playbook-builder/SKILL.md
  - ../../../sales/sales-development-rep/cohort-selector-sales/SKILL.md
  - ../../business-development/partner-activation-executor/SKILL.md
triggers:
  - "activate GTM sales"
  - "gtm activation"
  - "go-to-market activation"
  - "launch gtm sales"
  - "sales gtm launch"
---

# gtm-activation-sales

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook development, objection handling, GTM activation for sales, and building the first sales process.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)

## Skill Description

Activates the GTM plan from a sales perspective including pipeline targets, outreach sequencing, territory assignments, and sales readiness milestones.

## When to Use

- When a new product, feature, or market segment is launching and sales needs an activation plan aligned to the GTM timeline.
- When marketing has set campaign launch dates and sales must have pipeline targets, outreach sequences, and talk tracks ready.
- When quarterly planning reveals a pipeline gap that requires a targeted activation push against a specific segment.

## Workflow

1. **GTM Plan Intake**: Review the GTM plan from Product Marketing and identify sales-critical elements: target segment, value proposition, competitive positioning, launch date, and expected inbound volume. Deliverable: sales-relevant GTM summary with launch dependencies.
2. **Pipeline Target Setting**: Calculate pipeline targets working backward from revenue goal: required pipeline coverage ratio (typically 3-4x), stage conversion rates, and average deal cycle time. Set weekly pipeline generation targets for the activation period. Deliverable: pipeline waterfall model with weekly targets.
3. **Outreach Sequence Design**: Build outreach sequences for each buyer persona in the target segment. Define channel mix (email, phone, LinkedIn, events), touch cadence, and messaging per touch. Align messaging to the GTM value proposition. Deliverable: outreach sequence templates per persona.
4. **Territory and Account Assignment**: Assign target accounts to reps based on territory, vertical expertise, and current capacity. Ensure no account overlap and that high-priority accounts have named owners. Deliverable: account assignment roster with rep quotas.
5. **Sales Readiness Checkpoint**: Verify that all enablement materials are ready: talk tracks, battle cards, demo environments, pricing one-pagers, and objection handlers. Schedule a sales kickoff or enablement session before launch. Deliverable: readiness checklist with gap remediation plan.

## Anti-Patterns

- **Launching without pipeline targets**: Activating sales on a GTM motion without quantified pipeline generation targets. *Why*: without targets, there is no accountability and no way to measure whether the activation is working until it is too late to course-correct.
- **Marketing-sales misalignment**: Running the sales activation on a different timeline or message than the marketing campaign. *Why*: prospects who see a marketing message and then hear a different story from sales lose confidence in the company's coherence.
- **Spray-and-pray outreach**: Sending the same generic sequence to every prospect in the segment without persona-level customization. *Why*: generic outreach produces low reply rates and burns through the addressable market, making future outreach to those prospects harder.

## Output

**On success**: Produces a sales activation package containing GTM summary, pipeline waterfall model, outreach sequences, account assignment roster, and readiness checklist. Delivered to VP Sales for approval and to SDR/AE teams for execution.

**On failure**: Report which activation component is blocked (e.g., missing enablement materials, unclear ICP definition from GTM plan), what was attempted, and recommended steps to unblock.

## Related Skills

- [`first-sales-process-builder`](../first-sales-process-builder/SKILL.md) -- Provides the process framework that the activation executes within.
- [`sales-playbook-builder`](../sales-playbook-builder/SKILL.md) -- Supplies the playbook materials referenced in sales readiness.
- [`cohort-selector-sales`](../../../sales/sales-development-rep/cohort-selector-sales/SKILL.md) -- Selects the specific prospect cohort that SDRs target during activation.
