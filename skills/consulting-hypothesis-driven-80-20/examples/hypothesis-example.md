# Example: reduce SMB churn with limited data

## Context
- Governing question: What is the fastest reliable path to reduce SMB monthly churn in the next two quarters?
- Success metric: Monthly logo churn rate.
- Time horizon: Two quarters.
- Decision deadline: VP Product needs plan by next Friday.

## Decision or recommendation
- Recommended top hypothesis to test first: Improving onboarding completion will reduce churn fastest.
- Why it is first (80/20 rationale): Highest expected impact with existing product analytics and short feedback loop.
- Decision checkpoint date: March 22.

## Analysis
### Hypothesis set
1. If first-week onboarding completion increases, then SMB churn decreases, because users reach first value faster.
2. If plan packaging is simplified, then churn decreases, because customers choose plans that match actual usage.
3. If support first-response time drops below four hours, then churn decreases, because unresolved blockers shrink.

### Signal design
- Hypothesis 1 confirming signal: 15 percent lift in activation with lower 30-day churn in matched cohorts.
- Hypothesis 1 disconfirming signal: Activation improves but churn remains unchanged.
- Hypothesis 1 kill threshold: No churn improvement after two onboarding release cycles.
- Hypothesis 2 confirming signal: Fewer downgrade or cancellation reasons tied to pricing confusion.
- Hypothesis 2 disconfirming signal: Plan-switch behavior unchanged after packaging update.
- Hypothesis 2 kill threshold: No movement in churn reason distribution within six weeks.

### 80/20 prioritization
- Scoring model used: (Impact x Confidence) / (Effort x Speed), plus data availability tie-breaker.
- Top 1 score and rationale: Onboarding hypothesis scored highest due to high impact and immediate measurable signal.
- Top 2 score and rationale: Pricing-packaging second due to medium effort and moderate confidence.

## Risks
- Risk: cohort effects distort causality.
- Mitigation: use matched cohorts by acquisition channel and account size.
- Risk: simultaneous product changes mask signal.
- Mitigation: freeze unrelated onboarding experiments during test window.

## Next actions
- Test task: Launch onboarding checkpoint redesign experiment with holdout cohort.
- Owner: Growth PM.
- Date: March 8 launch; March 22 checkpoint.
- Success signal: Churn in test cohort at least 1.2 points lower vs control by checkpoint.

## Assumptions
- Assumption: Current analytics event quality is sufficient to track activation to churn path.
- Confidence (high/medium/low): Medium.
- Validation needed: Data engineering audit of event completeness before experiment start.
