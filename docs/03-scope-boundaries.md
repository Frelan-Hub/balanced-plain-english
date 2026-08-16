# Scope Boundaries

The single most important design rule in this project:

> **Communication standards optimize expression. Execution and verification mechanisms guarantee
> completion and correctness.**

`balanced-plain-english.md` must not grow into a universal task-execution policy.

## In scope

The standard governs how a correct answer is expressed:

- what is included, omitted, ordered, and emphasized
- depth relative to the task
- word choice, terminology consistency, and sentence construction
- when to ask rather than assume
- how uncertainty is presented
- how progress is reported during agentic work

## Out of scope

The standard does not govern, and must not be extended to govern:

| Concern | Owning layer |
|---|---|
| Whether the engineering answer is correct | Engineering conventions, review, tests |
| Whether the architecture is appropriate | Governance and architectural principle |
| Whether the task was actually completed | Execution and validation |
| Whether every requested section exists in the output | Execution and validation |
| Whether tests ran | Execution and validation |
| Whether files were written | Execution and validation |
| Whether acceptance criteria are satisfied | Execution and validation |
| What may be changed and on what evidence | Governance |

## The rule that generates this boundary

> Do not solve every task-completion weakness by adding more prose to the communication standard.

This rule exists because the failure mode is attractive. When a test exposes a weakness, the
cheapest visible fix is a new sentence in the standard. Applied repeatedly, that turns a one-page
communication contract into an unbounded policy document — longer, harder to install, harder to
test, and coupled to assumptions about execution that do not transfer across tools.

## Worked example from the evidence

The comprehensive engineering stress test requested an explicit output structure:

```text
A. Findings
B. Clarifications / Assumptions
C. Corrected Implementation
D. Tests
E. Complexity
F. Architecture Decision
G. Final Recommendation
```

The ON response did not reliably produce every section.

**Tempting fix:** add a rule to the standard requiring all requested sections.

**Correct classification:** the standard already says *"fulfill all explicit requirements,
constraints, requested outputs, and acceptance criteria before optimizing for brevity."* The
instruction exists. It was not reliably executed. Adding a second, more emphatic sentence would not
change the mechanism that failed — it would only add length.

**Owning layer:** execution and validation. A checklist pass that verifies each requested section
is present before the response is returned solves this. A communication rule cannot guarantee it.

This case is recorded in full in
[evidence/claude/results.md](../evidence/claude/results.md#scenario-6--comprehensive-engineering-stress-test)
and treated as a genuine limitation, not explained away, in
[analysis/limitations.md](../analysis/limitations.md).

## How to classify a newly observed defect

Ask, in order:

1. **Is the information absent, or present but poorly expressed?**
   Absent → not a communication defect. Present but buried, repeated, or padded → communication.

2. **Would the defect persist if the model executed the existing rules perfectly?**
   Yes → the rule set is incomplete; consider the standard.
   No → this is an execution or verification failure.

3. **Is the smallest sufficient fix a change in expression rules, or added process?**
   Expression rules → candidate change to the standard.
   Added process → belongs to execution, validation, or governance.

Only a defect that reaches "communication" at step 1, "yes" at step 2, and "expression rules" at
step 3 justifies unfreezing the standard. Those are exactly the unfreeze conditions recorded in
[standard/README.md](../standard/README.md#frozen).

## What this boundary buys

- The standard stays one page and stays portable.
- Its evidence stays interpretable, because the thing being tested does not change shape between
  test cycles.
- Failures get attributed to the layer that can actually fix them.
- The standard does not accumulate vendor-specific or workflow-specific assumptions, which is what
  would break its use across models and tools.
