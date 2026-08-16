# Contributing

The most useful contribution is **evidence**, not rules.

## What is wanted

| Contribution | Value |
|---|---|
| Token counts for ON/OFF runs | Highest — closes the largest gap |
| A controlled run against a non-Claude model | High — the only way to test the small-effect ambiguity |
| A blinded second rating of the existing evidence | High — addresses the largest methodological weakness |
| Additional scenarios in an untested domain | Useful — everything here is Python backend work |
| Null or negative results | As valuable as positive ones |
| Corrections to claims that overstate the evidence | Always accepted |

## What is not wanted

**New rules for the standard.** It is frozen at 1.1.0, and the freeze is a design decision, not
inertia.

The failure mode being avoided: a test exposes a weakness, the cheapest visible fix is a new
sentence in the standard, and applied repeatedly that turns a one-page portable communication
contract into an unbounded policy document coupled to assumptions about execution.

The unfreeze conditions are in [standard/README.md](standard/README.md#frozen). All three must hold:

1. Evidence from an additional model family or scenario set shows a **communication** defect.
2. The defect is not attributable to execution, validation, or governance.
3. The smallest sufficient fix is a change in expression rules, not added process.

If you believe a change is warranted, open an issue with the evidence and an argument against each
condition before proposing text.

## Submitting evidence

1. Use standard version **1.1.0, unmodified**. A modified standard produces evidence about a
   different document, and the existing evidence does not transfer to it.
2. Follow [evidence/methodology.md](evidence/methodology.md).
3. Fill in [experiments/templates/run-record.md](experiments/templates/run-record.md) per scenario.
   The counter-evidence field is required — write "none observed" rather than leaving it blank.
4. Score with [experiments/templates/scoring-rubric.md](experiments/templates/scoring-rubric.md).
   Report engineering and communication subtotals separately; do not combine them.
5. Store complete, unedited raw responses under `evidence/<model>/raw/`.
6. Put interpretation in `analysis/`, never in `evidence/`.

New model evidence goes in a new directory under `evidence/`. It does not merge into or overwrite
the Claude record.

## Rules that apply to every change

1. **Raw outputs are never edited to fit a conclusion.** If the analysis and the raw record disagree,
   the raw record is authoritative.
2. **Every claim in `analysis/` must be traceable to a file in `evidence/`.** One that is not is a
   defect, not a stronger conclusion.
3. **Attach confidence to claims, not to a disclaimer at the end.**
4. **Do not add a claim this repository explicitly forbids.** The list is in
   [analysis/limitations.md](analysis/limitations.md#what-must-never-be-claimed): no measured token
   reduction, no cost reduction, no context-window savings, no statistical significance, no
   universality.
5. **Keep the five sections separate** — canonical standard, evidence, analysis, deployment, future
   experiments. Mixing them is how an evidence repository turns into marketing.

## Reporting a problem with a claim

Open an issue identifying the specific sentence and what the evidence actually supports. Claims that
outrun their evidence are treated as defects with the same weight as factual errors, because the
whole point of the repository is that it does not overstate.

## Deployment sync

If you change a deployed copy of the standard, you have created a second source of truth. Don't.
Sync is one-way, canonical to copy, verified by:

```bash
diff <(sed -n '/^# Balanced Plain English$/,$p' <DEPLOYED_FILE>) standard/balanced-plain-english.md
```

Expected output: nothing.
