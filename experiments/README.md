# Future Experiments

Pre-registered protocols. Results live in [`evidence/`](../evidence/), never here.

| Experiment | Question | Status | Priority |
|---|---|---|---|
| [01 — Token efficiency](01-token-efficiency.md) | Does the standard reduce output tokens without reducing quality? | **RUN** → [v2 benchmark](../evidence/claude/benchmark-v2/README.md) | — |
| [02 — Cross-model validation](02-cross-model.md) | Does it produce a comparable effect on a more verbose model? | Not run | **Highest** |
| [03 — Conversation efficiency](03-conversation-efficiency.md) | Does it reduce clarification and correction turns? | Not run | Medium |

Experiment 01 is kept as a **pre-registration**: written before execution, preserved unedited, with
the deviations between what it specified and what was delivered recorded at the bottom of it. That
record is what makes the result auditable.

## Templates

| Template | Use |
|---|---|
| [run-record.md](templates/run-record.md) | One per scenario run, both conditions |
| [scoring-rubric.md](templates/scoring-rubric.md) | Qualitative scoring, engineering and communication scored separately |

## Why in this order

**01 is done.** It was first because it was cheapest to run and closed the largest gap. It converted
the repository's weakest claims — every efficiency statement was a design argument — into a measured
result. It also produced a defect worth fixing: its quality evaluation was intended to be blind and
was not.

**02 is now the highest priority.** Everything measured so far is Claude. It is also the only
experiment that can distinguish a real effect from a task-set artifact, by testing whether the
reduction survives on a different model family.

**03 remains last** because it has the highest potential value and the hardest measurement problem.
It needs a fixed definition of "satisfactory outcome," a scripted or simulated user, and a metric
that does not penalize the clarifying questions the standard prescribes.

**A repeat of 01** is worth running before 03, with condition markers stripped from responses and
per-run quality scores preserved. See
[what a repeat should change](01-token-efficiency.md#what-a-repeat-should-change).

## Rules for any experiment added here

1. **Test standard version 1.1.0 unmodified.** A tuned variant produces evidence about a different
   document.
2. **Fix success and failure conditions before running.** Every protocol here states both in advance.
   A result that can be reinterpreted afterward is not evidence.
3. **Report null and negative results.** They are as publishable as positive ones. Experiment 01
   returning "no meaningful token difference" would remove a claim that should not be made, which is
   a useful outcome.
4. **Raw outputs go in `evidence/`, interpretation in `analysis/`.** Never merge them.
5. **Record counter-evidence explicitly.** The run-record template has a required field for it.

## What is deliberately not planned

No experiment is planned to test whether adding more rules to the standard improves outcomes.

The validation cycle's own recommendation was to freeze the standard and collect evidence rather than
continue adding prose. Extending a communication standard in response to execution failures is the
specific failure mode this project is trying to avoid. See
[docs/03-scope-boundaries.md](../docs/03-scope-boundaries.md) and
[standard/README.md](../standard/README.md#frozen).
