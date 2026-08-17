# Experiment 01 — Token Efficiency

**Status: RUN.** Executed as the
[v2 Token Efficiency Benchmark](../evidence/claude/benchmark-v2/README.md) on Claude Opus 5.

**Result:** 50.45% aggregate output-token reduction across 20 paired scenarios, 19/20 runs positive,
no material quality difference detected, 40/40 task completions. The pre-registered success
condition was met; the failure condition was not triggered.

This document is preserved as the **pre-registration**. It was written before the benchmark ran and
is not edited to match what happened — that is the point of writing it first. Deviations between what
it specified and what was delivered are recorded in
[Deviations](#deviations-from-this-protocol-as-executed) below and in the
[benchmark report](../evidence/claude/benchmark-v2/README.md#deviations-from-the-pre-registered-protocol).

---

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

---

## Deviations from this protocol, as executed

Recorded rather than quietly dropped. The benchmark met some pre-registered requirements and missed
others.

| This protocol required | v2 delivered | Effect |
|---|---|---|
| Minimum 5 runs per condition per scenario | 1 | Run variance not separated from treatment effect |
| At least 15 scenarios, more than one domain | 20 scenarios, 20 domains | **Met**, exceeded on breadth |
| Quality scored blind to condition | Intended; did not hold in any pair | Quality result substantially weakened |
| Verbatim prompt text recorded | Met | — |
| Token counts from the platform, not estimated | Met — JSONL telemetry | — |
| Report input, output, and total separately | Output only | No total-cost claim possible |
| Report distribution, not only the mean | Met — mean, median, range, per-run table | — |
| Quality gate before token comparison | Met — 40/40 completions, no PARTIAL or FAIL | — |
| Fixed success/failure conditions applied unchanged | Met | — |

The input-token requirement could not be met: the telemetry records `input_tokens: 2` on every run
because real input arrives through the prompt cache. This is a platform measurement limitation, not
an omission by the benchmark.

The blinding failure is the significant one. This protocol called blinding the fix for "the largest
bias in the existing evidence," and it did not hold — the benchmark runs were told their own
condition and echoed it into their response headers. Any repeat must strip condition markers from
responses before evaluation.

## What a repeat should change

In priority order:

1. **Strip condition disclosure from responses before evaluation.** Mechanical fix, removes the
   largest defect in the v2 quality result.
2. **Preserve per-run quality scores.** v2's aggregates cannot be recomputed from any artifact.
3. **Five runs per cell**, as originally specified.
4. **Independently authored scenarios.**
5. **A second model family** — though that is properly
   [experiment 02](02-cross-model.md).
