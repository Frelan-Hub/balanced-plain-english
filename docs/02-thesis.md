# Thesis

## Statement

> Balanced Plain English is not a "shorter answers" rule.
>
> It is a quality-preserving communication and semantic-compression standard:
> **complete the required work first, then remove unnecessary communication overhead.**
>
> Plain language applies to expression, not to the removal of technical correctness, necessary
> complexity, uncertainty, edge cases, or explicit requirements.

## The two operations, in order

The standard describes a sequence, not a single instruction. The order is the whole design.

```text
1. Complete the required substance
   requirements, constraints, requested outputs, acceptance criteria,
   edge cases, uncertainty, technical distinctions

2. Then compress the expression
   remove restatement, filler, redundant conclusions, unnecessary caveats,
   narration, invented frameworks, jargon that adds no precision
```

Running these in the wrong order produces the failure this project exists to avoid. Compression
applied before completion removes substance, because substance is harder to state compactly than
filler is.

The standard encodes the order explicitly:

- *"Fulfill all explicit requirements, constraints, requested outputs, and acceptance criteria
  before optimizing for brevity."*
- *"When a task is complex, reduce unnecessary wording and repetition only after the required
  substance is complete."*

## What is being compressed

Semantic compression targets the parts of a response that carry no decision-relevant information:

| Compressed | Preserved |
|---|---|
| Restating the question | The answer |
| Repeating the conclusion | The conclusion, stated once |
| Introductory framing | Requirements and constraints |
| Narration of routine work | Findings that change the plan |
| Caveats that change no decision | Uncertainty that changes a decision |
| Jargon where ordinary English is equally precise | Technical terms that add precision |
| The same reasoning in three forms | Edge cases and failure modes |
| Invented frameworks and labels | Justified complexity |

The optimization target is the ratio of the right column to total length. Neither column's absolute
size is the goal.

## Why "plain" does not mean "simplified"

Plain English is a property of *expression*. Simplification is an operation on *content*. The
standard permits the first and forbids the second where content is load-bearing:

> Plain language applies to communication and presentation, not to engineering correctness.
>
> Do not simplify away requirements, constraints, edge cases, uncertainty, technical distinctions,
> or necessary complexity merely because they are difficult to explain.

A hard technical distinction stated in ordinary words is compliant. The same distinction dropped
because it was awkward to phrase is a violation, regardless of how clean the result reads.

This is why the standard also says *"do not dumb down technical ideas"* immediately after *"make
complex ideas easier to understand."* Those two sentences are the whole boundary.

## Layer separation

The thesis holds only because the standard stays inside one layer and refuses the others.

| Layer | Optimizes | Canonical file in the author's system |
|---|---|---|
| Communication standard | Expression | `balanced-plain-english.md` |
| Engineering conventions | Implementation quality | `CONVENTIONS.md` |
| Governance | Architecture and change | `GOVERNANCE.md`, `PRINCIPLES.md` |
| Execution and validation | Completion and correctness | Execution mechanisms, tests, verification |

Each layer answers a different question:

```text
Communication  → Is this expressed with the least overhead that preserves meaning?
Conventions    → Is this the right implementation?
Governance     → Is this change permitted, justified, and minimally sufficient?
Execution      → Did it actually happen, and is it correct?
```

A defect belongs to the layer that owns its question. The validation record contains a direct
example: in one stress test the model omitted explicitly requested output sections. That is an
execution-completeness defect. Fixing it by adding rules to the communication standard would have
made the standard longer, less portable, and quietly turned it into an engineering-control policy.

The boundary is stated as a rule in [03-scope-boundaries.md](03-scope-boundaries.md).

## Why this is worth having as a standard

A communication contract that survives model replacement is worth more than a marginally better
prompt. The standard is plain Markdown with no vendor syntax, no tool calls, and no assumptions
about a specific runtime. That is a deliberate design property, not an accident of formatting: it
is what allows one document to be installed globally, invoked selectively as a skill, or pasted
into a different vendor's system prompt without rewriting.

The goal is not to make every model behave identically. It is:

> A common communication contract that remains useful across replaceable models without becoming a
> hidden engineering-control layer.

## Relationship to the architectural principle

The standard is an instance of the author's governing principle — **L/T/E/E/F-Agnostic** (Lean,
Thin, Efficient, Effective, Flexible, Agnostic) — applied to communication rather than to systems:

| Property | How the standard satisfies it |
|---|---|
| Lean | One page, no ceremony, no configuration |
| Thin | One responsibility; explicitly refuses the adjacent ones |
| Efficient | Optimizes useful information per token of context and output |
| Effective | Judged on verified communication outcomes, not elegance |
| Flexible | Frozen but replaceable; version-pinned to its evidence |
| Agnostic | No vendor, model, CLI, or runtime dependency |

The same principle also constrains this repository: evidence before rules, and no claim beyond what
the evidence supports.
