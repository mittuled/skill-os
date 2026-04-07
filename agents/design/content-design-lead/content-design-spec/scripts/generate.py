#!/usr/bin/env python3
"""
content-design-spec — Generate content design specification with voice, tone, and copy standards.
Input (JSON via stdin or -i):
  {
    "product": str,
    "brand": str,
    "product_type": str,       # e.g. "B2B SaaS", "Developer Tool", "Consumer App"
    "voice_attributes": [      # 3-5 attributes
      {
        "attribute": str,      # e.g. "Direct"
        "not": str,            # contrast: "not Blunt"
        "do_example": str,
        "dont_example": str
      }
    ],
    "primary_personas": list[str],  # e.g. ["Software Engineers", "Product Managers"]
    "key_surfaces": list[str],  # e.g. ["Onboarding", "Error messages", "Settings"]
    "terminology": [            # product-specific terms
      {
        "term": str,
        "definition": str,
        "approved_usage": str,
        "avoid": str           # deprecated or incorrect alternatives
      }
    ]
  }
Output: Content design specification as Markdown.
"""

import json
import sys
import argparse

COPY_PATTERNS = {
    "button_labels": {
        "rule": "Use verb + object. Avoid 'OK', 'Yes', 'Submit'. Make buttons predict the outcome.",
        "examples": [
            ("Save changes", "Submit"),
            ("Delete project", "Yes"),
            ("Start free trial", "OK"),
        ],
    },
    "error_messages": {
        "rule": "State what went wrong + what to do next. Never blame the user.",
        "examples": [
            ("Your file exceeds 10MB. Try a smaller file.", "Upload failed."),
            ("This email is already in use. Sign in instead?", "Invalid email."),
        ],
    },
    "empty_states": {
        "rule": "Explain what belongs here + provide a clear first action. Never leave a blank space.",
        "examples": [
            ("You haven't created any pipelines yet. Create your first pipeline →", "No pipelines."),
            ("Your team hasn't shared any files. Upload a file to get started.", "No files yet."),
        ],
    },
    "success_messages": {
        "rule": "Confirm what happened, briefly. Don't over-celebrate. Skip 'Congratulations!'",
        "examples": [
            ("Pipeline deployed successfully.", "Great job! Your pipeline has been deployed!"),
            ("Settings saved.", "Congrats! Settings have been saved successfully!"),
        ],
    },
    "form_validation": {
        "rule": "Inline, specific, actionable. Show on blur (not on submit). Use friendly language.",
        "examples": [
            ("Enter a valid email address.", "Email is invalid."),
            ("Password must be at least 8 characters.", "Password too short."),
        ],
    },
    "loading_states": {
        "rule": "Tell the user what is happening. Use active present tense.",
        "examples": [
            ("Running tests...", "Loading..."),
            ("Deploying your pipeline...", "Please wait."),
        ],
    },
    "destructive_actions": {
        "rule": "Be explicit about the consequence. Use the specific noun, not generic 'this'.",
        "examples": [
            ("Delete 'Production Pipeline'? This cannot be undone.", "Are you sure?"),
            ("Remove Sarah Chen from this project? She will lose access immediately.", "Confirm?"),
        ],
    },
}

GRAMMAR_RULES = [
    ("Capitalisation", "Sentence case for all UI text (headings, labels, buttons). Title Case only for product names and proper nouns."),
    ("Punctuation", "No full stops in button labels, headings, or single-line UI text. Use full stops in multi-sentence body text."),
    ("Numbers", "Spell out one through nine; use numerals for 10+. Always use numerals for data values."),
    ("Dates", "Use unambiguous formats: 'March 31, 2026' or '31 Mar 2026'. Avoid '03/31/26'."),
    ("Abbreviations", "Spell out on first use: 'Application Programming Interface (API)'. Use the abbreviation thereafter."),
    ("Ampersand", "Use 'and' in prose. Ampersand (&) only acceptable in navigation and tight UI space."),
    ("Contractions", "Use contractions to sound natural (you're, it's, we'll). Avoid in formal/legal contexts."),
    ("Exclamation marks", "Limit to one per feature area maximum. Reserve for genuine moments of delight, not routine confirmations."),
]

ACCESSIBILITY_STANDARDS = [
    ("Alt text", "Describe the function, not the appearance. Decorative images: alt=''. Icons with labels: alt=''."),
    ("ARIA labels", "Add aria-label when the visible text is insufficient. Be specific: 'Delete project: Flowline Production' not 'Delete'."),
    ("Link text", "Links must make sense out of context. Use 'View deployment logs' not 'click here'."),
    ("Error association", "Error messages must be programmatically associated with the input (aria-describedby)."),
    ("Loading announcements", "Dynamic loading states must be announced via aria-live='polite'."),
    ("Button vs link", "Use <button> for actions, <a> for navigation. Never use 'click here' as visible text."),
]

TONE_BY_CONTEXT = [
    ("Success / Celebration", "Warm but understated. Confirm clearly. Skip superlatives."),
    ("Error / Failure", "Empathetic, not apologetic. Focus on resolution, not the problem."),
    ("Onboarding", "Encouraging and instructive. Assume intelligence; explain only what is genuinely new."),
    ("Destructive actions", "Direct and specific. No softening language. Consequences must be unambiguous."),
    ("Empty states", "Helpful and forward-looking. Guide the next action."),
    ("Settings / Config", "Precise and informative. User expertise is assumed."),
    ("Notifications", "Concise. Lead with what changed, follow with what to do."),
]


def validate_input(data: dict) -> list[str]:
    required = ["product", "brand", "product_type", "voice_attributes", "primary_personas", "key_surfaces"]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "voice_attributes" in data:
        if len(data["voice_attributes"]) < 3:
            errors.append("voice_attributes: minimum 3 attributes required")
        if len(data["voice_attributes"]) > 5:
            errors.append("voice_attributes: maximum 5 attributes — focus on what differentiates your voice")
    return errors


def generate(data: dict) -> str:
    product = data["product"]

    voice_section = []
    for attr in data["voice_attributes"]:
        voice_section.append(
            f"### {attr['attribute']}, not {attr['not']}\n\n"
            f"**Do**: {attr['do_example']}\n\n"
            f"**Don't**: {attr['dont_example']}\n"
        )
    voice_md = "\n".join(voice_section)

    tone_rows = "\n".join(
        f"| {ctx} | {tone} |" for ctx, tone in TONE_BY_CONTEXT
    )

    terminology_section = []
    if "terminology" in data and data["terminology"]:
        term_rows = "\n".join(
            f"| **{t['term']}** | {t['definition']} | {t['approved_usage']} | {t['avoid']} |"
            for t in data["terminology"]
        )
        terminology_section = [
            "## Terminology Glossary",
            "",
            "| Term | Definition | Approved Usage | Avoid |",
            "|------|-----------|----------------|-------|",
            term_rows,
            "",
        ]

    patterns_section = []
    for pattern_key, pattern in COPY_PATTERNS.items():
        label = pattern_key.replace("_", " ").title()
        examples_md = "\n".join(
            f"  - **Do**: _{ex[0]}_  |  **Don't**: ~~{ex[1]}~~" for ex in pattern["examples"]
        )
        patterns_section.append(f"### {label}\n\n**Rule**: {pattern['rule']}\n\n{examples_md}\n")

    patterns_md = "\n".join(patterns_section)

    grammar_rows = "\n".join(f"| {rule} | {desc} |" for rule, desc in GRAMMAR_RULES)

    a11y_rows = "\n".join(f"| {std} | {desc} |" for std, desc in ACCESSIBILITY_STANDARDS)

    surfaces_md = "\n".join(f"- {s}" for s in data["key_surfaces"])
    personas_md = "\n".join(f"- {p}" for p in data["primary_personas"])

    lines = [
        f"# Content Design Specification: {product}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Product | {product} |",
        f"| Brand | {data['brand']} |",
        f"| Product Type | {data['product_type']} |",
        f"| Voice Attributes | {len(data['voice_attributes'])} defined |",
        f"| Primary Personas | {', '.join(data['primary_personas'][:2])} |",
        f"| Skill | content-design-spec |",
        "",
        "## Context",
        "",
        f"**Primary personas:**",
        personas_md,
        "",
        f"**Key product surfaces covered:**",
        surfaces_md,
        "",
        "## Voice and Tone Framework",
        "",
        "### Voice Attributes",
        "",
        voice_md,
        "### Tone by Context",
        "",
        "| Context | Tone Direction |",
        "|---------|----------------|",
        tone_rows,
        "",
    ] + terminology_section + [
        "## Copy Pattern Library",
        "",
        patterns_md,
        "## Grammar and Mechanics",
        "",
        "| Rule | Standard |",
        "|------|---------|",
        grammar_rows,
        "",
        "## Accessibility Copy Standards",
        "",
        "| Standard | Implementation |",
        "|----------|---------------|",
        a11y_rows,
        "",
        "## Living Document Protocol",
        "",
        "This spec is a living document. Update when:",
        "- A new product surface introduces copy patterns not covered here",
        "- Terminology changes following a rename or repositioning",
        "- Voice calibration feedback from research reveals misalignment",
        "- Accessibility audit identifies a pattern gap",
        "",
        "**Owner**: Content Design Lead",
        "**Review cadence**: Quarterly or triggered by above conditions",
        "**Change log**: Maintain at the bottom of the document with date + summary of change",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate content design specification")
    parser.add_argument("-i", "--input", help="Input JSON file (default: stdin)")
    parser.add_argument("-o", "--output", help="Output Markdown file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    errors = validate_input(data)
    if errors:
        print("Input validation errors:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    output = generate(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Content design spec written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
