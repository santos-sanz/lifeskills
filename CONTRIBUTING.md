# Contributing to Lifeskills

## Add or change a skill

1. Keep the skill content in English and preserve the existing directory name unless a breaking release is intentional.
2. Keep `SKILL.md` self-contained with the required headings, explicit activation boundaries, guardrails, handoffs, and `Use $ARGUMENTS as initial context.`.
3. Add or update at least one reference, one template, one golden example, and the four canonical benchmark prompts.
4. Register required output sections, critical guardrails, and handoffs in `quality/benchmark-manifest.json`.
5. Use the shared evidence labels: Fact, Inference, Assumption, and Unknown.
6. Give every action an owner, due date, and success signal.

## Validate locally

```bash
python3 scripts/lint_skills.py
python3 scripts/validate_benchmark.py
python3 -m unittest discover -s tests -v
```

All checks must pass before opening a pull request. Run the manual response benchmark for every affected skill and record the model, commit, evaluator, scores, and guardrail result using `quality/eval-log-template.md`.

## Quality rules

- Do not fabricate sources, figures, citations, commitments, or outcomes.
- Keep named frameworks attributed in `quality/framework-sources.md`.
- Add a handoff when a skill's output naturally becomes another skill's input.
- Treat high-stakes, privacy, safety, legal, medical, financial, and regulatory cases as requiring explicit uncertainty and appropriate escalation.

## Versioning

Changes that preserve skill names and output behavior are content-compatible. New required headings or changed activation boundaries are contract changes and must be called out in the pull request. Breaking renames or removals require a migration note and a major version decision.
