# Technical Feasibility Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | technical-feasibility-check |
| Feature / System | [Name of proposed feature or system] |
| Requested By | [Product owner / stakeholder name] |
| Decision Deadline | [Date by which go/no-go is needed] |

## Executive Summary

[2–3 sentences stating the verdict (feasible / feasible-with-caveats / not-feasible) and the primary reasons. Lead with the recommendation, not the methodology.

GUIDANCE: Good — "The real-time collaboration feature is feasible with caveats: WebSocket infrastructure requires new deployment configuration (2-week spike needed) and third-party presence API costs exceed current budget at scale." Bad — "We investigated the feature and looked at various constraints and risks."]

## Verdict

**Recommendation**: [ FEASIBLE | FEASIBLE WITH CAVEATS | NOT FEASIBLE ]

| Caveat # | Description | Blocking? | Resolution Path |
|----------|-------------|-----------|-----------------|
| 1 | [Specific caveat] | [Yes/No] | [How to resolve] |
| 2 | [Specific caveat] | [Yes/No] | [How to resolve] |

GUIDANCE: Blocking caveats must be resolved before sprint commitment. Non-blocking caveats should appear in the project risk register.

## Component Breakdown

[Table of every technical component with its uncertainty classification.]

| Component | Description | Certainty | Risk Level |
|-----------|-------------|-----------|------------|
| [e.g., Auth integration] | [What it does] | Well-understood / Uncertain | Low / Medium / High |
| [e.g., Real-time sync engine] | [What it does] | Well-understood / Uncertain | Low / Medium / High |

GUIDANCE: Good — 5+ components with distinct responsibilities, each independently assessable. Bad — "Frontend and backend" as two components.

## Constraint Matrix

[Assessment of all constraint dimensions against the feature requirements.]

| Constraint Dimension | Current State | Requirement | Gap | Severity |
|---------------------|---------------|-------------|-----|----------|
| Timeline | [Available weeks] | [Estimated weeks] | [Delta] | [None/Low/High] |
| Team Skills | [Available expertise] | [Required expertise] | [Gap description] | [None/Low/High] |
| Infrastructure | [Current capacity] | [Required capacity] | [Delta] | [None/Low/High] |
| Third-Party Dependencies | [Available APIs/services] | [Required APIs/services] | [Gap description] | [None/Low/High] |
| Regulatory / Compliance | [Current compliance posture] | [Requirements] | [Gap description] | [None/Low/High] |

GUIDANCE: Every row must have a specific measurement or verified data point. Avoid "TBD" — if unknown, that IS the gap.

## Risk Register

| # | Risk | Component | Type | Likelihood | Impact | Mitigation |
|---|------|-----------|------|------------|--------|------------|
| R1 | [Specific risk] | [Component] | Latency/API/Data/Security/Skills | H/M/L | H/M/L | [Action to reduce risk] |
| R2 | [Specific risk] | [Component] | Latency/API/Data/Security/Skills | H/M/L | H/M/L | [Action to reduce risk] |

GUIDANCE: Good — "Third-party rate limits of 100 req/min will be exceeded at projected load of 500 concurrent users — mitigate by batching and caching." Bad — "API integration may be complex."

## Spike Findings

[Results of any time-boxed prototyping or research conducted for high-risk components.]

| Component | Spike Objective | Duration | Result | Conclusion |
|-----------|-----------------|----------|--------|------------|
| [Component name] | [Hypothesis tested] | [Hours/days] | [Pass/Fail/Partial] | [What was learned] |

GUIDANCE: Include this section only if spikes were conducted. If no spike was feasible, document why and what assumption is being made instead.

## Recommendations

[Prioritized actions following from this assessment.]

**P1 — Required before sprint commitment:**
- [Specific action, owner, deadline]

**P2 — Required during sprint:**
- [Specific action, owner, checkpoint]

**P3 — Recommended before launch:**
- [Specific action, owner]

## Appendices

### A. Methodology

Assessment conducted using the `technical-feasibility-check` skill. Scoring applied against rubric at `references/scoring-rubric.md`. Spike methodology: time-boxed investigation with pre-defined hypotheses and documented outcomes.

### B. Supporting Data

[Attach: API documentation reviewed, PoC code links, vendor quotes, benchmark results, relevant architecture diagrams]
