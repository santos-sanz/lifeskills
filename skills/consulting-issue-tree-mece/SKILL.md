---
name: consulting-issue-tree-mece
description: Build MECE issue trees for complex business problems. Use when you need rigorous problem decomposition, branch prioritization, and a decision-ready analysis backlog.
---

# MECE Issue Tree

Use $ARGUMENTS as initial context.

## When to use this skill
- Diagnosing root causes in performance decline or execution failures.
- Structuring strategic questions into mutually exclusive branches.
- Creating a prioritized analysis plan before data deep-dives.
- Aligning teams on problem scope and ownership.

## When not to use this skill
- Do not use it as a final recommendation, market forecast, or execution plan.
- Do not use it when the problem is already structured and only a falsifiable test plan is missing.

## Required inputs
- Problem statement, metric, and baseline.
- Scope boundaries (segment, geography, time horizon).
- Available data and decision deadline.
- Metric definition, numerator/denominator, units, and known exclusions.

## Workflow
1. Convert the request into one decision-oriented problem statement.
2. Select tree type: driver, process, option, or hypothesis tree.
3. Build 2-3 levels of MECE branches with parallel labels.
4. Run formal checks for overlap, gaps, level-mixing, units, and parent-child reconciliation.
5. Prioritize branches by impact, controllability, and learning speed.
6. Translate top branches into an analysis backlog with owners and timing.

## Ask-first questions
Ask up to 3 questions before building the tree:
1. Which metric and baseline define the problem severity?
2. What scope is explicitly in or out?
3. What decision must this tree support?

## Assumption policy
- Proceed if data is incomplete, but list assumptions in a dedicated section.
- Tag assumptions with confidence and validation path.
- Do not invent branch evidence; flag unknowns explicitly.
- State whether the tree is a driver, process, option, or hypothesis structure and why.

## Output contract
Always produce these sections in order:
1. Context
2. Decision or Recommendation
3. Analysis
4. Risks
5. Next Actions
6. Assumptions
- Every backlog item includes an owner, due date, required dataset, and success signal.
- Label evidence as Fact, Inference, Assumption, or Unknown.

## Guardrails
- No branch overlap at the same level.
- No mixing causes and outcomes in one branch layer.
- No "other" bucket unless unavoidable and quantified.
- Keep branch naming at equivalent abstraction depth.
- Do not mix causes, outcomes, actions, and metrics at the same branch level.

## Handoffs
- Use `consulting-hypothesis-driven-80-20` when the top branches need falsifiable tests and kill criteria.
- Use `decision-analysis-under-uncertainty` when the tree must become an explicit option decision.
- Use `pyramid-principle-structured-communication` for the final executive storyline.

## Resources
- `references/issue-tree-patterns.md` - Tree patterns and branch design rules.
- `references/mece-checks.md` - Validation gates and failure diagnostics.
- `templates/issue-tree.md` - Decision-ready tree template.
- `examples/issue-tree-example.md` - Golden example with partial information.

## Keywords
issue tree, MECE, root cause, problem structuring, analysis backlog, driver tree
