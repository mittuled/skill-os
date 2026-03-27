---
name: accessibility-auditor
description: >
  This skill audits the completed frontend for accessibility compliance before release. Use when asked to verify WCAG conformance, run a pre-release accessibility review, or certify a feature for launch. Also consider when legal or compliance teams request an accessibility attestation. Suggest when a release candidate is tagged and no accessibility sign-off exists.
department: engineering
agent: sr-frontend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../accessibility-checker-eng/SKILL.md
  - ../design-implementer/SKILL.md
  - ../cross-platform-tester/SKILL.md
---

# accessibility-auditor

## Agent: Sr. Frontend Developer

L3 senior frontend developer (Nx) responsible for implementing UI components, ensuring accessibility, and validating cross-platform compatibility.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Audits the completed frontend for accessibility compliance against WCAG 2.1 AA standards before release, producing a conformance report with pass/fail verdicts and remediation guidance for any violations.

## When to Use

- A release candidate is ready and no accessibility sign-off has been recorded.
- A new user-facing feature has completed development and needs pre-launch accessibility verification.
- Legal or compliance requests a formal accessibility conformance attestation.
- Customer feedback or support tickets report accessibility barriers.
- The product targets a regulated industry (healthcare, government, finance) with mandated accessibility standards.

## Workflow

1. **Define audit scope**: Identify all pages, flows, and interactive components included in the release. Deliverable: audit scope document listing URLs and component inventory.
2. **Run automated scans**: Execute axe-core, Lighthouse accessibility, or equivalent tooling against every in-scope page. Deliverable: raw scan results with issue severity ratings.
3. **Perform manual testing**: Test keyboard navigation, screen reader compatibility (NVDA, VoiceOver), focus management, and color contrast using manual inspection. Deliverable: manual test checklist with pass/fail per criterion.
4. **Classify findings**: Categorize each violation by WCAG success criterion, severity (critical, major, minor), and affected user group. Deliverable: classified issue list.
5. **Draft remediation guidance**: For each violation, write a specific fix recommendation with code examples where applicable. Deliverable: remediation plan with estimated effort per issue.
6. **Produce conformance report**: Compile automated and manual results into a single report with overall pass/fail verdict. Deliverable: accessibility conformance report.
7. **Communicate results**: Share the report with the product manager and design lead. Escalate critical blockers that must be fixed before release. Deliverable: stakeholder notification with release recommendation.

## Anti-Patterns

- **Automated-only auditing.** Relying solely on automated tools misses 30-50% of accessibility issues that require human judgment (focus order, meaningful alt text, cognitive load). *Why*: automated scanners cannot evaluate user experience or intent.
- **Auditing after deployment.** Running the audit post-release means inaccessible features reach users. *Why*: remediation after launch is more expensive and harms users in the interim.
- **Vague violation reports.** Listing WCAG criteria without specific element references or fix guidance leaves developers guessing. *Why*: actionable reports reduce mean time to remediation.
- **Skipping assistive technology testing.** Testing only with sighted keyboard navigation misses screen reader announcement issues. *Why*: screen reader users depend on semantic HTML and ARIA attributes that visual inspection cannot verify.

## Output

**On success**: Produces an accessibility conformance report containing automated scan results, manual test outcomes, classified violations with WCAG criterion references, and remediation guidance per issue. Includes an overall pass/fail verdict and release recommendation.

**On failure**: Report which pages or components could not be audited (e.g., authentication walls, dynamic content), what partial results were obtained, and what additional access or tooling is needed to complete the audit.

## Related Skills

- [`accessibility-checker-eng`](../accessibility-checker-eng/SKILL.md) -- checks accessibility during development; this skill validates the final result.
- [`design-implementer`](../design-implementer/SKILL.md) -- implements the UI that this skill audits for conformance.
- [`cross-platform-tester`](../cross-platform-tester/SKILL.md) -- tests cross-platform behaviour; accessibility auditing covers assistive technology compatibility.
