# Research-Informed Flow Design Reference

## Purpose

Guidelines for designing user flows that are grounded in research data rather than assumptions — ensuring flows reflect real user mental models, terminology, and task sequences.

## From Research to Flow: Translation Process

| Research Output | What It Informs | Flow Design Decision |
|----------------|----------------|---------------------|
| JTBD map (job stages) | The backbone of the user flow | Each job stage becomes a major node in the flow |
| Interview findings (current behaviour) | Entry points and first actions | Flow entry state matches user's existing mental model |
| Task sequence from contextual inquiry | Step order within the flow | Steps ordered to match natural task cadence |
| Terminology from interviews | Labels and CTA copy | Use participant language, not product jargon |
| Drop-off points from analytics | Where branches and safety nets are needed | Add back navigation, confirmation steps at drop-off points |
| Session analysis friction findings | States and error handling | Error and recovery states address observed failure points |

## Mental Model Alignment Principles

Users bring expectations from prior experience. Research-informed flows respect those expectations:

| Principle | How to Apply |
|-----------|-------------|
| Match the user's task sequence | If research shows users check X before doing Y, design the flow with that order |
| Use user vocabulary | Terminology used by majority of interview participants should appear in labels |
| Preserve familiar patterns | Only introduce unfamiliar interaction patterns when research shows a genuine need |
| Locate actions where users expect them | Follow eye-tracking and click-map patterns to position CTAs |

## Flow Validation Against Research Data

Before finalising a flow design, validate each decision against evidence:

| Flow Element | Research Evidence Required | Validation Question |
|-------------|--------------------------|-------------------|
| Entry point choice | Research shows how users approach this task naturally | Does the entry point match where users are when the need arises? |
| Step sequence | Task analysis or contextual inquiry | Does the sequence match the natural order users perform these tasks? |
| Label choices | Interview transcripts, vocabulary analysis | Are labels drawn from participant language, not product terminology? |
| Exit and escape paths | Abandonment patterns from analytics | Are exit paths placed where users expect to be able to stop? |
| Error states | Session recordings, support ticket themes | Do error messages address the specific failures users experience? |
| Success state | User goal statements from JTBD | Does the confirmation communicate the outcome the user cares about? |

## Flow Fidelity Levels and Research Requirements

| Flow Fidelity | Research Input Needed | When to Use |
|--------------|----------------------|------------|
| Rough flow (boxes and arrows) | JTBD job stages; basic task structure | Early exploration; before user research complete |
| Validated flow | Interview findings + task analysis | After discovery research; before wireframing |
| Annotated flow with research callouts | Full research synthesis | For design handoffs that justify each step |

## Decision Point Design Based on Research

When designing branch points in a flow, ground each branch in evidence:

| Decision Type | Research Question to Answer | Evidence Source |
|-------------|---------------------------|----------------|
| Role-based branch | Do different user types need different paths? | Interviews with multiple segments |
| State-based branch | What preconditions change the flow? | Contextual inquiry; analytics |
| Permission-based branch | What does the user have access to? | User data analysis; interviews |
| Error branch | What are the realistic failure modes? | Support ticket analysis; session recordings |
| Optional step branch | Which steps can be skipped without impeding the job? | Task completion analysis; JTBD map |

## Annotation Standards for Research-Informed Flows

Document the research evidence behind each major flow decision:

| Annotation Type | Format |
|----------------|--------|
| Research citation | "[RES] 8/12 participants started from the dashboard — not notifications" |
| Language note | "[LANG] Participants used 'team' not 'workspace' — label updated" |
| Sequence rationale | "[SEQ] Address captured before payment — matches offline purchase mental model (interview P03, P07)" |
| Open question | "[?] No research on whether users expect progress to save mid-flow" |

## Common Flow Design Anti-Patterns (and Research Fixes)

| Anti-Pattern | Problem | Research-Informed Fix |
|-------------|---------|----------------------|
| Flow assumes user starts from home screen | Users arrive from email, notifications, or external links | Research entry points; design for all realistic starting contexts |
| Steps ordered by system logic, not user logic | Forces users to prepare information in unnatural sequence | Map to natural task cadence from contextual inquiry |
| Progress not preserved on back navigation | Users use back to reconsider; losing data causes abandonment | Session data shows back as a reconsideration signal, not cancellation |
| Error states use technical system language | Users cannot understand what happened or what to do | Use support ticket language — the words users use to describe the problem |
| Confirmation copy focuses on system outcome | "Request submitted" tells user the system acted, not whether their goal was met | State the user outcome: "Your project is now live" not "Record updated" |
