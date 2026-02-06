# Example: profitability decline with incomplete diagnostics

## Context
- Problem statement: Operating profit dropped 13 percent quarter-over-quarter.
- Metric and baseline: Margin moved from 21 percent to 17 percent in two quarters.
- Scope boundaries: North America B2B segment, excluding new acquisitions.
- Decision deadline: CFO review in 10 days.

## Decision or recommendation
- Decision this tree informs: Where to focus the first two analytical workstreams to recover margin within the next quarter.
- Recommended focus branches: Net price realization, service delivery cost, and enterprise retention.
- Why these branches first: They combine high impact with available early indicators.

## Analysis
### Tree type and rationale
- Tree type: Driver.
- Selection rationale: Profit decline requires decomposition into revenue and cost drivers before options are compared.

### Issue tree (ASCII)
Profit decline
|- Revenue deterioration
|  |- Price realization
|  |- Volume
|     |- New logos
|     |- Retention
|- Cost inflation
   |- Delivery labor cost
   |- Cloud infrastructure cost
   |- Support rework cost

### MECE validation
- Overlap check passed: Yes. Price and volume separated; no duplicated metrics.
- Exhaustiveness check passed: Yes for in-scope profit drivers; taxes and one-off items marked out-of-scope.
- Level consistency check passed: Yes. All second-level branches are drivers, not actions.

### Branch prioritization
- Price realization (5, 4, 4): contract-level data available and immediate margin effect.
- Delivery labor cost (4, 4, 3): timesheet variance suggests controllable leakage.
- Retention (4, 3, 3): potential high impact but slower validation cycle.

## Risks
- Risk: misclassifying one-off discount campaign effects as structural pricing issue.
- Mitigation: isolate campaign cohort before drawing conclusions.
- Risk: cost branch misses hidden vendor surcharge clauses.
- Mitigation: include procurement contract audit in first sprint.

## Next actions
- Analysis task: Build net price waterfall by segment and channel.
- Owner: Pricing lead.
- Date: March 11.
- Success signal: Identify at least 2 points of recoverable margin.

## Assumptions
- Assumption: Revenue recognition timing did not materially distort quarter comparison.
- Confidence (high/medium/low): Medium.
- Validation needed: Finance reconciliation with controller team.
