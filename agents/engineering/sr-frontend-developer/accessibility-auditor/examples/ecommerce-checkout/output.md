# Accessibility Audit Report: E-commerce Checkout

**Standard:** WCAG 2.1 Level AA
**Pages tested:** Cart, Shipping, Payment, Confirmation
**Tools used:** axe-core, NVDA, VoiceOver, Lighthouse

## Critical Issues

### 1. Form Inputs Missing Visible Labels (WCAG 1.3.1, 3.3.2)

**Location:** Shipping address form
**Issue:** Placeholder text used as only label. Disappears on input focus.
**Impact:** Screen readers cannot identify fields. Users with cognitive disabilities lose context.

```html
<!-- Before: placeholder-only -->
<input type="text" placeholder="Street address" />

<!-- After: proper labeling -->
<label for="street-address">Street address</label>
<input type="text" id="street-address" autocomplete="street-address" />
```

### 2. Error Messages Not Programmatically Associated (WCAG 3.3.1)

**Location:** All form fields
**Issue:** Validation errors appear visually but are not linked to inputs via `aria-describedby`.

```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  aria-describedby="email-error"
  aria-invalid="true"
/>
<span id="email-error" role="alert">Please enter a valid email address</span>
```

### 3. Focus Not Visible on Checkout Steps (WCAG 2.4.7)

**Location:** Step indicator (Cart > Shipping > Payment > Confirm)
**Issue:** `outline: none` applied globally with no replacement focus style.

```css
/* Before */
*:focus { outline: none; }

/* After */
*:focus-visible {
  outline: 2px solid #1a73e8;
  outline-offset: 2px;
}
```

## Major Issues

### 4. Color-Only Error Indication (WCAG 1.4.1)

**Location:** Credit card form
**Issue:** Invalid fields highlighted only with red border. No icon or text for color-blind users.
**Fix:** Add error icon + text alongside the color change.

### 5. Keyboard Trap in Payment iFrame (WCAG 2.1.2)

**Location:** Stripe Elements iframe
**Issue:** Tab key cycles within iframe without escape path.
**Fix:** Add `tabindex` management and a "Skip to order summary" link before the iframe.

### 6. Missing Live Region for Cart Updates (WCAG 4.1.3)

**Location:** Cart quantity stepper
**Issue:** Changing quantity updates total visually but screen readers are not notified.

```html
<div aria-live="polite" aria-atomic="true">
  Cart total: $45.99 (3 items)
</div>
```

## Minor Issues

### 7. Insufficient Color Contrast on "Apply Coupon" Link (WCAG 1.4.3)

**Current:** #999 on #fff = 2.85:1 (fails AA)
**Required:** 4.5:1 minimum
**Fix:** Change to #595959 on #fff = 7.0:1

### 8. Missing `autocomplete` Attributes (WCAG 1.3.5)

**Location:** Shipping and payment forms
**Fix:** Add appropriate autocomplete values.

```html
<input type="text" id="name" autocomplete="name" />
<input type="text" id="cc-number" autocomplete="cc-number" />
<input type="text" id="postal-code" autocomplete="postal-code" />
```

## Summary

| Severity | Count | WCAG Criteria |
|----------|-------|---------------|
| Critical | 3 | 1.3.1, 2.4.7, 3.3.1, 3.3.2 |
| Major | 3 | 1.4.1, 2.1.2, 4.1.3 |
| Minor | 2 | 1.3.5, 1.4.3 |

**Overall:** Fails WCAG 2.1 AA. 6 blocking issues must be resolved before launch.
