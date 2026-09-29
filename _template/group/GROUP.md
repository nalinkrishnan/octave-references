# {{Group title}}

> {{One sentence: the GTM job every build in this group does.}}

Every architecture in this group does the same job on a different platform or delivers to a different destination. Work that applies to all of them lives here and in `shared/`, not copied into each build.

## Shared contract

What every build in this group takes in and puts out, whatever the platform.

**Input:** {{…}}

**Output:** {{…}}

## Shared components (`shared/`)

| Component | File | Used by |
|-----------|------|---------|
| {{e.g. Octave library prerequisites}} | `shared/{{…}}` | all |

## Variants

See the group's section in [CATALOG.md](../../CATALOG.md).

## Cross-build conventions

- {{Rules every build in this group follows, e.g. same scoring rubric, same gate order.}}

## Changing something group-wide

1. Change it in `shared/` or in this file.
2. Check every build listed in `uses_shared` of its `build.json` for anything that needs updating.
3. Note the change in the root `CHANGELOG.md` under the group name.
