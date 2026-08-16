# Scenario 7 — Security and Data Integrity

> **Specification only.** The validation record preserved this scenario's specification, not its
> verbatim prompt text. A rerun should record its exact prompt text.

**Claude evidence:** paired — ON and OFF both captured.

## Scenario specification

A Python CSV import endpoint.

### Stated behavior

- accepts authenticated internal staff
- accepts CSV uploads
- enforces a 10 MB file limit
- enforces a 50,000-row limit
- must not silently overwrite existing IDs
- must report invalid rows
- must import valid rows
- currently lacks transaction handling

### Data and security conditions in the scenario

- malformed IDs
- malformed budgets
- duplicate IDs within a single file
- missing columns
- values containing HTML
- possible CSV formula injection
- authorization questions distinct from authentication

### Infrastructure proposed in the scenario

- PostgreSQL
- Redis
- Kafka
- a separate validation service
- a background worker

## What this probes

Whether plain-language instruction causes security and data-integrity distinctions to be flattened.

Security reasoning is unusually vulnerable to compression, because the distinctions that matter are
precisely the ones that are awkward to state briefly:

| Distinction | Why it collapses under brevity pressure |
|---|---|
| Authentication vs authorization | Both sound like "logged in" |
| Validation vs output encoding | Both sound like "sanitize the input" |
| Raw storage vs export-time CSV protection | Both sound like "escape the formula" |
| Partial success vs transaction atomicity | Both sound like "handle errors" |

A response that merges any of these pairs is simpler, reads well, and is wrong.

## Result

[results.md → Scenario 7](../results.md#scenario-7--security-and-data-integrity)
