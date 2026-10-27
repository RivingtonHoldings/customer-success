#!/usr/bin/env python3
"""Deterministic helpers for the Baldwin Bible refresh.

Claude does the reading and judgment; this script keeps the Jira state and the
tracker table consistent so neither depends on parsing JSON by eye.

Subcommands:
  jira-ingest  Merge searchJiraIssuesUsingJql result files into sync-state.json
               and print what is new or changed since the last run.
  set-scope    Override the scope of one ticket (kept across runs).
  set-cursor   Record a cursor for a source (slack channel ts, notion, intercom).
  tracker      Rebuild jira/tracker.md from sync-state.json.
  summary      Print counts per status group and scope.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SITE = "https://perchwell.atlassian.net/browse/"

# Markers that put a ticket outside Baldwin when Baldwin itself is not named.
OTHER_MLS = re.compile(r"\b(CRMLS|NYC|RLS|REBNY)\b", re.I)
BALDWIN = re.compile(r"baldwin", re.I)

STATUS_GROUPS = {
    "open": {"to do", "triage", "reopened", "blocked", "outstanding issues",
             "backlog", "open", "selected for development"},
    "in_progress": {"in progress", "in development"},
    "review": {"in review", "ready for testing", "in qa", "testing",
               "code review", "ready for release"},
    "done": {"done", "closed", "released", "resolved"},
    "wont": {"won't do", "wont do", "duplicate", "cancelled", "canceled"},
}
GROUP_TITLES = [
    ("open", "Open"),
    ("in_progress", "In progress"),
    ("review", "In review or testing"),
    ("done", "Done"),
    ("wont", "Won't do"),
]
CATEGORY_FALLBACK = {"new": "open", "indeterminate": "in_progress", "done": "done"}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_state(path):
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    return {"last_run": None, "jira": {"cursor": None, "tickets": {}},
            "slack": {"channels": {}}, "notion": {"cursor": None, "pages": {}},
            "intercom": {"cursor": None}}


def save_state(path, state):
    Path(path).write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def status_group(status_name, category_key):
    name = (status_name or "").strip().lower()
    for group, names in STATUS_GROUPS.items():
        if name in names:
            return group
    return CATEGORY_FALLBACK.get(category_key or "", "open")


def auto_scope(summary, labels):
    if any(BALDWIN.search(l) for l in labels) or BALDWIN.search(summary or ""):
        return "Baldwin-only"
    if OTHER_MLS.search(summary or ""):
        return "Other MLS only"
    return "All MLSs"


def iter_issues(files):
    for f in files:
        data = json.loads(Path(f).read_text())
        nodes = data.get("issues", {}).get("nodes")
        if nodes is None:
            nodes = data.get("issues", []) if isinstance(data.get("issues"), list) else []
        for n in nodes:
            yield n


def cmd_jira_ingest(args):
    state = load_state(args.state)
    tickets = state["jira"]["tickets"]
    new, changed, seen = [], [], set()
    for n in iter_issues(args.files):
        key = n["key"]
        if key in seen:
            continue
        seen.add(key)
        f = n.get("fields", {})
        status = f.get("status") or {}
        labels = f.get("labels") or []
        rec = {
            "project": (f.get("project") or {}).get("key"),
            "type": (f.get("issuetype") or {}).get("name"),
            "summary": f.get("summary"),
            "status": status.get("name"),
            "group": status_group(status.get("name"),
                                  (status.get("statusCategory") or {}).get("key")),
            "labels": labels,
            "components": [c.get("name") for c in (f.get("components") or [])],
            "updated": f.get("updated"),
        }
        old = tickets.get(key)
        if old and old.get("scope_source") == "manual":
            rec["scope"], rec["scope_source"] = old["scope"], "manual"
        else:
            rec["scope"], rec["scope_source"] = auto_scope(rec["summary"], labels), "auto"
        if old is None:
            rec["first_seen"] = now_iso()[:10]
            new.append(key)
        else:
            rec["first_seen"] = old.get("first_seen")
            if old.get("status") != rec["status"]:
                rec["previous_status"] = old.get("status")
                changed.append(key)
        tickets[key] = rec
    state["jira"]["cursor"] = args.cursor or now_iso()
    save_state(args.state, state)

    def line(k, extra=""):
        t = tickets[k]
        return f"{k}\t{t['type']}\t{t['status']}{extra}\t{t['scope']}\t{t['summary']}"

    print(f"ingested {len(seen)} tickets: {len(new)} new, {len(changed)} status changes")
    if new:
        print("\nNEW")
        for k in sorted(new):
            print(line(k))
    if changed:
        print("\nSTATUS CHANGED")
        for k in sorted(changed):
            print(line(k, f" (was {tickets[k].get('previous_status')})"))


def cmd_set_scope(args):
    state = load_state(args.state)
    t = state["jira"]["tickets"].get(args.key)
    if not t:
        sys.exit(f"{args.key} not in state")
    t["scope"], t["scope_source"] = args.scope, "manual"
    save_state(args.state, state)
    print(f"{args.key} scope = {args.scope}")


def cmd_set_cursor(args):
    state = load_state(args.state)
    if args.source == "slack":
        if not args.channel:
            sys.exit("--channel is required for slack")
        state["slack"]["channels"].setdefault(args.channel, {})["ts"] = args.value
    else:
        state[args.source]["cursor"] = args.value
    state["last_run"] = now_iso()
    save_state(args.state, state)
    print(f"{args.source} {args.channel or ''} cursor = {args.value}")


def esc(s):
    return (s or "").replace("|", "\\|")


def cmd_tracker(args):
    state = load_state(args.state)
    tickets = {k: t for k, t in state["jira"]["tickets"].items()
               if t.get("scope") != "Other MLS only"}
    out = ["# Baldwin Jira tracker", "",
           "Every Jira ticket that touches Baldwin, rebuilt by `/baldwin-refresh` from "
           "`docs/sync-state.json`. Do not edit by hand; change a ticket's scope with "
           "`bible.py set-scope` instead.", "",
           f"Last rebuilt: {now_iso()[:10]}. {len(tickets)} tickets. Scope "
           "\"All MLSs\" means the ticket is platform-wide, which means it reaches Baldwin "
           "members too.", ""]
    for group, title in GROUP_TITLES:
        rows = sorted(((k, t) for k, t in tickets.items() if t.get("group") == group),
                      key=lambda kt: kt[1].get("updated") or "", reverse=True)
        out.append(f"## {title} ({len(rows)})")
        out.append("")
        if not rows:
            out += ["None.", ""]
            continue
        out.append("| Ticket | Type | Status | Scope | Summary | Updated |")
        out.append("|---|---|---|---|---|---|")
        for k, t in rows:
            out.append(f"| [{k}]({SITE}{k}) | {esc(t.get('type'))} | {esc(t.get('status'))} | "
                       f"{t.get('scope')} | {esc(t.get('summary'))} | "
                       f"{(t.get('updated') or '')[:10]} |")
        out.append("")
    Path(args.out).write_text("\n".join(out))
    print(f"wrote {args.out}: {len(tickets)} tickets")


def cmd_summary(args):
    state = load_state(args.state)
    counts = {}
    for t in state["jira"]["tickets"].values():
        counts.setdefault((t.get("group"), t.get("scope")), 0)
        counts[(t.get("group"), t.get("scope"))] += 1
    for (g, s), c in sorted(counts.items(), key=lambda x: (str(x[0][0]), str(x[0][1]))):
        print(f"{g}\t{s}\t{c}")
    print(f"slack channels with cursors: {len(state['slack']['channels'])}")
    print(f"last run: {state.get('last_run')}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("jira-ingest")
    p.add_argument("--state", required=True)
    p.add_argument("--cursor", help="ISO time to store as the new Jira cursor (default now)")
    p.add_argument("--files", nargs="+", required=True)
    p.set_defaults(fn=cmd_jira_ingest)
    p = sub.add_parser("set-scope")
    p.add_argument("--state", required=True)
    p.add_argument("--key", required=True)
    p.add_argument("--scope", required=True,
                   choices=["Baldwin-only", "All MLSs", "Other MLS only"])
    p.set_defaults(fn=cmd_set_scope)
    p = sub.add_parser("set-cursor")
    p.add_argument("--state", required=True)
    p.add_argument("--source", required=True, choices=["slack", "notion", "intercom", "jira"])
    p.add_argument("--channel")
    p.add_argument("--value", required=True)
    p.set_defaults(fn=cmd_set_cursor)
    p = sub.add_parser("tracker")
    p.add_argument("--state", required=True)
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_tracker)
    p = sub.add_parser("summary")
    p.add_argument("--state", required=True)
    p.set_defaults(fn=cmd_summary)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
