# Framework: iteration-prioritiser-f

Defines the prioritisation methodology for ranking feedback-phase iteration items based on user impact, engineering effort, and product goal alignment.

## Feedback Categorization

Before scoring, classify every feedback item into exactly one category:

| Category | Definition | Example |
|----------|-----------|---------|
| **Bug** | Functionality deviates from accepted acceptance criteria | "Submit button does not respond on iOS Safari" |
| **Usability Issue** | Functionality works but UX creates friction or confusion | "Users cannot find the export feature without prompting" |
| **Missing Feature** | Capability that was in scope but not delivered | "Filter by date range was in the spec but not built" |
| **Enhancement** | New capability not in the original scope | "Users want CSV export in addition to PDF" |

Bugs and missing features from the accepted spec are prioritised by default over enhancements and usability issues.

## Impact-Effort Scoring Matrix

### Impact Score (1–10)

| Score | Definition | Signals |
|-------|-----------|---------|
| 9–10 | Blocks core user flow or revenue path | Cannot complete primary use case; affects > 50% of beta users |
| 7–8 | Significantly degrades key workflow | Requires a workaround; affects 20–50% of users |
| 5–6 | Noticeable friction but workable | Affects < 20% of users; workaround exists and is simple |
| 3–4 | Minor annoyance | Affects edge cases or power users only; no workaround needed |
| 1–2 | Cosmetic or preference-based | Would be nice; no measurable impact on task completion |

### Effort Score (1–10)

| Score | Definition | Engineering Signals |
|-------|-----------|-------------------|
| 9–10 | > 2 weeks of engineering work | Requires architectural change, new infrastructure, or cross-team coordination |
| 7–8 | 1–2 weeks | Multiple services affected, significant testing required |
| 5–6 | 3–5 days | Single service, isolated change, regression risk manageable |
| 3–4 | 1–3 days | Small code change, well-understood area, low regression risk |
| 1–2 | Hours | Config change, copy fix, single-line code change |

### Priority Score Formula

```
Priority Score = Impact Score / Effort Score
```

Items are ranked by priority score (higher = address first). This is the impact-effort ratio — high-impact/low-effort items score highest.

### Priority Quadrant Classification

| Quadrant | Impact | Effort | Action |
|----------|--------|--------|--------|
| Quick Win | High (≥7) | Low (≤4) | Do in current iteration |
| Major Effort | High (≥7) | High (≥7) | Plan for dedicated iteration |
| Fill-In | Low (≤4) | Low (≤4) | Include when capacity allows |
| Avoid | Low (≤4) | High (≥7) | Defer indefinitely or reject |

## Milestone Adjustment Factor

After scoring, apply milestone adjustments to the final ranking:

| Condition | Adjustment |
|-----------|-----------|
| Item is a beta exit criterion | Elevate to P1 regardless of score |
| Item was promised in writing to a reference customer | Elevate by one priority tier |
| Item is a security or data privacy issue | Elevate to P1 regardless of score |
| Item conflicts with the upcoming GA feature scope | Defer to post-GA backlog |

## Iteration Capacity Planning

| Metric | How to Calculate |
|--------|----------------|
| Available capacity | Team size × sprint days × 0.7 (30% overhead for reviews, meetings, unplanned work) |
| Item effort in days | Effort Score: 1–2 = 0.5 days, 3–4 = 2 days, 5–6 = 4 days, 7–8 = 8 days, 9–10 = 14 days |
| Max items per iteration | Sum item effort days until available capacity is reached; stop there |

## Iteration Planning Checklist

- [ ] All feedback items collected and deduplicated
- [ ] Every item categorized (Bug / Usability / Missing Feature / Enhancement)
- [ ] Impact and effort scored with engineering input on effort
- [ ] Priority score calculated and items sorted
- [ ] Milestone adjustments applied
- [ ] Iteration scope selected within capacity
- [ ] Acceptance criteria written for selected items
- [ ] Rationale communicated for items deferred
