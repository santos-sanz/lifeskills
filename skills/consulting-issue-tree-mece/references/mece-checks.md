# MECE validation gates

Use these gates before finalizing the tree.

## Gate 1: mutual exclusivity
- Test: Could one datapoint belong to more than one sibling branch?
- If yes, branch definitions are overlapping.
- Fix: tighten definitions with explicit inclusion and exclusion rules.

## Gate 2: collective exhaustiveness
- Test: Does the parent metric fully decompose into children?
- If no, missing branch or scope mismatch exists.
- Fix: add missing branch or narrow parent definition.

## Gate 3: level integrity
- Test: Are all siblings drivers, or are some actions/outcomes?
- If mixed, decision logic will break.
- Fix: separate driver layer from action layer.

## Gate 4: clarity
- Test: Would two analysts build the same branch assignment?
- If no, labels are ambiguous.
- Fix: rename branches with measurable definitions.

## Gate 5: usefulness
- Test: Does each priority branch map to a feasible analysis in current timeline?
- If no, tree may be academically correct but operationally weak.
- Fix: collapse or reframe low-actionability branches.

## Failure patterns to avoid
- "Other" as a large unresolved bucket.
- Deep branches with no data path.
- Mixing internal and external drivers without separation.
