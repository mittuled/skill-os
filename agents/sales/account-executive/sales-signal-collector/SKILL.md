---
name: sales-signal-collector
description: >
  This skill collects and documents signals from sales conversations including
  objections, competitors mentioned, and buying triggers. Use when asked to
  capture field intelligence, log deal signals, or document prospect feedback.
  Also consider after any substantive prospect interaction.
  Suggest when deal notes lack structured signal data.
department: sales
agent: account-executive
version: 1.0.0
complexity: simple
related-skills:
  - ../sales-signal-synthesizer/SKILL.md
  - ../../../sales/sales-manager/objection-handler-updater-sales/SKILL.md
  - ../../../sales/sales-development-rep/follow-up-sequence-builder/SKILL.md
  - ../expansion-motion-sales/SKILL.md
  - ../../sales-development-rep/cohort-selector-sales/SKILL.md
  - ../../sales-development-rep/cold-outreach-builder/SKILL.md
  - ../../sales-development-rep/decision-maker-mapper/SKILL.md
triggers:
  - "log signals from this call"
  - "capture deal intelligence"
  - "document prospect objections"
  - "what did we learn from this conversation"
---

# sales-signal-collector

## Agent: Account Executive

L3 account executive (Nx) responsible for sales signal synthesis, signal collection, and expansion sales motions.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)

## Skill Description

Collects and documents structured signals from sales conversations including objections, competitors mentioned, buying triggers, and decision-process details.

## When to Use

- When a discovery call, demo, or negotiation surfaces new information about the prospect's buying process, objections, or competitive landscape.
- When a deal advances or stalls and the reasons need to be captured for pipeline review.
- When multiple conversations across deals reveal a pattern that Product, Marketing, or Sales leadership should know about.

## Workflow

1. **Signal Capture**: Within 24 hours of a prospect interaction, log structured signals in the CRM: objections raised, competitors mentioned, buying triggers identified, decision-maker names, timeline commitments, and budget indicators. Tag each signal by type (objection, competitor, trigger, blocker). Deliverable: structured signal entries in CRM with tags.
2. **Context Annotation**: Add context to each signal: what prompted it, how the prospect framed it, and what it implies for deal progression. Link signals to the relevant MEDDIC criteria (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion). Deliverable: annotated signal log with MEDDIC mapping.
3. **Pattern Flagging**: When a signal appears across 3+ deals within a quarter, flag it as a pattern and escalate to the Sales Manager with deal references. Deliverable: pattern flag with supporting deal evidence.

## Anti-Patterns

- **Delayed capture**: Logging signals days after the conversation when details have faded. *Why*: delayed capture loses nuance and context; the difference between "budget is tight" and "budget is allocated to a competing initiative until Q3" determines the right next step.
- **Unstructured notes**: Dumping free-text notes without categorization or tagging. *Why*: unstructured notes cannot be aggregated or searched, making pattern detection across deals impossible.

## Output

**On success**: Produces structured, tagged signal entries in the CRM with MEDDIC mapping and context annotations. Pattern flags escalated to Sales Manager when thresholds are met.

**On failure**: Report which signals could not be captured (e.g., recording failed, conversation was off-the-record), what partial information is available, and recommended follow-up to fill gaps.

## Related Skills

- [`sales-signal-synthesizer`](../sales-signal-synthesizer/SKILL.md) -- Synthesizes collected signals into actionable insights for Product and Marketing.
- [`objection-handler-updater-sales`](../../../sales/sales-manager/objection-handler-updater-sales/SKILL.md) -- Consumes objection signals to update the objection handler.
