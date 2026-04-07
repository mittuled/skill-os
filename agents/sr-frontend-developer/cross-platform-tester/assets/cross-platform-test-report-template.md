# Cross-Platform Test Report: [Feature / Release Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Tester | Sr Frontend Developer |
| Feature | [Feature or release name] |
| Skill | cross-platform-tester |
| Status | [Pass / Fail / Conditional Pass] |

## Test Matrix

### Browsers (Desktop)

| Browser | Version | OS | Result | Issues |
|---------|---------|-----|--------|--------|
| Chrome | [Latest] | macOS / Windows | [Pass/Fail] | |
| Firefox | [Latest] | macOS / Windows | [Pass/Fail] | |
| Safari | [Latest] | macOS | [Pass/Fail] | |
| Edge | [Latest] | Windows | [Pass/Fail] | |

### Mobile

| Browser | Version | OS | Device | Result | Issues |
|---------|---------|-----|--------|--------|--------|
| Safari | [iOS Latest] | iOS [16/17] | iPhone 14/15 | [Pass/Fail] | |
| Chrome | [Android Latest] | Android 13/14 | Pixel / Samsung | [Pass/Fail] | |
| Samsung Internet | [Latest] | Android | Samsung Galaxy | [Pass/Fail] | |

### Minimum Supported Versions

| Browser | Min Version Tested | Result |
|---------|------------------|--------|
| Chrome | [Last 2 major] | [Pass/Fail] |
| Firefox | [Last 2 major] | [Pass/Fail] |
| Safari | [Last 2 major] | [Pass/Fail] |

## Visual Regression

| Screen / Component | Chrome | Firefox | Safari | Safari iOS | Chrome Android |
|-------------------|--------|---------|--------|-----------|----------------|
| [Homepage hero] | [Pass] | [Pass] | [Fail — see issue 1] | [Pass] | [Pass] |
| [Product card] | | | | | |
| [Checkout form] | | | | | |
| [Navigation menu] | | | | | |

## Functional Tests Across Platforms

| Feature | Chrome | Firefox | Safari | Safari iOS | Android Chrome |
|---------|--------|---------|--------|-----------|----------------|
| [Form submission] | [Pass] | | | | |
| [File upload] | | | | | |
| [Payment flow] | | | | | |
| [OAuth login] | | | | | |
| [Notifications / alerts] | | | | | |

## Issues Found

| # | Browser / OS | Severity | Description | Reproducible? | Fix |
|---|-------------|---------|-------------|--------------|-----|
| 1 | [Safari 17 / macOS] | [High] | [CSS grid gap not rendering correctly] | [Yes — screenshot attached] | [Use padding fallback] |

## Verdict

**Overall result**: [PASS / FAIL]
**Blocking issues**: [N — list IDs]

**Sign-off**: [Name] | Date: [YYYY-MM-DD]
