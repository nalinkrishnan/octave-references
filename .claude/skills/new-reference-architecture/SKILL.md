---
name: new-reference-architecture
description: Port a finished customer build into the public octave-references library as a company-agnostic reference architecture. Scaffolds from _template, strips customer specifics, parameterizes IDs into config templates, writes build.json + docs, rebuilds the catalog, and runs the scrub check. Use when asked to "add this to reference architectures", "make this a reference build", "port this build", "genericize this build".
---

# New Reference Architecture

The library is a **public** repo. Every step here is about getting the logic in and keeping the customer out.

## 1. Decide: new or extend

Run `/find-reference-architecture` against the source build. If an existing architecture covers the same GTM job, extend it (add a variant section, new config options, bump `derived_from_builds`) instead of creating a near-duplicate.

## 2. Scaffold

```bash
python3 scripts/new_architecture.py <build-id>
```

`build-id` names the *type* of build, never the customer (`inbound-reverse-email`, not `acme-prometheus`). Add the customer's name to `.scrub-denylist.txt` now.

## 3. Inventory the source build

List every file in the source. Sort each into:

| Bucket | Goes to |
|--------|---------|
| Logic (code, flow exports, prompts, agent instructions) | `src/` after scrubbing |
| Company values (IDs, property names, channel IDs, owner names, domains) | placeholder in `config/settings.example.json` or `.env.example` |
| Our internal values (to run it on Octave's stack) | `config/settings.local.json` / `.env` (gitignored) |
| Customer data (lists, transcripts, briefs, screenshots, outputs) | Nowhere. Leave it behind. |

Show the user this inventory before porting.

## 4. Port and parameterize

- Replace every hardcoded ID/name with a config lookup. No hardcoded fallback values.
- Prompts and agent instructions: replace the customer's product, personas, and competitors with `{{PLACEHOLDER}}` or with instructions to pull them from the Octave library at runtime.
- N8N exports: strip `credentials` IDs, `webhookId`, workflow IDs, `errorWorkflow`; note each in `SETUP.md` as a manual step.
- Example records use `Acme` / `acme.com`.

## 5. Document

Fill `build.json` first (it drives search), then `README.md`, `ARCHITECTURE.md` (include design decisions and gates), `SETUP.md` (include a small-batch test step).

## 6. Verify and ship

```bash
python3 scripts/build_catalog.py
python3 scripts/scrub_check.py
```

Both must pass. Then read every changed file once more for anything the regexes can't catch (a customer's product name, a rep's first name, a distinctive metric). Commit one architecture per commit and push.
