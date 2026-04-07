# Scoring Rubric: pricing-review-runner

Evaluates the quality and completeness of a periodic pricing review across competitiveness, margin health, win/loss signal, willingness-to-pay evidence, and recommendation quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Competitive Benchmarking | 25% | Feature-adjusted price comparison against 3-5 direct competitors with current data |
| 2 | Margin Analysis | 25% | Gross and contribution margin calculated by tier, segment, and deal size |
| 3 | Win/Loss Signal Integration | 20% | Pricing-related win/loss data from sales used to validate or challenge price assumptions |
| 4 | Willingness-to-Pay Evidence | 15% | Quantified signals from sales, CS, and product on buyer price sensitivity |
| 5 | Recommendation Quality | 15% | Recommendations include modelled revenue and margin impact for each proposed change |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Competitors benchmarked on feature-adjusted basis with current quotes, all tiers analysed, win/loss data covers >80% of recent deals, WTP triangulated from 3+ sources, every recommendation has modelled impact | Present to pricing committee; implement approved changes |
| A | 8.0 – 8.9 | Strong | 3+ competitors benchmarked, key tiers analysed, win/loss data covers 60–79% of deals, WTP from 2 sources, recommendations have directional impact models | Minor data gaps acceptable; proceed to pricing committee |
| B | 7.0 – 7.9 | Good | 2–3 competitors benchmarked with minor data gaps, most tiers analysed, win/loss covers 40–59% of deals, WTP from 1 source | Fill data gaps before presenting recommendations; schedule follow-up |
| C | 5.0 – 6.9 | Adequate | 1–2 competitors benchmarked, partial tier analysis, win/loss data sparse, WTP anecdotal | Defer pricing changes; invest 2 weeks in data collection before re-running review |
| D | 3.0 – 4.9 | Weak | Competitor data more than 6 months old, tier analysis incomplete, no win/loss input, no WTP evidence | Do not change pricing on this basis; restart data collection |
| F | 0.0 – 2.9 | Failing | No competitive benchmark, no margin analysis, no win/loss data, no WTP evidence | Review cannot support any pricing decisions; flag to CFO |

## Signal Tables

### Competitive Benchmarking

| Score | Evidence |
|-------|----------|
| 9-10 | 5 direct competitors benchmarked on feature-adjusted basis; pricing data from current public pages or sales quotes within 90 days; includes packaging differences (seat-based, usage-based, flat) |
| 7-8 | 3–4 competitors benchmarked; pricing current within 6 months; minor feature-adjustment gaps; all primary competitors covered |
| 5-6 | 2–3 competitors benchmarked; pricing 6–12 months old; limited feature adjustment; one or more major competitors missing |
| 3-4 | 1–2 competitors with partial data; pricing over 12 months old; no feature adjustment applied |
| 0-2 | No competitive benchmark present or data is clearly fabricated / outdated beyond 2 years |

### Margin Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Gross margin and contribution margin calculated for every pricing tier, every customer segment (SMB/mid-market/enterprise), and every deal size band; COGS allocated fully-loaded including hosting, support, and implementation |
| 7-8 | Gross margin by tier and segment; contribution margin present but missing 1–2 dimensions; COGS allocated with minor exclusions documented |
| 5-6 | Gross margin at company level and 2+ tiers; contribution margin absent or estimated; COGS partially allocated |
| 3-4 | Company-level gross margin only; no tier or segment breakdown; COGS not fully allocated |
| 0-2 | No margin analysis present or methodology is clearly flawed (e.g., using revenue as a proxy for margin) |

### Win/Loss Signal Integration

| Score | Evidence |
|-------|----------|
| 9-10 | Win/loss data covers >80% of deals from the last 12 months; pricing explicitly coded as a factor in exit surveys; analysis distinguishes price objections from value objections |
| 7-8 | Win/loss data covers 60–79% of recent deals; pricing flagged as a factor in the majority of records; some distinction between price and value |
| 5-6 | Win/loss data covers 40–59% of deals; pricing mentioned in some records but inconsistently coded; no distinction between price and value objections |
| 3-4 | Win/loss data sparse (<40% coverage); pricing mentioned anecdotally by sales leadership only; no systematic analysis |
| 0-2 | No win/loss data incorporated; pricing assessment based on analyst opinion only |

### Willingness-to-Pay Evidence

| Score | Evidence |
|-------|----------|
| 9-10 | WTP triangulated from 3+ sources: sales deal velocity at different price points, NPS/CSAT by tier, feature utilization rates by tier, and at least one direct survey or Van Westendorp price sensitivity test |
| 7-8 | WTP from 2 sources; sales and CS data present; direct survey data absent but other quantitative proxies used |
| 5-6 | WTP from 1 source; primarily qualitative sales input; no quantitative validation |
| 3-4 | WTP entirely anecdotal; single sales rep observations only; no attempt at quantification |
| 0-2 | No WTP evidence; pricing recommendation is disconnected from buyer behaviour data |

### Recommendation Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Every recommendation has a modelled revenue and margin impact; model includes base, upside, and downside scenarios; implementation plan includes grandfathering policy, rollout timing, and contract implications |
| 7-8 | Most recommendations have directional impact models; base case present for all; implementation considerations addressed for primary changes |
| 5-6 | Some recommendations have impact estimates; models are high-level or single-scenario; implementation plan partial |
| 3-4 | Recommendations present but no modelled impact; implementation not addressed |
| 0-2 | Recommendations absent or consist only of "raise prices" without any analysis |
