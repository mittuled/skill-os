# Thematic Analysis Framework

## Purpose

A structured reference for synthesising qualitative user feedback into credible, actionable themes using established qualitative research methods.

## Coding Approaches

### Open Coding (Grounded Theory)
Generate codes directly from raw data without imposing a pre-existing framework:
- Read each feedback entry in full before applying any code
- Use short, descriptive labels (2–5 words)
- Prefer in-vivo codes (participant's own language) where possible
- Apply multiple codes to a single entry if it contains distinct ideas
- Do not interpret at this stage — describe only

### Axial Coding
Connect open codes into higher-order categories:
- Group codes that describe the same phenomenon
- Name the category by its defining characteristic, not by a single code
- Look for relationships: cause–effect, context–consequence, condition–strategy

### Selective Coding
Identify the central theme(s) that integrate all categories:
- One to three core themes per synthesis pass
- Each core theme must be supported by at least 3 independent participants or sources
- State each core theme as a declarative sentence: "Users feel [X] when [Y] because [Z]"

---

## Affinity Diagramming Decision Table

| Situation | Action |
|-----------|--------|
| Two clusters describe the same user goal from different angles | Merge — use the broader goal as the theme name |
| One cluster has 15+ items but spans unrelated contexts | Split by context (e.g., "navigation confusion — mobile" vs. "navigation confusion — onboarding") |
| A cluster has only 1–2 items | Hold in "orphan" pile; revisit after full coding |
| A cluster's name only describes a feature, not a user experience | Rename to describe the user's reaction or need (e.g., not "filter UI" → "users cannot find filters") |
| Themes from different sources contradict each other | Preserve both as distinct findings; note the source divergence explicitly |

---

## Theme Validity Checklist

Before finalising a theme, verify:

- [ ] Supported by 3+ independent data points (different participants or sources)
- [ ] Named with user-centred language (describes what users experience, not what the product does)
- [ ] Has at least 2 representative verbatim quotes
- [ ] Frequency count documented (how many items coded to this theme)
- [ ] Intensity rating noted (see scale below)
- [ ] Design implication drafted (what should change, and for whom)

---

## Intensity Scale

Rate each theme by user intensity, separate from frequency:

| Level | Label | Description |
|-------|-------|-------------|
| 1 | Mild friction | Users notice but continue without interruption |
| 2 | Moderate friction | Users pause, backtrack, or express frustration |
| 3 | Significant friction | Users fail the task or seek external help |
| 4 | Critical friction | Users cannot complete a core goal; some abandon |
| 5 | Blocking | Users cannot use the product at all for the intended purpose |

---

## Priority Matrix: Frequency vs. Intensity

Use this matrix to guide design prioritisation recommendations:

| | Low Intensity (1–2) | High Intensity (3–5) |
|---|---|---|
| **High Frequency** | Polish backlog — schedule for incremental improvement | P1 — fix in next sprint |
| **Low Frequency** | Observation — monitor for growth | P2 — investigate; may affect a critical segment |

---

## Cross-Source Triangulation

A finding gains credibility when it appears across multiple independent source types:

| Sources Corroborating | Credibility Level | Recommendation |
|-----------------------|-------------------|----------------|
| 1 source type only | Hypothesis | Do not act without corroboration; recommend follow-up study |
| 2 source types | Moderate | Include in synthesis with source caveat |
| 3+ source types | Strong | Treat as validated finding; recommend design action |

---

## Common Synthesis Biases to Avoid

| Bias | Description | Mitigation |
|------|-------------|------------|
| Confirmation bias | Coding data to support existing product hypotheses | Code with a second reviewer; use blind coding for first pass |
| Recency bias | Over-weighting recent feedback | Review feedback over a defined window (e.g., 90 days); date-stamp all items |
| Salience bias | Memorable stories weighting more than frequency suggests | Track frequency counts; do not rely on recall |
| Outlier suppression | Ignoring low-frequency findings that contradict the main narrative | Document all themes, including minority ones; flag divergence |
| Single-source over-reliance | Drawing conclusions from only one feedback channel | Cross-check any single-source theme with at least one other channel |
