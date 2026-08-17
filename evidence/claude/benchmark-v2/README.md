# Balanced Plain English Token Efficiency Benchmark v2

Standard version under test: **1.1.0**, unmodified.
Model: **Claude Opus 5** (`claude-opus-5`).
Measurement: **output tokens only**, from Claude Code JSONL session telemetry.

> **Headline, stated at the strength the evidence supports:**
>
> In this benchmark, enabling Balanced Plain English produced a **50.45% aggregate reduction in
> output tokens** across 20 paired scenarios, while an A/B quality evaluation detected **no material
> quality difference** and all 40 responses completed the task.
>
> This is a measured result for one model, one standard version, and one 20-scenario task set. It is
> not a general claim that Balanced Plain English reduces tokens by 50%.

---

## Objective

The [v1 qualitative validation](../raw/CLAUDE-BALANCED-PLAIN-ENGLISH-TESTS.md) established that the
standard did not appear to degrade engineering quality, but it collected **no token counts**. Every
efficiency statement in this repository was therefore a design argument rather than a measurement,
and the repository said so.

This benchmark closes that gap. It answers the question posed in
[experiments/01-token-efficiency.md](../../../experiments/01-token-efficiency.md):

> Does the standard reduce output tokens without reducing correctness, completeness, or technical
> precision?

The experiment was designed to be able to fail. A large token reduction accompanied by dropped
requirements would have been recorded as a failure, not an optimization.

## Experimental Design

| Property | Value |
|---|---|
| Paired scenarios | 20 |
| Total executions | 40 |
| Runs per condition per scenario | 1 |
| Model | Claude Opus 5, held constant |
| Standard version | 1.1.0, unmodified |
| Session isolation | Each execution in its own Claude Code session |
| Prompt | Identical across conditions, used verbatim |
| Raw evidence | JSONL session logs preserved for all 40 executions |

Each scenario was run once with the standard disabled and once with it enabled. Model, settings,
tools, and execution environment were held constant. The intended sole variable was the Balanced
Plain English condition.

### Scenario coverage

Twenty complex scenarios spanning distinct domains — a deliberate widening from v1, which was
entirely Python backend work:

| Run | Domain | Run | Domain |
|---|---|---|---|
| BPE-001 | software architecture | BPE-011 | knowledge management |
| BPE-002 | AI system architecture | BPE-012 | document intelligence |
| BPE-003 | architecture and BIM operations | BPE-013 | AI governance |
| BPE-004 | interior design operations | BPE-014 | workflow automation |
| BPE-005 | AI evaluation | BPE-015 | technical QA |
| BPE-006 | security architecture | BPE-016 | privacy and local AI |
| BPE-007 | complex code analysis | BPE-017 | cost and efficiency |
| BPE-008 | requirements engineering | BPE-018 | incident response |
| BPE-009 | decision analysis | BPE-019 | system design tradeoffs |
| BPE-010 | multi-agent orchestration | BPE-020 | complex strategic planning |

## Conditions

| Condition | Meaning |
|---|---|
| OFF | Balanced Plain English disabled |
| ON | Balanced Plain English v1.1.0 enabled |

## Model

Claude Opus 5 (`claude-opus-5`) for all 40 executions, both conditions, and the quality evaluation.

## Measurement

Output-token telemetry read from the `usage.output_tokens` field of assistant messages in Claude
Code JSONL session logs. Each paired row records the session file for both conditions, so every
number traces to a specific preserved log.

**What is measured:** output tokens.

**What is not measured, and is not claimed anywhere in this report:**

| Not measured | Why it matters |
|---|---|
| Total inference cost | Requires input, cache-creation, and cache-read tokens priced together |
| Input tokens | The telemetry records `input_tokens: 2` for every run; real input arrives via cache. The field is unusable for comparison |
| Context and cache tokens | Recorded in the raw CSVs but not analysed here |
| Latency | Not captured |

The standard itself consumes input tokens on every ON request. A complete cost assessment would have
to net that recurring cost against the output saving. This benchmark does not do that, so **output
token reduction must not be restated as cost reduction**.

## Results

| Metric | Value |
|---|---|
| Total OFF output tokens | **285,757** |
| Total ON output tokens | **141,604** |
| Total tokens saved | **144,153** |
| Aggregate output-token reduction | **50.45%** |
| Mean per-run reduction | **47.81%** |
| Median per-run reduction | **54.83%** |
| Runs with positive reduction | **19 / 20** |
| Range | −3.38% to +72.28% |

Every figure above is recomputed from the raw paired telemetry by
[`verify.py`](verify.py). None is transcribed.

### Per-run results

| Run | Domain | OFF | ON | Saved | Reduction |
|---|---|---:|---:|---:|---:|
| BPE-001 | software architecture | 15,997 | 9,045 | 6,952 | 43.46% |
| BPE-002 | AI system architecture | 15,490 | 6,641 | 8,849 | 57.13% |
| BPE-003 | architecture and BIM operations | 11,703 | 7,012 | 4,691 | 40.08% |
| BPE-004 | interior design operations | 12,440 | 5,352 | 7,088 | 56.98% |
| BPE-005 | AI evaluation | 12,771 | 8,127 | 4,644 | 36.36% |
| BPE-006 | security architecture | 17,349 | 5,630 | 11,719 | 67.55% |
| BPE-007 | complex code analysis | 13,186 | 5,680 | 7,506 | 56.92% |
| BPE-008 | requirements engineering | 15,156 | 12,492 | 2,664 | 17.58% |
| BPE-009 | decision analysis | 14,991 | 5,543 | 9,448 | 63.02% |
| BPE-010 | multi-agent orchestration | 17,296 | 8,126 | 9,170 | 53.02% |
| BPE-011 | knowledge management | 13,194 | 5,699 | 7,495 | 56.81% |
| BPE-012 | document intelligence | 18,704 | 5,184 | 13,520 | **72.28%** |
| BPE-013 | AI governance | 17,183 | 7,317 | 9,866 | 57.42% |
| BPE-014 | workflow automation | 5,613 | 5,803 | −190 | **−3.38%** |
| BPE-015 | technical QA | 14,724 | 7,424 | 7,300 | 49.58% |
| BPE-016 | privacy and local AI | 10,480 | 8,407 | 2,073 | 19.78% |
| BPE-017 | cost and efficiency | 14,210 | 9,497 | 4,713 | 33.17% |
| BPE-018 | incident response | 14,794 | 6,896 | 7,898 | 53.39% |
| BPE-019 | system design tradeoffs | 12,826 | 4,013 | 8,813 | 68.71% |
| BPE-020 | complex strategic planning | 17,650 | 7,716 | 9,934 | 56.28% |
| **Total** | | **285,757** | **141,604** | **144,153** | **50.45%** |

Machine-readable: [`data/paired-results.csv`](data/paired-results.csv),
[`data/paired-results.json`](data/paired-results.json).

### The runs that did not follow the pattern

Three runs are worth naming rather than averaging away.

**BPE-014 (−3.38%) — the only regression.** ON produced *more* output than OFF. Two facts about this
run are relevant and are stated together:

- It is the only run where the standard did not reduce output.
- Its OFF value (5,613) is a statistical outlier: the next-smallest OFF response is 10,480, and 5,613
  falls below the lower Tukey fence of 6,632 for the OFF distribution. This scenario also required an
  OFF rerun after an incomplete first attempt (see [Reproducibility](#reproducibility)).

An unusually short OFF baseline is a plausible reason a percentage reduction went slightly negative.
That is an observation about the data, not a licence to exclude the run. **BPE-014 is retained in
every figure in this report.**

**BPE-008 (17.58%) and BPE-016 (19.78%) — the weakest positive results.** Both are well below the
median. Reduction is not uniform across domains, and this benchmark is not large enough to explain
why.

## Quality Validation

An A/B quality evaluation was run separately from the token measurement, comparing both responses in
each pair against the original benchmark requirements.

### Method

| Property | Value |
|---|---|
| Pairs evaluated | 20 |
| Evaluator | Model-based |
| A/B ordering | Randomised per pair |
| Rubric total | 10 points |
| Completion scale | PASS / PARTIAL / FAIL |

Rubric dimensions, 0–2 each: Correctness, Requirement Coverage, Constraint Adherence, Useful
Specificity, Efficiency / Unnecessary Verbosity.

### Blinding did not hold

The evaluation was intended to be blind. **It was not**, and the report does not describe it as such.

The A/B labels were anonymised and the ordering randomised, but each benchmark run had been told its
own condition and echoed it into its response header — for example
`Condition: OFF (Balanced Plain English disabled)`. Inspecting the preserved evaluation inputs:

| Disclosure | Count |
|---|---|
| Pairs where the condition appears in at least one response | **20 / 20** |
| Pairs where it appears in **both** responses | 12 / 20 |
| Pairs where the condition was genuinely concealed | **0 / 20** |

The condition was recoverable in every pair. Any claim resting on blinding is therefore unsupported,
and the quality result must be read as an **unblinded model-based evaluation**.

This does not affect the token measurement, which is telemetry and cannot be influenced by evaluator
expectation.

### Results

| Metric | OFF | ON |
|---|---:|---:|
| Average score | 9.70 / 10 | 9.50 / 10 |
| Median score | 10 / 10 | 9.5 / 10 |
| Head-to-head wins | not recoverable | not recoverable |
| Ties | 4 | 4 |
| Task completion | 20/20 PASS | 20/20 PASS |
| PARTIAL or FAIL | 0 | 0 |
| Material quality differences | 0 / 20 | 0 / 20 |

The 0.20-point average difference favours OFF. It was judged non-material: no pair was scored as a
material quality difference by the evaluator's threshold, and no response was partially completed or
failed. The per-pair gap sizes behind that threshold were not preserved, so "every non-tied difference
was a single rubric point" cannot be asserted as fact (see below).

### The supported wording

> An A/B quality evaluation detected no material quality difference across the 20 paired tests.

Not supported, and used nowhere in this repository:

- "identical quality"
- "quality was proven equal"
- "blind evaluation"
- any claim of statistical significance
- any human quality rating

### Two integrity notes on the quality data

**Per-run scores were not preserved.** Only aggregates were reported. Unlike the token figures, the
quality figures **cannot be independently recomputed** from the preserved artifacts. They are
recorded on the benchmark author's word.

**Head-to-head win counts are not recoverable.** No preserved artifact — including the original
benchmark brief — records a win count in either direction; the brief reports only averages, medians,
ties, and the material-difference count. A prior version of this report published an arithmetic-derived
split (OFF 10 / ON 6), on the reasoning that the averages and medians "require" that split if every
non-tied pair differed by exactly one rubric point. That single-point-gap assumption is not itself a
preserved fact — "material quality differences: 0/20" shows every pair's gap stayed under the
evaluator's materiality threshold, not that every non-tied gap was exactly one point. A different mix
of gap sizes among the 16 non-tied pairs would produce a different split from the same averages. Because
the derivation rests on an unverified assumption, win counts are reported here as **not recoverable**
rather than republished under either labeling. The 20 anonymised A/B files that would settle this
directly were not located among the evidence available for this audit; only the aggregate
`quality-summary.json` survived.

## Interpretation

### What this evidence supports

1. **A large, consistent output-token reduction on this task set.** 50.45% aggregate, 19 of 20 runs
   positive, median 54.83%. The effect is large enough that it is not plausibly noise.
2. **No material quality cost, on an unblinded model-based evaluation.** All 40 responses completed
   the task. The largest observed gap in any pair was one rubric point.
3. **The v1 finding holds under measurement.** v1 concluded qualitatively that the standard reduces
   communication overhead without degrading engineering quality. v2 measures the overhead reduction
   and finds no material quality cost. The two are consistent.
4. **The effect extends beyond v1's single domain.** v1 was entirely Python backend work. v2 spans
   20 domains and the reduction appears across them.

### What this evidence does not support

1. **Any general claim about Balanced Plain English and tokens.** This is one model, one standard
   version, one 20-scenario set, one run per cell. "Balanced Plain English reduces tokens by 50%" is
   not a claim this benchmark licenses.
2. **Cost reduction.** Output tokens only. Input, cache, and total cost were not analysed.
3. **Latency improvement.** Not measured.
4. **Statistical significance.** One run per condition per scenario. No confidence intervals are
   computed, and none should be inferred from the spread.
5. **Quality equivalence.** The evaluation detected no *material* difference. It was unblinded, and
   its per-run data was not preserved. It cannot establish equivalence.
6. **Conversation-level efficiency.** Every execution was single-turn. Whether clearer first
   responses reduce follow-up turns remains untested — see
   [experiments/03](../../../experiments/03-conversation-efficiency.md).

### Why the effect is plausibly real

The reduction is large, consistent in direction, and concentrated where the standard predicts it:
its explicit targets are restatement, redundant conclusions, unnecessary framing, over-caveating,
and explaining the obvious. A ~50% output reduction with completion preserved on all 40 runs is
consistent with removing that overhead rather than removing substance.

This reasoning is *consistent with* the measurement. It is not additional evidence for it.

## Limitations

Stated plainly, because they determine how much weight the result carries.

| Limitation | Effect |
|---|---|
| **One model** | Claude Opus 5 only. No cross-model evidence. See [experiments/02](../../../experiments/02-cross-model.md) |
| **One run per condition per scenario** | Model output varies between runs; treatment effect and run variance are not separated |
| **20 scenarios** | Broad in domain, small in count |
| **Model-based quality evaluation** | Not human-rated |
| **Unblinded** | Condition recoverable in 20/20 pairs |
| **Per-run quality scores not preserved** | The quality aggregates cannot be independently recomputed |
| **Output tokens only** | Not total cost, not latency, not context or cache tokens |
| **Single-turn** | No conversation-level measurement |
| **Benchmark-specific** | Scenarios were authored by the standard's author |
| **No statistical testing** | No significance test, no confidence intervals |

The scenarios being author-written deserves particular weight. A task set written by the person who
wrote the standard may favour the kind of response the standard produces. Independent scenarios would
be a stronger test than more runs of these.

### Deviations from the pre-registered protocol

[experiments/01-token-efficiency.md](../../../experiments/01-token-efficiency.md) was written before
this benchmark ran and specified requirements it did not fully meet. Recorded here rather than
quietly dropped:

| Protocol required | Benchmark delivered | Effect |
|---|---|---|
| Minimum 5 runs per condition per scenario | 1 | Run variance not separated from treatment effect |
| At least 15 scenarios, more than one domain | 20 scenarios, 20 domains | Met, and exceeded on domain breadth |
| Quality scored blind to condition | Intended, did not hold | Quality result weakened |
| Verbatim prompt text recorded | Met — prompts preserved in the evidence set | Met |
| Token counts from the platform, not estimated | Met — JSONL telemetry | Met |
| Report input, output, and total separately | Output only; input telemetry unusable | No total-cost claim possible |

The protocol's success and failure conditions were fixed in advance and are applied unchanged:
fewer unnecessary tokens with equal or better correctness and completeness is the success condition,
and it was met. Fewer tokens with missing requirements would have been a failure; no run was scored
PARTIAL or FAIL.

## Reproducibility

### How the artifacts relate

```text
Claude Code JSONL session logs          40 sessions, one per execution
        │                               preserved outside the repository
        ├─ BPE_OFF_results_final.csv    OFF telemetry extract
        ├─ BPE_ON_results_final.csv     ON telemetry extract
        │
        └─ BPE_PAIRED_results.csv       authoritative paired dataset
                │                       links each run to both session files
                │
                ├─ verify.py            recomputes every published figure
                ├─ data/paired-results.csv    derived, machine-readable
                └─ data/paired-results.json   derived, with summary block

Quality evaluation inputs               20 anonymised A/B files (not located — see below)
        └─ data/quality-summary.json    aggregate results only
```

`BPE_PAIRED_results.csv` is authoritative. The per-condition CSVs are extracts.

### Verifying

```bash
python evidence/claude/benchmark-v2/verify.py
```

Recomputes totals, aggregate reduction, mean, median, positive-run count, and every per-run
percentage from `raw/BPE_PAIRED_results.csv`, and asserts them against the figures published above.
Exit code 0 means every published number was reproduced. Add `--emit` to regenerate `data/`.

### Known defect in the source telemetry

`raw/BPE_OFF_results_final.csv` is preserved as received and **is not consistent with the paired
dataset**. It lists aborted first-attempt OFF sessions for four runs:

| Run | Aborted session output | Assistant messages | Final rerun output |
|---|---:|---:|---:|
| BPE-011 | 526 | 2 | 13,194 |
| BPE-012 | 364 | 2 | 18,704 |
| BPE-013 | 1,717 | 4 | 17,183 |
| BPE-014 | 514 | 2 | 5,613 |

All four aborted sessions terminated after 2–4 assistant messages. `BPE_PAIRED_results.csv` uses the
completed reruns, with different session IDs, and its values are the ones published here.

The file is kept unedited because it is source evidence. **Do not compute aggregates from it.** Note
that the benchmark brief described only BPE-014 as having been rerun; the preserved telemetry shows
four affected runs.

### Independent recount

An independent recount was performed directly from the JSONL logs, summing `output_tokens` across
**all** deduplicated assistant messages per session. This is a broader rule than the one the source
CSVs used — it includes setup and tool-use turns — and it yields uniformly higher absolute values:

| | Published (CSV rule) | Independent recount (all assistant messages) |
|---|---:|---:|
| Total OFF | 285,757 | 291,781 |
| Total ON | 141,604 | 147,903 |
| Aggregate reduction | **50.45%** | **49.31%** |
| Mean reduction | 47.81% | 46.89% |
| Median reduction | 54.83% | 53.73% |
| Positive runs | 19/20 | 19/20 |

The offset is positive for all 40 sessions (OFF +163 to +661, ON +154 to +686), consistent with a
narrower extraction rule in the source tooling rather than an error in either.

**The headline is robust to the extraction rule**: ~50% under both, with the same 19/20 positive
runs. The published figures use the CSV rule for consistency with the source telemetry.

## Files

| Path | Contents |
|---|---|
| [`verify.py`](verify.py) | Recomputes and asserts every published figure |
| [`data/paired-results.csv`](data/paired-results.csv) | Per-run results, machine-readable |
| [`data/paired-results.json`](data/paired-results.json) | Per-run results plus summary block |
| [`data/quality-summary.json`](data/quality-summary.json) | Quality aggregates, blinding status, integrity notes |
| [`raw/BPE_PAIRED_results.csv`](raw/BPE_PAIRED_results.csv) | Authoritative paired telemetry, as received |
| [`raw/BPE_ON_results_final.csv`](raw/BPE_ON_results_final.csv) | ON telemetry extract, as received |
| [`raw/BPE_OFF_results_final.csv`](raw/BPE_OFF_results_final.csv) | OFF telemetry extract, as received — contains four superseded rows |
| [`raw/BENCHMARK_DESIGN_V2.md`](raw/BENCHMARK_DESIGN_V2.md) | Benchmark design, as written before execution |

Raw JSONL session logs are preserved outside the repository. `BPE_PAIRED_results.csv` records the
session filename for both conditions of every run.

## Relationship to v1

v1 is not superseded and has not been modified. The two answer different questions:

| | v1 — Qualitative validation | v2 — Token efficiency benchmark |
|---|---|---|
| Question | Does the standard degrade engineering quality? | Does it reduce output tokens without a quality cost? |
| Scenarios | 8, Python backend | 20, twenty domains |
| Paired comparisons | 3 | 20 |
| Token counts | None | 40 executions |
| Quality method | Unblinded single human rater | Unblinded model-based rubric |
| Record | [v1 raw record](../raw/CLAUDE-BALANCED-PLAIN-ENGLISH-TESTS.md), [results](../results.md) | This report |

v1's qualitative claim of reduced communication overhead is what v2 measures. The results are
consistent.
