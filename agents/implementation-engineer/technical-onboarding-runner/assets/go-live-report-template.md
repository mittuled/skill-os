# Go-Live Report

**Customer**: `[Customer Name]`
**Product**: `[Product / Module implemented]`
**Implementation Engineer**: `[Name]`
**Implementation Lead**: `[Name]`
**Report Version**: `[v1.0 Final]`
**Go-Live Date**: `YYYY-MM-DD`
**Hypercare End Date**: `YYYY-MM-DD`
**Status**: `[ ] Hypercare Active  [ ] Hypercare Complete  [ ] Handed Off to Customer Success`

---

## 1. Implementation Summary

| Field | Value |
|-------|-------|
| Implementation Tier | `[ ] Tier 1  [ ] Tier 2  [ ] Tier 3  [ ] Tier 4` |
| Original Go-Live Target | `YYYY-MM-DD` |
| Actual Go-Live Date | `YYYY-MM-DD` |
| Days Variance | `[+N / -N / On time]` |
| Requirements Doc Version | `[v2.0 Final — signed YYYY-MM-DD]` |
| Scope Changes | `[ ] None  [ ] Minor  [ ] Significant — see Section 7` |
| Implementation Playbook Used | `[Playbook name / version]` |

**Implementation Narrative** *(2–4 sentences)*:
> `[Describe what was implemented, key integrations, any notable decisions made, and how the customer reached go-live.]`

---

## 2. Go-Live Readiness Scorecard

| Check | Status | Notes |
|-------|--------|-------|
| All acceptance criteria passed | `[ ] Yes  [ ] No` | `[Link to UAT results]` |
| All integrations tested and active | `[ ] Yes  [ ] No` | `[List integrations confirmed]` |
| Data migration validated in production | `[ ] Yes  [ ] N/A` | `[Migration record count / quality result]` |
| SSO and MFA enforced | `[ ] Yes  [ ] No` | `[IdP confirmed]` |
| Admin users trained | `[ ] Yes  [ ] No` | `[# of admins trained; date]` |
| End users trained | `[ ] Yes  [ ] No` | `[# of end users trained; date]` |
| Customer success team briefed | `[ ] Yes  [ ] No` | `[CSM name; briefing date]` |
| Hypercare plan agreed | `[ ] Yes  [ ] No` | `[Hypercare duration; end date]` |
| Customer confirmed readiness | `[ ] Yes  [ ] No` | `[Sign-off contact; date]` |

**Scorecard Result**: `[ ] All Clear — Go-Live Approved  [ ] Conditional — See Open Items`

---

## 3. Environment Configuration Confirmation

| Configuration Area | Configured | Verified By | Notes |
|-------------------|-----------|------------|-------|
| Admin accounts (≥2) | `[ ]` | `[Name]` | |
| SSO configuration | `[ ]` | `[Name]` | `[IdP / method]` |
| MFA enforced for all users | `[ ]` | `[Name]` | |
| RBAC roles assigned | `[ ]` | `[Name]` | `[Role count]` |
| Branding applied | `[ ]` | `[Name]` | |
| Email notifications (custom domain) | `[ ] / [ ] N/A` | `[Name]` | |
| Data retention policy set | `[ ]` | `[Name]` | `[Retention period]` |
| Backup / restore configured | `[ ] / [ ] N/A` | `[Name]` | |

---

## 4. Integration Status

| Integration | Status | Test Result | Notes |
|-------------|--------|------------|-------|
| `[Integration 1]` | `[ ] Active  [ ] Disabled  [ ] N/A` | `[ ] Pass  [ ] Fail` | `[Error details if any]` |
| `[Integration 2]` | `[ ] Active  [ ] Disabled  [ ] N/A` | `[ ] Pass  [ ] Fail` | |
| `[Integration 3]` | `[ ] Active  [ ] Disabled  [ ] N/A` | `[ ] Pass  [ ] Fail` | |

**Deviations from Integration Catalogue**:
- `[List any deviations from the standard integration guide, or "None"]`

---

## 5. Data Migration Results

*Complete this section only if data migration was in scope. Mark N/A otherwise.*

| Metric | Value |
|--------|-------|
| Source record count | `[N records]` |
| Successfully migrated | `[N records (N%)]` |
| Failed / skipped | `[N records — see failure log]` |
| Deduplication removed | `[N duplicate records]` |
| Customer validation sample | `[N% sample reviewed; approved YYYY-MM-DD]` |
| Customer sign-off date | `YYYY-MM-DD` |
| Migration log location | `[Link or path]` |

**Migration Issues**:
- `[Describe any failures, root causes, and resolutions — or "None"]`

---

## 6. Acceptance Testing Results

| Criterion | Source | IE Test | UAT Result | Resolution |
|-----------|--------|---------|-----------|------------|
| `[Criterion 1]` | Req F-001 | `[ ] Pass  [ ] Fail` | `[ ] Pass  [ ] Fail` | `[Action taken if fail]` |
| `[Criterion 2]` | Req F-002 | `[ ] Pass  [ ] Fail` | `[ ] Pass  [ ] Fail` | |
| `[Criterion 3]` | Req I-001 | `[ ] Pass  [ ] Fail` | `[ ] Pass  [ ] Fail` | |
| `[Criterion 4]` | Req D-001 | `[ ] Pass  [ ] Fail` | `[ ] N/A` | `[N/A — migration only]` |

**UAT Sign-Off**: `[Customer name, title] — YYYY-MM-DD`

**Blockers Resolved Before Go-Live**:
- `[Blocker 1: description → resolution]`
- `[Or "None"]`

**Non-Blockers Deferred to Hypercare**:
- `[Item 1: description → owner → target resolution date]`
- `[Or "None"]`

---

## 7. Scope Changes

*Document any changes from the original signed requirements.*

| Change # | Original Requirement | Change Made | Reason | Approved By |
|----------|---------------------|------------|--------|------------|
| SC-001 | `[Original scope]` | `[What changed]` | `[Customer request / technical constraint]` | `[Name + date]` |

**Impact of Scope Changes**: `[ ] None  [ ] Timeline impact  [ ] Additional cost — see attached SOW amendment`

---

## 8. Training Delivered

| Session | Date | Attendees | Format | Materials |
|---------|------|-----------|--------|-----------|
| Admin training | `YYYY-MM-DD` | `[N admins — names]` | `[ ] Live  [ ] Recorded` | `[Link to recording / deck]` |
| End user training | `YYYY-MM-DD` | `[N users — role]` | `[ ] Live  [ ] Recorded` | `[Link]` |
| `[Additional session]` | `YYYY-MM-DD` | `[Attendees]` | | |

**Training Gaps**: `[Note any stakeholders who could not attend and follow-up plan — or "None"]`

---

## 9. Hypercare Plan

| Activity | Frequency | Owner | Notes |
|----------|-----------|-------|-------|
| Daily check-in with customer tech contact | Daily (Week 1) | `[IE Name]` | `[Contact name + channel]` |
| Integration health check | Daily (Weeks 1–2) | `[IE Name]` | `[Monitoring dashboard link]` |
| Error log review | Daily (Weeks 1–2) | `[IE Name]` | |
| Status update to Implementation Lead | Daily (Wk 1); weekly (Wk 2+) | `[IE Name]` | |
| Issue triage and resolution | As needed | `[IE Name]` | |
| Hypercare exit review | `YYYY-MM-DD` | `[IL Name]` + customer | |

**Open Issues at Go-Live**:

| Issue # | Description | Severity | Owner | Target Resolution |
|---------|-------------|----------|-------|------------------|
| H-001 | `[Issue description]` | `P1 / P2 / P3` | `[Name]` | `YYYY-MM-DD` |

**Hypercare Exit Criteria**:
- [ ] No open P1 or P2 issues
- [ ] All integrations error-free for 5 consecutive business days
- [ ] Customer confirms system operating as expected
- [ ] Formal handoff to Customer Success completed

---

## 10. Customer Success Handoff

| Handoff Item | Detail |
|-------------|--------|
| CSM assigned | `[Name + email]` |
| Handoff call date | `YYYY-MM-DD` |
| QBR schedule | `[First QBR target date]` |
| Known expansion interest | `[Modules or features discussed for future — or "None"]` |
| Open support tickets at handoff | `[N tickets — link to queue — or "None"]` |
| Key customer contacts shared | `[ ] Yes  [ ] No` |
| Implementation summary shared with CSM | `[ ] Yes  [ ] No` |

---

## 11. Implementation Retrospective

*Complete at hypercare exit. Used for playbook improvement.*

**What went well**:
- `[Item 1]`
- `[Item 2]`

**What could be improved**:
- `[Item 1 — suggested improvement]`
- `[Item 2 — suggested improvement]`

**Recommended playbook updates**:
- `[Specific change to recommend to Implementation Lead — or "None"]`

---

*Go-Live Report v1.0 — Implementation / Implementation Engineer*
