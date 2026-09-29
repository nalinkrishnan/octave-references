---
name: find-reference-architecture
description: Search the Octave reference-architecture library for builds similar to a new request and give a head start. Reads catalog.json, ranks matches by problem, systems, Octave capabilities, runtime, and tags, then summarizes the top matches and what would need to change. Use when starting any new customer build or POC, or when asked "have we built something like this", "find a similar build", "reference architecture for X", "head start on X".
---

# Find Reference Architecture

## Locate the library

The library root is the folder containing `catalog.json` and `architectures/`. Check in order:

1. Current repo root, if it has `catalog.json`
2. `$OCTAVE_REFERENCES_DIR` if set
3. `~/Documents/octave/ccprojects/reference-architecture`

If none exist, tell the user and suggest `git clone https://github.com/nalinkrishnan/octave-references`.

Run `python3 scripts/build_catalog.py` from the library root first, so the catalog reflects any unindexed edits.

## Search

1. Restate the new build in one line: trigger → steps → output, the systems available, and the runtime they want.
2. Read `catalog.json` (a list of groups, each with its `builds`). First pick the group: the GTM job (`abm`, `outbound`, `extract-insights`, `sales`). Read that group's `GROUP.md` for the shared contract and trigger types. Then score each architecture on:
   - **Problem / outcome match** (highest weight): same GTM job, even if different systems
   - **Platform + destination**: an exact `platform`/`destination` match beats a partial one; a same-group build on another platform still gives the shared logic
   - **Octave capabilities overlap**: same tools (`qualify_company`, `run_email_agent`, …)
   - **Systems overlap**: required systems the user has; note any they lack and whether `systems.swappable` covers it
   - **Tags / category**
3. For the top 3, open `README.md` and `ARCHITECTURE.md` to confirm the fit. Don't rank from metadata alone. Skip `stub` builds as a starting point (no content yet), but mention one if it's the exact slot, plus the group's `shared/` components.
4. If nothing scores well, say so plainly. Name the nearest partial matches and which components are reusable (e.g. "the CRM gate from X, the Slack delivery from Y").

## Output

```
Best match: <title> (architectures/<group>/<id>/) · <status>
  Why: <1–2 lines>
  Reuse as-is: <components>
  Change: <components + what changes>
  Missing: <what this build needs that the architecture doesn't have>

Also relevant: <title> — <one line>, <title> — <one line>
```

Then offer to copy it as the starting point for the new build (into the customer/POC folder the user names, not into this library).

## After the build ships

Remind the user: if the new build is a new *type* or materially extends an existing one, port it back here with `/new-reference-architecture`.
