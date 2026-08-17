# Evidence

What was actually observed. Interpretation lives in [`analysis/`](../analysis/), not here.

Two evidence sets, answering different questions. Neither supersedes the other.

| Set | Question | Scale |
|---|---|---|
| **v1 — qualitative validation** | Does the standard degrade engineering quality? | 8 scenarios, 3 paired, no token counts |
| **v2 — token efficiency benchmark** | Does it cut output tokens without a quality cost? | 20 scenarios, 20 paired, 40 executions |

### v1 — qualitative validation

| File | Contents |
|---|---|
| [methodology.md](methodology.md) | A/B design, evaluation rule, scoring approach, known methodological weaknesses |
| [claude/results.md](claude/results.md) | Per-scenario record: prompt, condition, observation, finding |
| [claude/scorecard.md](claude/scorecard.md) | Qualitative rubric scores, with an explicit statement of what they are not |
| [claude/prompts/](claude/prompts/) | The prompt for each scenario |
| [claude/raw/](claude/raw/) | The original validation record, unedited |

### v2 — token efficiency benchmark

| File | Contents |
|---|---|
| [claude/benchmark-v2/](claude/benchmark-v2/) | Full report: design, results, quality validation, limitations, reproducibility |
| [claude/benchmark-v2/verify.py](claude/benchmark-v2/verify.py) | Recomputes and asserts every published figure |
| [claude/benchmark-v2/data/](claude/benchmark-v2/data/) | Machine-readable per-run results and quality aggregates |
| [claude/benchmark-v2/raw/](claude/benchmark-v2/raw/) | Source telemetry as received, including a flagged defect |

Headline: **50.45% aggregate output-token reduction**, 19/20 runs positive, no material quality
difference detected, 40/40 task completions. Output tokens only — not cost, not latency.

## Evidence ledger — v1

Eight scenarios were run. They do not all carry the same weight, and the difference matters more
than the total:

| Evidence type | Scenarios | Count |
|---|---|---|
| Paired ON/OFF Claude responses | 6, 7, 8 | **3** |
| Single-condition Claude observation | 1, 3, 4, 5 | 4 |
| No Claude evidence captured | 2 | 1 |

Only the three paired scenarios support an ON-versus-OFF comparison. The four single-condition
scenarios test whether ON behavior is acceptable in absolute terms — useful, but not comparative.
Scenario 2's captured responses came from a different model and are excluded rather than presented
as Claude evidence.

Any **v1** claim that rests on comparison rests on three scenarios. That is stated plainly wherever
such a claim appears. v2 has 20 paired comparisons and does not share this weakness — but has
weaknesses of its own, listed in
[its limitations section](claude/benchmark-v2/README.md#limitations).

## Conditions

| Condition | Meaning |
|---|---|
| ON | `balanced-plain-english.md` v1.1.0 enabled |
| OFF | Only `balanced-plain-english.md` disabled; all other instruction files unchanged |

## Rules for this directory

1. Raw outputs are never edited to fit a conclusion. `benchmark-v2/raw/BPE_OFF_results_final.csv`
   contains four superseded rows and is kept unedited and flagged rather than cleaned.
2. Negative and mixed results stay in the record. Three are recorded: a v2 run that regressed
   (BPE-014, −3.38%), a v1 omitted output-section failure under ON, and two over-strong inferences
   under ON in the v1 incident scenario.
3. Every claim in `analysis/` must be traceable to a file here. One that is not is a defect.
4. New evidence is appended; it does not overwrite existing records. v2 did not modify any v1 file.
