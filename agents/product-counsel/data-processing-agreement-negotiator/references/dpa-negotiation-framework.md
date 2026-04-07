# DPA Negotiation Framework

Reference framework for negotiating data processing agreements covering GDPR Article 28 requirements, standard contractual clauses, and key negotiation positions.

## GDPR Article 28 Mandatory Clauses

Every DPA must contain these clauses to comply with GDPR Article 28(3):

| # | Required Clause | Description | Negotiation Notes |
|---|----------------|-------------|-------------------|
| 1 | Processing Instructions | Processor acts only on documented instructions from the controller | Non-negotiable; define instruction format and change process |
| 2 | Confidentiality | Persons authorised to process must commit to confidentiality | Standard; ensure NDA coverage for all personnel |
| 3 | Security Measures | Appropriate technical and organisational measures per Article 32 | Negotiate specific measures in security schedule; reference ISO 27001/SOC 2 |
| 4 | Sub-Processor Controls | Prior specific or general written authorisation for sub-processors | Key negotiation point: specific vs. general authorisation, notification period (14-30 days), objection rights |
| 5 | Data Subject Rights Assistance | Processor assists controller in responding to data subject requests | Define SLA for assistance (5-10 business days), cost allocation |
| 6 | Breach Notification | Processor notifies controller without undue delay after becoming aware | Negotiate specific timeline (24-72 hours), notification content requirements |
| 7 | Data Return/Deletion | Delete or return all personal data after services end | Define timeline (30-90 days), certification of deletion, format for return |
| 8 | Audit Rights | Controller may audit or inspect processor compliance | Negotiate audit frequency, cost, notice period, third-party audit acceptance |

## Cross-Border Transfer Mechanisms

| Mechanism | When to Use | Requirements |
|-----------|------------|-------------|
| Standard Contractual Clauses (SCCs) | Transfer to countries without adequacy decision | Execute EU Commission approved SCCs (Module 1-4), conduct Transfer Impact Assessment |
| Adequacy Decision | Transfer to countries deemed adequate by EU Commission | Verify current adequacy status (can be revoked) |
| Binding Corporate Rules | Intra-group transfers | Supervisory authority approval required; expensive, suitable for large organisations |
| Derogations (Art. 49) | One-off transfers, explicit consent | Last resort; not suitable for systematic transfers |

## Key Negotiation Positions

### Terms Where Company Should Hold Firm
- Breach notification within 72 hours (GDPR deadline for controller reporting)
- Right to audit (can accept third-party audit reports as alternative)
- Sub-processor change notification with meaningful objection window
- Data deletion certification at contract termination

### Terms Where Company Can Show Flexibility
- Liability caps (proportional to contract value and data sensitivity)
- Indemnification scope (mutual vs. one-way, carve-outs for wilful misconduct)
- Audit cost allocation (vendor bears cost for compliance audits, company bears cost for ad hoc audits)
- Sub-processor notification timeline (14-30 day range acceptable)

## DPA Risk Tiering

| Tier | Data Type | Assessment Depth | DPA Complexity |
|------|-----------|-----------------|----------------|
| Tier 1 (Critical) | Sensitive PII, health data, financial data | Full DPA with custom security schedule, TIA, sub-processor audit | Complex negotiation expected |
| Tier 2 (Standard) | Standard PII (name, email, usage data) | Standard DPA template with security schedule | Moderate negotiation |
| Tier 3 (Low) | Business data, anonymised/aggregated data | Simplified DPA or data protection clauses in main agreement | Minimal negotiation |
