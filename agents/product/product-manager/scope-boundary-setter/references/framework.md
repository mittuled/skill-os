# Framework: Scope Boundary Setting

## Core Model

Explicit scope classification system that separates committed work (In), excluded work (Out), and conditional work (Conditional) with a change protocol to enforce the boundary during execution.

## Scope Classification

| Category | Definition | Criteria for Inclusion |
|----------|-----------|----------------------|
| In | Committed for this sprint/release; team is accountable for delivery | Has estimate, acceptance criteria, assigned owner, no unresolved blockers |
| Out | Explicitly excluded; will not be worked on in this cycle | Documented reason for exclusion; may be backlogged for future |
| Conditional | May be promoted to In if a specific trigger fires | Trigger condition defined (e.g., "if dependency ships by Wednesday") |

## Capacity Buffer Model

| Category | % of Total Capacity | Purpose |
|----------|-------------------|---------|
| Committed scope (In) | 80-85% | Stories and tasks with estimates |
| Buffer (unplanned) | 10-15% | Production incidents, clarification loops, sick days |
| Conditional scope | 5-10% | Items promoted if buffer is unused and trigger fires |

## Change Protocol Template

A scope change request must include:
1. **Requestor**: Who is asking for the change
2. **Item description**: What is being added (with estimate)
3. **Trade-off**: What existing In-scope item is being removed or deferred to make room
4. **Impact assessment**: Effect on sprint goal, timeline, and dependencies
5. **Approval**: Named approver (typically PM or engineering lead)

## Scope Lock Record

| Field | Value |
|-------|-------|
| Sprint/Release | [identifier] |
| Lock Timestamp | [YYYY-MM-DD HH:MM] |
| Total Capacity | [X story points / hours] |
| Committed Utilisation | [Y% of capacity] |
| Buffer | [Z% of capacity] |
| Sign-off | [Names of PM, eng lead, and stakeholders who acknowledged] |

## Change Log Format

| # | Date | Request | Requestor | Decision | Trade-Off | Approver |
|---|------|---------|-----------|----------|-----------|----------|
| 1 | ... | Add story X | ... | Approved | Defer story Y | ... |
