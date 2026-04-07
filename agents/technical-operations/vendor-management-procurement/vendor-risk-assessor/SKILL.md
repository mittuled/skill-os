---
name: vendor-risk-assessor
description: >
  This skill assesses vendor risk including financial stability, security posture, and concentration risk.
  Use when asked to evaluate vendor reliability, conduct due diligence, or assess third-party risk.
  Also consider when a vendor handles sensitive data or is a single point of failure.
  Suggest when onboarding a new vendor for a critical business function.
department: technical-operations
agent: vendor-management-procurement
version: 1.0.0
complexity: medium
related-skills: []
---

# vendor-risk-assessor

## Agent: Vendor Management & Procurement

L1 vendor management and procurement function (1x) reporting to the COO, responsible for vendor contracts, risk assessment, procurement process, and vendor performance reviews.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The vendor risk assessor evaluates the risk profile of current and prospective vendors across financial stability, security posture, operational resilience, and concentration risk to protect the organisation from third-party failures.

## When to Use

- When a new vendor is being evaluated during the procurement process and risk assessment is required.
- When an existing vendor experiences a security incident, financial difficulty, or leadership change.
- When the organisation has high concentration risk with a single vendor for a critical function.
- When compliance frameworks require periodic third-party risk assessments.

## Workflow

1. **Define risk criteria**: Establish the risk dimensions to evaluate: financial stability, security posture, operational resilience, compliance, and concentration risk. Deliverable: risk assessment framework.
2. **Gather vendor information**: Request security questionnaires, SOC 2 reports, financial statements, and business continuity plans from the vendor. Deliverable: vendor information package.
3. **Assess each dimension**: Score the vendor on each risk dimension using the defined framework. Apply the scoring rubric at `references/scoring-rubric.md`. Deliverable: risk scorecard.
4. **Identify mitigations**: For elevated risks, define mitigation strategies such as contractual protections, backup vendors, or monitoring. Deliverable: risk mitigation plan.
5. **Document and recommend**: Compile the assessment into a risk report with a clear accept, mitigate, or reject recommendation. Deliverable: vendor risk assessment report.

## Anti-Patterns

- **Checkbox compliance**: Treating the assessment as a form to complete rather than a genuine evaluation of risk. *Why*: superficial assessments miss real risks and create false confidence.
- **Assessing only at onboarding**: Evaluating vendor risk once and never revisiting. *Why*: vendor risk profiles change over time; a stable vendor today may be financially distressed next year.
- **Ignoring concentration risk**: Assessing individual vendor risk without considering how much of the business depends on a single vendor. *Why*: even a low-risk vendor becomes a critical risk if it is the sole provider for essential infrastructure.

## Output

**On success**: A vendor risk assessment report with a risk scorecard, identified mitigations for elevated risks, and a clear accept/mitigate/reject recommendation.

**On failure**: Report which risk dimensions could not be assessed (e.g., vendor refused to share SOC 2 report), what was evaluated, and recommend whether to proceed with limited information or require the vendor to comply.

## Related Skills

- [`procurement-process-runner`](../procurement-process-runner/SKILL.md) -- risk assessment feeds into procurement evaluation scoring.
- [`vendor-contract-manager`](../vendor-contract-manager/SKILL.md) -- contract terms should reflect the mitigations identified in the risk assessment.
- [`vendor-performance-reviewer`](../vendor-performance-reviewer/SKILL.md) -- performance reviews may surface operational risks that trigger a reassessment.
