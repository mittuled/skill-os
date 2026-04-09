---
name: cross-platform-tester
description: >
  This skill tests the frontend across browsers, devices, and operating systems to ensure consistent behaviour. Use when asked to verify cross-browser compatibility, validate responsive behaviour, or test on specific device targets. Also consider when a release targets a new platform or browser version. Suggest when a feature uses APIs with uneven browser support.
department: engineering
agent: sr-frontend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../accessibility-auditor/SKILL.md
  - ../design-implementer/SKILL.md
triggers:
  - "test cross-platform"
  - "cross-browser testing"
  - "cross-platform compatibility"
  - "multi-browser test"
  - "device compatibility test"
---

# cross-platform-tester

## Agent: Sr. Frontend Developer

L3 senior frontend developer (Nx) responsible for implementing UI components, ensuring accessibility, and validating cross-platform compatibility.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Tests the frontend across browsers, devices, and operating systems to verify consistent visual rendering, interaction behaviour, and performance within the defined browser support matrix.

## When to Use

- A feature reaches QA-ready status and must be validated across the browser support matrix before release.
- The application adopts a new web API (e.g., CSS container queries, View Transitions) with uneven browser support.
- User reports or analytics indicate rendering or behaviour anomalies on specific platforms.
- A new device form factor or OS version enters the supported platform list.
- A CSS or JavaScript framework upgrade may introduce cross-browser regressions.

## Workflow

1. **Confirm test matrix**: Retrieve the current browser and device support matrix from project documentation. Deliverable: test matrix listing browser/version, OS, and device combinations.
2. **Identify risk areas**: Review the changeset for features using APIs or CSS properties with known cross-browser inconsistencies (check caniuse.com or MDN compatibility tables). Deliverable: risk assessment listing high-risk features per browser.
3. **Execute visual regression tests**: Run visual comparison tools (Percy, Chromatic, or Playwright screenshot assertions) across matrix targets. Deliverable: visual diff report with flagged deviations.
4. **Test interactive behaviour**: Manually or via automation verify form submissions, animations, gestures (touch, hover), and keyboard interactions on each target. Deliverable: interaction test results per platform.
5. **Measure performance**: Run Lighthouse or WebPageTest on representative matrix targets to catch platform-specific performance regressions. Deliverable: performance scores per platform.
6. **Document and triage findings**: Log each defect with platform, reproduction steps, expected vs. actual behaviour, and severity. Deliverable: cross-platform defect report with triage recommendations.
7. **Recommend polyfills or fallbacks**: For unavoidable incompatibilities, propose polyfills, progressive enhancement strategies, or graceful degradation paths. Deliverable: mitigation plan per defect.

## Anti-Patterns

- **Testing only on Chrome.** Chrome-only testing misses Safari layout quirks, Firefox accessibility differences, and mobile browser limitations. *Why*: each rendering engine has unique behaviours that only surface on that engine.
- **Skipping real devices.** Emulators miss touch latency, viewport quirks, and OS-level font rendering differences. *Why*: emulated environments approximate but do not replicate real device constraints.
- **Testing at the end.** Deferring cross-platform testing to the final sprint stage leaves no time to fix platform-specific bugs. *Why*: cross-browser fixes often require architectural changes that are expensive to retrofit.
- **No defined support matrix.** Testing without a documented matrix leads to inconsistent coverage and scope creep. *Why*: without boundaries, every browser bug becomes a potential release blocker.

## Output

**On success**: Produces a cross-platform test report containing visual regression results, interaction test outcomes, performance scores per platform, and a defect list with severity and mitigation recommendations. Includes an overall platform-readiness verdict.

**On failure**: Report which matrix combinations could not be tested (e.g., unavailable devices, BrowserStack quota), what partial coverage was achieved, and what additional resources are needed to complete testing.

## Related Skills

- [`accessibility-auditor`](../accessibility-auditor/SKILL.md) -- audits accessibility which overlaps with assistive technology cross-platform concerns.
- [`design-implementer`](../design-implementer/SKILL.md) -- builds the frontend that this skill validates across platforms.
