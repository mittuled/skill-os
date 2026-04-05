# Checklist: github-org-setup

Verification checklist for configuring a GitHub organization to production-grade security and access standards.

## Phase 1: Organization Structure

- [ ] Define team hierarchy mapping to the engineering team structure (squads, platform, security, ops)
- [ ] Identify repository visibility defaults: internal (for monorepos), private (for sensitive services), or public (for OSS)
- [ ] Designate at least two organization owners (no single-owner risk)
- [ ] Confirm billing and license capacity before provisioning teams

**Exit criteria**: Team structure documented, owner list confirmed with two minimum.

## Phase 2: Team and Permission Configuration

- [ ] Create GitHub teams with descriptive names matching org chart (e.g., `backend-engineers`, `platform-team`)
- [ ] Assign team roles: `member` for most developers, `maintainer` for team leads
- [ ] Grant repository access via teams only — no individual user repository permissions
- [ ] Apply least-privilege access levels: `read` (external contributors), `write` (team members), `maintain` (leads), `admin` (owners only)
- [ ] Remove or audit any pre-existing individual repository permissions
- [ ] Set up SAML/SSO if the organization uses an identity provider (Okta, Azure AD)
- [ ] Enable two-factor authentication requirement for all organization members

**Exit criteria**: All repository access granted through teams, no individual grants, 2FA enforced.

## Phase 3: Repository Standards

- [ ] Configure organization-level repository creation policy (who can create repositories)
- [ ] Create template repositories with standard files: `.gitignore`, `LICENSE`, `CODEOWNERS`, CI pipeline stubs
- [ ] Set default branch name to `main` across all repositories
- [ ] Configure default branch protection (see Phase 4) as the organization default
- [ ] Enable repository dependency graphs organization-wide

**Exit criteria**: Template repositories created, default branch name standardized.

## Phase 4: Branch Protection Rules (for each critical repository)

- [ ] Enable branch protection on `main` (and `production` if used)
- [ ] Require pull request before merging: minimum 1 reviewer (2 for security-critical repos)
- [ ] Enable "Require approvals to be up-to-date" (dismiss stale reviews on new commits)
- [ ] Require status checks to pass: CI build, unit tests, linting (specify checks by name)
- [ ] Require branches to be up to date before merging
- [ ] Disallow force pushes to protected branches
- [ ] Disallow deletion of protected branches
- [ ] Set up CODEOWNERS for security-critical paths (`/auth`, `/payments`, `/infra`)
- [ ] Require code owner review for CODEOWNERS-matched files

**Exit criteria**: Branch protection enabled on all critical branches, force push blocked.

## Phase 5: Security Features

- [ ] Enable Dependabot security alerts for all repositories
- [ ] Enable Dependabot auto-updates (grouped by patch/minor) for dependency updates
- [ ] Enable GitHub Advanced Security (secret scanning) if on Enterprise plan
- [ ] Enable code scanning with CodeQL for repositories with application code
- [ ] Configure secret scanning push protection to block commits containing detected secrets
- [ ] Enable private vulnerability reporting for repositories receiving external contributions
- [ ] Review and configure organization-level Actions permissions (restrict to trusted actions only)

**Exit criteria**: Secret scanning active, Dependabot alerts enabled, CodeQL scanning running on CI.

## Phase 6: Audit and Documentation

- [ ] Export and review the organization audit log for any anomalous access events
- [ ] Document team permissions matrix: team name → repository access level
- [ ] Document branch protection policy with rationale for any exceptions
- [ ] Store documentation in the internal wiki and link from the engineering onboarding guide
- [ ] Schedule quarterly access review: verify team membership matches current org chart
- [ ] Configure organization-level audit log retention (90 days minimum; 1 year recommended)

**Exit criteria**: Documentation published, access review scheduled, audit log retention configured.
