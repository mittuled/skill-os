# Market Sizing Brief

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | market-sizer-data |

## Executive Summary

[2-3 sentences stating the base-case SOM, the primary methodology used, and the confidence level.

GUIDANCE: Lead with the actionable number. Example: "Based on a bottom-up model validated against two top-down cross-checks, the base-case SOM for [product category] in [geography] is $[X]M ARR by [year]. The estimate carries medium confidence; the two highest-sensitivity assumptions are adoption rate and ARPU."]

## Market Boundary Definition

[Precise scope of the market being sized.

GUIDANCE:
- Good: "B2B SaaS companies with 10–500 employees in North America and Western Europe, using a CRM, who experience ≥3 support tickets/week related to onboarding automation."
- Bad: "Mid-market companies that need our product."
- Format: Prose with explicit inclusion/exclusion criteria for product category, geography, company size, role, and use-case.]

**Product Category:** [Category name]
**Geography:** [Countries / regions included]
**Target Segment:** [Company size, role, industry vertical]
**Time Horizon:** [Year of estimate, e.g., 2025 annual run-rate]
**Exclusions:** [What is explicitly not included and why]

## TAM / SAM / SOM Estimates

[Three-tier market sizing with both bottom-up and top-down figures.

GUIDANCE:
- Good: Present all three layers with a table comparing bottom-up vs. top-down estimates and explicit scenario ranges.
- Bad: A single TAM number from one analyst report with no SOM derivation.
- Format: Table with Bear / Base / Bull columns for each layer.]

| Market Layer | Bear Case | Base Case | Bull Case | Methodology |
|-------------|----------|---------- |---------- |------------|
| TAM | [$M] | [$M] | [$M] | [Top-down: analyst report source] |
| SAM | [$M] | [$M] | [$M] | [TAM × segment filter: N customers × adoption rate] |
| SOM | [$M] | [$M] | [$M] | [SAM × realistic market share %] |

**Bottom-Up vs. Top-Down Reconciliation:**
[Describe the divergence between methods and which estimate is used as the primary, with rationale.]

## Data Sources

[All sources used with recency and reliability notes.

GUIDANCE:
- Good: Table with source name, date, what it was used for, and a reliability rating.
- Bad: A bullet list of source names with no context on how they were used or how current they are.
- Format: Table.]

| Source | Date | Used For | Reliability |
|--------|------|---------|------------|
| [Source name] | [YYYY-MM] | [TAM estimate / segment count / ARPU benchmark] | [High / Medium / Low — with reason] |

## Assumptions Log

[Document every key assumption driving the model with its source and scenario variants.

GUIDANCE:
- Good: Every row in the model that is not directly observable has an entry here.
- Bad: Omitting assumptions that drove the SOM number by more than 10%.
- Format: Table with Bear/Bull variants and sensitivity classification.]

| Assumption | Bear Value | Base Value | Bull Value | Source | SOM Sensitivity |
|-----------|-----------|-----------|-----------|--------|----------------|
| Addressable customers | [N] | [N] | [N] | [source] | [High / Med / Low] |
| Y1 adoption rate | [%] | [%] | [%] | [source] | [High / Med / Low] |
| ARPU | [$] | [$] | [$] | [source] | [High / Med / Low] |
| Market share % | [%] | [%] | [%] | [comparable benchmarks] | [High / Med / Low] |

## Sensitivity Analysis

[Which assumptions most affect the SOM estimate.

GUIDANCE:
- Good: Tornado chart or table showing SOM impact of ±20% change in each key assumption.
- Bad: "The model is sensitive to adoption rate." Quantify the sensitivity.
- Format: Table with assumption, base SOM, and SOM at ±20% change.]

| Assumption | Base SOM | SOM at −20% | SOM at +20% | Impact Range |
|-----------|---------|------------|------------|------------|
| Adoption rate | [$M] | [$M] | [$M] | [±$M] |
| ARPU | [$M] | [$M] | [$M] | [±$M] |
| Addressable customers | [$M] | [$M] | [$M] | [±$M] |

## Recommendations

[Prioritized list of decisions or next steps.

GUIDANCE:
- P1: Whether the SOM justifies further investment in the category.
- P2: Which assumptions require primary research to reduce uncertainty.
- P3: Which adjacent segments to size next if the primary opportunity validates.]

## Appendices

### A. Methodology

[Document the bottom-up model formula, top-down source details, and reconciliation logic. Include date range for all data used.]

### B. Supporting Data

[Raw data tables from sources, search volume keyword clusters, comparable S-1 filing excerpts, or analyst report citations used in the model.]
