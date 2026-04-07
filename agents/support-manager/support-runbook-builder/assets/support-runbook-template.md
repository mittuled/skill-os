# Support Runbook

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Support Manager / Senior Agent name] |
| Version | [1.0] |
| Status | [Draft / Review / Published] |
| Skill | support-runbook-builder |
| Last Reviewed | [YYYY-MM-DD] |
| Review Owner | [Name] |

---

# Runbook Entry: [Scenario Name]

*Duplicate this section for each scenario in the runbook library.*

## Trigger Conditions

[What symptoms or ticket content tells the agent to use this runbook.

GUIDANCE:
- Good: "Customer reports 'SAML assertion failed' or 'You don't have access' error after clicking SSO login button"
- Bad: "Login issues"
- Format: Bulleted list of specific observable conditions]

## Scope

**Tier**: [Tier-1 / Tier-2 / Engineering-only]

**Agent Prerequisites**: [List what the agent needs before starting — e.g., admin panel access, Datadog access, customer account ID]

## Diagnostic Steps

[Steps to identify the root cause. Each step = one action.

GUIDANCE:
- Good: "1. Open the customer's account in the admin panel. Search by email address."
- Bad: "1. Check the account and see what's wrong."
- Format: Numbered list; end each step with the expected result]

1. [Action] → Expected result: [What the agent should see]
2. [Action] → Expected result: [What the agent should see]
3. [Action] → Expected result: [What the agent should see]

## Resolution Paths

[Keyed to diagnostic outcomes. Each path ends with a resolution or escalation.]

### Path A: [Root Cause]

**Condition**: [What diagnostic step N revealed]

1. [Resolution action 1]
2. [Resolution action 2]
3. Confirm resolution: [What the agent and customer should see when fixed]

→ Use Response Template A (below)

### Path B: [Root Cause]

*(Repeat as needed)*

## Decision Tree

[For scenarios with 3+ resolution paths, provide a visual decision tree.

GUIDANCE:
- Good: Plain-text ASCII tree showing the diagnostic branch logic
- Bad: "Follow the steps above and use judgment"]

```
[Scenario Title]
  ├── [Diagnostic finding 1] → Path A
  ├── [Diagnostic finding 2] → Path B
  └── [Cannot determine] → Escalate (see below)
```

## Response Templates

### Template A — [Resolution outcome]

> [Customer-facing message. Use plain English. Include any action the customer needs to take.]

### Template B — [Resolution outcome]

> [Customer-facing message.]

### Template: Escalation to customer

> Thank you for your patience. I've gathered the information needed and am escalating your ticket to our [technical team / specialist team] for further investigation. You'll hear back within [SLA based on priority].

## Escalation Criteria

[Specific, observable conditions that require escalating beyond this tier.

GUIDANCE:
- Good: "Escalate to Engineering if: the error persists after completing Path A, OR the admin panel shows the account status as 'provisioning_error'"
- Bad: "Escalate if you can't fix it"]

Escalate to **[Team / Queue name]** when:

- [ ] [Specific condition 1]
- [ ] [Specific condition 2]
- [ ] Resolution has not been achieved after completing all diagnostic paths

**Escalation target**: [Queue name in ticketing system / Slack channel / Named contact]
**What to include in escalation**: [List of information to capture before escalating]

---

## Appendix: Response Time Targets

| Priority | First Response | Resolution |
|----------|---------------|------------|
| P0 | 1 hour | 4 hours |
| P1 | 4 hours | 8 hours |
| P2 | 8 hours | 24 hours |
| P3 | 24 hours | 72 hours |
