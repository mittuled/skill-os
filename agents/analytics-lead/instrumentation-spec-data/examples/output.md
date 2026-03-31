# Instrumentation Spec: User Signup Flow v1.0

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Feature | User Signup |
| Total Events | 3 |
| Skill | instrumentation-spec-data |

## Universal Properties (on every event)

| Property | Type | Required | Description |
|---------|------|----------|-------------|
| user_id | string | Yes | Unique user identifier |
| anonymous_id | string | Yes | Pre-login anonymous session ID |
| timestamp | datetime | Yes | ISO 8601 UTC event timestamp |
| session_id | string | Yes | Session identifier |
| platform | string | Yes | web \| ios \| android \| server |

## Event 1: signup_page_viewed

**Trigger**: Fired when the user navigates to or loads the page
**Firing location**: Client-side

| Property | Type | Required | Description |
|---------|------|----------|-------------|
| *universal properties* | — | Yes | See above |
| referrer_source | string | No | UTM source or referrer domain |
| variant | string | No | A/B test variant shown |

**Sample call**:
```js
analytics.track('signup_page_viewed', { user_id, timestamp, session_id, platform, referrer_source, variant });
```

**Query example**:
```sql
SELECT COUNT(*) FROM events WHERE event_name = 'signup_page_viewed' AND DATE(timestamp) = CURRENT_DATE()
```

## Event 2: signup_form_submitted

**Trigger**: Fired when the user submits the form successfully (after client validation passes)
**Firing location**: Client-side

| Property | Type | Required | Description |
|---------|------|----------|-------------|
| *universal properties* | — | Yes | See above |
| signup_method | string | Yes | email \| google \| github |
| plan_selected | string | No | Plan tier selected at signup |

## Event 3: account_created

**Trigger**: Fired server-side when the API endpoint responds with a success status
**Firing location**: Server-side (authoritative for signup counts)

| Property | Type | Required | Description |
|---------|------|----------|-------------|
| *universal properties* | — | Yes | See above |
| user_id | string | Yes | Newly created user ID |
| plan_tier | string | Yes | Assigned plan tier |

## Implementation Notes

1. Universal properties must be present on every event — use a shared event wrapper
2. Server-side `account_created` is the authoritative source for signup counts — do not use client-side `signup_form_submitted` for revenue or signup reporting
3. All events must be validated in staging before production rollout using the Segment debugger or equivalent
