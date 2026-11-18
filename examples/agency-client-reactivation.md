# Agency client reactivation brief

Example brief for an agency or consultancy reaching back out to past clients.

## Who it's for

- Goal: every past client gets a personal note on what changed in their market since we worked together.
- For: the agency owner, who decides which clients to contact and sends every note.
- Working means: [4] past clients reply in the first month.
- Proved wrong if: [20] notes go out and nobody replies within three weeks.

## Where the work happens

- Client list: `reference/past-clients.csv` (company, contact role, project, end date). Read-only.
- One thread per client, named `client-[company]`, on its own branch.
- Each client thread pulls public news, site changes, job posts and filings since the project ended, and writes `notes/[company].md`: three changes, each with its source and date, and how each ties to the work we did.
- One drafting thread turns approved notes into a short email draft in `drafts/[company].md`.
- At most [three] client threads at a time.

## How a thread checks its own work

- Every change cites a URL and the date read, from [2025 or 2026] only.
- The drafting thread pastes the word count of each draft (under 120 words) and the one fact it leads with.
- A reviewer thread checks each note against its sources and flags any line the source doesn't support. The reviewer never reviews its own work.
- A claim with no source counts as unchecked.

## When something is missing

- No public change since the project ended: write "nothing found" with the searches tried, and stop. No filler note.
- Contact unknown or left the company: mark it and post it as Waiting on you.
- A site that blocks access gets named with its domain.

## What needs my go-ahead

- Which clients to contact. The owner ticks them in `reference/past-clients.csv` before any draft starts.
- Every send. Threads write drafts only.
- Any mention of pricing, a new offer or a meeting.
- Merging to main and any change to this brief.

## Guardrails

- Drafts only. No email or CRM send tools, even when a connector offers them.
- No client-confidential material from past projects (reports, contracts, internal numbers) in any cloud thread. Public sources and our own case notes only.
- Personal life stays out, even when it's public.
- Every pull request shows what changed, the evidence, what was deleted, and the decisions waiting on the owner.
