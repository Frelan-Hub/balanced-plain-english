# Cross-Model Deployment

Use the same communication contract across model vendors.

> **Evidence status:** portability is a **construction property**, verifiable by inspecting the
> standard. It is *not* a tested result. No controlled ON/OFF run has been performed against a
> second model family. See [experiments/02](../experiments/02-cross-model.md).

## Why it is portable

The standard is plain Markdown containing:

- no vendor names
- no tool-call syntax
- no framework or runtime assumptions
- no client-specific formatting directives
- no references to any specific model's capabilities

It is a set of instructions about how to express an answer. Nothing in it depends on who is
executing it. That is verifiable by reading the file, which is why the claim is made at all — it is
an inspection result, not an inference from testing.

This is deliberate, and it is the property that makes the standard worth maintaining as a separate
document. A communication contract that survives model replacement is an asset. One that must be
rewritten per vendor is a maintenance cost.

## Installing

Paste the body of [`standard/balanced-plain-english.md`](../standard/balanced-plain-english.md)
into whatever the target system uses for persistent instructions.

| Target | Mechanism |
|---|---|
| API integrations | The `system` parameter |
| CLI agents | Global instruction or rules file |
| IDE assistants | Custom-instructions or rules file |
| Chat interfaces | Custom or project instructions |
| Agent frameworks | System-prompt configuration |

No adaptation is required. If a target system needs the text modified to work, that modification is
a vendor-specific concern and belongs in an adapter layer, not in the standard.

## Expect different magnitudes of effect

The same standard will not produce the same visible change across models.

A model whose default output is already concise, assumption-aware, and architecturally restrained
has little room to improve. A model whose default is verbose — heavy preambles, restatement, closing
summaries, hedging — has a great deal.

This was observed directly in the Claude evidence: the OFF baseline was already strong, which made
the ON/OFF difference small. That is a property of the *model*, not a measurement of the standard's
effectiveness.

```text
Small observed difference
    ≠
Standard is ineffective

Small observed difference
    =
Baseline was already close to the target
    OR
Standard is ineffective

These are not distinguishable without a model that has more headroom.
```

Which is exactly why cross-model evidence is the highest-value evidence this project is missing
after token counts.

## The goal is not identical behavior

Different models will express the same contract differently. They have different default registers,
different structural habits, and different levels of native verbosity.

> The goal is not to make every model behave identically. It is a common communication contract that
> remains useful across replaceable models without becoming a hidden engineering-control layer.

Model-specific tuning — adding rules that address one vendor's particular verbosity habit — should
be resisted. It couples the standard to a model, which forfeits the property that makes it worth
having.

If a model needs vendor-specific handling, that handling belongs in a vendor adapter around the
standard, not inside it.

## Contributing cross-model evidence

The protocol is in [experiments/02-cross-model.md](../experiments/02-cross-model.md).

Requirements for the evidence to be usable:

1. Use standard version **1.1.0**, unmodified. A modified standard produces evidence about a
   different document.
2. Run the same scenarios, so results are comparable to the Claude record.
3. Record both conditions in full, unedited.
4. Record token counts if the platform exposes them.
5. Submit raw outputs and analysis as separate files.

Evidence is added under a new model-named directory in `evidence/`. It does not overwrite or merge
into the Claude record.
