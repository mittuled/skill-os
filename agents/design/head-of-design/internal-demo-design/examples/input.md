# Scenario: Internal Demo for Onboarding Redesign — Concept Direction

The design team has completed two weeks of exploration on a redesigned onboarding flow. Leadership has not seen the work since the project kick-off. The Head of Design is running an internal demo to get directional alignment and surface concerns before moving to detailed design.

## Input Parameters

```json
{
  "demo_title": "Onboarding Redesign — Concept Direction Demo",
  "objectives": [
    "Get directional buy-in on the stepped vs. conversational onboarding approach",
    "Surface engineering feasibility concerns before committing to detailed design",
    "Identify open questions about first-time user data collection requirements"
  ],
  "audience": ["CEO", "CPO", "CTO", "Head of Customer Success"],
  "design_artifacts": [
    "Figma prototype — Concept A (stepped onboarding)",
    "Figma prototype — Concept B (conversational onboarding)",
    "User research synthesis doc (5 usability test sessions)"
  ],
  "open_questions": [
    "Should the onboarding flow collect company size and role upfront or defer to in-product prompts?",
    "Is the conversational format feasible within the current front-end framework?",
    "What is the minimum viable onboarding for the enterprise self-serve tier?"
  ],
  "feedback_notes": [
    {
      "category": "Usability concerns",
      "comment": "Stepped approach felt too long in user tests — 7 steps is too many",
      "action_item": "Reduce stepped flow to 4 steps maximum",
      "owner": "Visual Interaction Designer"
    },
    {
      "category": "Engineering feasibility flags",
      "comment": "Conversational format requires new chat-style component not in the design system",
      "action_item": "Engineering to assess effort for conversational component",
      "owner": "Engineering Lead"
    },
    {
      "category": "Positive validation",
      "comment": "Both concepts successfully surface the core value prop within the first 2 screens",
      "action_item": null,
      "owner": null
    }
  ]
}
```
