# {{Title}} — Architecture

## Flow

```
{{trigger}} → {{step}} → {{step}} → {{output}}
```

## Components

| # | Component | System | Input | Output | Notes |
|---|-----------|--------|-------|--------|-------|
| 1 | {{…}} | {{…}} | {{…}} | {{…}} | {{…}} |

## Data contract

{{The shape of the record that moves between steps. Field names are generic; CRM-specific names are mapped in config/.}}

```json
{
  "company_domain": "acme.com"
}
```

## Configuration points

Everything that changes per company, and where it's set.

| Setting | Where | Example |
|---------|-------|---------|
| {{…}} | `config/settings.example.json` | {{…}} |

## Design decisions

- **{{Decision}}.** {{Why, and what was tried instead.}}

## Gates and safety

{{CRM gate, suppression, test-batch-first, rate limits. What stops this build from emailing a customer or an open deal.}}

## Known limits

- {{…}}
