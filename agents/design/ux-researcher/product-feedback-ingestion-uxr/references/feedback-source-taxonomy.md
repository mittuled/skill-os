# Product Feedback Source Taxonomy

## Purpose

A classification system for all feedback sources that flow into UX research, with guidance on signal quality, processing priority, and appropriate use in design decisions.

## Source Classification Matrix

| Source Type | Signal Type | Volume | Reliability | Recency | Priority |
|-------------|------------|--------|-------------|---------|---------|
| In-depth user interviews | Qualitative — motivations and behaviours | Low | High | Study-specific | High |
| Usability test sessions | Qualitative — task performance | Low | High | Study-specific | High |
| Session recordings (Hotjar, FullStory, PostHog) | Behavioural — actual usage | Medium | High | Continuous | High |
| Support tickets | Qualitative — problems at scale | High | Medium | Continuous | High |
| NPS open-text responses | Qualitative — sentiment drivers | Medium | Medium | Periodic | Medium |
| CSAT survey responses | Mixed — satisfaction + comments | High | Medium | Periodic | Medium |
| In-app feedback widgets | Qualitative — in-context frustration | Medium | Medium | Continuous | Medium |
| App store reviews | Qualitative — high-friction moments | High | Low | Continuous | Medium |
| Social media mentions | Qualitative — public sentiment | High | Low | Continuous | Low |
| Sales call notes | Qualitative — pre-sale needs | Medium | Medium | Continuous | Medium |
| Customer success call notes | Qualitative — post-sale problems | Medium | Medium | Continuous | High |
| Feature requests (product board) | Quantitative — stated demand | High | Low | Continuous | Low |

**Reliability note**: "Reliable" means the source captures actual behaviour or genuine problem, not social desirability or speculative preference.

## Signal Quality Assessment

### High-Reliability Sources
Suitable for making design decisions without additional validation:
- User interviews (observational data, not self-report)
- Session recordings (actual behaviour captured)
- Usability test task failures

### Medium-Reliability Sources
Useful for hypothesis generation; validate with behavioural data:
- Support tickets (indicates problem exists but not how widespread)
- Survey responses (self-report; subject to social desirability)
- CS call notes (filtered through CS framing)

### Low-Reliability Sources
Directional only; do not build features based solely on these:
- Feature requests (vocal minority may not represent majority need)
- App store reviews (extreme sentiment bias)
- Social media (context-free, sample bias)

## Feedback Volume vs. Signal Value

High volume does not equal high signal:

| Volume | Signal Value | How to Treat |
|--------|-------------|-------------|
| High volume, low reliability | Directional trend | Look for corroboration in behavioural data |
| High volume, high reliability | Strong signal | Act after synthesis |
| Low volume, high reliability | Targeted insight | Weight per evidence quality, not count |
| Low volume, low reliability | Anecdote | Document; do not act without corroboration |

## Ingestion Standards by Source

### Support Tickets
- Review cadence: Weekly
- Tagging requirement: Product area + issue type + user segment (where identifiable)
- Pattern threshold: 3+ tickets in same category = flag for researcher review
- Escalation trigger: Any ticket describing data loss, blocking error, or safety concern

### Session Recordings
- Review cadence: Bi-weekly batch (5-10 recordings per batch minimum)
- Selection criteria: Prioritise sessions on flows with known low completion rates or recent design changes
- Minimum watch time: Full session — do not skim
- Note requirement: Observation log for each session reviewed

### NPS / CSAT Open Text
- Processing cadence: Monthly
- Method: Thematic coding of open text; do not rely solely on score
- Cross-reference: Correlate low scores with specific product areas where text mentions them

### In-App Feedback Widgets
- Review cadence: Weekly scan; daily during major releases
- Triage: Segment by screen/feature if tool supports it
- Signal type: Contextual frustration — indicates friction at the moment of capture

## Deduplication and Cross-Source Correlation

When the same issue appears across multiple sources, document it as a multi-source signal:

| Finding | Support Tickets | Session Recordings | Interviews | NPS Text | Signal Strength |
|---------|----------------|-------------------|------------|---------|----------------|
| [e.g. Users confused by checkout CTA hierarchy] | 8 tickets | 5/15 sessions | 4/12 participants | 3 mentions | Strong — 4 sources |
| [e.g. Mobile keyboard covers input field] | 3 tickets | 2/10 sessions | 0 | 1 mention | Moderate — 3 sources |

## Anti-Patterns in Feedback Ingestion

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Treating feature requests as validated needs | Vocal users request features they won't actually use | Trace request to a confirmed user job before designing |
| Processing only recent feedback | Recency bias obscures persistent structural problems | Review 3-month rolling window, not just last 2 weeks |
| Ingesting without tagging | Untagged feedback cannot be searched or synthesised | Tag at ingestion; make it mandatory |
| One-person review without validation | Single-researcher interpretation introduces bias | Cross-check key themes with a second reviewer |
| Reporting volume ("42 users reported X") as evidence of priority | Volume alone does not determine design priority | Cross-reference with task severity, not just count |
