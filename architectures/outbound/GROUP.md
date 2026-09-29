# Outbound

> Turn a qualified contact into outreach: an Octave-written email sequence, or a call talk track written back to the CRM.

Every build in this group differs on two axes:

- **Platform** (how it runs): `clay`, `cargo`, `claude`, `n8n`
- **Job** (what it produces):
  - `email-sequencer`: generates a multi-step email sequence with an Octave sequence agent and loads it into a sending tool
  - `talktrack-crm`: generates a call talk track (opener, discovery questions, objection handling) and writes it to the contact/task in the CRM

Build ids are `<platform>-<job>`. Work that applies to all of them lives here and in `shared/`.

## Shared contract

**Input:** a contact (name, title, email, LinkedIn URL, company domain), plus optional runtime context (signal, prior engagement, call notes).

**Output:**
- `email-sequencer`: N email steps (subject + body) with the agent id and version that wrote them, pushed to the sending tool.
- `talktrack-crm`: a talk track written to a CRM field, note, or task on the contact.

## Shared components (`shared/`)

| Component | File | Used by |
|-----------|------|---------|
| Octave agent setup (sequence agent, content agent, writing style) | `shared/octave-agents.md` | all |
| Runtime context format | `shared/runtime-context.md` | all |
| Campaign gate (open deals, customers, recent meetings, opt-outs) | `shared/campaign-gate.md` | all |
| Talk track template | `shared/talktrack-template.md` | talktrack-crm |

(Planned. Nothing written yet.)

## Cross-build conventions

- Campaign gate runs before anything is generated or sent.
- Generate for a test batch and review it before loading a full list.
- Writing style lives in the Octave agent, not in platform-side prompts.

## Changing something group-wide

1. Change it in `shared/` or in this file.
2. Check every build whose `build.json` → `uses_shared` lists that component.
3. Note the change in the root `CHANGELOG.md` under **outbound**.
