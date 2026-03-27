---
name: requirements-extractor
description: >
  This skill extracts and structures functional and non-functional requirements from stakeholder
  inputs and discovery artifacts. Use when asked to turn interview notes, feature requests, or
  discovery findings into a structured requirements document. Also consider when a PRD lacks
  traceable requirements or when scope discussions keep circling without a shared source of truth.
  Suggest when the user is about to begin sprint planning without a validated requirements set.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "extract requirements from these notes"
  - "turn interview notes into requirements"
  - "what are the requirements for this feature"
  - "structure these feature requests"
---

# requirements-extractor

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Extracts and structures functional and non-functional requirements from discovery and stakeholder inputs into a traceable, prioritised requirements document.

## When to Use
- When discovery interviews, sales calls, or support tickets have produced raw input that needs to be distilled into discrete, testable requirements
- When a feature request arrives from leadership or customers and must be decomposed before engineering can estimate it
- When conflicting stakeholder expectations surface and the team needs a single authoritative requirements list to resolve ambiguity

## Workflow
1. **Gather raw inputs**: Collect all source material — interview transcripts, support tickets, feature request threads, competitive notes, and existing PRD fragments. Tag each source with origin and date. Deliverable: indexed input inventory with source metadata.
2. **Identify requirement candidates**: Parse each input for explicit asks, implicit needs, and constraints. Write each as a single declarative sentence starting with "The system shall..." or "The user can...". Deliverable: flat list of candidate requirement statements.
3. **Classify and structure**: Categorise each requirement as functional, non-functional (performance, security, accessibility, compliance), or constraint. Assign a unique ID (e.g., FR-001, NFR-001). Group by feature area. Deliverable: structured requirements table with ID, category, statement, and source traceability.
4. **Prioritise and flag gaps**: Apply MoSCoW or RICE to rank requirements. Flag any requirement that lacks a clear acceptance criterion or has conflicting sources. Deliverable: prioritised requirements list with gap annotations.
5. **Validate with stakeholders**: Walk the requirements list through product, engineering, and the original requesters. Confirm each requirement is understood, feasible, and correctly prioritised. Deliverable: sign-off record or revision log.

## Anti-Patterns
- **Solution-stuffed requirements**: Writing "add a dropdown that filters by date" instead of stating the underlying need. *Why*: Embedding implementation details in requirements constrains engineering options and produces brittle specs that resist design iteration.
- **Orphan requirements**: Including requirements that cannot be traced back to any discovery input or business goal. *Why*: Untraceable requirements erode trust in the document and invite scope creep because no one can explain why they exist.
- **Monolithic requirement blocks**: Bundling multiple behaviours into a single requirement statement. *Why*: Compound requirements are impossible to estimate, test, or partially deliver — they hide complexity and block incremental progress.

## Output
**On success**: A structured requirements document containing uniquely identified, categorised, and prioritised requirement statements with source traceability and acceptance criteria — formatted as a markdown table suitable for embedding in a PRD or importing into a backlog tool.

**On failure**: Report which inputs could not be parsed (ambiguous recordings, missing context), which requirements lack acceptance criteria or stakeholder agreement, and recommend specific follow-up interviews or data pulls to close the gaps.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
