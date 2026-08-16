# Findings

Interpretation of [evidence/claude/results.md](../evidence/claude/results.md). Every claim here
should be traceable to that record. Confidence qualifiers are attached because they belong to the
claims, not to a disclaimer at the end.

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

## What follows from all seven

**Verdict: keep the standard, freeze it, and collect quantitative evidence next.**

The evidence supports continued use as a communication standard. It does not support a performance
claim, and it does not yet distinguish a small real effect from no effect.

The next evidence should be, in order of value:

1. Token counts — [experiments/01](../experiments/01-token-efficiency.md)
2. A model family with a more verbose baseline — [experiments/02](../experiments/02-cross-model.md)
3. Conversation-level turn counts — [experiments/03](../experiments/03-conversation-efficiency.md)

Adding rules to the standard is not on that list, and that is deliberate.
