# Evidence

What was actually observed. Interpretation lives in [`analysis/`](../analysis/), not here.

| File | Contents |
|---|---|
| [methodology.md](methodology.md) | A/B design, evaluation rule, scoring approach, known methodological weaknesses |
| [claude/results.md](claude/results.md) | Per-scenario record: prompt, condition, observation, finding |
| [claude/scorecard.md](claude/scorecard.md) | Qualitative rubric scores, with an explicit statement of what they are not |
| [claude/prompts/](claude/prompts/) | The prompt for each scenario |
| [claude/raw/](claude/raw/) | The original validation record, unedited |

## Evidence ledger

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

Any claim in this repository that rests on comparison rests on three scenarios. That is stated
plainly wherever such a claim appears.

## Conditions

| Condition | Meaning |
|---|---|
| ON | `balanced-plain-english.md` v1.1.0 enabled |
| OFF | Only `balanced-plain-english.md` disabled; all other instruction files unchanged |

## Rules for this directory

1. Raw outputs are never edited to fit a conclusion.
2. Negative and mixed results stay in the record. Two are recorded: an omitted output-section
   failure under ON, and two over-strong inferences under ON in the incident scenario.
3. Every claim in `analysis/` must be traceable to a file here. One that is not is a defect.
4. New evidence is appended under a model-named directory; it does not overwrite existing records.
