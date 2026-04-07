# GitHub Organization Setup Checklist: [Org Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Organization | [GitHub org name] |
| Skill | github-org-setup |
| Status | [In Progress / Complete] |

---

## Category 1: Organization Settings

- [ ] Organization name and profile set (logo, description, URL)
- [ ] Default repository visibility: Private
- [ ] Base permissions for org members: Read (not Write)
- [ ] Fork policy: Disabled for private repos (unless explicitly required)
- [ ] Member email visibility: Private (members only)
- [ ] Two-factor authentication required for all org members
- [ ] SSH certificate authority configured (if using SAML/SSO)
- [ ] SAML SSO enabled and tested with IdP (Okta / Azure AD / Google)
- [ ] Verified domain(s) for organization

---

## Category 2: Teams and Access Control

- [ ] Team structure mirrors org chart (Engineering / Frontend / Backend / DevOps / etc.)
- [ ] Team maintainers assigned (at least 2 per team)
- [ ] Repository access granted to teams (not individual members)
- [ ] Admin access limited to senior engineers only (< 5 people)
- [ ] No individuals with direct admin access to production repos outside their team
- [ ] Outside collaborators reviewed and minimized
- [ ] Offboarding procedure tested: removing a user removes all repo access

---

## Category 3: Repository Standards

**Default branch settings (apply to all repos via ruleset):**

- [ ] Default branch name: `main`
- [ ] Branch protection on `main`:
  - [ ] Require PR before merging
  - [ ] Require minimum 1 approving review
  - [ ] Dismiss stale PR approvals on new commits
  - [ ] Require status checks to pass (CI must pass)
  - [ ] Require branches to be up to date
  - [ ] No direct pushes to `main` (enforce for admins too)
  - [ ] No force pushes
  - [ ] No branch deletion

- [ ] Required PR template created (`.github/PULL_REQUEST_TEMPLATE.md`)
- [ ] Issue templates created (Bug report, Feature request)
- [ ] CODEOWNERS file configured for critical paths
- [ ] `.gitignore` and `.gitattributes` in default template repo

---

## Category 4: Security Settings

- [ ] Secret scanning enabled (org-wide)
- [ ] Push protection enabled (prevent secret commits)
- [ ] Dependabot security alerts enabled (org-wide)
- [ ] Dependabot version updates enabled for critical repos
- [ ] Code scanning (CodeQL) enabled for all application repos
- [ ] GitHub Advanced Security enabled (if on Enterprise)
- [ ] Security advisories policy: private vulnerability reporting enabled

---

## Category 5: Actions and CI/CD

- [ ] GitHub Actions enabled
- [ ] Allowed actions policy: [All / Only verified actions + specific allowlist]
- [ ] Default workflow permissions: Read (not Write) — jobs request write only when needed
- [ ] Secrets management: org-level secrets for shared credentials, repo-level for service-specific
- [ ] Required workflows: CI pipeline enforced on all PRs via ruleset
- [ ] Runner type: [GitHub-hosted / Self-hosted — document runner setup]
- [ ] Artifact retention policy set (default 90 days → reduce to 30 for cost)

---

## Category 6: Audit and Compliance

- [ ] Audit log streaming enabled to: [SIEM / S3 / Splunk]
- [ ] Audit log retention: [90 days / 1 year]
- [ ] Webhooks configured for relevant org events (push, PR, member changes)
- [ ] GitHub Enterprise compliance features configured (if applicable)

---

## Open Items

| # | Category | Item | Owner | Due |
|---|----------|------|-------|-----|
| 1 | [Category] | [Specific item] | [Role] | [Date] |
