# Unit Economics Viability Gate Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [CFO / VP Finance] |
| Version | [1.0] |
| Status | [Draft / Final] |
| Business Model / Segment | [Name of model or segment being gated] |
| Gate Decision | [PASS / CONDITIONAL PASS / FAIL] |
| Skill | unit-econ-viability-gate |

## Executive Summary

[2-3 sentences stating the gate decision, the composite score, and the two most important findings.

GUIDANCE: Lead with the verdict. Example of good: "The SMB segment unit economics receive a CONDITIONAL PASS with a composite score of 6.8 (Grade C). LTV/CAC of 2.4x and a 22-month payback period are below target thresholds; approval requires reducing average CAC by 15% within 90 days before full-scale marketing investment. The enterprise segment scores 8.5 and is PASS with no conditions." Bad: "The unit economics look reasonable but there are some areas for improvement."]

## Input Package Validation

[Confirm which inputs were available and their quality.

GUIDANCE:
- Good: Flag any input with reliability concerns — downstream scores should reflect data quality uncertainty.
- Bad: Accept all inputs without source verification.
- Format: Checklist with source and quality rating]

| Input | Source | Period | Quality | Notes |
|-------|--------|--------|---------|-------|
| CAC by channel | [Source] | [Period] | [High/Medium/Low] | [Any concerns] |
| Gross margin | [Source] | [Period] | [High/Medium/Low] | [Any concerns] |
| LTV / churn rate | [Source] | [Period] | [High/Medium/Low] | [Any concerns] |
| Payback period target | [Source] | N/A | [High/Medium/Low] | [Any concerns] |
| Runway | [Source] | [Date] | [High/Medium/Low] | [Any concerns] |

## Scoring Summary

[Apply the rubric from `references/scoring-rubric.md`.

GUIDANCE:
- Good: Score each criterion with the specific evidence that drove the score. Do not use the same score for all criteria.
- Bad: Apply scores without citing observable evidence.
- Format: Scoring table with criterion, weight, score, and evidence summary]

| # | Criterion | Weight | Score (0-10) | Weighted Score | Evidence Summary |
|---|-----------|--------|--------------|----------------|-----------------|
| 1 | LTV/CAC Ratio | 30% | [X] | [X × 0.30] | [Specific data point] |
| 2 | CAC Payback Period | 25% | [X] | [X × 0.25] | [Specific data point] |
| 3 | Gross Margin Sustainability | 20% | [X] | [X × 0.20] | [Specific data point] |
| 4 | Churn and Retention Durability | 15% | [X] | [X × 0.15] | [Specific data point] |
| 5 | Sensitivity Resilience | 10% | [X] | [X × 0.10] | [Specific data point] |
| **Composite** | | **100%** | | **[Total]** | **Grade: [A+/A/B/C/D/F]** |

## LTV/CAC Analysis

[Detailed LTV/CAC calculation by segment and channel.

GUIDANCE:
- Good: Show the numerator and denominator separately; show both gross-margin LTV and contribution-margin LTV.
- Bad: Present only the ratio without the components.
- Format: Calculation table segmented by channel or customer tier]

| Segment | Fully-Loaded CAC | ARPU | Gross Margin % | Gross Churn Rate | Gross-Margin LTV | LTV/CAC | Target | Status |
|---------|-----------------|------|----------------|-----------------|-----------------|---------|--------|--------|
| [Inbound / SMB] | $[X] | $[X] | [X]% | [X]% | $[X] | [X]x | 3x | [PASS/FAIL] |
| [Outbound / Mid-Market] | $[X] | $[X] | [X]% | [X]% | $[X] | [X]x | 3x | [PASS/FAIL] |
| [Enterprise] | $[X] | $[X] | [X]% | [X]% | $[X] | [X]x | 3x | [PASS/FAIL] |

## Payback Period Validation

[CAC payback analysis with runway overlay.

GUIDANCE:
- Good: Show payback in the context of current runway. Flag any scenario where payback exceeds 60% of runway.
- Bad: Report payback without runway context.
- Format: Table with payback, runway, and ratio]

| Segment | CAC | Monthly GM per Customer | Payback (months) | Current Runway (months) | Payback as % of Runway | Status |
|---------|-----|------------------------|-----------------|------------------------|----------------------|--------|
| [Segment] | $[X] | $[X] | [X] | [X] | [X]% | [FLAG if >60%] |

## Sensitivity Matrix

[Stress test results for three standard scenarios.

GUIDANCE:
- Good: Show the original score and the stressed score side-by-side. Identify which variable has the largest impact.
- Bad: Show only the stressed results without the baseline.
- Format: Matrix with scenario, assumption change, resulting LTV/CAC, payback, and gate status]

| Scenario | Variable Changed | Change | LTV/CAC | Payback | Gate Status |
|----------|-----------------|--------|---------|---------|-------------|
| Base Case | — | — | [X]x | [X] mo | [PASS/CONDITIONAL/FAIL] |
| Churn Stress | Gross churn rate | +[X]pp | [X]x | [X] mo | [PASS/CONDITIONAL/FAIL] |
| CAC Inflation | Fully-loaded CAC | +[X]% | [X]x | [X] mo | [PASS/CONDITIONAL/FAIL] |
| GM Compression | Gross margin | -[X]pp | [X]x | [X] mo | [PASS/CONDITIONAL/FAIL] |
| Combined Stress | All three above | Combined | [X]x | [X] mo | [PASS/CONDITIONAL/FAIL] |

**Most impactful variable**: [Variable name] — a [X]pp / [X]% adverse change shifts the gate from [PASS] to [CONDITIONAL/FAIL]

## Gate Decision and Conditions

[Formal verdict with binding conditions and monitoring triggers.

GUIDANCE:
- Good: Conditions are specific, measurable, time-bound, and assigned to a named owner.
- Bad: Conditional approval without defined thresholds or owners.
- Format: Decision block + conditions table]

**Gate Decision**: [PASS / CONDITIONAL PASS / FAIL]

**Composite Score**: [X.X] | **Grade**: [A+/A/B/C/D/F]

### Conditions (if CONDITIONAL PASS)

| # | Condition | Metric | Required Threshold | Deadline | Owner | Re-gate Trigger |
|---|-----------|--------|-------------------|----------|-------|-----------------|
| 1 | [Description] | [Metric] | [Threshold] | [Date] | [Owner] | [What triggers re-evaluation] |
| 2 | [Description] | [Metric] | [Threshold] | [Date] | [Owner] | [What triggers re-evaluation] |

## Recommendations

[Specific actions to improve or maintain unit economics viability.

- P1: [Critical conditions or blockers — must resolve before business model commitment]
- P2: [Important: improvements needed within 90 days to avoid re-gate failure]
- P3: [Monitoring setup: dashboards, alert thresholds, cadence for ongoing tracking]]

## Appendices

### A. Data Sources and Methodology

[Document each input source, calculation methodology, and any adjustments made to raw data]

### B. CAC Attribution Detail

[Breakdown of CAC components: sales headcount cost, marketing spend, tools, overhead allocation by channel]
