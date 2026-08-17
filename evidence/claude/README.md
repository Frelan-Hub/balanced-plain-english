# Claude Evidence

Model family: Claude. Standard version tested: **1.1.0** in both evidence sets.

## v2 — Token efficiency benchmark

**[benchmark-v2/](benchmark-v2/)** — Claude Opus 5, 20 paired scenarios, 40 executions.

50.45% aggregate output-token reduction, 19/20 runs positive, no material quality difference
detected, 40/40 task completions. Output tokens only. Every figure is recomputed by
[`benchmark-v2/verify.py`](benchmark-v2/verify.py) rather than transcribed.

## v1 — Qualitative validation

| File | Contents |
|---|---|
| [results.md](results.md) | Per-scenario observations and findings |
| [scorecard.md](scorecard.md) | Qualitative rubric scores and what they are not |
| [prompts/](prompts/) | Prompt or specification for each of the eight scenarios |
| [raw/](raw/) | The original validation record, unedited |

Preserved unchanged by the v2 work.

### v1 evidence strength

| Scenarios | Evidence |
|---|---|
| 6, 7, 8 | Paired ON/OFF — supports comparison |
| 1, 3, 4, 5 | Single condition — supports absolute judgment only |
| 2 | No Claude response captured |

### v1 headline

ON tends to reduce unnecessary communication overhead while preserving the technical substance the
task requires. v2 measures that overhead reduction; the two are consistent.

## Results recorded against the standard

Kept in place rather than summarized away:

- **v2, BPE-014:** ON produced more output than OFF (−3.38%), the only regression in 20 runs.
- **v1, scenario 6:** ON omitted explicitly requested output sections.
- **v1, scenario 8:** ON made two inferences stronger than the evidence supported.

Also recorded: v2's quality evaluation was intended to be blind and
[was not](benchmark-v2/README.md#blinding-did-not-hold).
