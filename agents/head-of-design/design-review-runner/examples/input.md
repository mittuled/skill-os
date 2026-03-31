# Scenario: Pre-Handoff Design Review — Billing Settings Redesign

The visual interaction designer has completed the billing settings redesign and is requesting a pre-handoff review before the Figma file is marked dev-ready. The Head of Design is running the structured review session.

## Input Parameters

```json
{
  "deliverable_name": "Billing Settings Redesign — Figma file v3",
  "review_type": "pre_handoff",
  "criteria": {
    "design_system_compliance": "pass",
    "accessibility_compliance": "blocking",
    "interaction_completeness": "advisory",
    "content_quality": "pass",
    "product_alignment": "pass",
    "handoff_readiness": "advisory"
  },
  "notes": {
    "accessibility_compliance": "Payment method card does not meet 3:1 contrast requirement for the 'active' badge on dark backgrounds.",
    "interaction_completeness": "Downgrade confirmation dialog missing the 'cancel' state — only 'confirm downgrade' is documented.",
    "handoff_readiness": "Prototype is linked but annotations are missing on the invoice history table columns."
  },
  "feedback_items": [
    {
      "theme": "Visual consistency",
      "feedback": "Invoice table rows use a slightly different spacing token than the rest of the settings page — should align to space-4.",
      "severity": "advisory",
      "owner": "Visual Interaction Designer"
    }
  ]
}
```
