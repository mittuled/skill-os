# Session Analysis Framework

## Purpose

A structured framework for analysing user session recordings to extract actionable design insights. Covers observation methodology, friction classification, and insight documentation standards.

## Analysis Methodology

### The OERS Method (Observe, Evaluate, Recognise, Surface)

| Stage | Activity | Output |
|-------|----------|--------|
| Observe | Watch sessions without forming conclusions; note raw behaviours | Raw observation log |
| Evaluate | Classify each behaviour against the friction taxonomy | Tagged observation list |
| Recognise | Identify patterns across multiple sessions | Pattern clusters |
| Surface | Formulate design insights and recommendations | Insight register |

Watch sessions at least twice: first at normal speed to experience the flow as a user, then at 0.5× speed to catch micro-hesitations.

### Minimum Session Sample

| User Segment | Minimum Sessions | Saturation Point |
|-------------|-----------------|-----------------|
| Single flow, single segment | 5 sessions | 8-10 sessions |
| Multi-flow analysis | 10 sessions | 15-20 sessions |
| Post-launch broad audit | 20 sessions | 30+ sessions |

Nielsen's Rule: 5 sessions reveal ~85% of usability issues for a single user group. Do not stop at 3.

## Friction Taxonomy

Classify each observed behaviour into a friction type:

| Friction Type | Definition | Behavioural Signal |
|--------------|------------|-------------------|
| Navigation confusion | User cannot determine where to go next | Repeated back-taps, hovering between options, pogo-sticking |
| Label ambiguity | User does not understand what a UI element does or means | Pausing before tapping, reading labels multiple times, wrong selection corrected |
| Interaction dead end | User reaches a state with no clear path forward | Idle state of 5+ seconds, rage-taps, session abandonment |
| Form friction | Input process causes hesitation or error | Backspace usage, field re-entry, validation error loops |
| Trust signal gap | User hesitates at a decision point requiring commitment | Scrolling up and down on confirmation screens, exiting before confirming |
| Load frustration | Wait times cause user to lose context or abandon | Rage-taps during loading, back navigation during load, session exit |
| Visual hierarchy failure | User misses a primary action or key information | Scrolling past a CTA, overlooking a status indicator |
| Cognitive overload | Too many choices or too much information causes hesitation | Long dwell time before choosing, random selection behaviour |

## Severity Classification

Rate each friction instance by its impact on task completion:

| Severity | Definition | Examples |
|----------|------------|---------|
| Critical | Prevents task completion; causes session abandonment | Dead end with no escape, broken flow |
| Major | Significantly slows task completion; causes visible frustration | Repeated validation failures, 10+ second hesitation |
| Minor | Slows user slightly; no frustration visible | Brief hesitation before correct action, minor label ambiguity |
| Observation | User behaviour worth noting; no friction present | Unexpected but successful navigation path |

## Observation Logging Standards

For each observation, record:

| Field | Format | Example |
|-------|--------|---------|
| Session ID | [SES-XXX] | SES-012 |
| Timestamp | [MM:SS in recording] | 02:34 |
| Screen | [Screen name] | Cart — checkout entry |
| Friction type | [Type from taxonomy] | Navigation confusion |
| Severity | [Critical/Major/Minor/Observation] | Major |
| Behaviour observed | [Factual description of what the user did] | "User tapped the 'Continue shopping' button instead of 'Checkout', then immediately tapped back" |
| Hypothesised cause | [Design hypothesis — not fact] | "CTA label 'Continue shopping' placed above 'Checkout' creates ambiguity about which is the primary action" |

## Pattern Recognition Threshold

| Pattern Strength | Definition |
|-----------------|------------|
| Strong signal | Same friction observed in 4+ sessions independently |
| Moderate signal | Same friction observed in 2-3 sessions |
| Weak signal | Single-session observation — note but do not act alone |
| Noise | Single occurrence in an outlier session — document only |

## Design Recommendation Format

For each pattern surfaced, document a design recommendation:

**Pattern**: [Brief description of observed pattern]
**Sessions affected**: [Number of sessions where observed / total sessions reviewed]
**Friction type**: [Type]
**Severity**: [Critical/Major/Minor]
**Root cause hypothesis**: [Design element causing the behaviour]
**Recommendation**: [Specific design change to address]
**Effort estimate**: [Hours / Days]
**Validation method**: [How to confirm fix worked — e.g. "Re-test with 5 sessions post-change"]
