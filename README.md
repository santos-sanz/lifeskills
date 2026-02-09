# Lifeskills

A curated collection of non-coding skills for AI agents, focusing on high-impact soft skills such as negotiation, persuasion, structured communication, and consulting frameworks. These skills follow the standard Agent Skills format and are designed to enhance agent capabilities in business and interpersonal contexts.

**Language:** English

## Available Skills

### Negotiation & Influence

#### [negotiation-voss-tactical-empathy](skills/negotiation-voss-tactical-empathy)
Implements Chris Voss's "Never Split the Difference" tactical empathy framework.
*   **Best for:** Salary negotiations, vendor contracts, high-stakes discussions.
*   **Key Capabilities:** Mirroring, labeling, calibrated questions, and handling objections.

#### [persuasion-cialdini-influence-design](skills/persuasion-cialdini-influence-design)
Leverages Robert Cialdini's 6 Principles of Persuasion.
*   **Best for:** Marketing copy, pitch decks, persuasive emails, and landing pages.
*   **Key Capabilities:** Integrating Reciprocity, Scarcity, Authority, Consistency, Liking, and Social Proof.

### Structured Communication

#### [pyramid-principle-structured-communication](skills/pyramid-principle-structured-communication)
Applies Barbara Minto's Pyramid Principle for top-down communication.
*   **Best for:** Executive summaries, leadership memos, and strategy presentations.
*   **Key Capabilities:** Structuring arguments from conclusion to supporting details.

### Mindset & Personal Strategy

#### [luffy-mindset](skills/luffy-mindset)
Applies an audacious, practical "Luffy Mindset" for bold execution plans when explicitly requested.
*   **Best for:** Breaking hesitation, pursuing ambitious goals, and converting fear into action.
*   **Key Capabilities:** Fearless reframing, 3-7 step action planning, risk countermoves, and 24-hour commitment starts.

### Consulting Frameworks

#### [consulting-issue-tree-mece](skills/consulting-issue-tree-mece)
Constructs MECE (Mutually Exclusive, Collectively Exhaustive) issue trees.
*   **Best for:** Problem structuring, root cause analysis, and scoping projects.
*   **Key Capabilities:** Breaking down complex problems into manageable components.

#### [consulting-hypothesis-driven-80-20](skills/consulting-hypothesis-driven-80-20)
Focuses on hypothesis-driven analysis and the Pareto Principle (80/20 rule).
*   **Best for:** Rapid problem solving, prioritizing high-impact workstreams.
*   **Key Capabilities:** formulating testable hypotheses and prioritizing analysis.

#### [consulting-market-competition-analysis](skills/consulting-market-competition-analysis)
Provides tools for market sizing and competitive landscape mapping.
*   **Best for:** Market entry strategies, product positioning, and competitive intelligence.
*   **Key Capabilities:** TAM/SAM/SOM analysis, Porter's Five Forces.

#### [consulting-portfolio-growth-strategy](skills/consulting-portfolio-growth-strategy)
Frameworks for portfolio management and growth strategy.
*   **Best for:** Strategic planning, resource allocation, and M&A evaluation.
*   **Key Capabilities:** BCG Matrix, GE-McKinsey Matrix, Ansoff Matrix.

## Installation

To add these skills to your agent's repertoire:

```bash
npx skills add https://github.com/santos-sanz/lifeskills
```

## Usage

Once installed, these skills are automatically available to the agent. You can invoke them explicitly or rely on the agent's intent detection.

**Examples:**

*   *"Help me negotiate a vendor renewal for 2026 using tactical empathy."*
*   *"Draft a persuasive email to the CFO using Cialdini's principles."*
*   *"Create a MECE issue tree to analyze why user retention is dropping."*

## Repository Structure

Each skill is self-contained within the `skills/` directory:

```
skills/
  <skill-name>/
    SKILL.md       # Core instructions and metadata
    references/    # Framework guides, checklists, and heuristics
    templates/     # Markdown templates for structured output
    examples/      # Few-shot examples to guide the agent
```
