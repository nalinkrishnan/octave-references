# TODO

## Next
- [ ] Pick the first build to fill in (port from an existing ccprojects build with `/new-reference-architecture`)
- [ ] Write group `shared/` components, starting with ABM: output schema, ranking rubric, brief template, CRM gate, Octave prerequisites

## Open questions
- Which build to fill first. Suggested: abm/claude-abm-slack (port from `poc/abm` + `poc/bait`), which also produces the ABM `shared/` components.
- Other port candidates from ccprojects: `artemis` → outbound/n8n-talktrack-crm; `poseidon` / batch campaigns → outbound/claude-email-sequencer; `muse/hera` → abm/n8n-abm-slack (signals); `swarm-briefs` → sales/llm-abm.

## Decisions
- ABM trigger types: `scheduled`, `web-visit`, `wake-the-dead`, `job-change`, `buying-signal` (2026-09-29)
- extract-insights builds keep their names (`<voice>-slack`); platform `tbd` until we know how they're built (2026-09-29)
- sales builds: destination is `chat` (2026-09-29)

## Done
- [x] Scaffold repo: template, catalog builder, scaffolder, scrub check + pre-push hook, search + port skills (2026-09-29)
- [x] Group structure: 4 groups (abm, outbound, extract-insights, sales), 30 stub architectures, GROUP.md per group, catalog grids (2026-09-29)
