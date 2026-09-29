# {{Title}} — Setup

## 1. Prerequisites

- [ ] Octave workspace with an API key
- [ ] {{Other system}} access with {{scopes}}

## 2. Credentials

```bash
cp .env.example .env
# fill in every value
```

## 3. Config

```bash
for f in config/*.example.*; do cp "$f" "${f/.example./.local.}"; done
# fill in every {{PLACEHOLDER}} in config/*.local.*
```

`*.local.*` files are gitignored.

## 4. Octave library prerequisites

{{Entities, agents, or skills the workspace needs before the first run.}}

## 5. Deploy

{{Steps.}}

## 6. Test on a small batch

{{Exact command to run on 2–3 records, and what a passing result looks like. Never run on the full list first.}}

## 7. Go live

{{Schedule, monitoring, where errors go.}}

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| {{…}} | {{…}} | {{…}} |
