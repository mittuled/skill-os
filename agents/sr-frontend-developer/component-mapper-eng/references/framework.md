# Framework: Component Mapping and Design Token Alignment

Reference for mapping Figma design components to codebase component implementations, resolving naming mismatches, and enforcing design token consistency.

## Component Classification Taxonomy

Every component belongs to exactly one classification level:

| Level | Name | Description | Examples |
|-------|------|-------------|---------|
| L0 | Primitive | Single HTML element with styling, no composition | Button, Input, Text, Icon |
| L1 | Atom | 2–4 primitives composed into a reusable unit | TextField (Label + Input + ErrorMessage), Badge |
| L2 | Molecule | Atoms composed into a functional UI unit | SearchBar, FormField, Card, Dropdown |
| L3 | Organism | Molecules + domain logic composing a full UI section | Header, ProductList, CheckoutForm |
| L4 | Template | Layout skeleton defining placement of organisms, no domain data | PageLayout, DashboardShell |
| L5 | Page | Template + live data + routing | ProductDetailPage, AccountSettingsPage |

**Mapping rule**: Design components map to L0–L3. L4–L5 components are code-side only constructs.

## Naming Convention Alignment

Figma and code often diverge in naming. Apply this resolution priority:

1. **Exact match**: Figma name = Code name — no action needed.
2. **Semantic match**: Different surface name, same concept — use code name; document Figma alias.
3. **Structural mismatch**: Figma has one component; code splits it into 2+ — map one-to-many; document the split.
4. **Missing in code**: Figma component exists but no code equivalent — create a new component; use Figma name as default.
5. **Deprecated in design**: Code component has no Figma counterpart — flag for design review; do not add new usages.

### Naming Pattern Matrix

| Figma Pattern | Code Convention (React) | Code Convention (Vue) | Code Convention (Web Component) |
|---------------|------------------------|----------------------|----------------------------------|
| `ComponentName / Variant` | `<ComponentName variant="x">` | `<component-name variant="x">` | `<component-name variant="x">` |
| `ComponentName / State=Hover` | CSS pseudo-class `:hover` | Same | Same |
| `ComponentName / Size=Large` | `size="lg"` prop | `size="lg"` prop | `size="lg"` attribute |
| `ComponentName / Icon=Left` | `iconPosition="left"` | Same | Same |

## Design Token Mapping

### Token Categories and CSS Custom Property Naming

| Category | Figma Token Name | CSS Custom Property | Example Value |
|----------|-----------------|---------------------|---------------|
| Color — Brand | `color/brand/primary` | `--color-brand-primary` | `#1A73E8` |
| Color — Semantic | `color/feedback/error` | `--color-feedback-error` | `#D93025` |
| Color — Neutral | `color/neutral/700` | `--color-neutral-700` | `#3C4043` |
| Spacing | `spacing/4` | `--spacing-4` | `16px` |
| Spacing | `spacing/8` | `--spacing-8` | `32px` |
| Typography — Size | `type/body/size` | `--type-body-size` | `16px` |
| Typography — Weight | `type/heading/weight` | `--type-heading-weight` | `600` |
| Border Radius | `radius/md` | `--radius-md` | `8px` |
| Shadow | `shadow/card` | `--shadow-card` | `0 2px 8px rgba(0,0,0,0.1)` |
| Motion — Duration | `motion/fast` | `--motion-fast` | `150ms` |
| Motion — Easing | `motion/ease-out` | `--motion-ease-out` | `cubic-bezier(0.0, 0, 0.2, 1)` |

### Token Tiers (3-tier system)

```
Tier 1: Global (primitives)     → color/blue/500 = #4285F4
          ↓ aliased by
Tier 2: Semantic (intent)       → color/brand/primary → color/blue/500
          ↓ consumed by
Tier 3: Component (specific)    → button/background/primary → color/brand/primary
```

**Rule**: Components must consume Tier 3 or Tier 2 tokens. Consuming Tier 1 directly is a code smell — it bypasses semantic intent.

## State Coverage Matrix

Every interactive component must handle all applicable states. Use this matrix to verify coverage during mapping:

| Component Type | Default | Hover | Focus | Active | Disabled | Loading | Error | Empty | Selected |
|---------------|---------|-------|-------|--------|----------|---------|-------|-------|----------|
| Button | Required | Required | Required | Required | Required | Optional | — | — | Optional |
| Input | Required | Required | Required | Required | Required | — | Required | Required | — |
| Dropdown | Required | Required | Required | Required | Required | Required | Required | Required | Required |
| Card | Required | Optional | Optional | Optional | Optional | Optional | — | Required | Optional |
| List item | Required | Required | Required | Required | Optional | — | — | Required | Required |

**Mapping gap rule**: If a required state exists in Figma but is absent from code, open a component-gap ticket before proceeding with page implementation.

## Variant Mapping Decision Tree

```
Does the Figma variant differ only in color/spacing?
  └── Yes → Map to CSS modifier or design token; no new component variant needed
  └── No → Does it differ in structure (different DOM)?
       └── Yes → New component variant required (add variant prop)
       └── No → Does it differ in behaviour/interaction?
            └── Yes → New component or composition pattern
            └── No → Figma design inconsistency — flag to designer
```

## Component Inventory Template

Use this table to document the mapping for each Figma frame analyzed:

| Figma Component | Classification | Code Component | Token Coverage | State Coverage | Gaps |
|----------------|---------------|----------------|----------------|----------------|------|
| [Figma name] | [L0–L5] | [ComponentName in codebase] | [Complete/Partial/Missing] | [Complete/Partial] | [List gaps] |

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correct Pattern |
|-------------|---------------|----------------|
| Hardcoding hex values in component CSS | Bypasses token system; breaks theme switching | Use CSS custom property from token tier 2 or 3 |
| One giant "smart" component for every variant | Hard to test, slow to render, poor reusability | Split on L0–L3 classification boundary |
| Duplicating a component to support one new state | Explodes component count; diverges styles | Add state prop or CSS modifier to existing component |
| Using pixel values from Figma directly in code | Breaks responsive scaling; loses semantic spacing | Map to spacing token first |
| Ignoring Figma's "Detached from component" flag | Indicates one-off design that may not need a code component | Confirm with designer whether to standardize or leave as template-level HTML |
