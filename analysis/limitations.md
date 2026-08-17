# Limitations

Read this before citing anything from this repository.

## The short version

There are two evidence sets with different strengths and different weaknesses.

**v2 — token efficiency benchmark.** A real measurement: 40 executions, telemetry-derived, 20 paired
comparisons, independently recomputable. Its weaknesses are one model, one run per cell, an
author-written task set, and a quality evaluation that was intended to be blind and was not.

**v1 — qualitative validation.** One unblinded rater's judgment, one run per condition, eight
scenarios, one domain, no token counts. It supports a directional conclusion, not a number.

The token figures are the strongest evidence here. The quality figures are the weakest.

## What the evidence does not establish

- statistical significance of any kind
- total inference cost, or latency
- behavior across model families other than Claude
- behavior across very long contexts
- behavior under conflicting instructions
- conversation-level or multi-turn efficiency
- production-scale agent execution
- long-running autonomous workflows
- quality *equivalence* between conditions

## What must never be claimed

This repository does not claim, and no one citing it should claim:

- **cost reduction** — v2 measured output tokens only; input telemetry is unusable and cache tokens
  were not analysed
- **latency improvement** — not measured
- **context-window savings** — not analysed
- **statistically significant improvement** — one run per condition per scenario, no confidence
  intervals
- **that quality was proven equal or identical** — no material difference was *detected*, by an
  unblinded evaluation whose per-run scores were not preserved
- **a blind quality evaluation** — blinding did not hold in any of the 20 pairs
- **universal improvement** across models, tasks, or task types
- **that Balanced Plain English reduces tokens by ~50% generally** — that figure belongs to one
  model and one author-written task set

## What may be claimed, with its scope attached

> In the v2 benchmark — Claude Opus 5, standard v1.1.0, 20 paired scenarios, 40 executions —
> enabling Balanced Plain English produced a 50.45% aggregate reduction in output tokens, with no
> material quality difference detected and 40/40 task completions.

Drop any part of that scope clause and the claim becomes unsupported.

## Superseded estimate

Earlier versions of [token-efficiency.md](token-efficiency.md) carried an engineering estimate of
"approximately 5–10%" potential unnecessary-output reduction, explicitly labelled as unmeasured. The
measured aggregate is 50.45%. The estimate was wrong by roughly an order of magnitude and is
retained in that document, with both candidate explanations, rather than deleted.

## v2 benchmark — methodological weaknesses

Full list in the [benchmark report](../evidence/claude/benchmark-v2/README.md#limitations). The four
that carry the most weight:

### Blinding did not hold

The quality evaluation was intended to be blind. The condition appears in the response text of
**20/20 pairs**, in both responses in 12/20 — each run was told its condition and echoed it into its
response header. A/B ordering was randomised; condition was not concealed.

This does not affect the token measurement, which is telemetry. It substantially weakens the quality
result.

### Per-run quality scores were not preserved

Only aggregates were reported. The token figures can be recomputed from raw telemetry by
[`verify.py`](../evidence/claude/benchmark-v2/verify.py); the quality figures cannot be recomputed
from anything. They rest on the benchmark author's report.

### Author-written scenarios

The 20 scenarios were written by the standard's author. A task set written by the person who wrote
the standard may favour the responses it produces. Independent scenarios would be a stronger test
than more runs of these.

### One run per condition per scenario

The pre-registered protocol asked for a minimum of five. With one sample per cell, run-to-run
variance is not separated from treatment effect.

The effect size (50.45% aggregate, 19/20 runs positive) is large enough that noise is an implausible
explanation for the *direction*. It is not large enough to justify any precision in the number.

## v1 validation — methodological weaknesses

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

### No token measurement in v1

No token counts were collected in any v1 run. This gap is now closed by
[v2](../evidence/claude/benchmark-v2/README.md), which measured 40 executions — but it is closed for
v2's task set and model, not retroactively for v1's.

### Prompt text not preserved for the three strongest scenarios

Scenarios 6, 7, and 8 — the only paired ones — have their specifications preserved but not their
verbatim prompt text. A rerun can reproduce them in substance but not byte-for-byte, which weakens
strict comparability against future evidence.

## What the evidence does support

Stated at the strength it actually has:

**From v2** — on Claude Opus 5, across 20 author-written scenarios spanning 20 domains, one run per
condition: enabling the standard reduced output tokens by 50.45% in aggregate, with 19 of 20 runs
positive, all 40 responses completing the task, and no material quality difference detected by an
unblinded model-based rubric.

**From v1** — on eight Python engineering scenarios judged by one unblinded rater: enabling the
standard was associated with less unnecessary communication overhead, and was **not** associated with
any observed loss of correctness, edge-case handling, technical distinction, security reasoning, or
architectural restraint.

The v1 half is still load-bearing. The main risk of a plain-language instruction is that it degrades
engineering quality; the token measurement would be worthless without evidence on that question, and
v2's quality gate is weaker than v1's on exactly that point despite covering more scenarios.

## Honest summary of confidence

| Claim | Confidence | Why |
|---|---|---|
| The standard reduces output tokens on complex prompts | **High, for the tested model and task set** | Telemetry-derived, 20 paired comparisons, 19/20 positive, independently recomputable, robust to extraction rule |
| The standard does not degrade engineering quality | Moderate | Probed by v1 scenarios designed to expose it; v2 shows 40/40 completions but was unblinded |
| The standard reduces communication overhead | Moderate | v1 qualitative signal, now consistent with a measured 50% output reduction |
| The standard reduces total inference cost | None | Output tokens only; input and cache not analysed |
| The standard reduces latency | None | Not measured |
| The standard reduces follow-up turns | None | Not tested; all v2 executions single-turn |
| The standard transfers across models | None (design argument only) | No cross-model runs |
| Quality is equal between conditions | None | No material difference *detected*; unblinded, per-run scores not preserved |
