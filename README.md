# Claude Projects starter

A one-file starting point for your first Claude Project. Fill in `AGENTS.md`, connect it to a project, and send the first message below.

Built for the UCL Live lunch and learn on Claude's Projects beta, Friday, November 20, 2026, in Austin.

## Fastest start: paste one line into Claude Code

Open Claude Code (the desktop app's Code tab, the terminal, or claude.ai/code) and paste:

> Set me up with a Claude Project using https://github.com/serious-ai/claude-projects-starter. Follow its SETUP.md.

Claude asks you the five questions one at a time, writes your brief, makes a private copy of this repo in your GitHub if you want one, and tells you exactly what to paste into Projects. `SETUP.md` is the script it follows. The paths below do the same thing by hand.

## What Projects is

Projects is a feature of Claude Code (web, desktop and phone apps, left sidebar) where you talk to one main conversation, the coordinator, and give it a goal. The coordinator starts workers, called threads, for each piece of the work, runs them side by side, and tells you what's ready for your review. Every thread starts from the same project instructions, up to 16,000 characters, and that is what `AGENTS.md` in this repo holds.

The Projects folders in the Claude chat app (a set of files plus custom instructions) are a separate, older feature. Projects is in beta on the Pro, Max and Ultra plans, with a waitlist at https://claude.com/form/projects.

## Is it a project?

Go down the table. The first yes decides.

| If the work... | Use |
|---|---|
| fits in one conversation | a regular chat or session |
| is one job on a schedule, no back and forth | a scheduled task |
| is a goal that keeps producing tasks | a project |

Cloud or laptop doesn't decide it. A project's threads can run in the cloud, on your own computer, or a mix.

## Pick your path

### Path 1: No Git, no code

1. Open `AGENTS.md` in this repo (or one of the files in `examples/`) and copy the text.
2. Fill in the brackets with your own goal, folders and rules.
3. Paste it into whichever you have today: a Claude chat Project's custom instructions, a Claude Cowork project, or the instructions box when you create a Claude Project.
4. Upload the files the work needs (a folder of SOPs, proposals or client notes). Threads hand back files in the project's Library.

Read `docs/start-without-git.md` first. It covers connectors, which reach every thread.

### Path 2: GitHub

1. Click **Use this template** at the top of this page and create a private repo from it.
2. Edit `AGENTS.md` in your new repo. Replace every bracket with your own lines, or start from the closest file in `examples/`.
3. Install the Claude GitHub App on that repo: https://github.com/apps/claude/installations/new
4. In Claude Code, create a project, write a one-line goal (an outcome, like you'd hand a capable hire for a quarter), and point it at the repo.
5. Check thread model and effort in Project settings, General, and set them on purpose.

The included check (`scripts/check_brief.py`) runs on every push and fails if `AGENTS.md` loses one of its five headings or grows past 16,000 characters.

### Path 3: Already on Claude Code

Your setup carries over in part. Cloud threads load the repo's root `CLAUDE.md`, `.claude/CLAUDE.md` and `.claude/rules/`. They leave behind hooks (even ones committed to the repo), permission rules, repo skills, `.mcp.json` servers, settings and subfolder `CLAUDE.md` files. Local threads keep your hooks but start without the project memory.

- Move every rule that must hold into `AGENTS.md` (this repo's `CLAUDE.md` just points there).
- Turn each hook into a GitHub check on every pull request, or run that step as a local thread. Enforce the rest outside Claude: branch protection, connectors switched off, secrets left out of the environment.
- Use `/send-to-project` to move a running local session into a project.

Details in `docs/moving-from-claude-code.md`, and the full checklist of guardrails that hold in `docs/project-guardrails.md`.

## The first message to send

Paste this into the project conversation once it's created:

> Propose the threads you'd start for this goal and wait for my go-ahead. At most two at a time. Only post when something finishes or is blocked.

Then send one small real task (about a 20-minute job). Open the thread when it finishes, read what it assumed and what it couldn't reach, and fix that gap in `AGENTS.md` before you send more.

## What's in here

| File | What it's for |
|---|---|
| `AGENTS.md` | The brief every thread reads first. The one file you fill in. |
| `REVIEW.md` | What the reviewer thread checks: what failure looks like, severity, what to skip, the evidence bar, a three-round cap. |
| `SETUP.md` | The script Claude follows when you paste this repo's link and ask it to set you up. |
| `CLAUDE.md` | Points Claude Code at `AGENTS.md`. |
| `examples/` | Eight filled briefs, one per business goal. Copy the closest one over `AGENTS.md`. |
| `docs/` | Guardrails that hold in a project, moving from Claude Code, and starting with documents only. |
| `.github/pull_request_template.md` | What every thread's change has to show: evidence, deletions, decisions for you. |
| `scripts/check_brief.py` | Holds the brief's shape. Run `python3 scripts/check_brief.py` or pass a path. |

## Links

- Projects docs: https://code.claude.com/docs/en/claude-projects
- Projects waitlist: https://claude.com/form/projects
- Damon Bodine's Claude Projects starter kit (brief builder, prompts, week-one plan): https://claude.ai/artifact/CvRk5oyLfDKKMngWFytFXi

## Credits

Built by Chris Duff, MD, Serious AI (https://seriousai.partners).

The five questions, the "is it a project?" test and the first message come from Damon Bodine's Claude Projects workshop for Claude Community Austin at Capital Factory, November 12, 2026, and his starter kit linked above. Damon is a Claude Code Ambassador in Austin and runs the software agency Clear Road Labs. This repo is a community resource, not an official Anthropic one. Where it disagrees with the Projects docs, the docs win.

## License

Code (`scripts/`, `.github/`) is Apache-2.0, see `LICENSE`. Docs and briefs (every `.md` file) are CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
