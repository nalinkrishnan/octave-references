# Octave Reference Architectures

Company-agnostic blueprints for GTM automations built on [Octave](https://octavehq.com). Each architecture started as a real build, was stripped of anything customer-specific, and was rebuilt to run on any environment that has credentials for the systems it needs.

Use them to:

- **Get a head start.** Find the build closest to what you need, copy it, fill in your credentials and config.
- **See how the pieces fit.** Every architecture documents its data flow, the systems it touches, and the decisions behind it.
- **Run them yourself.** Nothing here is tied to one company's workspace, CRM, or IDs.

## Catalog

See [CATALOG.md](CATALOG.md) for the full index (generated from each architecture's `build.json`). Machine-readable version: [catalog.json](catalog.json).

## Repo layout

```
architectures/<build-id>/   one folder per architecture type
  README.md                 what it does, who it's for, what you need
  build.json                metadata used for search + the catalog
  ARCHITECTURE.md           data flow, components, design decisions
  SETUP.md                  step-by-step: credentials, config, deploy, test
  .env.example              every credential the build reads (no values)
  config/                   company-specific settings, as templates
  src/                      code, workflow exports, prompts, agent configs
  diagrams/                 optional visuals
_template/                  starting point for a new architecture
scripts/                    catalog builder, scaffolder, scrub check
```

## Using an architecture

1. Pick one from [CATALOG.md](CATALOG.md) and read its `README.md` → `SETUP.md`.
2. Copy `.env.example` to `.env` and fill in your credentials. `.env` is gitignored.
3. Copy each file in `config/` from `*.example.*` to its real name and fill in your values (workspace IDs, CRM property names, channel IDs, and so on).
4. Follow `SETUP.md` to deploy and test on a small batch before running anything at scale.

## Company-agnostic rules

Every architecture in this repo follows these rules. PRs that break them get sent back.

- **No credentials, ever.** Secrets are read from environment variables named in `.env.example`.
- **No hardcoded IDs.** Workspace IDs, workflow IDs, CRM property names, list IDs, channel IDs, sender IDs all live in `config/` templates with placeholder values.
- **No customer data.** No company names, people, emails, deal data, transcripts, or screenshots from a real account. Examples use fictional companies (`acme.com`, `example.com`).
- **Systems are named, not assumed.** `build.json` lists every system required; `SETUP.md` explains how to swap the swappable ones (e.g. HubSpot ↔ Salesforce).

Run `python3 scripts/scrub_check.py` before every push. The pre-push hook runs it automatically once enabled (`git config core.hooksPath .githooks`).

## Contributing a new architecture

```bash
python3 scripts/new_architecture.py <build-id>   # copies _template/
# fill in the files, then:
python3 scripts/build_catalog.py                  # regenerates CATALOG.md + catalog.json
python3 scripts/scrub_check.py                    # must pass
```

## License

MIT. See [LICENSE](LICENSE).
