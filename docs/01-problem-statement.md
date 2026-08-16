# Problem Statement

## The observed problem

AI coding assistants can produce output that is technically correct and still costly to use.

The recurring failure is not wrong information. It is unnecessary communication overhead around
correct information:

- restating the question before answering it
- repeating the conclusion in a summary that adds nothing
- introductory framing that carries no content
- narrating routine work step by step
- caveats that do not change any decision
- jargon where ordinary English is equally precise
- explaining obvious code line by line
- expressing the same reasoning two or three times in different forms
- turning a simple idea into a named framework with categories and labels

Each item is individually minor. Together they lower the useful information per unit of reading
effort, and per token.

## Why "be concise" fails

The intuitive correction is an instruction to be brief, or a word or sentence limit.

This trades one defect for a worse one. Brevity pressure removes whatever is hardest to state
compactly, and in engineering work the hardest things to state compactly are usually the ones that
matter most:

| Removed under brevity pressure | Consequence |
|---|---|
| Edge cases | Silent failure in production |
| Uncertainty and unknowns | False confidence, wrong decisions |
| Explicit requirements from the prompt | Incomplete work reported as complete |
| Technical distinctions | Wrong mental model carried forward |
| Justified complexity | Under-designed system |
| Assumptions made to fill a spec gap | Undetected behavior invented by the model |

A shorter response that omits a required element is not an improvement. It is a defect with a
smaller footprint, which makes it harder to notice.

## The real objective

The target is not response length in either direction.

> Maximize useful information density while preserving correctness, completeness, technical
> nuance, engineering judgment, explicit requirements, and necessary complexity.

Two responses can be the same length and differ substantially in how much of that length does
work. The optimization target is the ratio, not the numerator or the denominator alone.

## Why this needs a standard rather than a prompt

Ad-hoc instructions in individual prompts have three problems:

1. They are re-typed, so they drift. The rule is slightly different every time.
2. They are not evaluable. There is no fixed text to run an A/B test against.
3. They are vendor-shaped. An instruction written for one tool's prompt format does not transfer.

A single fixed document solves all three. It can be versioned, frozen, tested ON and OFF against
identical prompts, and installed into any system that accepts a system prompt or instruction file.

## Scope of the problem being solved

In scope:

- how a correct answer is expressed
- what is included, omitted, ordered, and emphasized
- when to ask rather than assume
- how uncertainty is presented

Out of scope, deliberately:

- whether the engineering answer is correct
- whether the architecture is appropriate
- whether the task was actually completed
- whether tests ran and files were written

Those belong to other layers. See [03-scope-boundaries.md](03-scope-boundaries.md). Solving them
here would produce a document that is longer, less portable, and no longer a communication
standard.
