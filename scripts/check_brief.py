#!/usr/bin/env python3
"""Check that a project brief keeps its shape.

Fails if the brief is missing any of the five question headings or runs
past the 16,000-character limit for Claude Projects instructions.

Usage: python3 scripts/check_brief.py [path ...]   (default: AGENTS.md)
"""
import re
import sys
from pathlib import Path

LIMIT = 16_000
HEADINGS = [
    "Who it's for",
    "Where the work happens",
    "How a thread checks its own work",
    "When something is missing",
    "What needs my go-ahead",
]


def check(path: Path) -> list[str]:
    if not path.is_file():
        return [f"{path}: file not found"]
    text = path.read_text(encoding="utf-8")
    found = {m.strip() for m in re.findall(r"^##\s+(.+?)\s*$", text, re.M)}
    problems = [f"{path}: missing heading '## {h}'" for h in HEADINGS if h not in found]
    if len(text) > LIMIT:
        problems.append(f"{path}: {len(text):,} characters, over the {LIMIT:,} limit")
    return problems


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv] or [Path("AGENTS.md")]
    failed = False
    for path in paths:
        problems = check(path)
        if problems:
            failed = True
            print("\n".join(problems))
        else:
            size = len(path.read_text(encoding="utf-8"))
            print(f"{path}: ok ({size:,} of {LIMIT:,} characters, 5 of 5 headings)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
