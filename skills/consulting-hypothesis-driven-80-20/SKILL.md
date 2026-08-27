---
name: consulting-hypothesis-driven-80-20
description: Build hypothesis-driven workplans with explicit 80/20 prioritization. Use when rapid decision-making requires testing assumptions, ranking opportunities, and focusing on highest-leverage analyses.
---

# Hypothesis Driven 80/20

Use $ARGUMENTS as initial context.

## When to use this skill
- Ambiguous problems that need fast direction before full analysis.
- Prioritizing limited team capacity across competing hypotheses.
- Designing a test plan with clear stop or continue criteria.
- Converting broad strategic questions into measurable experiments.

## When not to use this skill
- Do not use it to create a broad issue tree, a market inventory, or a portfolio allocation without a testable decision question.
- Do not label opinions as hypotheses when no measurable disconfirming signal is possible.

## Required inputs
- Governing business question and target metric.
- Time horizon and decision deadline.
- Data constraints and available analysis bandwidth.
- Current baseline, unit of analysis, and minimum reliable signal.

## Workflow
1. Define one decision question and explicit success metric.
2. Generate 3-7 falsifiable hypotheses using strict format.
3. For each hypothesis define expected signal, disconfirming signal, kill threshold, and measurement window.
4. Score hypotheses with 80/20 lens: impact, confidence, effort, speed.
5. Select top 1-2 hypotheses for minimum viable tests.
6. Build workplan with owners, deadlines, and decision checkpoints.

## Ask-first questions
Ask up to 3 questions before ranking hypotheses:
1. Which single metric determines decision success?
2. What is the latest acceptable date for a go or no-go decision?
3. Which datasets are trusted and immediately accessible?

## Assumption policy
- If critical data is unavailable, proceed with transparent assumptions.
- Annotate each assumption with confidence and validation action.
- Avoid merged hypotheses; keep one causal chain per hypothesis.
- Record data quality, sample limitations, and the test's decision relevance.

## Output contract
Always produce these sections in order:
1. Context
2. Decision or Recommendation
3. Analysis
4. Risks
5. Next Actions
6. Assumptions
- Every test includes an owner, due date, success signal, and decision checkpoint.
- Label evidence as Fact, Inference, Assumption, or Unknown.

## Guardrails
- Hypotheses must follow: "If X, then Y, because Z.".
- Avoid descriptive statements that cannot be disproven.
- Include both confirming and disconfirming signals.
- Stop low-value analysis once kill threshold is reached.
- Do not use false precision when the data cannot support a numeric threshold.

## Handoffs
- Use `consulting-issue-tree-mece` when the causal structure is still unclear.
- Use `decision-analysis-under-uncertainty` when several tested options must be compared.
- Use `execution-operating-system` when experiments become a sustained delivery program.

## Resources
- `references/hypothesis-design.md` - Falsifiability rules and signal design.
- `references/80-20-prioritization.md` - Scoring and sequencing framework.
- `templates/hypothesis-plan.md` - Decision-ready hypothesis template.
- `examples/hypothesis-example.md` - Golden example with incomplete inputs.

## Keywords
hypothesis driven, 80/20, falsifiable hypothesis, prioritization, test plan, consulting
