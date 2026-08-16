# Experiment 01 — Token Efficiency

**Status:** not run.
**Priority:** highest. This closes the largest gap in the evidence.

## Question

Does the standard reduce output tokens without reducing correctness, completeness, or technical
precision?

## Why this first

Every efficiency statement in this repository is currently a design argument. Token counts are cheap
to collect, mechanically objective, and would convert the weakest claims in the project into either
a supported result or a refuted one.

Either outcome is useful. A refutation is a real finding: it would mean the standard improves
communication quality without reducing length, which is still worth knowing and would remove a claim
that should not be made.

## Design

Identical prompts, two conditions, standard version 1.1.0.

```text
ON  → balanced-plain-english.md enabled
OFF → balanced-plain-english.md disabled, everything else unchanged
```

Requirements that fix the weaknesses in the original cycle:

| Requirement | Fixes |
|---|---|
| Verbatim prompt text recorded for every scenario | Scenarios 6–8 currently have specifications only |
| Minimum 5 runs per condition per scenario | Separates treatment effect from output variance |
| Quality scored blind to condition | Removes the largest bias in the existing evidence |
| At least 15 scenarios, across more than one domain | Current set is 8, all Python backend |
| Token counts from the platform, not estimated | Estimates would reintroduce judgment |

If blinding a second rater is not possible, blind the condition labels during scoring and record that
the rater was the author. State the compromise rather than omitting it.

## Data to record per run

```text
Input tokens
Output tokens
Total tokens

Correctness
Completeness
Requirement fidelity
Technical precision
Useful information density
Unnecessary-content score
Task completion
```

Use [templates/run-record.md](templates/run-record.md) and
[templates/scoring-rubric.md](templates/scoring-rubric.md).

## Analysis

```text
Raw Output Reduction %
=
(OFF output tokens − ON output tokens)
÷ OFF output tokens
× 100
```

Report the distribution, not only the mean. With 5+ runs per cell, report median and range. A mean
difference smaller than the within-condition spread is not a result.

Then apply the quality gate. A run where the ON response fails correctness, completeness, or
requirement fidelity is **excluded from the efficiency comparison and reported separately as a
quality failure**. Token savings from a response that dropped a requirement are not savings.

## Success and failure conditions

Fixed in advance. This is the part that makes the experiment falsifiable.

**Success:**

```text
ON
↓
fewer unnecessary tokens
+
same or better correctness
+
same or better completeness
+
same or better technical precision
```

**Failure, regardless of the size of the reduction:**

```text
ON
↓
20% fewer tokens
+
missing requirements
```

**Null result:** no meaningful token difference with quality preserved. This would refute the
efficiency hypothesis while leaving the communication-quality findings intact, and it must be
reported as plainly as a positive result would be.

> Token reduction is subordinate to engineering and communication quality.

## What a positive result would and would not license

Would license: a stated measured reduction, for the tested model, scenarios, and standard version,
with the distribution shown.

Would not license: a cost-saving claim, a context-window claim, extrapolation to other models, or
extrapolation to task types not tested.

## Practical note on input tokens

The standard itself consumes input tokens in every ON request — roughly one page of Markdown. A
complete efficiency assessment must account for this: an output reduction that is smaller than the
recurring input cost of the standard is a net loss on short exchanges, even if the output-only
comparison looks favorable.

Report input, output, and total separately for this reason. Total tokens is the honest headline
number for single-turn tasks.
