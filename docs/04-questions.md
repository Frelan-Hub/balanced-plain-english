# Evaluation Questions and Evidence Status

## Primary question

> Does `balanced-plain-english.md` reduce unnecessary AI verbosity while preserving engineering
> quality?

**Status:** measured for Claude Opus 5, with scope limits.

The [v2 benchmark](../evidence/claude/benchmark-v2/README.md) measured a **50.45% aggregate
output-token reduction** across 20 paired scenarios, with no material quality difference detected and
40/40 task completions. The verbosity half of the question is answered by telemetry; the quality half
rests on an unblinded evaluation and is weaker. Scope: one model, one author-written task set, one
run per cell, output tokens only. Details in
[analysis/limitations.md](../analysis/limitations.md).

## Secondary questions

Status values used below:

| Status | Meaning |
|---|---|
| **Measured** | Quantified from telemetry; scope-limited but not a judgment call |
| **Supported (qualitative)** | Consistent with observed test behavior; unblinded, unmeasured |
| **Mixed** | Some supporting evidence and some counter-evidence |
| **Unmeasured** | Design hypothesis; no measurement collected |
| **By design** | Answered by the standard's construction and deployment, not by testing |

| # | Question | Status | Basis |
|---|---|---|---|
| 1 | Does it improve clarity? | Supported (qualitative) | Incident-analysis scenario showed explicitly structured reasoning from evidence to action |
| 2 | Does it improve useful information density? | Supported (qualitative), partly measured | v2: same task completed in 50.45% fewer output tokens with no material quality loss detected. The denominator is measured; the numerator is still judged |
| 3 | Does it improve communication discipline? | Supported (qualitative) | Strongest and most repeated signal across scenarios |
| 4 | Does it preserve technical precision? | Supported (qualitative) | No observed case of simpler-but-incorrect output |
| 5 | Does it preserve technical nuance? | Supported (qualitative) | Edge cases, security reasoning, and technical distinctions retained under ON |
| 6 | Does it preserve architecture restraint? | Supported (qualitative) | Unnecessary infrastructure rejected under ON in three scenarios |
| 7 | Does it improve completeness before concision? | **Mixed** | v1: ON omitted requested output sections in one scenario. v2: 40/40 task completions, no PARTIAL or FAIL |
| 8 | Does it reduce unnecessary response tokens? | **Measured** | v2: 50.45% aggregate output-token reduction, 19/20 runs positive, median 54.83%. Output tokens only — not cost, not latency |
| 9 | Does it reduce unnecessary follow-up turns? | **Unmeasured** | Not tested. See [experiments/03](../experiments/03-conversation-efficiency.md) |
| 10 | Can it be used across different models? | By design; **validation pending** | Plain Markdown, no vendor syntax. Cross-model runs not yet captured. See [experiments/02](../experiments/02-cross-model.md) |
| 11 | Can it operate globally? | By design | Installs as a global instruction file. See [deployment/global.md](../deployment/global.md) |
| 12 | Can it operate selectively as a skill? | By design | Packaged as an on-demand skill. See [deployment/skill.md](../deployment/skill.md) |

**Summary:** one measured, five supported qualitatively, one mixed, one unmeasured, one answered by
design with validation pending, and three answered by design and deployment rather than by testing.

## Notes on individual questions

### Q7 — completeness before concision

Still mixed, with evidence pulling in both directions.

Against: in the v1 comprehensive stress test, ON did not produce every explicitly requested output
section. For: in v2, all 40 responses — 20 of them ON — completed the task, with no response scored
PARTIAL or FAIL.

The v2 result is reassuring but does not overturn the v1 one. v2 scored *task completion*, not
whether every requested structural element was present, and its evaluation was unblinded.

The conclusion is unchanged: a communication rule cannot guarantee execution completeness. See
[03-scope-boundaries.md](03-scope-boundaries.md).

### Q8 — response tokens

**Measured.** The v2 benchmark found a 50.45% aggregate output-token reduction across 20 paired
scenarios on Claude Opus 5, with 19/20 runs positive and a median per-run reduction of 54.83%.

Three qualifications travel with that number and must not be dropped:

1. **Output tokens only.** Input telemetry is unusable (`input_tokens: 2` on every run) and cache
   tokens were not analysed. This is not a cost claim, and not a latency claim.
2. **One model, one author-written task set, one run per cell.** No statistical significance.
3. **The quality gate was unblinded.** A token reduction only counts if quality held; the evidence
   that it held is weaker than the evidence for the reduction itself.

An earlier estimate in this repository put the reduction at 5–10%. It was wrong by roughly an order
of magnitude and is retained, with both candidate explanations, in
[analysis/token-efficiency.md](../analysis/token-efficiency.md).

### Q9 — follow-up turns

**Still unmeasured.** Every v2 execution was single-turn. Whether clearer first responses reduce
clarification and correction turns is untested, and remains the weakest hypothesis in this
repository. See [experiments/03](../experiments/03-conversation-efficiency.md).

### Q10 — cross-model use

Portability is a construction property that can be inspected directly: the standard contains no
vendor names, no tool syntax, no runtime assumptions, and no formatting that depends on a particular
client. It installs anywhere a system prompt or instruction file is accepted.

What has *not* been done is a controlled ON/OFF run against a second model family. Until that
exists, the answer is "portable by construction, unvalidated by evidence."

One test in the initial suite captured responses from a non-Claude model. Those were deliberately
excluded from the Claude results rather than presented as cross-model evidence.

v2 did not change this. It measured a second Claude model, not a second model family, so it is now
the **largest** open gap: every number in this repository comes from Claude. See
[experiments/02](../experiments/02-cross-model.md).

### Q11 and Q12 — global and selective operation

These are deployment facts, not test outcomes, and are stated as such. Both modes are in use in the
author's environment: the standard loads globally through an instruction-file import, and the same
text is packaged as an on-demand skill for selective invocation.

Neither mode has been A/B tested against the other. There is no evidence that one produces better
adherence than the other.
