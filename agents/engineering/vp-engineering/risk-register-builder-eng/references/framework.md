# Framework: risk-register-builder-eng

Guides the construction and maintenance of engineering risk registers using structured risk identification, assessment, and mitigation planning.

## Risk Register Entry Standard

Every risk entry must contain:

| Field | Format |
|-------|--------|
| Risk ID | R-001, R-002, etc. |
| Description | One sentence: what could happen and its impact |
| Category | Technical / Operational / Resource / External / Security |
| Likelihood | Low (< 20%) / Medium (20-60%) / High (> 60%) |
| Impact | Low (minor delay) / Medium (phase delay) / High (milestone missed) / Critical (project failure) |
| Risk Score | Likelihood × Impact matrix value (see below) |
| Mitigation Strategy | Avoid / Reduce / Transfer / Accept |
| Mitigation Actions | Specific steps to execute the strategy |
| Owner | Named individual |
| Status | Open / Mitigating / Accepted / Closed |
| Date Identified | YYYY-MM-DD |
| Review Date | Next scheduled review date |

## Risk Score Matrix

|  | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|--|----------------|-------------------|-----------------|---------------------|
| **High Likelihood (3)** | 3 - Medium | 6 - High | 9 - Critical | 12 - Critical |
| **Medium Likelihood (2)** | 2 - Low | 4 - Medium | 6 - High | 8 - High |
| **Low Likelihood (1)** | 1 - Low | 2 - Low | 3 - Medium | 4 - Medium |

## Risk Categories

| Category | Examples |
|----------|----------|
| Technical | Unproven technology, integration complexity, scalability limits, data migration risk |
| Operational | Deployment complexity, monitoring gaps, on-call burden, rollback difficulty |
| Resource | Key-person dependency, skill gaps, team attrition, competing priorities |
| External | Third-party API changes, vendor reliability, regulatory changes, partner timeline |
| Security | Unreviewed threat model, dependency vulnerabilities, data exposure, auth gaps |

## Mitigation Strategy Selection

| Strategy | When to Use | Example |
|----------|------------|---------|
| Avoid | Risk is unacceptable and can be eliminated by changing approach | "Use proven database instead of experimental one" |
| Reduce | Risk cannot be eliminated but can be lowered | "Conduct spike to reduce uncertainty" |
| Transfer | Risk can be shifted to another party | "Use managed service instead of self-hosting" |
| Accept | Risk is low enough or mitigation cost exceeds impact | "Accept that third-party API may change; monitor changelog" |

## Review Cadence

| Trigger | Action |
|---------|--------|
| Phase boundary | Full register review; close mitigated risks; assess new risks |
| After incident | Assess whether incident reveals new risks |
| Scope change | Evaluate risk impact of added/removed scope |
| Sprint planning | Quick scan for risks that affect sprint tasks |
| Retrospective | Cross-reference retrospective findings with risk register |

## Escalation Thresholds

| Risk Score | Required Action |
|-----------|-----------------|
| 1-3 (Low) | Monitor; review at phase boundary |
| 4-6 (Medium) | Active mitigation required; review weekly |
| 7-9 (High) | Escalate to VP Engineering; mitigation plan within 48 hours |
| 10-12 (Critical) | Escalate to CTO; mitigation plan within 24 hours; consider scope/timeline change |
