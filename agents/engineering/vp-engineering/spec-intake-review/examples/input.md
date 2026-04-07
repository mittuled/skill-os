# Scenario: Reviewing PRD for Export Feature

Product submitted a PRD for a data export feature. VP Engineering reviews it for engineering readiness.

## Input Parameters

```json
{
  "spec_name": "PRD-2026-051: Data Export Feature",
  "scores": {
    "user_stories_or_jtbd": 90,
    "acceptance_criteria": 75,
    "success_metrics": 60,
    "non_functional_requirements": 40,
    "scope_clarity": 80,
    "edge_cases": 50
  },
  "notes": {
    "non_functional_requirements": "No performance SLA specified for export of large datasets (100K+ records). No accessibility requirements for the UI.",
    "edge_cases": "Empty dataset export and concurrent export requests not addressed."
  },
  "open_questions": [
    "What is the maximum export file size supported?",
    "Should exports expire after N days or remain indefinitely?",
    "Is CSV the only format or do we also support XLSX/JSON?"
  ],
  "action_items": [
    "Add performance SLA: export of 100K records must complete in <30 seconds",
    "Document accessibility requirements for export button and download link",
    "Add edge case: empty export (0 records) should return empty file, not error",
    "Clarify file format requirements — CSV only or multi-format?"
  ]
}
```
