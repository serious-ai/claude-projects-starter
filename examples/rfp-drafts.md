# RFP drafts brief

Example brief for drafting every proposal in the pipeline against past wins.

## Who it's for

- Goal: a first draft for every RFP in the pipeline, each checked against our past wins.
- For: the sales lead, who owns pricing and sign-off.
- Working means: every open RFP has a draft five business days before it's due.
- Proved wrong if: drafts need more than an hour of rework each after the first two weeks.

## Where the work happens

- Open RFPs: `rfps/[name]/request.pdf`, plus `rfps/[name]/notes.md` with the due date and our contact.
- Past wins: `reference/wins/` (proposals that won, with the client's feedback). Read-only.
- One thread per RFP, named `rfp-[name]`, writing `rfps/[name]/draft.md` and `rfps/[name]/compliance.md`.
- One reviewer thread checks every draft.
- At most [two] RFP threads at a time, earliest due date first.

## How a thread checks its own work

- `compliance.md` lists every requirement in the RFP with the section of the draft that answers it. Paste the count: requirements found, answered, open.
- Every claim about our results cites the past win it came from (file and section).
- Paste the word or page count against the RFP's limit.
- The reviewer thread reads the RFP fresh, checks the compliance list, and never reviews its own work.

## When something is missing

- A requirement we have no past answer for: leave a marked gap in the draft and list it as Waiting on you.
- A question only the client can answer: draft the clarifying question for the sales lead to send.
- Pricing sections stay blank with the inputs the sales lead needs to fill them.

## What needs my go-ahead

- Pricing, terms and staffing commitments.
- Submitting anything, and every message to the client.
- Any claim about a past client by name.

## Guardrails

- Drafts only. No submit or send tools.
- No client-confidential numbers from past projects unless that client allowed reuse.
- Every pull request shows what changed, the evidence, what was deleted, and the decisions waiting on the sales lead.
