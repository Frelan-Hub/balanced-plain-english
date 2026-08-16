# Analysis

Interpretation of the evidence. Observations themselves live in [`evidence/`](../evidence/).

| File | Contents |
|---|---|
| [findings.md](findings.md) | Seven findings with confidence levels and their evidential basis |
| [limitations.md](limitations.md) | What the evidence cannot support, and what must never be claimed |
| [token-efficiency.md](token-efficiency.md) | Why the design should reduce tokens, why raw count is the wrong metric, and what remains unmeasured |

## Rule for this directory

Every claim must be traceable to a file in [`evidence/`](../evidence/). A claim that is not is a
defect, not a stronger conclusion.

## The three-line summary

1. Enabling the standard was associated with less unnecessary communication overhead, and with no
   observed loss of engineering quality.
2. The evidence cannot distinguish a small real effect from no effect, because Claude's baseline is
   already close to the target behavior.
3. No token measurement exists. No efficiency percentage in this repository is a result.

Read [limitations.md](limitations.md) before citing anything from here.
