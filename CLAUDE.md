# CLAUDE.md — Octave Reference Architectures

This folder is its **own git repo** (`github.com/nalinkrishnan/octave-references`, **PUBLIC**). It sits inside the private `ccprojects` workspace but is gitignored there. Commit and push from inside this folder only.

## Purpose

A library of company-agnostic reference architectures distilled from customer builds. Two jobs:

1. **Head start.** Before starting any new customer build, search here for the closest match (`/find-reference-architecture`) and start from it.
2. **Runnable by anyone.** Each architecture runs on any environment that has credentials for its required systems. Octave runs them on our own internal stack; a prospect or teammate runs them on theirs.

## Structure: groups and architectures

- **Group** (`architectures/<group>/`) = a GTM job: `abm`, `outbound`, `extract-insights`, `sales`. Holds `GROUP.md` (the job, shared input/output contract, conventions), `group.json` (axes + trigger types), and `shared/` (components every build uses).
- **Architecture** (`architectures/<group>/<build-id>/`) = that job on one platform, delivering to one destination. Platform-specific by design. Ids follow `<platform>-<job>-<destination>` where the pattern fits (`clay-abm-slack`, `n8n-email-sequencer`, `llm-callprep`).

**Working at the group level:** when a change applies across a group (ranking rubric, output schema, gate rules, a new trigger type), make it once in `GROUP.md` / `shared/`, then check every build whose `build.json` → `uses_shared` lists that component. Don't copy shared logic into individual builds; reference it.

Status per build: `stub` → `draft` → `tested` → `production`. Only claim `tested` after an end-to-end run on a real environment.

## Two-layer model (public template, private values)

| Layer | Where | Tracked? |
|-------|-------|----------|
| Architecture (logic, prompts, flow exports, docs) | `architectures/<group>/<id>/` | Yes, public |
| Config templates with placeholders | `…/<id>/config/*.example.*`, `.env.example` | Yes, public |
| Octave's own values (internal workspace, our HubSpot props, our N8N IDs) | `…/<id>/config/*.local.*`, `.env` | **No**, gitignored |

When porting a customer build: the logic goes in the architecture, the customer's values are thrown away, and our internal values go in `*.local.*` so we can run it ourselves.

## Hard rules (public repo)

- **Never commit** credentials, `.env`, `*.local.*`, customer names, real people/emails, deal data, call transcripts, screenshots from real accounts, N8N workflow IDs, Trigger.dev project IDs, HubSpot portal IDs, Slack channel IDs, or Octave oIds.
- Every ID or name that differs per company is a placeholder in `config/` (e.g. `{{CRM_OWNER_PROPERTY}}`), read at runtime. No hardcoded fallbacks.
- Examples use fictional companies only: `Acme`, `acme.com`, `example.com`.
- Run `python3 scripts/scrub_check.py` before every commit. It also runs on pre-push (`git config core.hooksPath .githooks`). Customer names to catch live in `.scrub-denylist.txt` (gitignored, local only; add to it whenever a new customer build starts).
- Before pushing, also do the manual security review from the root `ccprojects/CLAUDE.md` "Public Skill Library" section.

## Adding an architecture

1. `python3 scripts/new_architecture.py <group-id> <build-id>` (kebab-case, platform + job + destination, never the customer: `clay-abm-slack`, not `acme-abm`). New job type? `python3 scripts/new_group.py <group-id> "Title"` first.
2. Fill `build.json` first. It drives search. List the group `shared/` components it relies on in `uses_shared`. Be specific in `summary`, `problem`, `systems`, `octave_capabilities`, and `tags`.
3. Write `README.md` → `ARCHITECTURE.md` → `SETUP.md`, then port code into `src/`.
4. Parameterize everything company-specific into `config/*.example.*` + `.env.example`.
5. `python3 scripts/build_catalog.py` then `python3 scripts/scrub_check.py`.
6. Commit (one architecture per commit), push.

## Session protocol

Follows the root `ccprojects/CLAUDE.md` contract: read `TODO.md` at session start, commit after each meaningful change, update `TODO.md` + `CHANGELOG.md` at session end, push.
