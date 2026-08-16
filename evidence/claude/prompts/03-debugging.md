# Scenario 3 — Debugging

**Prompt text:** verbatim.
**Claude evidence:** single condition. The record does not label the observation ON or OFF.

## Prompt

```text
Find the bug in this Python code and provide the minimal fix:

def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

Requirements:
- Identify the problem.
- Provide the minimal correction.
- Explain why the correction is needed.
- Do not redesign the function.
- Do not add unnecessary error-handling unless it is required by the identified problem.
```

## What this probes

Whether a spec gap is surfaced or silently filled.

The defect is straightforward: an empty input raises `ZeroDivisionError`. The interesting part is
what comes next. "Fix it" does not specify what an empty input *should* return. Zero, `None`, and
raising a clearer exception are all defensible, and they are different API contracts.

The failure mode being watched for is a model that picks one, implements it, and does not mention
that it made a choice.

## Result

[results.md → Scenario 3](../results.md#scenario-3--debugging)
