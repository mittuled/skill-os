# Revenue Impact Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Operations Analyst] |
| Feature / Release | [Name and version] |
| Launch Date | [YYYY-MM-DD] |
| Measurement Window | [30 / 60 / 90 days post-launch] |
| Methodology | [Difference-in-differences / Trend-adjusted pre/post] |
| Skill | revenue-impact-monitor |

## Executive Summary

[2-3 sentences covering the headline revenue finding, confidence level, and recommended action.
GUIDANCE: State the verdict clearly — "The feature drove a statistically significant X% increase in upgrade rate (p < 0.05), contributing an estimated $Y in incremental MRR over 30 days." or "Results are inconclusive at this window; recommend extending observation to 60 days."]

## Cohort Definition

| Group | Definition | Size |
|-------|-----------|------|
| Treatment | [Users who received the feature] | [N] |
| Control | [Holdout / matched cohort] | [N] |
| Analysis period | [Pre: YYYY-MM-DD to YYYY-MM-DD; Post: YYYY-MM-DD to YYYY-MM-DD] | |

## Primary Metrics

| Metric | Pre-Launch (Treatment) | Post-Launch (Treatment) | Control Change | Attributed Impact | p-value | Verdict |
|--------|----------------------|------------------------|----------------|-----------------|---------|---------|
| Upgrade rate | | | | | | |
| MRR change | | | | | | |
| Feature-to-revenue conversion | | | | | | |

## Guardrail Metrics

| Metric | Pre-Launch | Post-Launch | Change | Status |
|--------|-----------|------------|--------|--------|
| Churn rate | | | | Green / Amber / Red |
| Downgrade rate | | | | Green / Amber / Red |

## Confounding Factor Assessment

| Factor | Checked? | Ruling |
|--------|---------|--------|
| Seasonal trend | | [Ruled out / Possible confounder — note impact] |
| Concurrent marketing campaign | | |
| Pricing change | | |
| Sales activity spike | | |
| Platform incident | | |

## Revenue Attribution Estimate

[Calculated revenue impact with methodology note.

GUIDANCE:
- Good: "Treatment group upgrade rate: 8.2% vs control 5.4% = +2.8 pp lift. Applied to 4,200 eligible users: 118 incremental upgrades × avg upgrade value $45 MRR = **$5,310 incremental MRR**. Confidence: 95% (p = 0.03)."
- Bad: "Revenue went up"
- Format: Show the calculation chain explicitly]

## Interpretation and Caveats

[Any limitations, confounding factors that could not be fully ruled out, or segments where results differ.
GUIDANCE: Be honest about uncertainty — it builds credibility. Note which caveats materially change the interpretation.]

## Recommendations

[Next steps based on findings.
GUIDANCE: P1 = act on within 1 sprint; P2 = schedule for next planning cycle.]
