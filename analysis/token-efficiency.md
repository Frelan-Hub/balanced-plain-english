# Token Efficiency

> **Nothing in this document is a measurement.** No token counts were collected in any run. This is
> a design argument and a proposed evaluation model. The 5–10% figure below is an engineering
> estimate of potential unnecessary-output reduction, not a result.

## The claim being made, precisely

Not: "the standard reduces tokens by X%."

Instead:

> The standard is *designed* in a way that should support token efficiency, and the observed Claude
> responses provide qualitative evidence of reduced communication overhead.

Those are different statements. The first requires measurement that does not exist. The second is
what the evidence supports.

## Why the design should reduce tokens

The standard explicitly targets output that carries no decision-relevant information:

- repetition
- restating the user's request
- unnecessary introductions
- redundant conclusions
- excessive caveats
- unnecessary jargon
- explaining obvious code
- repeating the same reasoning in multiple forms

Every item is output tokens spent on nothing the reader can act on. Removing them should reduce
output length. That is a reasonable inference from the rule set, and it is still an inference.

## Why raw token count is the wrong metric

The obvious measurement — count output tokens, compare — would reward exactly the failure this
project exists to prevent. A response that drops a required section, an edge case, or a stated
uncertainty is shorter. Under raw token counting it scores as an improvement.

```text
Shorter + incomplete  ≠  more efficient
```

So the metric must be quality-adjusted:

```text
Quality-Adjusted Token Efficiency
=
Useful / Required Information
÷
Tokens Used
```

This is a **conceptual metric**, not a computable formula — "useful/required information" has no
agreed unit. Its practical use is as a gate rather than a number: a token comparison is only
meaningful when the response also satisfies correctness, technical precision, explicit requirements,
required outputs, necessary edge cases, necessary uncertainty, and acceptance criteria.

Fail any of those, and the token count is not reported as an efficiency result at all.

## Two levels of efficiency

```text
Response efficiency
    ↓
fewer unnecessary tokens per response

Conversation efficiency
    ↓
fewer unnecessary clarification and correction turns
```

The second may matter more than the first. A clearer first response that prevents one clarification
round-trip saves an entire request-response cycle — the full input context plus a new output — which
is a larger saving than trimming filler from a single answer.

It is also the weaker of the two hypotheses. It is supported by the communication design and by
nothing else. No multi-turn conversations were tested. See
[experiments/03](../experiments/03-conversation-efficiency.md).

## Current working estimate

> **Potential unnecessary-output reduction: approximately 5–10%.**

This is an engineering hypothesis based on observed communication behavior. It is **not** an
empirical measurement.

Do not represent 5–10% as a measured Claude token reduction until token counts are collected. Do not
convert it to a cost figure. Do not extrapolate it to context-window savings.

The estimate is stated here rather than omitted because it is the working assumption the project
operates under, and a stated assumption can be tested. An unstated one cannot.

## What would settle this

The protocol is specified in [experiments/01-token-efficiency.md](../experiments/01-token-efficiency.md).
Summary of what it must record per run:

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

Then compute:

```text
Raw Output Reduction %
=
(OFF output tokens − ON output tokens)
÷ OFF output tokens
× 100
```

alongside a quality-adjusted assessment.

## Success and failure conditions

Defined in advance, so the result cannot be reinterpreted after the fact.

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

**Failure — including when token reduction is large:**

```text
ON
↓
20% fewer tokens
+
missing requirements
```

That second outcome must be classified as a failure, not an optimization. Committing to this in
advance is what keeps the experiment honest: without it, any token reduction can be reported as a
win and any quality loss explained away afterward.

> Token reduction is subordinate to engineering and communication quality.

## Strategic reading

The current evidence supports this characterization:

> `balanced-plain-english.md` is a communication-efficiency layer, not an engineering-reasoning
> layer.

Its potential advantages, in the order the evidence supports them:

```text
Clearer communication
        +
Higher useful-information density
        +
Less unnecessary response overhead
        +
Better uncertainty presentation
        +
Better scope discipline
        +
Preserved engineering quality
```

Token reduction, if it exists, is a consequence of the first three — not the objective. A standard
optimized directly for token count would be a different and worse document.
