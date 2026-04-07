# Cross-Platform Design Test Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Feature | [Feature or surface tested] |
| Design Version | [Figma file version or link] |
| Version | [1.0] |
| Status | [Draft / Review / Sign-off Ready] |

## Test Scope

[Define which platforms, devices, and breakpoints were tested.]

| Platform | Device / Viewport | OS Version | Browser / App | Included |
|----------|-------------------|-----------|---------------|----------|
| Web — Desktop | 1440px width | – | Chrome latest | [✓ / ✗] |
| Web — Desktop | 1280px width | – | Chrome latest | [✓ / ✗] |
| Web — Tablet | 768px width | – | Safari | [✓ / ✗] |
| Web — Mobile | 375px width | – | Safari iOS | [✓ / ✗] |
| Web — Mobile | 360px width | – | Chrome Android | [✓ / ✗] |
| iOS Native | iPhone 14 Pro | iOS 17 | Native app | [✓ / ✗] |
| iOS Native | iPad Pro 12.9" | iOS 17 | Native app | [✓ / ✗] |
| Android Native | Pixel 7 | Android 14 | Native app | [✓ / ✗] |

## Summary

**Overall result**: [PASS / PASS WITH ISSUES / FAIL]

[1-2 sentences summarising the test outcome. GUIDANCE: State the number of issues found by severity. e.g. "The checkout flow renders correctly on 6 of 8 tested surfaces. 2 critical layout issues found on Android 360px and iPad landscape orientation."]

## Findings by Screen

[Document findings per screen for each platform. One table per screen.]

### Screen: [Screen Name]

| Platform | Result | Issue Description | Severity | Screenshot Ref |
|----------|--------|-------------------|----------|----------------|
| Web 1440px | [Pass] | – | – | – |
| Web 1280px | [Pass] | – | – | – |
| Web 375px | [Fail] | [e.g. CTA button overlaps with bottom navigation bar on scroll] | [Critical] | [IMG-01] |
| iOS Native | [Pass] | – | – | – |
| Android 360px | [Fail] | [e.g. Input field text truncated at 360px — label wraps incorrectly] | [Major] | [IMG-02] |

### Screen: [Screen Name]

| Platform | Result | Issue Description | Severity | Screenshot Ref |
|----------|--------|-------------------|----------|----------------|
| [Platform] | [Result] | [Description] | [Severity] | [Ref] |

## Issue Register

[All issues consolidated across screens, prioritised by severity.]

| ID | Screen | Platform | Issue Description | Severity | Designer Action | Owner | Target Fix |
|----|--------|----------|-------------------|----------|----------------|-------|-----------|
| P-01 | [Screen] | [Android 360px] | [e.g. CTA hidden behind system navigation bar] | Critical | [Redesign bottom spacing to account for nav bar height] | [Designer] | [Sprint X] |
| P-02 | [Screen] | [iPad landscape] | [e.g. Two-column layout breaks at landscape orientation] | Major | [Add landscape grid variant or lock to portrait] | [Designer] | [Sprint X] |
| P-03 | [Screen] | [Web 375px] | [e.g. Touch target for stepper button is 28px — below 44px minimum] | Major | [Increase tap area to 44×44px minimum] | [Designer] | [Sprint X] |

**Severity scale**:
- **Critical**: Renders the flow unusable on that platform — blocks ship
- **Major**: Significant usability degradation — must fix before ship
- **Minor**: Cosmetic or low-impact inconsistency — fix in next iteration
- **Note**: Observation with no user impact

## Platform-Specific Adaptation Checklist

[Verify platform conventions are respected for each surface type.]

### iOS (Native)
- [ ] Navigation uses native iOS patterns (back swipe, navigation bar title)
- [ ] Tab bar follows iOS HIG 5-tab maximum
- [ ] Safe area insets respected (top notch, bottom home indicator)
- [ ] Touch targets minimum 44×44pt
- [ ] Text uses Dynamic Type scaling

### Android (Native)
- [ ] Navigation follows Material Design guidelines (back button, bottom nav)
- [ ] Status bar and navigation bar heights accounted for in layout
- [ ] Touch targets minimum 48×48dp
- [ ] Supports both light and dark system theme

### Web (Responsive)
- [ ] Breakpoints defined at 375px, 768px, 1280px, 1440px minimum
- [ ] No horizontal scroll on any breakpoint
- [ ] Focus states visible (keyboard navigation)
- [ ] Images and media scale with viewport

## Sign-Off

| Role | Name | Decision | Date |
|------|------|----------|------|
| UX/UI Designer | | [Approved / Revise] | |
| Head of Design | | [Approved / Revise] | |
| Engineering Lead | | [Confirmed buildable] | |
