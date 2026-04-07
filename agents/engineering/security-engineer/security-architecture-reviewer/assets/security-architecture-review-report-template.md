# Security Architecture Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | security-architecture-reviewer |
| System / Service | [System name and owning team] |
| Architecture Version | [Design doc version or commit] |
| Frameworks Reviewed | [SOC 2 / GDPR / HIPAA / PCI-DSS / NIST CSF] |

## Executive Summary

[2-3 sentences covering the overall security posture, the most critical finding, and the approval recommendation.
GUIDANCE: Lead with the verdict. Example: "Architecture review CONDITIONAL APPROVAL: 1 critical finding (implicit trust between payment service and internal admin API must be resolved before launch) and 3 high-severity findings requiring remediation within 60 days. Defense-in-depth is well-structured at the perimeter but internal segmentation is absent."]

## Architecture Overview

[Brief description of the reviewed architecture.

GUIDANCE:
- Good: "Three-tier web application: React SPA → API Gateway → microservices (checkout, payments, users, inventory). Postgres databases per service. Redis cache. AWS hosted. External integrations: Stripe (payments), SendGrid (email), Twilio (SMS)."
- Bad: "Modern cloud application."
- Format: Bullet list of components, data flows, and trust boundaries reviewed]

### Data Classification Summary

[Map data types to classification level.

GUIDANCE: This drives the encryption and access control requirements that will be assessed.]

| Data Type | Classification | Applicable Regulations | Storage Location |
|-----------|---------------|----------------------|-----------------|
| [Payment card data] | Restricted | PCI-DSS | [Service/store name] |
| [User PII] | Confidential | GDPR, CCPA | [Service/store name] |
| [Application logs] | Internal | — | [Service/store name] |
| [Public content] | Public | — | [Service/store name] |

## Defense-in-Depth Assessment

[Evaluate each architectural layer for security controls.

GUIDANCE:
- Good: "Network layer: VPC with private/public subnet separation. Security groups enforce least-privilege. ALB with WAF rules for OWASP Top 10. Gap: no NACLs between database tier and application tier."
- Bad: "Network security is acceptable."
- Format: Table with layer, control present, gap, and severity]

| Layer | Controls Present | Gaps Identified | Severity |
|-------|-----------------|-----------------|----------|
| Network | [VPC segmentation, WAF, security groups] | [Describe gaps] | [Critical/High/Medium/Low] |
| Transport | [TLS versions, certificate management] | [Describe gaps] | |
| Application | [Input validation, output encoding, auth libraries] | [Describe gaps] | |
| Data | [Encryption at rest, field-level encryption, masking] | [Describe gaps] | |
| Identity | [IAM model, MFA, service accounts, RBAC] | [Describe gaps] | |

## Trust Boundary Analysis

[Evaluate each trust boundary crossing.

GUIDANCE:
- Good: "Boundary: External user → API Gateway. Controls: JWT validation, rate limiting (100 req/min/IP), OWASP WAF rule set. Status: PASS. Boundary: Checkout service → Payment service. Controls: mTLS, OAuth 2.0 client credentials. Status: PASS. Boundary: Payment service → Internal Admin API. Controls: None — implicit trust. Status: FAIL — CRITICAL."
- Bad: "Most service communications are secure."
- Format: Table with one row per trust boundary]

| Trust Boundary | Authentication | Authorization | Input Validation | Rate Limiting | Status |
|---------------|----------------|---------------|-----------------|---------------|--------|
| [External → API Gateway] | [JWT / API key] | [RBAC scope] | [WAF / schema validation] | [N req/min] | [PASS/FAIL] |
| [Service A → Service B] | [mTLS / none] | [OAuth scope / none] | [Schema validation / none] | [N req/min / none] | [PASS/FAIL] |

## Compliance Alignment Matrix

[Map architecture controls to applicable compliance requirements.

GUIDANCE: Flag each requirement as Met, Partial, or Gap. Partial and Gap must have remediation notes.]

| Framework | Requirement | Architecture Control | Status | Gap / Remediation |
|-----------|------------|---------------------|--------|-------------------|
| SOC 2 CC6.1 | Logical access controls | [IAM, RBAC configuration] | [Met/Partial/Gap] | [Note if not met] |
| GDPR Art. 32 | Encryption at rest | [AES-256 on all PII stores] | [Met/Partial/Gap] | [Note if not met] |
| GDPR Art. 32 | Encryption in transit | [TLS 1.2+ on all paths] | [Met/Partial/Gap] | [Note if not met] |
| PCI-DSS 3.4 | Card data encryption | [Tokenization via Stripe] | [Met/Partial/Gap] | [Note if not met] |

## Security Findings

[All findings with severity classification and remediation guidance.

GUIDANCE: Each finding must have a severity, affected component, attack scenario, and specific remediation. "Add authentication" is not specific. "Enforce OAuth 2.0 client credentials flow between payment-service and admin-api using the existing internal IdP" is specific.]

### Critical Findings (Block Launch)

| # | Finding | Component | Attack Scenario | Remediation | Effort |
|---|---------|-----------|----------------|-------------|--------|
| C1 | [Finding title] | [Component] | [How an attacker would exploit this] | [Specific fix] | [Story points / days] |

### High Findings (Fix Within 30 Days)

| # | Finding | Component | Attack Scenario | Remediation | Effort |
|---|---------|-----------|----------------|-------------|--------|
| H1 | [Finding title] | [Component] | [Attack scenario] | [Specific fix] | [Effort] |

### Medium Findings (Fix Within 90 Days)

| # | Finding | Component | Risk | Remediation | Effort |
|---|---------|-----------|------|-------------|--------|
| M1 | [Finding title] | [Component] | [Risk description] | [Specific fix] | [Effort] |

## Approval Recommendation

| Condition | Status |
|-----------|--------|
| Zero critical findings | [Met / Not Met — N critical findings] |
| High findings have remediation plan | [Met / Not Met] |
| Compliance gaps documented with plan | [Met / Not Met] |
| **Verdict** | **[APPROVED / CONDITIONAL / REJECTED]** |

**Conditions for approval (CONDITIONAL)**:
1. [Specific remediation with deadline]
2. [Specific verification required]

## Recommendations

- **P1 — Block**: [Critical finding to fix before any production traffic]
- **P2 — Pre-GA**: [High finding requiring remediation within 30 days of launch]
- **P3 — Roadmap**: [Medium finding to plan into next quarter]

## Appendices

### A. Annotated Architecture Diagram

[Architecture diagram with trust boundaries, data classifications, and security control markers annotated.]

### B. Methodology

[Frameworks used for review: STRIDE, OWASP ASVS level, CIS Benchmarks, NIST CSF. Reviewers and time period.]
