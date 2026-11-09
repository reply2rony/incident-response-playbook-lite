#!/usr/bin/env python3
"""Starter learning template: summarise the incident response log.

Usage:
    python3 scripts/playbook-summary.py incident-response-playbook-lite.csv
    python3 scripts/playbook-summary.py incident-response-playbook-lite.csv --severity high
    python3 scripts/playbook-summary.py incident-response-playbook-lite.csv --status open

Summarises the CSV by severity, status and phase, and flags open
high-severity incidents and incidents with no lessons-learned note.
Sample data only; no real company data.
"""
import argparse
import csv
import sys
from collections import Counter


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description="Summarise the incident response log.")
    ap.add_argument("csv_file", help="path to incident-response-playbook-lite.csv")
    ap.add_argument("--severity", help="filter by severity (e.g. high)")
    ap.add_argument("--status", help="filter by status (e.g. open)")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.severity:
        rows = [r for r in rows if r.get("severity", "").lower() == args.severity.lower()]
    if args.status:
        rows = [r for r in rows if r.get("status", "").lower() == args.status.lower()]

    if not rows:
        print("No matching incidents.")
        sys.exit(0)

    print(f"Incidents: {len(rows)}")
    print()
    print("By severity:")
    for sev, n in Counter(r.get("severity", "") for r in rows).most_common():
        print(f"  {sev}: {n}")
    print()
    print("By status:")
    for st, n in Counter(r.get("status", "") for r in rows).most_common():
        print(f"  {st}: {n}")
    print()
    print("By phase:")
    for ph, n in Counter(r.get("phase", "") for r in rows).most_common():
        print(f"  {ph}: {n}")
    print()
    open_high = [r for r in rows
                 if r.get("status", "").lower() == "open"
                 and r.get("severity", "").lower() in ("critical", "high")]
    if open_high:
        print("Open critical/high incidents — need attention first:")
        for r in open_high:
            print(f"  {r['incident_id']} ({r['severity']}, phase: {r['phase']}) — {r['title']}, lead: {r['incident_lead']}")
    else:
        print("No open critical/high incidents.")
    print()
    no_lessons = [r for r in rows
                  if r.get("status", "").lower() == "closed"
                  and not r.get("lessons_learned", "").strip()]
    if no_lessons:
        print("Closed incidents with no lessons-learned note:")
        for r in no_lessons:
            print(f"  {r['incident_id']} — {r['title']}")
    else:
        print("Every closed incident has a lessons-learned note.")


if __name__ == "__main__":
    main()
