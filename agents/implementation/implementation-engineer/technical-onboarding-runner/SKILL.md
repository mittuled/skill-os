---
name: technical-onboarding-runner
description: >
  This skill runs the technical onboarding process for new customers including configuration,
  integration, and validation. Use when asked to set up a customer environment, configure
  integrations, or run go-live validation. Also consider when requirements extraction is complete
  and implementation is ready to begin. Suggest when a signed customer is waiting for technical setup.
department: implementation
agent: implementation-engineer
version: 1.0.0
complexity: medium
related-skills:
  - implementation-requirements-extractor
  - implementation-playbook-builder
  - integration-catalogue-builder
triggers:
  - "run technical onboarding"
  - "execute customer onboarding"
  - "onboard new customer"
  - "deploy customer environment"
  - "technical onboarding setup"
---

# technical-onboarding-runner

## Agent: Implementation Engineer

L2 implementation engineer (Nx, multi-instance) responsible for extracting customer requirements and running technical onboarding.

Department ethos: [ideal-implementation.md](../../../../departments/implementation/ideal-implementation.md)

## Skill Description

The technical onboarding runner configures the customer's product environment, sets up integrations, migrates data, and validates the deployment against acceptance criteria to bring the customer from signed deal to live production usage.

## When to Use

- When requirements extraction is complete and the customer is ready for technical implementation.
- When a customer's environment needs configuration, integration setup, and data migration.
- When a go-live date is approaching and the implementation needs validation against acceptance criteria.
- When a customer upgrades or adds modules requiring additional technical setup.

## Workflow

1. **Set up the environment**: Provision and configure the customer's product environment based on the requirements document. Deliverable: configured customer environment.
2. **Configure integrations**: Set up integrations with the customer's systems using the integration catalogue guides. Deliverable: configured integrations with connectivity verification.
3. **Migrate data**: Execute data migration from the customer's existing systems with mapping, transformation, and validation. Deliverable: migrated dataset with quality report.
4. **Run acceptance testing**: Validate the implementation against the acceptance criteria defined in the requirements document. Deliverable: acceptance test results.
5. **Conduct customer training**: Walk the customer's team through the configured environment, workflows, and key features. Deliverable: training session with materials delivered.
6. **Execute go-live**: Transition the customer to production usage, confirm systems are operational, and enter the hypercare period. Deliverable: go-live confirmation and hypercare plan.

## Anti-Patterns

- **Configuring without requirements sign-off**: Starting technical setup before the customer has signed off on requirements. *Why*: unsigned requirements lead to rework when the customer clarifies or changes expectations mid-implementation.
- **Skipping acceptance testing**: Going live without running the implementation against documented acceptance criteria. *Why*: untested implementations surface issues in production that damage the customer's first experience.
- **No hypercare period**: Declaring implementation complete at go-live without a stabilisation period. *Why*: the first days of production usage always surface issues; without hypercare, these become support tickets that erode satisfaction.

## Output

**On success**: A customer live in production with a configured environment, working integrations, migrated data, passed acceptance tests, trained users, and an active hypercare period.

**On failure**: Report which implementation steps failed (e.g., integration connectivity error, data migration quality issue), what was completed, and provide a remediation plan with revised go-live date.

## Related Skills

- [`implementation-requirements-extractor`](../implementation-requirements-extractor/SKILL.md) -- requirements extraction produces the specification this skill implements.
- [`implementation-playbook-builder`](../../../implementation/implementation-lead/implementation-playbook-builder/SKILL.md) -- the playbook defines the process this skill follows for each customer.
- [`integration-catalogue-builder`](../../../implementation/implementation-lead/integration-catalogue-builder/SKILL.md) -- the catalogue provides the integration setup guides used during onboarding.
