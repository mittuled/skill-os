# Access Provisioning Report

**Period**: `[Month YYYY]` or `[Specific Event: New Hire / Role Change / Offboarding]`
**Prepared By**: `[IT Operations Manager]`
**Date**: `YYYY-MM-DD`
**Report Type**: `[ ] Routine Provisioning  [ ] Access Review  [ ] Incident Response`

---

## 1. Summary

| Metric | Count |
|--------|-------|
| Total provisioning actions this period | `##` |
| New access grants | `##` |
| Access modifications | `##` |
| Access revocations | `##` |
| Pending provisioning requests | `##` |
| SLA breaches | `##` |
| Unresolved exceptions | `##` |

---

## 2. Provisioning Actions Log

| Ticket ID | User | Action | System(s) | Access Level | Requested By | Approved By | Completed Date | SLA Met? |
|-----------|------|--------|-----------|--------------|-------------|-------------|----------------|----------|
| `TICKET-####` | `user@company.com` | `GRANT` | `[System]` | `[Tier]` | `[Name]` | `[Name]` | `YYYY-MM-DD` | `[ ] Yes [ ] No` |
| `TICKET-####` | `user@company.com` | `REVOKE` | `[System]` | `[Tier]` | `[Name]` | `[Name]` | `YYYY-MM-DD` | `[ ] Yes [ ] No` |

---

## 3. SLA Performance

| SLA Category | Target | Actual Average | Breaches |
|-------------|--------|---------------|---------|
| New hire standard access | Before start date | `X days` | `#` |
| Role change | 2 business days | `X hours` | `#` |
| Offboarding — standard | Same day | `X hours` | `#` |
| Offboarding — sensitive | 2 hours | `X hours` | `#` |
| Temporary access | 4 business hours | `X hours` | `#` |

**SLA Breach Details** *(if any)*:
```
[Describe each breach: Ticket ID, what was delayed, root cause, corrective action]
```

---

## 4. Access Review Results

*(Complete for periodic access reviews)*

| Access Type | Accounts Reviewed | Certified | Modified | Revoked | Escalated |
|------------|------------------|-----------|---------|---------|-----------|
| Admin / Tier 0 | `#` | `#` | `#` | `#` | `#` |
| Privileged / Tier 1 | `#` | `#` | `#` | `#` | `#` |
| Contractor / Guest | `#` | `#` | `#` | `#` | `#` |

**Revocation Details**:
```
[List any revoked access with justification]
```

---

## 5. Exceptions and Escalations

| Exception | User / System | Reason | Status | Owner | Target Resolution |
|-----------|--------------|--------|--------|-------|------------------|
| `[Description]` | `[User]` | `[Why it is an exception]` | `Open / Resolved` | `[Owner]` | `YYYY-MM-DD` |

---

## 6. Systems Provisioning Coverage

| System | Provisioning Method | Auto-Deprovisioning? | Last Audit |
|--------|--------------------|--------------------|-----------|
| `[System Name]` | `[SCIM / Manual / HRIS]` | `[ ] Yes  [ ] No` | `YYYY-MM-DD` |
| `[System Name]` | `[SCIM / Manual / HRIS]` | `[ ] Yes  [ ] No` | `YYYY-MM-DD` |

---

## 7. Upcoming Scheduled Reviews

| Review Type | Scope | Due Date | Assigned To |
|-------------|-------|---------|-------------|
| Monthly admin review | Tier 0 accounts | `YYYY-MM-DD` | `[Name]` |
| Quarterly privileged review | Tier 1 accounts | `YYYY-MM-DD` | `[Name]` |
| Contractor review | Active contractors | `YYYY-MM-DD` | `[Name]` |

---

## 8. Recommendations

```
[Optional: list any process improvements, tooling gaps, or policy updates recommended
based on this period's provisioning activity]
```

---

*Template version 1.0 — Technical Operations / IT Operations Manager*
