---
name: accessibility-auditor-design
description: >
  This skill conducts full accessibility audits of shipped product experiences against WCAG
  and platform-specific standards. Use when asked to audit accessibility, evaluate inclusive
  design compliance, or assess assistive technology support. Also consider when a product
  launch has shipped without prior accessibility review. Suggest when post-launch analytics
  reveal user drop-off patterns consistent with accessibility barriers.
department: design
agent: head-of-design
version: 1.0.0
complexity: complex
related-skills: []
---

# accessibility-auditor-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Conducts full accessibility audits of shipped product experiences against WCAG standards, platform heuristics, and assistive technology compatibility requirements.

## When to Use

- When a product or feature has shipped and requires a comprehensive post-launch accessibility evaluation.
- When user complaints, support tickets, or session data indicate potential accessibility barriers.
- When regulatory requirements or partner contracts mandate documented accessibility compliance.
- When onboarding a newly acquired product or third-party integration that lacks accessibility documentation.

## Workflow

1. **Define audit scope**: Identify the product surfaces, user flows, and platforms to audit. Collect the applicable compliance level (WCAG 2.1 AA minimum). Deliverable: scoped audit brief listing screens, flows, and success criteria.
2. **Inventory existing state**: Pull current accessibility annotations, design tokens (colour contrast ratios, focus states, touch targets), and any prior audit reports. Deliverable: baseline inventory document.
3. **Execute automated checks**: Run automated tooling (axe-core, Lighthouse accessibility, colour-contrast analyzers) across all scoped surfaces. Record every violation with severity, WCAG criterion, and screenshot. Deliverable: raw automated findings log.
4. **Perform manual testing**: Test keyboard navigation, screen reader compatibility (VoiceOver, NVDA, TalkBack), magnification, reduced motion, and high-contrast mode. Document interaction sequences that fail. Deliverable: manual testing results matrix.
5. **Classify and prioritize findings**: Score each issue by severity (critical, major, minor), affected user population, and remediation effort. Apply the scoring rubric at `references/scoring-rubric.md`. Group by WCAG principle (Perceivable, Operable, Understandable, Robust). Deliverable: prioritized issue register.
6. **Draft remediation recommendations**: For each finding, specify the design change required -- updated colour tokens, focus ring additions, ARIA label corrections, reflow adjustments. Assign to design or engineering. Deliverable: remediation plan with owners and effort estimates.
7. **Compile audit report**: Assemble findings, screenshots, compliance scores, and remediation plan into a structured report. Include executive summary with pass/fail verdict. Deliverable: accessibility audit report.
8. **Present and hand off**: Walk stakeholders through critical findings and remediation timeline. File issues in the backlog with audit references. Deliverable: backlog tickets linked to audit findings.

## Anti-Patterns

- **Automated-only auditing**: Relying solely on automated tools and skipping manual assistive technology testing. *Why*: automated scanners catch roughly 30% of accessibility issues; keyboard traps, screen reader announcement order, and cognitive load problems require human evaluation.
- **Severity inflation**: Marking every finding as critical to force immediate action. *Why*: teams deprioritize everything when everything is urgent, and real critical issues (keyboard traps, missing alt text on primary actions) get buried.
- **Retrofitting bias**: Recommending overlay widgets or bolt-on fixes instead of design-level corrections. *Why*: overlays introduce new accessibility failures, create maintenance debt, and do not address root cause design decisions.
- **Scope creep into redesign**: Expanding the audit into a full redesign initiative without explicit approval. *Why*: the audit's value is diagnostic; mixing diagnosis with solution work delays the report and blurs accountability.

## Output

**On success**: Produces an accessibility audit report containing executive summary, compliance scorecard (per WCAG principle), prioritized issue register with screenshots, and a remediation plan with ownership assignments. Delivered as a structured document shared with design, engineering, and product leadership.

**On failure**: Report the audit scope that could not be completed, the blocking reason (missing platform access, unavailable assistive technology, incomplete design tokens), and recommended next steps to unblock. Every gap must specify what is needed to resume.

## Related Skills

- [`accessibility-checker-design`](../accessibility-checker-design/SKILL.md) -- Pre-handoff accessibility checks feed into post-launch audit baselines.
- [`design-review-runner`](../design-review-runner/SKILL.md) -- Design reviews may surface accessibility concerns that trigger a full audit.
- [`session-analysis`](../../../design/visual-interaction-designer/session-analysis/SKILL.md) -- Session recordings reveal real-user accessibility friction that scopes audit focus areas.
