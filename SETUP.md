# Set up a project from this template (instructions for Claude)

Someone pasted this repo's link into Claude Code and asked you to set them up. Your job: interview them, write their `AGENTS.md`, put it where their project can use it, and tell them the last few clicks. Many people doing this have never used GitHub, so explain each step in plain words.

## 1. Interview, one question at a time

Ask each question on its own and wait for the answer. Offer the closest file in `examples/` as a starting point when their goal matches one.

1. **What's the goal?** An outcome for the next quarter, who benefits, and how they'd know it's working. If they give a task ("research clinics"), ask what that task is for.
2. **When a worker hits something it doesn't have, what should it do?** Ask this one early, because people skip it. The default answer: stop, post the exact file, site or decision it needs, and keep working on what isn't blocked.
3. **Where does the work happen?** Which folders, files or repos, and what one worker owns. Which parts need their own computer (private files, anything that sends), and which can run in the cloud.
4. **How should a worker check its own work?** The exact checks, and the evidence it pastes back.
5. **What stays with you?** Sends, merges, money, accounts, anything a customer sees.
6. **GitHub or no GitHub?** If they don't know, explain in one line: GitHub is a free place to keep the brief and the work, where every change is recorded, reviewed and undoable. Either path works.

Done when all six have an answer you could turn into a checkable line.

## 2. Write their AGENTS.md

- Start from `AGENTS.md` in this repo (or the example they picked). Keep the five `##` question headings and the Guardrails section. Replace every bracket with their answers and delete lines that don't fit.
- Copy `REVIEW.md` alongside it and fill in one sentence on what failure looks like for them.
- Every line should be checkable: "run the tests and paste the summary," never "test your changes."
- Stay under 16,000 characters. Run `python3 scripts/check_brief.py <path>` if you can, or check the five headings and the length yourself.
- Show them the finished brief and ask for changes before you save it anywhere.

Done when the check passes and they've said the brief looks right.

## 3. Put it somewhere

**With GitHub**, if the `gh` command is installed and signed in (`gh auth status`):
1. Propose a repo name and say it will be private. Wait for a yes.
2. `gh repo create <name> --template serious-ai/claude-projects-starter --private --clone`
3. Write their brief over `AGENTS.md` in the new repo, commit, and push.
4. Ask them to install the Claude GitHub App on that repo: https://github.com/apps/claude/installations/new (this is their click).

If `gh` isn't installed or signed in, offer to walk them through it (`brew install gh`, then `gh auth login`), or switch to the no-GitHub path. Never create a GitHub account for them.

**Without GitHub:** save the brief as `AGENTS.md` in a folder they choose, and show the full text so they can copy it.

Done when the brief is saved (and pushed, with GitHub) and they have the full text in front of them.

## 4. Hand over the last steps

Tell them, in this order:
1. Open Claude Code (web, desktop or phone app) and choose **Projects** in the left sidebar. If they don't have it yet, join the waitlist at https://claude.com/form/projects and paste the brief into a Claude chat Project or Cowork project until access lands.
2. Create a project, and pick the repo if they made one.
3. Paste into Project settings, Memory, Project instructions: the whole brief with no repo. With a repo, a short version is enough: the goal, the guardrails, and "Read AGENTS.md in the repo first."
4. In Project settings, General, set thread model and effort on purpose.
5. Send this first message: "Propose the threads you'd start for this goal and wait for my go-ahead. At most two at a time. Only post when something finishes or is blocked."
6. Give it one small real task first (about 20 minutes of work), then read what it assumed before sending more.

Point them to `docs/project-guardrails.md` for what holds in cloud threads and what doesn't. Done when they've seen all six steps and know which ones are their clicks.

## Rules for you

- Ask before creating anything in their accounts. Never create accounts, accept terms or enter passwords for them.
- No secrets, passwords or API keys in the brief or the repo.
- No patient health information or client records in the brief. Projects runs on consumer plans, and Anthropic's BAA doesn't cover project threads.
