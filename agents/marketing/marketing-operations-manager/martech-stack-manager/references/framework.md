# Framework: martech-stack-manager

Defines the core stack layer model, vendor evaluation criteria, integration patterns, and total cost of ownership methodology for selecting and managing the marketing technology stack.

## Core Martech Stack Layers

Every marketing function requires coverage across these layers. Identify your tool for each:

| Layer | Purpose | Primary Tools (Examples) | Integration Priority |
|-------|---------|--------------------------|---------------------|
| **CRM** | Source of truth for leads, contacts, and deals | Salesforce, HubSpot CRM, Pipedrive | Critical — all layers sync to CRM |
| **Marketing Automation Platform (MAP)** | Lead nurture, email, scoring, campaign orchestration | Marketo, HubSpot Marketing, Pardot/Account Engagement | Critical — connects to CRM and all capture tools |
| **Customer Data Platform (CDP)** | Unified customer profile across all touchpoints | Segment, mParticle, RudderStack | High — enables identity resolution and audience building |
| **Analytics & Reporting** | Campaign performance, website analytics, attribution | Google Analytics 4, Looker, Tableau | Critical — connects to all active channels |
| **Ad Platforms** | Paid acquisition across search and social | Google Ads, LinkedIn Campaign Manager, Meta Ads | Critical — UTM + pixel integration to MAP and CRM |
| **Engagement / Personalization** | On-site and in-app personalization, chat | Drift, Intercom, Mutiny | Medium — integrates with MAP and CRM |
| **Content Management System (CMS)** | Website, landing page, and blog management | WordPress, Webflow, HubSpot CMS | High — form integration to MAP |
| **Event / Webinar Platform** | Virtual events, webinars, virtual demos | Zoom Webinars, On24, Demio | Medium — integrates with MAP for registration and attendance |
| **Sales Enablement** | Content library, sales collateral distribution | Highspot, Seismic, Notion | Low — one-directional from marketing to sales |

## Vendor Evaluation Matrix

Score each vendor 1–5 on each criterion. Weight by company priority.

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Feature fit to requirements | 25% | Does the tool cover 80%+ of stated requirements out-of-the-box? |
| CRM and MAP integration | 20% | Is the integration native, bidirectional, and field-mappable without custom code? |
| Total cost of ownership | 20% | License + implementation + training + ongoing admin cost over 3 years |
| Team adoption likelihood | 15% | Ease of use for the primary users; available training; support quality |
| Data security and compliance | 10% | SOC 2 Type II, GDPR compliance, data residency options |
| Scalability | 10% | Can the tool scale to 3× current volume without re-platforming? |
| **Composite** | **100%** | Score ≥ 3.5/5 to advance to shortlist |

## Integration Patterns

| Pattern | When to Use | Complexity | Risk |
|---------|------------|-----------|------|
| Native connector | Both tools have a certified integration | Low | Low |
| iPaaS middleware (Zapier, Make, Workato) | No native connector; low-volume use case | Low–Medium | Medium |
| API-to-API (custom) | High-volume; mission-critical; no native option | High | High |
| Webhook | Real-time event-triggered sync | Medium | Medium |
| CRM bidirectional sync | Any tool that creates or modifies contacts | High | High — data corruption risk if not mapped carefully |

**Integration documentation standard**: Every integration must have a data flow diagram, field mapping document, and test plan before go-live.

## Build vs. Buy vs. Renew Decision Criteria

| Scenario | Decision | Rationale |
|----------|---------|-----------|
| Vendor covers ≥ 80% of requirements at acceptable TCO | Renew / Buy | Cost-effective; integration maintained by vendor |
| Vendor covers < 60% of requirements | Replace | Better fit likely available |
| Internal team can build at < 50% of vendor TCO | Build | Only if team has capacity and security is manageable |
| Contract renewal with significant price increase (> 30%) | Re-evaluate | Request alternative quotes; use as leverage or trigger replacement |
| Category-defining capability gap (e.g., no CDP) | Invest | Missing layer creates downstream data quality debt |

## Stack Health Audit Criteria

Conduct semi-annual stack audit against these criteria:

| Category | Questions |
|----------|-----------|
| **Utilization** | Is this tool used by > 80% of licensed seats? Are all major features being used? |
| **Redundancy** | Does another tool in the stack do this job equally well? |
| **Integration health** | Are all integrations syncing without errors? Is field mapping current? |
| **Data quality** | Is the tool introducing duplicate records, data loss, or mapping errors? |
| **ROI** | Can we attribute operational efficiency or revenue impact to this tool? |
| **Contract risk** | Is the contract auto-renewing? When does it renew? What are cancellation terms? |

## Total Cost of Ownership Model

| Cost Component | Year 1 | Year 2 | Year 3 |
|---------------|--------|--------|--------|
| License / subscription | $[X] | $[X] | $[X] |
| Implementation / onboarding | $[X] | $0 | $0 |
| Integration development | $[X] | $[X] | $[X] |
| Internal admin time (FTE hours × rate) | $[X] | $[X] | $[X] |
| Training | $[X] | $[X] | $[X] |
| **3-year TCO** | | | **$[X]** |
