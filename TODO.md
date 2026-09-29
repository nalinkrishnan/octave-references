# TODO

## Next
- [ ] Pick the first build to fill in (port from an existing ccprojects build with `/new-reference-architecture`)
- [ ] Write group `shared/` components, starting with ABM: output schema, ranking rubric, brief template, CRM gate, Octave prerequisites

## Open questions
- ABM trigger types: `scheduled`, `web-visit`, `wake-the-dead`, `job-change`, `buying-signal` are the starting list. Confirm or trim.
- `extract-insights` platform: builds are named by voice + destination, no platform yet. Pick one (claude? n8n?) or keep them platform-free.
- `sales` destination: LLM builds output to the chat. Is that the destination, or should some write to CRM/docs?
- Port candidates from ccprojects: `poc/abm` + `poc/bait` → abm/claude-abm-slack; `artemis` → outbound/n8n-talktrack-crm; `poseidon` / batch campaigns → outbound/claude-email-sequencer; `muse/hera` → abm/n8n-abm-slack (signals); `swarm-briefs` → sales/llm-abm.

## Done
- [x] Scaffold repo: template, catalog builder, scaffolder, scrub check + pre-push hook, search + port skills (2026-09-29)
- [x] Group structure: 4 groups (abm, outbound, extract-insights, sales), 30 stub architectures, GROUP.md per group, catalog grids (2026-09-29)
