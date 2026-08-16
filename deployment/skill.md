# Skill Deployment

Apply the standard on demand, to specific tasks only.

Use this mode when you want the communication contract available but not always on — for example
when some of your work benefits from it and some does not.

## Installing

A ready-to-install package is in
[`skill/balanced-plain-english/`](skill/balanced-plain-english/).

Copy it to your skills directory:

```bash
cp -r deployment/skill/balanced-plain-english ~/.claude/skills/
```

Project-scoped instead of user-scoped:

```bash
cp -r deployment/skill/balanced-plain-english .claude/skills/
```

Invoke it with `/balanced-plain-english`, or let the agent select it when the task matches the
skill's description.

## How a skill differs from global deployment

| | Global | Skill |
|---|---|---|
| Applies to | Every session | Sessions where it is invoked |
| Loaded into context | Always | On demand |
| Context cost | Constant | Only when used |
| Consistency | Guaranteed | Depends on invocation |
| Best for | A default communication contract | Selective application |

The trade-off is real. On-demand loading keeps context minimal — which is the right default under a
lean-architecture principle — but a standard that is only sometimes active produces only sometimes
consistent output.

**All evidence in this repository was collected with the standard globally active.** No comparison
between global and skill deployment has been run, and there is no evidence that invocation-based
loading produces equivalent adherence. Treat skill mode as a convenience, not as an evidence-backed
equivalent.

## When skill mode is the better choice

- Some of your work benefits from the standard and some does not. Creative drafting, brainstorming,
  and exploratory writing have different communication goals than engineering work.
- You are evaluating the standard before adopting it globally.
- You share a machine or configuration with people who have not adopted it.
- Context budget is tight and the standard is only occasionally relevant.

## When global mode is better

- You want the contract to be the baseline rather than something you remember to ask for.
- You are collecting evidence and need consistent conditions across runs.
- Most of your work is technical.

## Package contents

```text
skill/balanced-plain-english/
└── SKILL.md
```

One file. The skill has no scripts, no references, and no supporting assets, because the standard is
one page of instructions with nothing to execute.

## Duplication and sync

The skill package contains a **derived copy** of the standard, not a second original. It must
contain the full text to be installable and portable — a skill that points at a file outside itself
does not survive being copied to another machine.

Canonical ownership is preserved by labelling the copy as derived and checking it:

```bash
diff <(sed -n '/^# Balanced Plain English$/,$p' deployment/skill/balanced-plain-english/SKILL.md) standard/balanced-plain-english.md
```

The `sed` range extracts from the standard's first heading to the end of file, so the check is
independent of frontmatter length. Expected output: nothing.

This check passes for the package as shipped.

Sync direction is one-way: canonical to package. Never edit the package copy directly. If the
standard is ever unfrozen and revised, update the canonical file, then regenerate the copies, then
re-run both diff checks.
