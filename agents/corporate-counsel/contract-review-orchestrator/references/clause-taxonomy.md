# Clause Taxonomy: contract-review-orchestrator

Standard clause categories for contract analysis, organized by risk area with expected presence by contract type.

## Clause Categories by Risk Area

### Financial Risk

| # | Clause Type | Description |
|---|-------------|-------------|
| 1 | Payment Terms | Due dates, methods, currency, late payment consequences |
| 2 | Pricing & Fees | Base pricing, variable charges, fee schedules |
| 3 | Price Escalation | Annual increases, adjustment mechanisms, caps |
| 4 | Audit Rights | Right to audit billing, usage, or financial records |
| 5 | Taxes | Tax responsibility allocation, withholding, exemptions |

### Liability & Indemnification

| # | Clause Type | Description |
|---|-------------|-------------|
| 6 | Liability Cap | Maximum aggregate liability, per-incident caps |
| 7 | Consequential Damages | Exclusion or inclusion of indirect/consequential damages |
| 8 | Indemnification | Mutual vs. one-sided, scope, carve-outs |
| 9 | Insurance | Required coverage types, minimums, certificate requirements |
| 10 | Force Majeure | Events excusing performance, notice requirements |

### Intellectual Property

| # | Clause Type | Description |
|---|-------------|-------------|
| 11 | IP Ownership | Pre-existing IP, work product, derivative works |
| 12 | License Grant | Scope, exclusivity, territory, sublicensing rights |
| 13 | Non-Compete | Restrictions on competitive activities |
| 14 | Non-Solicit | Restrictions on hiring or soliciting personnel |
| 15 | Confidentiality | Definition of confidential information, obligations, duration |

### Data & Privacy

| # | Clause Type | Description |
|---|-------------|-------------|
| 16 | Data Processing | Permitted processing purposes, instructions, restrictions |
| 17 | Data Protection | Security measures, encryption, access controls |
| 18 | Breach Notification | Timeframes, content requirements, remediation obligations |
| 19 | Sub-Processors | Approval rights, notification, liability chain |
| 20 | Data Return/Destruction | Post-termination data handling, certification |
| 21 | Cross-Border Transfer | Data localization, transfer mechanisms (SCCs, BCRs) |

### Term & Termination

| # | Clause Type | Description |
|---|-------------|-------------|
| 22 | Term & Renewal | Initial term, renewal mechanism, auto-renewal |
| 23 | Termination for Convenience | Right to exit without cause, notice period |
| 24 | Termination for Cause | Breach triggers, cure periods, material breach definition |
| 25 | Effect of Termination | Surviving obligations, wind-down, transition assistance |

### Operational

| # | Clause Type | Description |
|---|-------------|-------------|
| 26 | Service Levels (SLA) | Uptime, response times, performance metrics, remedies |
| 27 | Warranties | Representations, scope, disclaimer language |
| 28 | Change Management | Amendment process, change order procedures |
| 29 | Assignment | Right to assign, change of control provisions |
| 30 | Governing Law & Venue | Jurisdiction, dispute resolution, arbitration |
| 31 | Notices | Delivery methods, addresses, deemed-received timing |
| 32 | Entire Agreement | Integration clause, superseding prior agreements |

## Expected Clauses by Contract Type

| Clause Type | SaaS | Services | NDA | Employment | Partnership | Licensing |
|-------------|-------|----------|-----|------------|-------------|-----------|
| Payment Terms | Required | Required | — | Required | Required | Required |
| Pricing & Fees | Required | Required | — | — | Recommended | Required |
| Liability Cap | Required | Required | Recommended | — | Required | Required |
| Indemnification | Required | Required | — | Recommended | Required | Required |
| IP Ownership | Required | Required | — | Required | Required | Required |
| License Grant | Required | — | — | — | Recommended | Required |
| Confidentiality | Required | Required | Required | Required | Required | Required |
| Data Processing | Required | Recommended | — | Recommended | Recommended | Recommended |
| Breach Notification | Required | Recommended | — | — | Recommended | Recommended |
| Term & Renewal | Required | Required | Required | Required | Required | Required |
| Termination for Convenience | Required | Required | Required | Recommended | Recommended | Recommended |
| Termination for Cause | Required | Required | — | Required | Required | Required |
| SLA | Required | Recommended | — | — | — | — |
| Warranties | Required | Required | — | — | Required | Required |
| Governing Law & Venue | Required | Required | Required | Required | Required | Required |

## Red-Flag Clause Patterns

- **Unlimited liability**: Any contract lacking a liability cap or explicitly stating unlimited liability
- **One-sided indemnification**: Indemnification obligations that run only in one direction without reciprocal protections
- **IP assignment by default**: Clauses that assign company IP to the counterparty as a default rather than through explicit negotiation
- **Auto-renewal with price escalation**: Automatic renewal combined with uncapped price increases
- **Broad change of control**: Assignment clauses that allow counterparty to assign freely upon acquisition without consent
- **No termination for convenience**: Contracts with no exit mechanism outside of material breach
- **Unlimited sub-processing**: Data processing terms that allow unlimited delegation to sub-processors without notice or approval
- **Unilateral amendment**: Clauses allowing one party to modify terms without the other's consent
- **Non-mutual non-compete**: Non-compete restrictions that bind only one party
- **Waiver of jury trial without arbitration**: Eliminating jury trial rights without providing an alternative dispute mechanism
