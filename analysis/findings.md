# Findings

Interpretation of [evidence/claude/results.md](../evidence/claude/results.md) (v1) and
[evidence/claude/benchmark-v2/](../evidence/claude/benchmark-v2/README.md) (v2). Every claim here
should be traceable to one of those records. Confidence qualifiers are attached because they belong
to the claims, not to a disclaimer at the end.

Findings 1–7 are from v1 and are unchanged. Findings 8–10 are from v2.

## Finding 1 — Communication overhead decreased; substance did not

**Confidence: low to moderate. Basis: three paired scenarios, unblinded.**

The most repeated signal across the paired scenarios:

> ON tends to communicate complex engineering reasoning with less unnecessary overhead.

Most visible in explanations, architecture decisions, incident analysis, and assumption handling.
Least visible in short implementation tasks, where there is little overhead available to remove.

What makes this more than a preference judgment is that it holds together with Finding 2. Reduced
overhead *with* preserved substance is the claim. Either half alone would be uninteresting.

## Finding 2 — No observed degradation of engineering quality

**Confidence: moderate. Basis: all scenarios, including three designed specifically to expose it.**

Across the observed tests, ON produced no case of:

- simpler but incorrect code
- suppressed edge cases
- refused justified complexity
- architectural under-design
- loss of technical terminology where it was needed

This is the primary success condition, and the scenarios were built to break it. Scenario 4 applied
brevity pressure to an architecture judgment. Scenario 7 targeted the security distinctions most
likely to collapse under compression. Scenario 6 buried a completeness requirement inside a long
ambiguous prompt.

Under ON, the security distinctions survived:

| Preserved distinction | Would have been lost by naive simplification |
|---|---|
| Authentication vs authorization | "the user is logged in" |
| Validation vs output encoding | "sanitize the input" |
| Raw storage vs export-time protection | "escape the formula" |
| Partial success vs transaction atomicity | "handle the error" |

Architecture restraint also survived in the correct direction: unnecessary infrastructure was
rejected while justified mechanisms were still recommended. The model did not over-correct into
treating plain language as a mandate for minimal engineering.

## Finding 3 — The uncertainty boundary became more visible, imperfectly

**Confidence: low to moderate. Basis: one scenario, with recorded counter-evidence.**

The incident scenario produced the clearest single instance of the intended behavior. ON structured
its reasoning as an explicit chain from observed output through the numerical delta, sample-record
analysis, and possible defect class, to what could not yet be proven, what evidence was required,
what containment was immediate, and what corrective direction followed.

It also refused the scenario's built-in trap:

> "Yesterday's output is not a trustworthy baseline."

Historical stability does not prove historical correctness. A service with inconsistent input
handling may have been producing wrong numbers all along.

**The counter-evidence, in the same response.** Two inferences exceeded the evidence: describing the
numerical delta as *"the signature of the core defect,"* and asserting that a swallowing mechanism —
`try/except`, an `isinstance` filter, or `.get(..., 0)` — must exist. Both are plausible. Neither was
established by what the scenario supplied.

The useful conclusion is narrower than "ON handles uncertainty better." It is:

> Clear presentation of an inference does not make the inference warranted. Better *structure*
> around uncertainty is not the same as better *calibration* of uncertainty.

Structure is a communication property and is within the standard's scope. Calibration is a reasoning
property and is not. This distinction is easy to lose when a well-organized response reads as a
confident one.

## Finding 4 — A communication standard cannot guarantee task completion

**Confidence: high. Basis: direct observation, single clear instance.**

Scenario 6 requested seven explicit output sections. ON did not reliably produce all of them —
despite the standard containing an explicit rule requiring exactly that.

The rule was present. It was not reliably executed.

This is the most architecturally useful result in the set, because it establishes a boundary rather
than a score:

> Communication standards optimize expression. Execution and verification mechanisms guarantee
> completion and correctness.

The tempting response — add a stronger sentence to the standard — would not have changed the
mechanism that failed. It would only have made the standard longer. The defect belongs to the
execution layer, and it is why the standard is frozen rather than extended. See
[docs/03-scope-boundaries.md](../docs/03-scope-boundaries.md).

## Finding 5 — Requirement-fidelity defects appeared under both conditions

**Confidence: moderate. Basis: two paired scenarios.**

Neither condition was clean:

| Condition | Defect | Scenario |
|---|---|---|
| OFF | Implemented owner-name deduplication the spec did not require | 6 |
| OFF | Introduced a status vocabulary conflicting with the one supplied in the prompt | 7 |
| ON | Omitted explicitly requested output sections | 6 |

The failure shapes differ. OFF **added** unrequested behavior. ON **omitted** requested structure.

Both are requirement-fidelity failures, and the pairing is informative: it suggests the standard
shifts *which* fidelity errors occur rather than eliminating them. That is a weaker and more honest
reading than the scorecard's +4 on requirement fidelity implies on its own.

## Finding 6 — Claude is a weak instrument for detecting this effect

**Confidence: moderate. Basis: OFF-condition behavior across all paired scenarios.**

OFF was already highly capable at technical reasoning, ambiguity detection, architecture restraint,
security reasoning, and concise explanation. It surfaced its own assumptions unprompted:

> "These are the points where the spec allows more than one reading."

A model already near the target behavior has limited room to visibly improve. Two readings of the
small observed difference are equally consistent with this evidence:

1. The standard works, and Claude's headroom is small.
2. The standard does little, and the small difference is noise.

**This evidence cannot distinguish them.** Saying so is the correct conclusion; picking the flattering
reading would not be.

Discriminating between them requires a model with a more verbose baseline, where a real effect would
have room to show. That is the purpose of
[experiments/02-cross-model.md](../experiments/02-cross-model.md), and it is the highest-value
evidence this project is currently missing after token counts.

## Finding 7 — The scorecard's shape is more informative than its values

**Confidence: moderate, as a pattern. The values themselves carry little information.**

The largest indicative gaps fall on communication discipline, clarity, and useful information
density. The smallest fall on technical precision, technical nuance, architecture restraint, and
engineering quality.

The near-flat result on the second group is the desired outcome, not a weak one. Substantial movement
there — in either direction — would indicate the communication standard was influencing engineering
reasoning, which is a design failure regardless of whether the influence looked positive.

> The standard primarily affects expression and communication efficiency, while leaving core
> engineering capability largely unchanged.

That is exactly the architectural behavior the layer separation predicts.

## Finding 8 — The overhead reduction is large and measurable

**Confidence: high, for the tested model and task set. Basis: 20 paired comparisons, telemetry.**

Enabling the standard reduced output tokens by **50.45% in aggregate** across 20 paired scenarios on
Claude Opus 5. Median per-run reduction 54.83%; 19 of 20 runs positive; range −3.38% to +72.28%.

Three properties make this the strongest evidence in the repository:

1. **It is telemetry, not judgment.** Output-token counts cannot be influenced by rater expectation —
   the weakness that limits every other finding here.
2. **It is independently recomputable.** [`verify.py`](../evidence/claude/benchmark-v2/verify.py)
   reproduces every published figure from raw telemetry.
3. **It is robust to the extraction rule.** An independent recount using a broader rule gives 49.31%
   against the published 50.45%, with the same 19/20 positive runs.

The effect is large enough that noise is an implausible explanation for its *direction*. It is not
grounds for precision in the number: one run per cell, one model, one author-written task set.

**Counter-evidence, retained:** BPE-014 regressed (−3.38%). Its OFF baseline (5,613 tokens) is a
statistical outlier below the lower Tukey fence, and that scenario required an OFF rerun. An
atypically short baseline is a plausible reason a percentage went slightly negative — an observation
about the data, not grounds to exclude the run. It is included in every published figure.

## Finding 9 — No material quality cost was detected, on a weak instrument

**Confidence: low to moderate. Basis: 20 pairs, unblinded model-based rubric, per-run scores lost.**

All 40 responses completed the task. No pair was scored as a material quality difference by the
evaluator's threshold. Averages: OFF 9.70, ON 9.50 out of 10. Head-to-head win counts were not
preserved and are not recoverable from any artifact — see
[benchmark report](../evidence/claude/benchmark-v2/README.md#two-integrity-notes-on-the-quality-data).

The direction slightly favours OFF. That is worth stating rather than rounding away: the measured
0.20-point gap is small and was judged non-material, but it is not zero and it does not favour the
standard.

Two defects limit how much this finding can carry, and both are serious:

1. **Blinding did not hold.** The condition appears in the response text of all 20 pairs — 12/20 in
   both responses. The evaluation is unblinded in every pair, not most.
2. **Per-run scores were not preserved.** Unlike the token figures, these cannot be recomputed from
   any artifact.

The defensible statement is narrow: *no material quality difference was detected*. Not that quality
was equal, and not that the evaluation was blind.

This is the weakest link in the v2 evidence chain, and it is the link the token result depends on. A
50% token reduction only means something if quality held. The token measurement is strong; the
evidence that quality held is not.

## Finding 10 — The effect extends beyond v1's single domain

**Confidence: moderate. Basis: 20 domains, one scenario each.**

v1 was entirely Python backend engineering, and its narrowness was recorded as a limitation. v2 spans
software and AI architecture, BIM and interior design operations, security, requirements engineering,
governance, incident response, strategic planning, and twelve others. The reduction appears across
them.

This widens the claim's domain coverage. It does not deepen it: one scenario per domain cannot
characterize any domain, and reduction was uneven — 17.58% on requirements engineering and 19.78% on
privacy/local AI against 72.28% on document intelligence. The benchmark is not large enough to
explain that spread.

## What follows from all ten

**Verdict: keep the standard, keep it frozen, and fix the quality instrument next.**

The evidence now supports a measured efficiency claim, scoped to one model and one task set. It still
does not support a cost claim, a latency claim, a cross-model claim, or a claim of quality
equivalence.

The next evidence should be, in order of value:

1. **A second model family** — [experiments/02](../experiments/02-cross-model.md). Everything
   measured is Claude. This is now the largest gap.
2. **A genuinely blind quality evaluation with per-run scores preserved.** v2's token measurement is
   strong and its quality gate is weak; the pairing is unbalanced.
3. **Independently authored scenarios**, to test whether the effect survives a task set the standard's
   author did not write.
4. **Conversation-level turn counts** —
   [experiments/03](../experiments/03-conversation-efficiency.md).

Adding rules to the standard is still not on that list, and that is still deliberate. A large
measured result is not a reason to start editing the thing that was measured — it is a reason to keep
it fixed so later evidence remains comparable.
