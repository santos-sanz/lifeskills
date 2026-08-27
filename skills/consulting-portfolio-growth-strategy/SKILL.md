---
name: consulting-portfolio-growth-strategy
description: Build portfolio and growth strategy decisions with BCG, GE/McKinsey, and Ansoff logic. Use when allocating capital, prioritizing business units, and sequencing growth moves under constraints.
---

# Portfolio and Growth Strategy

Use $ARGUMENTS as initial context.

## When to use this skill
- Portfolio reallocation across business units or product lines.
- Growth planning where trade-offs and dependency management matter.
- Strategy reviews with invest, hold, harvest, or exit decisions.
- Cases requiring transparent scoring logic and governance.

## When not to use this skill
- Do not use it for a single product's execution plan or a market analysis with no allocation decision.
- Do not treat BCG, GE/McKinsey, or Ansoff categories as automatic recommendations.

## Required inputs
- Portfolio units and baseline performance metrics.
- Strategic objective (growth, profitability, cash generation, risk reduction).
- Resource constraints and planning horizon.
- Capacity baseline, dependencies, scoring evidence, and downside tolerance.

## Workflow
1. Define unit boundaries and decision objective.
2. Select framework (BCG, GE/McKinsey, Ansoff, or combined).
3. Build weighted scoring model for attractiveness and competitive position with normalized units.
4. Run weight sensitivity and dependency checks before classifying units into invest, hold, harvest, or exit buckets.
5. Allocate capital and capacity with explicit dependency checks.
6. Sequence growth moves with milestone-based checkpoints.

## Ask-first questions
Ask up to 3 questions before mapping units:
1. What is the primary objective of this portfolio cycle?
2. Which constraints are binding (budget, talent, time, risk)?
3. What level of downside risk is acceptable?

## Assumption policy
- Continue with assumptions if unit data is incomplete.
- Mark assumptions with confidence and expected impact if wrong.
- Keep scoring criteria explicit to avoid hidden bias.
- Record data vintage, scoring evidence, and what would change each classification.

## Output contract
Always produce these sections in order:
1. Context
2. Decision or Recommendation
3. Analysis
4. Risks
5. Next Actions
6. Assumptions
- Every allocation action includes an owner, due date, success signal, and review gate.
- Show scoring criteria, weights, units, and sensitivity results before the recommendation.

## Guardrails
- Do not map units without stating scoring criteria and weights.
- Avoid framework-only outputs without resource implications.
- Include dependencies between units before final allocation.
- Separate short-term cash optimization from long-term strategic value.
- Do not recommend an allocation that exceeds verified capacity or ignores transition cost.

## Handoffs
- Use `consulting-market-competition-analysis` when attractiveness depends on external market sizing or competitor evidence.
- Use `decision-analysis-under-uncertainty` when the portfolio decision needs explicit scenario and reversibility analysis.
- Use `execution-operating-system` after allocation to run the multi-period delivery cadence.

## Resources
- `references/portfolio-frameworks.md` - Framework selection and scoring rules.
- `references/growth-levers.md` - Growth move catalog and sequencing logic.
- `templates/portfolio-growth-plan.md` - Decision-ready template.
- `examples/portfolio-growth-example.md` - Golden example with constraints.

## Keywords
portfolio strategy, BCG matrix, GE McKinsey, Ansoff, capital allocation, growth sequencing
