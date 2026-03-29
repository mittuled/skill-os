# Framework: Scope Adjustment

## Core Model

MoSCoW prioritisation applied mid-phase to re-rank scope items when constraints change. The goal is to preserve the phase's core value commitment while cutting or deferring lower-value items.

## MoSCoW Classification

| Category | Definition | Mid-Phase Rule |
|----------|-----------|----------------|
| Must Have | Required for the phase to deliver its core value proposition | Never cut without escalation to initiative owner |
| Should Have | Important but the phase can deliver value without it | First candidates for deferral if capacity drops |
| Could Have | Desirable if capacity permits | Cut immediately when constraints tighten |
| Won't Have | Explicitly excluded from this phase | Already out of scope; documented for future phases |

## Scope Option Modelling

When adjusting scope, produce 2-3 scenarios:

| Scenario | What Ships | What is Deferred | Exit Criteria Impact | Timeline Impact |
|----------|-----------|-----------------|---------------------|----------------|
| A (minimal cut) | Must + all Should | Could items | Full exit criteria met | +N days |
| B (moderate cut) | Must + priority Should | Remaining Should + Could | Core exit criteria met | On schedule |
| C (aggressive cut) | Must only | All Should + Could | Minimum viable exit criteria | Ahead of schedule |

## Decision Record Format

Every scope adjustment must produce:
1. **Trigger**: What changed (quantified)
2. **Options evaluated**: The 2-3 scenarios with trade-offs
3. **Decision**: Which option was selected and by whom
4. **Rationale**: Why this option best preserves the phase's core value
5. **Downstream updates**: What artifacts were revised (phase plan, backlog, stakeholder comms)

## Deferral Protocol

Deferred items must have:
- A landing zone (which future phase or backlog)
- Confirmation that the landing zone has capacity
- A staleness review date (if not picked up by date X, re-evaluate whether the item still matters)
