# Framework: Requirements Extraction

## Core Model

Systematic extraction of requirements from unstructured inputs using RICE prioritisation and MoSCoW classification, producing traceable, testable requirement statements.

## Requirement Statement Format

Every requirement follows: `[ID] [Category] The system shall <verb> <object> <condition>.`

- **ID**: FR-001 (functional), NFR-001 (non-functional), CON-001 (constraint)
- **Category**: Functional, Performance, Security, Accessibility, Compliance, Constraint
- **Statement**: Single behaviour per statement, declarative, no implementation details

## RICE Scoring for Prioritisation

| Factor | Scoring | Description |
|--------|---------|-------------|
| Reach | Number of users/accounts affected per quarter | How many users does this touch? |
| Impact | 0.25 (minimal) to 3 (massive) | How much does this move the needle per user? |
| Confidence | 0-100% | How sure are we about reach and impact estimates? |
| Effort | Person-weeks | How much work is required? |

**RICE Score** = (Reach x Impact x Confidence) / Effort

## MoSCoW Classification

Applied after RICE scoring to create a delivery-oriented grouping:
- **Must**: RICE > threshold AND required for launch viability
- **Should**: RICE > threshold but launch can proceed without
- **Could**: Moderate RICE, included if capacity permits
- **Won't**: Low RICE or explicitly deferred

## Source Traceability Matrix

| Req ID | Statement | Category | Source | Source Date | RICE Score | MoSCoW | Acceptance Criteria |
|--------|-----------|----------|--------|-------------|------------|--------|-------------------|
| FR-001 | ... | Functional | Interview #3 | 2026-03-15 | 42 | Must | ... |

## Gap Detection Checklist

- [ ] Every requirement has at least one acceptance criterion
- [ ] No requirement bundles multiple behaviours
- [ ] Every requirement traces to at least one source
- [ ] Conflicting sources are flagged and resolution documented
- [ ] Non-functional requirements cover performance, security, accessibility at minimum
