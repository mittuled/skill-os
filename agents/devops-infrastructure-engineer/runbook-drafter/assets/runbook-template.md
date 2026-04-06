# Runbook: [Service Name] — [Scenario Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | runbook-drafter |
| Service | [Service name and owner team] |
| Severity | [SEV-1 / SEV-2 / SEV-3 / SEV-4] |
| Alert Link | [Link to monitoring alert that triggers this runbook] |
| Last Tested | [YYYY-MM-DD or "Never"] |

## Executive Summary

[2-3 sentences describing the failure scenario, its business impact, and the primary recovery action.
GUIDANCE: Lead with user impact and the single most important action. Example: "This runbook covers a Postgres primary instance failure causing complete write outage. Primary action is to promote the replica to primary, which takes 3-5 minutes and requires no application changes."]

## Symptoms

[Observable indicators that this runbook applies to the current situation.

GUIDANCE:
- Good: "Alert fires: `postgres_primary_replication_lag > 30s` AND `postgres_write_errors > 0`. Health check URL `/health` returns 503. Application logs show: `FATAL: could not connect to the server`."
- Bad: "The database is not working."
- Format: Bullet list of exact alert names, error messages, and dashboard readings]

- Alert: `[exact-alert-name]` firing in [monitoring system]
- Error in logs: `[exact error string]`
- Dashboard indicator: [metric name] reads [threshold]

## Triage Steps

[Quick diagnostic commands to confirm the failure type before executing remediation.

GUIDANCE:
- Include exact commands with expected healthy vs. unhealthy output side-by-side.
- Mark each step with its expected execution time.
- Include a "this is a false positive if..." line where applicable.]

**Step 1 — Check service health** (30 seconds)
```bash
# Command here
# Expected healthy output:
# STATUS: OK, 0 errors
# Expected unhealthy output:
# ERROR: connection refused
```

**Step 2 — Check recent deployments** (1 minute)
```bash
# Command here — look for deployments in the last 30 minutes
```

**Step 3 — Identify failure scope** (2 minutes)
```bash
# Command to determine which hosts / regions are affected
```

→ If failure is limited to a single instance: proceed to [Remediation: Single Instance](#single-instance-remediation)
→ If failure affects all instances: proceed to [Remediation: Full Outage](#full-outage-remediation)
→ If no clear failure detected: this may be a false positive — see [False Positive Check](#false-positive-check)

## Remediation

### Single Instance Remediation

[Numbered steps, each with the exact command and expected output.

GUIDANCE:
- Good: "Step 1: Remove the failed instance from the load balancer target group. Command: `aws elbv2 deregister-targets ...`. Expected output: empty response indicating success. Verification: `aws elbv2 describe-target-health ...` should show instance in `unused` state."
- Bad: "Remove the instance from the load balancer."]

1. [Step with exact command]
   ```bash
   # Command
   ```
   Verify: [Verification command and expected output]

2. [Next step]

### Full Outage Remediation

1. [Step 1]
   ```bash
   # Command
   ```
   Verify: [Verification command]

### False Positive Check

[Steps to confirm a false alert before closing it.

GUIDANCE: Include the log query and dashboard view that confirm the system is actually healthy. Specify how long to monitor before closing the alert.]

## Post-Remediation Validation

[Steps to confirm full service recovery.

GUIDANCE: Include end-to-end health check, key metric recovery confirmation, and SLO burn rate check. These run after remediation regardless of which path was taken.]

1. Run end-to-end smoke test: `[command or URL to test]`
2. Verify error rate returns to baseline: [dashboard link / metric query]
3. Confirm SLO burn rate drops below threshold: [dashboard link]
4. Notify incident channel: `[Slack channel name]` — "Service [name] recovered at [time]. Incident ticket: [link]"

## Escalation Path

[When to escalate and to whom.

GUIDANCE: Specify timeout-based escalation — do not rely on human judgment to decide when to escalate.]

- After **15 minutes** without resolution: page `[on-call senior engineer]` via [paging system]
- After **30 minutes** without resolution: page `[incident commander]` and open incident in [incident management tool]
- If data loss is confirmed or suspected: immediately page `[VP Engineering]` regardless of timeline

## Rollback Instructions

[If this runbook involves making changes, document how to undo them.

GUIDANCE: Every change step should have a corresponding undo command.]

| Change Made | Undo Command |
|-------------|-------------|
| [Action from remediation] | `[Exact rollback command]` |

## Appendices

### A. Architecture Context

[Brief architecture diagram or description of the affected component. Include: key dependencies, data flow, and which other services depend on this one.]

### B. Common False Positives

[Known scenarios where this alert fires without a real incident. Include the distinguishing signal and the close-without-action procedure.]

| False Positive Scenario | Distinguishing Signal | Resolution |
|------------------------|----------------------|------------|
| [Scenario] | [What to look for] | [How to close] |

### C. Revision History

| Date | Author | Change Summary |
|------|--------|----------------|
| [YYYY-MM-DD] | [Name] | Initial draft |
