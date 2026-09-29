# ABM

> Pick the accounts worth working now, research them against the Octave library, and hand a ranked list with briefs to the team where they work.

Every build in this group does the same job. They differ on two axes:

- **Platform** (how it runs): `clay`, `claude`, `cargo`, `n8n`
- **Destination** (where the output lands): `slack`, `salesforce`, `hubspot`, `custom`

Build ids are `<platform>-abm-<destination>`. Work that applies to all 16 lives here and in `shared/`, not copied into each build.

## Trigger types

Every build should support these triggers, which decide which accounts enter a run and what the "why now" says. The trigger changes what goes in; the research → rank → deliver core stays the same.

| Trigger | What starts it | Why-now angle |
|---------|----------------|---------------|
| `scheduled` | Weekly/daily run over a target account list | Best-fit accounts with the freshest signals |
| `web-visit` | Account identified on the website | They're looking right now |
| `wake-the-dead` | Closed-lost or gone-quiet accounts | What changed since they said no |
| `job-change` | Champion or buyer moves into a target account | Known relationship, new seat |
| `buying-signal` | Hiring, funding, launch, tech change | Event that creates the need |

This list is confirmed (2026-09-29).

Add a trigger here first (and to `group.json` → `trigger_types`), then to the builds.

## Shared contract

**Input:** a list of accounts (domain required), the trigger type, and optionally trigger context (visit pages, loss reason, the person who moved, the signal).

**Output per account:** rank, fit/qualification score, matched segment + personas, recommended contacts, a one-line why-now, and a link to a full account brief.

Destinations only change how that output is delivered: a Slack message, CRM fields/tasks/notes (Salesforce or HubSpot), or a webhook/file (`custom`).

## Shared components (`shared/`)

| Component | File | Used by |
|-----------|------|---------|
| Octave library prerequisites (segments, personas, qualifiers, buying triggers) | `shared/octave-prerequisites.md` | all |
| Ranking rubric | `shared/ranking-rubric.md` | all |
| Account brief template | `shared/brief-template.md` | all |
| Output schema | `shared/output-schema.json` | all |
| CRM gate rules (open deals, customers, recent meetings) | `shared/crm-gate.md` | all |

(Planned. Nothing written yet.)

## Cross-build conventions

- Same ranking rubric and output schema on every platform, so outputs can be compared across builds.
- CRM gate runs before research: no open deals, no current customers.
- Test on 3–5 accounts before any full run.

## Changing something group-wide

1. Change it in `shared/` or in this file.
2. Check every build whose `build.json` → `uses_shared` lists that component.
3. Note the change in the root `CHANGELOG.md` under **abm**.
