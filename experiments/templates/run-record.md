# Run Record — Template

Copy this file for each scenario run. One file per scenario, containing both conditions.

Fill in what you measured. Leave a field blank and mark it "not collected" rather than estimating —
an estimate recorded in a measurement field becomes a number someone later cites as data.

---

## Identification

| Field | Value |
|---|---|
| Scenario ID | |
| Scenario name | |
| Standard version | 1.1.0 |
| Standard modified? | No / Yes (if yes, this is evidence about a different document) |
| Model family | |
| Model version | |
| Date | |
| Deployment mode | Global / Skill / System prompt |
| Runs per condition | |
| Rater | |
| Rater blind to condition? | Yes / No |

## Prompt

Record the **verbatim** prompt text. If only a specification is available, say so explicitly.

```text

```

## Condition ON

### Tokens

| Metric | Value |
|---|---|
| Input tokens | |
| Output tokens | |
| Total tokens | |

### Raw response

Store the complete unedited response at `evidence/<model>/raw/<scenario>-on.md` and link it here.
Do not paste an abridged version into this record.

### Scores

See [scoring-rubric.md](scoring-rubric.md).

| Dimension | Score | Note |
|---|---|---|
| Correctness | | |
| Completeness | | |
| Requirement fidelity | | |
| Technical precision | | |
| Technical nuance preservation | | |
| Uncertainty handling | | |
| Architecture restraint | | |
| Scope discipline | | |
| Clarity | | |
| Useful information density | | |
| Unnecessary content | | |
| Task completion | | |

## Condition OFF

### Tokens

| Metric | Value |
|---|---|
| Input tokens | |
| Output tokens | |
| Total tokens | |

### Raw response

Path: `evidence/<model>/raw/<scenario>-off.md`

### Scores

| Dimension | Score | Note |
|---|---|---|
| Correctness | | |
| Completeness | | |
| Requirement fidelity | | |
| Technical precision | | |
| Technical nuance preservation | | |
| Uncertainty handling | | |
| Architecture restraint | | |
| Scope discipline | | |
| Clarity | | |
| Useful information density | | |
| Unnecessary content | | |
| Task completion | | |

## Comparison

### Quality gate

Answer before computing any token comparison:

- [ ] ON response satisfies correctness
- [ ] ON response satisfies completeness
- [ ] ON response satisfies requirement fidelity

If any box is unchecked, the run is a **quality failure**. Record the token numbers, but do not
report them as an efficiency result.

### Token difference

```text
Raw Output Reduction %
=
(OFF output tokens − ON output tokens)
÷ OFF output tokens
× 100
```

Result:

Also record the total-token difference. The standard consumes input tokens on every ON request; an
output saving smaller than that recurring input cost is a net loss on short exchanges.

### Verdict

PASS / CONDITIONAL PASS / MIXED / FAIL / NULL

### Finding

State what was observed and what it does and does not support.

### Counter-evidence

**Required field.** Record anything the run showed that argues against the standard, or against the
expected result. If there is genuinely none, write "none observed" — do not leave it blank.

A run record with no counter-evidence field is not usable as evidence, because it cannot be
distinguished from one where counter-evidence was found and dropped.
