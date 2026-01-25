# Lifeskills

Non-coding skills for AI agents. This repo focuses on negotiation, persuasion, and consulting analysis frameworks. Skills follow the Agent Skills format and are written in English.

## Available Skills

### negotiation-voss-tactical-empathy
Tactical empathy negotiation based on Chris Voss.

Use when:
- Preparing salary, vendor, or contract negotiations
- Handling objections, anchors, or stalled conversations
- Building talk tracks, concessions, and closing plans

### persuasion-cialdini-influence-design
Ethical persuasion using Cialdini principles.

Use when:
- Writing persuasive emails, landing pages, or decks
- Creating proposals, pitches, or internal change messages
- Designing campaigns that need social proof or authority

### pyramid-principle-structured-communication
Structured communication using the Pyramid Principle.

Use when:
- Writing executive summaries or leadership updates
- Building a storyline for a presentation or memo
- Turning analysis into a clear recommendation

### consulting-issue-tree-mece
MECE issue trees and problem structuring.

Use when:
- Breaking down complex problems into drivers
- Building root cause trees or analysis plans
- Scoping consulting workstreams

### consulting-hypothesis-driven-80-20
Hypothesis-driven analysis with 80/20 prioritization.

Use when:
- Structuring analysis around testable hypotheses
- Prioritizing work by impact and speed to learn
- Building evidence plans and workstreams

### consulting-market-competition-analysis
Market sizing and competitive landscape analysis.

Use when:
- Defining market boundaries, segments, and sizing
- Mapping competitors and positioning
- Evaluating market entry or expansion options

### consulting-portfolio-growth-strategy
Portfolio review and growth strategy frameworks.

Use when:
- Allocating resources across business units
- Evaluating portfolio attractiveness and position
- Identifying and sequencing growth moves

## Installation

Install all skills from this repo:

```bash
npx skills add https://github.com/santos-sanz/lifeskills
```

## Usage

Skills are automatically available once installed. Invoke them directly or let the agent detect the right skill.

Examples:

```text
/negotiation-voss-tactical-empathy vendor renewal for 2026
```

```text
Design a persuasive proposal for CFO approval
```

```text
Build an issue tree for declining retention
```

## Skill Structure

Each skill lives in `skills/<skill-name>/` and includes:

- `SKILL.md` - Instructions and metadata
- `references/` - Frameworks, checklists, and guidance
- `templates/` - Structured output formats
- `examples/` - Sample outputs

## Repository Layout

```
skills/
  <skill-name>/
    SKILL.md
    references/
    templates/
    examples/
```
