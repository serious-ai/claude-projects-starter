# Real estate underwriting brief

Example brief for underwriting every listing that meets a buy box.

## Who it's for

- Goal: underwrite every listing that meets my buy box, within a day of it hitting the market.
- For: the investor, who decides every offer.
- Buy box: [single-family, 3+ bedrooms, built after 1970, in these ZIP codes, listed under $X].
- Working means: every matching listing has a one-page underwrite before the investor's weekly review.
- Proved wrong if: the investor's own numbers differ from the underwrite by more than [10%] on most listings.

## Where the work happens

- New listings arrive in `listings/inbox/` as [exported CSV or listing links].
- One thread per listing, named `[address]`, writing `listings/[address].md`: comps, price history, rent estimate, repair allowance, and the numbers against the buy box.
- Underwriting model: `reference/model.md` (formulas and assumptions). Read-only.
- One reviewer thread checks the math on every underwrite.
- At most [three] listing threads at a time.

## How a thread checks its own work

- Every comp lists address, sale date, price, size and distance, with its source and the date read. Comps from the last [12] months only.
- The full price history for the subject and each comp, from the listing source.
- Paste each formula with its inputs filled in, so the math can be checked line by line.
- The reviewer thread recomputes every number and never reviews its own work.

## When something is missing

- Fewer than [three] usable comps: say so, list what was found, and stop. No stretched comps.
- A field the source doesn't show (lot size, year built, HOA) stays "unknown" with where it looked.
- Post blocked listings as Waiting on you with the missing piece.

## What needs my go-ahead

- Every offer, and any contact with an agent or seller.
- Any change to the buy box or the model.
- Paid data pulls or new data subscriptions.

## Guardrails

- Underwrites only. No messages to agents, sellers or lenders.
- Owner names and contact details from public records stay in this private repo.
- A value is a range with its assumptions, never one number.
- Every pull request shows what changed, the evidence, what was deleted, and the decisions waiting on the investor.
