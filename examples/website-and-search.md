# Website and search brief

Example brief for working through a site audit, one reviewable change at a time.

## Who it's for

- Goal: fix every issue our site audit finds, one change at a time.
- For: the business owner and the site's visitors, starting with [the service pages that bring in leads].
- Working means: the audit's open issue count drops each week and no fix breaks a page.
- Proved wrong if: fixes keep getting reverted, or search traffic to fixed pages drops for four straight weeks.

## Where the work happens

- Site source: this repo. Audit export: `reference/audit-[date].csv`. Read-only.
- One thread per fix, named `fix-[issue-id]`, each opening its own pull request. One issue per pull request.
- Work order: broken links and missing titles first, then page speed, then content gaps.
- At most [two] fix threads at a time.

## How a thread checks its own work

- Build the site locally with [`npm run build`] and paste the last lines of output.
- Paste a before and after for the issue: the audit row, and the fixed tag, link or score.
- For a page change, paste a screenshot of the page at phone and desktop width.
- A reviewer thread checks every pull request, and the reviewer never reviews its own work.

## When something is missing

- An issue that needs a decision (redirect target, which page to keep): stop and post it as Waiting on you with the options.
- An issue that needs access the thread doesn't have (hosting settings, DNS, analytics): name it and move to the next issue.
- Copy that needs facts the site doesn't state (prices, hours, credentials): leave a marked gap. Never make it up.

## What needs my go-ahead

- Every merge to the live site.
- Deleting a page, changing a URL, or adding a redirect.
- Any new claim about the business, its people or its results.
- DNS, hosting and analytics settings.

## Guardrails

- Pull requests only. No direct pushes to main. Branch protection holds this outside Claude.
- No secrets or API keys in the repo or in pull requests.
- One issue per pull request, so each change is easy to review and undo.
- Every pull request shows what changed, the evidence, what was deleted, and the decisions waiting on the owner.
