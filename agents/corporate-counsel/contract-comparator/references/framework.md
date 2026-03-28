# Comparison Framework: contract-comparator

Methodology for aligning, comparing, and scoring contract differences.

## Clause Alignment Algorithm

Clauses are aligned between two documents using a three-pass approach, in priority order:

### Pass 1: Heading Match
- Match clauses with identical or near-identical section headings
- Normalize headings: strip numbering, lowercase, remove articles
- Confidence: High (90%+) when headings match exactly

### Pass 2: Content Similarity
- For unmatched clauses, compare content using key legal phrase matching
- Match clauses sharing 60%+ of substantive legal phrases (excluding boilerplate connectors)
- Confidence: Medium (70-89%) based on phrase overlap percentage

### Pass 3: Taxonomy Position
- For remaining unmatched clauses, map to the standard clause taxonomy
- Match clauses assigned to the same taxonomy category
- Confidence: Low (50-69%) — flag for manual verification

### Unmatched Clauses
- Clauses in Version A with no match in Version B: classified as **Deletions**
- Clauses in Version B with no match in Version A: classified as **Additions**
- Both carry automatic "Review Required" flags

## Favorability Scoring

Each difference is scored on a three-point scale:

| Score | Label | Definition | Example |
|-------|-------|------------|---------|
| +1 | Favorable | Change shifts risk, obligation, or cost to the counterparty or grants the company additional rights | Liability cap reduced from 24 months to 12 months of fees |
| 0 | Neutral | Change has no material impact on either party's position | "Thirty (30) days" changed to "30 days" |
| -1 | Unfavorable | Change shifts risk, obligation, or cost to the company or removes company rights | Termination for convenience removed; only for-cause termination remains |

## Deviation Severity Classification

| Severity | Definition | Weight | Examples |
|----------|------------|--------|----------|
| Critical | Change fundamentally alters risk allocation, creates new liability exposure, or removes essential protections | 3x | Removing liability cap, adding unlimited indemnification, eliminating termination rights |
| Material | Change meaningfully affects commercial terms, operational obligations, or legal position | 2x | Shortening cure period from 30 to 10 days, adding audit obligations, changing governing law |
| Minor | Change affects form, process, or non-material terms | 1x | Changing notice address, adjusting formatting, minor definitional clarifications |

## Net Favorability Calculation

```
Net Score = Σ (favorability score × severity weight) for all differences

Interpretation:
  > +5:   Strongly favorable — counterparty conceded significantly
  +1 to +5: Moderately favorable — net position improved
  0:       Neutral — changes balance out
  -1 to -5: Moderately unfavorable — net position weakened
  < -5:    Strongly unfavorable — significant concessions to counterparty
```

## Comparison Output Categories

For each aligned clause pair, the comparison produces:

1. **Clause reference**: Section numbers from both versions
2. **Your version**: Full text from Version A (company standard or prior version)
3. **Their version**: Full text from Version B (counterparty version or current version)
4. **Change type**: Addition / Deletion / Modification
5. **Favorability**: Favorable / Neutral / Unfavorable
6. **Severity**: Critical / Material / Minor
7. **Impact summary**: One sentence describing what the change means for the company
8. **Recommendation**: Accept / Negotiate / Reject with rationale
