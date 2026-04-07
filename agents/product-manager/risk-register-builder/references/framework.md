# Framework: Product Risk Register

## Core Model

Structured risk identification, scoring, and mitigation planning across four categories: delivery, technical, market, and compliance. Uses a likelihood x impact matrix to prioritise mitigation effort.

## Risk Categories

| Category | Scope | Example Risks |
|----------|-------|---------------|
| Delivery | Schedule, staffing, dependencies | Key engineer leaves, dependency team delays, scope creep |
| Technical | Architecture, scalability, integration | API rate limits, data migration failures, performance degradation |
| Market | Competition, timing, adoption | Competitor launches first, market window shifts, low adoption |
| Compliance | Regulatory, data privacy, contractual | New regulation, data residency violation, SLA breach |

## Likelihood x Impact Matrix

|  | Low Impact (1) | Medium Impact (2) | High Impact (3) |
|---|---|---|---|
| **High Likelihood (3)** | 3 (Medium) | 6 (High) | 9 (Critical) |
| **Medium Likelihood (2)** | 2 (Low) | 4 (Medium) | 6 (High) |
| **Low Likelihood (1)** | 1 (Low) | 2 (Low) | 3 (Medium) |

## Mitigation Strategies

| Strategy | When to Use | Example |
|----------|-------------|---------|
| Avoid | Risk can be eliminated by changing the plan | Remove dependency by building in-house |
| Reduce | Risk likelihood or impact can be decreased | Add integration tests, hire backup resource |
| Transfer | Risk can be shifted to another party | Insurance, vendor SLA with penalties |
| Accept | Risk is low enough to absorb if it materialises | Document rationale, set monitoring trigger |

## Trigger Threshold Pattern

For each high-severity risk, define:
- **Leading indicator**: Observable metric or event that signals risk materialisation
- **Threshold**: Specific value that triggers escalation
- **Escalation path**: Who is notified, what decision is made, within what timeframe

Example: "If API latency exceeds 500ms in staging for 3 consecutive test runs, escalate to tech lead within 4 hours for architecture review."

## Review Cadence

| Initiative Stage | Review Frequency | Trigger for Ad-Hoc Review |
|-----------------|-----------------|--------------------------|
| Active delivery | Per sprint | Scope change, dependency shift, team change |
| Roadmap-level | Monthly | Strategic pivot, competitive move, regulatory change |
| Post-launch | Quarterly | Adoption anomaly, incident, vendor change |
