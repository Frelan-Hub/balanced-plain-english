# Qualitative Scorecard

> **Read this first.** The numbers below are a **subjective evaluation rubric**, not measurements.
>
> They summarize one unblinded rater's qualitative judgments across eight scenarios, expressed on a
> common percentage scale so the *pattern* can be compared across dimensions. They are not
> benchmark scores, not measured model performance, and not statistically meaningful.
>
> Do not cite any individual number as a measured improvement.

## Scores

| Dimension | ON | OFF | Indicative ON advantage |
|---|---:|---:|---:|
| Clarity | 95% | 90% | +5 |
| Technical precision | 96% | 95% | +1 |
| Technical nuance preservation | 97% | 96% | +1 |
| Completeness | 92% | 88% | +4 |
| Requirement fidelity | 91% | 87% | +4 |
| Uncertainty handling | 96% | 92% | +4 |
| Architecture restraint | 97% | 96% | +1 |
| Scope discipline | 95% | 91% | +4 |
| Conciseness | 94% | 91% | +3 |
| Useful information density | 96% | 91% | +5 |
| Engineering quality preserved | 98% | 97% | +1 |
| Communication discipline | 96% | 90% | +6 |

```text
Claude ON   ≈ 95%
Claude OFF  ≈ 92%

Indicative overall difference ≈ +3 points
```

## The pattern is the result

The individual numbers carry almost no information. Their **shape** carries the finding:

| Band | Dimensions | Reading |
|---|---|---|
| Largest gaps (+5 to +6) | Communication discipline, clarity, useful information density | The standard's intended effect |
| Moderate gaps (+4) | Completeness, requirement fidelity, uncertainty handling, scope discipline | Secondary effects of the completeness-first rule |
| Smallest gaps (+1) | Technical precision, technical nuance, architecture restraint, engineering quality | The standard's intended *non*-effect |

The small numbers are as important as the large ones, and they are the reason the scorecard is worth
publishing at all.

If technical precision or engineering quality had moved substantially, that would indicate the
communication standard was leaking into engineering reasoning — a design failure, regardless of the
direction of the change. A near-flat result on those four dimensions is the desired outcome.

Restated:

> The standard primarily affects **expression and communication efficiency**, while leaving core
> engineering capability largely unchanged.

## Per-dimension notes

**Communication discipline (+6)** — the strongest observed benefit. ON reduced repetition,
unnecessary framing, redundant conclusions, and unnecessary explanation.

**Clarity (+5)** — ON organized complex reasoning more explicitly and made the relationships between
evidence, uncertainty, decisions, and actions easier to follow. Scenario 8 is the clearest instance.

**Useful information density (+5)** — the target is maximum useful information per token without
sacrificing engineering quality, not shorter responses. Note that this dimension is *judged*, not
computed; no token counts exist.

**Completeness (+4)** — v1.1.0 places completeness before concision. Not scored higher because
scenario 6 showed ON still omitting explicitly requested sections.

**Requirement fidelity (+4)** — ON preserved explicit requirements rather than optimizing for
brevity too early. Both conditions still produced fidelity defects in scenario 6 and 7.

**Uncertainty handling (+4)** — ON made the known / possible / unknown / needs-verification boundary
more visible. Tempered by the two over-strong inferences recorded in scenario 8.

**Scope discipline (+4)** — ON stayed closer to the requested task, supporting *minimum sufficient
response, not minimum-length response*.

**Conciseness (+3)** — deliberately not the primary optimization. A shorter response that omits
required technical information is a failure, not a win.

**Technical precision (+1)** — small by design. Claude already demonstrated strong precision without
the standard.

**Technical nuance (+1)** — no evidence that plain-language requirements removed edge cases,
technical distinctions, uncertainty, security considerations, or justified complexity.

**Architecture restraint (+1)** — architecture is governed elsewhere. ON preserved the ability to
reject unnecessary infrastructure while still recommending justified mechanisms.

**Engineering quality preserved (+1)** — the critical result is not that ON improves engineering
reasoning. It is that communication optimization did not materially degrade it.

## What this scorecard is not

- Not a measurement of model performance
- Not a benchmark
- Not statistically significant
- Not blinded
- Not multi-rater
- Not derived from token counts
- Not generalizable beyond the eight scenarios and one model family tested

Three of the eight scenarios have paired ON/OFF Claude responses. The ON and OFF columns above are
informed primarily by those three. See the evidence ledger in [../README.md](../README.md).
