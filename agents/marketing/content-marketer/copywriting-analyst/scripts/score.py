#!/usr/bin/env python3
"""
score.py — Computes readability and persuasion scores for marketing copy.

Purpose: Accepts a JSON object with copy text, computes Flesch-Kincaid grade level,
         average sentence length, passive voice percentage, and persuasion marker
         presence, then outputs a structured JSON assessment.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    echo '{"text": "Your copy here...", "audience": "b2b_saas"}' | python3 score.py
    python3 score.py < copy.json
    python3 score.py -o report.json < copy.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AUDIENCE_BENCHMARKS: dict[str, dict[str, tuple[float, float]]] = {
    "b2b_saas": {
        "fk_grade": (8.0, 10.0),
        "avg_sentence_length": (15.0, 20.0),
        "passive_pct": (0.0, 10.0),
    },
    "b2c": {
        "fk_grade": (6.0, 8.0),
        "avg_sentence_length": (12.0, 16.0),
        "passive_pct": (0.0, 5.0),
    },
    "technical": {
        "fk_grade": (10.0, 12.0),
        "avg_sentence_length": (18.0, 22.0),
        "passive_pct": (0.0, 15.0),
    },
}

POWER_WORDS: set[str] = {
    "proven", "guaranteed", "instant", "exclusive", "free", "new", "results",
    "discover", "secret", "powerful", "breakthrough", "transform", "unlock",
    "effortless", "limited", "urgent", "fastest", "easiest", "save", "boost",
}

PASSIVE_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"\b(?:is|are|was|were|been|being|be)\s+\w+ed\b", re.IGNORECASE),
    re.compile(r"\b(?:is|are|was|were|been|being|be)\s+\w+en\b", re.IGNORECASE),
]


def split_sentences(text: str) -> list[str]:
    """Split text into sentences."""
    sentences = re.split(r'[.!?]+\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


def count_syllables(word: str) -> int:
    """Estimate syllable count for a word."""
    word = word.lower().strip(".,!?;:'\"()-")
    if not word:
        return 0
    count = 0
    vowels = "aeiouy"
    prev_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def flesch_kincaid_grade(sentences: list[str], words: list[str]) -> float:
    """Compute Flesch-Kincaid Grade Level."""
    num_sentences = len(sentences)
    num_words = len(words)
    if num_sentences == 0 or num_words == 0:
        return 0.0
    num_syllables = sum(count_syllables(w) for w in words)
    grade = (0.39 * (num_words / num_sentences) +
             11.8 * (num_syllables / num_words) - 15.59)
    return round(max(0.0, grade), 1)


def passive_voice_pct(sentences: list[str]) -> float:
    """Estimate percentage of sentences containing passive voice."""
    if not sentences:
        return 0.0
    passive_count = 0
    for sentence in sentences:
        for pattern in PASSIVE_PATTERNS:
            if pattern.search(sentence):
                passive_count += 1
                break
    return round((passive_count / len(sentences)) * 100, 1)


def count_persuasion_markers(text: str) -> dict[str, dict]:
    """Count persuasion markers in text."""
    lower_text = text.lower()
    words_in_text = set(re.findall(r'\b\w+\b', lower_text))

    found_power = words_in_text & POWER_WORDS
    has_numbers = bool(re.search(r'\b\d+%?\b', text))
    has_social_proof = bool(re.search(
        r'(?:customer|client|team|company|user)s?\s+(?:love|trust|rely|use|choose)',
        lower_text
    )) or bool(re.search(r'(?:testimonial|case study|review)', lower_text))
    has_risk_reversal = bool(re.search(
        r'(?:free trial|money.?back|no credit card|cancel anytime|risk.?free|guarantee)',
        lower_text
    ))
    has_objection = bool(re.search(
        r'(?:no (?:hidden|extra)|worry|concern|but what|even if|whether)',
        lower_text
    ))

    return {
        "social_proof": {"present": has_social_proof, "quality": 3 if has_social_proof else 0},
        "specificity": {"present": has_numbers, "quality": 3 if has_numbers else 0},
        "power_words": {"present": len(found_power) > 0, "count": len(found_power), "words": sorted(found_power)},
        "objection_handling": {"present": has_objection, "quality": 3 if has_objection else 0},
        "risk_reversal": {"present": has_risk_reversal, "quality": 3 if has_risk_reversal else 0},
    }


def analyse_copy(data: dict) -> dict:
    """Run full copy analysis."""
    text = data.get("text", "")
    audience = data.get("audience", "b2b_saas")

    if not text.strip():
        return {"error": "No text provided", "scores": None}

    benchmarks = AUDIENCE_BENCHMARKS.get(audience, AUDIENCE_BENCHMARKS["b2b_saas"])
    sentences = split_sentences(text)
    words = re.findall(r'\b\w+\b', text)

    fk_grade = flesch_kincaid_grade(sentences, words)
    avg_sent_len = round(len(words) / max(1, len(sentences)), 1)
    passive_pct = passive_voice_pct(sentences)
    persuasion = count_persuasion_markers(text)

    def in_range(val: float, low: float, high: float) -> str:
        if low <= val <= high:
            return "pass"
        return "needs_work"

    fk_low, fk_high = benchmarks["fk_grade"]
    sl_low, sl_high = benchmarks["avg_sentence_length"]
    pv_low, pv_high = benchmarks["passive_pct"]

    return {
        "error": None,
        "audience": audience,
        "word_count": len(words),
        "sentence_count": len(sentences),
        "readability": {
            "flesch_kincaid_grade": fk_grade,
            "fk_benchmark": f"{fk_low}-{fk_high}",
            "fk_status": in_range(fk_grade, fk_low, fk_high),
            "avg_sentence_length": avg_sent_len,
            "sl_benchmark": f"{sl_low}-{sl_high}",
            "sl_status": in_range(avg_sent_len, sl_low, sl_high),
            "passive_voice_pct": passive_pct,
            "pv_benchmark": f"{pv_low}-{pv_high}%",
            "pv_status": in_range(passive_pct, pv_low, pv_high),
        },
        "persuasion": persuasion,
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON input: {exc}"}))
        sys.exit(1)

    result = analyse_copy(data)
    output = json.dumps(result, indent=2)

    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
            print(f"Report written to {args[idx]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
