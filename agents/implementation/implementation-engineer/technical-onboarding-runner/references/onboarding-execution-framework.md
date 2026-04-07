# Technical Onboarding Execution Framework

Reference for the `technical-onboarding-runner` skill.

---

## 1. Pre-Onboarding Checklist

Complete before any technical work begins:

- [ ] Requirements document is signed and filed
- [ ] Sales handoff reviewed and aligned with requirements
- [ ] Implementation plan and timeline agreed with customer
- [ ] Customer contacts confirmed: technical lead, business lead, executive sponsor
- [ ] All customer dependencies confirmed with deadlines (API creds, data exports, access)
- [ ] Environment provisioned and accessible
- [ ] Integration catalogue guides identified for each required integration
- [ ] Kickoff meeting scheduled with all customer stakeholders

---

## 2. Kickoff Meeting Agenda

The kickoff meeting sets expectations and builds the relationship. Cover:

| Agenda Item | Duration | Purpose |
|-------------|---------|---------|
| Introductions | 5 min | Names, roles, and how the customer and IE will work together |
| Project scope and timeline | 10 min | Walk through phases; confirm go-live target |
| Requirements summary | 10 min | Review key functional, integration, and migration requirements |
| Customer responsibilities | 10 min | Walk through dependencies and due dates customer must meet |
| Communication cadence | 5 min | Agree on update frequency, format, and escalation path |
| Q&A | 10 min | Address questions and surface any new concerns |

**Output**: Kickoff notes sent within 24 hours with action items, owner, and due dates.

---

## 3. Environment Configuration Standards

When provisioning and configuring the customer's environment:

| Configuration Area | Standard | How to Verify |
|-------------------|---------|--------------|
| Admin access | Customer has at least 2 admin accounts (not just one) | Check admin user list |
| SSO configuration | SSO-only login enforced; local login disabled if SSO in use | Test SSO login; verify local bypass blocked |
| MFA | Enforced for all users before go-live | Check MFA compliance report |
| User roles | RBAC roles match requirements; least privilege applied | Review role assignments |
| Branding | Customer logo and colour scheme applied per spec | Visual check |
| Email notifications | From address configured to customer domain (if supported) | Send test notification |
| Data retention | Retention policy set per customer compliance requirement | Check settings |
| Backup / restore | Configured and tested (if applicable) | Check backup schedule |

---

## 4. Integration Execution Checklist

For each integration in scope:

- [ ] Read the integration guide in the integration catalogue before starting
- [ ] Confirm customer has provided the required credentials and access
- [ ] Set up integration in staging environment first (if staging available)
- [ ] Test data flow with a small sample before enabling for all records
- [ ] Verify field mapping against the data mapping document
- [ ] Document any deviations from the catalogue guide
- [ ] Confirm with customer that data arriving in the system is correct
- [ ] Test error handling (what happens when the integration fails or is rate-limited)
- [ ] Enable integration in production
- [ ] Set up monitoring or alerts for integration failures (if supported)

---

## 5. Data Migration Execution Steps

| Step | Activity | Quality Gate |
|------|---------|-------------|
| 1 | Receive and validate customer data export | File format matches agreed spec; no corruption |
| 2 | Deduplicate source data | Deduplication report reviewed with customer |
| 3 | Map source fields to product fields | Field mapping document signed off |
| 4 | Transform data as needed | Transformation log documented |
| 5 | Run migration in staging | Customer validates 10% sample in staging |
| 6 | Customer approves staging migration | Written approval received |
| 7 | Run migration in production | Post-migration validation script run |
| 8 | Customer validates production data | Customer sign-off on data quality |

**Migration Failure Response**:
- Stop migration immediately if >5% of records fail
- Document failed records with error messages
- Investigate root cause before re-running
- Notify Implementation Lead if root cause is unclear

---

## 6. Acceptance Testing Protocol

Run acceptance tests against the requirements document acceptance criteria:

| Test Phase | Who Runs It | Criteria Source | Pass Threshold |
|-----------|------------|----------------|---------------|
| Internal testing | Implementation Engineer | Acceptance criteria from requirements | All criteria pass |
| User acceptance testing | Customer | Customer's own workflow scenarios | Customer sign-off |

**During UAT**:
- Schedule a joint UAT session with the customer team
- Walk through each acceptance criterion together
- Document pass/fail for each criterion
- For failures: classify as blocker (must fix before go-live) or non-blocker (fix in hypercare)
- No go-live until all blockers are resolved

---

## 7. Go-Live Readiness Scorecard

| Check | Status | Notes |
|-------|--------|-------|
| All acceptance criteria passed | `[ ] Yes  [ ] No` | |
| All integrations tested and active | `[ ] Yes  [ ] No` | |
| Data migration validated in production | `[ ] Yes  [ ] N/A` | |
| SSO and MFA enforced | `[ ] Yes  [ ] No` | |
| Admin users trained | `[ ] Yes  [ ] No` | |
| End users trained | `[ ] Yes  [ ] No` | |
| Customer success team briefed | `[ ] Yes  [ ] No` | |
| Hypercare plan agreed | `[ ] Yes  [ ] No` | |
| Customer has confirmed readiness | `[ ] Yes  [ ] No` | |

**Go-live is blocked until all items are Yes.**

---

## 8. Hypercare Protocol

Hypercare is the heightened support period immediately after go-live. Standard duration: 2–4 weeks depending on implementation tier.

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Daily check-in with customer technical contact | Daily (Week 1) | Implementation Engineer |
| Check error logs and integration health | Daily (Weeks 1–2) | Implementation Engineer |
| Status update to Implementation Lead | Daily (Week 1); then weekly | Implementation Engineer |
| Issue triage and resolution | As needed | Implementation Engineer |
| Hypercare exit review | End of hypercare period | Implementation Lead + Customer |

**Hypercare Exit Criteria**:
- No open critical (P1/P2) issues
- All integrations running without errors for 5 consecutive business days
- Customer confirms system is operating as expected
- Formal handoff to steady-state customer success completed

---

*Reference version 1.0 — Implementation / Implementation Engineer*
