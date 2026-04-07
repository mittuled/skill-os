# Social Listening Framework

Reference framework for signal taxonomy, sentiment scoring, and escalation triggers in ongoing social listening programmes.

## Signal Taxonomy

Categorise every monitored signal into one of five types before taking action.

| Signal Type | Definition | Examples | Priority |
|------------|-----------|---------|---------|
| **Brand mention** | Direct reference to company name, product, or branded hashtag | @BrandName, #ProductName, "we use [brand]" | Monitor daily |
| **Intent signal** | Language indicating purchase, switching, or evaluation intent | "looking for [category]", "replacing [competitor] with", "anyone tried [brand]?" | Alert immediately |
| **Sentiment shift** | Sustained change in positive/negative ratio over 7-day window | Spike in negative mentions post-launch, sudden drop in positive sentiment | Alert if >10% shift |
| **Competitive signal** | Mentions comparing brand to competitors or competitor-only conversation | "[Competitor] vs [Brand]", "[Competitor] is better because", competitor launch posts | Review weekly |
| **Crisis signal** | Rapid volume spike or organised negative campaign | 3× normal mention volume in <4 hours, coordinated hashtag usage, viral complaint thread | Escalate within 1 hour |

---

## Monitoring Keyword Set

### Tier 1 — Always On (Real-Time Alerts)

| Category | Keywords / Phrases |
|---------|-------------------|
| Brand core | [Brand name], [Product name(s)], [Branded hashtag(s)] |
| Executive mentions | [CEO name], [key executive names] |
| Crisis triggers | "[Brand] scam", "[Brand] breach", "[Brand] outage", "[Brand] problem" |
| High-intent purchase | "switch to [brand]", "try [brand]", "cancel [competitor]", "vs [brand]" |

### Tier 2 — Daily Review

| Category | Keywords / Phrases |
|---------|-------------------|
| Competitor comparison | "[Competitor 1] vs [Brand]", "[Brand] alternative", "better than [Brand]" |
| Product feedback | [Feature names], [product area terms], "[Brand] [feature] not working" |
| Category conversation | [2-3 generic category terms relevant to ICP] |
| Industry events | [Event hashtags when active] |

### Tier 3 — Weekly Summary

| Category | Keywords / Phrases |
|---------|-------------------|
| Thought leadership | [CEO/spokesperson name(s)] in category discussion |
| Partnership mentions | [Partner brand names] |
| Recruitment sentiment | "[Brand] glassdoor", "[Brand] culture", "working at [Brand]" |

---

## Sentiment Scoring Model

### Classification Rules

| Sentiment | Definition | Examples |
|-----------|-----------|---------|
| **Positive** | Favourable mention; praise, recommendation, or enthusiasm | "love [Brand]", "just signed up, amazing", "switched from X and never going back" |
| **Neutral** | Factual reference; no clear valence; informational | "[Brand] announced X feature", "does [Brand] integrate with Y?" |
| **Negative** | Criticism, complaint, disappointment, or warning | "support is terrible", "[Brand] is broken again", "don't use [Brand] for [use case]" |
| **Mixed** | Contains both positive and negative signals in same post | "great product, terrible pricing" → classify by dominant frame |

### Sentiment Scoring Scale (0-10)

| Score | Label | Characteristics |
|-------|-------|----------------|
| 9-10 | Strongly positive | Unprompted advocacy; recommendation to others; emotional enthusiasm |
| 7-8 | Positive | Satisfaction expressed; feature praise; general endorsement |
| 5-6 | Neutral/Informational | Question, news citation, or category mention without clear opinion |
| 3-4 | Negative | Complaint or criticism; single issue; moderate frustration |
| 1-2 | Strongly negative | Severe criticism; anger; public call to avoid the brand |
| 0 | Crisis-level | Viral complaint; coordinated campaign; safety or legal claim |

**Volume-weighted sentiment score** = Σ (signal score × signal reach) ÷ total reach

---

## Escalation Triggers and Response Protocol

| Trigger | Threshold | Response Time | Escalation Path |
|---------|-----------|--------------|----------------|
| Tier-1 crisis keyword detected | Any match | 30 minutes | Social Manager → PR Manager → VP Marketing |
| Mention volume spike | >3× 7-day baseline in <4 hours | 1 hour | Social Manager → PR Manager |
| Sentiment shift (7-day) | >10% negative increase | 4 hours | Social Manager → PR Manager |
| Competitor negative story about brand | Any Tier-1 outlet pickup | 1 hour | PR Manager → VP Marketing |
| Executive mentioned negatively (>100 impressions) | 100+ impressions | 2 hours | Social Manager → PR Manager |
| Product outage or bug trending | Any mention of outage + 20+ posts | 30 minutes | Social Manager → Product + Support |
| Customer data or security claim | Any | Immediate | PR Manager → Legal → CEO |

### Response Decision Tree

```
Mention detected
└── Is it a crisis trigger? (See table above)
    ├── YES → Escalate immediately; do NOT respond publicly without PR sign-off
    └── NO → Sentiment?
        ├── Positive → Engage (like, reply with gratitude, amplify if appropriate)
        ├── Neutral/Question → Respond with helpful information within 4 business hours
        └── Negative
            ├── Valid complaint → Acknowledge publicly; move to DM for resolution
            ├── Invalid/Misinformation → Provide factual correction; do not argue
            └── Troll/Bad faith → Do not engage; monitor for escalation
```

---

## Share of Voice Tracking

Calculate weekly for competitive landscape view.

| Brand | Mentions (7d) | Weighted SOV | vs. Prior Week |
|-------|-------------|-------------|---------------|
| [Our Brand] | | [X]% | [↑/↓/→] |
| [Competitor A] | | [X]% | |
| [Competitor B] | | [X]% | |

**Weighting**: Apply 3× multiplier for Tier-1 outlet or influencer (>100K followers) mentions; 1× for standard mentions.

---

## Reporting Cadence

| Report | Frequency | Audience | Key Contents |
|--------|-----------|---------|-------------|
| Alert notification | Real-time (threshold-based) | PR Manager, Social Manager | Crisis or escalation trigger details |
| Daily digest | Daily (09:00) | Social Manager | Volume, top mentions, sentiment snapshot |
| Weekly summary | Monday | Marketing leadership | SOV, sentiment trend, competitive signals, recommended actions |
| Monthly deep-dive | Monthly | VP Marketing, CMO | Full trend analysis, theme identification, programme recommendations |
