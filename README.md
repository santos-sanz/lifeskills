# Lifeskills

A curated collection of non-coding skills for AI agents focused on business-critical communication, strategy, negotiation, and influence.

These skills follow a shared quality contract for decision-ready outputs and explicit handling of uncertainty.

Language of skill content: English.

## Skills included

## Negotiation and influence

### [negotiation-voss-tactical-empathy](skills/negotiation-voss-tactical-empathy)
Negotiation planning and execution with tactical empathy, strategy/script separation, BATNA/ZOPA framing, and conditional concessions.

### [persuasion-cialdini-influence-design](skills/persuasion-cialdini-influence-design)
Ethical persuasion design using Cialdini principles with principle-to-evidence-to-claim traceability.

## Structured communication

### Mindset & Personal Strategy

#### [luffy-mindset](skills/luffy-mindset)
Applies an audacious, practical "Luffy Mindset" for bold execution plans when explicitly requested.
*   **Best for:** Breaking hesitation, pursuing ambitious goals, and converting fear into action.
*   **Key Capabilities:** Fearless reframing, 3-7 step action planning, risk countermoves, and 24-hour commitment starts.

### Consulting Frameworks

## Consulting frameworks

### [consulting-issue-tree-mece](skills/consulting-issue-tree-mece)
MECE issue-tree decomposition with formal validation gates and prioritized analysis backlog mapping.

### [consulting-hypothesis-driven-80-20](skills/consulting-hypothesis-driven-80-20)
Hypothesis-driven planning with falsifiable design, kill criteria, and 80/20 prioritization.

### [consulting-market-competition-analysis](skills/consulting-market-competition-analysis)
Market sizing and competitive analysis with top-down/bottom-up triangulation and uncertainty-aware scenarios.

### [consulting-portfolio-growth-strategy](skills/consulting-portfolio-growth-strategy)
Portfolio allocation and growth sequencing using BCG, GE/McKinsey, and Ansoff logic.

## Shared output contract

Every skill is designed to return the same section order:
1. Context
2. Decision or Recommendation
3. Analysis
4. Risks
5. Next Actions
6. Assumptions

This improves consistency across skills and makes outputs easier to review in high-stakes workflows.

## Quality system

The repository includes a reusable evaluation framework in [`quality/`](quality):
- `quality/rubric.md`: common scoring rubric (1-5).
- `quality/test-prompts.md`: 4 test prompts per skill (28 total).
- `quality/eval-log-template.md`: logging template for manual evaluations.

Target acceptance thresholds:
- Per-skill average >= 4.2
- No criterion below 3.5
- Zero critical guardrail failures

## Installation

```bash
npx skills add https://github.com/santos-sanz/lifeskills
```

## Repository structure

```text
skills/
  <skill-name>/
    SKILL.md
    references/
    templates/
    examples/
quality/
  rubric.md
  test-prompts.md
  eval-log-template.md
```

## Design principles used in this version

This iteration integrated patterns commonly used in high-quality agent skills ecosystems:
- Prompt contracts for predictable outputs.
- Rubric-driven evaluation for quality control.
- Explicit uncertainty and assumption tagging.
- Ethical guardrails for persuasion and negotiation tasks.
