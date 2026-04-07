# SaaS Stack Management Framework

Reference for the `saas-stack-manager` skill.

---

## 1. SaaS Portfolio Categories

Organise the SaaS registry by functional category to identify overlap and consolidation opportunities.

| Category | Examples | Primary Owner |
|----------|---------|--------------|
| **Identity & Security** | Okta, 1Password, CrowdStrike | IT Operations |
| **Communication** | Slack, Zoom, Google Workspace | IT Operations |
| **CRM & Sales** | Salesforce, HubSpot, Outreach | Revenue Operations |
| **Marketing** | Marketo, Mailchimp, Semrush | Marketing Ops |
| **Engineering** | GitHub, Sentry, Datadog, PagerDuty | Engineering |
| **Product & Design** | Figma, Miro, Linear, Notion | Product / Design |
| **Finance & Legal** | Stripe, Ramp, DocuSign, Carta | Finance / Legal |
| **Customer Support** | Intercom, Zendesk, Loom | Customer Support |
| **HR & People** | Rippling, Lattice, Greenhouse | People Ops |
| **Data & Analytics** | dbt, Snowflake, Looker, Metabase | Data |

---

## 2. SaaS Registry — Required Fields

| Field | Description |
|-------|-------------|
| `tool_name` | Vendor and product name |
| `category` | Functional category from the table above |
| `owner` | Internal team or individual responsible |
| `licence_type` | Per-seat / flat fee / usage-based |
| `licence_count` | Number of licences purchased |
| `active_users_30d` | Users logged in within last 30 days |
| `utilisation_rate` | `active_users_30d / licence_count` |
| `annual_spend` | Total annual contract value |
| `renewal_date` | Contract renewal date |
| `auto_renews` | Yes / No |
| `payment_method` | Corporate card / invoice |
| `contract_owner` | Person responsible for renewal decision |
| `sso_integrated` | Yes / No |
| `data_classification` | Confidential / Internal / Public |
| `vendor_soc2` | SOC 2 Type II certified? Yes / No |
| `last_reviewed` | Date of last utilisation review |

---

## 3. Utilisation Thresholds

| Utilisation Rate | Classification | Action |
|-----------------|---------------|--------|
| >80% | Healthy | No action; monitor at renewal |
| 60–80% | Moderate | Review if lower-tier plan available |
| 40–60% | Low | Identify unused licences; downsize at renewal |
| 20–40% | Poor | Evaluate whether tool serves its purpose |
| <20% | Critical | Initiate cancellation review; likely consolidation candidate |

---

## 4. New Tool Evaluation Criteria

When a team requests a new SaaS tool, score against:

| Criterion | Weight | Questions to Answer |
|-----------|--------|---------------------|
| **Functional fit** | 30% | Does it solve the stated problem? Does it cover 80%+ of requirements? |
| **Existing stack overlap** | 25% | Does any current tool already do this? Can an existing tool be extended? |
| **Security posture** | 20% | SOC 2 certified? SSO supported? Data residency acceptable? |
| **Total cost** | 15% | Per-seat cost × projected users × 3 years vs. alternatives |
| **Integration compatibility** | 10% | APIs available? Connects to existing tools in the stack? |

**Scoring**:
- 85%+ → Approve
- 70–85% → Approve with conditions (e.g., SSO required before rollout)
- 50–70% → Defer: revisit existing tools first
- <50% → Deny: existing stack meets need or cost/risk not justified

---

## 5. Renewal Decision Framework

Review each renewal 60–90 days before the renewal date:

| Step | Action |
|------|--------|
| 1 | Pull utilisation data for the past 90 days |
| 2 | Interview the tool owner: Is the tool delivering value? |
| 3 | Review invoices: Are all licences justified? |
| 4 | Check the market: Are competitors offering better pricing? |
| 5 | Decide: Renew / Downsize / Upgrade / Cancel / Replace |
| 6 | Negotiate: Lead with utilisation data and competitive alternatives |

### Negotiation Leverage Points

- Low utilisation rate (use data to justify downsizing)
- Competitive alternatives available (name them)
- Long relationship / multi-year commitment offer
- Prepay annual vs. monthly for discount
- Reference customer or case study agreement

---

## 6. Shadow IT Detection and Response

| Detection Method | How |
|-----------------|-----|
| Credit card reconciliation | Review expense reports and card statements for SaaS subscriptions |
| SSO login monitoring | Flag authentication attempts to non-SSO-integrated apps |
| Employee offboarding | Departing employees often surface tools that only they knew about |
| Vendor billing notifications | Forward vendor invoices to IT for unknown tools |

**Response Protocol**:
1. Identify the tool and its owner
2. Assess risk (data stored, users, integrations)
3. If approved for continued use: onboard into managed stack (SSO, registry)
4. If not approved: offboard and data-migrate if needed
5. Communicate the managed procurement process to the requesting team

---

## 7. SaaS Consolidation Signals

Escalate to consolidation review when:

- Two or more tools serve the same primary use case
- A tool's utilisation has been <40% for two consecutive reviews
- A vendor has been acquired and roadmap is uncertain
- A single platform (e.g., Notion, Google Workspace) can replace multiple point solutions
- Annual spend on a category exceeds benchmark without corresponding utilisation

---

*Reference version 1.0 — Technical Operations / IT Operations Manager*
