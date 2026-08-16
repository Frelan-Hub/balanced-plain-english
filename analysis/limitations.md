# Limitations

Read this before citing anything from this repository.

## The short version

The evidence is **controlled qualitative evidence**, not a benchmark. It is one unblinded rater's
judgment, one run per condition, eight scenarios, one domain, one model family, no token counts.

It supports a directional conclusion. It does not support a number.

## What the tests do not establish

- statistical significance
- behavior across every coding domain
- behavior across very long contexts
- behavior under conflicting instructions
- behavior across all Claude model variants
- production-scale agent execution
- long-running autonomous workflows

## What must never be claimed

Until quantitative measurements exist, this repository does not claim, and no one citing it should
claim:

- a verified percentage reduction in output tokens
- verified cost reduction
- verified context-window savings
- statistically significant performance improvement
- universal improvement across Claude models
- universal improvement across all tasks

The 5–10% figure that appears in [token-efficiency.md](token-efficiency.md) is an engineering
estimate of *potential* unnecessary-output reduction. It is not a measured Claude token reduction
and must not be presented as one.

## Specific methodological weaknesses

### Single unblinded rater who authored the standard

The largest weakness. The person judging whether ON responses were clearer is the person who wrote
the rule set and expected them to be. Expectation bias is uncontrolled.

Mitigation applied: negative results were recorded rather than dropped — the omitted output sections
in scenario 6 and the two over-strong inferences in scenario 8. That is evidence of a genuine
attempt at honesty, not a substitute for blinding.

### One run per condition

Model output varies between runs on identical input. With a single sample per cell, treatment effect
and run-to-run variance cannot be separated. Some portion of every observed difference may be noise.

### Three of eight scenarios support comparison

Only scenarios 6, 7, and 8 have paired ON/OFF Claude responses. Scenarios 1, 3, 4, and 5 have a
single condition, and scenario 2 has no Claude evidence. Every comparative claim rests on three
scenarios.

### Narrow domain

All scenarios are Python backend engineering: data processing, CSV import, incident analysis. The
standard is written for general technical communication. Nothing here tests it on frontend work,
infrastructure, data science, documentation, or non-engineering tasks.

### Weak instrument

Claude's baseline already exhibits much of the target behavior — concise explanation, ambiguity
detection, architecture restraint. A treatment applied to a subject already near the target produces
a small measurable difference regardless of whether the treatment works.

This cuts both ways, and both directions should be stated:

- It explains why the observed effect is small without implying the standard is ineffective.
- It equally means these results **cannot** demonstrate that the standard is effective, because a
  small difference is exactly what a null effect would also produce.

Distinguishing those two requires a model with a more verbose baseline. That is
[experiments/02](../experiments/02-cross-model.md).

### No token measurement

The efficiency argument is entirely design-level. No input, output, or total token counts were
collected in any run. This is the single most fixable gap; see
[experiments/01](../experiments/01-token-efficiency.md).

### Prompt text not preserved for the three strongest scenarios

Scenarios 6, 7, and 8 — the only paired ones — have their specifications preserved but not their
verbatim prompt text. A rerun can reproduce them in substance but not byte-for-byte, which weakens
strict comparability against future evidence.

## What the evidence does support

Stated at the strength it actually has:

For Claude, on eight engineering scenarios, judged by one unblinded rater: enabling the standard was
associated with less unnecessary communication overhead, and was **not** associated with any
observed loss of correctness, edge-case handling, technical distinction, security reasoning, or
architectural restraint.

The second half is the load-bearing part. The main risk of a plain-language instruction is that it
degrades engineering quality. Across these scenarios, it did not.

That is a reasonable basis for continued use. It is not a basis for a performance claim.

## Honest summary of confidence

| Claim | Confidence | Why |
|---|---|---|
| The standard does not degrade engineering quality | Moderate | Directly probed by scenarios designed to expose it; consistent across all runs |
| The standard reduces communication overhead | Low to moderate | Consistent qualitative signal; unblinded, three paired comparisons |
| The standard reduces token usage | None | Not measured |
| The standard reduces follow-up turns | None | Not tested |
| The standard transfers across models | None (design argument only) | No cross-model runs |
