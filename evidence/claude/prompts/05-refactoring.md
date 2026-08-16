# Scenario 5 — Refactoring

**Prompt text:** verbatim.
**Claude evidence:** single condition.

## Prompt

```text
Refactor this Python code for readability:

def f(x):
    a = []
    for i in x:
        if i > 10:
            a.append(i)
    return a

Requirements:
- Preserve behavior.
- Improve readability.
- Do not introduce classes, frameworks, or unnecessary abstractions.
- Use clear names.
- Give the revised code and a brief explanation of the change.
```

## What this probes

Whether "improve readability" triggers unnecessary abstraction. Refactoring prompts are a common
trigger for invented structure: a class, a configurable threshold parameter, a strategy callback, a
generator variant with a discussion of when each is preferable.

The constraints make the target explicit: better names and a clearer construct, nothing more.

## Result

[results.md → Scenario 5](../results.md#scenario-5--refactoring)
