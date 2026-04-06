# Framework: Revenue Attribution Monitoring

Defines the attribution model selection criteria, tracking configuration standards, and data quality monitoring protocol for multi-touch revenue attribution.

## Attribution Model Selection

| Model | Best For | Limitation |
|-------|----------|-----------|
| First-touch | Top-of-funnel channel investment decisions; understanding awareness drivers | Ignores all mid-funnel and closing-stage touchpoints |
| Last-touch | Bottom-of-funnel and closing-motion optimisation | Ignores awareness and nurture channels that built intent |
| Linear | Even credit across all touchpoints; simple to explain | Does not reflect the relative importance of each touchpoint |
| W-shaped | Balanced credit for awareness (first touch), lead creation, and opportunity creation | Ignores post-opportunity-creation touchpoints (e.g., proposal meetings) |
| Time-decay | Businesses with short sales cycles where recency matters most | Undervalues early-stage brand investment |
| Custom multi-touch | Companies with defined high-value touchpoints (e.g., demo = 30% credit) | Most complex to implement and maintain |

**Default recommendation**: W-shaped for B2B SaaS with deal cycles > 30 days.

## Tracking Configuration Standards

### UTM Parameter Convention

| Parameter | Purpose | Required Values |
|-----------|---------|-----------------|
| utm_source | Traffic source | google / linkedin / email / direct / referral / organic |
| utm_medium | Channel type | cpc / email / social / content / webinar |
| utm_campaign | Campaign name | [YYYY-QQ]-[campaign-name] (e.g., 2025-Q3-enterprise-webinar) |
| utm_content | Ad or content variant | [variant-name] for A/B testing |
| utm_term | Keyword (paid search) | Target keyword |

All inbound URLs from paid channels must include utm_source, utm_medium, and utm_campaign. Missing UTMs break attribution for that touchpoint.

### CRM Source Field Population

| Trigger | Source Field Value |
|---------|--------------------|
| UTM source captured | Map utm_source → CRM Lead Source |
| Direct website visit (no UTM) | "Direct" |
| Sales-created lead | "Outbound — [channel]" |
| Partner referral | "Partner — [partner name]" |
| Customer referral | "Customer Referral" |

### Touchpoint Capture Points

| Stage | Touchpoint Captured | System |
|-------|--------------------|----|
| First website visit | First-touch source via UTM or IP | Marketing automation |
| Form submission | Form-specific UTM + page URL | Marketing automation + CRM |
| Sales email | Email sent/opened/clicked | CRM email sync |
| Demo booked | Booking source (calendar tool) | CRM activity |
| Opportunity created | Last-touch source at creation | CRM |

## Data Quality Monitoring

Run the following checks on a weekly basis:

| Check | Threshold for Alert | Query Logic |
|-------|--------------------|----|
| Leads with missing Lead Source | > 5% of weekly new leads | Leads created in last 7 days WHERE LeadSource IS NULL |
| Opportunities with missing First-Touch | > 10% of new opps | Opportunities created in last 7 days WHERE FirstTouch IS NULL |
| UTM coverage on paid campaigns | < 95% of paid traffic | Paid channel visits WHERE utm_source IS NULL / Total paid visits |
| Broken UTM links | Any | UTM click-through → 404 or redirect dropping params |
| Untagged email campaigns | Any | Sent campaigns WHERE utm_medium != 'email' |

## Attribution Reporting Cadence

| Report | Frequency | Audience | Key Metric |
|--------|-----------|----------|------------|
| Channel Attribution Summary | Weekly | Marketing | Pipeline created by channel |
| Campaign ROI Report | Monthly | Marketing + Finance | Revenue attributed per $ spent |
| Attribution Audit | Quarterly | RevOps + Marketing | Data quality score + model review |
| Attribution Dispute Resolution | On demand | RevOps + Sales + Marketing | Specific deal or campaign disputed |
