# Framework: Sales Signal Synthesis

## Purpose

Provides the methodology for aggregating, analyzing, and converting raw sales signals into actionable themes with revenue-weighted prioritization.

## Signal Aggregation Method

### Data Sources

| Source | Signal Types | Extraction Method |
|--------|-------------|-------------------|
| CRM signal entries | Objections, competitors, triggers, blockers | Export tagged signals for analysis period |
| Call recordings (Gong/Chorus) | Verbatim buyer statements, tone, context | Keyword search + manual review of flagged calls |
| CRM loss reasons | Primary and secondary loss reasons | Export closed-lost deals with reason codes |
| Slack #sales channel | Anecdotal signals, rep frustrations, pattern observations | Keyword search for objection/competitor/feature terms |
| Rep 1:1 notes | Qualitative themes, emerging patterns | Sales Manager provides aggregated notes |

### Filtering Criteria

- **Minimum frequency**: Signal must appear in 3+ deals to qualify as a theme
- **Recency**: Prioritize signals from the last 2 quarters; older signals carry less weight
- **Deal stage**: Separate signals by stage (discovery vs. negotiation signals have different implications)
- **Outcome correlation**: Flag signals that appear disproportionately in closed-lost vs. closed-won

## Theme Extraction Method

### Step 1: Group by Type

| Signal Type | Downstream Owner | Action Category |
|------------|-----------------|-----------------|
| Objections | Sales Management | Update objection handler, refine talk tracks |
| Competitive mentions | Sales + Marketing | Update battle cards, adjust positioning |
| Feature requests | Product | Evaluate for roadmap, document workarounds |
| Buying triggers | Sales + Marketing | Optimize outreach timing, refine targeting |
| Deal blockers | Cross-functional | Remove blockers, adjust qualification criteria |

### Step 2: Identify Themes Within Types

For each signal type, cluster related signals into themes:
- **Affinity grouping**: Signals that describe the same underlying concern in different words
- **Root cause analysis**: Multiple surface signals may share one root cause (e.g., "too expensive" and "can't justify ROI" may both stem from weak value articulation)
- **Stage clustering**: Same theme at different stages may require different interventions

### Step 3: Rank by Impact

For each theme, calculate:

**Revenue-Weighted Priority Score** = (Pipeline Value Affected x Win Rate Delta) / Number of Themes

Where:
- **Pipeline Value Affected** = Sum of pipeline value for deals where the theme appeared
- **Win Rate Delta** = Win rate for deals without this theme minus win rate for deals with this theme

## Impact Scoring Method

### Quantitative Metrics Per Theme

| Metric | How to Calculate | Why It Matters |
|--------|-----------------|----------------|
| Frequency | Count of deals where theme appeared | Validates it is a pattern, not an outlier |
| Pipeline value | Sum of ACV for affected deals | Quantifies revenue at risk |
| Win rate impact | Win rate with theme vs. without | Shows correlation with deal outcome |
| Stage impact | Average stage where theme appears | Indicates when intervention is needed |
| Cycle impact | Average cycle time with theme vs. without | Shows if theme delays decisions |

### Confidence Levels

| Level | Criteria | Recommendation Strength |
|-------|----------|------------------------|
| High | 10+ deals, statistically significant win rate delta, consistent across segments | Recommend with conviction; assign P1 |
| Medium | 5-9 deals, directionally consistent win rate impact | Recommend with caveat; assign P2 |
| Low | 3-4 deals, unclear win rate correlation | Flag for monitoring; assign P3 |

## Recommendation Drafting Standards

### Recommendation Structure

Each recommendation must include:

1. **Theme reference**: Which theme this addresses
2. **Specific action**: What exactly should be done (not "improve X" but "create Y to achieve Z")
3. **Responsible team**: Product, Marketing, Sales Management, or SE
4. **Expected impact**: Estimated pipeline recovery or win rate improvement
5. **Urgency**: P1 (this sprint), P2 (this quarter), P3 (next quarter)
6. **Evidence**: Deal references that support the recommendation

### Routing Rules

| Theme Type | Primary Owner | Secondary Owner |
|------------|--------------|-----------------|
| Product gap (feature missing) | Product | SE (workaround documentation) |
| Positioning gap (messaging misaligned) | Marketing | Sales (talk track update) |
| Process gap (sales execution issue) | Sales Management | RevOps (CRM/process change) |
| Technical gap (integration/security) | Engineering | SE (interim solution) |
| Competitive gap (losing to specific competitor) | Marketing + Sales | SE (technical differentiation) |
