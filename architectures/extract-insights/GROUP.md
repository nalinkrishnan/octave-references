# Extract Insights

> Mine recorded calls and conversations for patterns, and post what the team should know to Slack.

Builds in this group differ by **whose voice** is being analyzed:

- `customervoice`: what buyers and customers say (pains, objections, competitors named, language they use) → feeds messaging, positioning, and the Octave library.
- `repvoice`: what reps say (talk tracks that land, value props used, where they go off-message) → feeds coaching and enablement.

Build ids are `<voice>-<destination>`. Both deliver to Slack today.

## Shared contract

**Input:** call recordings or transcripts over a time window (from a call recorder, the CRM, or Octave's synced calls), optionally filtered by deal stage, segment, or rep.

**Output:** a digest posted to Slack: top themes with counts, quoted evidence with links back to the call, and suggested actions (library update, coaching note).

## Shared components (`shared/`)

| Component | File | Used by |
|-----------|------|---------|
| Transcript source setup | `shared/transcript-sources.md` | all |
| Theme extraction prompt / Octave extractor config | `shared/extraction.md` | all |
| Slack digest format | `shared/slack-digest.md` | all |

(Planned. Nothing written yet.)

## Cross-build conventions

- Every insight quotes its evidence and links to the source call. No unsourced claims.
- Real names of customers and callers never appear in examples in this repo.

## Changing something group-wide

1. Change it in `shared/` or in this file.
2. Check every build whose `build.json` → `uses_shared` lists that component.
3. Note the change in the root `CHANGELOG.md` under **extract-insights**.
