# Framework: Support Runbook Builder

Defines the structure, content standards, and maintenance model for operational support runbooks.

## Runbook Architecture

### Entry Structure

Every runbook entry contains exactly these components:

| Component | Purpose | Required |
|-----------|---------|----------|
| Title | Concise description of the scenario (e.g., "Customer cannot log in — SSO error") | Yes |
| Trigger Conditions | What symptoms or ticket content signals this runbook applies | Yes |
| Scope | Who handles this: Tier-1 / Tier-2 / Engineering-only | Yes |
| Prerequisites | Tooling access or information required before starting | Yes |
| Diagnostic Steps | Numbered steps to identify the root cause | Yes |
| Resolution Steps | Numbered steps to fix the issue, keyed to diagnostic outcomes | Yes |
| Decision Tree | Visual branch logic for scenarios with multiple resolution paths | For complex scenarios |
| Response Template | Customer-facing language for each resolution outcome | Yes |
| Escalation Criteria | Specific conditions that require escalation beyond this tier | Yes |
| Escalation Target | Named queue, team, or person to escalate to | Yes |

### Decision Tree Format

Use plain-text decision trees for scenarios with more than 2 resolution branches:

```
START: Customer cannot log in
  ├── SSO error message? → [SSO Runbook Section A]
  ├── Password reset not working?
  │   ├── Email not received → [Check email deliverability - Section B]
  │   └── Email received, link expired → [Resend reset link - Section C]
  └── Account locked? → [Unlock account - Section D]
```

### Runbook Tiers

| Tier | Scope | Escalation |
|------|-------|-----------|
| Tier-1 | How-to questions, common configuration steps, password resets, account updates | Escalate to Tier-2 if not resolved in 2 diagnostic steps |
| Tier-2 | Technical errors, API issues, data issues, integration failures | Escalate to Engineering if root cause requires code-level access |
| Engineering | Infrastructure issues, bugs, data corruption, security incidents | Engineering owns; support monitors and communicates |

## Scenario Prioritisation

Score each scenario for runbook priority using:

**Priority Score** = (Monthly ticket volume × 1.0) + (Average resolution time in hours × 0.5) + (Resolution time variance × 0.3)

Scenarios with the highest priority scores have the most impact on agent efficiency and should be documented first.

## Quality Standards

| Standard | Requirement |
|----------|-------------|
| Step length | Each diagnostic or resolution step is one action; no compound steps |
| Verification | Each resolution step includes what the agent should see to confirm it worked |
| Language | Plain English; no internal jargon or system names unfamiliar to a new agent |
| Escalation clarity | Escalation criteria are specific and observable, not subjective (e.g., "if the error persists after step 3", not "if it seems complicated") |
| Template completeness | Every resolution path has a corresponding customer-facing response template |

## Maintenance Triggers

| Trigger | Action | Timeline |
|---------|--------|----------|
| New feature launch | Create runbooks for predicted ticket types | Before launch |
| Post-mortem finding | Update runbook if agents improvised during an incident | Within 1 week |
| Agent feedback | Update when an agent reports a runbook was missing a step | Within 1 sprint |
| Quarterly review | Full library review; deprecate stale entries | Quarterly |
| CRM routing change | Update escalation targets in all affected runbooks | Same day |
