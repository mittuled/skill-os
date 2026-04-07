# Cross-Platform Design Test Matrix

A reference for planning and executing design verification across platforms, devices, and input methods.

---

## Platform Coverage Tiers

### Tier 1 — Must Test (every release)

| Platform | Viewport / Spec | OS Version | Input Methods |
|----------|----------------|-----------|--------------|
| Web / Mobile | 375×812 (iPhone 14 base) | Latest Safari iOS | Touch, keyboard |
| Web / Tablet | 768×1024 (iPad) | iPadOS latest | Touch, keyboard, mouse (split view) |
| Web / Desktop | 1280×800 | macOS + Windows, Chrome latest | Mouse, keyboard |
| Android Mobile | 360×800 (common Android baseline) | Android 12+ | Touch, keyboard |

### Tier 2 — Should Test (major feature releases)

| Platform | Viewport / Spec | Notes |
|----------|----------------|-------|
| Web / Large Desktop | 1440×900 | Check for content max-width and layout scaling |
| iOS Native | iPhone SE (375px, small form factor) | Content prioritization on smallest viewport |
| Android Large | 412×915 (Pixel 7 Pro) | Large-screen Android layout |
| Foldable / Tablet Android | 600×960 expanded | Responsive adaptation for foldable devices |

### Tier 3 — Edge Case (when feature is relevant)

| Platform | When to Include |
|----------|----------------|
| High-contrast mode (Windows) | When feature includes custom colour or icon work |
| iOS large text / Dynamic Type | When feature includes text-heavy layouts |
| Reduced motion | When feature includes animations or transitions |
| Dark mode | When design includes dark mode support |

---

## Visual Check Dimensions

For each screen at each breakpoint:

| Dimension | What to Verify |
|-----------|---------------|
| Layout reflow | Does content restack correctly at this width? No horizontal overflow? |
| Typography scaling | Is text legible? Line lengths within 45–75 characters? |
| Touch targets | ≥ 44pt (iOS), ≥ 48dp (Android), ≥ 44px (Web) for all interactive elements |
| Image / media cropping | Are images cropped correctly at this breakpoint? |
| Spacing token application | Spacing values consistent with design system for this density? |
| Content truncation | Is truncation happening at intended points? Ellipsis or wrapping as designed? |
| Sticky / fixed elements | Do sticky headers, bottom bars, FABs behave correctly across scroll positions? |

---

## Interaction Parity Checklist by Platform

| Interaction | Web Desktop | Web Mobile | iOS | Android |
|-------------|------------|-----------|-----|---------|
| Primary navigation | Sidebar / top nav | Bottom tab / hamburger | Tab bar | Bottom nav |
| Modals | Centre overlay | Full-screen sheet | Bottom sheet or full screen | Bottom sheet |
| Drawers | Side panel slide | Full-screen slide | Side panel | Side panel |
| Pull to refresh | N/A | Yes (if list is scrollable) | Yes | Yes |
| Long press / right click | Right click context menu | Long press menu | Long press menu | Long press menu |
| Hover states | Required | N/A | N/A | N/A |
| Focus indicators | Required (keyboard) | Required (keyboard/switch) | Required (keyboard) | Required (keyboard) |
| Back navigation | Browser back button | Swipe back / browser back | Swipe back / back button | Android back gesture / button |

---

## Accessibility Modes by Platform

| Mode | Platform | What to Test |
|------|----------|-------------|
| VoiceOver | iOS / macOS | Screen reader navigation, ARIA labels, focus order |
| TalkBack | Android | Screen reader navigation, content descriptions |
| NVDA / JAWS | Windows Web | Screen reader navigation for web |
| High contrast | Windows | Colour contrast with high contrast themes |
| Large text / Dynamic Type | iOS | Layout at XXXL text size |
| Reduced motion | iOS / Web | Animations disabled; functional fallbacks present |
| Zoom (200%) | Web | Content accessible at 200% browser zoom |

---

## Deviation Severity Scale

| Severity | Definition | Required Action |
|---------|-----------|----------------|
| Critical | Feature is unusable on this platform/device | Block release; fix before ship |
| Major | Significant visual or interaction issue; degrades experience meaningfully | Fix in current release if possible; otherwise file for next cycle |
| Minor | Noticeable visual inconsistency; does not block task completion | File as improvement ticket; address in next iteration |
| Intentional Adaptation | Deliberate platform-specific variation (e.g., iOS sheet vs. web modal) | Document as accepted divergence; not a bug |

---

## Test Execution Log Format

```
Screen:              [Screen name]
Platform:            [Platform + device spec]
Breakpoint:          [Viewport dimensions]
Tester:              [Name]
Date:                [YYYY-MM-DD]
Figma Reference:     [Link]
Staging URL:         [Link]
---
Visual Check:        PASS / FAIL — [Notes]
Interaction Check:   PASS / FAIL — [Notes]
Accessibility Mode:  PASS / FAIL / N/A — [Notes]
Deviations Found:    [List with severity]
```
