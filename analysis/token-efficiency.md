# Token Efficiency

> **Status: measured, on one model.** The [v2 benchmark](../evidence/claude/benchmark-v2/README.md)
> collected output-token telemetry for 40 executions on Claude Opus 5 and found a **50.45%
> aggregate output-token reduction** with no material quality difference detected.
>
> This document previously argued that the standard *should* reduce tokens and carried an
> unmeasured 5–10% estimate. That estimate is superseded and recorded below as a miss.

## What is now measured

| Metric | Value |
|---|---:|
| Aggregate output-token reduction | 50.45% |
| Mean per-run | 47.81% |
| Median per-run | 54.83% |
| Runs with positive reduction | 19 / 20 |
| Range | −3.38% to +72.28% |
| Task completion | 40 / 40 |
| Material quality differences | 0 / 20 |

Scope: Claude Opus 5, standard v1.1.0, 20 author-written scenarios, one run per cell, **output
tokens only**.

## What is still not measured

The distinction the benchmark forces, and which must be preserved in every restatement:

| Measured | Not measured |
|---|---|
| Output tokens | Total inference cost |
| | Input tokens — telemetry records `input_tokens: 2` on every run |
| | Context and cache tokens |
| | Latency |
| | Conversation-level turn count |

**Output-token reduction is not cost reduction.** A complete cost assessment would price input,
cache-creation, and cache-read tokens alongside output, and would net the standard's own recurring
input cost — roughly one page of Markdown on every ON request — against the output saving. The
benchmark does none of that.

For short exchanges, the standard's input cost could plausibly exceed its output saving. The v2
scenarios were complex and produced 5,000–19,000 output tokens per run, where the input cost is
proportionally small. That reasoning is not a measurement either.

## The estimate that was wrong

This document previously carried:

> **Potential unnecessary-output reduction: approximately 5–10%.**

The measured aggregate is 50.45% — roughly five to ten times the estimate.

The estimate is recorded rather than deleted, because being wrong by that margin is informative. Two
readings, and the evidence does not fully separate them:

1. **The estimate was too conservative.** It was reasoned from the *categories* of waste the standard
   targets — restatement, redundant conclusions, filler — without weighing how much of a long
   response those categories actually occupy. On complex prompts, they occupy far more than 10%.
2. **The task set favours large reductions.** The v2 scenarios are complex, open-ended, and
   architectural — exactly the shape of prompt where an unconstrained model produces the most
   framing, preamble, and elaboration. A task set of short factual questions would likely show much
   smaller reductions, because there is less overhead available to remove.

Reading 2 is a real constraint on generalizing the 50.45% figure, and it is why the benchmark report
states the result as specific to its task set.

## Why raw token count is still the wrong metric

The measurement does not retire the metric design. It makes it operational.

A response that drops a required section, an edge case, or a stated uncertainty is shorter. Under
raw token counting it scores as an improvement:

```text
Shorter + incomplete  ≠  more efficient
```

So token comparison is gated on quality, not reported alongside it:

```text
Quality-Adjusted Token Efficiency
=
Useful / Required Information
÷
Tokens Used
```

This remains a **conceptual metric** — "useful/required information" has no agreed unit. Its
practical use is as a gate. In v2 the gate was applied through task completion and the rubric: all
40 responses completed the task and no pair differed by more than one rubric point, so the token
comparison was admissible.

Had any ON run been scored PARTIAL or FAIL, its token saving would have been reported as a quality
failure rather than an efficiency result. None was.

## Two levels of efficiency

```text
Response efficiency          MEASURED — 50.45% aggregate output reduction
    ↓
fewer unnecessary tokens per response

Conversation efficiency      NOT MEASURED
    ↓
fewer unnecessary clarification and correction turns
```

The second may matter more than the first. A clearer first response that prevents one clarification
round-trip saves an entire request-response cycle — the full input context plus a new output — which
is larger than trimming filler from a single answer.

It remains the weaker hypothesis, supported by the communication design and nothing else. Every v2
execution was single-turn. See
[experiments/03](../experiments/03-conversation-efficiency.md).

## Success and failure conditions, as applied

Fixed in [experiments/01](../experiments/01-token-efficiency.md) before the benchmark ran, and
applied unchanged:

**Success condition — met:**

```text
ON
↓
fewer unnecessary tokens        50.45% aggregate reduction
+
same or better correctness      no material difference detected
+
same or better completeness     40/40 task completions
+
same or better precision        no pair differed by more than 1 rubric point
```

**Failure condition — not triggered:**

```text
ON
↓
20% fewer tokens
+
missing requirements
```

No run was scored PARTIAL or FAIL under either condition.

Fixing these in advance is what makes the result usable. Without a pre-registered failure condition,
any token reduction can be reported as a win and any quality loss explained away afterward.

> Token reduction is subordinate to engineering and communication quality.

That ordering did not change because a large number arrived.

## Caveats that survive the measurement

1. **The quality gate was unblinded.** The condition appears in the response text of all 20 pairs.
   The gate detected no material difference; it cannot establish that none exists.
2. **Per-run quality scores were not preserved.** The token figures are independently
   recomputable; the quality figures are not.
3. **One run per cell.** Run variance is not separated from treatment effect. The pre-registered
   protocol asked for five runs per condition.
4. **Author-written scenarios.** A task set written by the standard's author may favour the
   responses the standard produces.
5. **One model.** No cross-model measurement exists.

## Strategic reading

The characterization is unchanged, and now has a number attached to its first term:

> `balanced-plain-english.md` is a communication-efficiency layer, not an engineering-reasoning
> layer.

```text
Less unnecessary response overhead      measured: 50.45% fewer output tokens
        +
Preserved engineering quality           no material difference detected
        +
Clearer communication                   v1 qualitative
        +
Higher useful-information density       v1 qualitative
        +
Better uncertainty presentation         v1 qualitative
        +
Better scope discipline                 v1 qualitative
```

Token reduction remains a *consequence* of removing communication overhead, not the objective. A
standard optimized directly for token count would be a different and worse document — it would hit
the failure condition above rather than the success condition.
