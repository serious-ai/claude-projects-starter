# Starting without Git

You don't need GitHub or any code to use a project. Documents work fine, and this page is the path for that.

## Start with a folder you already keep

1. Pick one folder of documents you keep coming back to: SOPs, proposals, client notes, listings, resumes.
2. Pick one goal that produces documents from it. "Turn our SOPs into a searchable playbook, one page per process, with the gaps flagged" is a good shape.
3. Copy `AGENTS.md` from this repo (or the closest file in `examples/`), fill in the brackets, and paste it as the instructions.
4. Upload the folder, or connect a Drive folder. Threads hand back files in the project's Library.
5. Send the first message: "Propose the threads you'd start for this goal and wait for my go-ahead. At most two at a time. Only post when something finishes or is blocked."

The same brief works today in a Claude chat Project (as its custom instructions) or a Claude Cowork project, so you can start before your Projects access lands.

## Switch off connectors first

Every connector on your Claude account reaches every thread. If your account is connected to email, a calendar, a CRM or a shared drive, a thread can see it and may be able to act in it.

Before you create the project:

- Open your Claude account's connector settings and list what's connected.
- Switch off anything a thread shouldn't read or touch for this goal.
- Keep anything that can send, post or delete switched off unless the goal needs it, and even then keep "drafts only" in the brief.

Switching a connector off holds every time, which a line in the brief can't promise.

## Keep sensitive data out

Projects runs on consumer plans (Pro, Max and Ultra), which sit under Anthropic's Consumer Terms. Anthropic's business associate agreement (BAA) doesn't cover cloud sessions or Remote Control. Keep patient health information, client records and anything that identifies a client out of a project today. Check the plan, the terms and the BAA scope before any client work goes near it: https://code.claude.com/docs/en/legal-and-compliance

## When you outgrow it

Once you want a record of every change and an undo, put the documents in a private GitHub repo made from this template. Each thread's work then lands as a pull request you can read and approve.
