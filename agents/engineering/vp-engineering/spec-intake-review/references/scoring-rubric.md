# Scoring Rubric: spec-intake-review

Evaluates the completeness and engineering-readiness of an incoming feature specification before it enters the engineering planning pipeline.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Functional Completeness | 25% | Presence of user stories, acceptance criteria, edge cases, and success metrics |
| 2 | Non-Functional Requirements | 20% | Coverage of performance, security, accessibility, and observability requirements |
| 3 | Scope Clarity | 20% | Explicitness of in-scope and out-of-scope boundaries with no ambiguous grey areas |
| 4 | Feasibility Readiness | 20% | Absence of unresolvable technical blockers; dependencies and constraints identified |
| 5 | Ambiguity Level | 15% | Number and severity of open questions, contradictions, or implicit assumptions |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All user stories have testable acceptance criteria, NFRs quantified, scope boundaries explicit, zero open questions | Accept spec; proceed to backlog population |
| A | 8.0 – 8.9 | Strong | Acceptance criteria present for all stories, NFRs addressed, scope clear, minor open questions | Accept with minor clarifications tracked as tasks |
| B | 7.0 – 7.9 | Good | Most stories have acceptance criteria, NFRs partially addressed, scope mostly clear | Accept conditionally; return open questions to product within 2 days |
| C | 5.0 – 6.9 | Adequate | Some acceptance criteria missing, NFRs vague, scope boundaries blurry | Return for revision with specific feedback per section |
| D | 3.0 – 4.9 | Weak | Multiple stories lack acceptance criteria, NFRs absent, significant ambiguities | Return for major revision; schedule spec pairing session |
| F | 0.0 – 2.9 | Failing | No acceptance criteria, no NFRs, scope undefined, contradictions present | Reject; spec is not ready for engineering review |

## Signal Tables

### Functional Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Every user story has given/when/then acceptance criteria; edge cases enumerated with expected behaviour; success metrics defined with measurement method and target values |
| 7-8 | Acceptance criteria present for all primary stories; most edge cases identified; success metrics defined but measurement method unclear |
| 5-6 | Acceptance criteria present for some stories; edge cases mentioned but not enumerated; success metrics listed without targets |
| 3-4 | User stories present but acceptance criteria missing; no edge case analysis; success metrics absent |
| 0-2 | No user stories or requirements; feature described in a single paragraph without structure |

### Non-Functional Requirements

| Score | Evidence |
|-------|----------|
| 9-10 | Performance targets specified (latency percentiles, throughput); security requirements enumerated (auth, data classification); accessibility level stated (WCAG); observability requirements defined (logging, metrics, tracing) |
| 7-8 | Performance and security requirements specified; accessibility mentioned; observability partially addressed |
| 5-6 | Performance mentioned qualitatively ("should be fast"); security addressed at high level; accessibility and observability absent |
| 3-4 | One NFR category mentioned vaguely; others absent |
| 0-2 | No non-functional requirements present |

### Scope Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | Explicit in-scope list with numbered items; explicit out-of-scope list with rationale for each exclusion; future-phase items separated; no grey areas |
| 7-8 | In-scope and out-of-scope lists present; most boundaries clear; one or two items could be interpreted either way |
| 5-6 | In-scope described but out-of-scope not explicitly stated; boundaries inferred from context |
| 3-4 | Scope described narratively without explicit boundaries; easy to over- or under-interpret |
| 0-2 | No scope definition; feature boundaries completely undefined |

### Feasibility Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | All technical dependencies identified with status; third-party APIs evaluated; infrastructure requirements stated; no unresolvable blockers; spike results included for unknowns |
| 7-8 | Major dependencies identified; infrastructure needs noted; one or two unknowns flagged for spikes |
| 5-6 | Some dependencies mentioned; infrastructure needs vague; unknowns acknowledged but not scoped |
| 3-4 | Dependencies not systematically identified; reliance on unproven technology without acknowledgment |
| 0-2 | No feasibility consideration; spec assumes capabilities that may not exist |

### Ambiguity Level

| Score | Evidence |
|-------|----------|
| 9-10 | Zero open questions; all decisions made; no contradictory statements; assumptions explicitly documented |
| 7-8 | One or two minor open questions; no contradictions; assumptions documented |
| 5-6 | Three to five open questions; one minor contradiction; some implicit assumptions |
| 3-4 | More than five open questions; multiple contradictions; significant implicit assumptions |
| 0-2 | Spec is predominantly ambiguous; contradictions throughout; critical decisions deferred |
