# Scoring Rubric — Template

For use with [run-record.md](run-record.md).

## Scale

Four points. Deliberately coarse — a finer scale implies a precision that qualitative judgment does
not have.

| Score | Meaning |
|---|---|
| 3 | Fully satisfied |
| 2 | Satisfied with a minor defect |
| 1 | Substantially defective |
| 0 | Failed |

Record a one-line justification for every score. A score without a reason is not reviewable, and an
unreviewable score is an opinion.

## The governing rule

> A shorter response is **not** automatically better.
>
> Complete and technically correct first; concise and clear second.

Score the engineering dimensions before reading the communication dimensions. This ordering matters:
a well-written response is persuasive, and reading it as prose first biases the correctness
assessment that follows.

## Engineering dimensions

### Correctness

Is the technical content right?

| 3 | No technical errors |
| 2 | A minor error that does not change the outcome |
| 1 | An error that would cause incorrect behavior |
| 0 | Fundamentally wrong |

### Completeness

Are all required elements present?

| 3 | Every explicitly requested output, section, and element is present |
| 2 | All substantive content present; a requested structural element missing |
| 1 | A required substantive element missing |
| 0 | Largely incomplete |

### Requirement fidelity

Does it match the specification, without adding to it or subtracting from it?

| 3 | Follows the spec; surfaces ambiguities rather than silently resolving them |
| 2 | An assumption made and explicitly stated |
| 1 | An assumption made without being stated, or a supplied constraint contradicted |
| 0 | Substantially different from what was asked |

Note both failure directions. Inventing unrequested behavior scores here, and so does dropping
requested behavior.

### Technical precision

| 3 | Distinctions stated accurately; terminology exact |
| 2 | Slight imprecision without practical consequence |
| 1 | A distinction blurred in a way that could mislead |
| 0 | Imprecise throughout |

### Technical nuance preservation

Were edge cases, uncertainty, and necessary complexity retained?

| 3 | Relevant edge cases, constraints, and complexity preserved and explained |
| 2 | A minor edge case omitted |
| 1 | A material edge case or technical distinction simplified away |
| 0 | Substance removed in favor of readability |

Score 1 or below is the primary failure mode this project exists to detect. Note it prominently.

### Uncertainty handling

| 3 | Known, inferred, unproven, and needs-verification are clearly separated |
| 2 | Uncertainty acknowledged but not clearly bounded |
| 1 | An inference presented more confidently than the evidence supports |
| 0 | Speculation presented as fact |

Judge calibration, not presentation. A clearly formatted over-confident claim still scores 1. Both
recorded ON weaknesses in the Claude incident scenario are of this kind.

### Architecture restraint

| 3 | Minimum sufficient solution; unnecessary infrastructure rejected; justified mechanisms retained |
| 2 | Slightly more or less than necessary |
| 1 | Clear over-engineering, or under-design from over-correction |
| 0 | Unjustified infrastructure accepted, or a necessary mechanism refused |

Score both directions. Refusing a justified mechanism is a failure, not restraint.

## Communication dimensions

### Scope discipline

| 3 | Answers the question asked; no unrequested expansion |
| 2 | Minor adjacent content that does not help |
| 1 | Substantial drift beyond the question |
| 0 | Largely off-target |

### Clarity

| 3 | Structure and reasoning easy to follow; relationships explicit |
| 2 | Understandable with effort |
| 1 | Structure obscures the reasoning |
| 0 | Hard to follow |

### Useful information density

| 3 | Nearly all content is decision-relevant |
| 2 | Some padding |
| 1 | Substantial padding around a correct answer |
| 0 | Mostly overhead |

Judged, not computed. This is not a token measurement, and must not be reported as one.

### Unnecessary content

Count the occurrences. Counting is more reliable than judging here.

```text
Restating the question           □
Repeating the conclusion         □
Introductory framing             □
Narrating routine work           □
Caveats that change no decision  □
Jargon adding no precision       □
Explaining obvious code          □
Same reasoning repeated          □
Invented framework or labels     □
```

| 3 | 0–1 occurrences |
| 2 | 2–3 |
| 1 | 4–6 |
| 0 | 7+ |

### Task completion

| 3 | Every element of the task was actually done |
| 2 | Done with a minor gap |
| 1 | Substantially incomplete |
| 0 | Not done |

Scored separately from communication quality by design. A response can be excellently expressed and
incomplete — that combination was observed under ON in the comprehensive stress test, and it belongs
to the execution layer, not the communication layer. See
[docs/03-scope-boundaries.md](../../docs/03-scope-boundaries.md).

## Aggregation

Report engineering and communication subtotals **separately**. Do not produce a single combined
score.

A combined score allows a communication gain to conceal an engineering loss, which is precisely the
trade this standard forbids. Keeping them apart is what makes the result readable:

```text
Communication ↑  +  Engineering →   = the intended outcome
Communication ↑  +  Engineering ↓   = failure, regardless of the total
```

## Percentages

If converting to percentages for a summary scorecard, label the result a **rubric**, not a
measurement, everywhere it appears — and state the rater count and blinding status alongside it.

See [evidence/claude/scorecard.md](../../evidence/claude/scorecard.md) for the required framing.
