#!/usr/bin/env python3
"""Validate the deterministic benchmark contract for every Lifeskills skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README_PATH = ROOT / "README.md"
PROMPTS_PATH = ROOT / "quality" / "test-prompts.md"
MANIFEST_PATH = ROOT / "quality" / "benchmark-manifest.json"
EXPECTED_PROMPT_TYPES = (
    "Happy path",
    "Missing critical info",
    "Conflicting objectives",
    "High-stakes constraint",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def heading_matches(actual: str, expected: str) -> bool:
    actual_normalized = normalize(actual)
    expected_normalized = normalize(expected)
    return actual_normalized == expected_normalized or actual_normalized.startswith(
        f"{expected_normalized} ("
    )


def skill_names() -> set[str]:
    return {
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and not path.is_symlink()
    }


def parse_prompt_bank(text: str) -> dict[str, list[str]]:
    matches = list(re.finditer(r"^## ([^\n]+)\n", text, re.MULTILINE))
    sections: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        content = text[match.end() : end]
        sections[match.group(1).strip()] = re.findall(
            r"^### ([^\n]+)$", content, re.MULTILINE
        )
    return sections


def markdown_headings(path: Path) -> list[str]:
    return re.findall(r"^## ([^\n]+)$", path.read_text(encoding="utf-8"), re.MULTILINE)


def validate() -> list[str]:
    errors: list[str] = []
    if not MANIFEST_PATH.exists():
        return ["quality/benchmark-manifest.json is missing."]

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"quality/benchmark-manifest.json is invalid JSON: {exc}"]

    names = skill_names()
    manifest_skills = manifest.get("skills")
    if manifest.get("version") != 1:
        errors.append("quality/benchmark-manifest.json must declare version 1.")
    if manifest.get("prompt_types") != list(EXPECTED_PROMPT_TYPES):
        errors.append("benchmark manifest prompt_types do not match the canonical four prompt types.")
    if not isinstance(manifest_skills, dict):
        return errors + ["benchmark manifest skills must be an object."]
    if set(manifest_skills) != names:
        missing = sorted(names - set(manifest_skills))
        extra = sorted(set(manifest_skills) - names)
        if missing:
            errors.append(f"benchmark manifest is missing skills: {', '.join(missing)}")
        if extra:
            errors.append(f"benchmark manifest has unknown skills: {', '.join(extra)}")

    prompt_sections = parse_prompt_bank(PROMPTS_PATH.read_text(encoding="utf-8"))
    if set(prompt_sections) != names:
        errors.append("benchmark prompt sections do not match the skill directories.")
    for name in sorted(names):
        if prompt_sections.get(name) != list(EXPECTED_PROMPT_TYPES):
            errors.append(f"{name} must contain the four canonical benchmark prompt types in order.")

        skill_dir = SKILLS_DIR / name
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        entry = manifest_skills.get(name, {})
        required_sections = entry.get("required_output_sections", [])
        guardrails = entry.get("critical_guardrails", [])
        handoffs = entry.get("handoffs", [])
        if not required_sections:
            errors.append(f"{name} has no required output sections in the benchmark manifest.")
        for phrase in guardrails:
            if not isinstance(phrase, str) or normalize(phrase) not in normalize(skill_text):
                errors.append(f"{name} is missing critical guardrail text: {phrase!r}")
        known_handoffs = names - {name}
        for target in handoffs:
            if target not in known_handoffs:
                errors.append(f"{name} has an invalid handoff target: {target!r}")
            elif f"`{target}`" not in skill_text:
                errors.append(f"{name} does not document handoff target `{target}`.")

        for resource_dir in ("references", "templates", "examples"):
            resource_files = sorted((skill_dir / resource_dir).glob("*.md"))
            if not resource_files:
                errors.append(f"{name}/{resource_dir} has no Markdown resources.")
                continue
            if resource_dir in ("templates", "examples"):
                headings = markdown_headings(resource_files[0])
                missing = [
                    section
                    for section in required_sections
                    if not any(heading_matches(actual, section) for actual in headings)
                ]
                if missing:
                    errors.append(
                        f"{name}/{resource_dir} is missing output headings: {', '.join(missing)}"
                    )

    readme = README_PATH.read_text(encoding="utf-8")
    if "quality/benchmark-manifest.json" not in readme:
        errors.append("README.md must document quality/benchmark-manifest.json.")
    if "scripts/validate_benchmark.py" not in readme:
        errors.append("README.md must document scripts/validate_benchmark.py.")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"\n{len(errors)} benchmark issue(s) found.")
        return 1
    print(f"OK: deterministic benchmark contract validated for {len(skill_names())} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
