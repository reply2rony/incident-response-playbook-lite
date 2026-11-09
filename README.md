# Incident Response Playbook Lite — Starter Template

A starter learning template for running a small IT incident response:
detect it, triage it, contain it, fix it, and write down what was
learned — with fictional sample incidents only. It is a playbook
plus a small incident log in CSV form, so an IT team can practise
the steps on made-up examples before a real incident ever happens.
Sample content only — no real company data, no invented metrics,
and no claim of production use.

## What it is

- `docs/playbook-guide.md` — the playbook: the five response phases,
  severity levels, roles, and a checklist for each phase.
- `incident-response-playbook-lite.csv` — the incident log in CSV form,
  so you can copy it, filter it, and add your own sample incidents.
- `scripts/playbook-summary.py` — a starter Python script that
  summarises the log by severity and phase, and flags open high-severity
  incidents and overdue actions. Labelled a starter learning template;
  it is not a production tool.

## How to use

1. When something goes wrong, open a row in
   `incident-response-playbook-lite.csv` — one row per incident — and
   record what happened, when it was detected, and who is leading it.
2. Work the checklist in `docs/playbook-guide.md` in order — detect,
   triage, contain, eradicate, recover, then lessons learned.
3. Update the row as the incident moves through the phases, and close
   it only after the lessons-learned note is written.
4. Summarise the log from the command line:

```bash
python3 scripts/playbook-summary.py incident-response-playbook-lite.csv
python3 scripts/playbook-summary.py incident-response-playbook-lite.csv --severity high
python3 scripts/playbook-summary.py incident-response-playbook-lite.csv --status open
```

## Severity levels (starter guide)

| Severity | Meaning | First response |
|----------|---------|----------------|
| Critical | Service down, or data at risk | Act at once, tell the team lead |
| High | Major service degraded | Start containment within the hour |
| Medium | Limited impact, workaround exists | Plan the fix the same day |
| Low | Minor issue, no service impact | Fix in the next regular window |

Levels above are starter suggestions for a learning template, not a
standard for any real organisation.

## Sample / Demo notice

All incidents, systems, people, and times in this repo are fictional
samples for learning. The diagram in `docs/diagram.png` is a locally
generated illustration labelled "Sample / Demo" — it is not a
screenshot of a real system, and this template does not claim any
production use.

## License

MIT — see `LICENSE`.
