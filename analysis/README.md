# Analysis

Interpretation of the evidence. Observations themselves live in [`evidence/`](../evidence/).

| File | Contents |
|---|---|
| [findings.md](findings.md) | Findings with confidence levels and their evidential basis |
| [limitations.md](limitations.md) | What the evidence cannot support, and what must never be claimed |
| [token-efficiency.md](token-efficiency.md) | The measured result, what it does not cover, and why raw token count is still the wrong metric |

## Rule for this directory

Every claim must be traceable to a file in [`evidence/`](../evidence/). A claim that is not is a
defect, not a stronger conclusion.

## The three-line summary

1. **Measured:** on Claude Opus 5 across 20 paired scenarios, the standard cut output tokens by
   50.45% in aggregate with no material quality difference detected and 40/40 task completions.
2. **Scope:** output tokens only, one model, one author-written task set, one run per cell. Not cost,
   not latency, not statistical significance, not quality equivalence.
3. **The v1 qualitative findings still stand** and are unmodified. v2 measures the overhead reduction
   v1 could only describe.

Read [limitations.md](limitations.md) before citing anything from here.
