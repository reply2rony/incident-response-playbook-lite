# Incident Response Playbook — Guide

A starter guide for running a basic incident response in a small
IT team. This is a learning template — adapt the steps to your own
organisation's policy. All incidents, systems, people, and times
below are fictional.

## The six phases

### 1. Detect

Something is wrong. Note the first sign, the time it was spotted,
and who spotted it. Common first signs: a service stops answering,
an alert fires, users report the same error, or a log shows an
unusual pattern. Record it in `incident-response-playbook-lite.csv`
right away — do not rely on memory.

### 2. Triage

Work out how bad it is before you act:

- **What is affected?** One service, one department, or everything?
- **Who is affected?** How many users, and can they work around it?
- **How bad is it?** Use the severity table in the README —
  critical, high, medium, or low.
- **Who leads?** Name one incident lead. One person decides; the
  rest help. Write the name in the log.

A wrong severity is worse than a slow one: a critical incident
treated as low will not get the help it needs.

### 3. Contain

Stop the damage from spreading. Containment is not the fix — it
is the bandage:

- Take the affected service offline or isolate the affected system.
- Block the suspicious account, address, or connection.
- Switch users to the workaround, if there is one.

Record what you contained, when, and what is still exposed. Never
skip containment to jump straight to the fix — an uncontained
incident can get worse while you work.

### 4. Eradicate and recover

Remove the cause, then bring the service back:

- **Eradicate** — remove the faulty update, close the bad account,
  clear the bad data, or rebuild the affected system from a known
  good state. Record the root cause in the log.
- **Recover** — restore the service, check it answers normally,
  and watch it for a while before calling it done. A service that
  looks fixed for five minutes is not yet proven fixed.

### 5. Lessons learned

After the incident closes, write down three things in the log:

- What happened, in plain language.
- What worked, and what slowed the response down.
- One change to make so it does not happen again — or so the next
  response is faster.

An incident with no lessons-learned note is an incident that will
repeat itself.

### 6. Communicate (throughout)

At every phase, tell the people who need to know:

- **Users** — what is broken, what the workaround is, and when the
  next update comes. Short, honest, no jargon.
- **The team lead** — severity, containment status, and what help
  is needed.
- **Afterwards** — a short summary of what happened and what
  changed.

Silence during an incident is almost as bad as the incident itself.

## Roles (starter suggestions)

| Role | Does |
|------|------|
| Incident lead | Decides severity, assigns tasks, owns communication |
| Responder | Works the fix, reports progress to the lead |
| Communicator | Sends user and team updates |
| Note-taker | Keeps the log current through every phase |

In a small team one person may hold two roles — but the incident
lead and the note-taker should be different people if you can.

## Common mistakes (starter notes)

- Starting the fix before writing anything down.
- Treating the first symptom as the cause.
- Containing nothing because the fix "looks quick".
- Declaring recovery before watching the service for a while.
- Skipping the lessons-learned note because everyone is tired.
- Recording real system names, accounts, or passwords in a shared log.

## Adding your own incidents

Add a row to `incident-response-playbook-lite.csv` with: incident_id,
detected_at, title, severity, status, phase, affected_system,
incident_lead, action_taken, and lessons_learned. Keep every entry
fictional in samples — never commit real incident details.

## Sample / Demo notice

All incidents here are fictional samples for learning, labelled
"Sample / Demo" in the diagram. This template does not claim any
production use.
