# Framework: CS Onboarding Playbook (Product Perspective)

## Core Model

The customer success onboarding playbook defines the sequence of milestones a new customer must reach to achieve their first value moment, and maps product-side responsibilities against CS-side responsibilities for each step.

## Activation Milestone Map

| Milestone | Definition | Owner | Target Time |
|-----------|-----------|-------|-------------|
| Account created | User signs up and verifies email | Product | Day 0 |
| Onboarding started | User completes step 1 of onboarding flow | Product | Day 0–1 |
| Setup complete | User has configured the minimum viable setup | Product + CS | Day 1–3 |
| First value moment | User achieves the outcome that justified buying | Product + CS | Day 3–7 |
| Habit established | User returns and completes the core workflow independently | Product | Day 14–30 |

## Time-to-Value (TTV) Framework

- **TTV definition**: The elapsed time from account creation to first value moment
- **TTV target**: Set per segment (e.g., SMB: <7 days; Enterprise: <21 days)
- **TTV bottlenecks**: Identify the step with the highest drop-off rate — that is the highest-priority fix
- **TTV measurement**: Track at the cohort level, segment by plan tier and onboarding path

## Friction Audit Categories

| Friction Type | Definition | Product Signal |
|---|---|---|
| Setup friction | Too many steps before first use | High step-abandonment rate |
| Comprehension friction | User does not understand what to do next | Support tickets asking "how do I..." |
| Permission friction | User lacks rights to complete a required action | Error screens during onboarding |
| Integration friction | User must connect external tool before proceeding | Drop-off at integration step |
| Motivation friction | User does not see why they should complete the step | Low completion despite no errors |

## Playbook Update Triggers

Update the playbook when:
1. A new feature changes the first-run experience or setup flow
2. Onboarding completion rate drops >10% vs prior 30-day average
3. TTV for any segment increases >20% vs baseline
4. CS team reports repeated confusion at a specific step
5. A product redesign alters navigation or terminology in the onboarding path

## Product vs CS Responsibility Boundary

| Responsibility | Product | CS |
|---|---|---|
| In-product onboarding flow design | Yes | Advisory |
| Checklist / tooltip copy | Yes | Reviewer |
| Live onboarding calls | No | Yes |
| Follow-up sequence (email/chat) | Advisory | Yes |
| Escalation handling | No | Yes (escalate bugs to Product) |
| Playbook maintenance | Review changes | Owns document |
