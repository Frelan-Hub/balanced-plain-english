# Evaluation Questions and Evidence Status

## Primary question

> Does `balanced-plain-english.md` reduce unnecessary AI verbosity while preserving engineering
> quality?

**Status:** supported qualitatively for Claude, with two limits.

The observed effect is small, because Claude already exhibits much of the target behavior without
the standard. And the evidence is unblinded single-rater judgment over a small scenario set, not a
measured benchmark. Details in [analysis/limitations.md](../analysis/limitations.md).

## Secondary questions

Status values used below:

| Status | Meaning |
|---|---|
| **Supported (qualitative)** | Consistent with observed test behavior; unblinded, unmeasured |
| **Mixed** | Some supporting evidence and some counter-evidence |
| **Unmeasured** | Design hypothesis; no measurement collected |
| **By design** | Answered by the standard's construction and deployment, not by testing |

| # | Question | Status | Basis |
|---|---|---|---|
| 1 | Does it improve clarity? | Supported (qualitative) | Incident-analysis scenario showed explicitly structured reasoning from evidence to action |
| 2 | Does it improve useful information density? | Supported (qualitative) | Complex reasoning conveyed with less surrounding overhead; ratio not measured |
| 3 | Does it improve communication discipline? | Supported (qualitative) | Strongest and most repeated signal across scenarios |
| 4 | Does it preserve technical precision? | Supported (qualitative) | No observed case of simpler-but-incorrect output |
| 5 | Does it preserve technical nuance? | Supported (qualitative) | Edge cases, security reasoning, and technical distinctions retained under ON |
| 6 | Does it preserve architecture restraint? | Supported (qualitative) | Unnecessary infrastructure rejected under ON in three scenarios |
| 7 | Does it improve completeness before concision? | **Mixed** | Rule is explicit and directionally effective, but ON omitted requested output sections in one scenario |
| 8 | Does it reduce unnecessary response tokens? | **Unmeasured** | No token counts collected. See [experiments/01](../experiments/01-token-efficiency.md) |
| 9 | Does it reduce unnecessary follow-up turns? | **Unmeasured** | Not tested. See [experiments/03](../experiments/03-conversation-efficiency.md) |
| 10 | Can it be used across different models? | By design; **validation pending** | Plain Markdown, no vendor syntax. Cross-model runs not yet captured. See [experiments/02](../experiments/02-cross-model.md) |
| 11 | Can it operate globally? | By design | Installs as a global instruction file. See [deployment/global.md](../deployment/global.md) |
| 12 | Can it operate selectively as a skill? | By design | Packaged as an on-demand skill. See [deployment/skill.md](../deployment/skill.md) |

**Summary:** six supported qualitatively, one mixed, two unmeasured, three answered by design and
deployment rather than by testing.

## Notes on individual questions

### Q7 — completeness before concision

This is the honest weak point, and it is deliberately not smoothed over.

The rule works as a directional instruction: the ON responses consistently surfaced assumptions,
ambiguities, and constraints rather than compressing them away. But in the comprehensive stress
test, ON did not produce every explicitly requested output section.

The correct conclusion is not that the rule failed. It is that a communication rule cannot
guarantee execution completeness. See [03-scope-boundaries.md](03-scope-boundaries.md).

### Q8 and Q9 — token efficiency

The standard is *designed* to reduce unnecessary tokens: it targets repetition, restatement,
redundant conclusions, unnecessary caveats, and explanation of obvious code. The design rationale is
sound and the observed behavior is consistent with it.

None of that is a measurement.

No claim of a percentage token reduction, cost reduction, or context-window saving is made anywhere
in this repository. The working hypothesis of roughly 5–10% reduction in unnecessary output, carried
over from the validation record, is labelled as an engineering estimate in
[analysis/token-efficiency.md](../analysis/token-efficiency.md) and must not be cited as a result.

### Q10 — cross-model use

Portability is a construction property that can be inspected directly: the standard contains no
vendor names, no tool syntax, no runtime assumptions, and no formatting that depends on a particular
client. It installs anywhere a system prompt or instruction file is accepted.

What has *not* been done is a controlled ON/OFF run against a second model family. Until that
exists, the answer is "portable by construction, unvalidated by evidence."

One test in the initial suite captured responses from a non-Claude model. Those were deliberately
excluded from the Claude results rather than presented as cross-model evidence.

### Q11 and Q12 — global and selective operation

These are deployment facts, not test outcomes, and are stated as such. Both modes are in use in the
author's environment: the standard loads globally through an instruction-file import, and the same
text is packaged as an on-demand skill for selective invocation.

Neither mode has been A/B tested against the other. There is no evidence that one produces better
adherence than the other.
