# Benchmark v2 — Raw Telemetry

Source files as received. **Preserved unedited**, including a known defect.

| File | Role |
|---|---|
| `BPE_PAIRED_results.csv` | **Authoritative.** Paired per-run telemetry, links each run to both session logs |
| `BPE_ON_results_final.csv` | ON telemetry extract |
| `BPE_OFF_results_final.csv` | OFF telemetry extract — **contains four superseded rows** |
| `BENCHMARK_DESIGN_V2.md` | Benchmark design, written before execution |

## Authoritative source

`BPE_PAIRED_results.csv` is the dataset every published figure derives from. It is the input to
[`../verify.py`](../verify.py).

## Known defect in `BPE_OFF_results_final.csv`

Despite its name, this file is **not** the final OFF dataset. It lists aborted first-attempt OFF
sessions for four runs:

| Run | Session in this file | Output tokens | Assistant messages | Final value used |
|---|---|---:|---:|---:|
| BPE-011 | `64f2ba83…` | 526 | 2 | 13,194 |
| BPE-012 | `e796fc38…` | 364 | 2 | 18,704 |
| BPE-013 | `948b4593…` | 1,717 | 4 | 17,183 |
| BPE-014 | `0e0543bb…` | 514 | 2 | 5,613 |

Each aborted session terminated after 2–4 assistant messages, against 3–4 for the completed reruns
with output in the 5,613–18,897 range. `BPE_PAIRED_results.csv` uses the completed reruns under
different session IDs.

Rows for BPE-001 to BPE-010 and BPE-015 to BPE-020 match the paired dataset exactly.

**Do not compute aggregates from this file.** It is kept because raw evidence is not edited to fit a
conclusion — the rule in [CONTRIBUTING.md](../../../../CONTRIBUTING.md).

The benchmark brief described only BPE-014 as having been rerun. The preserved telemetry shows four
affected runs. This is recorded as a discrepancy between the brief and the artifacts, resolved in
favour of the artifacts.

## Telemetry field notes

**`InputTokens` is unusable.** Every row records `2`. Real input arrived through the prompt cache and
appears under `CacheCreation` and `CacheRead`. This is why the benchmark reports an **output-token**
reduction and makes no total-cost claim.

**`ThinkingTokens`** is recorded but not analysed.

**Timestamps** are as emitted by the extraction tooling. `BPE_ON_results.csv` and
`BPE_ON_results_final.csv` in the source working directory differ only in timestamps; all token
values are identical, so only the final file is preserved here.

## Session logs

Raw Claude Code JSONL session logs for all 40 executions are preserved outside the repository. Each
row of `BPE_PAIRED_results.csv` records the session filename for both conditions, so any published
number can be traced to a specific log.

An independent recount from those logs is reported in
[the benchmark report](../README.md#independent-recount). It uses a broader extraction rule, yields
uniformly higher absolute values, and produces a 49.31% aggregate reduction against the published
50.45% — the headline is robust to the extraction rule.
