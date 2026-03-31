# IT Helpdesk Queue — Meridian AI

| Field | Value |
|---|---|
| Company | Meridian AI |
| Total Tickets | 5 |
| Open Tickets | 5 |
| P1 (Critical) | 1 |
| P2 (High) | 2 |
| P3 (Medium) | 2 |
| P4 (Low) | 0 |
| P1+P2 Requiring Immediate Action | 3 |
| Skill | it-helpdesk-operator |

## Ticket Queue — Priority Order

### P1 — INC-041: VPN Down — Engineering Team (Connectivity)
**Requester:** Marcus Webb (Senior Engineer)
**SLA:** 2 hours
**Impact:** High — multiple users affected; full engineering team blocked from AWS dev environment

**Resolution Steps:**
1. Confirm if issue is VPN, WiFi, or application-specific
2. Try basic restart (device, router, VPN reconnect) — if team-wide, skip individual troubleshooting
3. Check status pages: AWS status, VPN provider (Tailscale/Cisco AnyConnect)
4. Check VPN server/gateway logs for errors
5. Escalate to network admin or CTO if infrastructure-level issue
6. Post status update in #engineering Slack channel within 15 minutes

**Immediate Action:** Check VPN gateway status page and AWS us-east-1 status NOW. If VPN provider issue, post in #engineering immediately so team can plan around it.

---

### P2 — INC-042: Google Account Lockout — Diana Torres (Password Reset)
**Requester:** Diana Torres (Head of Design)
**SLA:** 1 hour
**Impact:** High — user fully blocked from email, Notion, Figma

**Resolution Steps:**
1. Verify Diana's identity (manager confirmation or employee ID)
2. Reset Google Workspace account in admin console
3. Re-enroll MFA with new device (Google Authenticator or hardware key)
4. Send temporary access via secure channel (SMS to confirmed mobile)
5. Confirm Diana can log into Google, Notion, and Figma
6. Log MFA device change in access register

---

### P2 — INC-043: MacBook Pro Won't Boot — Kevin Park (Hardware Issue)
**Requester:** Kevin Park (Operations)
**SLA:** 4 hours
**Impact:** Medium — single user; flashing folder icon = missing OS or disk failure

**Resolution Steps:**
1. Ask Kevin to try: hold Option at boot → check if drives appear
2. If no drives: likely SSD failure — pull loaner MacBook from inventory
3. If drives appear: attempt macOS Recovery (Cmd+R at boot)
4. Schedule data recovery if SSD is failed (check Time Machine or cloud backup first)
5. Book device for repair (Apple Authorised or mail-in)
6. Update asset tracker with repair status

**Note:** Kevin's MacBook is the 5-year Intel MacBook Pro flagged in the hardware lifecycle audit as overdue for replacement. This repair incident is a good trigger to accelerate replacement.

---

### P3 — INC-044: Salesforce + Outreach Install — New Hire 2 (Software Install)
**Requester:** New Hire 2 (Sales)
**SLA:** 2 hours
**Impact:** Medium — single user

**Resolution Steps:**
1. Confirm Salesforce and Outreach are on approved tool list (both standard Sales tools)
2. Assign Salesforce licence from existing 10-seat contract (7 unused seats)
3. Deploy Outreach licence — confirm seat is available
4. Configure Salesforce via MDM or guided install
5. Confirm both tools are working

---

### P3 — INC-045: Deleted Notion Page — Jordan Lee (Data Recovery)
**Requester:** Jordan Lee (CPO)
**SLA:** 8 hours
**Impact:** Medium — Q2 product roadmap content recoverable from Notion trash

**Resolution Steps:**
1. Check Notion trash (recoverable within 30 days): Settings → Trash → restore page
2. If not in trash: check Notion page history (version history available on paid plans)
3. If recovered: advise Jordan to duplicate to a safe location immediately
4. Advise Jordan to use Notion lock/archive feature for critical documents

**Likely Resolution:** Notion pages are retained in trash for 30 days. Deleted yesterday — should be recoverable via Notion trash immediately. Jordan can do this themselves: click Trash in Notion sidebar, find the page, click Restore.

## Today's Work Plan

| Time | Action |
|---|---|
| Now | Check VPN/AWS status page — update #engineering within 15 min |
| Next 30 min | Reset Diana Torres' Google account and MFA |
| Within 1 hr | Call Kevin Park re: MacBook boot issue; pull loaner if needed |
| After lunch | Provision Salesforce/Outreach for New Hire 2 |
| Before EOD | Guide Jordan Lee to recover Notion page via trash |
