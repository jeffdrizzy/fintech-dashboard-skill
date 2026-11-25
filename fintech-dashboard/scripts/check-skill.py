#!/usr/bin/env python3
"""Validate the fintech-dashboard agent skill.

Checks:
  - SKILL.md exists and starts with YAML frontmatter
  - name is present, lowercase with hyphens, max 64 chars
  - description is present, max 1024 chars, no angle brackets
  - SKILL.md is under 500 lines
  - all files referenced from SKILL.md exist
  - no region-specific content in the skill folder

Usage:
  python3 check-skill.py
Run from the fintech-dashboard/ directory, or from anywhere;
the script resolves paths relative to its own location.
"""

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
MAX_LINES = 500
MAX_NAME = 64
MAX_DESC = 1024

FORBIDDEN_TERMS = ["nigeria", "naira", "stackr", "kova"]

errors = []
warnings = []


def fail(message):
    errors.append(message)
    print("FAIL: " + message)


def ok(message):
    print("OK: " + message)


def main():
    if not SKILL_MD.exists():
        fail("SKILL.md not found at " + str(SKILL_MD))
        print("FAILED: %d error(s)" % len(errors))
        return 1

    text = SKILL_MD.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. Frontmatter is first, between --- markers
    if not lines or lines[0].strip() != "---":
        fail("SKILL.md must start with --- frontmatter on line 1")
        print("FAILED: %d error(s)" % len(errors))
        return 1

    try:
        end = lines.index("---", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed with ---")
        print("FAILED: %d error(s)" % len(errors))
        return 1

    frontmatter = "\n".join(lines[1:end])

    # 2. Angle brackets anywhere in frontmatter
    if "<" in frontmatter or ">" in frontmatter:
        fail("frontmatter contains angle brackets")
    else:
        ok("no angle brackets in frontmatter")

    # 3. Name
    name_match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.M)
    if not name_match:
        fail("frontmatter is missing name:")
    else:
        name = name_match.group(1).strip()
        if len(name) > MAX_NAME:
            fail("name is %d chars, max %d" % (len(name), MAX_NAME))
        elif not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            fail("name must be lowercase letters, digits, and hyphens: " + name)
        else:
            ok("name is %r (%d chars)" % (name, len(name)))

    # 4. Description
    desc_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.M)
    if not desc_match:
        fail("frontmatter is missing description:")
    else:
        desc = desc_match.group(1).strip()
        if len(desc) > MAX_DESC:
            fail("description is %d chars, max %d" % (len(desc), MAX_DESC))
        elif "<" in desc or ">" in desc:
            fail("description contains angle brackets")
        else:
            ok("description is %d chars" % len(desc))
        if "when" not in desc.lower() and "use" not in desc.lower():
            warnings.append("description should state when to use the skill")

    # 5. Line count
    if len(lines) >= MAX_LINES:
        fail("SKILL.md is %d lines, must be under %d" % (len(lines), MAX_LINES))
    else:
        ok("SKILL.md is %d lines (under %d)" % (len(lines), MAX_LINES))

    # 6. Referenced files exist
    refs = re.findall(r"`(references/[^`]+|examples/[^`]+)`", text)
    refs = sorted(set(refs))
    if not refs:
        warnings.append("no references/ or examples/ files are linked from SKILL.md")
    for ref in refs:
        path = SKILL_DIR / ref
        if path.exists():
            ok("referenced file exists: " + ref)
        else:
            fail("referenced file missing: " + ref)

    # 7. No region-specific content in the skill folder
    skill_files = [SKILL_MD]
    skill_files += sorted((SKILL_DIR / "references").glob("*.md"))
    skill_files += sorted((SKILL_DIR / "examples").glob("*.md"))
    for path in skill_files:
        content = path.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN_TERMS:
            if term in content:
                fail("forbidden term %r found in %s" % (term, path.name))
    if not any("forbidden term" in e for e in errors):
        ok("no region-specific terms in skill files")

    # 8. Companion files exist
    for rel in ["scripts/check-skill.py"]:
        if (SKILL_DIR / rel).exists():
            ok("companion file exists: " + rel)

    if warnings:
        for w in warnings:
            print("WARN: " + w)

    if errors:
        print("FAILED: %d error(s)" % len(errors))
        return 1

    print("PASSED: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
