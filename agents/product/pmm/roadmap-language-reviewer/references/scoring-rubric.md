# Scoring Rubric: Roadmap Language Reviewer

Evaluates the external-readiness and positioning alignment of roadmap language across decks, changelogs, and customer-facing materials.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Buyer-Centric Language | 25% | Replacement of engineering jargon with outcome-oriented, persona-relevant language |
| 2 | Positioning Alignment | 25% | Consistency of roadmap item framing with current positioning and messaging hierarchy |
| 3 | Commitment Hygiene | 20% | Appropriate use of forward-looking disclaimers; no unqualified date or scope commitments |
| 4 | Narrative Coherence | 15% | Roadmap tells a strategic story about product direction, not a disconnected feature list |
| 5 | Competitive Sensitivity | 15% | Items that reveal strategic vulnerabilities or implementation details are flagged and reframed |
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
| A+ | 9.0 – 10.0 | Exceptional | All items use buyer language, align with positioning, carry appropriate disclaimers, and tell a coherent story | Approve for external sharing without changes |
| A | 8.0 – 8.9 | Strong | Minor language tweaks needed; overall alignment and commitment hygiene are solid | Approve with tracked minor edits returned to PM |
| B | 7.0 – 7.9 | Good | Most items are buyer-ready but two to three need reframing for positioning alignment or jargon removal | Approve conditionally; edits required before external use |
| C | 5.0 – 6.9 | Adequate | Mix of buyer-ready and engineering-language items; some commitment language is too firm | Return for revision; flag specific items needing rewrite |
| D | 3.0 – 4.9 | Weak | Majority of items use internal jargon; committal language on unconfirmed features; no narrative thread | Return for full rewrite; schedule joint session with PM |
| F | 0.0 – 2.9 | Failing | Roadmap is an internal engineering tracker shared externally without any PMM review | Block external sharing; escalate to product and PMM leadership |

## Signal Tables

### Buyer-Centric Language
| Score | Evidence |
|-------|----------|
| 9-10 | Every item title and description uses buyer outcomes ("Enable teams to X") with no engineering jargon; persona-relevant framing throughout |
| 7-8 | Most items use buyer language; one to two items retain technical terms that could confuse external audiences |
| 5-6 | Roughly half the items are buyer-ready; the other half use implementation language ("refactor X service", "migrate to Y") |
| 3-4 | Majority of items are engineering-oriented with occasional buyer-friendly titles |
| 0-2 | Entire roadmap uses internal engineering language with no buyer translation |

### Positioning Alignment
| Score | Evidence |
|-------|----------|
| 9-10 | Every roadmap item reinforces current differentiation pillars; messaging hierarchy themes are reflected in item framing |
| 7-8 | Most items align with positioning; one to two items frame capabilities in a way that does not connect to current differentiation |
| 5-6 | Some items align; others introduce framing that contradicts or dilutes positioning (e.g., emphasising a non-differentiating capability) |
| 3-4 | Roadmap framing bears little relation to the positioning document; appears written independently |
| 0-2 | Roadmap items actively contradict current positioning or position the product in a different category |

### Commitment Hygiene
| Score | Evidence |
|-------|----------|
| 9-10 | All unconfirmed items use "planned", "exploring", or "under consideration"; no specific dates for unshipped features; standard disclaimer present |
| 7-8 | Most items appropriately qualified; one to two items use language that could be interpreted as a commitment |
| 5-6 | Several items imply firm delivery dates or scope without qualification |
| 3-4 | Multiple items make date-specific or scope-specific promises on unconfirmed features |
| 0-2 | Roadmap reads as a binding delivery schedule with no forward-looking disclaimers |

### Narrative Coherence
| Score | Evidence |
|-------|----------|
| 9-10 | Roadmap items are sequenced to tell a strategic story; themes are grouped; the overall trajectory reinforces product vision |
| 7-8 | Clear thematic grouping; narrative thread visible but could be stronger in transitions between themes |
| 5-6 | Items grouped by quarter but no narrative connecting them; reads as a prioritised backlog |
| 3-4 | Random ordering; no thematic grouping; each item is isolated from the next |
| 0-2 | Flat list of engineering tasks with no attempt at strategic framing |

### Competitive Sensitivity
| Score | Evidence |
|-------|----------|
| 9-10 | All items reviewed for competitive exposure; items that could reveal strategy are reframed; no implementation details leaked |
| 7-8 | Most items reviewed; one item could benefit from reframing to avoid revealing a competitive gap |
| 5-6 | Some items inadvertently reveal that a competitor has a capability you lack; not flagged |
| 3-4 | Multiple items expose strategic weaknesses or implementation approach to competitors |
| 0-2 | Roadmap openly reveals competitive gaps, infrastructure limitations, or strategic pivots |
