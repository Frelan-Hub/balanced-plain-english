# Future Experiments

Protocols for evidence that does **not** exist yet. Nothing in this directory is a result.

| Experiment | Question | Status | Priority |
|---|---|---|---|
| [01 — Token efficiency](01-token-efficiency.md) | Does the standard reduce output tokens without reducing quality? | Not run | Highest |
| [02 — Cross-model validation](02-cross-model.md) | Does it produce a comparable effect on a more verbose model? | Not run | High |
| [03 — Conversation efficiency](03-conversation-efficiency.md) | Does it reduce clarification and correction turns? | Not run | Medium |

## Templates

| Template | Use |
|---|---|
| [run-record.md](templates/run-record.md) | One per scenario run, both conditions |
| [scoring-rubric.md](templates/scoring-rubric.md) | Qualitative scoring, engineering and communication scored separately |

## Why in this order

**01 first** because it is the cheapest to run and closes the largest gap. Every efficiency statement
in this repository is currently a design argument. Token counts are mechanically objective and would
convert the weakest claims into either a supported result or a refuted one.

**02 second** because it is the only experiment that can distinguish a small real effect from no
effect. Claude's baseline is already close to the target behavior, so additional Claude testing
cannot resolve that ambiguity no matter how much of it is done.

**03 last** because it has the highest potential value and the hardest measurement problem. It needs
a fixed definition of "satisfactory outcome," a scripted or simulated user, and a metric that does
not penalize the clarifying questions the standard prescribes.

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
