# Compliance GA Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | compliance-ga-reviewer-eng |
| Release | [Product / Feature name and version] |
| Review Target | [GA release date] |

## Executive Summary

[2-3 sentences stating the overall compliance verdict, the frameworks reviewed, and the most significant finding or blocker.
GUIDANCE: Lead with the go/no-go verdict. Example: "This release is NOT approved for GA. Two blocker gaps were identified: audit logging is disabled on the payments database and the incident response runbook has not been tested. Both must be remediated before launch."]

## Scope Matrix

[Table mapping each applicable framework to the release components it covers.

GUIDANCE:
- Good: Map each framework requirement to the specific engineering deliverable (e.g., "SOC 2 CC6.1 → IAM role configuration in Terraform module auth-v2")
- Bad: "SOC 2 applies to this release" with no mapping to specific controls
- Format: Table with columns: Framework, Requirement ID, Requirement Description, Engineering Deliverable]

| Framework | Requirement ID | Requirement Description | Engineering Deliverable | In Scope? |
|-----------|---------------|------------------------|------------------------|-----------|
| [SOC 2 Type II / GDPR Art. 32 / HIPAA / PCI-DSS] | [e.g., CC6.1] | [e.g., Logical access uses unique credentials] | [e.g., IAM Terraform module, auth service] | [Yes/No] |

## Control Verification Results

[Evidence-linked verification for each in-scope control.

GUIDANCE:
- Good: "CC6.1 — Verified: IAM policy export shows all roles have unique credentials; MFA enforced via Okta group policy (screenshot: okta-mfa-policy-2026-04-06.png)"
- Bad: "CC6.1 — Implemented" with no evidence link
- Format: Table with status (Verified / Partial / Gap)]

| Framework | Control ID | Control | Status | Evidence Link | Notes |
|-----------|-----------|---------|--------|---------------|-------|
| [Framework] | [ID] | [Control description] | [Verified / Partial / Gap] | [Link or filename] | [Gaps or compensating controls] |

## Gap Assessment

[Classified list of identified gaps. Only complete this section if gaps exist.

GUIDANCE:
- Good: "BLOCKER — Audit logging not enabled on payments_db. No evidence of database query logging. Regulatory exposure: PCI-DSS Req 10.2. Owner: @infra-team. Deadline: 2026-04-10."
- Bad: "Some logging is missing"
- Format: Group by severity (Blocker / Major / Minor)]

### Blockers (must resolve before GA)

| # | Gap Description | Framework Ref | Owner | Deadline |
|---|----------------|--------------|-------|----------|
| [1] | [Specific control missing with impact] | [Framework + Req ID] | [@owner] | [YYYY-MM-DD] |

### Major Gaps (should resolve before GA)

| # | Gap Description | Framework Ref | Owner | Deadline |
|---|----------------|--------------|-------|----------|

### Minor Gaps (accepted risk with documentation)

| # | Gap Description | Risk Acceptance Rationale | Owner |
|---|----------------|--------------------------|-------|

## Remediation Tracker

[For each Blocker and Major gap, document the remediation plan.

GUIDANCE:
- Good: "Gap 1 — Blocker: Enable CloudTrail on payments_db RDS instance. Task: INFRA-342. Owner: @jorge-infra. Steps: (1) Enable enhanced monitoring, (2) Enable CloudTrail data events for S3 and RDS, (3) Verify logs appear in CloudWatch. Due: 2026-04-10."
- Bad: "Team will fix the logging issue"]

| Gap # | Severity | Remediation Steps | Owner | Due Date | Verification Method |
|-------|---------|-------------------|-------|----------|---------------------|
| [1] | [Blocker] | [Step 1, Step 2, Step 3] | [@owner] | [YYYY-MM-DD] | [How to re-verify] |

## Sign-Off Decision

[The formal compliance verdict for this release.

GUIDANCE: Choose one of the three states below and remove the others. For conditional approvals, list every condition explicitly.]

**VERDICT: [ GO | CONDITIONAL GO | NO-GO ]**

---

**GO**: All controls verified. No blocker or major gaps. Release is approved for GA.

---

**CONDITIONAL GO**: Release is approved for GA subject to the following conditions being met by [date]:
- [ ] [Condition 1 with specific deliverable]
- [ ] [Condition 2 with specific deliverable]

---

**NO-GO**: Release is blocked. The following blockers must be remediated and re-reviewed:
- [ ] [Blocker 1 description]
- [ ] [Blocker 2 description]

**Security Engineer sign-off**: _________________________ Date: _________

## Recommendations

[Prioritized recommendations beyond the current release scope.

GUIDANCE: Each recommendation should be specific, actionable, and prioritized. Focus on structural improvements that prevent future compliance gaps.]

- **P1**: [Immediate action required — specific improvement with clear outcome]
- **P2**: [Important improvement for next sprint]
- **P3**: [Long-term structural improvement]

## Appendices

### A. Methodology

[Frameworks assessed, assessment methods used (manual review, automated scan, configuration export), time period covered, and any limitations of this review.]

### B. Evidence Index

[Index of all evidence artifacts reviewed, with filenames, collection dates, and sources.]

| Evidence ID | Description | Source | Date Collected |
|-------------|-------------|--------|----------------|
| E001 | [e.g., IAM policy export] | [e.g., AWS Console] | [YYYY-MM-DD] |
