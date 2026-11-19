# Healthcare lead engine brief

Example brief, adapted from a real project that went live November 16, 2026. Swap in your own state, practice size and offer.

## Who it's for

- Goal: personal first-touch material for every independent medical group in [Texas] with 10 to 100 clinicians.
- For: the owner, who approves every send. Each first email carries something built for that practice from public data, plus a link to a free tool the practice can run on its own files.
- Working means: [3] first conversations a week.
- Proved wrong if: sends go out and no conversations follow after the first few weeks.

## Where the work happens

| # | Thread | Runs | Why there |
|---|---|---|---|
| 1 | Market count | Cloud | Public CMS and AHRQ data only |
| 2 | Practice profiles | Cloud | Public web and CMS files |
| 3 | Free tool | Local, on the owner's computer | The point is that a practice's files never leave the computer |
| 4 | Reads and first-email drafts | Local | The owner's voice and format checks run as local hooks |
| 5 | Partner list | Cloud | Public web |

- Market count: from the CMS Doctors and Clinicians file and AHRQ's group practice linkage file, count groups by clinician band and system affiliation. Output `segments/groups.csv` and `segments/README.md` with the counts, file versions and release dates.
- Practice profiles: one file per group in `profiles/`, with service mix from public Medicare data against same-specialty peers, payers listed on the site, open billing or coding roles (2025 and 2026 posts only) and the practice administrator. Every field carries its source URL and the date read.
- Reads and drafts: one file per practice in `drafts/[week]/`, a one-screen read plus a first email under 90 words.
- Each thread on its own branch with its own draft pull request.
- Network access: Full, because profiles read practice websites, which Limited blocks. Public data only is a rule in this brief, not a network setting.

## How a thread checks its own work

- Paste into the pull request: the exact commands run and their output, row counts, and file versions with release dates.
- The free tool ships with a test that fails the build on any network request, and the pull request shows that test passing.
- A second thread reviews every pull request, and the reviewer never reviews its own work. Each fix the reviewer asks for becomes a rule in this brief.
- A claim with no pasted evidence counts as unchecked.

## When something is missing

- Stop at the gap and post it as Waiting on you: the exact file, host or decision missing, plus a one-line ask.
- A blocked download gets named with its domain, so the owner can decide whether to allow it.
- Real data or a named gap, every time. A field the thread can't source stays "unknown," and a recipient whose address the source doesn't support goes back to "unknown."

## What needs my go-ahead

- Every send, post, publish and schedule. Drafts go to the repo.
- Merging to main, making any repo public, and any change to this brief.
- Creating accounts, accepting terms, and any paid data or scraping run.
- Which partners to contact, picked from the partner list.

## Guardrails

- Drafts only. No send tools, even when a connector offers them.
- No patient health information and no real patient data, ever. Public CMS files are aggregate and de-identified. Every sample is synthetic and labeled "Sample data," and a finding from sample data never appears as evidence in a draft.
- Practice names stay in this private repo and in drafts, never on a public surface.
- Every claim about a practice rests on a dated 2025 or 2026 source, cited inline. Payer or vendor statistics carry their source in the same sentence.
- One personal read per practice, sent only to the person it was made for.
- Each pull request lists what was added, what was deleted, and what the owner needs to decide.
- Threads on Opus at high effort. At most [three] threads at a time, a preference the owner checks against plan usage.
- Local threads start without project memory, so anything the drafting thread must know lives in this brief.
