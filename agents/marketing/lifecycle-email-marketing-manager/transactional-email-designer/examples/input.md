# Scenario: Transactional Email Library for SaaS Collaboration Tool

Design the transactional email template library for a SaaS collaboration tool that currently sends plain-text transactional emails with no brand consistency.

## Context

- **Product**: CollabSpace — team collaboration platform with messaging, files, and projects
- **Monthly active users**: 15,000 across 400 workspaces
- **Current state**: All transactional emails are plain-text sent from noreply@collabspace.com using the same domain as marketing emails
- **Problem**: Marketing spam complaints have caused transactional emails (password resets, invites) to land in spam for 8% of users

## Transactional Email Types Needed

1. Email verification (new signup)
2. Password reset
3. Team invitation
4. Comment mention notification
5. File shared notification
6. Subscription confirmation
7. Payment receipt
8. Payment failure alert
9. Plan upgrade/downgrade confirmation
10. Workspace data export ready
