# Scenario: Checkout Flow Accessibility Check Before Dev Handoff

The team has completed the visual design for a redesigned checkout flow covering 6 screens: cart summary, address entry, payment entry, order review, confirmation, and error states. The head of design is conducting the pre-handoff accessibility check before the Figma file is marked dev-ready.

## Input Parameters

```json
{
  "artifact_name": "Checkout Flow v2 — Figma file rev 14",
  "criteria": {
    "contrast_normal_text": "pass",
    "contrast_large_text": "pass",
    "touch_target_size": "pass",
    "color_not_sole_indicator": "fail",
    "focus_states_documented": "fail",
    "focus_order_logical": "pass",
    "alt_text_specified": "pass",
    "aria_labels_documented": "fail",
    "error_messages_descriptive": "pass"
  },
  "notes": {
    "color_not_sole_indicator": "Error states on form fields use only red border — no icon or text label added to indicate error.",
    "focus_states_documented": "Focus rings are missing on the primary CTA buttons across all 6 screens.",
    "aria_labels_documented": "Credit card icon in payment field and lock icon in security badge have no ARIA labels in the spec."
  }
}
```
