# Design Feasibility Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | design-feasibility-reviewer |
| Design Title | [Name of design / mockup] |
| Design Version | [Figma / Sketch file version] |
| Review Stage | [Wireframe / High-fidelity / Pixel-perfect] |
| Sprint Target | [Sprint number or date] |

## Executive Summary

[2–3 sentences covering overall feasibility verdict, the most significant infeasible or modified component, and any performance risk.

GUIDANCE: Good — "The checkout redesign is largely feasible; the animated cart-item transition requires a CSS-only fallback on Android 10 and below, and the real-time stock-count polling will increase API load by 40x at peak — both have documented mitigations." Bad — "We reviewed the designs and found some issues."]

## Feasibility Summary

| Component | Verdict | Effort | Notes |
|-----------|---------|--------|-------|
| [Component name] | Feasible / Modified / Infeasible | [XS/S/M/L/XL] | [One-line note] |

GUIDANCE: Populate one row per component identified in decomposition. "Modified" = achievable with specified design changes. "Infeasible" = cannot be built within stated constraints.

## Component Assessments

### [Component 1 Name]

**Technical Description**: [What this component requires technically]

**Constraint Analysis**:

| Constraint | Current State | Requirement | Gap |
|------------|---------------|-------------|-----|
| [e.g., API data availability] | [What exists] | [What design needs] | [Delta / None] |
| [e.g., Latency budget] | [Current p99] | [Design requires] | [Delta / None] |

**Verdict**: [ Feasible | Feasible with Modifications | Infeasible ]

**Alternative (if Modified or Infeasible)**: [Specific design change that achieves the user intent within constraints]

**Effort Estimate**: [Story points or day range]

**Performance Note**: [Any performance impact to flag, or "None"]

---

### [Component 2 Name]

[Repeat structure for each component]

GUIDANCE: Include at least 4–6 component sections for a standard screen design. Break animations, data-loading, state management, and platform-specific behaviors into separate components.

## Effort-Value Analysis

[Flags for components where engineering effort is disproportionate to user value.]

| Component | Effort | User Value | Recommendation |
|-----------|--------|------------|----------------|
| [Component] | [Days] | [High/Med/Low] | Build / Defer / Descope |

GUIDANCE: Any component estimated > 5 days must appear in this table. Include a rationale for the recommendation — e.g., "Defer: complex animation adds delight but does not affect conversion; revisit in Q3."

## Recommendations

**P1 — Must resolve before sprint commitment:**
- [Specific design change or decision needed, with owner]

**P2 — Address during sprint:**
- [Engineering decisions to be made during implementation]

**P3 — Consider for future iteration:**
- [Low-priority design improvements or performance enhancements]

## Appendices

### A. Methodology

Review conducted using `design-feasibility-reviewer` skill. Scoring applied against rubric at `references/scoring-rubric.md`. Constraints verified against: [list actual systems checked — e.g., API docs v2.3, device testing on Samsung A52, React Native 0.72 release notes].

### B. Design Artifacts Referenced

[Links to Figma files, wireframes, prototype URLs, interaction specs]

### C. Technical Reference Data

[API response samples, latency measurements, device benchmark results that support constraint claims]
