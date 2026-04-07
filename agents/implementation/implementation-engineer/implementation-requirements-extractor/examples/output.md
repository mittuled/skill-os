# Implementation Requirements Document — Bright Horizons Healthcare

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Customer | Bright Horizons Healthcare |
| Contract | $240,000 ARR / 24 months / 500 seats |
| Status | DRAFT — Pending BAA and Workday API credentials |
| Completeness | 100% sections populated |
| Sign-Off Required | Yes |
| Skill | implementation-requirements-extractor |

## Executive Summary

Bright Horizons Healthcare is replacing spreadsheet-based compliance tracking for 500 clinical staff across Compliance, HR, and Clinical Operations. All six requirements sections are populated from two discovery sessions. Two open items must be resolved before implementation can proceed: the HIPAA BAA (in legal review) and Workday API credentials. Target go-live is June 1 per the contractual commitment.

## Sales Context

| Field | Detail |
|---|---|
| Contract value | $240,000 ARR |
| Seats | 500 (Compliance, HR, Clinical Operations) |
| Term | 24 months |
| Key commitment | Replace spreadsheet compliance tracking by June 1 |

## Functional Requirements

1. Track compliance certifications for 500 clinical staff with expiry alerts
2. Generate monthly compliance reports for department heads
3. Support custom compliance frameworks (HIPAA, OSHA, Joint Commission)
4. Role-based dashboards: staff (own certs), manager (team status), admin (org-wide)

## Technical Environment

| Item | Specification |
|---|---|
| Identity | Azure Active Directory, SAML 2.0 SSO |
| Workstations | Windows 11, Chrome browser |
| Infrastructure | Cloud-only (no on-premise) |
| Compliance requirement | HIPAA BAA required before any data ingestion |

## Integration Requirements

| Integration | Method | Purpose |
|---|---|---|
| Azure AD | SAML 2.0 + SCIM | SSO and automated user provisioning |
| Workday | REST API | Employee roster sync (department, role, start date) |
| Microsoft 365 | SMTP relay | Certification expiry notification emails |

## Data Migration Requirements

- 500 employee records from Excel spreadsheets (HR to provide export by April 10)
- 3 years of historical certification records in CSV format
- Data mapping session required with HR to confirm field alignment before migration run

## User and Access Requirements

| Role | Count | Access Level |
|---|---|---|
| Admin | 3 | Full org-wide admin (IT Director, Compliance Lead, HR Director) |
| Manager | 50 | Team dashboard — view team certification status |
| Staff | 447 | Self-service — view own certifications, upload documents |

## Acceptance Criteria

- [ ] All 500 employee records migrated and verified (row count and spot-check)
- [ ] SSO login functional for 100% of provisioned users
- [ ] Workday sync updating employee roster within 24 hours of changes
- [ ] Monthly compliance report generation tested by each department head
- [ ] Customer IT Director signs off on security configuration

## Open Items (Blocking)

| Item | Owner | Expected Resolution |
|---|---|---|
| HIPAA BAA — legal review in progress | Bright Horizons Legal + [Company] Legal | April 5 |
| Workday API credentials — IT provisioning | Bright Horizons IT Director | April 7 |

**Implementation cannot proceed past environment setup until both open items are resolved.**

## Next Steps

1. Send this document to the Bright Horizons IT Director and Compliance Lead for review
2. Schedule sign-off call for April 8 (after BAA and Workday credentials expected)
3. Once signed, begin environment setup and Azure AD SSO configuration in parallel
