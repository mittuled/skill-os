# Growth Dashboard Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Dashboard Name | [e.g., Growth AARRR Dashboard] |
| Platform | [Metabase / Looker / Amplitude / Mixpanel / Custom] |
| Primary Audience | [Growth Lead, Growth Engineer, Leadership] |
| Refresh Cadence | [Real-time / Hourly / Daily] |
| Skill | metrics-dashboard-growth |

## Dashboard Structure

The growth dashboard is structured in AARRR order — Acquisition at top, Referral at bottom.

| Section | Priority | Views Included |
|---------|----------|---------------|
| 0. Summary Scorecard | Top | 5 most important growth numbers |
| 1. Acquisition | High | Signups by channel, CAC, channel CVR |
| 2. Activation | High | Activation rate, time-to-activate, cohort curves |
| 3. Retention | High | D1/D7/D30/D90 retention, churn rate |
| 4. Revenue | High | MRR, ARPU, LTV, CAC payback |
| 5. Referral / Loops | Medium | Viral coefficient, referral rate, loop metrics |
| 6. Experiments | Medium | Active experiments, variant performance, significance |

---

## Section 0: Summary Scorecard

| KPI | Definition | Target | Current | Trend (WoW) |
|-----|-----------|--------|---------|-------------|
| Weekly Signups | COUNT(signup_completed) rolling 7 days | [target] | [current] | [▲/▼ X%] |
| Activation Rate (D7) | Activated users ÷ signups (D7 window) | [target] | [current] | [▲/▼ X pp] |
| D30 Retention | Users active in D28-D35 ÷ D0 cohort | [target] | [current] | [▲/▼ X pp] |
| MRR | Sum of monthly recurring revenue | [target] | [current] | [▲/▼ X%] |
| Blended CAC | Total acquisition spend ÷ new paid users | [target] | [current] | [▲/▼ X%] |

---

## Section 1: Acquisition Views

### View 1.1: Daily Signups by Channel

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Stacked bar chart (daily), line chart (trend) |
| X-axis | Date |
| Y-axis | Signup count |
| Dimensions | utm_source / channel grouping |
| Data source | `events.signup_completed` |
| Date range default | Last 30 days |
| Filters | Date range, plan type, geographic region |

**Channel grouping logic**:
- Paid search: utm_source IN ('google', 'bing') AND utm_medium = 'cpc'
- Paid social: utm_source IN ('linkedin', 'facebook', 'twitter') AND utm_medium IN ('cpc', 'paid')
- Organic: utm_medium = 'organic' OR utm_source IS NULL AND referrer IS NULL
- Email: utm_medium = 'email'
- Referral: utm_source = 'referral' OR referred_by_user_id IS NOT NULL
- Content/SEO: utm_medium = 'organic' AND utm_source IN ('google', 'bing')

### View 1.2: CAC by Channel

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Table with conditional formatting |
| Rows | Channel |
| Columns | Signups, Paid conversions, Spend ($), CAC ($), LTV:CAC |
| Data sources | `events.signup_completed` + marketing spend import |
| Date range default | Current month, prior month |

---

## Section 2: Activation Views

### View 2.1: Activation Rate by Signup Cohort

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Line chart (multiple cohort lines) |
| X-axis | Days since signup (0-30) |
| Y-axis | Cumulative activation rate (%) |
| Dimensions | Signup cohort (weekly or monthly) |
| Data source | `events.signup_completed` JOIN `events.activation_event` |
| Activation definition | [event_name, threshold, time window] |

### View 2.2: Time-to-Activation Distribution

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Histogram |
| X-axis | Hours/days to first activation event |
| Y-axis | User count |
| Key markers | Median, 75th percentile |

---

## Section 3: Retention Views

### View 3.1: Cohort Retention Table

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Retention heat-map table |
| Rows | Signup cohort (weekly) |
| Columns | D1, D7, D14, D28, D30, D60, D90 |
| Color scale | 0-100% (red → green) |
| Data source | `events.session_started` or `events.feature_used` |

### View 3.2: Retention Curves

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Line chart |
| X-axis | Day since signup |
| Y-axis | Retention rate (%) |
| Dimensions | Activated vs. non-activated cohorts; plan tier |

---

## Section 5: Referral / Loop Views

### View 5.1: Viral Coefficient Trend

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Line chart (weekly trend) |
| Y-axis | k = (referral_link_shared events / triggered users) × acceptance rate |
| Target line | [k = 0.20 target] |

### View 5.2: Loop Funnel

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Funnel chart |
| Stages | Trigger → Share → Click → Signup → Activation |
| Data sources | Loop events from instrumentation |

---

## Section 6: Experiment Views

### View 6.1: Active Experiments Table

| Spec Parameter | Value |
|---------------|-------|
| Chart type | Table |
| Columns | Experiment name, Variants, N per variant, Conversion rate (control), Conversion rate (variant), Lift, p-value, Status, Days to significance |
| Data source | `events.experiment_assigned` JOIN `events.[goal_event]` |
| Link | Each row links to detailed experiment analysis |

---

## Validation Checklist

Before publishing the dashboard:

- [ ] Each metric verified against raw warehouse query (spot-check 3 time periods)
- [ ] Channel grouping logic tested against known attribution data
- [ ] Retention curves produce expected values for known cohorts
- [ ] Experiment table shows correct sample sizes and conversion rates
- [ ] Dashboard documentation page written (metric definitions, caveats)
- [ ] Access permissions set: Growth team (edit), Leadership (view)
- [ ] Data freshness indicator present on all time-series charts
- [ ] Mobile view functional (for leadership access on mobile)
