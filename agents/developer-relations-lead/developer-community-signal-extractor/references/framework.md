# Framework: developer-community-signal-extractor

Defines the developer signal taxonomy, source map, classification protocol, and routing matrix for extracting actionable technical signals from developer communities.

## Developer Signal Taxonomy

| Category | Definition | Subcategories | Business Impact |
|----------|-----------|--------------|----------------|
| API Pain Point | Friction using an API endpoint, parameter, or behaviour | Authentication, Rate limiting, Response schema, Versioning | High — direct DX impact |
| SDK Bug | Defect in SDK code, packaging, or compatibility | Crash, Wrong output, Dependency conflict, IDE integration | Critical — blocks developers |
| Missing Feature | Capability developers want that does not exist | New endpoint, Webhook event, SDK method, Language support | High — roadmap input |
| Documentation Gap | Developer unable to find or understand information | Missing guide, Outdated code sample, Unclear error reference | High — increases support cost |
| Performance Complaint | Latency, timeout, or reliability issue reported | Slow endpoint, Inconsistent availability, Rate limit too low | Critical — production impact |
| Migration Friction | Difficulty upgrading from old to new version | Breaking changes, Unclear deprecation path, Migration guide gap | High — retention risk |
| Praise Signal | Developer explicitly cites a positive experience | Feature praise, DX compliment, Recommendation intent | Medium — validation and testimonial |
| Competitive Signal | Developer compares to or switches from/to a competitor | Feature gap, Pricing comparison, SDK ergonomics comparison | High — strategic intelligence |
| Use Case Discovery | Unexpected or creative application of the product | Novel integration, Ecosystem use, Industry-specific pattern | Medium — product insight |

## Source Map

| Source | Signal Quality | Update Latency | Access Method | Primary Signal Types |
|--------|--------------|---------------|--------------|---------------------|
| GitHub Issues (open) | Very High | Real-time | GitHub API / manual | SDK bugs, API pain points, missing features |
| GitHub Issues (closed) | High | Historical | GitHub API | Resolution patterns, recurring issues |
| Discord / Slack #help | High | Real-time | Manual monitoring, bot export | Documentation gaps, API pain points |
| Stack Overflow tags | Medium–High | 1–7 days | API or tag monitoring | Documentation gaps, common integration errors |
| Twitter/X developer mentions | Medium | Real-time | Social monitoring tool | Competitive signals, praise, public frustrations |
| Conference session Q&A | Very High | Per event | Manual notes | Strategic concerns, feature requests from advanced users |
| Developer survey responses | High | Per survey | Survey tool export | Systematic view of all signal types |
| NPS follow-up interviews | Very High | Per interview | CRM | Churn indicators, migration friction |

## Signal Classification Protocol

Each extracted signal must be tagged with:

| Field | Required Values | Notes |
|-------|----------------|-------|
| Category | From taxonomy above | Required |
| Severity | P0–P3 (see scale below) | Required |
| Product Area | API / SDK / Docs / Platform / Billing | Required |
| Source | Platform and URL | Required |
| Developer Segment | Hobbyist / Startup / SMB / Enterprise | Required |
| Frequency | Unique developer count mentioning same issue | Required |
| Timeline Correlation | [None / Release vN.N / Outage YYYY-MM-DD] | If applicable |
| Verbatim | Exact quote from developer (1–2 sentences) | Required |

### Severity Scale

| Severity | Trigger | Routing SLA |
|----------|---------|------------|
| P0 — Outage-class | SDK crash or API 5xx blocking multiple developers in production | Same-day to engineering |
| P1 — High Impact | Issue preventing integration reported by 5+ developers in 30 days | 48 hours to engineering/docs |
| P2 — Moderate | Feature gap or docs issue impacting progress of 2–4 developers | Weekly synthesis |
| P3 — Low | Single mention, cosmetic issue, or minor enhancement | Monthly synthesis |

## Pattern Analysis Method

1. **Cluster by semantic overlap** (>60% overlap = same signal)
2. **Correlate with product timeline**: Map signal spikes against releases, changelog events, and outages
3. **Segment weighting**: Apply segment multiplier (Enterprise = 3×, SMB = 2×, Startup = 1.5×, Hobbyist = 1×) for business impact scoring
4. **Velocity tracking**: Compare signal frequency this period vs. 30-day rolling average — flag > 50% increase as trending

## Routing Matrix

| Category | Primary Route | Secondary Route | Expected Action |
|----------|-------------|----------------|----------------|
| SDK Bug (P0/P1) | Engineering (immediate) | Support | GitHub issue opened, fix in next sprint |
| API Pain Point | Product Manager | Engineering | Added to backlog with developer count |
| Missing Feature | Product Manager | DevRel | Backlog ticket with community vote context |
| Documentation Gap | Technical Writer | DevRel | Docs task opened |
| Performance Complaint | Engineering (SRE) | Product | Perf investigation opened |
| Migration Friction | Technical Writer | Engineering | Migration guide improvement task |
| Competitive Signal | PMM | Sales | Competitive brief updated |
| Use Case Discovery | Product | Marketing | Potential case study / blog content |
