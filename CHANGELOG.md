# Changelog

## 2026-09-29
- Restructured into groups: `architectures/<group>/<build>/`. Each group has `GROUP.md`, `group.json` (axes, trigger types), and `shared/` for cross-build work.
- Created 4 groups and 30 stub builds: abm (16: clay/claude/cargo/n8n × slack/salesforce/hubspot/custom), outbound (8), extract-insights (2), sales (4).
- Decisions: ABM trigger list confirmed; extract-insights platform `tbd`; sales destination `chat`.
- Catalog renders a platform × destination (or platform × job) grid per group; `new_group.py` added; `new_architecture.py` now takes a group.
- Scaffolded the repo: `_template/`, `scripts/` (catalog builder, scaffolder, scrub check), pre-push scrub hook, `/find-reference-architecture` and `/new-reference-architecture` skills.
- Public/private split: architecture + `*.example.*` configs are public; `*.local.*`, `.env`, and `.scrub-denylist.txt` stay local.
