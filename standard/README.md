# Canonical Standard

This directory holds the standard itself and nothing else.

| File | Role |
|---|---|
| [`balanced-plain-english.md`](balanced-plain-english.md) | The standard, verbatim |

## Version

**Standard version: 1.1.0 — frozen.**

Version numbering is recorded here rather than inside the standard, so the standard file stays a
clean, portable, paste-anywhere document with no repository metadata in it.

| Version | Change | Reason |
|---|---|---|
| 1.0.0 | Initial standard | — |
| 1.1.0 | Added **Completeness before concision** and **Technical nuance**; extended the quality check from 7 items to 9 | The first stress-test cycle exposed a recurring completeness weakness and a risk that plain language would be read as permission to simplify away engineering detail |

Version 1.1.0 is the version all evidence in this repository was collected against — both the v1
qualitative validation and the [v2 token efficiency benchmark](../evidence/claude/benchmark-v2/README.md).

The standard was **not modified** for or during the v2 benchmark. Keeping it fixed is what makes the
two evidence sets comparable.

## Frozen

The standard is deliberately frozen at 1.1.0. The recommendation from the validation cycle was to
stop adding rules and start collecting evidence.

Adding prose to a communication standard is the wrong response to most observed failures. When a
test shows an agent omitting a requested section, failing to run tests, or not writing a file, the
defect belongs to the execution or validation layer. Fixing it here makes the standard longer,
less portable, and quietly turns it into an engineering-control policy — which is exactly the
failure mode this project is trying to avoid.

Conditions for unfreezing:

1. Evidence from an additional model family or scenario set shows a **communication** defect.
2. The defect is not attributable to execution, validation, or governance.
3. The smallest sufficient fix is a change in expression rules, not added process.

## Source of truth

For the author's AI operating system, the canonical file is:

```text
~/.ai/balanced-plain-english.md
```

The copy in this directory is a **published distribution mirror**. Sync is one-way: upstream to
repository. For anyone outside that environment, this repository is the reference copy.

This preserves single canonical ownership — one authoritative file, with a derived copy that is
explicitly labelled as derived rather than allowed to become a second competing original.

Verification that this copy is unmodified:

```bash
sha256sum ~/.ai/balanced-plain-english.md standard/balanced-plain-english.md
```

Both must produce `62aa7ca170421a8d0152c6326f31c618ca7a2d056688fda440d8f33d5bac2341`.

## Reading it

The standard is one page. Read it directly rather than reading a summary of it. Everything else in
this repository is evidence, analysis, or installation instructions for that one page.
