#!/usr/bin/env python3
"""
run.py — Orchestrates the full hiring-plan-builder workflow.

Runs the complete hiring plan builder workflow: score input document and generate output template.

Usage:
    python3 run.py <input-document.md>              # Score and generate report
    python3 run.py <input-document.md> -o output/   # Write all outputs to directory
    python3 run.py --generate-only                   # Generate template only

Dependencies: Python 3.10+ standard library only.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent


def run_score(doc_path: Path) -> dict:
    """Run the scoring script and return results."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "score.py"), str(doc_path), "--json"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Scoring failed: {result.stderr}", file=sys.stderr)
        return {"error": result.stderr}
    return json.loads(result.stdout)


def run_generate(output_path: Path | None = None) -> str:
    """Run the template generator."""
    cmd = [sys.executable, str(SCRIPT_DIR / "generate.py")]
    if output_path:
        cmd.extend(["-o", str(output_path)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Generation failed: {result.stderr}", file=sys.stderr)
        return ""
    return result.stdout


def main() -> None:
    args = sys.argv[1:]
    
    if not args or "-h" in args or "--help" in args:
        print("Usage: python3 run.py <input-document.md> [-o output-dir/]")
        print("       python3 run.py --generate-only [-o output.md]")
        sys.exit(0)
    
    if "--generate-only" in args:
        output_path = None
        if "-o" in args:
            idx = args.index("-o") + 1
            if idx < len(args):
                output_path = Path(args[idx])
        result = run_generate(output_path)
        if not output_path:
            print(result)
        return
    
    doc_path = Path(args[0])
    if not doc_path.exists():
        print(f"Error: File not found: {doc_path}", file=sys.stderr)
        sys.exit(1)
    
    # Determine output directory
    output_dir = None
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            output_dir = Path(args[idx])
            output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Score
    print(f"Scoring {doc_path.name}...")
    scores = run_score(doc_path)
    
    if "error" not in scores:
        print(f"  Composite: {scores['composite_score']}/10.00 ({scores['grade']} — {scores['grade_label']})")
        for name, data in scores.get("criteria", {}).items():
            print(f"  {name}: {data['score']}/10")
    
    if output_dir:
        score_path = output_dir / "scores.json"
        score_path.write_text(json.dumps(scores, indent=2) + "\n", encoding="utf-8")
        print(f"  Scores written to {score_path}")
        
        report_path = output_dir / "report.md"
        run_generate(report_path)
        print(f"  Template written to {report_path}")
    
    print("Done.")


if __name__ == "__main__":
    main()
