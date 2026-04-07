# Email Optimisation Programme Scoring: Q3 B2B SaaS Onboarding

## Scores

| Criterion | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Hypothesis Quality | 7 | 20% | 1.40 |
| Test Design Rigour | 6 | 25% | 1.50 |
| Statistical Discipline | 5 | 25% | 1.25 |
| Business Impact Measurement | 3 | 20% | 0.60 |
| Knowledge Compounding | 4 | 10% | 0.40 |
| **Composite** | | | **5.15** |

## Grade: C — Adequate

## Rationale

**Hypothesis Quality (7/10)**: Hypotheses are documented in Notion before launch, which is solid practice. However, some tests (CTA colour, emoji) lack a clear rationale for why the change would drive the target metric. The welcome email subject line test had a strong, audience-grounded hypothesis.

**Test Design Rigour (6/10)**: Most tests isolate a single variable correctly. The Day-7 content test was called at n=400 — far below the minimum sample size for reliable results. No evidence of pre-calculated sample sizes or holdout groups.

**Statistical Discipline (5/10)**: Some tests report p-values correctly (subject line, send time). However, the emoji test was reported as a "lift" despite p=0.08 exceeding the 0.05 threshold, and the Day-7 test was stopped early. No confidence intervals reported.

**Business Impact Measurement (3/10)**: Only email-level metrics (opens, clicks) are tracked. No connection to trial-to-paid conversion or revenue. The programme cannot demonstrate whether winning variants actually improve the business outcome.

**Knowledge Compounding (4/10)**: Results are shared verbally in standups but not archived. The team does not reference prior test data when designing new experiments, leading to risk of repeated tests and lost institutional knowledge.

## Recommendations

1. **P1**: Implement downstream conversion tracking per test variant — connect email engagement to trial-to-paid conversion within the analytics stack.
2. **P1**: Establish a minimum sample size calculator and enforce it before launching any test. Do not call tests early.
3. **P2**: Archive all test results in a searchable database with tags (variable type, sequence position, outcome). Reference prior results in new test hypothesis documents.
4. **P2**: Standardise the significance threshold at p < 0.05 and report confidence intervals alongside lift percentages.
5. **P3**: Add quantified expected lift to every hypothesis based on prior test data or industry benchmarks.
