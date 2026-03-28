# Scoring Rubric: Accessibility Auditor Design

Evaluates WCAG conformance and assistive technology compatibility across perceivable, operable, understandable, and robust principles.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Perceivable | 25% | 0-10 | WCAG Perceivable principle: text alternatives, captions, contrast, content adaptability |
| Operable | 25% | 0-10 | WCAG Operable principle: keyboard access, timing, seizure safety, navigation |
| Understandable | 20% | 0-10 | WCAG Understandable principle: readability, predictability, input assistance |
| Robust | 15% | 0-10 | WCAG Robust principle: parsing, compatibility with assistive technologies |
| Assistive Technology Compatibility | 15% | 0-10 | Real-device testing with screen readers, magnifiers, switch access, and voice control |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | WCAG AAA conformance across all principles; verified with 4+ assistive technologies; zero critical or major issues | Ship and add to accessibility showcase; schedule annual re-audit |
| A | 8.0 – 8.9 | Strong | WCAG AA full conformance; tested with 2-3 assistive technologies; minor issues documented | Ship with minor fixes tracked; re-test after remediation |
| B | 7.0 – 7.9 | Good | WCAG AA mostly met but gaps in contrast, keyboard navigation, or AT compatibility | Fix identified AA failures before release; re-audit affected components |
| C | 5.0 – 6.9 | Adequate | Partial WCAG AA conformance; keyboard traps or missing alt text present; limited AT testing | Block release for accessibility remediation sprint |
| D | 3.0 – 4.9 | Weak | Widespread AA failures; primary flows unusable via keyboard or screen reader | Escalate to design and engineering leads; remediate before any user exposure |
| F | 0.0 – 2.9 | Failing | No meaningful accessibility; application is unusable for users with disabilities | Halt release; engage accessibility specialist for full remediation |

## Signal Tables

### Perceivable
| Score | Evidence |
|-------|----------|
| 9-10 | All images have meaningful alt text; video has captions and audio descriptions; contrast ratios meet AAA (7:1); content reflows at 400% zoom without loss |
| 7-8 | Alt text present on all images; contrast meets AA (4.5:1); content reflows at 200% zoom; minor gaps in multimedia alternatives |
| 5-6 | Most images have alt text but some are decorative without null alt; contrast meets AA for body text but fails on some UI elements; reflow issues at high zoom |
| 3-4 | Many images missing alt text; contrast failures on primary text; content does not reflow; no captions on video |
| 1-2 | Systematic missing alt text; widespread contrast failures; no multimedia alternatives; content unusable at increased zoom |

### Operable
| Score | Evidence |
|-------|----------|
| 9-10 | Full keyboard navigation with visible focus indicators; no keyboard traps; skip navigation present; all interactive elements reachable; touch targets 44x44px minimum |
| 7-8 | Keyboard navigation works for all primary flows; focus indicators visible; minor gaps in secondary interactions; touch targets mostly compliant |
| 5-6 | Keyboard navigation works for most flows but some interactive elements unreachable; focus indicators inconsistent; some touch targets too small |
| 3-4 | Keyboard traps present; focus order is illogical; many interactive elements keyboard-inaccessible; no skip navigation |
| 1-2 | Application is unusable via keyboard; no focus management; mouse-only interactions throughout |

### Understandable
| Score | Evidence |
|-------|----------|
| 9-10 | Language attributes set; form inputs have visible labels and error messages; navigation is consistent; no unexpected context changes; reading level appropriate |
| 7-8 | Language set; most forms have labels and errors; navigation mostly consistent; minor unexpected behaviours documented |
| 5-6 | Language partially set; some forms rely on placeholder-only labels; inconsistent navigation patterns; some context changes without warning |
| 3-4 | No language attribute; forms lack labels or error guidance; navigation patterns vary across pages; frequent unexpected behaviours |
| 1-2 | Content is disorganized; forms are unusable without visual cues; no error prevention or correction mechanisms |

### Robust
| Score | Evidence |
|-------|----------|
| 9-10 | Valid, well-structured HTML; ARIA used correctly and only when native HTML is insufficient; compatibility verified with current versions of major assistive technologies |
| 7-8 | HTML is well-structured; ARIA is mostly correct; minor parsing issues; compatible with most assistive technologies |
| 5-6 | HTML has some structural issues; ARIA misused in places (redundant or incorrect roles); compatibility untested on some platforms |
| 3-4 | Significant HTML parsing errors; ARIA used incorrectly creating confusion for assistive technologies; tested on one AT only |
| 1-2 | Invalid HTML; ARIA absent or systematically misused; no assistive technology testing performed |

### Assistive Technology Compatibility
| Score | Evidence |
|-------|----------|
| 9-10 | Tested with VoiceOver, NVDA, TalkBack, and at least one additional AT; all primary flows functional; announcement order logical; no AT-specific bugs |
| 7-8 | Tested with 2-3 screen readers; primary flows functional; minor announcement issues documented |
| 5-6 | Tested with one screen reader only; primary flows mostly work; some announcement gaps or confusing interactions |
| 3-4 | Limited AT testing; screen reader cannot complete primary flows; significant interaction failures |
| 1-2 | No assistive technology testing performed; compatibility is unknown |
