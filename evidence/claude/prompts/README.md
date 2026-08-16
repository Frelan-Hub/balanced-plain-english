# Prompts

One file per scenario.

| # | Scenario | Prompt text | Claude evidence |
|---|---|---|---|
| 1 | [Simple implementation](01-simple-implementation.md) | Verbatim | ON only |
| 2 | [Existing-code explanation](02-code-explanation.md) | Verbatim | None captured |
| 3 | [Debugging](03-debugging.md) | Verbatim | Single condition |
| 4 | [Architecture restraint](04-architecture-restraint.md) | Verbatim | Single condition |
| 5 | [Refactoring](05-refactoring.md) | Verbatim | Single condition |
| 6 | [Comprehensive engineering stress](06-comprehensive-stress.md) | **Specification only** | ON and OFF |
| 7 | [Security and data integrity](07-security-data-integrity.md) | **Specification only** | ON and OFF |
| 8 | [Production incident](08-production-incident.md) | **Specification only** | ON and OFF |

## Verbatim versus specification

Scenarios 1–5 preserve the exact prompt text as issued.

For scenarios 6–8, the validation record preserved the scenario *specification* — inputs, required
outputs, proposed infrastructure, and constraints — but not the exact prompt wording. Those three
files record the specification and say so at the top. The prompt text has not been reconstructed or
invented to fill the gap.

This matters for reproduction: scenarios 6–8 can be re-created faithfully in substance, but a rerun
is not a byte-identical replay. Anyone rerunning them should record their exact prompt text in the
run record so future comparisons have a fixed reference.
