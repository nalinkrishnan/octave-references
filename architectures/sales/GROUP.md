# Sales

> On-demand deal assets an AE asks an LLM for: one-pagers, call prep, account plans, and follow-ups, grounded in the Octave library.

Builds in this group run in an LLM client connected to Octave (Claude, ChatGPT, or anything that speaks MCP). No orchestration platform. The build is the prompt, skill, or project instructions plus the Octave setup it depends on. Destination is always `chat`: the asset comes back in the conversation.

| Build | Produces |
|-------|----------|
| `llm-onepager` | A one-pager tailored to an account and persona |
| `llm-callprep` | Pre-call brief: attendees, account context, discovery questions, likely objections |
| `llm-abm` | An account plan for one named account: stakeholder map, angles, sequencing |
| `llm-followup` | Post-call follow-up email from the call transcript or notes |

`llm-abm` is the single-account, on-demand counterpart to the [ABM group](../abm/GROUP.md), which ranks many accounts on a schedule or trigger.

## Shared contract

**Input:** an account and/or person, plus whatever the AE has (call transcript, notes, deal stage).

**Output:** a document or email the AE can use as-is or lightly edit.

## Shared components (`shared/`)

| Component | File | Used by |
|-----------|------|---------|
| Octave MCP connection setup per LLM client | `shared/llm-setup.md` | all |
| Library prerequisites (personas, proof points, competitors) | `shared/octave-prerequisites.md` | all |
| Output style rules | `shared/style.md` | all |

(Planned. Nothing written yet.)

## Cross-build conventions

- Pull facts from Octave tools. Don't let the model invent proof points or customer names.
- Each build ships a copy-paste version (prompt) and a packaged version (skill or project).

## Changing something group-wide

1. Change it in `shared/` or in this file.
2. Check every build whose `build.json` → `uses_shared` lists that component.
3. Note the change in the root `CHANGELOG.md` under **sales**.
