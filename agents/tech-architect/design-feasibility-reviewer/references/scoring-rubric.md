# Scoring Rubric: design-feasibility-reviewer

Evaluates the rigor of a technical review of design proposals against implementation constraints and platform capabilities.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Technical Decomposition Depth | 25% | How thoroughly the design is broken into assessable technical components (data, state, interactions, animations, platform behaviors) |
| 2 | Constraint Mapping Accuracy | 25% | How precisely each component is matched against real API capabilities, latency budgets, device constraints, and framework limits |
| 3 | Verdict Specificity | 20% | How clearly each component is classified (feasible / feasible-with-modifications / infeasible) with concrete alternatives for non-feasible items |
| 4 | Effort-Value Assessment | 15% | Quality of effort estimates and identification of disproportionate engineering cost relative to user value |
| 5 | Performance Flagging | 15% | Whether performance-feasible but performance-problematic designs are explicitly flagged with quantitative impact |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All components decomposed and assessed with constraint data; every non-feasible item has a documented alternative; performance flags quantified | Approve; share as reference for design-engineering collaboration |
| A | 8.0 – 8.9 | Strong | Near-complete assessment with minor gaps; alternatives provided for most non-feasible items | Approve with minor follow-up items |
| B | 7.0 – 7.9 | Good | Most components assessed; 1–2 missing alternatives; effort estimates present | Approve with documented action items for engineering |
| C | 5.0 – 6.9 | Adequate | Decomposition is coarse; key constraints unverified; verdicts lack alternatives | Return to design team with specific questions; reassess before sprint commit |
| D | 3.0 – 4.9 | Weak | Review covers only obvious infeasibilities; no constraint mapping; no effort estimates | Reject; require structured review using decomposition framework |
| F | 0.0 – 2.9 | Failing | Blanket feasibility verdict without component-level analysis; or review not conducted | Do not proceed to sprint planning; escalate need for review |

## Signal Tables

### Technical Decomposition Depth

| Score | Evidence |
|-------|----------|
| 9–10 | Design broken into ≥ 6 distinct technical components including data requirements per screen, state management, interaction events, animation specs, and platform-specific behaviors |
| 7–8 | Design broken into 4–5 components; all major interaction patterns covered; one minor behavioral aspect not decomposed |
| 5–6 | Design broken into 2–3 high-level areas (e.g., "frontend", "backend"); interactions and state management not separately analysed |
| 3–4 | Single-component view of the design; only the most obvious technical requirement identified |
| 0–2 | No decomposition; review treats design as a monolithic whole or is absent |

### Constraint Mapping Accuracy

| Score | Evidence |
|-------|----------|
| 9–10 | Each component mapped against verified API endpoints, measured latency baselines, tested device capabilities, and documented framework limits; all claims traceable to source |
| 7–8 | Most components mapped against verified data; 1–2 constraints estimated rather than verified; sources documented |
| 5–6 | Constraints referenced but not verified against actual system state; latency budgets assumed, not measured |
| 3–4 | Only one constraint dimension assessed (e.g., API availability); device, performance, and framework limits not checked |
| 0–2 | No constraint mapping; review based on general engineering knowledge without reference to the actual system |

### Verdict Specificity

| Score | Evidence |
|-------|----------|
| 9–10 | Every component has an explicit verdict (feasible / feasible-with-modifications / infeasible); all modified/infeasible items have ≥ 1 specific alternative design that achieves the user intent |
| 7–8 | All components have verdicts; alternatives provided for infeasible items; modified items missing specific alternative in 1–2 cases |
| 5–6 | Verdicts present for major components; alternatives for infeasible items are vague ("simplify the animation") rather than specific |
| 3–4 | Only infeasible items have verdicts; feasible components have no documentation; no alternatives |
| 0–2 | Single verdict for the entire design without component breakdown |

### Effort-Value Assessment

| Score | Evidence |
|-------|----------|
| 9–10 | All components have story-point or day-range estimates; items with effort > 5 days have explicit value-effort flags and a recommendation (build/defer/descope) |
| 7–8 | Estimates for all major components; value-effort flags for 80%+ of high-effort items |
| 5–6 | T-shirt size estimates present for all components; no value-effort analysis |
| 3–4 | Effort estimates for some components only; no value-effort analysis |
| 0–2 | No effort estimates included in the review |

### Performance Flagging

| Score | Evidence |
|-------|----------|
| 9–10 | All rendering-intensive, real-time, or high-frequency interaction components tested or benchmarked; impact quantified (e.g., "list virtualization required: rendering 500+ rows causes > 200ms frame drop on mid-range Android") |
| 7–8 | Performance-sensitive components flagged with qualitative impact; benchmarking data cited for primary concern |
| 5–6 | One or two performance issues flagged without quantitative data; other performance-sensitive components not addressed |
| 3–4 | Performance mentioned only in response to obvious animations; no proactive flagging |
| 0–2 | No performance considerations in the review; all designs treated as equally implementable |
