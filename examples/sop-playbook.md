# SOP playbook brief

Example brief for turning scattered SOPs into one searchable playbook. Works without Git: upload the folders and the pages come back in the Library.

## Who it's for

- Goal: turn our SOPs into a searchable playbook, one page per process, with the gaps flagged.
- For: the operations lead, and every new hire who needs to find how a process runs.
- Working means: each department has a playbook section with an index, and every gap is on one list.
- Proved wrong if: the team keeps asking the same "how do we..." questions a month after the playbook ships.

## Where the work happens

- Source documents: one uploaded folder per department ([front desk, billing, scheduling, onboarding]). Read-only.
- One thread per department folder, writing `playbook/[department]/[process].md`.
- Page format: purpose, who owns it, when it runs, the steps, the tools used, and the source document it came from.
- One thread builds `playbook/index.md` and `playbook/gaps.md` once the department threads finish.
- At most [two] department threads at a time.

## How a thread checks its own work

- Every page names its source document and section. A step with no source is marked "not in the SOPs."
- Each department thread pastes a count: source documents read, pages written, gaps found.
- A reviewer thread spot-checks [three] pages per department against the sources, and never reviews its own work.

## When something is missing

- Two SOPs that disagree: write both versions on the page, flag it in `gaps.md`, and ask which one holds.
- A process mentioned but never written down: add it to `gaps.md` with where it was mentioned.
- A file that won't open: name it and move on.

## What needs my go-ahead

- Which gaps to fix, and who owns each one.
- Any change to how a process runs. The playbook records what's written today.
- Sharing the playbook outside the operations team.

## Guardrails

- No customer, patient or employee records in uploads. Remove names and account details before a folder goes in.
- Threads write new pages only. Source documents stay untouched.
- Check which connectors are on before starting, and switch off any a thread shouldn't touch.
- Each batch of pages lists what was added, what was dropped as duplicate, and the decisions waiting on the operations lead.
