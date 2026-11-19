# Guardrails that hold in a project

What we learned running a real project (a lead engine for Texas medical groups) on the Claude Projects beta, November 16 to 19, 2026, checked against the Projects docs on November 19, 2026. Use it as a checklist when you set up any project. Where this page and the docs disagree, the docs win: https://code.claude.com/docs/en/claude-projects

## 1. Decide where each thread runs, and write it down

- A thread can run in the cloud (on Anthropic's computers, laptop closed) or on your own computer through Remote Control (desktop app open, machine awake). A project can be all cloud, all local, or a mix.
- Cloud is the default for public data and volume work. Local is for anything private, anything a person will receive, and anything whose safety check is a hook.
- Name each thread's home and the reason in `AGENTS.md`, under "Where the work happens."

## 2. Know what a thread loads

| | Cloud thread | Local thread |
|---|---|---|
| Project instructions | Yes | Yes |
| Project memory | Yes | No |
| Repo's root `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/` | Yes | Yes, as a normal local session |
| Subfolder `CLAUDE.md`, repo skills, `.mcp.json` | No | Yes |
| Hooks and permission rules | No, even hooks committed to the repo | Yes, your machine's |
| Your `~/.claude` (user settings, skills, hooks) | No | Yes |
| claude.ai connectors and skills, plugins added in Project settings | Yes | Yes |

Hooks committed to a repo do run in a regular single-repo cloud session. Project threads skip them, however many repos the project has.

## 3. Turn each hook into something that holds in the cloud

For every hook or permission rule you rely on:

1. **Say it.** Write the rule into `AGENTS.md` as a line a thread can check ("run `vale drafts/` and paste the output").
2. **Check it.** Make it a GitHub check that runs on every pull request, then require that check before merging (repo Settings, Branches, add a rule, "Require status checks to pass"). A check runs no matter where the thread ran. See the example below.
3. **Must block in the moment?** If it has to stop something as it happens, like a send, that step runs as a local thread, where the hook still fires.

Example check (`.github/workflows/draft-check.yml`), failing a pull request when a draft contains a phrase you never want sent:

```yaml
name: Draft check
on: pull_request
jobs:
  drafts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Block banned phrases in drafts
        run: |
          if grep -rniE "guarantee|act now|limited time" drafts/; then
            echo "Banned phrase found in drafts/"; exit 1
          fi
```

Swap the grep for your own linter (Vale, a test suite, a script) once it works.

## 4. Keep local threads informed

- Local threads start without project memory. Anything a local thread must know goes in the project instructions or the repo's root `CLAUDE.md`.
- Once a week, ask the coordinator: "What did you save to memory that a local thread would need? Propose it as a change to AGENTS.md." Review it like any other change.
- Don't let threads rewrite the instructions on their own. Guardrail changes wait for you.

## 5. When the instructions run out of room

- The project instructions hold up to 16,000 characters.
- Keep the full brief in the repo as `AGENTS.md` (with `CLAUDE.md` pointing to it) and paste a short version into the instructions box that tells every thread to read it.
- At the limit, move rules that belong to one repo into that repo's root `CLAUDE.md`, and keep the instructions as the map: the goal, the guardrails, where things live.

## 6. Settings, with what to expect

- **Models and effort.** Set thread model and effort on purpose. The coordinator may show a model picker only, so pick its model and move on.
- **Network.** Limited allows a default list plus domains you add. Full allows everything. If threads must read ordinary websites, Limited will stall them, so move the "public data only" rule into the instructions and choose Full on purpose.
- **Thread cap.** A cap you write ("at most two at a time") is a preference Claude saves, not an enforced limit. The only hard limit is 500 new threads a day per account. Watch Project settings, Usage, for the first few days.
- **Setup script.** A cloud environment can run a setup script before each thread starts (install tools, write a user-level `CLAUDE.md`). Use it in place of SessionStart hooks.
- **Hardware.** Cloud threads use none of your computer's memory beyond the window showing them. Each local agent uses roughly 0.3 to 0.8 GB.

## 7. Data

- Projects runs on consumer plans (Pro, Max, Ultra). Anthropic's BAA doesn't cover cloud sessions or Remote Control, so keep patient health information and client-identifiable data out of every project thread.
- Every connector on your Claude account reaches every thread. Switch off the ones a thread shouldn't touch before you start.
