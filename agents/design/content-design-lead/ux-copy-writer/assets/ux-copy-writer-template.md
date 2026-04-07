# UX Copy Deck

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Content Design Lead name] |
| Version | [1.0] |
| Status | [Draft / Design Review / Engineering Ready / Approved] |
| Skill | ux-copy-writer |
| Feature / Flow | [Name of the feature or user flow] |
| Design File Link | [Figma or equivalent link] |
| Content Design Spec Version | [Link to spec version used as reference] |

## Executive Summary

[2-3 sentences: how many copy strings were produced, any voice/tone decisions made for this feature that extend the spec, and whether this deck is ready for design handoff.]

GUIDANCE: Example — "44 copy strings were produced for the onboarding flow, covering 7 screens from sign-up to first project creation. The tone in the celebration screen intentionally skews warmer than standard confirmation copy — this has been noted in the annotations and should be reviewed against the spec. The deck is ready for design annotation and engineering handoff."

## Copy Context Brief

[Context gathered before writing. This section justifies copy decisions — reviewers should understand why each choice was made.]

**User goal at this step**: [What the user is trying to accomplish]
**User emotional state**: [Anxious / Neutral / Excited / Task-focused — context matters for tone]
**Key constraints**: [Character limits, space constraints, technical limitations]
**Spec version reference**: [Which sections of the content design spec govern this copy]

## Copy Strings by Screen

[One section per screen or component. Order by user flow.]

GUIDANCE: Good — each string has its element type, the copy, tone rationale, and implementation notes. Bad — strings listed without context or annotation. Engineers should not have to guess why copy says what it says.

---

### [Screen 1: Screen Name]

**Screen context**: [What the user sees and is doing here]

| # | Element Type | Copy | Tone Note | Implementation Note |
|---|-------------|------|-----------|-------------------|
| 1 | Page heading | "[Heading text]" | [e.g., "Neutral — task-focused"] | — |
| 2 | Body copy | "[Body text]" | | |
| 3 | Primary button | "[Button label]" | | |
| 4 | Secondary button | "[Button label]" | | |
| 5 | [Error — required field] | "[Error message]" | Empathetic | aria-describedby on input |
| 6 | [Empty state] | "[Empty state message]" + "[CTA]" | Inviting | |

---

### [Screen 2: Screen Name]

[Same structure]

---

### [Component: Component Name]

[For reusable components that appear across multiple screens]

| # | Element Type | Copy | Tone Note | Implementation Note |
|---|-------------|------|-----------|-------------------|
| 1 | | | | |

## Variable and Pluralisation Reference

[Document all dynamic copy strings — variables and pluralisation rules engineers need to implement correctly.]

GUIDANCE: Every [variable] placeholder must be defined here. Every count-dependent string must have rules for 0, 1, and 2+ values.

| String # | Variable | Possible Values | Copy Variations |
|---------|---------|----------------|----------------|
| [#] | [user_name] | First name, or "you" if name unavailable | "Welcome, [name]" / "Welcome" |
| [#] | [item_count] | 0, 1, 2+ | 0: "No tasks yet"; 1: "1 task"; 2+: "[N] tasks" |

## Deferred Strings

[Copy strings that cannot be finalised yet due to unresolved design or product decisions.]

GUIDANCE: List what is blocked and why. Do not ship placeholder text — flag these as dependencies.

| String # | Element | Blocker | Placeholder (interim) | Owner |
|---------|---------|---------|----------------------|-------|
| [#] | [Element type] | [What decision is missing] | "[Temporary placeholder]" | [Name] |

## Appendices

### A. Spec Deviations

[Any copy decisions in this deck that diverge from the content design spec, with rationale.]

| String # | Deviation | Rationale | Approved By |
|---------|---------|----------|------------|
| [#] | [How it differs from spec] | [Why this exception is justified] | [Name] |

### B. Rejected Alternatives

[Alternative copy considered and rejected, with brief reasoning. Useful for review discussions.]

| String # | Alternative Considered | Reason Rejected |
|---------|----------------------|----------------|
| [#] | "[Alternative text]" | [Why the approved version was chosen] |
