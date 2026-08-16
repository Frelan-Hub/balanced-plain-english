# Claude — Results

Standard version under test: **1.1.0**.
Method: [../methodology.md](../methodology.md). Raw record: [raw/](raw/).

Each scenario below records what was observed and what was concluded. Negative and mixed results are
kept in place.

## Summary table

| # | Scenario | Evidence | Verdict |
|---|---|---|---|
| 1 | [Simple implementation](#scenario-1--simple-implementation) | ON only | PASS |
| 2 | [Existing-code explanation](#scenario-2--existing-code-explanation) | None captured | No finding |
| 3 | [Debugging](#scenario-3--debugging) | Single condition | CONDITIONAL PASS |
| 4 | [Architecture restraint](#scenario-4--architecture-restraint) | Single condition | PASS |
| 5 | [Refactoring](#scenario-5--refactoring) | Single condition | PASS |
| 6 | [Comprehensive engineering stress](#scenario-6--comprehensive-engineering-stress-test) | ON + OFF | Mixed — depth preserved, requested sections incomplete |
| 7 | [Security and data integrity](#scenario-7--security-and-data-integrity) | ON + OFF | PASS — nuance preserved under ON |
| 8 | [Production incident](#scenario-8--production-incident) | ON + OFF | Strongest ON result, with two over-strong inferences |

---

## Scenario 1 — Simple Implementation

**Prompt:** [prompts/01](prompts/01-simple-implementation.md) · **Condition:** ON only

### Observed — ON

```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

The explanation correctly described the modulo operation and why a remainder of `0` indicates an
even number.

### Finding

The response was correct, minimal, technically precise, concise, and free of unnecessary
abstraction. No tests were added, matching the constraint.

**Verdict: PASS**

### Limitation

No OFF response was captured, so this establishes that ON behavior is acceptable — not that it
differs from OFF. Claude's unmodified behavior on a prompt this simple is likely similar.

---

## Scenario 2 — Existing-Code Explanation

**Prompt:** [prompts/02](prompts/02-code-explanation.md) · **Condition:** none captured for Claude

The responses recorded during this cycle came from a different model. They are not represented as
Claude results.

The scenario established the evaluation criteria used later: safe key lookup, strict `is True`
behavior, missing-key behavior, truthy non-boolean edge cases, and explanation scope.

**Verdict: no finding.** Retained in the suite design so a future cycle can fill the gap.

---

## Scenario 3 — Debugging

**Prompt:** [prompts/03](prompts/03-debugging.md) · **Condition:** single, unlabelled in the record

### Observed

The model identified the empty-list division-by-zero problem and proposed returning `0`.

### Finding

The technical diagnosis was correct. The chosen behavior for an empty input was an **unstated API
decision** — the prompt did not specify whether an empty input should return `0`, return `None`, or
raise.

**Verdict: CONDITIONAL PASS**

### Why this was kept

It produced the most useful lesson in the early cycle:

> Correctness includes not silently inventing behavior where the specification is ambiguous.

This is a requirement-fidelity concern, and it fed directly into the **Completeness before
concision** addition in standard v1.1.0. A response that quietly fills a spec gap is not more
concise — it is less complete, in a way that is hard to notice.

---

## Scenario 4 — Architecture Restraint

**Prompt:** [prompts/04](prompts/04-architecture-restraint.md) · **Condition:** single

### Observed

The model rejected the unnecessary infrastructure and recommended Python's standard-library
`logging`.

It correctly distinguished:

| Recommended | Rejected |
|---|---|
| Useful local logging | Logging service |
| | Centralized structured storage |
| | Monitoring dashboard |

### Finding

**Verdict: PASS**

This confirmed the scenario's target hypothesis: plain-language communication did not suppress
architectural restraint, and did not cause the model to over-correct into "never use logging." The
distinction between *useful implementation* and *unnecessary complexity* was preserved under a
"keep the answer concise" constraint.

---

## Scenario 5 — Refactoring

**Prompt:** [prompts/05](prompts/05-refactoring.md) · **Condition:** single

### Observed

```python
def filter_greater_than_ten(numbers):
    return [number for number in numbers if number > 10]
```

Names improved, loop replaced with a comprehension, behavior preserved, no classes, no configurable
threshold, no strategy abstraction.

### Finding

**Verdict: PASS**

---

## Scenario 6 — Comprehensive Engineering Stress Test

**Prompt:** [prompts/06](prompts/06-comprehensive-stress.md) · **Condition:** ON and OFF

### Observed — OFF

A strong engineering response. It identified:

- unsafe budget access
- `None` and string budget problems
- unsafe owner access
- missing IDs
- incorrect falsy handling of zero
- redundant passes

It provided a single-pass implementation and a sanity test.

It surfaced assumptions explicitly:

> "These are the points where the spec allows more than one reading."

It correctly discussed boolean-as-integer behavior in Python, `NaN` and `Infinity`, negative
budgets, and `Decimal` for financial precision.

**Weakness under OFF:** it introduced deduplication of active owner names —

```python
seen_owners = set()
```

— a business behavior the specification did not establish. The assumption was explained, but it was
still implemented rather than raised as a question.

### Observed — ON

A similarly strong engineering result. The implementation stayed compact while handling numeric
strings, zero budgets, invalid budgets, non-finite numbers, missing owners, malformed values, and
single-pass aggregation.

Technical depth was **not** reduced. Retained distinctions included:

- valid vs invalid budgets
- boolean vs integer
- finite vs non-finite values
- safe owner traversal
- assumptions around missing identifiers

**Weakness under ON:** the response did not reliably produce every explicitly requested output
section. The prompt required seven sections (A–G); not all were fully provided.

### Finding

**Verdict: mixed.**

Positive: ON preserved technical depth in the scenario most likely to expose loss of depth.

Negative, and important:

> `balanced-plain-english.md` can influence communication quality, but it should not be expected to
> guarantee complete task execution.

Task completeness belongs to execution and verification mechanisms, and to prompting — not to the
communication standard. This result is the origin of the scope boundary in
[docs/03-scope-boundaries.md](../../docs/03-scope-boundaries.md), and it is the basis for the
"Mixed" status on evaluation question 7.

Both conditions produced a requirement-fidelity defect in this scenario — OFF invented
deduplication, ON dropped requested sections. Neither condition was clean.

---

## Scenario 7 — Security and Data Integrity

**Prompt:** [prompts/07](prompts/07-security-data-integrity.md) · **Condition:** ON and OFF

### Observed — OFF

A strong response. It identified:

- lack of overwrite protection
- partial writes after mid-import failure
- duplicate IDs within one file
- missing file and row limits
- missing header validation
- non-finite float handling
- unvalidated status and owner
- CSV encoding concerns
- authentication versus authorization
- CSV formula injection

It made the technical distinctions correctly:

| Distinguished | From |
|---|---|
| Authentication | Authorization |
| Validation | Output encoding |
| Raw storage | Export-time CSV protection |
| Partial success | Transaction atomicity |

It rejected the proposed distributed infrastructure as unnecessary at the stated scale.

**Weakness under OFF:** it introduced a placeholder status set —

```python
VALID_STATUSES = {"planning", "active", "on_hold", "done"}
```

— although the prompt had already supplied a different status vocabulary. A technically plausible
but specification-inconsistent assumption.

### Observed — ON

The ON response emphasized requirement identification, ambiguity, validation boundaries, data
integrity, security implications, minimum sufficient architecture, and the distinction between
storage and presentation concerns.

Technical nuance was preserved rather than simplified away. The response remained technically
sophisticated rather than becoming "simplified engineering."

### Finding

**Verdict: PASS.**

The standard did not suppress security or data-integrity reasoning — the outcome this scenario was
specifically constructed to detect. The security distinctions most vulnerable to compression
survived under ON.

---

## Scenario 8 — Production Incident

**Prompt:** [prompts/08](prompts/08-production-incident.md) · **Condition:** ON and OFF

### Observed — OFF

A strong engineering baseline. It correctly analyzed unsafe input assumptions, budget parsing, owner
access, invalid budget handling, and redundant processing, and it distinguished current evidence
from unknown mechanism. It recommended a small corrective path rather than a distributed
architecture.

**Verdict on OFF: strong baseline.**

### Observed — ON

A materially stronger incident-analysis structure.

The reasoning was organized as an explicit chain:

```text
Observed output
    ↓
Numerical delta
    ↓
Sample-record analysis
    ↓
Possible defect class
    ↓
What cannot yet be proven
    ↓
Evidence required
    ↓
Immediate containment
    ↓
Corrective direction
```

A particularly strong statement:

> "Yesterday's output is not a trustworthy baseline."

This recognized that historical stability does not prove historical correctness — the second trap
built into the scenario.

Recommended actions included: confirming the actual parsing and aggregation function; checking
exception handling; distinguishing received from processed records; validating at the boundary;
normalizing deliberately; tracking rejection reasons; failing loudly on excessive rejection;
preserving evidence before backfilling; notifying downstream consumers; and rerunning archived
inputs after remediation.

**Recorded weaknesses under ON.** The response contained two inferences stronger than the evidence
supported:

1. It described the numerical delta as *"the signature of the core defect."* That conclusion is
   stronger than the supplied evidence proves.
2. It speculated that a swallowing mechanism — a `try/except`, an `isinstance` filter, or
   `.get(..., 0)` — must exist. Plausible hypotheses, not established by the supplied evidence.

Both are notable because they occur in the same response that explicitly separated proven from
unproven. Clear presentation of an inference does not make the inference warranted.

### Finding

Despite those caveats, this was the strongest observed evidence that the standard can improve
**engineering communication discipline without removing technical depth**.

---

## Cross-scenario observations

### Communication improvement

The strongest repeated signal:

> ON tends to communicate complex engineering reasoning with less unnecessary overhead.

Most visible in explanations, architecture decisions, incident analysis, and assumption handling.

### Engineering quality preserved

Across the observed tests, ON showed no evidence of:

- simpler but incorrect code
- suppressed edge cases
- refusal of justified complexity
- architectural under-design
- loss of technical terminology where it was needed

This is the primary success condition. The standard's main risk was that it would trade engineering
quality for readability. It did not.

### Claude's baseline is already strong

OFF was already highly capable at technical reasoning, ambiguity detection, architecture restraint,
security reasoning, and concise explanation.

The observable ON/OFF difference is therefore smaller for Claude than it might be for a model whose
default is more verbose. That is not a failure of the standard — a model that already conforms to
the target behavior has little room to visibly change. It does mean Claude is a weak instrument for
detecting the standard's effect, which is a reason to run [experiments/02](../../experiments/02-cross-model.md).

## Verdict

**Keep `balanced-plain-english.md`.**

The strongest result is not that ON produces shorter answers. It is:

> ON tends to reduce unnecessary communication overhead while preserving the technical substance
> required by the task.

Read [analysis/limitations.md](../../analysis/limitations.md) before citing any of this.
