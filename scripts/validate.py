#!/usr/bin/env python3
"""Skill OS validation script.

Validates enriched SKILL.md files against the frontmatter schema
and constitutional requirements (v2.0.0).

Usage:
    python scripts/validate.py                              # Validate entire repo
    python scripts/validate.py agents/product-manager/      # Validate one agent
    python scripts/validate.py agents/pm/backlog-groomer/SKILL.md  # Validate one skill
"""

import os
import re
import sys
from pathlib import Path


# --- Constants ---

WORD_LIMITS = {"simple": 500, "medium": 1000, "complex": 1500}
VALID_COMPLEXITY = {"simple", "medium", "complex"}
REQUIRED_FIELDS = {"name", "description", "department", "agent", "version", "complexity", "related-skills"}
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 1024
NAME_MAX = 64
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
THIRD_PERSON_BLOCKLIST = ("You ", "I ", "We ", "Claude ")
PUSHY_KEYWORDS = ("use when", "suggest when", "also consider when")
REQUIRED_SECTIONS = [
    "Agent:", "Skill Description", "When to Use",
    "Workflow", "Anti-Patterns", "Output", "Related Skills",
]
ETHOS_PROFILE_MAX_WORDS = 500
REF_TOC_THRESHOLD_LINES = 300


# --- Helpers ---

def parse_frontmatter(text):
    """Extract YAML frontmatter from markdown text. Returns (dict, body)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("---", 3)
    if end == -1:
        return None, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()

    # Simple YAML parser (no external deps)
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # List item
        if stripped.startswith("- ") and current_key:
            if current_list is None:
                current_list = []
                fm[current_key] = current_list
            current_list.append(stripped[2:].strip())
            continue
        # Multi-line string continuation
        if line.startswith("  ") and current_key and current_key in fm and isinstance(fm[current_key], str):
            fm[current_key] += " " + stripped
            continue
        # Key: value
        if ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            current_key = key
            current_list = None
            if val == "" or val == "|" or val == ">":
                fm[key] = ""
            else:
                fm[key] = val
    return fm, body


def count_body_words(body):
    """Count words per FR-003: whitespace-delimited tokens excluding
    markdown heading markers, bullet markers, and code fence markers."""
    count = 0
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        # Skip code fence markers
        if stripped.startswith("```"):
            continue
        tokens = stripped.split()
        for token in tokens:
            # Skip heading markers
            if re.match(r"^#+$", token):
                continue
            # Skip bullet markers
            if token in ("-", "*", "+"):
                continue
            # Skip numbered list markers like "1." "2."
            if re.match(r"^\d+\.$", token):
                continue
            count += 1
    return count


def find_repo_root():
    """Walk up from scripts/ to find repo root (where agents/ lives)."""
    path = Path(__file__).resolve().parent.parent
    if (path / "agents").is_dir():
        return path
    # Fallback: current working directory
    cwd = Path.cwd()
    if (cwd / "agents").is_dir():
        return cwd
    return path


# --- Validators ---

class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, path, msg):
        self.errors.append(f"ERROR [{path}]: {msg}")

    def warn(self, path, msg):
        self.warnings.append(f"WARNING [{path}]: {msg}")

    @property
    def ok(self):
        return len(self.errors) == 0


def validate_skill(skill_path, repo_root, result):
    """Validate a single SKILL.md file."""
    rel = skill_path.relative_to(repo_root)

    try:
        text = skill_path.read_text(encoding="utf-8")
    except Exception as e:
        result.error(rel, f"Cannot read file: {e}")
        return

    fm, body = parse_frontmatter(text)

    # --- Frontmatter existence ---
    if fm is None:
        result.error(rel, "Missing YAML frontmatter (no opening ---)")
        return

    # --- Required fields ---
    for field in REQUIRED_FIELDS:
        if field not in fm:
            result.error(rel, f"Missing required frontmatter field: {field}")

    # --- Name validation ---
    name = fm.get("name", "")
    if name:
        if len(name) > NAME_MAX:
            result.error(rel, f"name exceeds {NAME_MAX} chars: {len(name)}")
        if not NAME_PATTERN.match(name):
            result.error(rel, f"name must be kebab-case [a-z0-9-]: '{name}'")
        # Must match parent directory name
        parent_dir = skill_path.parent.name
        if name != parent_dir:
            result.error(rel, f"name '{name}' does not match directory '{parent_dir}'")

    # --- Description validation ---
    desc = fm.get("description", "")
    if desc:
        if len(desc) < DESCRIPTION_MIN:
            result.error(rel, f"description too short ({len(desc)} chars, min {DESCRIPTION_MIN})")
        if len(desc) > DESCRIPTION_MAX:
            result.error(rel, f"description too long ({len(desc)} chars, max {DESCRIPTION_MAX})")
        for prefix in THIRD_PERSON_BLOCKLIST:
            if desc.startswith(prefix):
                result.warn(rel, f"description starts with '{prefix.strip()}' — should be third-person")
        desc_lower = desc.lower()
        has_pushy = any(kw in desc_lower for kw in PUSHY_KEYWORDS)
        if not has_pushy:
            result.warn(rel, "description missing pushy keywords (Use when/Suggest when/Also consider when)")

    # --- Version validation ---
    version = fm.get("version", "")
    if version and not VERSION_PATTERN.match(version):
        result.error(rel, f"version must be semver (X.Y.Z): '{version}'")

    # --- Complexity validation ---
    complexity = fm.get("complexity", "")
    if complexity and complexity not in VALID_COMPLEXITY:
        result.error(rel, f"complexity must be one of {VALID_COMPLEXITY}: '{complexity}'")

    # --- Department validation ---
    dept = fm.get("department", "")
    if dept:
        dept_dir = repo_root / "departments" / dept
        if not dept_dir.is_dir():
            result.error(rel, f"department '{dept}' has no matching directory at departments/{dept}/")

    # --- Agent validation ---
    agent = fm.get("agent", "")
    if agent:
        # Agent should match grandparent directory (agents/<agent>/<skill>/SKILL.md)
        expected_agent_dir = skill_path.parent.parent.name
        if agent != expected_agent_dir:
            result.error(rel, f"agent '{agent}' does not match agent directory '{expected_agent_dir}'")

    # --- Word count validation ---
    if complexity in WORD_LIMITS:
        word_count = count_body_words(body)
        limit = WORD_LIMITS[complexity]
        if word_count > limit:
            result.error(rel, f"body word count {word_count} exceeds {complexity} limit of {limit}")

    # --- Required sections ---
    for section in REQUIRED_SECTIONS:
        if section not in body:
            result.warn(rel, f"Missing section heading containing '{section}'")

    # --- Ethos profile reference ---
    if dept:
        ethos_filename = f"ideal-{dept}.md"
        if ethos_filename not in body and ethos_filename not in text:
            result.warn(rel, f"No reference to ethos profile '{ethos_filename}' found in file")

    # --- Triggers validation (optional field) ---
    triggers = fm.get("triggers", None)
    if triggers is not None:
        if not isinstance(triggers, list):
            result.warn(rel, "triggers must be a list of strings")
        else:
            for i, t in enumerate(triggers):
                if not isinstance(t, str) or not t.strip():
                    result.warn(rel, f"triggers[{i}] must be a non-empty string")
                elif len(t) < 5 or len(t) > 50:
                    result.warn(rel, f"triggers[{i}] should be 5-50 chars: '{t}' ({len(t)} chars)")

    # --- [GATE] marker validation ---
    if "[GATE]" in body:
        if complexity == "simple":
            result.warn(rel, "[GATE] marker found in a simple-complexity skill — gates are unusual for simple skills")

    # --- Related skills cross-reference paths ---
    related = fm.get("related-skills", [])
    if isinstance(related, list):
        for ref_path in related:
            if not ref_path:
                continue
            resolved = (skill_path.parent / ref_path).resolve()
            if not resolved.is_file():
                result.warn(rel, f"related-skills path does not resolve: {ref_path}")


def validate_ethos(ethos_path, repo_root, result):
    """Validate a department ethos profile."""
    rel = ethos_path.relative_to(repo_root)
    try:
        text = ethos_path.read_text(encoding="utf-8")
    except Exception as e:
        result.error(rel, f"Cannot read file: {e}")
        return

    word_count = count_body_words(text)
    if word_count > ETHOS_PROFILE_MAX_WORDS:
        result.error(rel, f"ethos profile word count {word_count} exceeds max {ETHOS_PROFILE_MAX_WORDS}")


def validate_allowed_tools(repo_root, result):
    """Validate allowed-tools.yaml if it exists."""
    policy_file = repo_root / "allowed-tools.yaml"
    if not policy_file.is_file():
        return

    try:
        text = policy_file.read_text(encoding="utf-8")
    except Exception as e:
        result.error("allowed-tools.yaml", f"Cannot read file: {e}")
        return

    # Simple YAML parsing — try yaml module, fall back to basic parsing
    try:
        import yaml
        data = yaml.safe_load(text)
    except ImportError:
        # No pyyaml — use basic string parsing
        data = {}
        for line in text.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if ":" in stripped and not stripped.startswith("-"):
                key, _, val = stripped.partition(":")
                val = val.strip()
                if val.isdigit():
                    data[key.strip()] = int(val)
                elif val == "[]":
                    data[key.strip()] = []
                elif val:
                    data[key.strip()] = val
                else:
                    data[key.strip()] = {}
        if not data:
            if "schema_version:" not in text:
                result.error("allowed-tools.yaml", "Missing schema_version field")
            return
    except Exception:
        if "schema_version:" not in text:
            result.error("allowed-tools.yaml", "Missing schema_version field")
        return

    if not isinstance(data, dict):
        result.error("allowed-tools.yaml", "File must be a YAML mapping")
        return

    # Check schema_version
    sv = data.get("schema_version")
    if sv is None:
        result.error("allowed-tools.yaml", "Missing schema_version field")
    elif sv != 1:
        result.warn("allowed-tools.yaml", f"Unknown schema_version: {sv} (expected 1)")

    # Check department references
    dept_tools = data.get("department", {})
    if isinstance(dept_tools, dict):
        for dept_name in dept_tools:
            if not (repo_root / "departments" / dept_name).is_dir():
                result.warn("allowed-tools.yaml", f"department '{dept_name}' not found in departments/")

    # Check agent references
    agent_tools = data.get("agent", {})
    if isinstance(agent_tools, dict):
        for agent_name in agent_tools:
            if not (repo_root / "agents" / agent_name).is_dir():
                result.warn("allowed-tools.yaml", f"agent '{agent_name}' not found in agents/")


def check_bidirectional_refs(all_skills, repo_root, result):
    """Check that cross-references are bidirectional (WARNING level)."""
    # Build map: skill_path -> list of related paths
    ref_map = {}
    for skill_path in all_skills:
        try:
            text = skill_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        if fm is None:
            continue
        related = fm.get("related-skills", [])
        if isinstance(related, list):
            resolved_refs = []
            for ref_path in related:
                if ref_path:
                    resolved = (skill_path.parent / ref_path).resolve()
                    resolved_refs.append(resolved)
            ref_map[skill_path.resolve()] = resolved_refs

    # Check bidirectionality
    for skill_abs, refs in ref_map.items():
        for ref_abs in refs:
            if ref_abs in ref_map:
                # Check if ref_abs points back to skill_abs
                back_refs = ref_map[ref_abs]
                if skill_abs not in back_refs:
                    rel = skill_abs.relative_to(repo_root)
                    ref_rel = ref_abs.relative_to(repo_root)
                    result.warn(rel, f"unidirectional cross-reference: references {ref_rel} but not referenced back")


def check_reference_toc(repo_root, result):
    """Check that reference files over 300 lines have a TOC."""
    for ref_file in repo_root.rglob("references/*.md"):
        try:
            lines = ref_file.read_text(encoding="utf-8").split("\n")
        except Exception:
            continue
        if len(lines) > REF_TOC_THRESHOLD_LINES:
            text = ref_file.read_text(encoding="utf-8")
            # Simple TOC detection: look for "Table of Contents" or a list of anchor links
            if "table of contents" not in text.lower() and "## Contents" not in text:
                rel = ref_file.relative_to(repo_root)
                result.warn(rel, f"reference file has {len(lines)} lines but no table of contents")


# --- Main ---

def main():
    repo_root = find_repo_root()
    result = ValidationResult()

    # Determine what to validate
    targets = sys.argv[1:] if len(sys.argv) > 1 else None

    if targets:
        # Validate specific paths
        skill_files = []
        for target in targets:
            target_path = Path(target).resolve()
            if target_path.is_file() and target_path.name == "SKILL.md":
                skill_files.append(target_path)
            elif target_path.is_dir():
                skill_files.extend(target_path.rglob("SKILL.md"))
            else:
                # Maybe it's relative
                abs_path = (repo_root / target).resolve()
                if abs_path.is_file() and abs_path.name == "SKILL.md":
                    skill_files.append(abs_path)
                elif abs_path.is_dir():
                    skill_files.extend(abs_path.rglob("SKILL.md"))
                else:
                    print(f"WARNING: Target not found: {target}", file=sys.stderr)
    else:
        # Full repo validation
        agents_dir = repo_root / "agents"
        skill_files = list(agents_dir.rglob("SKILL.md")) if agents_dir.is_dir() else []

    # Validate each skill file
    for skill_path in sorted(skill_files):
        validate_skill(skill_path, repo_root, result)

    # Validate ethos profiles
    departments_dir = repo_root / "departments"
    if departments_dir.is_dir():
        for ethos_file in sorted(departments_dir.rglob("ideal-*.md")):
            validate_ethos(ethos_file, repo_root, result)

    # Check bidirectional refs (full repo only, or if multiple files)
    if len(skill_files) > 1:
        check_bidirectional_refs(skill_files, repo_root, result)

    # Check allowed-tools.yaml
    validate_allowed_tools(repo_root, result)

    # Check reference file TOC requirements
    check_reference_toc(repo_root, result)

    # Report
    total_skills = len(skill_files)
    print(f"\nValidated {total_skills} skill file(s)")
    print(f"  Errors:   {len(result.errors)}")
    print(f"  Warnings: {len(result.warnings)}")

    if result.errors:
        print("\n--- ERRORS ---")
        for e in result.errors:
            print(f"  {e}")

    if result.warnings:
        print("\n--- WARNINGS ---")
        for w in result.warnings:
            print(f"  {w}")

    if result.ok:
        print("\n✓ PASS — no errors found")
    else:
        print(f"\n✗ FAIL — {len(result.errors)} error(s) found")

    sys.exit(0 if result.ok else 1)


if __name__ == "__main__":
    main()
