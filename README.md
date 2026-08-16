# Balanced Plain English

A communication standard for AI coding assistants, with the evidence used to evaluate it.

**Status:** controlled qualitative evidence. Not a benchmark. No measured token savings yet.

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

**Current answer, on the evidence collected so far:** yes, qualitatively, for Claude — with three
honest limits.

1. The observed effect is small, because Claude already exhibits much of the target behavior without
   the standard.
2. The evidence is unblinded single-rater judgment, one run per condition, across eight scenarios in
   one domain — not a measured benchmark.
3. Only **three** of those eight scenarios have paired ON/OFF Claude responses. Every comparative
   claim in this repository rests on those three.

The evidence cannot currently distinguish "a small real effect" from "no effect." Saying so is part
of the answer.

Twelve secondary questions and their evidence status are tracked in
[docs/04-questions.md](docs/04-questions.md): six supported qualitatively, one mixed, two unmeasured,
three answered by design and deployment rather than by testing.

---

## Repository layout

The repository separates five things that are easy to confuse. Keep them separate when adding to it.

| Section | Contains | Nature |
|---|---|---|
| [`standard/`](standard/) | The canonical standard, verbatim | **Canonical Standard** |
| [`evidence/`](evidence/) | Method, prompts, raw test record, results | **Evidence** |
| [`analysis/`](analysis/) | Findings, limitations, token-efficiency reasoning | **Analysis** |
| [`deployment/`](deployment/) | Global, skill, and cross-model installation | **Deployment** |
| [`experiments/`](experiments/) | Protocols and templates for evidence not yet collected | **Future Experiments** |

Raw outputs stay in `evidence/`. Interpretation stays in `analysis/`. A claim in `analysis/` that
is not traceable to `evidence/` is a defect.

---

## What the evidence supports

From eight controlled scenarios against Claude — three with paired ON/OFF responses, four
single-condition, one with no Claude response captured
([ledger](evidence/README.md#evidence-ledger), [full record](evidence/claude/raw/CLAUDE-BALANCED-PLAIN-ENGLISH-TESTS.md)):

- ON communicated complex engineering reasoning with less unnecessary overhead. This was the
  strongest and most repeated signal, clearest in incident analysis and architecture decisions.
- ON did not degrade engineering quality. No observed case of simpler-but-incorrect code,
  suppressed edge cases, refused justified complexity, or lost technical terminology.
- ON preserved architecture restraint. It still rejected unnecessary infrastructure rather than
  equating plain language with minimal engineering.
- ON made the boundary between known, possible, unknown, and needs-verification more visible.

## What the evidence does not support

- Any measured percentage reduction in tokens, cost, or context-window use. No token counts were
  collected in any run.
- Statistical significance of any kind.
- Universal improvement across tasks, domains, long contexts, or model variants.
- Guaranteed task completion. One test showed ON omitting explicitly requested output sections.
  That is an execution-layer responsibility, not a communication-layer one.

Two results are recorded against the standard rather than for it, and kept in place rather than
summarized away: ON omitted requested output sections in one scenario, and made two inferences
stronger than the evidence supported in another.

The percentage scorecard in [evidence/claude/scorecard.md](evidence/claude/scorecard.md) is a
subjective evaluation rubric, not measurement. Read
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

1. **Token counts.** Every efficiency statement here is a design argument.
   [experiments/01](experiments/01-token-efficiency.md)
2. **A model with a more verbose baseline.** The only way to distinguish a small real effect from no
   effect. [experiments/02](experiments/02-cross-model.md)
3. **A second, blinded rater.**

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
