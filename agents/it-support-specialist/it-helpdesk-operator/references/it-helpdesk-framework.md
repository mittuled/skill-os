# IT Helpdesk Operations Framework

Reference for the `it-helpdesk-operator` skill.

---

## 1. ITIL Incident Management Alignment

The helpdesk follows ITIL incident management principles to restore normal service operation as quickly as possible and minimise business impact.

| ITIL Concept | Helpdesk Application |
|-------------|---------------------|
| **Incident** | Any unplanned interruption to an IT service (hardware failure, software crash, access issue) |
| **Service Request** | Standard request for information or change (password reset, new software install, account creation) |
| **Problem** | Underlying cause of one or more incidents; escalated to IT Operations for root cause analysis |
| **Known Error** | Documented problem with a workaround; referenced during incident resolution |
| **Workaround** | Temporary fix that restores service; documented in ticket even if permanent fix is pending |

---

## 2. Ticket Category and Priority Matrix

### Category Classification

| Category | Description | Examples |
|----------|-------------|---------|
| **Hardware** | Physical device issues | Laptop not booting, screen damage, keyboard failure, printer jam |
| **Software** | Application or OS issues | App won't launch, software crash, update failure, licence error |
| **Access** | Authentication and permission issues | Password reset, account lockout, VPN issue, MFA problem |
| **Network** | Connectivity issues | Wi-Fi disconnects, VPN slow, can't reach internal services |
| **Account** | User account management | New account setup, account change, departing employee offboarding |
| **Security** | Security-related issues | Phishing email, suspicious activity, malware suspicion |

### Priority Assignment Matrix

| Priority | Criteria | SLA — First Response | SLA — Resolution |
|----------|----------|---------------------|-----------------|
| **P1 — Critical** | Multiple users affected; business operations blocked | 15 minutes | 2 hours |
| **P2 — High** | Single user blocked on core work function | 1 hour | 4 hours |
| **P3 — Medium** | User impaired but workaround available | 4 hours | 1 business day |
| **P4 — Low** | Non-urgent request; question or minor inconvenience | 1 business day | 3 business days |

---

## 3. First-Day IT Setup Checklist

Use this checklist for new hire IT onboarding:

- [ ] Identity account created (email, directory)
- [ ] SSO enrolled and MFA set up
- [ ] Laptop configured, tested, and delivered
- [ ] Password manager account created and vault shared
- [ ] VPN access configured and tested
- [ ] Required software installed (per role tier)
- [ ] Printer / peripheral setup (if office-based)
- [ ] IT helpdesk contact information provided to new hire
- [ ] Ticket created and linked to HRIS onboarding event

---

## 4. Common Issue Resolution Playbook

### Password Reset
1. Verify identity via secondary channel (manager confirmation or ID challenge)
2. Reset via IdP admin console
3. Force password change on next login
4. Confirm user can log in
5. Close ticket

### Account Lockout
1. Verify identity
2. Check lockout reason in IdP logs (failed attempts vs. suspicious activity)
3. If suspicious: escalate to IT Operations before unlocking
4. If routine lockout: unlock account in IdP
5. Advise user on MFA and password manager best practices

### Laptop Not Booting
1. Ask user to perform hard reset (hold power 10 seconds)
2. If no improvement: check power adapter; try known-good adapter
3. If no improvement: remote diagnostics via MDM (if device checks in)
4. If hardware failure confirmed: escalate to hardware lifecycle team
5. Issue loan device if user is blocked

### VPN Connectivity Issue
1. Confirm VPN client version is current
2. Ask user to disconnect, restart VPN client, reconnect
3. Check VPN server status (IT internal monitoring)
4. If server issue: notify IT Operations; post status update
5. If client issue: re-install VPN client

### MFA Not Working
1. Verify time sync on user's authenticator app (TOTP requires accurate clock)
2. If push MFA: check mobile data/Wi-Fi; push can fail without network
3. Provide emergency bypass code if available (log the use)
4. Reset MFA enrollment in IdP if device lost/changed
5. Re-enroll user in authenticator app

---

## 5. Escalation Decision Tree

```
Issue received
├── Security-related (phishing / malware / suspicious)?
│   └── ESCALATE IMMEDIATELY to IT Operations Manager + Security
│
├── Multiple users affected (P1)?
│   └── ESCALATE to IT Operations Manager; open incident ticket
│
├── Within Tier-1 scope (password / software / hardware basics)?
│   └── RESOLVE at Tier-1; document in ticket
│
├── Requires admin access to infrastructure / servers?
│   └── ESCALATE to IT Operations Manager
│
└── Requires vendor support (warranty / SaaS bug)?
    └── ESCALATE to vendor with ticket reference; monitor SLA
```

---

## 6. Ticket Quality Standards

Every closed ticket must include:

| Field | Requirement |
|-------|-------------|
| **Category** | Hardware / Software / Access / Network / Account / Security |
| **Priority** | P1 / P2 / P3 / P4 |
| **Root Cause** | One-line description of what caused the issue |
| **Resolution** | Steps taken and final fix applied |
| **Time to First Response** | Timestamp of first response to user |
| **Time to Resolution** | Timestamp of user confirmation or ticket close |
| **Escalated?** | Yes (to whom) / No |

---

*Reference version 1.0 — Technical Operations / IT Support Specialist*
