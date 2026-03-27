#!/usr/bin/env python3
"""
configure-secrets.py — Store credentials in the platform's native secret store.

Purpose:
    Detects the AI platform in use (Claude Code, generic) and writes a
    credential to the platform's secret store. NEVER writes secrets to
    any file in the repository.

Dependencies: None (Python 3.10+ standard library only)

Usage:
    python3 configure-secrets.py --tool slack --key SLACK_BOT_TOKEN --value xoxb-...
    python3 configure-secrets.py --tool github --key GITHUB_TOKEN --value ghp_...
    python3 configure-secrets.py --list
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def detect_platform() -> str:
    """Detect which AI platform is in use."""
    # Claude Code sets CLAUDE_CODE=1 or runs inside a known environment
    if os.environ.get("CLAUDE_CODE") or os.environ.get("CLAUDE_SESSION_ID"):
        return "claude-code"

    # Check for common CI/CD platforms
    if os.environ.get("GITHUB_ACTIONS"):
        return "github-actions"

    if os.environ.get("GITLAB_CI"):
        return "gitlab-ci"

    return "generic"


def get_env_file_path(platform: str) -> Path | None:
    """Get the path to the platform's secret store (env file outside repo)."""
    if platform == "claude-code":
        # Claude Code uses ~/.claude/.env for secrets
        claude_dir = Path.home() / ".claude"
        claude_dir.mkdir(exist_ok=True)
        return claude_dir / ".env"

    # Generic: use ~/.config/skill-os/.env
    config_dir = Path.home() / ".config" / "skill-os"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / ".env"


def is_inside_repo(path: Path) -> bool:
    """Check if a path is inside a git repository working tree."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )
        if result.returncode == 0:
            repo_root = Path(result.stdout.strip()).resolve()
            return str(path.resolve()).startswith(str(repo_root))
    except FileNotFoundError:
        pass
    return False


def read_env_file(path: Path) -> dict[str, str]:
    """Read an .env file into a dict."""
    env_vars: dict[str, str] = {}
    if not path.exists():
        return env_vars

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env_vars[key.strip()] = value.strip()
    return env_vars


def write_env_file(path: Path, env_vars: dict[str, str]) -> None:
    """Write a dict to an .env file."""
    with open(path, "w") as f:
        f.write("# skill-os managed secrets — DO NOT commit this file\n")
        for key, value in sorted(env_vars.items()):
            f.write(f"{key}={value}\n")

    # Restrict permissions to owner only
    path.chmod(0o600)


def store_secret(tool: str, key: str, value: str) -> dict:
    """Store a secret in the platform's secret store."""
    platform = detect_platform()
    env_path = get_env_file_path(platform)

    if env_path is None:
        return {
            "success": False,
            "error": f"No secret store available for platform: {platform}",
            "platform": platform,
        }

    # Safety check: never write inside the repo
    if is_inside_repo(env_path):
        return {
            "success": False,
            "error": "REFUSED: secret store path is inside the git repository. This is a security violation.",
            "path": str(env_path),
        }

    # Prefix key with tool name for namespacing
    namespaced_key = f"{tool.upper()}_{key}" if not key.startswith(tool.upper()) else key

    env_vars = read_env_file(env_path)
    env_vars[namespaced_key] = value
    write_env_file(env_path, env_vars)

    return {
        "success": True,
        "platform": platform,
        "store_path": str(env_path),
        "key": namespaced_key,
        "tool": tool,
        "message": f"Secret stored for {tool}. Key: {namespaced_key}",
    }


def list_secrets() -> dict:
    """List stored secret keys (not values) for all platforms."""
    platform = detect_platform()
    env_path = get_env_file_path(platform)

    if env_path is None or not env_path.exists():
        return {"platform": platform, "secrets": [], "count": 0}

    env_vars = read_env_file(env_path)
    # Only return keys, never values
    keys = sorted(env_vars.keys())

    return {
        "platform": platform,
        "store_path": str(env_path),
        "secrets": keys,
        "count": len(keys),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Store credentials in the platform's native secret store."
    )
    parser.add_argument("--tool", help="Tool name (e.g., slack, github)")
    parser.add_argument("--key", help="Secret key name (e.g., API_TOKEN)")
    parser.add_argument("--value", help="Secret value")
    parser.add_argument(
        "--list", action="store_true", help="List stored secret keys (not values)"
    )
    args = parser.parse_args()

    if args.list:
        result = list_secrets()
        print(json.dumps(result, indent=2))
        return

    if not all([args.tool, args.key, args.value]):
        parser.error("--tool, --key, and --value are required when storing a secret")

    result = store_secret(args.tool, args.key, args.value)
    print(json.dumps(result, indent=2))

    if not result["success"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
