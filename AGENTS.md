# [Project name] brief

Every thread in this project reads this file first. Replace each line in [brackets] with your own, delete the lines that don't fit, and keep every line specific enough that someone could check it. Write "run the tests and paste the summary," never "test your changes." The five headings below stay (the brief check looks for them), and the whole file stays under 16,000 characters. `docs/project-guardrails.md` explains the lines marked as guardrails.

Owner: [your name]. Last updated: [November 20, 2026].

## Who it's for

Write the goal as an outcome, who benefits, and the number that says it's working.

- Goal: [a first draft for every RFP in our pipeline, each checked against our past wins].
- For: [our sales team of three, who today spend about two days per proposal].
- Working means: [every open RFP has a draft five business days before it's due].
- Proved wrong if: [drafts need more than an hour of rework each after the first two weeks].

## Where the work happens

Name every repo, folder or file the work touches, and what one thread owns.

- Work lives in [this repo, `drafts/` for output, `reference/` for source material].
- One thread per [RFP], named `[rfp-name]`, each on its own branch with its own pull request.
- Run at most [two] threads at a time unless I say otherwise.
- Where each thread runs: [research threads] in the cloud, [anything that drafts what a person will receive] on my computer, because [our voice and safety checks run there as hooks].
- Network: [Full, because threads read ordinary websites | Limited, plus these domains]. Public data only is a rule in this file either way.
- Read-only sources: [`reference/past-wins/`, the uploaded pricing sheet]. Never edit them.

## How a thread checks its own work

List the exact checks, and the evidence each thread pastes back. You're several layers from the work, so this section matters most.

- Before calling anything done, [run `python3 scripts/check_brief.py` and any tests in the repo] and paste the command and its output into the pull request.
- Every number, claim or quote carries its source (file name and section, or a URL and the date read) in the same line.
- A second thread reviews every pull request, following `REVIEW.md`, and the reviewer never reviews its own work. One reviewer per pull request.
- Findings are Important (blocks the merge), Nit (minor, never blocks) or Pre-existing (a real problem this change didn't introduce).
- After three review-and-fix rounds, the reviewer stops and asks me instead of starting a fourth.
- A claim with no pasted evidence counts as unchecked.

## When something is missing

Say what a thread does when it hits something it doesn't have. Without this line, threads guess, fake it or stall.

- Stop at the gap and post it as Waiting on you: the exact file, site, login or decision missing, plus a one-line ask.
- Leave an unknown field marked "unknown," with what you tried. No guessing and no made-up sample data.
- If a site is blocked by the network settings, name the domain so I can decide whether to allow it.
- Keep working on the parts that aren't blocked.

## What needs my go-ahead

List what stays with you: sends, merges, money, anything a customer sees.

- Every email, post, publish and schedule. Threads write drafts only.
- Merging to the main branch, and any change to this file.
- Spending money, creating accounts, accepting terms or signing up for any service.
- [Pricing, and which clients we contact.]

## Guardrails

These hold on every run. Hooks and local permission rules don't run in cloud threads, even when committed to the repo, so each hard rule is also a GitHub check on every pull request or is set outside Claude (branch protection, connectors switched off, secrets left out).

- Drafts only. No send, post or publish tools, even when a connected account offers them.
- No patient health information (PHI), client records or client-identifiable data in any cloud thread. Use public data, our own material, or synthetic samples labeled "Sample data."
- Every pull request follows `.github/pull_request_template.md`: what changed, the evidence (commands run and their output), what was deleted, and the decisions waiting on me.
- The reviewer thread never reviews its own work, and a pull request waits until a separate reviewer says it's ready.
- No secrets, passwords or API keys in the repo or in a thread's messages.
- Local threads start without project memory. Anything a local thread must know lives in this file or the repo's root `CLAUDE.md`. Once a week the coordinator proposes moving what it saved to memory into this file, and I approve it.
- Prefer deleting over adding. Each pull request names what it removed.
