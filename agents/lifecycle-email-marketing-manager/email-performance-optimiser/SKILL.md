---
name: email-performance-optimiser
description: Runs systematic A/B tests across email programmes to maximise conversion rates and revenue per send.
department: marketing
agent: lifecycle-email-marketing-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# email-performance-optimiser

## Agent

L2 lifecycle and email marketing manager responsible for onboarding sequences, nurture campaigns, retention emails, re-engagement, and transactional email design.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Runs A/B tests on subject lines, send times, and content across all email programmes, then reports open, click, and conversion rates to continuously improve performance.

## When to Use

- Open rates or click-through rates drop below historical benchmarks for any email programme.
- A new email sequence launches and baseline performance data needs establishing through controlled experiments.
- Quarterly reviews reveal flat or declining conversion rates despite consistent send volume.
- The team debates a messaging or design change and needs data instead of opinions to decide.

## Workflow

1. Audit current email performance across all active sequences: open rate, click-through rate, conversion rate, unsubscribe rate, and revenue attributed per send.
2. Identify the highest-impact optimisation opportunities by calculating the revenue gap between current and benchmark performance for each sequence.
3. Formulate a test hypothesis for the top opportunity: specify the variable (subject line, send time, CTA, layout, or copy), the expected lift, and the minimum sample size for statistical significance.
4. Build the A/B test variant in the email platform. Ensure only one variable differs between control and test to isolate causation.
5. Launch the test to a randomised segment. Monitor deliverability and rendering during the first send window.
6. Wait for statistical significance before declaring a winner. Document the confidence level, sample size, and observed lift.
7. Roll the winning variant into production and update the sequence template. Archive the losing variant with learnings.
8. Publish a monthly optimisation report: tests run, winners deployed, cumulative lift in conversion and revenue, and the next round of test hypotheses.

## Anti-Patterns

- **Testing multiple variables simultaneously without a multivariate framework.** *Why*: Changing subject line and CTA in the same test makes it impossible to attribute which change caused the result.
- **Calling a winner before reaching statistical significance.** *Why*: Premature decisions based on small samples lead to false positives that degrade performance when rolled out.
- **Optimising for open rate while ignoring downstream conversion.** *Why*: A clickbait subject line can lift opens but tank conversions and increase unsubscribes, net-negative for revenue.
- **Running tests without a documented hypothesis.** *Why*: Random testing produces random learnings; hypothesis-driven testing builds a compounding knowledge base about what the audience responds to.

## Output

**Success artifacts:**
- A/B test briefs with hypothesis, variable, sample size, and success criteria
- Test result reports with statistical confidence and observed lift
- Monthly optimisation summary with cumulative performance improvement
- Updated email templates incorporating winning variants

**Failure reporting:**
- Flag tests with deliverability issues or rendering errors within 2 hours of launch
- Escalate sustained performance declines that persist after optimisation attempts to the marketing lead

## Related Skills

*No related skills defined yet.*
