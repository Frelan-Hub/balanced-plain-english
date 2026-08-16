# Experiment 03 — Conversation-Level Efficiency

**Status:** not run.
**Priority:** medium. Highest potential value, hardest to measure well.

## Question

Do clearer first responses reduce the number of clarification and correction turns needed to reach a
satisfactory outcome?

## Why this could matter more than response-level efficiency

Trimming filler from one answer saves a fraction of one response. Preventing one clarification
round-trip saves an entire request-response cycle: the full input context re-sent, plus a new
output.

```text
Response efficiency
    ↓
fewer unnecessary tokens per response

Conversation efficiency
    ↓
fewer unnecessary clarification and correction turns
```

The standard contains a rule aimed squarely at this:

> When important information is missing, don't assume it. State what is missing and ask for the
> minimum information needed to give a reliable answer.

An assumption silently made produces work that must be redone. A question asked once, early, does
not.

## Why it is hard to measure

Every difficulty below is a reason to design the experiment carefully, not a reason to skip it.

| Difficulty | Consequence |
|---|---|
| "Satisfactory outcome" needs a definition fixed before the run | Otherwise the stopping point drifts to favor the expected result |
| The human's follow-ups are part of the system under test | A rater who knows the condition steers the conversation |
| Real tasks vary enormously in required turns | Task variance can swamp treatment effect |
| Asking clarifying questions *adds* turns | The metric must not penalize the behavior the standard prescribes |

The last row is the trap. A response that asks one clarifying question uses more turns than one that
guesses — and is usually better. Counting turns alone would score the correct behavior as a
regression.

## Design sketch

Not a finished protocol. Anyone running this should tighten it first.

1. Define a set of tasks with **objectively checkable** completion criteria, fixed before any run.
2. Define the stopping condition in advance: the conversation ends when the criteria are met, or at
   a hard turn cap.
3. Script the user side, or use a second model as a consistent simulated user, so follow-ups do not
   vary with the rater's knowledge of the condition.
4. Run each task under ON and OFF.
5. Record:

```text
Turns to satisfactory outcome
Turns classified as clarification
Turns classified as correction
Total conversation tokens
Whether completion criteria were met
```

## Metric

Total conversation tokens to a verified satisfactory outcome — not turn count.

This handles the clarifying-question trap correctly. A conversation that spends one short turn
asking a question and then produces correct work should beat one that produces wrong work and then
spends two long turns fixing it, even though both took three turns.

Report the completion rate separately. A condition that reaches fewer satisfactory outcomes is not
more efficient regardless of its token total.

## Success and failure conditions

**Success:** fewer total conversation tokens to a verified satisfactory outcome, with an equal or
higher completion rate.

**Failure:** fewer tokens with a lower completion rate, or a higher rate of tasks abandoned at the
turn cap.

**Null result:** no meaningful difference. Report it. The conversation-efficiency hypothesis is
currently the weakest claim in this repository — supported by the communication design and nothing
else — and it should be dropped if it does not hold.

## Current status of the claim

From [analysis/token-efficiency.md](../analysis/token-efficiency.md):

> This is a hypothesis supported by the communication design, not yet a measured result.

Until this experiment runs, no conversation-efficiency benefit may be claimed anywhere in this
repository.
