---
name: sales-signal-collector-am
description: >
  This skill collects and documents signals from account conversations including expansion signals,
  risks, and competitive threats. Use when asked to log account intelligence, document customer
  feedback, or track competitive mentions. Also consider after any substantive customer interaction.
  Suggest when account signal data in the CRM is sparse or outdated.
department: account-management
agent: account-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# sales-signal-collector-am

## Agent: Account Manager

L2 account manager (Nx, multi-instance) responsible for collecting account signals and executing expansion motions.

Department ethos: [ideal-account-management.md](../../../departments/account-management/ideal-account-management.md)

## Skill Description

The sales signal collector captures, classifies, and documents signals from account conversations -- including expansion intent, churn risk, competitive threats, and product feedback -- so portfolio-level intelligence can be synthesised.

## When to Use

- After any substantive customer interaction (QBR, check-in, support escalation, renewal discussion).
- When a customer mentions a competitor, budget change, or strategic shift.
- When product feedback or feature requests surface during account conversations.
- When the AM lead requests a signal collection sweep to update portfolio intelligence.

## Workflow

1. **Capture raw signals**: After each customer interaction, record key signals: what was said, the context, and the customer's tone and urgency. Deliverable: raw signal notes.
2. **Classify the signal**: Tag each signal by type (expansion opportunity, churn risk, competitive threat, product feedback, relationship health). Deliverable: classified signal entry.
3. **Assess confidence**: Rate the signal's reliability (confirmed, inferred, speculative) based on the source and context. Deliverable: confidence-rated signal.
4. **Log in the CRM**: Enter the classified, confidence-rated signal into the CRM with the account, date, and source interaction. Deliverable: CRM signal entry.

## Anti-Patterns

- **Logging signals in personal notes**: Capturing signals in notebooks or personal documents instead of the CRM. *Why*: signals trapped in personal notes are invisible to the synthesiser and lost when the AM changes roles.
- **Binary signal recording**: Logging only strong positive or negative signals and ignoring ambiguous ones. *Why*: subtle signals often precede major account shifts; capturing them enables early pattern detection at the portfolio level.

## Output

**On success**: Classified, confidence-rated signal entries in the CRM for every substantive customer interaction, available for portfolio-level synthesis.

**On failure**: Report which interactions were not logged (e.g., informal conversations, high meeting volume), what was captured, and recommend process changes to improve signal coverage.

## Related Skills

- [`sales-signal-synthesizer-am`](../../account-management-lead/sales-signal-synthesizer-am/SKILL.md) -- the synthesiser aggregates the signals this skill collects into portfolio insights.
- [`expansion-motion-am`](../expansion-motion-am/SKILL.md) -- expansion signals collected here may trigger an expansion motion.
