---
name: session-analysis-uxr
description: >
  This skill analyses user session recordings and usability tests to identify research-backed
  design insights. Use when asked to review session recordings, analyse usability test videos,
  or extract patterns from user sessions. Also consider when the team has session recordings
  piling up without analysis. Suggest when the user has usability test data that has not been
  systematically reviewed.
department: design
agent: ux-researcher
version: 1.0.0
complexity: medium
related-skills:
  - prototype-usability-validator
  - user-feedback-synthesiser
  - feedback-loop-formaliser-uxr
triggers:
  - "analyse research session"
  - "session analysis uxr"
  - "research session review"
  - "analyse user session"
  - "session findings"
---

# session-analysis-uxr

## Agent: UX Researcher

L3 UX researcher (Nx) responsible for user feedback synthesis, session analysis, and feeding research findings back into the product and design cycle.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Analyses user session recordings and usability tests to identify research-backed design insights, surfacing behavioural patterns that self-reported feedback alone would miss.

## When to Use

- When usability test sessions have been recorded and need systematic analysis to extract findings beyond the facilitator's in-session observations.
- When session replay tools (e.g., FullStory, Hotjar) have accumulated recordings around a specific flow and the design team needs a behavioural analysis.
- When quantitative analytics show anomalies (rage clicks, unexpected drop-offs) that require session-level investigation to diagnose.

## Workflow

1. **Session Selection**: Select sessions for analysis based on criteria relevant to the research question (user segment, feature area, task type, anomaly flags). Deliverable: session sample list with selection rationale.
2. **Observation Framework Setup**: Define the behavioural signals to track: task completion, hesitations, error recovery, backtracking, rage clicks, verbal frustration markers (for think-aloud sessions), and time-on-task. Deliverable: observation coding framework.
3. **Session Review & Coding**: Review each session, timestamping and coding observed behaviours using the framework. Capture verbatim quotes and screenshot key moments. Deliverable: coded session logs.
4. **Pattern Identification**: Analyse coded data across sessions to identify recurring patterns. Distinguish between isolated incidents and systematic issues (3+ participants exhibiting the same behaviour). Deliverable: pattern summary with frequency counts.
5. **Insight Generation**: Translate patterns into design insights, each stating the observed behaviour, the probable cause, the user impact, and a recommended design response. Deliverable: session analysis report with prioritised insights.

## Anti-Patterns

- **Cherry-picking sessions**: Selecting only sessions that support a pre-existing hypothesis. *Why*: biased session selection produces findings that confirm assumptions rather than revealing the full picture of user behaviour.
- **Counting without context**: Reporting only frequency metrics (e.g., "4 of 6 users struggled") without describing the qualitative context of how and why they struggled. *Why*: frequency without context does not give designers enough information to craft an effective solution.
- **Analysis paralysis**: Attempting to code every micro-behaviour in every session rather than focusing on signals relevant to the research question. *Why*: exhaustive coding delays insight delivery and buries critical findings in noise.
- **Skipping timestamping**: Noting observations without session timestamps. *Why*: untimestamped observations cannot be verified or shared as video clips with stakeholders, reducing credibility and impact.

## Output

**On success**: Produces a session analysis report containing coded session logs, pattern summary with frequency data, and prioritised design insights with recommendations. Delivered as a shared document, optionally supplemented with timestamped video clips of key moments.

**On failure**: Report which sessions could not be analysed (e.g., recording quality issues, missing audio for think-aloud), what partial analysis was completed, and recommend re-recording or alternative analysis methods.

## Related Skills

- [`prototype-usability-validator`](../../../design/ux-research-lead/prototype-usability-validator/SKILL.md) — Usability test sessions are a primary input for session analysis.
- [`user-feedback-synthesiser`](../user-feedback-synthesiser/SKILL.md) — Session analysis complements self-reported feedback with observed behavioural data.
- [`feedback-loop-formaliser-uxr`](../feedback-loop-formaliser-uxr/SKILL.md) — Session analysis insights enter the formalised feedback loop.
