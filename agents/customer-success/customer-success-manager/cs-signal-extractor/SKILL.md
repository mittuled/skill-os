---
name: cs-signal-extractor
description: >
  This skill extracts product and market signals from customer success
  conversations and usage patterns. Use when asked to mine CS interactions for
  product insights, identify feature requests, or surface competitive
  intelligence. Also consider when product lacks customer signal input. Suggest
  when the user makes product decisions without systematic CS signal data.
department: customer-success
agent: customer-success-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# cs-signal-extractor

## Agent: Customer Success Manager

L3 customer success manager (Nx) responsible for signal extraction, feedback synthesis, early adopter success, and customer activation.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Extracts product and market signals from customer success conversations and usage patterns for input to product, marketing, and strategy teams.

## When to Use

- When CS conversations contain product feedback, feature requests, or competitive intelligence that should be routed to product.
- When usage pattern changes suggest emerging customer needs or shifting market dynamics.
- When product or marketing teams request structured signal data from CS interactions.

## Workflow

1. **Capture Raw Signals**: Record signals from CS interactions: feature requests, pain points, competitor mentions, use case evolution, and unmet needs. Tag each signal with customer, date, and context. Deliverable: tagged signal log.
2. **Classify Signals**: Categorize signals by type: product feedback, feature request, competitive intelligence, churn risk, and expansion opportunity. Deliverable: classified signal dataset.
3. **Assess Signal Strength**: Evaluate each signal's reliability -- single-customer anecdote vs. multi-customer pattern, strategic account vs. edge case. Deliverable: signal strength ratings.
4. **Route to Stakeholders**: Deliver classified signals to appropriate teams: product feedback to PM, competitive intelligence to strategy, churn signals to CS Manager. Deliverable: routed signal reports.

## Anti-Patterns

- **Unstructured signal capture**: Noting signals in free-text conversation logs without structured tagging. *Why*: untagged signals are unfindable and cannot be aggregated into patterns.
- **Filtering before capture**: Deciding which signals are "important enough" to record before capturing them. *Why*: weak individual signals may form strong patterns when aggregated; premature filtering loses data.
- **Signals without context**: Recording what the customer said without the surrounding context of why they said it. *Why*: a feature request without context cannot be properly prioritized or designed.

## Output

**On success**: Produces classified and strength-rated signal reports routed to product, marketing, and CS leadership. Delivered as structured signal data.

**On failure**: Report which interactions could not be processed (missing notes, unclear context), what signals were captured, and what process improvements would increase signal quality.

## Related Skills

- [`user-feedback-synthesiser-cs`](../user-feedback-synthesiser-cs/SKILL.md) -- Synthesizes individual signals into thematic insights.
- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- Signals contribute to health score calculations.
- [`expansion-motion-designer-cs`](../../../customer-success/head-of-customer-success/expansion-motion-designer-cs/SKILL.md) -- Expansion signals feed the expansion motion.
