# Instrumentation Verification Report (QA): [Feature / Release Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | QA / Test Engineer |
| Feature | [Feature or release name] |
| Environment | QA / Staging |
| Skill | instrumentation-verifier-qa |
| Status | [Pass / Fail / Conditional Pass] |

## Verdict

**Result**: [PASS / FAIL / CONDITIONAL PASS]
**Events verified**: [N of N required events passing]
**Events failing**: [N]

## Event Verification

### Required Events

| Event Name | Trigger | Properties Required | Result | Notes |
|-----------|---------|--------------------|----|------|
| [page_view] | [User navigates to any page] | [page_name, user_id, timestamp] | [Pass/Fail] | |
| [button_click] | [User clicks primary CTA] | [button_id, page_name, user_id] | | |
| [form_submitted] | [Form submit success] | [form_id, field_count, user_id] | | |
| [purchase_completed] | [Order confirmed] | [order_id, amount, currency, items] | | |
| [error_shown] | [Error displayed to user] | [error_code, page_name] | | |

### Event Property Validation

For each passing event, verify all required properties:

| Event | Property | Expected Type | Expected Value | Actual Value | Pass? |
|-------|----------|--------------|----------------|-------------|-------|
| [page_view] | page_name | string | [e.g., "checkout"] | [Actual] | |
| [page_view] | user_id | string (UUID) | [authenticated user UUID] | [Actual] | |
| [purchase_completed] | amount | number (cents) | [> 0] | [Actual] | |
| [purchase_completed] | currency | string (ISO 4217) | [e.g., "USD"] | [Actual] | |

### Negative Tests (Events That Should NOT Fire)

| Event | Condition | Expected | Result |
|-------|-----------|---------|--------|
| [purchase_completed] | User abandons cart | Should not fire | [Pass: not fired / Fail: fired] |
| [user_signed_up] | User logs in (not new signup) | Should not fire | |

## Duplicate Event Check

| Event | Expected Fires per Action | Actual Fires | Duplicates? |
|-------|--------------------------|-------------|------------|
| [button_click] | 1 per click | [N] | [Yes/No] |
| [page_view] | 1 per navigation | [N] | |

## Data Layer Verification

| Variable | Expected | Actual | Pass? |
|----------|---------|--------|-------|
| [dataLayer.userId] | [Authenticated user UUID] | [Actual] | |
| [dataLayer.pageCategory] | [e.g., "product"] | [Actual] | |

## Tools Used

| Tool | Purpose | Result Summary |
|------|---------|---------------|
| [Chrome DevTools / Network tab] | Verify event payloads sent | [N events validated] |
| [Analytics debug mode] | Validate event names and properties | [N events passing] |
| [Tag Inspector / Datadog RUM] | Catch duplicate or missing events | [N issues found] |

## Failing Events — Details

| # | Event | Failure Type | Evidence | Fix Required |
|---|-------|-------------|---------|-------------|
| 1 | [Event name] | [Missing / Wrong property / Fires when it shouldn't] | [Screenshot or payload] | [Specific fix] |

## Sign-off

- [ ] All required events fire on expected user actions
- [ ] No duplicate events
- [ ] All required properties present with correct types and values
- [ ] No events fire on unexpected user actions
- [ ] Data layer variables match expected values

**QA Sign-off**: [Name] | Date: [YYYY-MM-DD]
