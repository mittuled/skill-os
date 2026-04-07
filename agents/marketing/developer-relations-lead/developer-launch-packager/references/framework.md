# Framework: developer-launch-packager

Defines the asset inventory model, launch sequencing rules, versioning standards, changelog format, and readiness gates for packaging developer product launches.

## Asset Inventory Model

### Required Assets by Launch Type

| Asset | New Product | Major Version | Minor Version | Patch |
|-------|------------|--------------|--------------|-------|
| SDK packages (all target languages) | Required | Required | Required | Required |
| API reference docs | Required | Required | Update | Update |
| Quickstart guide | Required | Update | Check | Check |
| Sample applications (all target languages) | Required | Required | Update | Check |
| Migration guide | — | Required | Required if breaking | — |
| Changelog entry | Required | Required | Required | Required |
| Launch blog post | Required | Required | Optional | — |
| Release notes (concise) | — | Required | Required | Required |
| Social media posts | Required | Required | Optional | — |
| Developer newsletter section | Required | Required | Optional | — |
| Demo video / GIF | Required | Update | — | — |

### Asset Readiness States

| State | Definition | Blocks Launch? |
|-------|-----------|---------------|
| Not started | Work not begun | Yes |
| In progress | Draft exists but not reviewed | Yes |
| In review | Submitted for technical review | No (can proceed to staging) |
| Approved | Reviewed and signed off | No |
| Staged | Published to staging environment | No |
| Live | Published to production | N/A — published |

## Semantic Versioning Reference

| Change Type | Version Bump | Examples |
|------------|-------------|---------|
| Breaking change (removes/renames public API) | Major (v1 → v2) | Endpoint renamed, param removed, auth scheme changed |
| New feature (backward compatible) | Minor (v1.1 → v1.2) | New endpoint, new SDK method, new webhook event |
| Bug fix or backward-compatible patch | Patch (v1.1.0 → v1.1.1) | Error message fix, performance improvement, doc fix |
| Pre-release | v1.0.0-beta.1 | Public beta before stable release |

**Rule**: Never increment patch for documentation-only changes without a corresponding code change.

## Keep a Changelog Format

Each changelog entry must follow this structure:

```markdown
## [version] — YYYY-MM-DD

### Added
- [Feature or capability that is new]

### Changed
- [Behaviour that changed in a backward-compatible way]

### Deprecated
- [Feature that will be removed in a future major version]

### Removed
- [Feature removed in this version — major version only]

### Fixed
- [Bug that was corrected]

### Security
- [Vulnerability addressed — always include if applicable]
```

## Launch Sequence Protocol

Publish assets in this order. Do not deviate — out-of-sequence publishing creates developer confusion during peak traffic.

| Step | Asset | Timing | Why This Order |
|------|-------|--------|---------------|
| 1 | SDK packages (all package managers) | T-0 (launch moment) | Code available before docs are read |
| 2 | API reference docs (staged → live) | T-0 + 0 min | Developers verify API immediately |
| 3 | Changelog published | T-0 + 5 min | Existing developers check what changed |
| 4 | Migration guide (major versions only) | T-0 + 5 min | Upgrading developers need this before reading blog |
| 5 | Sample apps updated (GitHub) | T-0 + 10 min | Developers clone samples to verify |
| 6 | Launch blog post | T-0 + 15 min | Broader announcement after assets are live |
| 7 | Social media posts | T-0 + 15 min | Points to live blog and docs |
| 8 | Developer newsletter | T-0 + 1 hour | Give community time to discover before blast |

## Pre-Launch Readiness Gates

All gates must pass before publishing any asset.

### Gate 1: Engineering Sign-off
- [ ] SDK version pinned and tagged in all repositories
- [ ] Breaking changes documented and approved by product
- [ ] Deprecation notices in SDK for removed features
- [ ] API version confirmed and stable

### Gate 2: Documentation Readiness
- [ ] All docs updated for new version and staged
- [ ] Changelog entry written and reviewed
- [ ] Migration guide complete (major versions)
- [ ] Code samples tested against released SDK version
- [ ] All internal links verified working

### Gate 3: Asset Completeness
- [ ] Sample apps run against final SDK with zero errors
- [ ] Blog post reviewed by technical reviewer and edited
- [ ] Social copy approved by brand
- [ ] Newsletter draft reviewed

### Gate 4: First-Run Experience Validated
- [ ] Developer experience review completed (DX grade B or above)
- [ ] TTFHW measured against released assets (not staging)
- [ ] All P1 issues from DX review resolved
