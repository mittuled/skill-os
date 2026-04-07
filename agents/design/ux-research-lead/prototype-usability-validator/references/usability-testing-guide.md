# Usability Testing Guide

## Purpose

Standards and protocols for running prototype usability tests to validate design decisions before development handoff.

## Study Design Decision Table

| Objective | Method | Sessions | Format |
|-----------|--------|---------|--------|
| Validate task completion on a flow | Moderated think-aloud | 5-8 | Remote video / In-person |
| Compare two design alternatives | A/B task test (within-subjects) | 8-12 | Remote |
| Measure findability of a feature | First-click test | 20-50 | Unmoderated |
| Validate information architecture | Tree test | 30-50 | Unmoderated |
| Measure overall usability | System Usability Scale (SUS) + task test | 8-12 | Remote |

## Nielsen's Heuristics: Test Coverage Checklist

Use these as lenses when reviewing session recordings to identify usability issues:

| # | Heuristic | Description | Common Test Observation |
|---|-----------|-------------|------------------------|
| 1 | Visibility of system status | System should always keep users informed | Users unsure if an action completed; missing loading indicators |
| 2 | Match between system and real world | Use user language, not system language | Jargon in labels; unfamiliar icons |
| 3 | User control and freedom | Easy undo and escape | Users cannot back out of multi-step flows |
| 4 | Consistency and standards | Follow platform conventions | Non-standard navigation; inconsistent button behaviour |
| 5 | Error prevention | Design to prevent errors | Destructive actions without confirmation; ambiguous form validation |
| 6 | Recognition over recall | Minimise what users must remember | Key info not visible; users forget earlier selections |
| 7 | Flexibility and efficiency | Shortcuts for expert users | No keyboard shortcuts; no saved preferences |
| 8 | Aesthetic and minimalist design | No irrelevant information | Cluttered screens; too much information visible at once |
| 9 | Help users recognise, diagnose, recover from errors | Clear error messages | Generic error text; no recovery path |
| 10 | Help and documentation | Support available when needed | No contextual help; help docs not linked from UI |

## Session Protocol

### Pre-Session
- [ ] Prototype accessible and tested on researcher's device
- [ ] Recording software running (with participant consent)
- [ ] Task script printed or on second screen
- [ ] Timer ready
- [ ] Note-taking template open

### Session Opening (5 min)
1. Welcome participant; explain session purpose
2. Confirm recording consent
3. Explain think-aloud protocol: "Talk through what you're thinking as you do each task — there are no wrong answers. We're testing the design, not you."
4. Confirm participant's background matches screener

### Task Delivery Protocol
- Present one task at a time — never show multiple tasks simultaneously
- Read tasks verbatim — do not add context or hints
- Note exact start time per task
- Record:
  - Task start time
  - Task completion time (or abandonment time)
  - Whether task was completed successfully
  - Verbal commentary during task
  - Hesitations and errors observed

### Probing Questions (use sparingly — do not lead)
- "What are you thinking right now?"
- "What would you expect to happen next?"
- "If you were at home doing this, what would you do?"
- Do NOT ask: "Did you see the button?" / "Was that confusing?"

### Post-Task Questions
- "How easy or difficult did you find that task?" (1-7 scale)
- "Was anything surprising about that?"
- "Is there anything you would have wanted to do that you couldn't?"

## Severity Rating Scale (Nielsen)

Rate each usability issue found:

| Severity | Definition | Recommendation |
|----------|------------|---------------|
| 0 | Not a usability problem | Document; no action |
| 1 | Cosmetic — only if extra time available | Note; low priority |
| 2 | Minor usability problem — low priority fix | Fix before next major release |
| 3 | Major usability problem — important to fix | Fix before release |
| 4 | Usability catastrophe — imperative to fix | Block release; fix now |

## Task Success Criteria

Define success before testing:

| Definition | Use When |
|------------|---------|
| Binary (completed / not completed) | Clear end state — e.g. "Order placed successfully" |
| Partial success levels | Multi-step task where partial completion has value |
| Self-reported + observed | Task where user perception matters as much as completion |

## System Usability Scale (SUS)

After all tasks, administer the 10-item SUS survey for a standardised usability score.

| Score Range | Grade | Interpretation |
|-------------|-------|----------------|
| 90-100 | A+ | Excellent |
| 80-89 | A/B | Good |
| 70-79 | C | Acceptable |
| 60-69 | D | Poor |
| < 60 | F | Unacceptable — redesign required |

SUS benchmark: B2B SaaS industry average is ~72. Consumer apps ~77.

## Findings Classification

Categorise each finding:

| Type | Description | Example |
|------|-------------|---------|
| Task failure | User cannot complete the task | Cannot find checkout button |
| Task difficulty | User completes but with significant effort or errors | Finds button after 40-second search |
| User error | User performs wrong action, then self-corrects | Taps "Cancel" instead of "Back" |
| Design concern | Issue observed but task still completed easily | Misses secondary information that may matter in real use |
| Positive finding | Something that worked unusually well | Delight at confirmation animation |
