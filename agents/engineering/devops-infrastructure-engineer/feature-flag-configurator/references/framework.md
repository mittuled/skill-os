# Framework: Feature Flag Configurator

Defines the lifecycle, targeting patterns, and governance model for feature flags.

## Flag Lifecycle Stages

| Stage | State | Description | Max Duration |
|-------|-------|-------------|-------------|
| Created | Off everywhere | Flag exists in platform; code is deployed with flag guard | 1 sprint |
| Canary | On for internal users or 1–5% | Early validation in production | 1 week |
| Progressive rollout | On for increasing % | Percentage-based expansion with monitoring | 2 weeks |
| Full rollout | On for 100% of target segment | Feature fully live | Until cleanup deadline |
| Cleanup | Removed from code and platform | Code paths merged; flag deleted | 1 sprint after full rollout |

**Permanent flags are an anti-pattern.** Every flag must have a cleanup deadline set at creation time.

## Targeting Patterns

### User Segment Targeting

| Pattern | Use Case | Platform Implementation |
|---------|----------|------------------------|
| Internal users only | Dog-fooding before external exposure | User email matches `*@[company].com` |
| Beta opt-in | Voluntary early access | User attribute `beta_enrolled = true` |
| Percentage rollout | Gradual exposure | Consistent hashing on user ID, not session |
| Cohort rollout | A/B testing | Random assignment at first evaluation; sticky |
| Geographic rollout | Region-specific release | Country/region attribute match |
| Plan-based rollout | Feature behind paywall | Subscription tier attribute |

**Consistency rule**: Percentage rollouts must use sticky assignment (same user always sees the same variant). Never use random-per-request — it causes flickering and invalid A/B results.

### Environment Override Matrix

| Environment | Default State | Override Allowed | Notes |
|-------------|------------|-----------------|-------|
| Local dev | On | Yes | Developer override via `.env` |
| CI | On | No | Tests must cover both states |
| Staging | On | Yes | QA can toggle for test scenarios |
| Production canary | Off → % | Via targeting rules only | No manual override during rollout |
| Production | Per targeting rules | With change record | Requires approval for emergency toggles |

## Flag Naming Convention

```
[service]-[feature]-[variant]
```

| Component | Rule | Example |
|-----------|------|---------|
| service | Lowercase service name | `checkout` |
| feature | Dash-separated feature name | `new-payment-flow` |
| variant | Optional: `v2`, `experiment-a` | (omit if single variant) |

Full example: `checkout-new-payment-flow`, `api-rate-limit-v2`

## Documentation Requirements

Every flag must be documented in the flag platform with:

| Field | Required | Example |
|-------|----------|---------|
| Name | Yes | `checkout-new-payment-flow` |
| Description | Yes | "Enables redesigned payment form for Stripe PaymentElement migration" |
| Owner | Yes | `@team-payments` or `eng-payments@company.com` |
| Jira/Linear ticket | Yes | `ENG-1234` |
| Cleanup deadline | Yes | `2026-06-30` |
| Kill switch safe | Yes | "Disabled state returns to legacy Stripe Charges API" |

## Governance Controls

| Control | Trigger | Action |
|---------|---------|--------|
| Stale flag warning | Flag older than cleanup deadline | Automated Slack alert to owner |
| Stale flag escalation | Flag 2 weeks past cleanup deadline | Engineering manager notified |
| Stale flag removal | Flag 4 weeks past cleanup deadline | Flag removed from platform with 48h notice |
| Emergency toggle | Incident requiring instant rollback | Requires incident ticket; change logged automatically |
| Testing requirement | Before any flag exits staging | Both enabled and disabled states must pass CI |
