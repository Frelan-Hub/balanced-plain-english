# Deployment

Three modes. All use the same file, unmodified.

| Mode | When | Guide |
|---|---|---|
| Global | The contract should be the baseline for every session | [global.md](global.md) |
| Skill | On demand, for specific tasks only | [skill.md](skill.md) |
| Cross-model | The same contract across model vendors | [cross-model.md](cross-model.md) |

A ready-to-install skill package is in
[`skill/balanced-plain-english/`](skill/balanced-plain-english/).

## Choosing

```text
Most of your work is technical
    and you want consistent behavior
        → Global

Some of your work needs it, some does not
    or you are still evaluating it
        → Skill

You use more than one model or vendor
        → Cross-model, plus one of the above per tool
```

Global is the mode all evidence in this repository was collected under. No comparison between
deployment modes has been run.

## Copies and canonical ownership

Every deployment creates a **derived copy** of the standard. That is operationally necessary — an
instruction file has to exist where the tool reads it.

Two rules keep this from turning one standard into several:

1. Copies are labelled as derived. The canonical file is
   [`standard/balanced-plain-english.md`](../standard/balanced-plain-english.md), which is itself a
   published mirror of `~/.ai/balanced-plain-english.md` in the author's environment.
2. Sync is one-way, canonical to copy, and verified with a diff. Never edit a deployed copy.

The verification command is the same in every mode:

```bash
diff <(sed -n '/^# Balanced Plain English$/,$p' <DEPLOYED_FILE>) standard/balanced-plain-english.md
```

Expected output: nothing.

Run it after any change to the standard, and after any tool update that might have rewritten a
config file. Drift is silent — a stale copy produces an agent following rules that no longer exist,
described by evidence that no longer applies to it.

## Version

All deployments should carry standard version **1.1.0**. That is the version all evidence in this
repository was collected against. A deployment running 1.0.0 is missing **Completeness before
concision** and **Technical nuance** — the two sections added specifically to fix an observed
completeness weakness.
