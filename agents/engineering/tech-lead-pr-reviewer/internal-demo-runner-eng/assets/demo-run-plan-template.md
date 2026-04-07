# Internal Demo Run Plan: [Feature / Sprint Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD HH:MM] |
| Host | Tech Lead / PR Reviewer |
| Feature | [Feature or sprint deliverable] |
| Audience | [Engineering / Cross-functional / Stakeholder] |
| Environment | [Staging / Demo environment] |
| Skill | internal-demo-runner-eng |
| Duration | [30 / 45 / 60 min] |

## Demo Objectives

1. [Show working software meeting acceptance criteria for [feature]]
2. [Surface any integration issues before formal QA]
3. [Collect feedback from stakeholders on UX and edge cases]

## Demo Script

| # | Step | Who | Expected Outcome | Fallback |
|---|------|-----|-----------------|---------|
| 1 | [Navigate to [URL] and log in as [test user]] | [Host] | [Dashboard loads, user profile visible] | [Use recorded video if env down] |
| 2 | [Demonstrate [primary user flow]] | [Host] | [Flow completes; confirmation shown] | |
| 3 | [Demonstrate [error / edge case]] | [Host] | [Error handled gracefully; message shown] | |
| 4 | [Q&A and feedback] | [All] | [Issues captured in demo notes] | |

## Pre-Demo Checklist

- [ ] Staging environment stable and up
- [ ] Demo data seeded (test accounts, products, orders)
- [ ] Screen sharing tested
- [ ] Recording enabled (if applicable)
- [ ] Feature flags enabled for demo user
- [ ] Relevant stakeholders invited and confirmed

## Known Limitations for This Demo

[Be transparent about what is incomplete to set correct expectations:]

1. [Feature X is not yet integrated — placeholder UI shown]
2. [Performance under load not yet validated]

## Feedback Capture

| Feedback | Type | Severity | Owner | Ticket |
|---------|------|---------|-------|--------|
| [Feedback from demo] | [UX / Bug / Feature request] | [High/Med/Low] | [Role] | [Link] |

## Post-Demo Actions

| Action | Owner | Due |
|--------|-------|-----|
| [Create tickets for all High/Med feedback items] | Tech Lead | [Next day] |
| [Share demo recording with absent stakeholders] | Host | [Same day] |
