# IT Helpdesk Ticket Record

**Ticket ID**: `[IT-####]`
**Date Created**: `YYYY-MM-DD HH:MM UTC`
**Created By**: `[Agent Name]`

---

## 1. Requester Information

| Field | Value |
|-------|-------|
| **User Name** | `[Full Name]` |
| **Email** | `[user@company.com]` |
| **Department** | `[Department]` |
| **Location** | `[Office / Remote — City]` |
| **Device Asset ID** | `[ASSET-#### or N/A]` |

---

## 2. Ticket Classification

| Field | Value |
|-------|-------|
| **Category** | `[ ] Hardware  [ ] Software  [ ] Access  [ ] Network  [ ] Account  [ ] Security` |
| **Priority** | `[ ] P1 Critical  [ ] P2 High  [ ] P3 Medium  [ ] P4 Low` |
| **Subject** | `[Brief description of the issue]` |

**Issue Description**:
```
[Detailed description of the issue as reported by the user. Include:
- What they were trying to do
- What happened instead
- Error messages (exact text)
- When the issue started
- How many users affected]
```

---

## 3. Diagnosis

**Assigned To**: `[IT Support Specialist Name]`
**Assigned Date**: `YYYY-MM-DD`
**First Response Sent**: `YYYY-MM-DD HH:MM UTC`
**First Response SLA Met**: `[ ] Yes  [ ] No`

**Diagnostic Steps Taken**:
```
[Step-by-step record of diagnostics performed]
1. [Action taken] → [Result / observation]
2. [Action taken] → [Result / observation]
3. ...
```

**Root Cause Identified**:
```
[One-line summary of what caused the issue, or "Under investigation" if still diagnosing]
```

---

## 4. Resolution

**Resolution Method**: `[ ] Fixed by IT  [ ] Escalated to IT Operations  [ ] Escalated to Vendor  [ ] User action`

**Steps Applied**:
```
[Exact steps taken to resolve the issue]
1. [Step]
2. [Step]
```

**Workaround Provided**: `[ ] Yes  [ ] No`

If workaround: `[Describe the temporary workaround given to the user]`

**Permanent Fix Required**: `[ ] Yes (ticket #____)  [ ] No`

---

## 5. Escalation (if applicable)

**Escalated**: `[ ] Yes  [ ] No`

If Yes:
| Field | Value |
|-------|-------|
| **Escalated To** | `[IT Operations Manager / Security / Vendor: vendor name]` |
| **Escalation Date** | `YYYY-MM-DD HH:MM` |
| **Escalation Ticket Ref** | `[Reference ticket or incident ID]` |
| **Reason for Escalation** | `[Brief justification]` |
| **Context Provided** | `[ ] Diagnostic notes attached  [ ] Access granted to agent  [ ] Screenshots shared` |

---

## 6. Closure

**Resolution Date**: `YYYY-MM-DD HH:MM UTC`
**Time to Resolution**: `[X hours Y minutes]`
**SLA Met**: `[ ] Yes  [ ] No`

**User Confirmation**:
- `[ ] User confirmed issue is resolved`
- `[ ] Closed without confirmation (reason: ___________)`

**Follow-Up Required**: `[ ] Yes (due YYYY-MM-DD)  [ ] No`

---

## 7. Ticket Notes

```
[Any additional context, learnings, or notes for future reference.
Example: "This is the third occurrence of this VPN issue for this user — flag for
investigation of their network configuration."]
```

---

*Template version 1.0 — Technical Operations / IT Support Specialist*
