# Scoring Rubric: search-demand-validator

Evaluates the strength of search-based demand evidence for a product concept across volume, trend, intent, and competitive accessibility.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Search Volume Adequacy | 30% | Whether absolute monthly search volume across the keyword universe is sufficient to support the business model's growth targets |
| 2 | Trend Direction | 25% | Whether the primary keyword clusters are growing, stable, or declining over a 12–24 month horizon |
| 3 | Commercial Intent Signal | 25% | Proportion of high-intent (transactional) keywords versus informational keywords; CPC as a proxy for advertiser commercial value |
| 4 | Competitive Density | 20% | Whether top-ranking positions for primary keywords are capturable given domain authority and content investment constraints |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | >50K monthly searches across transactional keywords, 12-month growth trend >15% YoY, CPC >$5, KD <40 for top clusters | Proceed to market sizing; organic acquisition is a primary channel |
| A | 8.0 – 8.9 | Strong | 20K–50K monthly searches, growing trend, meaningful commercial CPC, moderate competition | Proceed; build SEO content strategy alongside product development |
| B | 7.0 – 7.9 | Good | 5K–20K monthly searches, stable or mildly growing trend, mixed intent signals | Proceed with caution; validate conversion economics before heavy SEO investment |
| C | 5.0 – 6.9 | Adequate | 1K–5K monthly searches or significant informational-only intent; flat trend | Consider whether paid acquisition or community channels compensate for low organic demand |
| D | 3.0 – 4.9 | Weak | <1K monthly searches or declining trend; high KD with no differentiated angle | Do not rely on organic search; validate demand via alternative channels (community, waitlist) |
| F | 0.0 – 2.9 | Failing | No meaningful search volume found; category does not exist in search data | Insufficient search demand; product education market-creation required; re-evaluate concept |

## Signal Tables

### Search Volume Adequacy

| Score | Evidence |
|-------|----------|
| 9–10 | Total keyword universe (seed + long-tail) shows >50K monthly searches; at least 5 clusters with >2K volume each; keyword map covers problem, solution, and competitor terms |
| 7–8 | 20K–50K monthly searches across keyword universe; 2–4 clusters with >1K volume; long-tail coverage complete |
| 5–6 | 5K–20K monthly searches; 1–2 high-volume clusters with sparse long-tail; some coverage gaps in problem or solution intent space |
| 3–4 | 1K–5K monthly searches; volume concentrated in 1 keyword; long-tail universe under-developed or irrelevant |
| 0–2 | <1K total monthly searches across full keyword universe; keyword tool returns "insufficient data" for most seed terms; category may be too new or niche for search data |

### Trend Direction

| Score | Evidence |
|-------|----------|
| 9–10 | Primary keyword clusters show >15% YoY growth over 24-month trend; no significant seasonal interference; Google Trends confirms sustained upward trajectory |
| 7–8 | 5–15% YoY growth; trend is positive but with some quarterly volatility; seasonal peaks are predictable and documentable |
| 5–6 | 0–5% YoY growth; trend is flat with no clear directional signal; 12-month window shows mixed movement |
| 3–4 | −1% to −10% YoY decline; trend is falling for 2+ consecutive 6-month periods; market showing signs of consolidation or replacement |
| 0–2 | >10% YoY decline sustained over 24 months; category being replaced by adjacent solution (e.g., "RSS readers" after social media dominance) |

### Commercial Intent Signal

| Score | Evidence |
|-------|----------|
| 9–10 | >50% of keyword volume is transactional intent (buy, pricing, comparison, "best X for Y"); average CPC >$5 across top 20 keywords; CPC rising YoY |
| 7–8 | 30–50% transactional intent; average CPC $2–$5; mix of informational and commercial terms with clear commercial cluster |
| 5–6 | 15–30% transactional intent; average CPC $0.50–$2; most volume is informational ("how to", "what is"); commercial intent exists but is a minority |
| 3–4 | <15% transactional intent; CPC <$0.50; majority of searches are informational or educational; audience is researching, not buying |
| 0–2 | Near-zero transactional intent; CPC <$0.10 or not reported; searches are definitional ("what is X") with no commercial signal; free-tier seekers dominate |

### Competitive Density

| Score | Evidence |
|-------|----------|
| 9–10 | Keyword difficulty (KD) <30 for primary clusters; top-ranking pages are thin content or low-authority domains; 3+ topical gaps where no authoritative content ranks |
| 7–8 | KD 30–50 for primary clusters; ranking mix includes some high-authority sites but also mid-tier content; differentiated angle could rank within 6–12 months with quality content |
| 5–6 | KD 50–65 for primary clusters; top 3 positions held by established brands; ranking requires sustained content investment over 12–18 months |
| 3–4 | KD 65–80 for primary clusters; first page dominated by category leaders (G2, Wikipedia, major SaaS vendors); organic acquisition requires high domain authority and significant content budget |
| 0–2 | KD >80 for primary clusters; SERP entirely owned by 2–3 dominant players with high domain authority; organic entry is not feasible for a new entrant without paid amplification |
