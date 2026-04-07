# Implementation Discovery Framework

Reference for the `implementation-requirements-extractor` skill.

---

## 1. Requirements Domains

Every implementation discovery must cover all five domains. Incomplete discovery in any domain is a risk to on-time, on-scope delivery.

| Domain | What to Capture | Common Blind Spots |
|--------|----------------|-------------------|
| **Functional** | Business workflows, user journeys, reporting needs | Edge cases and exceptions to standard workflow |
| **Technical** | Infrastructure, OS, browsers, network, APIs | Legacy systems, on-premise constraints |
| **Integration** | Which systems connect, data direction, field mapping | Auth method requirements, rate limits, data residency |
| **Data Migration** | Source data format, volume, quality, mapping | Historical data quality, deduplication rules |
| **Acceptance Criteria** | How the customer will know implementation is done | Unmeasurable success criteria ("it just works") |

---

## 2. Discovery Question Bank

### Functional Requirements

1. Walk me through how your team currently handles `[core use case]` today, step by step.
2. Who are the primary users of this system, and what are their daily workflows?
3. What reports or dashboards must exist on day one for go-live to be successful?
4. What are the non-negotiable features you need on day one vs. nice-to-haves in phase 2?
5. Are there any exception workflows or edge cases we should know about?
6. How many users will use this system, and across how many teams or offices?
7. What does a successful outcome look like to your team 90 days after go-live?

### Technical Requirements

1. What operating systems and browser versions do your users work with?
2. Do you have any network restrictions (firewalls, allowlists, proxy servers)?
3. Is your infrastructure on-premise, cloud, or hybrid?
4. Do you have SSO requirements? Which identity provider do you use?
5. What are your security policies around data storage and access logging?
6. Are there any compliance requirements we need to meet (HIPAA, SOC 2, GDPR)?

### Integration Requirements

1. Which systems do you need us to connect to? List all, including the ones you're unsure about.
2. For each integration: what data needs to flow, in which direction, and how often?
3. What authentication methods does each system support (API key, OAuth, etc.)?
4. Are there API rate limits or data volume constraints we should know about?
5. Who owns admin access for each system to set up the integration?
6. Have you integrated your existing systems before? What issues came up?

### Data Migration Requirements

1. Where does your existing data currently live?
2. How many records are we migrating? (Contacts, accounts, deals, historical data)
3. What is the format of your current data? (CSV, API export, database dump)
4. How important is historical data vs. starting fresh?
5. Are there duplicate records in your current data we need to handle?
6. Who on your team can provide and validate the data export?

### Acceptance Criteria

1. What specific tests will you run to confirm implementation is complete?
2. Who has final sign-off on go-live readiness on your side?
3. What would cause you to delay go-live?
4. How will you measure success in the first 30 days after go-live?
5. What is your target go-live date, and is there any flexibility?

---

## 3. Sales Handoff Review Checklist

Before the first discovery session, review the sales handoff for:

- [ ] SOW (Statement of Work) — what was sold and committed
- [ ] Deal notes — any promises made during sales cycle
- [ ] Pre-sales technical notes — any technical investigation completed
- [ ] Contract terms — timeline commitments, SLAs, payment milestones
- [ ] Champion and stakeholder map — who to involve in discovery
- [ ] Pricing tier — determines which features and integrations are included
- [ ] Identified risks or concerns from the sales team

**Red flags to escalate before discovery starts**:
- SOW promises a feature not yet in the product
- Timeline is shorter than the standard tier duration
- Customer has conflicting requirements described in deal notes
- No technical contact identified on the customer side

---

## 4. Requirements Document Structure

The completed requirements document must include:

| Section | Content |
|---------|---------|
| 1. Executive Summary | 1 page: project scope, timeline, key stakeholders |
| 2. Functional Requirements | User stories or workflow descriptions with priority (Must-Have / Nice-to-Have) |
| 3. Technical Requirements | Infrastructure, security, SSO, compliance requirements |
| 4. Integration Specifications | Per-integration: systems, data flow, authentication, field mapping |
| 5. Data Migration Plan | Sources, volumes, mapping, timeline, validation approach |
| 6. Acceptance Criteria | Measurable pass/fail criteria for go-live sign-off |
| 7. Risks and Dependencies | Identified risks with mitigations; customer dependencies |
| 8. Out of Scope | Explicit list of what is NOT included in this implementation |
| 9. Sign-Off | Customer name, title, signature, and date |

---

## 5. Requirements Sign-Off Protocol

**Do not start configuration work until requirements are signed.**

Sign-off process:
1. Share draft requirements document with customer technical and business contacts
2. Allow 3–5 business days for review
3. Conduct requirements review call to address questions and gaps
4. Incorporate feedback and reissue final version
5. Obtain written sign-off (email confirmation acceptable; wet signature for enterprise tier)
6. Store signed document in implementation management system
7. Share copy with Implementation Lead and Customer Success team

**Scope Change Protocol** (after sign-off):
- Any changes to signed requirements must be submitted as a formal change request
- Change requests require Implementation Lead review and customer re-sign-off
- Changes that affect timeline or cost require commercial team notification

---

*Reference version 1.0 — Implementation / Implementation Engineer*
