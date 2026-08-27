---
name: research-evidence-synthesis
description: Conduct source-backed research and synthesize evidence for decisions, comparisons, and recommendations. Use when claims need current, traceable, uncertainty-aware support.
---

# Research and Evidence Synthesis

Use $ARGUMENTS as initial context.

## When to use this skill
- A decision, recommendation, comparison, or briefing depends on external evidence.
- The user needs current facts, source traceability, or reconciliation of conflicting claims.
- Research must be scoped by geography, date, population, or market definition.

## When not to use this skill
- Do not use it for unsupported brainstorming or opinion generation when no evidence is required.
- Do not use it as a substitute for licensed legal, medical, financial, or safety advice.
- Do not turn a small, already-verified fact lookup into an unnecessarily broad report.

## Required inputs
- Research question and the decision or audience it supports.
- Scope boundaries: geography, population, time period, definitions, and exclusions.
- Required freshness, acceptable source types, and time available.
- Known sources, claims, or disagreements to investigate.

## Workflow
1. Convert the request into one answerable research question and define scope.
2. Create a source plan using primary, authoritative, independent, and contextual sources.
3. Gather a claim ledger with exact source, publication date, access date, method, and limitations.
4. Assess source quality, freshness, independence, and applicability to the question.
5. Reconcile conflicts by comparing definitions, samples, dates, incentives, and methods.
6. Separate facts, inferences, assumptions, and unknowns before synthesizing.
7. Deliver an evidence-backed synthesis, implications, citations, and the smallest useful next research step.

## Ask-first questions
Ask up to 3 questions before researching:
1. What decision or audience must this research support?
2. Which scope, geography, population, and freshness boundary is binding?
3. Which source types are trusted or disallowed?

## Assumption policy
- If scope is incomplete, state a narrow working scope and its confidence.
- Never infer that a source applies outside its population, date, geography, or method.
- Mark missing evidence as Unknown and state the validation path.
- Use confidence labels only with a reason tied to source quality or triangulation.

## Output contract
Always produce these sections in order:
1. Research question and scope
2. Executive synthesis
3. Evidence ledger
4. Conflicts and gaps
5. Implications or recommendation
6. Next actions
7. Sources and freshness
8. Assumptions
- Label material statements as Fact, Inference, Assumption, or Unknown.
- Record source, publication date, access date, and confidence for external claims.
- Every next action includes an owner, due date, and success signal.

## Guardrails
- Never fabricate citations, quotes, sources, dates, or research results.
- Separate facts from inferences and disclose material uncertainty.
- Prefer primary or authoritative sources and triangulate consequential claims.
- Protect personal data and do not expose private information found during research.
- Escalate high-stakes legal, medical, financial, or safety conclusions to an appropriate professional.

## Handoffs
- Use `consulting-market-competition-analysis` when the research is specifically for market sizing or competitor mapping.
- Use `decision-analysis-under-uncertainty` when evidence is sufficient and the main task is choosing among options.
- Use `pyramid-principle-structured-communication` to package the synthesis for executives.
- Use `persuasion-cialdini-influence-design` only after claims and proof points are verified.

## Resources
- `references/evidence-protocol.md` - Claim ledger, source hierarchy, freshness, and conflict resolution.
- `references/research-guardrails.md` - Citation, privacy, browsing, and high-stakes research safeguards.
- `templates/evidence-synthesis.md` - Evidence-led research output template.
- `examples/evidence-synthesis-example.md` - Golden example with traceable claims and gaps.

## Keywords
research, evidence synthesis, source quality, citations, triangulation, fact checking, literature review, uncertainty
