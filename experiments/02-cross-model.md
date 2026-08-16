# Experiment 02 — Cross-Model Validation

**Status:** not run.
**Priority:** high. This is the only way to distinguish a small real effect from no effect.

## Question

Does the standard produce a comparable effect on a model whose default output is more verbose than
Claude's?

## Why this matters more than it looks

The Claude evidence has a structural problem that no amount of additional Claude testing can fix.

Claude's OFF baseline is already concise, assumption-aware, and architecturally restrained. The
observed ON/OFF difference was therefore small. Two explanations fit that observation equally well:

1. The standard works, and Claude had little headroom.
2. The standard does little, and the small difference is noise.

**Claude cannot distinguish these.** A model already near the target behaves the same way under a
working treatment and a null one.

A model with a more verbose baseline can. If the standard is effective, the effect should be larger
where there is more overhead to remove. If the effect is absent there too, explanation 2 gains
substantial support.

This experiment is designed to be able to fail. That is the point.

## Design

Same scenarios as the Claude set, same A/B method, standard version 1.1.0 unmodified.

Candidate model families: Gemini, GPT, Llama, Mistral — any model family with a documented tendency
toward longer default responses. Select on baseline verbosity, not on capability.

### Rules

1. **Do not modify the standard for the target model.** A tuned variant produces evidence about a
   different document. If a model needs vendor-specific handling, that finding belongs in
   [deployment/cross-model.md](../deployment/cross-model.md), not in the standard.
2. Record the model version and date. Model behavior changes between releases.
3. Record token counts if the platform exposes them. Combining this with
   [experiment 01](01-token-efficiency.md) is efficient and costs almost nothing extra.
4. Store results under a new model-named directory in `evidence/`. Do not merge into the Claude
   record.

### Baseline calibration

Before running the scenarios, measure the model's OFF verbosity on the same prompts and compare it
to Claude's OFF verbosity. Without this, a large ON/OFF difference cannot be attributed to headroom
rather than to the standard, and the experiment loses the ability to answer its own question.

## Expected outcomes

| Outcome | Interpretation |
|---|---|
| Larger ON/OFF difference than Claude, quality preserved | Supports the standard; supports the headroom explanation |
| Similar small difference despite a more verbose baseline | Weakens the standard's claim substantially |
| Larger difference but degraded engineering quality | The standard behaves differently across models; a serious portability finding |
| Model ignores or misapplies the standard | A deployment or adherence finding, not a standard finding — investigate the instruction mechanism first |

The third row deserves emphasis. If a plain-language instruction that preserves engineering quality
on Claude degrades it on another model, the standard is not model-agnostic in practice, whatever its
text says. That would be the most consequential result this project could produce, and it would
require revisiting the portability claim in
[deployment/cross-model.md](../deployment/cross-model.md).

## What this cannot settle

Cross-model comparison tests portability, not universality. Two model families is not "works across
models" — it is two data points. State results as "observed on X and Y," never as a general claim.

## Contributing

Use [templates/run-record.md](templates/run-record.md). Submit raw outputs and analysis as separate
files. Raw outputs are never edited to fit a conclusion.
