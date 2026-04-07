---
name: cold-outreach-builder
description: >
  This skill builds personalized multi-touch cold outreach sequences with A/B
  variant emails optimized for target persona and buying stage. Use when launching
  outbound campaigns to new prospects. Also consider when existing sequences
  underperform (<2% reply rate). Suggest when SDR team onboards new territory
  or ICP segment.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: complex
related-skills:
  - ../cohort-selector-sales/SKILL.md
  - ../decision-maker-mapper/SKILL.md
  - ../follow-up-sequence-builder/SKILL.md
  - ../../../sales/sales-manager/sales-playbook-builder/SKILL.md
  - ../../../sales/account-executive/sales-signal-collector/SKILL.md
triggers:
  - "build outreach sequence"
  - "cold email campaign"
  - "outbound campaign needed"
  - "new territory outreach"
---

# cold-outreach-builder

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, cold outreach execution, and top-of-funnel pipeline generation.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds personalized multi-touch cold outreach sequences with A/B variant emails, cadence timing, and channel mix optimized for the target persona and buying stage.

## When to Use

- When launching a new outbound campaign to prospects who have no prior relationship with the company and a structured sequence is needed.
- When existing outreach sequences are underperforming (reply rate below 2% or meeting-set rate below 0.5%) and need to be rebuilt with fresh messaging and structure.
- When the SDR team is entering a new territory, vertical, or ICP segment and requires persona-specific outreach sequences from scratch.

## Workflow

1. **Prospect Profile Analysis**: Analyze the target prospect's profile, ICP fit score, industry, role, seniority, and known pain points. Review any available intent signals or engagement history. Identify the prospect's likely buying stage: unaware, problem-aware, solution-aware, or vendor-aware. Deliverable: prospect persona brief with buying stage classification.

2. **Framework Selection**: Select the outreach framework based on buying stage. Use AIDA (Attention, Interest, Desire, Action) for unaware and problem-aware prospects. Use PAS (Problem, Agitate, Solve) for prospects who acknowledge the pain but have not explored solutions. Use BAB (Before, After, Bridge) for solution-aware prospects who need to see the transformation. Reference [framework.md](references/framework.md) for detailed framework structures. Deliverable: selected framework with rationale.

3. **Sequence Construction**: Build a 5-email sequence with escalating value and urgency across the selected framework. Each email must have a single, clear CTA. Structure the arc: Email 1 (hook + relevance), Email 2 (social proof + problem validation), Email 3 (value proposition + differentiation), Email 4 (case study + objection preemption), Email 5 (breakup + final value offer). Deliverable: 5-email sequence draft with subject lines and body copy.

4. **A/B Variant Creation**: Create A/B variants for subject lines and opening hooks on Emails 1 and 3 (highest-leverage touchpoints). Variant A uses the primary approach; Variant B tests an alternative angle (e.g., question vs. statement, pain vs. aspiration, specific vs. broad). Deliverable: A/B variant pairs for subject lines and opening hooks.

5. **Cadence and Channel Definition**: Define the send cadence: Day 1 (Email 1), Day 3 (LinkedIn connection request), Day 5 (Email 2), Day 8 (LinkedIn message), Day 11 (Email 3), Day 15 (Phone call), Day 19 (Email 4), Day 24 (Email 5 breakup). Adjust intervals based on persona seniority — C-suite gets wider spacing (2x intervals), ICs get standard spacing. Reference [framework.md](references/framework.md) for cadence science. Deliverable: cadence calendar with channel assignments.

6. **Personalization Token Mapping**: Define personalization tokens for each email: company name, prospect first name, industry-specific pain point, recent trigger event (funding, hiring, product launch), mutual connection, and competitor reference. Map each token to a data source (CRM field, LinkedIn, news, intent data). Flag any token that requires manual research. Deliverable: personalization matrix mapping tokens to data sources per email.

7. **[GATE] Sequence Compilation**: Compile the complete outreach sequence using [outreach-sequence-template.md](assets/outreach-sequence-template.md). Include all emails with A/B variants, LinkedIn touchpoint scripts, phone call scripts, cadence calendar, and personalization guide. Review with SDR manager before deployment. Deliverable: completed outreach sequence document ready for sales engagement platform upload.

## Anti-Patterns

- **Feature-dump emails**: Leading with product features instead of prospect pain points. *Why*: cold prospects have no context for why features matter — feature lists get ignored, while pain-based messaging earns attention because it mirrors the prospect's internal dialogue.

- **Identical A/B variants**: Creating variants that differ by only a word or two. *Why*: statistically meaningless A/B tests waste the learning opportunity — variants must test genuinely different hypotheses (e.g., pain vs. aspiration framing) to produce actionable data.

- **Over-personalization that feels invasive**: Referencing personal details (children, hobbies, health) found on social media. *Why*: crosses the line from relevance to surveillance — prospects disengage when outreach feels creepy rather than informed. Stick to professional context: role, company, industry, and recent business events.

- **Same message, every persona**: Using one sequence for all ICP segments without adapting framework, language, or pain points. *Why*: a CFO cares about cost reduction and risk; a VP Engineering cares about developer velocity and reliability. Generic messaging signals laziness and gets deleted.

- **Ignoring reply-rate signals**: Running a sequence to completion even when Emails 1-2 show zero engagement across the cohort. *Why*: a 0% open rate on Email 1 means the subject line is broken — continuing to send damages domain reputation and wastes prospect attention.

- **Breakup email that burns the bridge**: Writing a hostile or guilt-tripping final email. *Why*: the breakup email often gets the highest reply rate because it removes pressure — poisoning it with passive aggression destroys the one moment the prospect was most likely to respond.

## Output

**On success**: Produces a complete multi-touch outreach sequence document following [outreach-sequence-template.md](assets/outreach-sequence-template.md) containing prospect persona brief, framework rationale, 5 emails with A/B variants, LinkedIn and phone scripts, cadence calendar, personalization matrix, and performance tracking metrics. Delivered to the SDR team for upload to the sales engagement platform.

**On failure**: Report what prevented sequence creation (e.g., insufficient prospect data for personalization, unclear ICP segment, no available framework fit), what was partially completed, and recommended next steps such as running a prospect research workflow first or requesting ICP clarification from the sales manager.

## Related Skills

- [`cohort-selector-sales`](../cohort-selector-sales/SKILL.md) — Provides the target prospect list that this outreach sequence will be deployed against.
- [`decision-maker-mapper`](../decision-maker-mapper/SKILL.md) — Supplies stakeholder intelligence that informs personalization and multi-threading within the sequence.
- [`follow-up-sequence-builder`](../follow-up-sequence-builder/SKILL.md) — Takes over when a prospect engages with the cold sequence but does not convert, designing contextual follow-up.
- [`sales-playbook-builder`](../../../sales/sales-manager/sales-playbook-builder/SKILL.md) — Defines the messaging framework and objection-handling guidelines that outreach sequences must align with.
- [`sales-signal-collector`](../../../sales/account-executive/sales-signal-collector/SKILL.md) — Provides engagement signals and trigger events used for personalization tokens.
