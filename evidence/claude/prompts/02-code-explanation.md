# Scenario 2 — Existing-Code Explanation

**Prompt text:** verbatim.
**Claude evidence:** none captured. The responses recorded in this cycle came from a different
model and are excluded rather than presented as Claude results.

## Prompt

```text
Explain what this Python code does:

def get_active_users(users):
    return [user for user in users if user.get("active") is True]

Requirements:
- Explain it in plain technical English.
- Do not rewrite the code.
- Explain the important behavior only.
- Mention one relevant edge case if there is one.
- Do not introduce unrelated concepts.
```

## What this probes

Scope discipline and edge-case retention in an explanation task. The code contains a specific,
easily-missed technical distinction — `is True` is an identity check, not a truthiness check — which
makes it a good test of whether plain language causes a real distinction to be flattened.

## Evaluation criteria established

- safe key lookup via `.get()`
- strict `is True` behavior
- missing-key behavior
- truthy non-boolean edge cases (`1`, `"yes"` — truthy but not `True`)
- explanation scope: no rewrite, no unrelated concepts

## Result

Retained as part of the suite design. No Claude finding.

[results.md → Scenario 2](../results.md#scenario-2--existing-code-explanation)
