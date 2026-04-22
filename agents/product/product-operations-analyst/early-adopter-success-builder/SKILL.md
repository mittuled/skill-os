---
name: early-adopter-success-builder
description: >
  This skill builds the programme to ensure early adopters achieve success with the product.
  Use when a product or feature is entering early access and the team needs a structured approach to early adopter support.
  Also consider when early adopter churn is high or when the team lacks a repeatable process for design partner engagement.
  Suggest when a beta launch is planned but no early adopter success criteria or support structure have been defined.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills:
  - adoption-tracker
  - cohort-selector
  - cs-onboarding-playbook
  - objection-handler-updater
  - iteration-prioritiser
  - revenue-impact-monitor
  - feedback-loop-formaliser
  - internal-comms-broadcaster
  - rollout-configurator-review
  - signal-synthesiser
  - support-ticket-triage
triggers:
  - "early adopter success"
  - "build early adopter program"
  - "early adopter enablement"
  - "early adopter plan"
  - "design partner success"
---

# early-adopter-success-builder

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Builds the programme to ensure early adopters achieve success with the product.

## When to Use
- When a product or feature is entering beta or early access and needs a structured adopter success plan
- When early adopters are churning or disengaging before reaching the product's core value moment
- When the team wants to convert early adopters into references, case studies, or expansion candidates
- When a design partner programme exists informally but lacks documented milestones and success criteria

## Workflow
1. **Define early adopter success criteria**: Identify what "success" means for early adopters — activation milestones, usage thresholds, and time-to-value benchmarks. Align these with the product's North Star metric. Deliverable: success criteria document with measurable milestones and target timelines.
2. **Design the engagement cadence**: Map the touchpoints between the product team and early adopters — onboarding calls, check-ins, feedback sessions, and escalation paths. Define who owns each touchpoint (product ops, CS, PM). Deliverable: engagement cadence calendar with owners and frequencies.
3. **Build the support structure**: Create the resources early adopters need — quick-start guides, known-issues lists, direct communication channels (Slack, email alias), and escalation procedures. Ensure early adopters know how to get help fast. Deliverable: early adopter support kit with all resources and access instructions.
4. **Establish feedback collection**: Set up structured feedback loops — in-app surveys, scheduled interviews, usage analytics dashboards. Define how feedback flows from adopters to the product team and what response SLA applies. Deliverable: feedback collection plan with channels, cadence, and routing rules.
5. **Track adopter health**: Monitor each early adopter's progress against the success criteria. Flag at-risk adopters (missed milestones, declining usage, negative feedback) for proactive intervention. Deliverable: adopter health dashboard or tracker with status per adopter.
6. **Iterate the programme**: After each cohort completes early access, run a retrospective on the programme itself. Identify what worked, what adopters struggled with, and what to change for the next cohort. Deliverable: programme retrospective summary with action items for the next iteration.

## Anti-Patterns
- **Treating early adopters like general users**: Providing the same support experience as GA customers instead of high-touch engagement. *Why*: Early adopters tolerate rough edges in exchange for access and influence — but only if they feel heard and supported. Standard support erodes that exchange.
- **Collecting feedback without acting on it**: Running surveys and interviews but never closing the loop with adopters on what changed. *Why*: Early adopters who see their feedback ignored stop providing it, and the programme loses its primary value — direct signal from real users.
- **No success criteria defined upfront**: Launching the programme without measurable milestones for what adopter success looks like. *Why*: Without criteria, the team cannot distinguish successful adopters from struggling ones, making intervention impossible and programme ROI unmeasurable.

## Output
**On success**: An early adopter success programme containing success criteria, engagement cadence, support resources, feedback collection plan, and health tracking — ready for execution with the next early access cohort.
**On failure**: Report which programme components could not be built (e.g., no analytics instrumentation for tracking, no CS capacity for touchpoints), what partial structure exists, and recommend prerequisites to resolve before the next early access launch.

## Related Skills
- [`adoption-tracker`](../adoption-tracker/SKILL.md) — sibling skill under the same agent — combine with adoption-tracker for end-to-end coverage
- [`cohort-selector`](../cohort-selector/SKILL.md) — sibling skill under the same agent — combine with cohort-selector for end-to-end coverage
- [`cs-onboarding-playbook`](../cs-onboarding-playbook/SKILL.md) — sibling skill under the same agent — combine with cs-onboarding-playbook for end-to-end coverage
- [`objection-handler-updater`](../objection-handler-updater/SKILL.md) — sibling skill under the same agent — combine with objection-handler-updater for end-to-end coverage
- [`iteration-prioritiser`](../iteration-prioritiser/SKILL.md) — sibling skill under the same agent — combine with iteration-prioritiser for end-to-end coverage
- [`revenue-impact-monitor`](../revenue-impact-monitor/SKILL.md) — sibling skill under the same agent — combine with revenue-impact-monitor for end-to-end coverage
- [`feedback-loop-formaliser`](../feedback-loop-formaliser/SKILL.md) — sibling skill under the same agent — combine with feedback-loop-formaliser for end-to-end coverage
- [`internal-comms-broadcaster`](../internal-comms-broadcaster/SKILL.md) — sibling skill under the same agent — combine with internal-comms-broadcaster for end-to-end coverage
- [`rollout-configurator-review`](../rollout-configurator-review/SKILL.md) — sibling skill under the same agent — combine with rollout-configurator-review for end-to-end coverage
- [`signal-synthesiser`](../signal-synthesiser/SKILL.md) — sibling skill under the same agent — combine with signal-synthesiser for end-to-end coverage
- [`support-ticket-triage`](../support-ticket-triage/SKILL.md) — sibling skill under the same agent — combine with support-ticket-triage for end-to-end coverage
