---
name: vendor-performance-reviewer
description: >
  This skill conducts periodic vendor performance reviews against SLA and contract terms.
  Use when asked to evaluate vendor delivery, measure SLA compliance, or assess vendor value.
  Also consider when users report declining vendor service quality.
  Suggest when a vendor contract renewal is approaching and performance data is needed.
department: technical-operations
agent: vendor-management-procurement
version: 1.0.0
complexity: simple
related-skills:
  - vendor-contract-manager
  - vendor-risk-assessor
triggers:
  - "review vendor performance"
  - "vendor scorecard"
  - "vendor QBR"
  - "assess vendor delivery"
  - "evaluate supplier performance"
---

# vendor-performance-reviewer

## Agent: Vendor Management & Procurement

L1 vendor management and procurement function (1x) reporting to the COO, responsible for vendor contracts, risk assessment, procurement process, and vendor performance reviews.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The vendor performance reviewer evaluates vendor delivery against contractual SLAs, service quality expectations, and value-for-money criteria on a periodic basis to inform renewal, renegotiation, or replacement decisions.

## When to Use

- When a scheduled quarterly or annual vendor review is due.
- When users report declining service quality or repeated issues with a vendor.
- When a contract renewal is approaching and performance data is needed to inform the renewal decision.
- When the organisation needs to justify continued spend on a vendor to leadership.

## Workflow

1. **Gather performance data**: Collect SLA compliance data, incident reports, user satisfaction feedback, and usage metrics for the review period. Deliverable: raw performance dataset.
2. **Score against criteria**: Rate the vendor on agreed criteria: SLA adherence, responsiveness, quality, and value. Apply the scoring rubric at `references/scoring-rubric.md`. Deliverable: vendor scorecard.
3. **Identify issues**: Flag SLA breaches, recurring problems, and areas where delivery fell short of expectations. Deliverable: issue log with severity ratings.
4. **Conduct the review meeting**: Present findings to the vendor, discuss issues, and agree on improvement actions. Deliverable: review meeting notes with action items.
5. **Recommend action**: Based on the scorecard, recommend renew, renegotiate, or replace. Deliverable: vendor action recommendation.

## Anti-Patterns

- **Reviewing without data**: Conducting reviews based on subjective impressions rather than measured SLA data. *Why*: opinion-based reviews lack credibility with the vendor and provide no baseline for improvement tracking.
- **Review without consequences**: Identifying performance issues but taking no follow-up action. *Why*: vendors learn that underperformance is tolerated, and service quality continues to decline.

## Output

**On success**: A completed vendor scorecard with SLA compliance data, an issue log, review meeting notes with agreed action items, and a clear renewal recommendation.

**On failure**: Report which performance data was unavailable (e.g., vendor did not provide SLA reports), what partial assessment was completed, and recommend how to obtain missing data before the renewal deadline.

## Related Skills

- [`vendor-contract-manager`](../vendor-contract-manager/SKILL.md) -- contract management uses performance review data to inform renewal negotiations.
- [`vendor-risk-assessor`](../vendor-risk-assessor/SKILL.md) -- risk assessment complements performance review by evaluating vendor stability.
