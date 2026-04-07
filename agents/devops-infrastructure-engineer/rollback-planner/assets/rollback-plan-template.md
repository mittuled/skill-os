# Rollback Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | rollback-planner |
| Deployment | [Deployment name / ticket / PR link] |
| Deploy Date | [Planned deployment date] |
| Rollback Class | [Simple / Moderate / Complex / Irreversible] |

## Executive Summary

[2-3 sentences covering the deployment's rollback complexity, estimated rollback time, and any data risk.
GUIDANCE: Lead with the rollback class and whether data is at risk. Example: "This deployment introduces a non-destructive additive schema migration (Moderate class). Rollback requires reverting the application artifact and retaining the new nullable column. Estimated rollback time: 8 minutes. No data loss risk."]

## Deployment Change Summary

[List what is being deployed that this rollback plan covers.

GUIDANCE:
- Good: "1) New user authentication service v2.3.1 (code only). 2) `users` table: add nullable column `sso_provider_id`. 3) Feature flag `auth-sso-migration` enabled to 10%."
- Bad: "New authentication feature."
- Format: Numbered list of specific changes]

1. [Application artifact: service name, version, repo commit]
2. [Database migration: migration name, type, reversible?]
3. [Configuration change: what changed from what to what]
4. [Feature flag change: flag name, new state]

## Rollback Complexity Assessment

[Explain why this deployment received its complexity classification.

GUIDANCE: Reference the specific change that drives the complexity rating. If a migration is involved, identify the migration type and rollback strategy from the framework.]

- **Classification**: [Simple / Moderate / Complex / Irreversible]
- **Primary complexity driver**: [e.g., "Destructive `DROP COLUMN` migration with no backward-compatible path"]
- **Data at risk**: [None / Description of risk]
- **Estimated rollback duration**: [X minutes from decision to service restored]
- **Rehearsal status**: [Not required / Rehearsed on YYYY-MM-DD in [environment]]

## Rollback Trigger Criteria

[Define the specific metric thresholds that should trigger a rollback decision.

GUIDANCE: Use exact numbers, not vague descriptions. The on-call engineer must be able to compare a dashboard value against this document and make a decision in seconds.]

| Metric | Rollback Trigger Threshold | Measurement Window |
|--------|---------------------------|-------------------|
| Error rate | > [X]% (baseline: [Y]%) | 5 consecutive minutes |
| p99 latency | > [X]ms (baseline: [Y]ms) | 5 consecutive minutes |
| Business metric | [Metric name] drops > [X]% | 10 minutes |
| Health check | > 50% instances failing | 2 consecutive minutes |

**Auto-rollback configured**: [Yes / No] — If yes, the deployment platform will trigger automatically.
**Rollback authority**: [On-call engineer / Incident commander] has unilateral authority to execute.

## Rollback Procedure

[Step-by-step procedure with exact commands. Steps must be in execution order.

GUIDANCE:
- Good: "Step 1: Disable feature flag `auth-sso-migration` in LaunchDarkly. Command: `ld --flag auth-sso-migration --state off`. Verify: error rate drops within 2 minutes."
- Bad: "Revert the deployment."
- Format: Numbered steps with exact commands and per-step verification]

**Step 1 — [Action name]** (Estimated: [X] seconds/minutes)
```bash
# Exact command
```
Verify: [How to confirm this step succeeded]

**Step 2 — [Action name]** (Estimated: [X] seconds/minutes)
```bash
# Exact command
```
Verify: [How to confirm this step succeeded]

**Step 3 — [Action name for migration if applicable]** (Estimated: [X] minutes)
```bash
# Exact rollback migration command
```
Verify: [Schema query to confirm migration was reversed]

## Validation Checklist

[Run after all rollback steps complete.

GUIDANCE: These are end-to-end validations, not just infrastructure checks. Include a business metric check.]

- [ ] Error rate returned to baseline range: [dashboard link]
- [ ] p99 latency returned to baseline range: [dashboard link]
- [ ] Health check endpoint returns 200: `[URL]`
- [ ] Business metric recovering: [metric name] at [expected value]
- [ ] Database schema confirmed: `[SQL query to verify schema state]`
- [ ] No new error types in logs for 5 minutes post-rollback

## Data Recovery Plan

[If this rollback risks data integrity, document the recovery steps.

GUIDANCE: If there is no data risk, write "No data at risk — this rollback is non-destructive." If there is risk, be specific about which records may be affected and how to recover them.]

[No data at risk — this rollback is non-destructive.]

— OR —

[Records affected: [description]. Recovery procedure: [steps]. DBA required: [Yes/No].]

## Escalation Path

| Time Since Rollback Start | Condition | Action |
|--------------------------|-----------|--------|
| 5 minutes | Rollback steps complete but service not recovered | Page senior engineer |
| 15 minutes | Service still degraded | Page incident commander; open SEV-1 |
| Any time | Data loss confirmed | Immediately page VP Engineering and DBA |

## Rehearsal Results

[Record rehearsal results if required for this complexity class.

GUIDANCE: Include the date, environment, who executed, actual time taken vs. estimated, and any steps that were incorrect in the plan.]

| Field | Value |
|-------|-------|
| Rehearsal date | [YYYY-MM-DD or "Not required"] |
| Environment | [Staging / Production-like staging] |
| Executed by | [Name] |
| Estimated time | [X minutes] |
| Actual time | [X minutes] |
| Issues found | [None / Description] |
| Plan updated | [Yes / No] |

## Appendices

### A. Related Runbooks

[Links to monitoring runbooks for incidents that may occur during this deployment.]

### B. Change Management Record

[Link to change management ticket, approval record, and deployment window authorization.]
