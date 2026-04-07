---
name: revenue-tooling-readiness
description: >
  This skill ensures all revenue tooling (CRM, billing, CPQ) is configured and ready before go-live.
  Use when asked to validate revenue tool readiness, run pre-launch tooling checks, or prepare
  billing systems. Also consider when a new pricing model requires billing system changes.
  Suggest when go-live is approaching and revenue tooling has not been validated end-to-end.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: simple
related-skills: []
---

# revenue-tooling-readiness

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)

## Skill Description

The revenue tooling readiness skill validates that all revenue-facing tools -- CRM, billing, CPQ, and analytics -- are correctly configured, integrated, and tested before go-live to prevent revenue leakage and operational failures.

## When to Use

- When a product launch or pricing change is approaching and revenue tooling needs end-to-end validation.
- When a new billing system or CPQ tool has been configured and needs pre-launch testing.
- When the launch checklist includes a RevOps readiness gate.

## Workflow

1. **Inventory revenue tools**: List all revenue-facing tools and their role in the deal-to-cash flow. Deliverable: revenue tooling map.
2. **Define readiness criteria**: Establish what "ready" means for each tool: data flowing correctly, automations firing, reports accurate. Deliverable: readiness checklist per tool.
3. **Run end-to-end test**: Process a test transaction through the full deal-to-cash workflow (CRM to billing to revenue recognition). Deliverable: test transaction results.
4. **Resolve issues**: Fix any failures found during testing and retest. Deliverable: issue resolution log.
5. **Sign off**: Issue a go/no-go recommendation based on test results. Deliverable: tooling readiness sign-off.

## Anti-Patterns

- **Testing tools in isolation**: Validating each tool independently without testing the end-to-end data flow. *Why*: individual tools can work perfectly while the integration between them fails silently.
- **Skipping billing validation**: Assuming billing "just works" because the CRM is configured. *Why*: billing errors cause revenue leakage that may not be detected for weeks or months.

## Output

**On success**: A tooling readiness sign-off confirming all revenue tools are configured, integrated, and validated with a successful end-to-end test transaction.

**On failure**: Report which tools failed testing, what the specific failures were, and provide a remediation plan with timeline to achieve readiness.

## Related Skills

- [`crm-setup-v1`](../crm-setup-v1/SKILL.md) -- CRM setup is a prerequisite; this skill validates it alongside other revenue tools.
- [`revenue-model-operationaliser`](../revenue-model-operationaliser/SKILL.md) -- the operationalised revenue model defines what the tooling must support.
