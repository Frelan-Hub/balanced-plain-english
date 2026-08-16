# Raw Record

| File | Description |
|---|---|
| `CLAUDE-BALANCED-PLAIN-ENGLISH-TESTS.md` | The original validation record, unedited |

This is the primary source for everything in [../results.md](../results.md),
[../scorecard.md](../scorecard.md), and [`analysis/`](../../../analysis/).

It is preserved verbatim. It is not rewritten when the analysis is revised — if the two ever
disagree, this file is authoritative and the analysis is wrong.

## Scope of what it contains

- test method and conditions
- per-scenario prompts and observations for the eight scenarios
- cross-test findings
- an explicit statement of what the tests do not prove
- the qualitative scorecard and its caveats
- token-efficiency reasoning, labelled as hypothesis
- the recommended quantitative validation protocol

## Note

The record contains the phrase *"a shorter response was not automatically considered better."* That
rule is what makes the rest of it evaluable. Read it before reading the results.
