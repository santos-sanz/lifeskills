# Issue tree patterns and branch design

## Choosing the right tree type
- Driver tree: best for diagnosing metric movement.
- Process tree: best for operational bottlenecks.
- Option tree: best for comparing strategic choices.
- Hypothesis tree: best for rapid test-and-learn cycles.

## Driver tree starter formulas
- Profit = Revenue - Cost
- Revenue = Price x Volume
- Volume = New customers + Expansion - Churn
- Cost = Fixed + Variable + Failure cost

## Process tree pattern
- Input quality -> Throughput -> Output quality -> Rework -> Cost/time impact

## Option tree pattern
- Option A, B, C
- Under each option: value upside, implementation effort, execution risk

## Branch design rules
- Keep sibling branches at the same abstraction level.
- Use nouns for branches, not action verbs.
- Ensure branches are mutually exclusive before adding child nodes.
- Avoid premature detail; keep depth proportional to decision urgency.

## Prioritization heuristic
- Score branches 1-5 on impact, controllability, and speed to evidence.
- Prioritize branches with highest weighted combination.
- Default weight set: impact 0.5, controllability 0.3, speed 0.2.

## Translation to analysis backlog
For each top branch, define:
- Key question
- Required dataset
- Owner
- Deadline
- Decision signal
