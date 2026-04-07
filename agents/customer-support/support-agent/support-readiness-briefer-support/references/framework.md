# Framework: Support Readiness Briefing

Defines the structure and content model for briefing the support team before a product release.

## Briefing Architecture

### Trigger Conditions

A readiness briefing is required when a release includes any of the following:
- New or changed user-facing features
- Breaking changes to existing workflows
- Changes to pricing, packaging, or billing
- API changes affecting integrations
- Deprecation of a feature with existing user adoption

### Briefing Format Selection

| Release Scope | Recommended Format | Delivery Window |
|---------------|-------------------|-----------------|
| Minor (1-2 UI changes) | Written async document | 48h before launch |
| Moderate (new feature or changed workflow) | Written doc + 30-min sync Q&A | 72h before launch |
| Major (new product, breaking changes, pricing) | Written doc + 60-min sync session + recorded video | 5+ days before launch |
| Breaking change with migration | Written doc + hands-on walkthrough + runbook updates | 7+ days before launch |

## Briefing Content Model

Every briefing must cover all five sections below, regardless of release scope.

### Section 1 — What Changed

| Element | Description |
|---------|-------------|
| Feature name | The official product name for the feature (matches what customers will see) |
| Change summary | 2-3 sentences: what existed before, what changed, and why |
| Affected customers | Which customer segments or tiers are affected (all customers / paying only / enterprise only) |
| Rollout scope | GA / beta / feature-flagged / phased rollout percentage |

### Section 2 — Expected Customer Questions

For each anticipated question, provide:
- The question customers are likely to ask
- The recommended agent response (in plain language)
- Whether there is a help article to link

| Question | Recommended Response | Help Article |
|----------|---------------------|-------------|
| [e.g., "Why did my dashboard change?"] | [Response text] | [URL or "Not yet published"] |

### Section 3 — Escalation Triggers

List scenarios where the agent should escalate rather than attempt resolution:
- Technical issues requiring engineering access
- Customer threats (churn, legal, executive escalation)
- Edge cases not covered by documented resolution paths

### Section 4 — Runbook and Macro Updates

| Update Type | Description | Status |
|-------------|-------------|--------|
| New runbook entry | [Scenario name] | [Draft / Published] |
| Updated runbook entry | [Scenario name] | [Draft / Published] |
| New macro | [Macro name and purpose] | [Draft / Published] |

### Section 5 — Known Issues and Workarounds

| Issue | Customer Impact | Workaround | Engineering ETA |
|-------|----------------|------------|-----------------|
| [Known bug or edge case] | [Impact description] | [Workaround steps] | [Date or "TBD"] |

## Delivery Quality Standards

- All customer-facing language must be in plain English, not engineering terminology
- Every "What Changed" section must be reviewed by product for accuracy
- Briefing must be delivered and confirmed received before the launch window opens
- Post-launch: collect agent feedback within 48h to identify briefing gaps for future releases
