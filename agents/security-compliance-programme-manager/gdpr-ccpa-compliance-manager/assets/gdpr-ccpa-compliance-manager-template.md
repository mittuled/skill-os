# GDPR / CCPA Compliance Programme Template

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager / DPO] |
| Version | [1.0] |
| Status | [Draft / Approved] |
| Skill | gdpr-ccpa-compliance-manager |
| Applicable Regulations | [GDPR / CCPA / CPRA / All] |
| Review Cycle | [Annual / Triggered by new processing activity] |

## Programme Scope

[1-2 sentences describing the data processing context and which regulations apply.

GUIDANCE: Example: "This programme governs personal data processing for EU and California residents across the core SaaS platform, marketing systems, and analytics pipelines. GDPR applies to EU/EEA residents; CCPA/CPRA applies to California residents."]

**Data subject categories:** [Customers / Employees / Prospects / End users]
**Jurisdictions covered:** [EU/EEA (GDPR) / California (CCPA/CPRA) / Other]
**DPO / Privacy contact:** [Name and email]

---

## Records of Processing Activities (ROPA) — GDPR Article 30

| # | Processing Activity | Data Categories | Data Subjects | Purpose | Lawful Basis (GDPR Art. 6) | Retention Period | Storage Location | Third-Party Recipients | International Transfer? | Transfer Mechanism |
|---|--------------------|-----------------|--------------|---------|-----------------------------|-----------------|-----------------|----------------------|------------------------|--------------------|
| 1 | [User account creation] | Name, email, hashed password | Customers | [Service provision] | [Contract Art. 6(1)(b)] | [Account lifetime + 2 years] | [AWS us-east-1] | [Auth0 (processor)] | [Yes / No] | [SCC / Adequacy decision / N/A] |
| 2 | [Marketing email] | Name, email, interaction data | Prospects | [Direct marketing] | [Consent Art. 6(1)(a)] | | | | | |
| 3 | [Payment processing] | Name, billing address, last 4 digits | Customers | [Transaction processing] | [Contract Art. 6(1)(b)] | | | | | |
| 4 | [Analytics / product telemetry] | Device ID, usage events | Users | [Product improvement] | [Legitimate interest Art. 6(1)(f)] | | | | | |
| 5 | [Support ticket data] | Name, email, communication content | Customers | [Support provision] | [Contract Art. 6(1)(b)] | | | | | |
| 6 | [Employee HR records] | Name, address, salary, performance | Employees | [Employment] | [Contract + legal obligation] | | | | | |
| [Add rows per processing activity] | | | | | | | | | | |

---

## Lawful Basis Register

| Processing Activity | GDPR Lawful Basis | GDPR Basis Documentation | CCPA / CPRA Equivalent | CCPA Sale / Share? | Opt-Out Mechanism |
|--------------------|-------------------|--------------------------|------------------------|-------------------|-------------------|
| [User account creation] | Contract Art. 6(1)(b) | [Terms of Service § N] | Business purpose | No | N/A |
| [Marketing email] | Consent Art. 6(1)(a) | [Consent log in [system]] | Consent | [Yes / No] | [Unsubscribe link / GPC] |
| [Analytics] | Legitimate interest Art. 6(1)(f) | [LIA completed MM/YYYY] | Business purpose | [Yes / No] | |
| [Profiling / targeted advertising] | Consent Art. 6(1)(a) | | Consent | Yes | [Opt-out link + GPC] |
| [Add rows] | | | | | |

**CCPA opt-out of sale/sharing:** [Implemented / Not implemented — target date]
**CPRA opt-out of sensitive personal information use:** [Implemented / Not implemented — target date]
**Global Privacy Control (GPC) signal honoured:** [Yes / No]

---

## Data Processing Agreement (DPA) Tracker

| Vendor / Processor | Data Categories Shared | Processing Purpose | DPA Executed? | DPA Date | GDPR Art. 28 Compliant? | SCCs Included? | CCPA Addendum? | Subprocessors Disclosed? | Next Review |
|-------------------|----------------------|-------------------|--------------|----------|--------------------------|----------------|----------------|--------------------------|-------------|
| [Vendor name] | [Categories] | [Purpose] | [Yes / No] | [MM/DD/YYYY] | [Yes / No] | [Yes / N/A] | [Yes / No / N/A] | [Yes / No] | [MM/YYYY] |
| | | | | | | | | | |
| | | | | | | | | | |

**Gaps requiring DPA execution:** [List vendors without DPAs]
**DPAs under negotiation:** [List with target dates]

---

## Cross-Border Transfer Register

| Transfer # | Data Exporter | Data Importer | Destination Country | Data Categories | Transfer Mechanism | Transfer Impact Assessment (TIA)? | TIA Date | Status |
|-----------|--------------|--------------|--------------------|-----------------|--------------------|-----------------------------------|----------|--------|
| XFER-001 | [Company name] | [Vendor / Entity] | [USA / India / etc.] | [Categories] | [SCC Module 2 / Adequacy decision / BCR] | [Yes / No] | [MM/YYYY] | [Active / Under review] |
| XFER-002 | | | | | | | | |

**Adequacy decisions relied upon:** [UK adequacy / Japan adequacy / etc.]
**SCCs version in use:** [June 2021 SCCs — Module [1/2/3/4]]

---

## Data Subject Request (DSR) Workflow Summary

| Right | Regulation | Statutory Deadline | Intake Channel | Verification Method | Processing Owner | Escalation Path |
|-------|-----------|-------------------|----------------|--------------------|-----------------|--------------------|
| Right to access (SAR) | GDPR Art. 15 | 30 days | [Email / Privacy portal] | [Identity verification process] | [Compliance / Engineering] | [Legal if contested] |
| Right to deletion | GDPR Art. 17 / CCPA | 30 days (GDPR) / 45 days (CCPA) | | | | |
| Right to portability | GDPR Art. 20 | 30 days | | | | |
| Right to rectification | GDPR Art. 16 | 30 days | | | | |
| Opt-out of sale/sharing | CCPA/CPRA | 15 business days | | | | |
| Right to restrict processing | GDPR Art. 18 | 30 days | | | | |
| Right to object | GDPR Art. 21 | 30 days | | | | |

**DSR intake URL / email:** [privacy@company.com / [URL]]
**DSR log location:** [GDrive / Jira project / Privacy tool]
**Authorized agent procedure:** [Documented at [URL] — CCPA requirement]

---

## DPIA Trigger Checklist

A Data Protection Impact Assessment (DPIA) is mandatory when any of the following apply:

- [ ] Large-scale profiling or automated decision-making with legal/significant effects (GDPR Art. 22)
- [ ] Systematic monitoring of publicly accessible areas
- [ ] Processing special categories of data (Art. 9) at scale
- [ ] Matching or combining datasets from multiple sources
- [ ] Processing children's data
- [ ] New technology with unknown privacy risks
- [ ] Processing that prevents data subjects from exercising rights

**DPIAs completed this period:**

| DPIA ID | Processing Activity / Feature | Risk Level | Mitigation Measures | DPO Sign-off | Date |
|---------|------------------------------|-----------|--------------------|--------------|----|
| DPIA-001 | [Activity] | [High / Medium] | [Measures] | [Yes / No] | [MM/DD/YYYY] |

---

## Privacy Compliance Dashboard

| Metric | Current Period | Prior Period | Target | Status |
|--------|---------------|-------------|--------|--------|
| DSR response rate within SLA (%) | [N]% | [N]% | 100% | [On track / At risk] |
| Average DSR response time (days) | [N] | [N] | < 25 days | |
| DPA coverage (% of processors with signed DPA) | [N]% | [N]% | 100% | |
| ROPA completeness (% of activities documented) | [N]% | [N]% | 100% | |
| Consent opt-in rate (marketing) | [N]% | [N]% | [N]% baseline | |
| Training completion — privacy module (%) | [N]% | [N]% | 100% | |
| Open privacy incidents / breaches | [N] | [N] | 0 | |

**Reporting period:** [Q1 / Q2 / Q3 / Q4 YYYY]
**Next regulatory monitoring review:** [MM/DD/YYYY — track new state privacy laws, EU guidance, enforcement actions]
