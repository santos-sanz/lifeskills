---
name: decision-analysis-under-uncertainty
description: Compare consequential options under incomplete information using explicit criteria, scenarios, reversibility, and decision triggers. Use when a choice must be made without false precision.
---

# Decision Analysis Under Uncertainty

Use $ARGUMENTS as initial context.

## When to use this skill
- A person or team must choose among options with incomplete or conflicting information.
- The choice has meaningful downside, timing pressure, or different reversibility profiles.
- Stakeholders need transparent criteria, trade-offs, and conditions for revisiting the decision.

## When not to use this skill
- Do not use it for a simple factual lookup or a decision already fixed by a legal, safety, or governance requirement.
- Do not create numeric scores when the criteria, units, or evidence cannot support them.
- Do not hide an unresolved issue tree or research gap behind a recommendation.

## Required inputs
- Decision statement, decision owner, deadline, and cost of inaction.
- Options in scope, including the status quo and a low-regret fallback where relevant.
- Decision criteria, constraints, risk tolerance, and available evidence.
- What is reversible, what is not, and which unknowns could change the choice.

## Workflow
1. Frame one decision, owner, deadline, and consequence of delay.
2. Define feasible options and remove options that violate hard constraints.
3. Agree criteria, units, weights, and evidence before scoring.
4. Model base, downside, and upside scenarios without false precision.
5. Assess reversibility, dependencies, second-order effects, and risk exposure.
6. Recommend one option, name the trade-off, and state what would change the decision.
7. Create a review date, trigger thresholds, owner, and next actions.

## Ask-first questions
Ask up to 3 questions before comparing options:
1. Who owns the decision, and what deadline is binding?
2. Which constraints are genuinely hard, and what is the cost of inaction?
3. Which unknown would most likely change the choice?

## Assumption policy
- Separate facts, inferences, assumptions, and unknowns in the option comparison.
- Show scoring method, weights, units, and sensitivity when numbers are used.
- Use ranges or qualitative levels when evidence does not support point estimates.
- Treat irreversible or high-impact decisions as requiring explicit approval and contingency planning.

## Output contract
Always produce these sections in order:
1. Decision and owner
2. Options
3. Criteria and weights
4. Scenario analysis
5. Reversibility and risk
6. Recommendation
7. Triggers and review date
8. Next actions
9. Assumptions
- Label material statements as Fact, Inference, Assumption, or Unknown.
- Every action includes an owner, due date, and success signal.
- State the condition that would change the recommendation.

## Guardrails
- Do not use false precision, hidden weights, or double-counted criteria.
- Do not invent probabilities, costs, evidence, stakeholder commitments, or risk tolerance.
- Include the status quo or explain why it is infeasible.
- Surface material downside scenarios and a practical mitigation or fallback.
- Escalate legal, medical, financial, safety, or governance constraints to the appropriate authority.

## Handoffs
- Use `research-evidence-synthesis` when the decision lacks verified evidence.
- Use `consulting-issue-tree-mece` when the decision problem is not yet decomposed.
- Use `high-agency` when the chosen path is blocked by a solvable execution constraint.
- Use `execution-operating-system` when the decision becomes a multi-week delivery program.
- Use `pyramid-principle-structured-communication` for the final decision memo.

## Resources
- `references/decision-framework.md` - Decision framing, criteria, weights, scenarios, and sensitivity.
- `references/risk-and-reversibility.md` - Reversibility, downside, triggers, and escalation rules.
- `templates/decision-analysis.md` - Decision comparison template.
- `examples/decision-analysis-example.md` - Golden example with visible trade-offs and triggers.

## Keywords
decision analysis, uncertainty, options, trade-offs, expected value, scenarios, reversibility, risk, decision memo
