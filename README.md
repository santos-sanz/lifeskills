# Lifeskills

A curated collection of non-coding skills for AI agents focused on business-critical research, communication, strategy, execution, negotiation, and influence.

The skills use explicit activation boundaries, decision-ready output contracts, evidence labels, and practical guardrails. Skill content is written in English for compatibility with the agent-skills ecosystem.

## Skills included

### Research and decisions

#### [research-evidence-synthesis](skills/research-evidence-synthesis)
Source-backed research with claim ledgers, freshness checks, conflict reconciliation, citations, and uncertainty-aware synthesis.

#### [decision-analysis-under-uncertainty](skills/decision-analysis-under-uncertainty)
Transparent option comparison using criteria, weights, scenarios, reversibility, risk, and decision triggers.

### Structured communication and influence

#### [pyramid-principle-structured-communication](skills/pyramid-principle-structured-communication)
Answer-first executive storytelling for board updates, recommendations, decision memos, and storyline-driven communication.

#### [persuasion-cialdini-influence-design](skills/persuasion-cialdini-influence-design)
Ethical persuasion design using principle-to-evidence-to-claim traceability and transparent calls to action.

#### [difficult-conversations-feedback](skills/difficult-conversations-feedback)
Specific, respectful preparation for feedback, conflict repair, boundaries, performance concerns, and relationship reset.

#### [negotiation-voss-tactical-empathy](skills/negotiation-voss-tactical-empathy)
Negotiation planning with tactical empathy, strategy-script separation, BATNA/ZOPA framing, and reciprocal concessions.

### Leadership and execution

#### [high-agency](skills/high-agency)
Rapid action under uncertainty with specific constraints, three options, ownership, feedback loops, and 24–72 hour plans.

#### [execution-operating-system](skills/execution-operating-system)
Multi-week operating cadence with workstreams, critical path, capacity, dependencies, metrics, review gates, and escalation.

#### [luffy-mindset](skills/luffy-mindset)
An audacious but reality-grounded action plan, activated only when the user explicitly requests the Luffy style.

### Consulting frameworks

#### [consulting-issue-tree-mece](skills/consulting-issue-tree-mece)
MECE issue-tree decomposition with formal validation gates and a prioritized analysis backlog.

#### [consulting-hypothesis-driven-80-20](skills/consulting-hypothesis-driven-80-20)
Falsifiable hypotheses, disconfirming signals, kill criteria, and 80/20 test prioritization.

#### [consulting-market-competition-analysis](skills/consulting-market-competition-analysis)
TAM/SAM/SOM triangulation, competitor and substitute mapping, source freshness, and scenario-aware implications.

#### [consulting-portfolio-growth-strategy](skills/consulting-portfolio-growth-strategy)
Portfolio allocation and growth sequencing using explicit scoring, sensitivity, capacity, and dependency checks.

## Routing and composition

Choose the skill that matches the primary job to be done, then hand off when the output changes type:

| Starting need | First skill | Typical next handoff |
| --- | --- | --- |
| Gather and verify external evidence | `research-evidence-synthesis` | Market analysis, decision analysis, or pyramid communication |
| Diagnose a complex problem | `consulting-issue-tree-mece` | Hypothesis-driven testing or decision analysis |
| Test the most important explanations | `consulting-hypothesis-driven-80-20` | Execution operating system or decision analysis |
| Compare consequential options | `decision-analysis-under-uncertainty` | High-agency, execution operating system, or pyramid communication |
| Allocate resources across units | `consulting-portfolio-growth-strategy` | Execution operating system |
| Unblock a 24–72 hour execution constraint | `high-agency` | Execution operating system or pyramid communication |
| Run a multi-week initiative | `execution-operating-system` | Pyramid communication for progress reporting |
| Prepare a conversation with behavior change or boundaries | `difficult-conversations-feedback` | Negotiation only if terms are exchanged |
| Prepare a negotiation with reciprocal terms | `negotiation-voss-tactical-empathy` | Pyramid communication or decision analysis |
| Draft an executive decision message | `pyramid-principle-structured-communication` | Final presentation layer |
| Draft influence messaging with proof | `persuasion-cialdini-influence-design` | Research first if proof is unverified |
| Request an explicitly Luffy-style motivational plan | `luffy-mindset` | High-agency or execution operating system if style is not requested |

## Shared output contract

Decision-oriented skills use a consistent contract where appropriate:

1. Context
2. Decision or Recommendation
3. Analysis
4. Risks
5. Next Actions
6. Assumptions

Specialized skills use their canonical templates. All skills must:

- distinguish Fact, Inference, Assumption, and Unknown;
- state confidence and validation needs when evidence is incomplete;
- include owner, due date, and success signal for actions;
- cite external claims with source and date, or mark them unverified;
- state material risks and the condition that would change the recommendation.

## Quality system

The repository includes a deterministic contract benchmark and a manual response-evaluation protocol:

- `quality/rubric.md`: common scoring rubric from 1–5.
- `quality/test-prompts.md`: 4 test prompts per skill (52 total).
- `quality/benchmark-manifest.json`: required sections, guardrails, and handoffs for every skill.
- `quality/eval-log-template.md`: manual evaluation log with model, commit, and rubric fields.
- `scripts/lint_skills.py`: structure, resource, catalog, and prompt coverage gate.
- `scripts/validate_benchmark.py`: deterministic benchmark-contract validator.

Target acceptance thresholds:

- Per-skill average >= 4.2.
- No criterion below 3.5.
- Zero critical guardrail failures.

The deterministic benchmark never calls an external model or requires credentials. Generated responses are evaluated manually against the rubric and recorded with the model, date, evaluator, and commit.

## Validation workflow

```bash
python scripts/lint_skills.py
python3 scripts/validate_benchmark.py
python3 -m unittest discover -s tests -v
```

Run all three checks after a skill edit. Fix every reported issue before opening a pull request.

## Installation

```bash
npx skills add https://github.com/santos-sanz/lifeskills
```

Once installed, these skills are automatically available to the agent. They can be invoked explicitly or selected from the user's intent when the activation boundary matches.

## Repository structure

```text
skills/
  <skill-name>/
    SKILL.md
    references/
    templates/
    examples/
scripts/
  lint_skills.py
  validate_benchmark.py
quality/
  benchmark-manifest.json
  rubric.md
  test-prompts.md
  eval-log-template.md
tests/
  test_validate_benchmark.py
```

## Versioning and attribution

The V2 contract is maintained as a backward-compatible content standard: existing skill directory names remain stable, while new headings and quality checks are additive. Framework source pointers and adaptation notes are documented in [`quality/framework-sources.md`](quality/framework-sources.md).
