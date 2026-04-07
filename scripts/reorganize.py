#!/usr/bin/env python3
"""
Reorganize agents/ from flat structure into department subdirectories.

Before: agents/<agent>/<skill>/SKILL.md
After:  agents/<dept>/<agent>/<skill>/SKILL.md
"""

import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

DEPT_MAP = {
    "engineering": [
        "vp-engineering", "tech-architect", "tech-lead-pr-reviewer", "database-expert",
        "sr-frontend-developer", "sr-backend-developer", "qa-test-engineer",
        "devops-infrastructure-engineer", "platform-engineer", "data-engineer",
        "security-engineer", "ai-ml-engineer"
    ],
    "product": [
        "vp-product", "product-manager", "product-operations-analyst",
        "pmm", "pmm-analyst-content-strategist"
    ],
    "marketing": [
        "vp-marketing", "demand-gen-manager", "content-marketer",
        "pr-communications-manager", "marketing-operations-manager",
        "social-media-manager", "lifecycle-email-marketing-manager",
        "event-marketing-manager", "analyst-relations-manager",
        "community-manager", "developer-relations-lead", "technical-writer"
    ],
    "design": [
        "head-of-design", "ux-ui-designer", "visual-interaction-designer",
        "brand-designer", "ux-research-lead", "ux-researcher",
        "content-design-lead", "content-designer-ux-writer"
    ],
    "data-growth": [
        "analytics-lead", "data-analyst", "growth-lead", "growth-engineer"
    ],
    "finance": [
        "cfo-vp-finance", "finance-manager", "fpa-analyst",
        "controller-accounting", "investor-relations-manager"
    ],
    "legal": [
        "general-counsel", "corporate-counsel", "product-counsel",
        "security-compliance-programme-manager"
    ],
    "sales": [
        "vp-sales", "sales-manager", "account-executive", "sales-development-rep",
        "business-development", "solutions-engineering-manager", "solutions-engineer"
    ],
    "agent-operations": [
        "vp-agent-operations", "agent-operations-manager", "skill-builder-lead",
        "skill-builder", "agent-trainer-skill-optimizer", "agent-configuration-manager"
    ],
    "customer-success": [
        "head-of-customer-success", "cs-manager", "customer-success-manager",
        "uat-coordinator-cs", "customer-programs-manager", "technical-account-manager"
    ],
    "customer-support": [
        "support-manager", "support-agent"
    ],
    "technical-operations": [
        "it-operations-manager", "it-support-specialist", "vendor-management-procurement"
    ],
    "revenue-operations": [
        "revenue-operations"
    ],
    "applied-research": [
        "applied-research-lead"
    ],
    "account-management": [
        "account-management-lead", "account-manager"
    ],
    "implementation": [
        "implementation-lead", "implementation-engineer"
    ]
}

# Build reverse map: agent -> dept
AGENT_TO_DEPT = {}
for dept, agents in DEPT_MAP.items():
    for agent in agents:
        AGENT_TO_DEPT[agent] = dept


def move_agents():
    """Move agent directories into department subdirectories."""
    agents_dir = REPO_ROOT / "agents"
    moved = []
    skipped = []

    for dept, agents in DEPT_MAP.items():
        dept_dir = agents_dir / dept
        dept_dir.mkdir(exist_ok=True)

        for agent in agents:
            src = agents_dir / agent
            dst = dept_dir / agent

            if src.exists():
                if dst.exists():
                    print(f"  SKIP (already exists): {agent} -> {dept}/{agent}")
                    skipped.append(agent)
                elif src == dept_dir:
                    # Edge case: dept name == agent name (e.g. revenue-operations)
                    # The dept dir IS the src dir. Move contents out via temp.
                    tmp = agents_dir / f"_tmp_{agent}"
                    shutil.copytree(str(src), str(tmp))
                    shutil.rmtree(str(src))
                    # Re-create the dept dir and move in
                    dept_dir.mkdir(exist_ok=True)
                    shutil.move(str(tmp), str(dst))
                    print(f"  MOVED (self-ref): {agent} -> {dept}/{agent}")
                    moved.append((agent, dept))
                else:
                    shutil.move(str(src), str(dst))
                    print(f"  MOVED: {agent} -> {dept}/{agent}")
                    moved.append((agent, dept))
            else:
                print(f"  NOT FOUND: {agent} (expected at agents/{agent}/)")

    print(f"\nMoved {len(moved)} agents, skipped {len(skipped)}")
    return moved


def fix_cross_agent_ref(match):
    """Replace ../../<agent>/ with ../../../<dept>/<agent>/"""
    prefix = match.group(1)  # e.g. "../../" or "[text](../../"
    agent = match.group(2)
    suffix = match.group(3)   # e.g. "/" or remaining path

    dept = AGENT_TO_DEPT.get(agent)
    if dept:
        return f"{prefix}../{dept}/{agent}{suffix}"
    else:
        # Unknown agent, leave as-is
        return match.group(0)


def fix_paths_in_skill_files():
    """Fix relative paths in all .md and .yaml files under agents/"""
    agents_dir = REPO_ROOT / "agents"
    fixed_count = 0

    for fpath in agents_dir.rglob("*"):
        if not fpath.is_file():
            continue
        if fpath.suffix not in (".md", ".yaml", ".yml"):
            continue

        content = fpath.read_text(encoding="utf-8")
        original = content

        # Fix: ../../allowed-tools.yaml -> ../../../allowed-tools.yaml
        content = content.replace(
            "../../allowed-tools.yaml",
            "../../../allowed-tools.yaml"
        )

        # Fix: ../../../departments/ -> ../../../../departments/
        content = content.replace(
            "../../../departments/",
            "../../../../departments/"
        )

        # Fix cross-agent relative refs: ../../<agent>/<rest>
        # Pattern: ../../<known-agent>/<something>
        # We need to turn ../../<agent>/ into ../../../<dept>/<agent>/
        # This appears in both markdown links and YAML frontmatter
        # Match: (../../)(<agent-slug>)(/)
        # Note: must NOT match ../../allowed-tools.yaml or ../../departments/
        cross_agent_pattern = re.compile(
            r'(\.\./\.\./)'
            r'(' + '|'.join(re.escape(a) for a in sorted(AGENT_TO_DEPT.keys(), key=len, reverse=True)) + r')'
            r'(/)'
        )

        def replace_cross_agent(m):
            lead = m.group(1)
            agent = m.group(2)
            trail = m.group(3)
            dept = AGENT_TO_DEPT.get(agent)
            if dept:
                return f"../../../{dept}/{agent}{trail}"
            return m.group(0)

        content = cross_agent_pattern.sub(replace_cross_agent, content)

        if content != original:
            fpath.write_text(content, encoding="utf-8")
            fixed_count += 1
            print(f"  FIXED paths: {fpath.relative_to(REPO_ROOT)}")

    print(f"\nFixed paths in {fixed_count} skill files")


def fix_paths_in_root_files():
    """Fix agents/<agent>/ references in root-level files."""
    root_files = [
        REPO_ROOT / "CLAUDE.md",
        REPO_ROOT / "README.md",
        REPO_ROOT / "SKILLS.md",
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "CONTRIBUTING.md",
        REPO_ROOT / "status.md",
    ]

    # Pattern to match agents/<agent>/ or agents/<agent>/<skill>
    # We need to insert the dept between agents/ and <agent>/
    agent_path_pattern = re.compile(
        r'(agents/)'
        r'(' + '|'.join(re.escape(a) for a in sorted(AGENT_TO_DEPT.keys(), key=len, reverse=True)) + r')'
        r'(/)'
    )

    def replace_agent_path(m):
        lead = m.group(1)
        agent = m.group(2)
        trail = m.group(3)
        dept = AGENT_TO_DEPT.get(agent)
        if dept:
            return f"agents/{dept}/{agent}{trail}"
        return m.group(0)

    fixed_count = 0
    for fpath in root_files:
        if not fpath.exists():
            continue
        content = fpath.read_text(encoding="utf-8")
        original = content
        content = agent_path_pattern.sub(replace_agent_path, content)
        if content != original:
            fpath.write_text(content, encoding="utf-8")
            fixed_count += 1
            print(f"  FIXED root file: {fpath.name}")

    print(f"Fixed {fixed_count} root files")


def fix_paths_in_specs():
    """Fix agents/<agent>/ references in specs/ and departments/ directories."""
    dirs_to_fix = [
        REPO_ROOT / "specs",
        REPO_ROOT / "departments",
        REPO_ROOT / "_shared",
    ]

    agent_path_pattern = re.compile(
        r'(agents/)'
        r'(' + '|'.join(re.escape(a) for a in sorted(AGENT_TO_DEPT.keys(), key=len, reverse=True)) + r')'
        r'(/)'
    )

    def replace_agent_path(m):
        lead = m.group(1)
        agent = m.group(2)
        trail = m.group(3)
        dept = AGENT_TO_DEPT.get(agent)
        if dept:
            return f"agents/{dept}/{agent}{trail}"
        return m.group(0)

    fixed_count = 0
    for base_dir in dirs_to_fix:
        if not base_dir.exists():
            continue
        for fpath in base_dir.rglob("*"):
            if not fpath.is_file():
                continue
            if fpath.suffix not in (".md", ".yaml", ".yml", ".txt"):
                continue
            content = fpath.read_text(encoding="utf-8")
            original = content
            content = agent_path_pattern.sub(replace_agent_path, content)
            if content != original:
                fpath.write_text(content, encoding="utf-8")
                fixed_count += 1
                print(f"  FIXED: {fpath.relative_to(REPO_ROOT)}")

    print(f"Fixed {fixed_count} files in specs/departments/_shared")


def main():
    print("=== Step 1: Moving agent directories ===")
    move_agents()

    print("\n=== Step 2: Fixing paths in skill files ===")
    fix_paths_in_skill_files()

    print("\n=== Step 3: Fixing paths in root files ===")
    fix_paths_in_root_files()

    print("\n=== Step 4: Fixing paths in specs/departments/_shared ===")
    fix_paths_in_specs()

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
