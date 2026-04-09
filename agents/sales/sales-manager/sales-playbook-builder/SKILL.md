---
name: sales-playbook-builder
description: >
  This skill builds the sales playbook including qualification criteria, discovery
  questions, and closing techniques. Use when asked to create or overhaul the
  sales playbook, document the sales methodology, or equip reps with deal
  execution materials. Also consider when onboarding new reps with no playbook.
  Suggest when reps lack standardized materials for running deals.
department: sales
agent: sales-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../first-sales-process-builder/SKILL.md
  - ../objection-handler-updater-sales/SKILL.md
  - ../gtm-activation-sales/SKILL.md
  - ../../../sales/vp-sales/opportunity-framer-sales/SKILL.md
  - ../../../sales/solutions-engineering-manager/solutions-playbook-builder/SKILL.md
  - ../../sales-development-rep/cold-outreach-builder/SKILL.md
  - ../../sales-development-rep/lead-qualifier/SKILL.md
  - ../../sales-development-rep/company-researcher/SKILL.md
  - ../../sales-development-rep/prospect-analyst-orchestrator/SKILL.md
  - ../../sales-development-rep/decision-maker-mapper/SKILL.md
triggers:
  - "build sales playbook"
  - "create sales playbook"
  - "sales playbook"
  - "write sales playbook"
  - "compile sales playbook"
---

# sales-playbook-builder

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook development, objection handling, GTM activation for sales, and building the first sales process.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)

## Skill Description

Builds the sales playbook including qualification criteria, discovery questions, competitive battle cards, and closing techniques that equip reps to execute deals consistently.

## When to Use

- When the sales team has no documented playbook and reps rely on tribal knowledge.
- When onboarding new reps and there are no standardized materials for ramping.
- When the sales process, ICP, or competitive landscape has changed enough that the existing playbook is outdated.

## Workflow

1. **Input Gathering**: Collect inputs from the opportunity frame (VP Sales), product positioning (PMM), competitive intelligence, and top-rep interviews. Identify the ICP, buyer personas, and the sales motion type. Deliverable: playbook input brief with source inventory.
2. **Qualification Criteria**: Define the MEDDIC (or BANT) qualification criteria tailored to the product and segment. For each criterion, provide what "good" looks like, red flags, and discovery questions to uncover it. Deliverable: qualification framework with scoring rubric.
3. **Discovery Question Bank**: Build a structured discovery question bank organized by buyer persona and deal stage. Include pain discovery, impact quantification, decision process mapping, and timeline validation questions. Deliverable: discovery question bank with persona tags.
4. **Competitive Battle Cards**: Create battle cards for the top 3 competitors covering positioning, strengths, weaknesses, landmines to set, and trap questions to ask. Include "why we win" and "why we lose" sections from win/loss data. Deliverable: competitive battle cards.
5. **Objection Handler**: Document the top 15 objections with response frameworks using the acknowledge-reframe-evidence pattern. Categorize by pricing, product, competition, timing, and trust. Deliverable: objection handler document.
6. **Closing Playbook**: Define closing techniques matched to deal types: trial close questions, proposal frameworks, negotiation guardrails, and mutual action plan templates. Deliverable: closing playbook section.
7. **Assembly and Review**: Assemble all components into a single navigable playbook. Review with VP Sales and 2 senior reps. Incorporate feedback and publish. Deliverable: complete sales playbook v1.0. [GATE]

## Anti-Patterns

- **Playbook as shelfware**: Building an exhaustive 100-page document that no rep reads. *Why*: playbooks succeed when they are referenced in the flow of work; length and complexity are inversely correlated with adoption.
- **Theory without examples**: Including frameworks without real deal examples that demonstrate how the framework applies. *Why*: reps learn from pattern matching on real scenarios, not abstract methodology.
- **Static playbook**: Publishing the playbook once without a defined update cadence. *Why*: competitive landscapes, product capabilities, and buyer expectations change quarterly; a stale playbook teaches outdated techniques.
- **Building without rep input**: Creating the playbook from management perspective without incorporating what top-performing reps actually say and do. *Why*: the gap between what management prescribes and what works in the field reduces credibility and adoption.

## Output

**On success**: Produces a complete sales playbook containing qualification framework, discovery question bank, competitive battle cards, objection handler, closing playbook, and mutual action plan templates. Delivered as a navigable document to the sales team with a training session scheduled.

**On failure**: Report which playbook section could not be completed (e.g., insufficient competitive intelligence for battle cards, no win/loss data for objection handler), what was attempted, and what inputs are needed.

## Related Skills

- [`first-sales-process-builder`](../first-sales-process-builder/SKILL.md) -- Provides the process framework the playbook operates within.
- [`objection-handler-updater-sales`](../objection-handler-updater-sales/SKILL.md) -- Maintains the objection handler component of the playbook over time.
- [`opportunity-framer-sales`](../../../sales/vp-sales/opportunity-framer-sales/SKILL.md) -- Supplies the opportunity frame and ICP definition the playbook is built around.
- [`solutions-playbook-builder`](../../../sales/solutions-engineering-manager/solutions-playbook-builder/SKILL.md) -- Builds the technical counterpart playbook for solutions engineers.
