# Framework: Signal Synthesiser (Data)

Defines the approach for combining quantitative signals from multiple sources into a unified product health view.

## Signal Source Taxonomy

| Source Category | Examples | Signal Type | Latency |
|----------------|---------|------------|---------|
| Product analytics | Amplitude, Mixpanel, Segment | User behaviour events, funnel metrics | Near real-time |
| Revenue data | Stripe, Chargebee, Salesforce | MRR, churn, expansion, NRR | Daily |
| Support | Intercom, Zendesk | Ticket volume, category, CSAT, resolution time | Daily |
| Infrastructure | Datadog, Sentry, PagerDuty | Error rates, latency, uptime | Real-time |
| Qualitative | NPS surveys, app store reviews, session recordings | Sentiment, verbatim feedback | Weekly |
| External | Google Analytics, App Store Connect | Organic traffic, store ratings | Daily |

## Anomaly Detection Method

For each signal, flag values that deviate more than 2σ from the trailing 30-day mean:

```
Z-score = (current_value − 30d_mean) / 30d_std_dev
Flag if |Z-score| > 2.0
```

For signals with known weekly seasonality: compute Z-score against the same day-of-week rolling average over the past 4 weeks.

## Cross-Source Correlation Protocol

When two or more signals move in the same direction in the same window:

1. Record the observed co-movement: source A moved X%, source B moved Y%, in the same direction over [time window].
2. Test for temporal precedence: did one signal lead the other (A moved first, B followed within N days)?
3. Generate a causal hypothesis if precedence is present; label as correlated-only if simultaneous.
4. Note explicitly if the correlation is likely spurious (e.g., marketing campaign explains both traffic and support volume simultaneously).

## Narrative Structure

Each synthesis report should follow this structure:

1. **Headline**: One sentence — the most important change in product health this period.
2. **Signal summary**: 3–5 bullets — each bullet states one signal with its value, direction, and anomaly status.
3. **Correlations**: Any cross-source patterns with causal hypothesis or correlation caveat.
4. **Root causes (if applicable)**: For Red anomalies, the leading hypothesis with supporting evidence.
5. **Action items**: 2–3 items, each with: signal → hypothesis → recommended action → owner.

## Synthesis Cadences

| Cadence | Scope | Audience | Distribution Channel |
|---------|-------|---------|---------------------|
| Weekly | All primary KPIs + anomaly flags | Product, Growth, Engineering leads | Slack #product-health |
| Monthly | Full signal synthesis including qualitative | Leadership, all cross-functional leads | Notion / email |
| Ad-hoc | Triggered by P0/P1 anomaly | On-call + relevant team lead | Slack DM + incident channel |

## Common Anti-Patterns and Mitigations

| Anti-Pattern | Detection | Mitigation |
|-------------|----------|-----------|
| Correlation stated as causation | Synthesis says "because X happened, Y changed" without precedence evidence | Always include "this is correlated with" or "A preceded B by N days" language |
| Dashboard forwarding | Report is a list of links | Synthesis must include a written narrative; no link-only deliverables |
| Cherry-picking anomalies | Only negative anomalies reported | Report all anomalies (positive and negative); note null results (stable metrics) |
| Stale synthesis | Report delivered after the decision meeting | Establish a hard delivery time: synthesis available 1 hour before the review meeting |
