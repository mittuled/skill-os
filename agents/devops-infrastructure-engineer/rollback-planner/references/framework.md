# Framework: Rollback Planner

Defines rollback complexity classification, trigger criteria, and procedure standards for deployment recovery planning.

## Rollback Complexity Classification

| Class | Characteristics | Rollback Approach | Rehearsal Required |
|-------|----------------|-------------------|-------------------|
| Simple | Code-only, stateless, no database changes | Redeploy previous artifact version | No |
| Moderate | Configuration changes, feature flag adjustments, additive schema migrations | Code revert + flag disable + retain new schema | Yes (staging) |
| Complex | Destructive schema migration, data transformation, multi-service coordinated deploy | Code revert + backward-compatible migration + data recovery | Yes (production-like staging) |
| Irreversible | Forward-only migration, no backward-compatible path | Partial rollback + emergency forward patch | N/A — escalate to VP Eng |

## Rollback Trigger Criteria

Triggers must be objective and measurable. "Things seem off" is not a trigger.

### Automatic Rollback Triggers (No Human Decision Required)

| Metric | Threshold | Action |
|--------|-----------|--------|
| Error rate | > [baseline + 1%] for 5 consecutive minutes | Auto-rollback if configured; else page immediately |
| p99 latency | > [baseline × 2] for 5 consecutive minutes | Page immediately |
| Health check failures | > 50% of instances fail health check for 2 minutes | Auto-rollback |
| Deployment error during rollout | Deployment controller reports failed instances | Halt deployment; assess |

### Human-Judged Rollback Triggers

| Signal | Assessment Time Limit | Default Action if Unresolved |
|--------|----------------------|------------------------------|
| Business metric drop > 5% | 10 minutes | Rollback |
| Unexpected error type in logs (not seen in pre-deploy baseline) | 5 minutes | Rollback |
| On-call instinct with supporting metric | 5 minutes to gather data | Rollback |

**Tie-breaking rule**: When rollback vs. forward-fix is ambiguous, bias toward rollback. The cost of an additional deployment is always less than the cost of a sustained production incident.

## Rollback Procedure Template Structure

Every rollback procedure document must contain:

1. **Complexity class** — Simple / Moderate / Complex / Irreversible
2. **Estimated rollback time** — How long the procedure takes from decision to restored service
3. **Data risk assessment** — Is any data at risk during or after rollback?
4. **Step-by-step procedure** — Exact commands in execution order
5. **Validation steps** — How to confirm the rollback succeeded
6. **Escalation path** — Who to notify if rollback takes longer than estimated or fails

## Schema Migration Rollback Strategies

| Migration Type | Rollback Strategy |
|----------------|------------------|
| Add nullable column | Drop the column |
| Add non-nullable column with default | Drop the column |
| Add non-nullable column without default | Complex — requires 3-phase migration pattern |
| Rename column | Maintain both names via view or application dual-write |
| Drop column | Cannot rollback without data restore — classify as Irreversible |
| Add index | Drop the index |
| Change column type | Complex — requires backward-compatible intermediate type |
| Change constraint | Drop or re-add the constraint |

## Rehearsal Requirements

| Rollback Class | Rehearsal Frequency | Environment | Pass Criteria |
|---------------|--------------------|-----------|-|
| Complex | Before every deployment of this type | Production-like staging | All steps complete; service healthy; data intact; time ≤ estimated duration |
| Moderate | Before first deployment of a new migration pattern | Staging | All steps complete; service healthy |
| Simple | No rehearsal required | — | — |

## Rollback Communication Templates

### Internal Notification (Slack/Teams)

```
ROLLBACK INITIATED
Service: [service name]
Time: [HH:MM UTC]
Reason: [Metric that triggered rollback — specific values]
ETA to restore: [estimated time]
Owner: [on-call engineer]
Incident: [link]
```

### Stakeholder Notification (for SEV-1/SEV-2)

```
[Time UTC] — We have initiated a rollback for [service] due to [impact description].
Estimated restore time: [ETA].
Updates every [X] minutes in [status page / channel].
```
