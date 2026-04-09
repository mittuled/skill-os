---
name: integration-catalogue-builder
description: >
  This skill builds and maintains the integration catalogue documenting supported integrations and
  setup guides. Use when asked to document integrations, create integration setup guides, or
  maintain an integration registry. Also consider when customers ask which integrations are
  available. Suggest when the product adds a new integration and documentation is missing.
department: implementation
agent: implementation-lead
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "build integration catalogue"
  - "document integrations"
  - "create integration inventory"
  - "catalogue integrations"
  - "integration library"
---

# integration-catalogue-builder

## Agent: Implementation Lead

L1 implementation lead (1x) reporting to the COO, responsible for implementation playbook and integration catalogue. Bridges signed deals and live customers through operational delivery.

Department ethos: [ideal-implementation.md](../../../../departments/implementation/ideal-implementation.md)

## Skill Description

The integration catalogue builder creates and maintains a comprehensive catalogue of supported integrations with setup guides, prerequisites, and known limitations so implementation engineers and customers can configure integrations reliably.

## When to Use

- When the product launches a new integration and it needs to be documented for implementation and customer use.
- When customers or prospects ask which integrations are supported and detailed documentation is missing.
- When implementation engineers report repeated questions about integration setup that should be self-serve.
- When a periodic catalogue review is due to update status, deprecate old integrations, or add new ones.

## Workflow

1. **Inventory integrations**: List all supported integrations with their current status (GA, beta, deprecated). Deliverable: integration inventory.
2. **Write setup guides**: For each integration, document prerequisites, configuration steps, authentication requirements, and data mapping. Deliverable: per-integration setup guide.
3. **Document limitations**: Record known limitations, unsupported features, and workarounds for each integration. Deliverable: limitations appendix per integration.
4. **Publish the catalogue**: Organise the catalogue by category (CRM, billing, SSO, etc.) and publish in a searchable format. Deliverable: published integration catalogue.
5. **Establish update cadence**: Define a review schedule to keep the catalogue current as integrations are added, updated, or deprecated. Deliverable: maintenance schedule.

## Anti-Patterns

- **Documenting happy path only**: Writing setup guides that cover only the default configuration without edge cases or error handling. *Why*: implementation engineers spend time troubleshooting undocumented errors that a comprehensive guide would have prevented.
- **Catalogue without versioning**: Not tracking which product version each integration guide applies to. *Why*: outdated guides cause failed integrations when the product or third-party API has changed.

## Output

**On success**: A published integration catalogue with per-integration setup guides, prerequisites, limitations, and a defined maintenance cadence.

**On failure**: Report which integrations could not be documented (e.g., no engineering documentation available, API unstable), what was catalogued, and recommend follow-ups with engineering.

## Related Skills

- [`implementation-playbook-builder`](../implementation-playbook-builder/SKILL.md) -- the playbook references the integration catalogue during the integration phase.
- [`technical-onboarding-runner`](../../../implementation/implementation-engineer/technical-onboarding-runner/SKILL.md) -- onboarding runners use the catalogue to configure customer integrations.
