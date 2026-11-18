# Moving from Claude Code to a project

If you already run Claude Code on your laptop, most of your setup carries into a project, and the parts that don't are the ones people rely on most: hooks and permission rules. This page says what a cloud thread loads, what it leaves behind, and where each rule should go instead.

## What a cloud thread loads

- The project instructions (this repo's `AGENTS.md`, pasted into the project, up to 16,000 characters).
- The project memory index (`MEMORY.md`), built up as you correct threads and say "remember this, because..."
- The repo's root `CLAUDE.md`, `.claude/CLAUDE.md` and `.claude/rules/`.
- Every connector on your Claude account (all of them, in every thread), skills from your account, and plugins from Project settings.

## What it leaves behind

- Hooks. Any check you run as a hook (a linter on drafts, a block on certain commands) won't fire.
- Permission rules and `settings.json`, including environment variables set there.
- Repo skills and `.mcp.json` servers.
- `CLAUDE.md` files in subfolders.

A thread that runs on your own computer through Remote Control gets the project instructions and your local hooks, but not the project memory files. It runs while the desktop app is open and the machine is awake.

## Where each rule goes

| The rule... | Put it in |
|---|---|
| applies to every thread from the start | `AGENTS.md`, pasted as the project instructions |
| was learned along the way | project memory: correct the thread once, then say "remember this, because..." |
| is about one repo only | that repo's root `CLAUDE.md`, kept under about 200 lines |
| must hold no matter what | outside Claude: branch protection, connectors switched off, secrets left out of the environment |

## A short checklist

1. List your hooks and permission rules. For each one, decide whether it becomes a line in `AGENTS.md`, a setting outside Claude, or a reason to keep that work local.
2. Move any rule from a subfolder `CLAUDE.md` into the root one or into `AGENTS.md`.
3. Turn off every account connector a thread shouldn't touch before you create the project.
4. Keep anything that sends, posts or touches a client inbox on your own machine, where your hooks still run.
5. Use `/send-to-project` to move a running local session into the project.
6. When a workstream moves to a project, retire its old routine or scheduled task the same week, so nothing runs two ways.

## Strip what the model no longer needs

Newer models repeat fewer mistakes. While you move rules over, delete the ones written for a mistake you haven't seen in weeks. A shorter brief is easier for a thread to follow and easier for you to review.

Damon Bodine's starter kit has more on this, including a week-one plan: https://claude.ai/artifact/CvRk5oyLfDKKMngWFytFXi
