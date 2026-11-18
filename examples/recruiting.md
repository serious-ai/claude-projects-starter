# Recruiting brief

Example brief for building a ranked short list for each open role.

## Who it's for

- Goal: a ranked short list for each open role, every claim tied to the resume.
- For: the hiring manager, who decides who gets a call.
- Working means: each open role has a short list of [8] within two days of applications closing.
- Proved wrong if: the hiring manager's own top five overlaps the list's top five by fewer than three, three roles running.

## Where the work happens

- Role descriptions: `roles/[role]/description.md` with must-haves and nice-to-haves.
- Applications: `roles/[role]/applicants/` (resumes with contact details removed before upload).
- One thread per role, named `role-[role]`, writing `roles/[role]/shortlist.md`: rank, applicant ID, how each must-have is met, and the resume line that shows it.
- At most [two] role threads at a time.

## How a thread checks its own work

- Every must-have on the short list quotes the resume line that meets it.
- Paste the count: applications read, met all must-haves, short-listed.
- A reviewer thread checks the top [three] for each role against the resumes, and never reviews its own work.

## When something is missing

- A must-have the resume doesn't clearly show: mark it "unclear," never "met."
- A role description with no must-haves: stop and ask the hiring manager to set them.
- A file that won't open: list the applicant ID and move on.

## What needs my go-ahead

- Who gets a call, and every message to an applicant.
- Any change to the must-haves.
- Sharing the short list outside the hiring team.

## Guardrails

- Rank only on the must-haves and nice-to-haves in the role description. Never on name, age, gender, photo, address, school prestige or gaps in work history.
- Remove names and contact details before upload. Threads work from applicant IDs.
- Drafts only. No messages to applicants.
- Every pull request shows what changed, the evidence, what was deleted, and the decisions waiting on the hiring manager.
