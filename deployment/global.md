# Global Deployment

Apply the standard to every session by default.

Use this mode when you want the communication contract to be the baseline rather than something you
remember to invoke. It is the mode the standard was written for.

## Claude Code — output style

The most direct mechanism. An output style replaces the default communication instructions for every
session.

**Location:**

```text
~/.claude/output-styles/balanced-plain-english.md
```

**Format:** YAML frontmatter followed by the standard body, verbatim.

```markdown
---
name: Balanced Plain English
description: Clear, precise English with the right amount of detail
keep-coding-instructions: true
---

# Balanced Plain English

...the full text of standard/balanced-plain-english.md...
```

**`keep-coding-instructions: true` matters.** Without it, the output style replaces the harness's
coding instructions instead of layering on top of them. The standard governs *how* things are said;
it is not a substitute for the tool-use and code-editing guidance the agent needs to work. Dropping
those is a direct violation of the scope boundary — the communication layer would be silently
removing execution-layer instructions.

Select it with the `/output-style` command in an interactive terminal session, or set it in your
Claude Code configuration.

## Claude Code — instruction-file import

An alternative, if you prefer the standard to sit alongside your other governance documents rather
than in the output-style slot.

In `~/.claude/CLAUDE.md`:

```markdown
@~/.ai/balanced-plain-english.md
```

The `@` prefix is an import directive — the file's contents are loaded. A Markdown link is inert
text and loads nothing.

### Choosing between the two

| | Output style | Instruction-file import |
|---|---|---|
| Replaces default communication instructions | Yes | No — adds to them |
| Sits with other governance files | No | Yes |
| Risk of conflicting with default verbosity guidance | Lower | Higher |
| Toggleable per session | Yes, via `/output-style` | No |

The output style is cleaner, because it *replaces* the default communication guidance rather than
competing with it. The import is better if you want one place where all your instruction files are
declared.

Do not enable both. Two copies of the same rules is duplication with no benefit, and if they ever
drift you have two competing sources of truth.

## Other agents and IDEs

Any tool that accepts a persistent instruction file or system prompt can host the standard. Paste
the body of [`standard/balanced-plain-english.md`](../standard/balanced-plain-english.md) in.

Common locations:

| Tool type | Mechanism |
|---|---|
| CLI agents | Global instruction file, or system-prompt flag |
| IDE assistants | Custom-instructions or rules file |
| API integrations | The `system` parameter |
| Chat interfaces | Custom instructions or project instructions |

No adaptation is needed. The standard contains no vendor syntax. See
[cross-model.md](cross-model.md).

## Keeping the copy in sync

Global deployment creates a **derived copy** of a canonical file. That is fine — it is operationally
required — but the copy must be labelled as derived and checked, or it becomes a second competing
original.

Verify after any change to the standard:

```bash
diff <(sed -n '/^# Balanced Plain English$/,$p' ~/.claude/output-styles/balanced-plain-english.md) ~/.ai/balanced-plain-english.md
```

The `sed` range extracts from the standard's first heading to the end of file, so the check does not
depend on how many lines of YAML frontmatter your deployment uses.

Expected output: nothing.

**This check is not optional.** Drift here is silent and consequential: an agent running a stale copy
behaves according to rules that no longer exist, and the evidence collected against version 1.1.0
does not describe it. If the standard is at 1.1.0 and the deployed copy is at 1.0.0, the agent is
missing both **Completeness before concision** and **Technical nuance** — the two additions made
specifically to fix an observed completeness weakness.

Sync direction is one-way: canonical to deployed copy. Never edit the deployed copy directly.

## Verifying it is active

Ask the agent to state its active communication instructions, or give it a task whose natural
response would be padded — a trivial question, or a request it would normally preface with a summary
of what it is about to do.

Signals the standard is active:

- no restatement of your question before the answer
- no summary paragraph after the conclusion
- routine tool work not narrated step by step
- the result stated first, not last

Signals it is not:

- "Great question! Let me help you with that."
- a closing paragraph repeating what was just said
- a step-by-step account of routine work you did not ask about

## When not to use global mode

If you want the standard applied only to specific work — for example, technical communication but
not creative or exploratory drafting — use [skill deployment](skill.md) instead.
