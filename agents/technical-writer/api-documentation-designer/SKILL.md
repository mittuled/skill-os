---
name: api-documentation-designer
description: >
  This skill designs the structure and format of API reference documentation.
  Use when asked to create an API docs architecture, define documentation standards, or restructure existing API references.
  Also consider when adding a new API product that needs documentation from scratch.
  Suggest when the user is about to write API docs without an information architecture.
department: marketing
agent: technical-writer
version: 1.0.0
complexity: medium
related-skills: []
---

# api-documentation-designer

## Agent: Technical Writer

L3 technical writer reporting to Developer Relations Lead, responsible for API documentation, developer guides, and documentation accuracy.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Designs the structure and format of API reference documentation to maximize developer comprehension and time-to-integration.

## When to Use

- When a new API product needs documentation architecture before writing begins.
- When existing API docs are disorganized and developers report difficulty finding information.
- When migrating API documentation to a new platform and needing to redesign the information architecture.
- When adding a second API product and needing consistent documentation standards across both.

## Workflow

1. **Audit existing documentation**: Review current API docs (if any) for structure, coverage gaps, and developer feedback on navigation and findability. Classify existing pages against the Divio type model in [framework.md](references/framework.md) to identify type mixing. Deliverable: documentation audit report.
2. **Define audience and use cases**: Identify the primary developer personas and their top API use cases. Use the documentation type selection table in the framework to determine which types are needed. Deliverable: audience-use case matrix with documentation type mapping.
3. **Design information architecture**: Select the IA pattern from the framework (task-first, resource-first, concept-first, or hybrid) and define the URL scheme, navigation structure, and cross-linking strategy. Deliverable: information architecture diagram.
4. **Define page templates**: Create standardized templates using the endpoint reference and quickstart template specifications from the framework. Deliverable: template library with field definitions.
5. **Establish style standards**: Adopt the style standards table from the framework as the base. Add product-specific conventions for parameter naming and domain terminology. Deliverable: API documentation style guide.
6. **Validate with developers**: Test the proposed structure with target developers through card sorting or prototype navigation exercises. Deliverable: validation findings with revisions.

## Anti-Patterns

- **Reference-only documentation**: Designing only auto-generated endpoint references without guides, tutorials, or conceptual content. *Why*: Reference docs answer "what" but not "how" or "why"; developers need task-oriented content to understand when and how to combine endpoints.
- **Flat structure**: Putting all documentation at one level without hierarchy or progressive disclosure. *Why*: Developers at different experience levels need different entry points; flat structures overwhelm beginners and frustrate experts who cannot jump to specifics.
- **Designing without API knowledge**: Creating an information architecture without understanding the API's domain model and key workflows. *Why*: Documentation structure should mirror the mental model developers need to build; an uninformed structure creates navigation that does not match developer tasks.

## Output

**On success**: Produces an API documentation design package containing information architecture, page templates, style guide, and validation findings. Delivered to technical writing and developer relations teams.

**On failure**: Report which design components could not be completed, what API information was unavailable, and recommend how to unblock. Every error must be actionable.

## Related Skills

- [`documentation-writer`](../documentation-writer/SKILL.md) — Writers use the templates and architecture designed here to produce actual documentation.
- [`api-developer-experience-reviewer`](../../developer-relations-lead/api-developer-experience-reviewer/SKILL.md) — API DX reviews surface documentation structure issues that feed back into design improvements.
- [`documentation-scale-planner`](../documentation-scale-planner/SKILL.md) — Documentation architecture must be designed with scalability considerations from the start.
