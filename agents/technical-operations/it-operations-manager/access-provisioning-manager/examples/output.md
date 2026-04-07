# Access Provisioning — Sarah Chen (VP Engineering)

| Field | Value |
|---|---|
| Company | Meridian AI |
| Request Type | Onboarding |
| Employee | Sarah Chen |
| Role | Senior Engineer (VP Engineering) |
| Department | Engineering |
| Manager | Alex Chen (CEO) |
| Start Date | 2026-04-14 |
| SLA | 4 hours (complete before end of April 13) |
| Systems to Grant | 11 |
| Systems to Revoke | 0 |
| Skill | access-provisioning-manager |

## Access to Provision

### Standard Senior Engineer Template
| System | Access Level | Notes |
|---|---|---|
| GitHub | Write + Org-Admin | Elevated per VP role |
| Slack | Full member | Add to #engineering, #leadership, #all-hands |
| Notion | Editor | Add to Engineering workspace |
| Zoom | Host licence | Standard |
| 1Password | Teams member | Add to Engineering vault |
| AWS (dev) | Developer | Standard |
| AWS (staging) | Developer | Standard |
| Jira | Member | Add to all Engineering projects |
| PagerDuty | Admin | Elevated per VP role |

### Additional Access (VP Engineering specific)
| System | Access Level | Notes |
|---|---|---|
| AWS (production) | Admin | Production access — requires MFA before activation |
| Rippling | Read-only HR | CEO approval documented |
| Google Drive (Board Materials) | View | CEO requested — confirm folder sharing with CEO before start date |

## Provisioning Checklist

- [ ] Create identity in SSO provider (Okta/Google Workspace) for Sarah Chen
- [ ] Set temporary password and enforce change at first login
- [ ] Enrol in MFA (authenticator app) — mandatory before first login
- [ ] Provision all systems per senior engineer + VP Engineering template
- [ ] Add to Slack channels: #engineering, #leadership, #all-hands, #eng-leads
- [ ] Send welcome email with IT onboarding guide
- [ ] Schedule 15-minute IT onboarding call for April 14 AM
- [ ] Confirm all access is working end-of-day April 14
- [ ] AWS production admin — activate only after MFA is confirmed
- [ ] Share board materials folder (Google Drive) — confirm with CEO

## Notes

- Board materials folder access was requested by CEO; confirm with CEO before provisioning as this is non-standard for engineering roles
- AWS production admin is elevated — ensure MFA is set up and confirmed before activating production credentials
- PagerDuty admin access gives Sarah on-call schedule management; brief her on current on-call rotation on day 1

## Security Notes

- Production AWS access should be reviewed at 90-day access review cycle (high-risk access)
- Document VP Engineering elevated access grants in the access register for SOC 2 audit evidence
