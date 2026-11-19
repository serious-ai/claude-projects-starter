# Review instructions

The reviewer thread reads this file before it reviews a pull request. `AGENTS.md` (and `CLAUDE.md`) hold the project itself: the goal, the stack, the conventions. This file is for review alone, so keep project context out of it. Replace each line in [brackets] with your own.

Adapted from the REVIEW.md example in Anthropic's Code Review docs (claude.com/product/code-review) and their "How the Claude Code team does code review" webinar, November 2026.

## What failure looks like here

[A change that sends something to a customer without approval, leaks client data, or can't be rolled back.]

## Severity

- **Important:** a real problem to fix before merging. It blocks the merge.
- **Nit:** minor, worth fixing but never blocking.
- **Pre-existing:** a real problem this change didn't introduce. Note it, don't block on it.

## Cap the nits

Report at most [five] Nits per review.

## Do not report

- Anything CI already checks.
- [Generated files under `[path]/`.]
- [Formatting, wording taste, anything else the team keeps dismissing.]

## Evidence

Each finding cites a `file:line` and says what happens. A claim about behavior needs that citation, never an inference from a name.

## Rounds

- One reviewer per pull request, with every lens inside it. A second review bot gives conflicting advice.
- After three review-and-fix rounds, stop and ask the person who asked for the change to step back and decide.
- A re-review covers only what changed since the last round. Drop findings already posted.
- When a finding is one of a pattern, say so once and list the places.

## Keep it current

When the same review comment keeps coming back, add a line here. When a change has to be rolled back, save it as a test case for the reviewer: the repo, the commit, the file and line, and what the reviewer should have said.
