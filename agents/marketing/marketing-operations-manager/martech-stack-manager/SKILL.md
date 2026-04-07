---
name: martech-stack-manager
description: >
  This skill selects, configures, and maintains marketing automation, email, analytics, and ad
  platforms. Use when evaluating new martech tools, onboarding a platform, or auditing the
  existing stack for redundancy and integration gaps. Also consider when a platform renewal
  is approaching. Suggest when marketing operations are slowed by tool limitations or
  broken integrations.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../email-deliverability-manager/SKILL.md
  - ../marketing-attribution-modeller/SKILL.md
---

# martech-stack-manager

## Agent: Marketing Operations Manager

L2 marketing operations manager (1x) responsible for martech stack, lead scoring, campaign analytics, attribution modelling, and email deliverability.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Selects, configures, and maintains the marketing technology stack -- marketing automation, ESP, analytics, ad platforms, and integrations -- ensuring reliable data flow and operational efficiency.

## When to Use

- When evaluating a new martech tool for purchase or replacement of an existing platform.
- When onboarding a new platform that requires configuration, integration, and team training.
- When auditing the existing stack for redundancy, integration gaps, or underutilized licenses.
- When a platform contract renewal is approaching and requires a build-vs-buy-vs-renew decision.

## Workflow

1. **Inventory current stack**: Document all marketing tools using the core stack layer model in [`references/framework.md`](references/framework.md). Apply the stack health audit criteria to identify overlapping capabilities, orphaned tools, and integration failures. Deliverable: martech stack inventory with utilization, cost, and layer coverage analysis.
2. **Identify gaps and requirements**: Map the stack layers from [`references/framework.md`](references/framework.md) against current marketing operational needs. Flag capability gaps and calculate 3-year TCO for gap-filling options. Deliverable: gap analysis with prioritized requirements.
3. **Evaluate solutions**: Score vendor options using the vendor evaluation matrix in [`references/framework.md`](references/framework.md). Apply the build vs. buy vs. renew decision criteria. Require composite score ≥ 3.5/5 to advance to recommendation. Deliverable: vendor evaluation matrix with recommendation.
4. **Implement and integrate**: Configure the selected platform using the integration patterns appropriate to each connection type from [`references/framework.md`](references/framework.md). Produce a data flow diagram and field mapping document before go-live. Deliverable: configured platform with validated integrations.
5. **Train and document**: Create operational documentation and train marketing team members. Establish support escalation paths and admin access controls. Deliverable: training materials and operational runbook.

## Anti-Patterns

- **Shiny-tool syndrome**: Adopting new tools based on vendor demos rather than defined operational requirements. *Why*: tools acquired without a clear use case become shelfware that adds cost and complexity without value.
- **Integration neglect**: Adding platforms without building proper data integrations to the rest of the stack. *Why*: disconnected tools create data silos that break attribution, scoring, and reporting accuracy.
- **Single-admin dependency**: Concentrating all platform administration knowledge in one person without documentation. *Why*: when that person is unavailable, the entire marketing operations stack becomes unmanageable.

## Output

**On success**: Produces a martech stack inventory, gap analysis, vendor evaluation matrix, configured platforms with validated integrations, and operational documentation. The stack reliably supports all marketing operations. Delivered to VP Marketing and marketing operations team.

**On failure**: Report which tools could not be properly configured or integrated, what workarounds are in place, vendor support ticket status, and recommend escalation paths or alternative solutions.

## Related Skills

- [`email-deliverability-manager`](../email-deliverability-manager/SKILL.md) — ESP configuration and sending infrastructure are managed as part of the martech stack.
- [`marketing-attribution-modeller`](../marketing-attribution-modeller/SKILL.md) — Attribution depends on clean data flow between stack components managed by this skill.
- [`campaign-analytics-reporter`](../campaign-analytics-reporter/SKILL.md) — Reporting accuracy depends on properly configured analytics and data integrations.
- [`lead-scoring-model-builder`](../lead-scoring-model-builder/SKILL.md) — Scoring models are implemented in the marketing automation platform managed here.
