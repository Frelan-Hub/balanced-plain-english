# Evidence Summary

One page for anyone reviewing this repository for evidence. Every figure links to its source.

## What is claimed

> Enabling Balanced Plain English v1.1.0 on Claude Opus 5, across 20 paired scenarios, produced a
> **50.45% aggregate reduction in output tokens** with **no material quality difference detected**
> and **40/40 task completions**.

Scope of that claim: one model, one standard version, one 20-scenario task set, one run per cell,
output tokens only.

## Evidence base

| | v1 — Qualitative validation | v2 — Token efficiency benchmark |
|---|---|---|
| Question | Does the standard degrade engineering quality? | Does it cut output tokens without a quality cost? |
| Model | Claude | Claude Opus 5 |
| Scenarios | 8, Python backend only | 20, twenty domains |
| Paired comparisons | 3 of 8 | 20 of 20 |
| Executions | — | 40 |
| Token counts | none | all 40 |
| Quality method | Unblinded, single human rater | Unblinded, model-based rubric |
| Verdict | No observed quality degradation | 50.45% output reduction, no material quality difference |
| Record | [results](evidence/claude/results.md) · [raw](evidence/claude/raw/CLAUDE-BALANCED-PLAIN-ENGLISH-TESTS.md) | [benchmark report](evidence/claude/benchmark-v2/README.md) |

## Headline numbers

| Metric | Value |
|---|---:|
| Total OFF output tokens | 285,757 |
| Total ON output tokens | 141,604 |
| Tokens saved | 144,153 |
| Aggregate reduction | **50.45%** |
| Mean per-run reduction | 47.81% |
| Median per-run reduction | 54.83% |
| Runs with positive reduction | 19 / 20 |
| Range | −3.38% to +72.28% |
| Task completion | OFF 20/20 PASS · ON 20/20 PASS |
| Quality average | OFF 9.70 / ON 9.50 |
| Material quality differences | 0 / 20 |

Reproduce every token figure:

```bash
python evidence/claude/benchmark-v2/verify.py
```

## What is explicitly not claimed

- Cost reduction — output tokens only; input telemetry is unusable (`input_tokens: 2` on every run)
- Latency improvement — not measured
- Context or cache-token savings — not analysed
- Statistical significance — one run per cell, no confidence intervals
- Quality equivalence — no material difference *detected*, on an unblinded evaluation
- Any general claim that Balanced Plain English reduces tokens by ~50% on other models or task sets
- Conversation-level efficiency — every execution was single-turn

## Known weaknesses, stated up front

These are the four a reviewer should weigh most heavily.

1. **The quality evaluation was not blind.** It was intended to be. The condition appears in the
   response text of **20/20 pairs** (in both responses in 12/20) — each run was told its condition
   and echoed it into its response header. A/B ordering was randomised; condition was not concealed.
2. **Per-run quality scores were not preserved.** Only aggregates were reported. Unlike the token
   figures, the quality figures cannot be independently recomputed.
3. **Scenarios were authored by the standard's author.** A task set written by the author of the
   standard may favour the responses it produces. Independent scenarios would test this harder than
   more runs of these would.
4. **One run per condition per scenario.** Run-to-run variance is not separated from treatment
   effect. The pre-registered protocol asked for five.

Full list: [benchmark limitations](evidence/claude/benchmark-v2/README.md#limitations) ·
[repository limitations](analysis/limitations.md).

## Data-integrity notes

Three discrepancies were found during verification and are recorded rather than silently corrected:

| Finding | Resolution |
|---|---|
| Brief stated 18/20 positive reductions | Recomputation gives **19/20**; only BPE-014 is negative. Corrected |
| Brief stated quality wins OFF 6 / ON 10 | Contradicts the averages and medians, which require OFF 10 / ON 6. Corrected by the author; not derivable from artifacts |
| Brief stated one rerun (BPE-014) | Telemetry shows **four** aborted OFF runs (BPE-011/012/013/014), all superseded in the paired dataset. Recorded |

`raw/BPE_OFF_results_final.csv` still contains the four superseded rows. It is preserved unedited and
flagged; aggregates must not be computed from it.

## Robustness

An independent recount from the raw JSONL logs, using a broader extraction rule than the source
tooling, gives **49.31%** aggregate reduction against the published 50.45%, with the same 19/20
positive runs. The headline does not depend on the extraction rule.
[Detail](evidence/claude/benchmark-v2/README.md#independent-recount).

## The one thing that would strengthen this most

A controlled run on a **second model family**. Everything measured so far is Claude. Portability is
currently a construction property of the standard — plain Markdown, no vendor syntax — not a tested
result. Protocol: [experiments/02](experiments/02-cross-model.md).
