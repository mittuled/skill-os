# Framework: Runbook Drafter

Defines the structure and standards for writing operational runbooks that enable consistent, rapid incident response.

## Runbook Types

| Type | Purpose | Trigger | Max Length |
|------|---------|---------|------------|
| Alert runbook | Response to a specific monitoring alert | PagerDuty / alerting system page | 2 pages |
| Maintenance runbook | Routine operational task | Scheduled or on-demand | 3 pages |
| Break-glass runbook | Emergency recovery procedure | Incident commander decision | 2 pages |
| Onboarding runbook | First-time setup for a new operator | On-call rotation entry | 5 pages |

## Runbook Structure Principles

1. **Action before context**: Put the diagnostic commands and remediation steps first. Background information belongs in an appendix.
2. **Exact commands**: Every command must be copy-pasteable. No placeholders unless clearly marked with `<REPLACE_ME>` syntax.
3. **Expected outputs**: After each diagnostic command, show the expected output for a healthy system so the operator can distinguish normal from abnormal.
4. **Decision points**: When the operator must choose between paths, use explicit branching: "If you see X → go to Step 4. If you see Y → go to Step 7."
5. **Validation steps**: Every remediation action must be followed by a verification step confirming it worked.

## Severity and Escalation Map

| Severity | Definition | Initial Response Time | Escalation Timeout | Escalation Path |
|----------|-----------|----------------------|-------------------|-----------------|
| SEV-1 | Full service outage or data loss | 5 minutes | 15 minutes | Incident commander → VP Engineering → CTO |
| SEV-2 | Significant degradation (> 10% error rate or > 2x latency) | 15 minutes | 30 minutes | On-call engineer → Senior engineer → Incident commander |
| SEV-3 | Minor degradation, no user impact | 1 hour | 4 hours | On-call engineer → Team lead |
| SEV-4 | Cosmetic or non-functional issue | Next business day | N/A | Team ticket queue |

## Runbook Backlog Prioritization

Score each candidate runbook to prioritize the order of creation:

| Factor | Weight | Score (1-5) | Notes |
|--------|--------|-------------|-------|
| Alert frequency | 35% | [score] | How often does this alert fire? |
| Business impact | 30% | [score] | Revenue or user impact of this failure? |
| Mean response time | 20% | [score] | How long does resolution currently take without a runbook? |
| Operator confidence | 15% | [score] | How often do engineers escalate this to a senior? |

**Priority Score** = Σ (score × weight). Runbooks scoring ≥ 4.0 are P1 — create before production go-live.

## Review and Maintenance Cadence

| Event | Action |
|-------|--------|
| Runbook used during incident | Review within 48 hours; update if any step was incorrect or missing |
| Service architecture change | Review all linked runbooks within 1 sprint |
| Quarterly review | Audit runbook library for stale commands, outdated screenshots, or changed service owners |
| New engineer on-call rotation | Walk new engineer through each P1 runbook before their first on-call shift |
