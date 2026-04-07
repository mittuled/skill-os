# Framework: milestone-definer-eng

Guides the definition of engineering milestones with binary success criteria tied to verifiable outcomes rather than activities.

## Milestone Definition Standard

Every milestone must contain:

| Field | Required | Format |
|-------|----------|--------|
| ID | Yes | M-001, M-002, etc. |
| Name | Yes | Outcome-based noun phrase (e.g., "API Integration Complete") |
| Target Date | Yes | YYYY-MM-DD |
| Success Criteria | Yes | Binary (met/not met) verifiable conditions; minimum 2 |
| Responsible Team | Yes | Team name or individual |
| Dependencies | Yes | List of prerequisite milestones or "none" |
| Verification Method | Yes | How success criteria will be demonstrated (test results, demo, metrics) |

## Milestone Categories

| Category | When to Use | Examples |
|----------|-------------|----------|
| Technical | Architecture or infrastructure readiness | "Database schema deployed to staging", "API contract signed off" |
| Integration | Components working together | "Frontend consumes backend API end-to-end", "Third-party webhook processing verified" |
| Quality | Testing and reliability thresholds | "E2E test suite covers all critical paths", "Load test passes at 2x projected traffic" |
| Operational | Production readiness | "Monitoring dashboards deployed", "Runbook reviewed by on-call team" |
| Delivery | User-facing outcomes | "Feature available to beta users", "GA rollout to 100% complete" |

## Success Criteria Rules

1. **Binary**: Each criterion is met or not met. No "partially met."
2. **Observable**: Verifiable by anyone with access, not dependent on one person's judgment.
3. **Time-bound**: Can be assessed at the milestone date; doesn't require waiting for future data.
4. **Outcome-based**: "API returns correct results for all 47 test scenarios" not "API code complete."

## Milestone Spacing Guidelines

| Delivery Duration | Recommended Milestone Count | Spacing |
|-------------------|---------------------------|---------|
| 1-2 sprints | 2 (mid-point + completion) | Weekly |
| 3-4 sprints | 3-4 | Every 1-2 sprints |
| 5-8 sprints | 4-6 | Every 1-2 sprints |
| 8+ sprints | 6-8 maximum | Every 2 sprints |

## Common Pitfalls

| Pitfall | Better Alternative |
|---------|-------------------|
| "Code complete" | "All acceptance criteria pass in CI" |
| "Design done" | "Architecture ADR approved by tech lead and VP" |
| "Testing complete" | "Zero P0/P1 bugs; regression suite green; load test at 2x passes" |
| "Ready for launch" | "Go-live checklist items all verified; rollback tested" |
