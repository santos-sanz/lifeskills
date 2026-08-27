# AI states and recovery patterns

## Core states
- Empty: explain the job, useful input, constraints, and a safe example without pretending the tool understands more than it does.
- Loading or streaming: show progress, latency expectation, stop control, and partial-result boundaries.
- Success: show the result, provenance or basis where available, edit controls, and the next meaningful action.
- Uncertainty: name missing context, confidence limits, alternative interpretations, and the verification step.
- Refusal: explain the safe boundary briefly and offer a lawful, useful alternative when possible.
- Error: preserve user input, explain what failed, offer retry or fallback, and provide escalation for consequential work.

## Recovery checks
- Can the user understand what happened without reading model internals?
- Can they recover without re-entering lost work?
- Is the next action safe, reversible, and clearly owned?
- Does the interface prevent a partial or stale output from being mistaken for final truth?

## Measurement
- Task completion and time to useful result
- Correction, retry, undo, and abandonment rate
- Comprehension and calibrated confidence
- Escalation, harmful-error, accessibility, and support-contact signals
