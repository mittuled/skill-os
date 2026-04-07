# Scoring Rubric: compliance-ga-reviewer-eng

Evaluates the compliance readiness of engineering deliverables against applicable security and regulatory frameworks as a gate condition for general availability release.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Control Implementation Coverage | 30% | Percentage of required controls that are implemented with verifiable evidence |
| 2 | Encryption and Data Protection | 20% | Encryption at rest and in transit, key management, and data handling procedures |
| 3 | Access Control and Identity | 20% | Least-privilege enforcement, MFA, audit logging, and identity management |
| 4 | Audit and Logging Completeness | 15% | Audit trail coverage, log retention, and tamper-proof storage |
| 5 | Incident Response Readiness | 15% | Documented procedures, tested runbooks, and escalation paths |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All controls implemented and evidenced; zero gaps; audit-ready today | Issue compliance sign-off; schedule next review in 12 months |
| A | 8.0 – 8.9 | Strong | All blockers resolved; 1–2 minor gaps with accepted risk | Issue conditional sign-off; log minor gaps in risk register |
| B | 7.0 – 7.9 | Good | No blocker gaps; 2–4 major gaps with remediation plans | Issue time-bounded sign-off; remediation due within 30 days |
| C | 5.0 – 6.9 | Adequate | 1–2 blocker gaps; partial controls in place | Delay GA until blockers resolved; escalate to CISO |
| D | 3.0 – 4.9 | Weak | Multiple blocker gaps; controls missing or unverified | Block GA release; initiate emergency remediation sprint |
| F | 0.0 – 2.9 | Failing | Fundamental controls absent; regulatory exposure is immediate | Stop all release activities; escalate to executive team |

## Signal Tables

### Control Implementation Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | 100% of required controls have documented evidence (screenshots, config exports, audit logs); zero controls marked "planned" or "in progress" |
| 7-8 | 95–99% controls evidenced; 1–2 controls have compensating controls with documented rationale |
| 5-6 | 85–94% controls evidenced; 3–5 controls pending with accepted risk documentation |
| 3-4 | 70–84% controls evidenced; multiple controls without evidence or compensating controls |
| 0-2 | Less than 70% controls evidenced; no systematic control tracking; evidence collection not started |

### Encryption and Data Protection

| Score | Evidence |
|-------|----------|
| 9-10 | AES-256 at rest on all data stores confirmed via config; TLS 1.3 enforced for all in-transit paths; key rotation automated with documented schedule; no plaintext sensitive data in logs |
| 7-8 | Encryption at rest enabled on all primary stores; TLS 1.2+ enforced; manual key rotation with documented schedule; 1–2 secondary stores pending encryption |
| 5-6 | Encryption at rest on 80–95% of stores; TLS enforced on external paths but not all internal paths; key rotation undocumented |
| 3-4 | Encryption at rest on primary database only; TLS optional or misconfigured; no key management procedure |
| 0-2 | No encryption at rest; plaintext sensitive data in storage or logs; HTTP allowed for sensitive endpoints |

### Access Control and Identity

| Score | Evidence |
|-------|----------|
| 9-10 | All human accounts have MFA enforced; IAM roles follow least-privilege with documented justification; service accounts use short-lived credentials; quarterly access review completed |
| 7-8 | MFA enforced for all admin accounts; most IAM roles scoped correctly; service accounts use long-lived credentials with rotation schedule |
| 5-6 | MFA enforced for subset of accounts; IAM roles have broad permissions without documented justification; no service account rotation |
| 3-4 | MFA not enforced; shared accounts in use; overprivileged service accounts; no access review process |
| 0-2 | No MFA; root/admin credentials used for routine operations; no IAM policy; access control undocumented |

### Audit and Logging Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All authentication, authorization, data access, and admin actions logged; logs stored in tamper-proof, immutable store; retention meets framework requirement (e.g., SOC 2: 1 year); alerting on log gaps |
| 7-8 | Auth and admin actions logged; data access logging on primary stores; retention documented; logs stored centrally but not immutable |
| 5-6 | Auth events logged; incomplete data access logging; retention policy exists but is not enforced technically |
| 3-4 | Partial auth logging; no data access logging; no defined retention policy; logs stored locally on instances |
| 0-2 | No centralized logging; critical events not logged; logs purged or inaccessible; no audit trail |

### Incident Response Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Incident response runbook exists, has been tested in a tabletop exercise within 12 months, and covers breach notification timelines for all applicable regulations (GDPR 72h, HIPAA 60d) |
| 7-8 | Runbook exists with escalation paths and regulatory timelines; not tested in the last 12 months |
| 5-6 | Runbook exists but is incomplete (missing contact lists, notification templates, or regulatory timelines) |
| 3-4 | Informal incident response process only; no documented runbook; key personnel identified but procedures unwritten |
| 0-2 | No incident response process; team does not know breach notification requirements; no escalation contacts |
