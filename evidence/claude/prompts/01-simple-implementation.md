# Scenario 1 — Simple Implementation

**Prompt text:** verbatim.
**Claude evidence:** ON only. No OFF response was captured for this scenario.

## Prompt

```text
Write a Python function called `is_even` that returns `True` when an integer is even and `False` otherwise.

Requirements:
- Use Python.
- Keep the implementation simple.
- Include a short explanation.
- Do not add unnecessary abstractions.
- Do not add tests unless needed to demonstrate the function.
```

## What this probes

Whether the standard causes over-explanation of trivial code, or unnecessary abstraction added to
demonstrate thoroughness.

The failure modes being watched for:

- an explanation longer than the function
- a class, decorator, or type-dispatch layer around a one-line operation
- tests added despite the constraint against them
- caveats about input validation that the prompt did not ask for

## Result

[results.md → Scenario 1](../results.md#scenario-1--simple-implementation)
