---
name: freelancer-contract-reviewer
description: >
  This skill reviews freelancer and contractor agreements through 14
  freelancer-specific analysis lenses including worker classification risk
  using the IRS 20-factor test. Use when engaging freelancers, contractors,
  or gig workers. Also consider when converting employees to contractor status
  or vice versa. Suggest when HR or hiring manager sends a contractor agreement
  for review.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../contract-review-orchestrator/SKILL.md
  - ../negotiation-strategist/SKILL.md
triggers:
  - "review freelancer contract"
  - "contractor agreement review"
  - "worker classification risk"
  - "independent contractor review"
---

# freelancer-contract-reviewer

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Reviews freelancer and contractor agreements through 14 freelancer-specific analysis lenses including worker classification risk using the IRS 20-factor test and the ABC test.

## When to Use

- When the company engages a freelancer, independent contractor, or consultant and needs the agreement reviewed before signing.
- When converting an employee to contractor status (or vice versa) and the engagement terms must be assessed for misclassification risk.
- When HR or a hiring manager submits a contractor agreement that includes provisions (exclusivity, fixed schedule, company tools) that may indicate misclassification.

## Workflow

1. **Classify Engagement Type**: Determine the engagement type: independent contractor, consultant, freelancer, or agency temp. Record the engagement duration, hours expected, and whether the worker serves multiple clients. Deliverable: engagement classification with key parameters.

2. **Apply Classification Tests**: Apply the IRS 20-factor test scoring each factor as Employee-like, Neutral, or Contractor-like. Apply the ABC test (California AB5) if the worker is California-based. Use the framework (see [framework.md](references/framework.md)) for detailed scoring criteria. Deliverable: completed classification test results with per-factor scores.

3. **Analyze Through 14 Lenses**: Review the agreement through all 14 freelancer-specific lenses: IP ownership, work product rights, payment terms, expense reimbursement, insurance requirements, non-compete/non-solicit, termination provisions, confidentiality, liability allocation, tax obligations, exclusivity, work schedule control, tool/equipment provision, and integration into business operations. Deliverable: 14-lens analysis with finding, risk level, and recommendation per lens.

4. **Score Dual Risk Axes**: Score the agreement on two axes using the scoring rubric (see [scoring-rubric.md](references/scoring-rubric.md)): Classification Risk (behavioral control, financial control, relationship type) and Contractual Risk (IP protection, liability, termination, payment). Calculate composite scores for each axis. Deliverable: dual-axis risk scores with per-criterion ratings.

5. **[GATE] Flag High-Risk Provisions**: Identify provisions that create elevated misclassification risk or contractual exposure. Flag compound red flags (e.g., exclusivity combined with full-time hours, company-provided tools combined with fixed schedule). Deliverable: high-risk provision register with compound risk analysis.

6. **Produce Review Report**: Assemble the final report using the template (see [freelancer-review-report-template.md](assets/freelancer-review-report-template.md)). Include dual risk scores, IRS 20-factor assessment, 14-lens analysis, high-risk provisions, and recommended modifications. Deliverable: freelancer contract review report delivered to requesting attorney, HR, or hiring manager.

## Anti-Patterns

- **Contract-text-only review**: Reviewing only the written agreement without considering the actual working arrangement. *Why*: courts and the IRS evaluate the reality of the relationship, not just the contract language; a contract calling someone a "contractor" does not prevent misclassification liability if the actual arrangement resembles employment.

- **Ignoring state-specific tests**: Applying only the IRS 20-factor test without considering stricter state tests like California's ABC test. *Why*: several states apply more restrictive classification tests than the federal standard; a worker who passes the IRS test may still be classified as an employee under state law.

- **Treating all contractors identically**: Applying the same risk assessment regardless of engagement duration, hours, or exclusivity. *Why*: a one-month project-based engagement carries fundamentally different classification risk than a 12-month full-time exclusive arrangement; risk assessment must scale with engagement intensity.

## Output

**On success**: Produces a freelancer contract review report containing dual risk scores (classification and contractual), IRS 20-factor assessment table, 14-lens analysis with findings and recommendations, high-risk provision register, and recommended contract modifications. Delivered to the requesting attorney, HR team, or hiring manager.

**On failure**: Report which analysis lenses could not be completed (e.g., missing information about actual working arrangement, unknown state jurisdiction), what partial risk assessment is available, and what additional information is needed. Include the partial report with confidence qualifiers on incomplete sections.

## Related Skills

- [`contract-review-orchestrator`](../contract-review-orchestrator/SKILL.md) -- Freelancer contracts that exceed risk thresholds should be escalated to full contract review orchestration for deeper analysis.
- [`negotiation-strategist`](../negotiation-strategist/SKILL.md) -- High-risk provisions identified in the review inform negotiation strategy for modifying contractor terms.
