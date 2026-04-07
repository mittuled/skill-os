# Iteration Design Brief

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Visual Interaction Designer] |
| Feature / Surface | [Shipped feature being iterated] |
| Data Sources | [Session recordings / analytics / usability findings] |
| Figma Link | [Link to iteration design file] |
| Version | [1.0] |
| Status | [In Design / Review / Approved for Development] |

## Problem Statement

[State what post-launch evidence triggered this iteration. Be specific about the signal and its magnitude. GUIDANCE: e.g. "Session analysis of 15 post-launch sessions shows 7/15 users abandon the onboarding profile setup step. Heatmap shows 62% of users scroll past the profile photo upload without engaging. Root cause hypothesis: upload CTA is below the fold on mobile at 375px."]

**Evidence source(s)**: [List data sources and dates reviewed]
**Metric impact**: [e.g. "Profile completion rate: 34% — target is 65%"]
**Affected user segment**: [e.g. New users on mobile iOS]

## Current State Description

[Describe the existing interaction design that is being changed.]

**Current screen / state**: [Screen name and state]
**Current interaction pattern**: [e.g. "Profile photo upload is a secondary CTA below the fold — users must scroll to see it"]
**Figma link (current design)**: [Link to current production design]

## Proposed Change

[Describe the iteration. One change per brief — do not bundle multiple iterations.]

**Change type**: [Label / Copy / Layout / Visual hierarchy / New state / Interaction pattern / Animation]
**Change description**: [Specific, concrete description of what will change]
**Hypothesis**: [e.g. "Moving the profile photo upload to above the fold and making it the primary CTA on Step 3 will increase profile completion rate by at least 20 percentage points"]
**Minimum effective change**: [State why you chose this scope and did not change more]

## Before / After Comparison

| Dimension | Current (Before) | Proposed (After) |
|-----------|-----------------|-----------------|
| CTA position | [e.g. Below fold — requires scroll] | [e.g. Above fold — visible without scroll] |
| CTA label | [e.g. "Upload a photo (optional)"] | [e.g. "Add your profile photo"] |
| CTA weight | [e.g. Secondary button style] | [e.g. Primary button style] |
| Skip affordance | [e.g. No skip option visible] | [e.g. "Skip for now" text link below primary CTA] |

## States to Redesign

[List every state affected by this iteration.]

| State | Status | Notes |
|-------|--------|-------|
| Default (no photo uploaded) | [Needs redesign] | [Primary focus of this iteration] |
| Uploading (loading) | [Needs redesign] | [Progress indicator required] |
| Uploaded (success) | [Existing — no change] | – |
| Error (upload failed) | [Needs redesign] | [Error message TBD — confirm with Content Design] |
| Skip path | [Needs redesign] | [Add "Skip for now" affordance] |

## Platforms Affected

- [ ] Web (desktop)
- [ ] Web (mobile 375px)
- [ ] iOS native
- [ ] Android native

## Validation Plan

[State how you will know whether the iteration worked.]

**Success metric**: [e.g. "Profile completion rate increases from 34% to 50%+"]
**Measurement method**: [e.g. Analytics event: profile_photo_uploaded within onboarding session]
**Measurement window**: [e.g. 2 weeks post-launch, minimum 200 new user sessions]
**Rollback criteria**: [e.g. If profile completion rate does not improve within 2 weeks, revert and re-investigate]

## Engineering Notes

[Any implementation notes relevant to the development team.]

- [e.g. No API changes required — change is purely visual/layout]
- [e.g. Profile photo upload endpoint remains unchanged]
- [e.g. "Skip for now" stores null for profile_photo_url — existing behaviour]

## Approvals

| Role | Name | Decision | Date |
|------|------|----------|------|
| Visual Interaction Designer | | [Approved] | |
| Head of Design | | [Approved] | |
| Product Manager | | [Approved] | |
