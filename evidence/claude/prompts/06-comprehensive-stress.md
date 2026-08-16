# Scenario 6 — Comprehensive Engineering Stress Test

> **Specification only.** The validation record preserved this scenario's specification, not its
> verbatim prompt text. Nothing below has been reconstructed as prompt wording. A rerun should
> record its exact prompt text.

**Claude evidence:** paired — ON and OFF both captured.

## Scenario specification

A Python service processes project dictionaries containing:

- `id`
- `name`
- `status`
- `budget`
- `owner`
- `tags`

### Required outputs

- active-project count
- total active-project budget
- active-project owner names
- IDs of active projects with missing or invalid budgets

### Defects present in the supplied implementation

- unsafe dictionary access
- inconsistent budget validation
- other correctness problems

### Infrastructure proposed in the scenario

Deliberately excessive, to test architectural restraint under a long prompt:

- Pydantic
- repository / service / domain layers
- a database
- Redis
- a message queue
- OpenTelemetry
- centralized logging
- a vector database
- a framework rewrite

### Required response sections

```text
A. Findings
B. Clarifications / Assumptions
C. Corrected Implementation
D. Tests
E. Complexity
F. Architecture Decision
G. Final Recommendation
```

## What this probes

Completeness under load. This is the scenario that produced the most useful negative result in the
suite.

Three things are tested at once:

1. Does correctness survive a long, ambiguous specification?
2. Is excessive proposed infrastructure rejected?
3. **Does an explicitly requested seven-section output structure actually get produced?**

The third is the reason this scenario matters most. A communication standard that says "fulfill all
explicit requirements before optimizing for brevity" is directly on trial when the prompt names
seven required sections.

## Result

[results.md → Scenario 6](../results.md#scenario-6--comprehensive-engineering-stress-test)
