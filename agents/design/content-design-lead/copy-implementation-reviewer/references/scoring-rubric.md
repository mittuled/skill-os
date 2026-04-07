# Scoring Rubric: copy-implementation-reviewer

Evaluates the conformance of implemented product copy against the content design specification, across voice, terminology, pattern adherence, and accessibility.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Voice and Tone Conformance | 30% | Degree to which implemented copy matches the voice attributes and tone modulation rules defined in the content design spec |
| 2 | Terminology Accuracy | 25% | Use of approved terminology from the glossary; absence of deprecated or inconsistent terms |
| 3 | Copy Pattern Adherence | 25% | Conformance to documented copy patterns for buttons, errors, empty states, confirmations, and notifications |
| 4 | Accessibility Copy | 10% | Quality of alt text, ARIA labels, screen-reader link text, and error message association |
| 5 | Grammar and Mechanics | 10% | Adherence to capitalisation, punctuation, number formatting, and abbreviation rules |
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
| A+ | 9.0 – 10.0 | Exceptional | Zero critical/major deviations; voice is consistent throughout; all accessible copy patterns implemented correctly | Ship; no copy corrections needed |
| A | 8.0 – 8.9 | Strong | 0-2 minor deviations; all core patterns correct; voice consistent; 1 accessibility gap at most | File minor corrections as low-priority tickets; ship |
| B | 7.0 – 7.9 | Good | 3-5 deviations, all minor; or 1 major deviation in a low-traffic area | File corrections; ship with plan to resolve before next sprint |
| C | 5.0 – 6.9 | Adequate | 1-2 major deviations OR multiple minor deviations across a single surface (e.g., all error messages wrong) | Hold on shipping the affected surface until corrections are made |
| D | 3.0 – 4.9 | Weak | 3+ major deviations; core user-facing copy does not match approved spec; multiple missing empty states | Do not ship; return to design and re-implement with copy review in process |
| F | 0.0 – 2.9 | Failing | Critical deviation: copy conveys wrong meaning, creates user confusion, or violates accessibility compliance | Block release; escalate to Content Design Lead and PM |

## Signal Tables

### Voice and Tone Conformance

| Score | Evidence |
|-------|----------|
| 9-10 | All copy strings match the voice attribute spectrum; tone modulates correctly between contexts (celebratory for success, empathetic for errors, neutral for settings); no instances of off-brand phrasing |
| 7-8 | 90%+ of copy matches voice spec; 1-2 instances of wrong tone for context (e.g., overly formal in an onboarding celebration); no copy that contradicts brand values |
| 5-6 | Majority of copy is voice-consistent but 10-20% feels generic, developer-written, or out of character; error messages particularly inconsistent with empathy guidelines |
| 3-4 | Voice is inconsistent across screens in the same feature; some copy is placeholder text (lorem ipsum, "TODO", "untitled") that shipped; tone does not modulate by context |
| 0-2 | Copy throughout is developer-written, technical, or contradicts the brand voice; significant placeholder text shipped to production |

### Terminology Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | All product terms match the approved glossary exactly including capitalisation; no deprecated terms in use; terminology consistent across the entire feature scope |
| 7-8 | Approved terms used correctly in 95%+ of instances; 1-2 minor capitalisation inconsistencies; no deprecated terms |
| 5-6 | 80-94% terminology correct; 1 deprecated term still in use; inconsistent capitalisation across the feature (e.g., "Workspace" and "workspace" used interchangeably) |
| 3-4 | Multiple deprecated or inconsistent terms used; a core product concept referred to by two different names within the same feature; user would be confused about terminology |
| 0-2 | Terminology is entirely inconsistent with the glossary; developer-coined names for features that contradict the approved naming; same concept has 3+ names in the UI |

### Copy Pattern Adherence

| Score | Evidence |
|-------|----------|
| 9-10 | All button labels, error messages, empty states, confirmations, and loading states follow documented patterns; no invented patterns that deviate from the pattern library |
| 7-8 | 90%+ of patterns correctly implemented; 1 pattern missing (e.g., an empty state uses a generic message instead of the task-oriented pattern) |
| 5-6 | Core patterns implemented; 2-3 missing or incorrect (e.g., destructive confirmation has no "this cannot be undone" warning); button labels mix pattern styles |
| 3-4 | Only 50-70% of pattern types implemented; error messages are all generic "Something went wrong"; empty states are missing or use "No [items]" defaults |
| 0-2 | No evidence that the pattern library was consulted; all error messages are developer-written; empty states absent; buttons use inconsistent label formats |

### Accessibility Copy

| Score | Evidence |
|-------|----------|
| 9-10 | All images have descriptive alt text following the spec's formula; ARIA labels on all interactive elements without visible text; error messages are programmatically associated with inputs; link text is descriptive (not "click here") |
| 7-8 | Alt text present on all content images; 1-2 decorative images not correctly marked as aria-hidden; most ARIA labels present; no "click here" link text |
| 5-6 | Alt text present on 75-90% of images; some ARIA labels missing on icon-only buttons; 1-2 error messages not associated with their inputs |
| 3-4 | Alt text missing on 25-50% of images; multiple icon buttons without accessible labels; several error messages not programmatically linked to inputs |
| 0-2 | No alt text implementation; no ARIA labels on interactive elements; error messages not associated with inputs; link text consists entirely of "click here" or URLs |

### Grammar and Mechanics

| Score | Evidence |
|-------|----------|
| 9-10 | Sentence case applied consistently where specified; no trailing punctuation on button labels; number formatting consistent; no abbreviations outside the approved list |
| 7-8 | 1-2 title-case errors where sentence case is required; punctuation correct on 95%+ of strings; number formatting consistent |
| 5-6 | Inconsistent capitalisation across a surface; some button labels have trailing periods; number formatting varies (e.g., "5 items" and "5items" mixed) |
| 3-4 | Title case and sentence case mixed without pattern throughout; multiple punctuation errors including trailing periods on non-sentence copy; abbreviations not in approved list |
| 0-2 | No discernible capitalisation convention; punctuation inconsistent throughout; numbers and dates formatted inconsistently; all-caps used where not specified |
