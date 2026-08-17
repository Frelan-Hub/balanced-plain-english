# Methodology — v1 Qualitative Validation

> Scope note: this document describes the **v1 qualitative validation** (8 scenarios, no token
> counts). The v2 token efficiency benchmark has its own design and measurement section — see
> [claude/benchmark-v2/README.md](claude/benchmark-v2/README.md). This file is preserved as written.

## Design

Controlled A/B comparison of identical prompts with the standard enabled (ON) and disabled (OFF).

```text
ON:
1. Enable balanced-plain-english.md
2. Clear the session context
3. Run the exact prompt
4. Save the complete response

OFF:
1. Disable only balanced-plain-english.md
2. Clear the session context
3. Run the exact same prompt
4. Save the complete response
```

Constraints held constant:

- The same prompt text was used for ON and OFF.
- No other governance or convention file was intentionally disabled. Only the communication
  standard was toggled.
- Each condition started from a cleared context, so no response was influenced by the other
  condition's output.

## What was evaluated

Two dimensions, scored separately and deliberately not merged.

**Engineering integrity**

- correctness
- technical precision
- edge-case handling
- requirement fidelity
- uncertainty handling
- architectural restraint

**Communication quality**

- clarity
- concision
- structure
- terminology
- scope discipline
- completeness

## Evaluation rule

> A shorter response was **not** automatically considered better.

The desired behavior is:

> Complete and technically correct first; concise and clear second.

A response that is shorter and omits a required element is classified as a failure, not an
optimization. This rule is what makes the evaluation a test of the standard's actual claim rather
than a test of output length.

## Scenario design

Scenarios were chosen to attack the standard's most plausible failure mode: that instructing a model
toward plain language would cause it to remove engineering substance.

| Scenario type | What it probes |
|---|---|
| Simple implementation | Does the standard cause over-explanation of trivial code? |
| Existing-code explanation | Is scope held, and is one relevant edge case surfaced? |
| Debugging | Is a spec gap surfaced or silently filled with invented behavior? |
| Architecture restraint | Does plain language get misread as "avoid all infrastructure"? |
| Refactoring | Is behavior preserved without introducing abstractions? |
| Comprehensive engineering stress | Does completeness survive under a large multi-section request? |
| Security and data integrity | Are security distinctions simplified away? |
| Production incident | Is the known/unknown boundary preserved under pressure to conclude? |

The last three are the load-bearing scenarios. They are long, ambiguous, and contain deliberately
excessive proposed infrastructure, so a model that trades substance for brevity has many
opportunities to reveal it.

## Scoring

Scoring was **qualitative and rubric-based**, performed by a single unblinded rater — the author.
Each scenario received a verdict (PASS, CONDITIONAL PASS, or a narrative finding) with the reasoning
recorded alongside it.

The percentage scorecard in [claude/scorecard.md](claude/scorecard.md) is a summary of those
qualitative judgments expressed on a common scale. It is a rubric, not a measurement instrument.

## Known methodological weaknesses

Stated here rather than buried, because they determine how much weight the results can carry.

| Weakness | Effect |
|---|---|
| Single unblinded rater, who is also the standard's author | Expectation bias is not controlled |
| No blinding of condition | The rater knew which response was ON |
| Small scenario count (8), single domain (Python engineering) | No basis for generalization |
| One run per condition per scenario | Model output variance is not separated from treatment effect |
| Not all scenarios have paired ON/OFF Claude responses | Three of eight support a genuine comparison |
| No token counts collected | No quantitative efficiency claim is possible **from v1** |
| Single model family | Cross-model portability is untested |

Consequence: the v1 results are **controlled qualitative evidence**, not a benchmark. See
[analysis/limitations.md](../analysis/limitations.md).

Of these weaknesses, the v2 benchmark addresses the token-count gap and the scenario count and
domain breadth. It does **not** address unblinded evaluation — v2's quality evaluation was intended
to be blind and [was not](claude/benchmark-v2/README.md#blinding-did-not-hold) — nor single runs per
cell, nor the single model family.

## Reproducing or extending this

To add evidence:

1. Use the run-record template in [experiments/templates/run-record.md](../experiments/templates/run-record.md).
2. Record the standard version tested. All evidence here is against **1.1.0**.
3. Save the complete raw response for both conditions, unedited, under `evidence/<model>/raw/`.
4. Keep raw outputs and interpretation in separate files.
5. Score against [experiments/templates/scoring-rubric.md](../experiments/templates/scoring-rubric.md).

Improvements that would materially strengthen the evidence, in order of value:

1. Token counts for both conditions (removes the largest gap — see
   [experiments/01-token-efficiency.md](../experiments/01-token-efficiency.md)).
2. A second rater, blinded to condition.
3. Multiple runs per condition to separate treatment effect from output variance.
4. A second model family.
