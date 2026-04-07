# Usability Test Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX Research Lead] |
| Feature Tested | [Feature or prototype name] |
| Prototype Link | [Figma prototype URL] |
| Participants | [X participants] |
| Test Format | [Moderated remote / Unmoderated / In-person] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |

## Executive Summary

[2-3 sentences: overall usability verdict, number of critical findings, headline recommendation. GUIDANCE: e.g. "8 participants completed a 4-task usability test on the checkout prototype. Task completion averaged 74% across all tasks; the payment step has a critical failure rate of 62.5%. Recommend redesigning the payment method selector before development handoff."]

**Overall SUS score**: [X / 100] — [Grade and interpretation]
**Recommendation**: [Proceed to development / Revise and retest / Major redesign required]

## Participants

| ID | Segment | Platform | Experience Level | Completed All Tasks? |
|----|---------|---------|-----------------|---------------------|
| P01 | [Segment] | [iOS / Android / Web] | [Novice / Intermediate / Expert] | [Yes / No] |
| P02 | [Segment] | [Platform] | [Level] | [Yes / No] |
| P03 | [Segment] | [Platform] | [Level] | [Yes / No] |

## Task Results

### Task Completion Summary

| Task # | Task Description | Completed | Partial | Failed | Avg Time (min) | Difficulty Rating (1-7) |
|--------|-----------------|-----------|---------|--------|----------------|------------------------|
| T1 | [e.g. Find and add the blue jacket to cart] | [X/8] | [X/8] | [X/8] | [X:XX] | [X.X] |
| T2 | [e.g. Proceed to checkout and enter your address] | [X/8] | [X/8] | [X/8] | [X:XX] | [X.X] |
| T3 | [e.g. Select a payment method and place the order] | [X/8] | [X/8] | [X/8] | [X:XX] | [X.X] |
| T4 | [e.g. Find your order confirmation] | [X/8] | [X/8] | [X/8] | [X:XX] | [X.X] |

### Task Success Rate Chart (text representation)

```
T1: [████████████████████] 100% (8/8)
T2: [████████████████    ]  75% (6/8)
T3: [████████            ]  38% (3/8) ← CRITICAL
T4: [████████████████████]  88% (7/8)
```

## Findings: Severity 4 (Catastrophic)

### [US-01] [Issue Title]

**Task affected**: Task [#]
**Participants affected**: [X/8]
**Heuristic**: [Nielsen heuristic number and name]

**Observation**:
[Factual description of what participants did — quote or paraphrase think-aloud commentary where possible.]
> "[Direct quote from participant]"

**Root cause**:
[Design element causing the failure — specific and actionable.]

**Recommendation**:
[Specific design change. One recommendation per finding.]

**Priority**: Block — fix before development handoff

---

## Findings: Severity 3 (Major)

### [US-02] [Issue Title]

**Task affected**: Task [#]
**Participants affected**: [X/8]
**Heuristic**: [Heuristic]
**Observation**: [Description]
**Root cause**: [Element]
**Recommendation**: [Fix]
**Priority**: Fix before release

---

## Findings: Severity 2 (Minor)

| ID | Issue | Task | Participants | Heuristic | Recommendation |
|----|-------|------|-------------|-----------|---------------|
| US-03 | [Issue] | T[#] | [X/8] | [#] | [Recommendation] |
| US-04 | [Issue] | T[#] | [X/8] | [#] | [Recommendation] |

## Positive Findings

[Document what worked well — important for preserving effective design decisions under revision pressure.]

| Finding | Task | Participants | Note |
|---------|------|-------------|------|
| [e.g. Order confirmation animation received positive commentary] | T4 | 6/8 | "Keep this — participants mentioned it made them feel confident"] |

## Recommended Actions

| Priority | Action | Addresses | Effort | Owner | Sprint |
|----------|--------|-----------|--------|-------|--------|
| P0 | [e.g. Redesign payment selector — current radio buttons not recognised as interactive] | US-01 | [1.5d] | [Designer] | Sprint [X] |
| P1 | [e.g. Add progress indicator to checkout flow] | US-02 | [0.5d] | [Designer] | Sprint [X] |
| P2 | [e.g. Relabel "Finalise" CTA → "Place order"] | US-03 | [0.5d] | [Content Design] | Sprint [X] |

## SUS Score Breakdown

| Participant | SUS Score |
|------------|-----------|
| P01 | [Score] |
| P02 | [Score] |
| Average | **[Score]** |
