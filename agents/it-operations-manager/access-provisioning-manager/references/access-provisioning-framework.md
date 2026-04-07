# Access Provisioning Framework

Reference for the `access-provisioning-manager` skill.

---

## 1. ITIL-Aligned Access Management Principles

Access management is the ITIL process that grants authorised users the right to use a service while preventing access to non-authorised users.

### Core ITIL Access Concepts

| Concept | Definition |
|---------|-----------|
| **Identity** | Unique information about a user that distinguishes them from others |
| **Rights / Access** | The actual privileges granted to the identity |
| **Services / Resources** | Systems, data, and tools the identity may access |
| **Service Groups** | Collections of services with common access patterns (e.g., "Engineering Stack") |
| **Directory Services** | Central identity store (e.g., Okta, Azure AD, Google Workspace) |

---

## 2. Least-Privilege Access Model

### Principle
Grant users the minimum access required to perform their job function. Start with zero access; add only what is explicitly needed.

### Role-Based Access Tiers

| Tier | Description | Example Roles | Review Cadence |
|------|-------------|---------------|----------------|
| **Tier 0 — Admin** | Full system admin, destructive operations | IT Admin, Security Admin | Monthly |
| **Tier 1 — Privileged** | Elevated read/write, financial, HR data | Finance Lead, HR Manager | Quarterly |
| **Tier 2 — Standard** | Normal business tool access | All employees | Annual |
| **Tier 3 — Read-Only** | View access only | Auditors, contractors | Per-engagement |
| **Tier 4 — Guest** | Scoped temporary access | External collaborators | Per-engagement |

---

## 3. Provisioning Request Decision Matrix

| Request Type | Approval Required | Provisioning SLA | Notes |
|-------------|------------------|-----------------|-------|
| New hire — standard access | Auto-approved via HRIS integration | Before start date | Triggered by HRIS onboarding event |
| New hire — privileged access | Manager + IT approval | Before start date | Requires documented business justification |
| Role change — lateral | Manager approval | 2 business days | Remove old access; add new access |
| Role change — promotion | Manager + department head approval | 2 business days | Expand access only after promotion effective |
| Temporary access (≤30 days) | Manager approval | 4 business hours | Set expiry date at provisioning |
| Contractor / vendor | Manager + Legal approval | 2 business days | Scope to project systems only |
| Offboarding — standard | Auto-triggered by HRIS termination | Same day | Immediate revocation of all access |
| Offboarding — sensitive | IT + Legal notification | Within 2 hours | HR-flagged involuntary terminations |

---

## 4. Joiner-Mover-Leaver (JML) Lifecycle

### Joiner Checklist
1. HRIS triggers provisioning event
2. IT creates identity in directory service
3. Provision standard role-based access group
4. Provision any additional approved access
5. Send welcome email with credentials via secure channel
6. Set 90-day access review for any elevated permissions

### Mover Checklist
1. HRIS role-change event triggers review
2. Identify access deltas (what to add, what to remove)
3. Remove access that no longer applies to new role
4. Provision access required for new role
5. Log all changes with business justification
6. Confirm with employee's new manager

### Leaver Checklist
1. HRIS termination event triggers deprovisioning
2. Disable identity (do not delete — preserve audit trail)
3. Revoke all active sessions (SSO, API tokens, VPN)
4. Reclaim licences and hardware
5. Transfer ownership of assets to manager
6. Archive mailbox and files per retention policy
7. Log completion with timestamp

---

## 5. Access Review Standards

### Periodic Review Schedule

| Access Type | Review Frequency | Reviewer |
|------------|-----------------|----------|
| Admin / Tier 0 | Monthly | IT Manager + CISO |
| Privileged / Tier 1 | Quarterly | Department head |
| Standard / Tier 2 | Annual | Manager |
| Contractor / Guest | End of engagement | Sponsoring manager |

### Access Review Decision Options

- **Certify**: Access is appropriate; no action
- **Modify**: Reduce or change access; IT to apply
- **Revoke**: Remove access immediately; IT to apply
- **Escalate**: Needs investigation before decision

---

## 6. Audit Log Requirements

Every provisioning action must capture:

| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 datetime of the action |
| `action` | `GRANT`, `REVOKE`, `MODIFY` |
| `identity` | User ID or email address |
| `system` | Target system name |
| `access_level` | Permission tier or role name |
| `approver` | Person who approved the request |
| `requester` | Person who initiated the request |
| `ticket_id` | Reference to the provisioning ticket |
| `justification` | Business reason for the access |

---

## 7. Common Provisioning Anti-Patterns and Mitigations

| Anti-Pattern | Risk | Mitigation |
|-------------|------|-----------|
| Copy-paste permissions from peer | Permission creep | Provision from role templates, not peer profiles |
| Delayed leaver deprovisioning | Insider threat, data exposure | Auto-trigger from HRIS same-day |
| No expiry on temporary access | Permanent access via "temporary" grants | Mandatory expiry date on all temporary grants |
| Provisioning without ticket | No audit trail | Enforce ticket-required in provisioning tool |
| Shared service accounts | Cannot attribute actions to individuals | Prohibit shared credentials; use role accounts with audit logging |

---

*Reference version 1.0 — Technical Operations / IT Operations Manager*
