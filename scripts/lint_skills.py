#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README_PATH = ROOT / "README.md"
PROMPTS_PATH = ROOT / "quality" / "test-prompts.md"

REQUIRED_HEADINGS = [
    "When to use this skill",
    "Required inputs",
    "Workflow",
    "Ask-first questions",
    "Assumption policy",
    "Output contract",
    "Guardrails",
    "Resources",
    "Keywords",
]

EXPECTED_PROMPT_SUBHEADINGS = [
    "Happy path",
    "Missing critical info",
    "Conflicting objectives",
    "High-stakes constraint",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter opener")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing frontmatter closer")

    raw_frontmatter = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}

    for line in raw_frontmatter.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+)$", line)
        if not match:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = match.groups()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        data[key] = value

    return data, body, raw_frontmatter


def extract_section(body: str, heading: str) -> str | None:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return None

    start = match.end()
    next_heading = re.search(r"^## \S", body[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(body)
    return body[start:end].strip("\n")


def collect_skill_dirs() -> list[Path]:
    if not SKILLS_DIR.exists():
        return []
    return sorted(
        [
            entry
            for entry in SKILLS_DIR.iterdir()
            if entry.is_dir() and not entry.is_symlink()
        ],
        key=lambda path: path.name,
    )


def lint_skills(errors: list[str]) -> set[str]:
    skill_dirs = collect_skill_dirs()
    if not skill_dirs:
        fail(errors, "No skill directories found under skills/.")
        return set()

    discovered: set[str] = set()

    for entry in sorted(SKILLS_DIR.iterdir(), key=lambda path: path.name):
        if entry.is_symlink():
            fail(errors, f"{entry.relative_to(ROOT)} is a symlink; skill targets must be real directories.")
        elif not entry.is_dir():
            fail(errors, f"{entry.relative_to(ROOT)} is not a directory.")

    for skill_dir in skill_dirs:
        discovered.add(skill_dir.name)
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists() or skill_file.is_symlink():
            fail(errors, f"{skill_dir.relative_to(ROOT)}/SKILL.md is missing or symlinked.")
            continue

        try:
            text = skill_file.read_text(encoding="utf-8")
            frontmatter, body, _ = parse_frontmatter(text)
        except Exception as exc:  # noqa: BLE001
            fail(errors, f"{skill_file.relative_to(ROOT)} frontmatter parse failed: {exc}")
            continue

        if frontmatter.get("name") != skill_dir.name:
            fail(
                errors,
                f"{skill_file.relative_to(ROOT)} frontmatter name {frontmatter.get('name')!r} does not match directory {skill_dir.name!r}.",
            )

        description = frontmatter.get("description", "").strip()
        if not description:
            fail(errors, f"{skill_file.relative_to(ROOT)} is missing a description in frontmatter.")

        for heading in REQUIRED_HEADINGS:
            if extract_section(body, heading) is None:
                fail(errors, f"{skill_file.relative_to(ROOT)} is missing required heading: ## {heading}.")

        if "Use $ARGUMENTS as initial context." not in body:
            fail(errors, f"{skill_file.relative_to(ROOT)} should include 'Use $ARGUMENTS as initial context.'")

        ask_section = extract_section(body, "Ask-first questions")
        if ask_section is not None:
            questions = [
                line
                for line in ask_section.splitlines()
                if re.match(r"^\d+\.\s+\S", line.strip())
            ]
            if not (1 <= len(questions) <= 3):
                fail(
                    errors,
                    f"{skill_file.relative_to(ROOT)} should list 1-3 ask-first questions; found {len(questions)}.",
                )

        resources_section = extract_section(body, "Resources")
        if resources_section is not None:
            resource_lines = [line.strip() for line in resources_section.splitlines() if line.strip()]
            for line in resource_lines:
                if not line.startswith("- "):
                    fail(errors, f"{skill_file.relative_to(ROOT)} has a malformed resources line: {line}")
                    continue
                match = re.search(r"`([^`]+)`", line)
                if not match:
                    match = re.search(r"\(([^)]+)\)", line)
                if not match:
                    fail(errors, f"{skill_file.relative_to(ROOT)} resources line is missing a local path: {line}")
                    continue
                target = match.group(1).strip()
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (skill_dir / target).resolve()
                if not resolved.exists():
                    fail(
                        errors,
                        f"{skill_file.relative_to(ROOT)} references missing resource: {target}",
                    )

        for nested in skill_dir.rglob("*"):
            if nested.is_symlink():
                fail(errors, f"{nested.relative_to(ROOT)} is a symlink; skill content must be fully tracked.")

    return discovered


def lint_readme(errors: list[str], skill_names: set[str]) -> None:
    text = README_PATH.read_text(encoding="utf-8")
    links = set(re.findall(r"\[([^\]]+)\]\(skills/([^)]+)\)", text))
    linked_skills = {target for _, target in links}

    missing = sorted(skill_names - linked_skills)
    extra = sorted(linked_skills - skill_names)

    if missing:
        fail(errors, f"README.md is missing links for: {', '.join(missing)}")
    if extra:
        fail(errors, f"README.md links unknown skills: {', '.join(extra)}")

    match = re.search(
        r"quality/test-prompts\.md`:\s*4 test prompts per skill \((\d+) total\)",
        text,
    )
    if not match:
        fail(errors, "README.md is missing the prompt-count statement for quality/test-prompts.md.")
    else:
        expected_total = len(skill_names) * 4
        actual_total = int(match.group(1))
        if actual_total != expected_total:
            fail(
                errors,
                f"README.md says {actual_total} total prompts, but {expected_total} are required for {len(skill_names)} skills.",
            )

    if "python scripts/lint_skills.py" not in text:
        fail(errors, "README.md is missing the local lint command in the validation workflow.")


def lint_prompt_bank(errors: list[str], skill_names: set[str]) -> None:
    text = PROMPTS_PATH.read_text(encoding="utf-8")
    section_matches = list(re.finditer(r"^## ([^\n]+)\n", text, re.MULTILINE))
    if not section_matches:
        fail(errors, "quality/test-prompts.md does not contain any skill sections.")
        return

    sections: dict[str, str] = {}
    for idx, match in enumerate(section_matches):
        name = match.group(1).strip()
        start = match.end()
        end = section_matches[idx + 1].start() if idx + 1 < len(section_matches) else len(text)
        sections[name] = text[start:end].strip()

    if set(sections) != skill_names:
        missing = sorted(skill_names - set(sections))
        extra = sorted(set(sections) - skill_names)
        if missing:
            fail(errors, f"quality/test-prompts.md is missing sections for: {', '.join(missing)}")
        if extra:
            fail(errors, f"quality/test-prompts.md has sections for unknown skills: {', '.join(extra)}")

    for name, content in sections.items():
        found = re.findall(r"^### ([^\n]+)$", content, re.MULTILINE)
        if found != EXPECTED_PROMPT_SUBHEADINGS:
            fail(
                errors,
                f"quality/test-prompts.md section {name!r} must contain the 4 standard prompt subheadings in order.",
            )


def main() -> int:
    errors: list[str] = []
    skill_names = lint_skills(errors)
    if skill_names:
        lint_readme(errors, skill_names)
        lint_prompt_bank(errors, skill_names)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"\n{len(errors)} lint issue(s) found.")
        return 1

    print(f"OK: {len(skill_names)} skills linted successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
