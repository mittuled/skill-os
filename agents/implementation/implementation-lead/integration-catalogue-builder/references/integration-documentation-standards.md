# Integration Documentation Standards

Reference for the `integration-catalogue-builder` skill.

---

## 1. Integration Catalogue Structure

Every integration in the catalogue must have its own entry following this structure:

```
catalogue/
└── <integration-name>/
    ├── overview.md        # Purpose, status, supported versions
    ├── setup-guide.md     # Step-by-step configuration instructions
    ├── data-mapping.md    # Field mapping between systems
    └── troubleshooting.md # Common errors and resolutions
```

---

## 2. Integration Status Definitions

| Status | Definition | Customer Visibility |
|--------|-----------|---------------------|
| **GA (Generally Available)** | Fully supported, documented, and tested | Listed in public catalogue |
| **Beta** | Functional but may have known gaps; limited support | Listed with Beta label and disclaimer |
| **Early Access** | Available to select customers on request | Not publicly listed; mention on request |
| **Deprecated** | No new customers; existing users supported until EOL date | Listed with deprecation notice and migration path |
| **EOL (End of Life)** | No longer supported; migration required | Listed with EOL date; migration guide linked |
| **Planned** | On the roadmap; not yet available | Not listed until at least Early Access |

---

## 3. Integration Setup Guide Template

Each setup guide must cover:

### Overview Section
- Integration name and version
- Status (GA / Beta / Deprecated)
- What the integration does and what data it syncs
- Supported platforms/versions of the third-party system
- Known limitations

### Prerequisites Section
- Required plan tier (which product plans include this integration)
- Required third-party system version or plan
- API credentials or tokens needed (what type, what permissions)
- Network / firewall requirements (if applicable)
- Who needs to be involved on the customer side

### Step-by-Step Configuration
Numbered steps with:
- Screenshots or UI navigation paths
- Exact field values and formats expected
- Explanation of non-obvious settings
- Test step to verify each major configuration block

### Authentication Guide
- Authentication method: API key / OAuth 2.0 / SAML / Basic Auth
- Where to generate or obtain credentials in the third-party system
- Scope / permission requirements
- Token rotation or expiry handling

### Data Mapping Reference
- Source system field → Product field mapping
- Data type conversions applied
- Required vs. optional field mappings
- Fields that are read-only or system-managed

### Testing Section
- How to verify the integration is working
- Sample test data or test scenario
- How to check sync status and logs

---

## 4. Known Limitations Documentation Standard

Every integration entry must explicitly document limitations. Never omit limitations from the catalogue.

| Limitation Type | Example | Documentation Format |
|----------------|---------|---------------------|
| **Feature gap** | "Attachment sync not supported" | State clearly; link to workaround if available |
| **Data volume** | "Syncs up to 100,000 records per run" | State the limit and what happens at the limit |
| **Update frequency** | "Syncs every 15 minutes; real-time not supported" | State frequency and any manual trigger option |
| **Version dependency** | "Requires Salesforce API v52 or higher" | State minimum version; link to version check guide |
| **Geographic / compliance** | "Data residency: EU only for GDPR requirements" | State clearly; link to compliance documentation |
| **Rate limits** | "Subject to third-party API rate limits: 500 calls/min" | State the limit and how to handle rate-limiting errors |

---

## 5. Integration Category Taxonomy

Organise the catalogue by category for discoverability:

| Category | Examples |
|----------|---------|
| **CRM** | Salesforce, HubSpot, Pipedrive |
| **Marketing Automation** | Marketo, Mailchimp, HubSpot Marketing |
| **Identity / SSO** | Okta, Azure AD, Google Workspace |
| **Billing / Finance** | Stripe, Chargebee, QuickBooks |
| **Communication** | Slack, Microsoft Teams, Zoom |
| **Analytics** | Snowflake, BigQuery, Looker |
| **Storage / Files** | AWS S3, Google Drive, Dropbox |
| **Customer Support** | Zendesk, Intercom, Freshdesk |
| **Productivity** | Notion, Confluence, Jira |
| **Custom / Webhook** | Generic webhook, REST API |

---

## 6. Catalogue Maintenance Schedule

| Task | Frequency | Owner | Trigger |
|------|-----------|-------|---------|
| Review all GA integrations for accuracy | Quarterly | Implementation Lead | Calendar |
| Update documentation after product version changes | With each release | Implementation Engineer | Release notes |
| Add new integrations | On GA launch | Implementation Lead | Engineering ship |
| Update deprecated integrations | On deprecation decision | Implementation Lead | Product decision |
| Audit for broken screenshots or links | Quarterly | Implementation Engineer | Calendar |
| Review integration usage data | Semi-annually | Implementation Lead | Analytics report |

---

## 7. Integration Documentation Quality Checklist

Before publishing any integration guide:

- [ ] Status is clearly stated (GA / Beta / Deprecated)
- [ ] Prerequisites are complete and accurate
- [ ] Step-by-step guide is tested end-to-end with the current product version
- [ ] All known limitations are documented
- [ ] Authentication section covers token scopes and rotation
- [ ] Data mapping table is accurate and complete
- [ ] Troubleshooting section covers at least 3 common errors
- [ ] A non-expert can follow the guide without assistance
- [ ] Screenshots reflect the current UI (not outdated)
- [ ] Version numbers for both the product and third-party system are specified

---

*Reference version 1.0 — Implementation / Implementation Lead*
