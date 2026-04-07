# Framework: developer-feedback-synthesiser

Defines the feedback normalization model, affinity mapping protocol, impact-feasibility scoring matrix, and synthesis report structure for consolidating developer feedback into actionable product improvements.

## Feedback Source Inventory

| Source | Developer Segment Skew | Update Frequency | Signal Type | Priority for Synthesis |
|--------|----------------------|-----------------|------------|----------------------|
| Support tickets | All — skewed toward blocked users | Weekly | Pain points, bugs | High |
| Community forum (forum.co / Discord) | Active users, enthusiasts | Daily | Feature requests, docs gaps, use cases | High |
| NPS survey (open-text) | Representative sample | Monthly/quarterly | Sentiment, themes | High |
| User interviews | Qualitative, selected | Per interview | Strategic insights, churn reasons | Very High |
| GitHub issues | Technical users, contributors | Real-time | Bugs, missing features, migration friction | High |
| Social media mentions | Broad, public | Real-time | Sentiment signals, competitive mentions | Medium |
| App store reviews | End users (if applicable) | Weekly | Broad sentiment, UX issues | Medium |
| Sales call notes (CRM) | Prospective / evaluating | Per call | Deal-blocking gaps, competitive objections | High |

## Normalization Protocol

Normalize all feedback to a common schema before analysis. This prevents source bias and enables cross-channel comparison.

**Required fields per feedback item:**

| Field | Values | Notes |
|-------|--------|-------|
| ID | Unique identifier | For deduplication tracking |
| Source | Channel name | From source inventory |
| Date | YYYY-MM-DD | Original feedback date |
| Developer Segment | Hobbyist / Startup / SMB / Enterprise / Unknown | From account data or context |
| Product Area | API / SDK / Docs / Onboarding / Billing / Platform | Primary area affected |
| Category | Bug / Feature Request / Docs Gap / UX Issue / Performance / Praise | From taxonomy |
| Sentiment | Positive / Neutral / Negative | Based on tone |
| Severity (raw) | Blocking / Significant / Minor | Developer's expressed urgency |
| Summary | 1-sentence description | Normalized phrasing |
| Verbatim | Original quote | Preserved for reference |
| Duplicate of | ID of parent signal | If duplicate |

## Affinity Mapping Protocol

1. **Group by semantic overlap** — items with > 60% overlap in problem description form a cluster
2. **Name the theme** after the underlying need, not the symptom (e.g., "Developers cannot debug auth failures" not "401 error complaints")
3. **Quantify**: count unique sources, total mentions, segment distribution
4. **Sort by business weight**:
   - Enterprise weight: 3× individual developer
   - SMB weight: 2×
   - Startup weight: 1.5×
   - Hobbyist: 1×
5. **Flag persistent themes**: issues appearing in 3+ consecutive synthesis cycles are escalated to "chronic" status

## Impact-Feasibility Matrix

Score each theme on two dimensions to generate a priority ranking.

### Business Impact Score (1–10)

| Score | Criteria |
|-------|---------|
| 9–10 | Blocks enterprise revenue, affects > 20% of active developers, or causes churn |
| 7–8 | Slows adoption for a key segment, affects 10–20% of developers, or surfaces in sales deals |
| 5–6 | Common friction but workaround exists; affects 5–10% of developers |
| 3–4 | Edge case; affects < 5% of developers; infrequent reports |
| 1–2 | Nice-to-have; single mention; no revenue or retention impact |

### Implementation Feasibility Score (1–10)

| Score | Criteria |
|-------|---------|
| 9–10 | < 1 week engineering effort; no external dependencies; no breaking changes |
| 7–8 | 1–3 week effort; minor refactoring; no breaking changes |
| 5–6 | 1–2 sprint effort; moderate complexity; may require design review |
| 3–4 | > 2 sprint effort; significant architecture changes or cross-team dependencies |
| 1–2 | Quarter+ effort; platform constraints; requires third-party changes |

### Priority Quadrants

| Quadrant | Impact | Feasibility | Action |
|----------|--------|------------|--------|
| Quick Win | High | High | Ship in current sprint |
| Strategic Bet | High | Low | Plan for next major release |
| Backlog Filler | Low | High | Add to backlog for opportunistic work |
| Deprioritize | Low | Low | Monitor; do not invest resources |

## Recommendation Format

Each synthesis report recommendation must follow this structure:

```
[THEME NAME] — Impact: [score]/10, Feasibility: [score]/10
Problem: [One sentence describing the developer experience failure]
Evidence: [N] mentions, [N] unique developers, [segment distribution]
Recommended action: [Specific product/docs/engineering change]
Expected outcome: [Metric improvement — activation, support ticket reduction, etc.]
Owner: [Product / Engineering / Docs / DevRel]
```
