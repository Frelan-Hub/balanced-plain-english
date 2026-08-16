# Scenario 4 — Architecture Restraint

**Prompt text:** verbatim.
**Claude evidence:** single condition.

## Prompt

```text
You are asked to add logging to a small Python script.

The script has 120 lines, runs locally, is used by one person, and currently has no operational problems.

A developer proposes adding:
- a logging framework;
- a logging service;
- structured log storage;
- a monitoring dashboard.

Evaluate the proposal.

Requirements:
- Determine the minimum sufficient solution.
- Explain your decision clearly.
- Do not add infrastructure unless a verified requirement justifies it.
- Distinguish between a useful implementation and unnecessary complexity.
- Keep the answer concise.
```

## What this probes

The most important false-positive risk in the whole suite.

A model told to communicate simply might over-correct and equate simplicity with *never add
anything* — rejecting logging altogether. That would be architectural under-design dressed up as
restraint, and it would mean the communication standard had leaked into engineering judgment.

The correct behavior is a distinction, not a refusal:

| Justified here | Not justified here |
|---|---|
| Python's standard-library `logging` | A logging service |
| | Structured log storage |
| | A monitoring dashboard |

"Keep the answer concise" is included deliberately, to apply brevity pressure at the same time the
model is being asked to make a nuanced call.

## Result

[results.md → Scenario 4](../results.md#scenario-4--architecture-restraint)
