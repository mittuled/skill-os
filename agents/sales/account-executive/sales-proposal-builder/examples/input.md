# Input: Sales Proposal — NovaTech Solutions

## Deal Context

- **Prospect**: NovaTech Solutions (Series C, $120M ARR, 600 employees)
- **Industry**: FinTech / Payment Processing
- **Deal stage**: Proposal
- **AE**: Jordan Blake
- **SE**: Alex Nguyen
- **Estimated ACV**: $95,000

## Confirmed Pain Points

1. Manual compliance reporting consuming 20 hours/week of senior engineering time
2. Deployment failures causing 3-4 production incidents per month
3. Audit trail gaps flagged in latest SOC 2 Type II audit
4. Current tooling (BuildMaster) lacks API extensibility, blocking automation roadmap

## Decision Criteria (from discovery)

- Must reduce compliance reporting effort by 75%+
- Must achieve <1% deployment failure rate
- Must provide audit-grade logging for SOC 2 compliance
- Must integrate with existing Jenkins, Datadog, and PagerDuty stack
- Decision timeline: contract signed by Q1 end (March 31)

## Budget and Authority

- Budget: $80K-$120K approved by VP Engineering (Claire Donovan)
- Economic Buyer: Claire Donovan, VP Engineering
- Champion: Raj Patel, Staff Engineer (evaluated 3 vendors, prefers us)
- Blocker: Mark Stevens, CISO (concerned about data residency)

## Competitors in Evaluation

- BuildMaster (incumbent) — renewing would be inertia play
- PipelineHQ — strong on CI/CD but weak on compliance features
