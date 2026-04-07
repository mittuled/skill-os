# Scenario: Design Effort Estimate for Team Collaboration Feature

The product manager has requested a design effort estimate for a new team collaboration feature that allows multiple workspace members to comment on, approve, and share assets within the product. The sprint planning cycle starts in 5 days and the PM needs design capacity commitment before finalizing scope.

## Input Parameters

```json
{
  "feature_name": "Team Collaboration — Comments, Approvals, and Sharing",
  "context": "New collaboration layer on top of the existing workspace. No existing comment or approval patterns in the design system.",
  "deliverables": [
    {"type": "user_flows", "complexity": "medium", "notes": "Comment thread flow, approval workflow, share dialog"},
    {"type": "wireframes", "complexity": "high", "notes": "15+ screens including responsive breakpoints at 3 widths"},
    {"type": "visual_design", "complexity": "high", "notes": "New components needed: comment bubble, approval badge, share modal"},
    {"type": "prototype", "complexity": "medium", "notes": "Interactive prototype for usability testing"},
    {"type": "design_system_update", "complexity": "high", "notes": "Add comment, approval, and sharing component families"},
    {"type": "handoff_spec", "complexity": "medium", "notes": "Full Figma spec with annotations"}
  ],
  "assumptions": [
    "Product spec is finalized before design begins",
    "Usability testing budget is approved for 5 participants",
    "Design system component library is current and accessible"
  ],
  "risks": [
    "Novel patterns with no design system precedent may require additional exploration rounds",
    "Responsive requirements across 3 breakpoints add 30% to wireframe scope",
    "Approval workflow may change based on engineering feasibility review"
  ]
}
```
