# 80/20 prioritization for hypothesis portfolios

## Objective
Concentrate effort on the smallest set of hypotheses most likely to drive the decision.

## Scoring model
- Impact (1-5): expected value if true.
- Confidence (1-5): credibility of current evidence.
- Effort (1-5): resources required to test.
- Speed (1-5): time to reliable signal.
- Priority score: (Impact x Confidence) / (Effort x Speed)
- Tie-breaker: data availability and reversibility of action.

## Default weighting option
If custom weighting is needed:
- Impact 50 percent
- Confidence 25 percent
- Effort 15 percent
- Speed 10 percent

## Sequencing logic
1. Test top 1 hypothesis first when decision cycle is short.
2. Run top 2 in parallel only if teams and data paths are independent.
3. Pause all low-score hypotheses until checkpoint review.

## Kill criteria discipline
- Define threshold before test starts.
- Stop or redesign tests when threshold is crossed.
- Document why a hypothesis was killed to avoid repeated work.

## Practical checklist
- Is the top hypothesis both high impact and fast to learn?
- Is there a fallback if top hypothesis is disproven?
- Are owners and deadlines explicit for each test?
