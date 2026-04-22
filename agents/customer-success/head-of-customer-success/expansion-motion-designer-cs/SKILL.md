---
name: expansion-motion-designer-cs
description: >
  This skill designs the expansion motion for CS including health-based triggers
  and handoff criteria to Account Management. Use when asked to define expansion
  criteria, design upsell workflows, or create CS-to-AM handoff processes. Also
  consider when expansion revenue is underperforming. Suggest when the user has
  healthy accounts but no systematic expansion process.
department: customer-success
agent: head-of-customer-success
version: 1.0.0
complexity: medium
related-skills:
  - cs-health-monitor
  - cs-signal-extractor
  - sla-definer-cs
triggers:
  - "design expansion motion"
  - "expansion motion cs"
  - "upsell strategy cs"
  - "create expansion playbook"
  - "expansion revenue cs"
---

# expansion-motion-designer-cs

## Agent: Head of Customer Success

L1 customer success leader reporting to the CBO (1x) responsible for CS strategy, SLA design, playbook creation, expansion motion, and training materials.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Designs the expansion motion for CS including health-based triggers, expansion qualification criteria, and handoff protocols to Account Management.

## When to Use

- When the CS team needs a systematic process for identifying and qualifying expansion opportunities.
- When expansion revenue is below targets and the CS-to-AM handoff process is undefined or broken.
- When customer health scores indicate expansion readiness but no structured motion exists to act on it.

## Workflow

1. **Define Expansion Signals**: Identify the health-based triggers that indicate expansion readiness -- usage growth, feature adoption breadth, high NPS, team expansion, approaching contract limits. Deliverable: expansion signal definitions with thresholds.
2. **Design Qualification Criteria**: Establish criteria for when an expansion signal becomes a qualified opportunity -- minimum health score, account tenure, usage consistency. Deliverable: expansion qualification framework.
3. **Map CS-to-AM Handoff**: Define the handoff process: what context CS provides to AM, when the handoff occurs, and how the customer experience remains seamless during the transition. Deliverable: handoff protocol with templates.
4. **Build CS Expansion Playbook**: Create the CS team's guide for nurturing expansion-ready accounts -- conversation frameworks, value quantification templates, and timing guidance. Deliverable: CS expansion playbook.
5. **Establish Tracking**: Define metrics for the expansion motion -- signal-to-opportunity conversion rate, handoff success rate, and CS-sourced expansion revenue. Deliverable: expansion metrics framework.

## Anti-Patterns

- **Premature expansion push**: Triggering expansion conversations before the customer has achieved full value from their current contract. *Why*: asking for more money before delivering promised value erodes trust and increases churn risk.
- **CS as sales**: Having CS managers directly sell expansion instead of qualifying and handing off to AM. *Why*: customers perceive CS as a trusted advisor; selling compromises that trust and the CS relationship.
- **Ignoring health signals**: Pursuing expansion with unhealthy accounts because of revenue pressure. *Why*: expanding an unhealthy account compounds their problems and accelerates churn.

## Output

**On success**: Produces an expansion motion design document containing signal definitions, qualification criteria, CS-to-AM handoff protocol, CS expansion playbook, and metrics framework. Delivered to the CS Manager and Account Management Lead.

**On failure**: Report which expansion motion components could not be designed (undefined health scoring, missing AM alignment), what was drafted, and what cross-functional alignment is needed.

## Related Skills

- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- Health monitoring provides the signals that trigger the expansion motion.
- [`cs-signal-extractor`](../../../customer-success/customer-success-manager/cs-signal-extractor/SKILL.md) -- Signal extraction identifies expansion indicators from customer interactions.
- [`sla-definer-cs`](../sla-definer-cs/SKILL.md) -- SLAs must be met before expansion is appropriate.
