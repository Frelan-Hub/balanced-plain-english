# Balanced Plain English

A communication standard for AI coding assistants, with the evidence used to evaluate it.

**Status:** measured on one model. A 20-scenario paired benchmark on Claude Opus 5 found a **50.45%
aggregate output-token reduction with no material quality difference detected**
([report](evidence/claude/benchmark-v2/README.md)). Output tokens only — not cost, not latency. One
model, one task set. Reviewer's overview: [EVIDENCE-SUMMARY.md](EVIDENCE-SUMMARY.md).

---

## The problem

AI coding assistants can produce technically correct but unnecessarily verbose communication:
restated questions, repeated conclusions, filler, redundant caveats, narrated routine work, and
simple ideas turned into frameworks.

The obvious fix — "be more concise" — is the wrong fix. Instructions that optimize for brevity
tend to remove the things engineering work depends on: edge cases, uncertainty, explicit
requirements, technical distinctions, and justified complexity.

## The objective

Not shorter answers.

> Maximize useful information density while preserving correctness, completeness, technical
> nuance, engineering judgment, explicit requirements, and necessary complexity.

## The thesis

> Balanced Plain English is not a "shorter answers" rule.
>
> It is a quality-preserving communication and semantic-compression standard:
> **complete the required work first, then remove unnecessary communication overhead.**
>
> Plain language applies to expression, not to the removal of technical correctness, necessary
> complexity, uncertainty, edge cases, or explicit requirements.

It works only because it stays inside one layer:

| Layer | Responsibility |
|---|---|
| Communication standard | Optimize expression |
| Engineering conventions | Optimize implementation quality |
| Governance | Control architecture and change |
| Execution and validation | Verify completion and correctness |

The standard must not grow into a universal engineering-control policy. See
[docs/02-thesis.md](docs/02-thesis.md) and [docs/03-scope-boundaries.md](docs/03-scope-boundaries.md).

---

## The question this repository answers

> Does `balanced-plain-english.md` reduce unnecessary AI verbosity while preserving engineering
> quality?

**Current answer:** yes, measured, on Claude Opus 5.

The [v2 benchmark](evidence/claude/benchmark-v2/README.md) ran 20 paired scenarios across 20 domains
— 40 executions — and found a **50.45% aggregate reduction in output tokens**, 19 of 20 runs
positive, with **no material quality difference detected** and 40/40 task completions.

Three limits belong next to that number:

1. **One model, one task set, one run per cell.** No statistical significance is claimed or implied.
2. **Output tokens only.** Input telemetry is unusable, so this is not a cost or latency claim.
3. **The quality evaluation was not blind.** It was intended to be; the condition appears in the
   response text of all 20 pairs. It detected no material difference, but it cannot establish
   quality equivalence.

The earlier [v1 qualitative validation](evidence/claude/results.md) is preserved unchanged. It asked
a different question — whether the standard degrades engineering quality — and found no evidence
that it does. v2 measures the overhead reduction v1 could only describe.

Twelve secondary questions and their evidence status are tracked in
[docs/04-questions.md](docs/04-questions.md).

---

## Repository layout

The repository separates five things that are easy to confuse. Keep them separate when adding to it.

| Section | Contains | Nature |
|---|---|---|
| [`standard/`](standard/) | The canonical standard, verbatim | **Canonical Standard** |
| [`evidence/`](evidence/) | Method, prompts, raw records, v1 results, v2 benchmark | **Evidence** |
| [`analysis/`](analysis/) | Findings, limitations, token-efficiency reasoning | **Analysis** |
| [`deployment/`](deployment/) | Global, skill, and cross-model installation | **Deployment** |
| [`experiments/`](experiments/) | Protocols and templates for evidence not yet collected | **Future Experiments** |

Raw outputs stay in `evidence/`. Interpretation stays in `analysis/`. A claim in `analysis/` that
is not traceable to `evidence/` is a defect.

---

## What the evidence supports

**Measured, from the [v2 benchmark](evidence/claude/benchmark-v2/README.md)** — 20 paired scenarios,
40 executions, Claude Opus 5:

- 50.45% aggregate output-token reduction; median per-run 54.83%; 19 of 20 runs positive.
- No material quality difference detected. Every non-tied pair differed by one rubric point, and all
  40 responses completed the task.
- The reduction appears across 20 distinct domains, not just the Python backend work v1 covered.

**Qualitative, from the [v1 validation](evidence/claude/results.md)** — 8 scenarios, 3 paired:

- ON communicated complex engineering reasoning with less unnecessary overhead.
- ON did not degrade engineering quality: no simpler-but-incorrect code, no suppressed edge cases,
  no refused justified complexity.
- ON preserved architecture restraint and made the known/unknown boundary more visible.

## What the evidence does not support

- **Cost or latency reduction.** v2 measured output tokens only. Input telemetry is unusable and
  cache tokens were not analysed.
- **Statistical significance.** One run per condition per scenario. No confidence intervals.
- **Quality equivalence.** No material difference was *detected*, by an unblinded model-based
  evaluation whose per-run scores were not preserved.
- **Any general "~50% fewer tokens" claim.** One model, one author-written task set.
- **Universal improvement** across models, long contexts, or conversation-level efficiency.
- **Guaranteed task completion.** A v1 test showed ON omitting explicitly requested output sections.
  That is an execution-layer responsibility, not a communication-layer one.

Results recorded against the standard rather than for it, kept in place rather than summarized away:
one v2 run regressed (BPE-014, −3.38%), and in v1 ON omitted requested output sections in one
scenario and over-inferred in another.

The percentage scorecard in [evidence/claude/scorecard.md](evidence/claude/scorecard.md) is a
subjective v1 rubric, not measurement — unlike the v2 token figures, which are telemetry. Read
[analysis/limitations.md](analysis/limitations.md) before citing any number from this repository.

---

## Using it

Three deployment modes, all covered in [deployment/](deployment/):

| Mode | When |
|---|---|
| [Global](deployment/global.md) | You want it to apply to every session by default |
| [Skill](deployment/skill.md) | You want it on demand, for specific tasks only |
| [Cross-model](deployment/cross-model.md) | You want the same contract across model vendors |

The standard is plain Markdown with no vendor-specific syntax. That is deliberate — it is the
property that lets one communication contract survive model and tool replacement.

A ready-to-install skill package is in
[deployment/skill/balanced-plain-english/](deployment/skill/balanced-plain-english/).

---

## What would strengthen this most

In order of value:

1. **A second model family.** Everything measured so far is Claude. Portability is currently a
   property of the standard's construction, not a tested result.
   [experiments/02](experiments/02-cross-model.md)
2. **A genuinely blind quality evaluation**, with per-run scores preserved. v2's was neither.
3. **Independently authored scenarios.** The v2 task set was written by the standard's author.
4. **Multiple runs per cell**, to separate run variance from treatment effect.

## Contributing evidence

New evidence is more useful than new rules. The standard is frozen at 1.1.0 and the unfreeze
conditions are deliberately narrow; see [standard/README.md](standard/README.md) and
[CONTRIBUTING.md](CONTRIBUTING.md).

If you run the standard against another model or scenario, use
[evidence/methodology.md](evidence/methodology.md) and the templates in
[experiments/templates/](experiments/templates/). Submit raw outputs and analysis separately, and
report null and negative results — they are as useful here as positive ones.

---

## License and attribution

Licensed under [CC BY 4.0](LICENSE). Author: Julius Frelan Cabias — Frelan | Arch ID Design AI
Visuals ([archidfrelanai.com](https://archidfrelanai.com)).
