---
name: anti-ai-tools-user-experience
description: Improve the user experience of AI tools by making capabilities, uncertainty, control, failure recovery, privacy, and outcomes clear. Use for AI product audits, interaction design, onboarding, and workflow improvements.
---

# Anti-AI-Slop User Experience for AI Tools

Use $ARGUMENTS as initial context.

## When to use this skill
- An AI tool feels confusing, generic, unpredictable, slow, opaque, or hard to correct.
- A team needs to design or audit AI interactions, onboarding, outputs, controls, or failure states.
- Users need better trust calibration, verification, editing, recovery, accessibility, or control.

## When not to use this skill
- Do not use it for visual polish without a defined user task, friction, or outcome.
- Do not optimize engagement by hiding uncertainty, cost, data use, limitations, or meaningful alternatives.
- Do not treat user research, accessibility review, security review, or high-stakes governance as optional copy work.

## Required inputs
- User type, job to be done, context, risk level, and success outcome.
- Current journey, product states, interaction constraints, and known failure evidence.
- Model capabilities, latency, confidence limitations, data use, human review, and escalation paths.
- Accessibility, localization, privacy, safety, and measurement requirements.

## Workflow
1. Define the user's task, desired outcome, cost of failure, and success signal.
2. Map the journey and mental model across entry, input, generation, review, action, and follow-up.
3. Inventory states: empty, loading, streaming, partial, success, uncertainty, refusal, error, correction, undo, and escalation.
4. Design affordances for control, verification, editing, provenance, privacy, and recovery at the moment they are needed.
5. Rewrite AI-facing copy to be specific, calm, and useful; remove generic promises and anthropomorphic overclaiming.
6. Test novice, expert, skeptical, accessibility, and high-risk scenarios with realistic failure cases.
7. Instrument completion, correction, abandonment, trust calibration, escalation, latency, and harmful-error signals.

## Ask-first questions
Ask up to 3 questions before auditing or designing:
1. What user task and outcome should improve, and how is success measured today?
2. Which AI behavior, product state, or user failure creates the most friction or risk?
3. What constraints govern data use, accessibility, human review, latency, and reversibility?

## Assumption policy
- Separate observed user evidence from design hypotheses and implementation assumptions.
- Never infer trust or usability from engagement alone; pair it with correction, comprehension, and outcome signals.
- If model behavior is unknown, label it and propose a test rather than promising reliability.
- State when the recommendation requires user research, accessibility, security, privacy, or domain review.

## Output contract
Always produce these sections in order:
1. User and context
2. Job and success criteria
3. Journey and friction map
4. Interaction and state design
5. Copy and affordance proposals
6. Safety, trust, and accessibility checks
7. Measurement and experiment
8. Next actions
9. Assumptions
- Make model uncertainty, data use, user control, and recovery visible where relevant.
- Every next action includes an owner, due date, and success signal.
- State the condition that triggers re-testing, escalation, or a change of approach.

## Guardrails
- Never imply model certainty, human judgment, memory, or capability that the system does not have.
- Make AI involvement, data use, cost, limitations, and meaningful user choices clear at the decision point.
- Provide correction, edit, undo, retry, refusal, and escalation paths for consequential interactions.
- Do not use dark patterns, fake empathy, hidden automation, or engagement pressure to compensate for weak utility.
- Test keyboard, screen-reader, contrast, localization, cognitive load, and low-bandwidth experiences.
- Route privacy, security, safety, legal, and high-stakes domain risks to the appropriate review authority.

## Handoffs
- Use `research-evidence-synthesis` when the audit lacks user evidence or current domain evidence.
- Use `decision-analysis-under-uncertainty` when product teams must choose among risky experience or model trade-offs.
- Use `anti-ai-slop-content-creation` for substantial user-facing copy that needs voice and specificity beyond interface labels.
- Use `pyramid-principle-structured-communication` for an executive product decision memo.

## Resources
- `references/ai-ux-principles.md` - Trust calibration, control, transparency, accessibility, and user outcome principles.
- `references/states-and-recovery.md` - AI interaction states, failure recovery, and escalation patterns.
- `templates/ai-tool-ux-audit.md` - AI tool experience audit and improvement template.
- `examples/ai-tool-ux-audit-example.md` - Golden example with state design, copy, and measurement.

## Keywords
AI UX, AI product design, user experience, trust calibration, human control, explainability, recovery, accessibility, AI tools, usability audit
