# Scoring Rubric: technical-feasibility-check

Evaluates the rigor and completeness of a technical feasibility assessment for a proposed feature or system.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Constraint Coverage | 25% | How thoroughly timeline, team skill, infrastructure, third-party, and regulatory constraints are analysed |
| 2 | Risk Identification | 25% | Quality and completeness of the risk register, including specific risk types and impact ratings |
| 3 | Spike / PoC Quality | 20% | Rigour of prototyping or research conducted for high-risk components |
| 4 | Component Decomposition | 15% | Granularity and accuracy of the technical breakdown into assessable units |
| 5 | Verdict Clarity | 15% | How clearly and defensibly the go/no-go recommendation is supported by evidence |
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
| A+ | 9.0 – 10.0 | Exceptional | All constraints documented with evidence, risk register with mitigation per item, spike results attached, crystal-clear go/no-go | Approve and proceed to architecture design |
| A | 8.0 – 8.9 | Strong | Minor gaps in 1 constraint dimension, risk register complete, verdict well-supported | Approve with minor caveats noted |
| B | 7.0 – 7.9 | Good | Constraints partially covered, some risks identified without mitigation, verdict supported but shallow | Request targeted additions before final sign-off |
| C | 5.0 – 6.9 | Adequate | Key constraints missing, risk register thin, no spike conducted for high-risk items | Return for supplementary investigation before approval |
| D | 3.0 – 4.9 | Weak | Only obvious constraints documented, risks listed without analysis, verdict unsupported | Reject and require full re-assessment with structured methodology |
| F | 0.0 – 2.9 | Failing | No structured assessment; gut-feel verdict with no evidence | Do not approve; escalate to engineering leadership for oversight |

## Signal Tables

### Constraint Coverage

| Score | Evidence |
|-------|----------|
| 9–10 | All five constraint dimensions documented (timeline, team skills, infrastructure, third-party APIs, regulatory); each with specific measurements or verified data points |
| 7–8 | Four of five dimensions present; one dimension addressed qualitatively without supporting data |
| 5–6 | Two or three dimensions present; timeline and team skill addressed but infrastructure and third-party dependencies absent |
| 3–4 | Only one or two dimensions present; constraints noted in passing without analysis |
| 0–2 | No structured constraint analysis; feature assessed as technically possible without reference to real-world limits |

### Risk Identification

| Score | Evidence |
|-------|----------|
| 9–10 | Risk register with ≥ 3 specific risks per uncertain component; each risk has type (latency/data/API/security), likelihood (H/M/L), impact, and proposed mitigation |
| 7–8 | Risk register with all high-risk components covered; most risks have likelihood and impact; 1–2 missing mitigations |
| 5–6 | Risks listed for major components only; likelihood and impact inconsistently applied; no mitigations |
| 3–4 | Generic risks listed (e.g., "integration may be complex") without specificity; no structure |
| 0–2 | No risk register; risks mentioned informally in prose or absent entirely |

### Spike / PoC Quality

| Score | Evidence |
|-------|----------|
| 9–10 | Time-boxed spike or PoC conducted for all high-risk components; results documented with pass/fail against specific hypotheses; duration recorded |
| 7–8 | Spike conducted for highest-risk component; findings documented; minor questions unresolved |
| 5–6 | Spike attempted but inconclusive; or spike conducted without documented hypotheses to test |
| 3–4 | Vendor docs or blog posts referenced as "research" without hands-on validation |
| 0–2 | No spike or research conducted; high-risk components approved on assumption |

### Component Decomposition

| Score | Evidence |
|-------|----------|
| 9–10 | Feature broken into ≥ 5 independently assessable components; each labelled as well-understood or uncertain; no overlapping responsibilities |
| 7–8 | Feature broken into 3–4 components with clear responsibilities; 1–2 components could be further split |
| 5–6 | Decomposition present but coarse; 1–2 large components contain mixed responsibilities that obscure risk |
| 3–4 | Feature treated as 1–2 monolithic blocks; risks and constraints cannot be traced to specific components |
| 0–2 | No decomposition; assessment covers the feature as a whole without structural breakdown |

### Verdict Clarity

| Score | Evidence |
|-------|----------|
| 9–10 | Verdict explicitly states feasible / feasible-with-caveats / not-feasible; each caveat references a specific constraint or risk; recommendation includes next steps |
| 7–8 | Clear verdict with supporting rationale; caveats present but 1–2 lack direct references to evidence |
| 5–6 | Verdict stated but rationale is general; caveats listed without traceability to risk register |
| 3–4 | Verdict implied rather than stated; reader must infer the recommendation from the body |
| 0–2 | No verdict; assessment ends without a recommendation |
