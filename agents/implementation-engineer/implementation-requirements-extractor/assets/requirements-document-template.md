# Implementation Requirements Document

**Customer**: `[Customer Name]`
**Product**: `[Product / Module being implemented]`
**Implementation Engineer**: `[Name]`
**Implementation Lead**: `[Name]`
**Document Version**: `[v1.0 Draft / v1.1 Updated / v2.0 Final]`
**Date**: `YYYY-MM-DD`
**Status**: `[ ] Draft  [ ] In Review  [ ] Approved — Sign-Off Date: YYYY-MM-DD`

---

## 1. Executive Summary

| Field | Value |
|-------|-------|
| Project Scope | `[1–2 sentence description of what is being implemented]` |
| Implementation Tier | `[ ] Tier 1  [ ] Tier 2  [ ] Tier 3  [ ] Tier 4` |
| Target Go-Live Date | `YYYY-MM-DD` |
| Customer Technical Contact | `[Name, Title, Email]` |
| Customer Business Contact | `[Name, Title, Email]` |
| Customer Executive Sponsor | `[Name, Title, Email]` |
| Implementation Engineer | `[Name, Email]` |
| Implementation Lead | `[Name, Email]` |

---

## 2. Functional Requirements

| Req # | Requirement | Priority | Notes |
|-------|-------------|----------|-------|
| F-001 | `[Functional requirement description]` | `Must-Have / Nice-to-Have` | `[Notes]` |
| F-002 | `[Requirement]` | `Must-Have` | |
| F-003 | `[Requirement]` | `Nice-to-Have` | `[Phase 2 candidate]` |

**Out of Scope** *(functional)*:
- `[Explicitly list what is NOT included]`
- `[Any feature requested but not contractually included]`

---

## 3. Technical Requirements

| Requirement | Detail | Constraint |
|-------------|--------|-----------|
| Operating systems | `[Windows 11, macOS 14+, etc.]` | `[Any exceptions]` |
| Browsers | `[Chrome 120+, Firefox 121+, etc.]` | |
| Authentication / SSO | `[IdP: Okta / Azure AD / Google]` | `[SAML or OIDC]` |
| MFA requirement | `[ ] Required  [ ] Optional` | `[Any specific MFA method required]` |
| Network restrictions | `[VPN required? Firewall rules? IP allowlist?]` | |
| Data residency | `[EU / US / APAC / No requirement]` | |
| Compliance requirements | `[GDPR / HIPAA / SOC 2 / None]` | |
| Infrastructure | `[Cloud / On-premise / Hybrid]` | |

---

## 4. Integration Specifications

### Integration 1: `[Integration Name]`

| Field | Detail |
|-------|--------|
| Third-party system | `[System name and version]` |
| Integration purpose | `[What this integration achieves]` |
| Data direction | `[Unidirectional: Source → Target / Bidirectional]` |
| Sync frequency | `[Real-time / Every ## minutes / Daily]` |
| Authentication method | `[API Key / OAuth 2.0 / SAML]` |
| Customer contact for setup | `[Name, Title]` |
| Customer dependency | `[What the customer must provide before setup can begin]` |
| Target completion | `YYYY-MM-DD` |

**Data Mapping**:
| Source Field | Target Field | Type | Required? |
|-------------|-------------|------|-----------|
| `[Field]` | `[Field]` | `String / Date / Number` | `Yes / No` |

**Known Limitations / Scope**:
```
[Any limitations specific to this integration or fields deliberately excluded]
```

---

*(Duplicate Section 4 block for each additional integration)*

---

## 5. Data Migration Plan

**Migration Required**: `[ ] Yes  [ ] No`

If Yes:

| Data Type | Source System | Format | Volume | Migration Priority |
|-----------|--------------|--------|--------|-------------------|
| `[e.g., Contacts]` | `[Old CRM]` | `CSV export` | `###,### records` | `1 — Must migrate` |
| `[e.g., Historical deals]` | `[Source]` | `API export` | `## records` | `2 — Nice to have` |

**Data Validation Approach**:
```
[How will we verify the migrated data is complete and accurate?
Who on the customer side will sign off on data quality?]
```

**Customer Data Delivery Deadline**: `YYYY-MM-DD`
**Migration Target Date**: `YYYY-MM-DD`

---

## 6. Acceptance Criteria

| Criterion | Test Method | Pass Condition | Owner |
|-----------|------------|---------------|-------|
| AC-001 | `[How to test]` | `[What defines pass]` | `[Customer / IE]` |
| AC-002 | `[How to test]` | `[Pass condition]` | `[Customer / IE]` |
| AC-003 | `[How to test]` | `[Pass condition]` | `[Customer]` |

---

## 7. Risks and Dependencies

| Risk / Dependency | Probability | Impact | Mitigation | Owner |
|------------------|------------|--------|-----------|-------|
| `[Risk description]` | `High / Medium / Low` | `High / Medium / Low` | `[Mitigation action]` | `[Owner]` |

**Customer Dependencies** *(items the customer must deliver for the project to stay on schedule)*:

| Dependency | Owner | Required By |
|------------|-------|------------|
| `[e.g., API credentials for integration X]` | `[Customer Contact]` | `YYYY-MM-DD` |
| `[e.g., Data export from legacy system]` | `[Customer Contact]` | `YYYY-MM-DD` |

---

## 8. Project Timeline

| Phase | Start Date | End Date | Dependencies |
|-------|-----------|---------|-------------|
| Discovery | `YYYY-MM-DD` | `YYYY-MM-DD` | — |
| Configuration | `YYYY-MM-DD` | `YYYY-MM-DD` | Signed requirements |
| Integration | `YYYY-MM-DD` | `YYYY-MM-DD` | Customer API credentials |
| Data Migration | `YYYY-MM-DD` | `YYYY-MM-DD` | Customer data export |
| Testing | `YYYY-MM-DD` | `YYYY-MM-DD` | Phases above complete |
| Go-Live | `YYYY-MM-DD` | — | Testing sign-off |

---

## 9. Sign-Off

By signing below, the customer confirms that this document accurately represents the requirements for this implementation project. Changes after sign-off require a formal change request.

| Name | Title | Date | Signature |
|------|-------|------|-----------|
| `[Customer Name]` | `[Title]` | `YYYY-MM-DD` | _________ |
| `[Implementation Lead]` | `Implementation Lead` | `YYYY-MM-DD` | _________ |

---

*Template version 1.0 — Implementation / Implementation Engineer*
