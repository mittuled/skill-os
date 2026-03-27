---
name: prd-assembler
description: >
  This skill assembles a complete product requirements document by synthesizing inputs from discovery,
  design, and engineering into a single authoritative spec. Use when a feature or product has cleared
  opportunity validation and needs a formal PRD before engineering begins. Also consider when an
  existing PRD is stale and must be refreshed after significant scope changes. Suggest when discovery
  artifacts, wireframes, and technical feasibility signals exist but no unified spec ties them together.
department: product
agent: vp-product
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "write the PRD"
  - "assemble a product requirements doc"
  - "create a spec for this feature"
  - "put together the PRD"
  - "draft the product spec"
---

# prd-assembler

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Assembles the product requirements document from inputs across discovery, design, and engineering into a single authoritative specification ready for sprint planning.

## When to Use
- When a validated opportunity needs a formal PRD before engineering commits resources
- When discovery research, design explorations, and technical feasibility assessments are available but scattered across separate artifacts
- When an existing PRD has drifted from reality due to scope negotiations, pivot decisions, or newly surfaced constraints
- When stakeholders request a single source of truth that captures problem statement, success criteria, user stories, and technical boundaries
- When transitioning from opportunity framing to build phase and the team needs a handoff document

## Workflow
1. **Inventory inputs**: Collect all discovery briefs, user research summaries, competitive analysis outputs, design wireframes, and engineering feasibility notes. Deliverable: input manifest listing every source artifact with status and owner.
2. **Define problem statement**: Distill the validated opportunity into a crisp problem statement with target persona, pain point, and desired outcome. Deliverable: problem statement block (3-5 sentences).
3. **Draft success criteria**: Translate the north-star metric and product goals into measurable acceptance criteria with specific thresholds and timeframes. Deliverable: success criteria table with metric, target, measurement method, and deadline.
4. **Compose user stories**: Write user stories in standard format (As a [persona], I want [action], so that [outcome]) covering the MVP scope. Prioritize using MoSCoW or RICE. Deliverable: prioritized user story list.
5. **Capture design requirements**: Reference wireframes and interaction specs, noting key UX decisions, accessibility requirements, and platform constraints. Deliverable: design requirements section with links to Figma files and annotation of open design questions.
6. **Document technical constraints**: Incorporate engineering feasibility findings including API dependencies, data model implications, performance budgets, and infrastructure requirements. Deliverable: technical constraints section with architecture notes and risk flags.
7. **Define scope boundaries**: Explicitly list what is in-scope for MVP and what is deferred. Call out assumptions and dependencies on other teams. Deliverable: scope section with in/out table and dependency map.
8. **Assemble and cross-reference**: Merge all sections into the PRD template. Ensure every user story traces back to a success criterion and every design requirement maps to a user story. Deliverable: complete PRD draft with traceability matrix.
9. **Circulate for sign-off**: Share the PRD with engineering lead, design lead, and key stakeholders. Collect feedback, resolve conflicts, and lock the version. Deliverable: signed-off PRD with version number, approval log, and distribution record.

## Anti-Patterns
- **Kitchen-sink PRD**: Including every conceivable feature and edge case in the initial document. *Why*: Bloated PRDs delay alignment, create ambiguity about MVP boundaries, and invite scope creep during sprint planning.
- **Copy-paste assembly**: Stitching discovery and design artifacts together verbatim without synthesis or reconciliation. *Why*: Raw inputs often contradict each other or use inconsistent terminology, producing a PRD that confuses rather than clarifies.
- **Missing acceptance criteria**: Writing user stories without measurable success criteria. *Why*: Engineering cannot verify completion, QA cannot write test cases, and launch decisions become subjective.
- **Solo authorship without review**: Finalizing the PRD without engineering and design sign-off. *Why*: Unreviewed specs surface feasibility gaps mid-sprint, causing costly rework and eroding cross-functional trust.
- **Scope ambiguity**: Failing to explicitly state what is out of scope. *Why*: Teams fill gaps with assumptions, leading to gold-plating or missed requirements discovered only at launch.

## Output
**On success**: A versioned PRD document containing problem statement, success criteria, prioritized user stories, design requirements, technical constraints, scope boundaries, and traceability matrix -- ready for sprint planning and stakeholder reference.
**On failure**: Report which input artifacts are missing or conflicting, what sections could not be completed, and recommend specific follow-up actions (e.g., "engineering feasibility for payment integration is unresolved -- schedule a spike before PRD finalization").

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
