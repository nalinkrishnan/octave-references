# CLAUDE.md — Octave Reference Architectures

This folder is its **own git repo** (`github.com/nalinkrishnan/octave-references`, **PUBLIC**). It sits inside the private `ccprojects` workspace but is gitignored there. Commit and push from inside this folder only.

## Purpose

A library of company-agnostic reference architectures distilled from customer builds. Two jobs:

1. **Head start.** Before starting any new customer build, search here for the closest match (`/find-reference-architecture`) and start from it.
2. **Runnable by anyone.** Each architecture runs on any environment that has credentials for its required systems. Octave runs them on our own internal stack; a prospect or teammate runs them on theirs.

## Two-layer model (public template, private values)

| Layer | Where | Tracked? |
|-------|-------|----------|
| Architecture (logic, prompts, flow exports, docs) | `architectures/<id>/` | Yes, public |
| Config templates with placeholders | `architectures/<id>/config/*.example.*`, `.env.example` | Yes, public |
| Octave's own values (internal workspace, our HubSpot props, our N8N IDs) | `architectures/<id>/config/*.local.*`, `.env` | **No**, gitignored |

When porting a customer build: the logic goes in the architecture, the customer's values are thrown away, and our internal values go in `*.local.*` so we can run it ourselves.

## Hard rules (public repo)

- **Never commit** credentials, `.env`, `*.local.*`, customer names, real people/emails, deal data, call transcripts, screenshots from real accounts, N8N workflow IDs, Trigger.dev project IDs, HubSpot portal IDs, Slack channel IDs, or Octave oIds.
- Every ID or name that differs per company is a placeholder in `config/` (e.g. `{{CRM_OWNER_PROPERTY}}`), read at runtime. No hardcoded fallbacks.
- Examples use fictional companies only: `Acme`, `acme.com`, `example.com`.
- Run `python3 scripts/scrub_check.py` before every commit. It also runs on pre-push (`git config core.hooksPath .githooks`). Customer names to catch live in `.scrub-denylist.txt` (gitignored, local only; add to it whenever a new customer build starts).
- Before pushing, also do the manual security review from the root `ccprojects/CLAUDE.md` "Public Skill Library" section.

## Adding an architecture

1. `python3 scripts/new_architecture.py <build-id>` (kebab-case, describes the *type* of build, never the customer: `abm-account-planning`, not `acme-abm`).
2. Fill `build.json` first. It drives search. Be specific in `summary`, `problem`, `systems`, `octave_capabilities`, and `tags`.
3. Write `README.md` → `ARCHITECTURE.md` → `SETUP.md`, then port code into `src/`.
4. Parameterize everything company-specific into `config/*.example.*` + `.env.example`.
5. `python3 scripts/build_catalog.py` then `python3 scripts/scrub_check.py`.
6. Commit (one architecture per commit), push.

## Session protocol

Follows the root `ccprojects/CLAUDE.md` contract: read `TODO.md` at session start, commit after each meaningful change, update `TODO.md` + `CHANGELOG.md` at session end, push.
