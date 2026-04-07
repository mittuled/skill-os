# Cohort Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Operations Analyst] |
| Feature | [Feature name and flag identifier] |
| Rollout Phase | [Phase 1 / Phase 2 / GA] |
| Skill | cohort-selector |

## Rollout Objective

[One paragraph describing what this rollout needs to prove, the primary metric being tested, and the minimum success threshold.
GUIDANCE: State the hypothesis — "If we roll out X to cohort Y, we expect to see Z metric move from A to B within N days."]

## Cohort Definition

### Inclusion Criteria

[Explicit rules that qualify a user or account for the cohort.

GUIDANCE:
- Good: "Plan tier = Pro or Enterprise; account age >= 30 days; not currently in Feature Flag X experiment; geography = US or UK"
- Bad: "Active users"
- Format: Bulleted list with each rule on its own line]

### Exclusion Criteria

[Explicit rules that disqualify a user or account.

GUIDANCE: Always include the standard exclusions (onboarding users, other A/B tests, churned accounts) plus any feature-specific ones.]

## Cohort Size and Percentage

| Dimension | Value |
|-----------|-------|
| Total eligible population | [N users / N accounts] |
| Cohort percentage | [X%] |
| Expected cohort size | [N users / N accounts] |
| Statistical power | [80% power at 95% confidence to detect MDE of X pp] |

## Representativeness Validation

| Dimension | Cohort % | Population % | Delta | Pass/Fail |
|-----------|----------|-------------|-------|-----------|
| Plan: Free | | | | |
| Plan: Pro | | | | |
| Plan: Enterprise | | | | |
| Geography: US | | | | |
| Geography: Other | | | | |
| Account age < 90 days | | | | |

## Risk Assessment

| Risk Tier | [Low / Medium / High / Critical] |
|-----------|----------------------------------|
| Revenue at risk (ARR) | [$X] |
| SLA exposure | [Yes / No — detail if yes] |
| Reversibility | [Instant flag-off / Migration required] |
| Key account exposure | [List any top-10 accounts in cohort] |

## Rollback Triggers

[Specific, measurable conditions that trigger pause or rollback.

GUIDANCE:
- Good: "Pause if server error rate exceeds 2% (baseline: 0.3%) for 2 consecutive hours. Rollback if Pro-tier activation drops >10% below baseline for 48 hours."
- Bad: "Roll back if something breaks"
- Format: Numbered list of trigger conditions with metric, threshold, and duration]

## Approvals Required

| Approver | Role | Required for |
|----------|------|-------------|
| [Name] | Product Manager | Cohort strategy sign-off |
| [Name] | Engineering Lead | Technical feasibility |
| [Name] | CS / Account Manager | Enterprise account exposure (if applicable) |
