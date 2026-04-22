---
name: crm-setup-v1
description: >
  This skill configures the initial CRM with pipeline stages, fields, and automation rules.
  Use when asked to set up a CRM, define sales pipeline stages, or configure deal tracking.
  Also consider when migrating from spreadsheets to a CRM for the first time.
  Suggest when the company closes its first deals and needs structured pipeline management.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: medium
related-skills:
  - revenue-model-operationaliser
  - revenue-tooling-readiness
triggers:
  - "set up CRM"
  - "configure CRM pipeline"
  - "CRM initial setup"
  - "define pipeline stages"
  - "build deal tracking"
---

# crm-setup-v1

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The CRM setup skill configures the initial CRM instance with pipeline stages, custom fields, automation rules, and integrations so the sales team has a structured system for tracking deals from lead to close.

## When to Use

- When the company is setting up a CRM for the first time to replace ad-hoc deal tracking.
- When the revenue model has been defined and needs to be operationalised in CRM pipeline stages.
- When migrating from one CRM to another and the new instance needs configuration.
- When a new product line or sales motion requires a separate pipeline in the existing CRM.

## Workflow

1. **Map the sales process**: Document the sales stages from lead qualification through close, aligned with the revenue model. Deliverable: pipeline stage definitions with entry/exit criteria.
2. **Define custom fields**: Create fields for deal metadata (deal size, source, product, close date, etc.) based on reporting needs. Deliverable: field schema document.
3. **Configure automation**: Set up automation rules for stage transitions, task creation, notifications, and data validation. Deliverable: automation rules with trigger conditions.
4. **Set up integrations**: Connect the CRM to marketing tools, email, calendar, and billing systems. Deliverable: integration configuration with data flow map.
5. **Import existing data**: Migrate any existing deal and contact data into the new CRM with field mapping and deduplication. Deliverable: migrated dataset with quality report.
6. **Test end-to-end**: Process a test deal through the full pipeline to validate stages, automations, and integrations. Deliverable: test results with issues resolved.

## Anti-Patterns

- **Over-customising for hypothetical needs**: Adding dozens of custom fields and automations before anyone has used the CRM. *Why*: unused complexity confuses sales reps and creates maintenance burden; start simple and iterate.
- **Configuring without sales input**: Building the pipeline stages based on theory rather than how deals actually progress. *Why*: a pipeline that does not match the real sales process is ignored by reps who revert to spreadsheets.
- **Skipping data hygiene on import**: Migrating dirty data from spreadsheets without deduplication and validation. *Why*: garbage data in a new CRM undermines trust in the system from day one.

## Output

**On success**: A configured CRM with pipeline stages matching the sales process, custom fields for reporting, working automations, connected integrations, and migrated data validated by an end-to-end test deal.

**On failure**: Report which configuration components are incomplete (e.g., integration blocked by API access), what was configured, and provide steps to complete the setup.

## Related Skills

- [`revenue-model-operationaliser`](../revenue-model-operationaliser/SKILL.md) -- the revenue model defines the pipeline stages this skill configures.
- [`revenue-tooling-readiness`](../revenue-tooling-readiness/SKILL.md) -- tooling readiness validates the CRM is ready alongside other revenue tools before go-live.
