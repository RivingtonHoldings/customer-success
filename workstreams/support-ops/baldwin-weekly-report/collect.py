"""Reduce saved Intercom search_conversations pages to the Baldwin conversations a report needs.

search_conversations returns full conversation objects, too large to read in
context, so each run saves the pages to files and runs this script on them.
It keeps Baldwin conversations started in the window, plus any tracker tickets,
and writes one small JSON file with only the fields the report uses.

Usage:
  python3 -I collect.py --start EPOCH --end EPOCH --out OUT.json PAGE.json [PAGE.json ...]

A page file may be the raw tool result ({"conversations": [...]}) or a saved
copy wrapping it. --start and --end are Unix seconds; a conversation counts
when start <= created_at < end.
"""

import argparse
import html
import json
import re
from collections import Counter

BALDWIN_VIP_TEAM = 10945385
MLS_STAFF_DOMAIN = "baldwinrealtors.com"
APP = "https://app.intercom.com/a/inbox/trq7czv5/inbox/conversation/"


def strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def subject_key(s):
    # "Re: Challenge accepted: ..." and "RE: [EXTERNAL] Challenge accepted: ..." group together.
    s = strip(s).lower()
    s = re.sub(r"^((re|fw|fwd|automatic reply)\s*:\s*|\[external\]\s*)+", "", s)
    return s.strip()


def is_baldwin(c):
    ca = c.get("custom_attributes") or {}
    if ca.get("MLS") == "Baldwin":
        return True
    if c.get("team_assignee_id") == BALDWIN_VIP_TEAM:
        return True
    if "baldwin" in ((c.get("ai_agent") or {}).get("source_title") or "").lower():
        return True
    return MLS_STAFF_DOMAIN in ((c.get("source") or {}).get("author") or {}).get("email", "")


def load(paths):
    convs = {}
    for p in paths:
        with open(p) as f:
            d = json.load(f)
        d = d.get("content", d) if isinstance(d, dict) else d
        for c in d.get("conversations", []):
            convs[c["id"]] = c
    return convs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("pages", nargs="+")
    a = ap.parse_args()

    convs = load(a.pages)
    in_window = [c for c in convs.values() if not c.get("ticket") and a.start <= c["created_at"] < a.end]
    # Replies to a Baldwin email campaign often arrive without the MLS attribute,
    # so a subject that 3 or more Baldwin conversations share pulls in the rest.
    baldwin_subjects = Counter(subject_key((c.get("source") or {}).get("subject"))
                               for c in in_window if is_baldwin(c))
    campaign_keys = {s for s, n in baldwin_subjects.items() if s and n >= 3}

    out, trackers = [], []
    for c in convs.values():
        ca = c.get("custom_attributes") or {}
        if c.get("ticket"):
            if "Tracker" in (c["ticket"].get("ticket_type") or ""):
                trackers.append({
                    "id": c["id"], "type": c["ticket"]["ticket_type"], "state": c["ticket"].get("state"),
                    "title": ca.get("_default_title_"), "jira": ca.get("jira_issue_key"),
                    "reports": ca.get("Customer reports"), "created_at": c["created_at"],
                    "linked": [o["id"] for o in c["linked_objects"]["data"] if o["type"] == "conversation"],
                })
            continue
        src = c.get("source") or {}
        if not (a.start <= c["created_at"] < a.end):
            continue
        if not (is_baldwin(c) or subject_key(src.get("subject")) in campaign_keys):
            continue
        author_email = (src.get("author") or {}).get("email") or ""
        rating = (c.get("conversation_rating") or {}).get("rating")
        ai = c.get("ai_agent") or {}
        out.append({
            "id": c["id"],
            "url": APP + c["id"],
            "created_at": c["created_at"],
            "state": c["state"],
            "type": ca.get("Type of Request"),
            "part": ca.get("Part of the Platform"),
            "title": c.get("title") or ca.get("AI Title"),
            "subject_key": subject_key(src.get("subject")),
            "from_mls_staff": MLS_STAFF_DOMAIN in author_email,
            # MLS staff ratings are not reliable, so they never count toward sentiment.
            "member_rating": None if MLS_STAFF_DOMAIN in author_email else rating,
            "fin_state": ai.get("resolution_state"),
            "teammate_replied": bool((c.get("statistics") or {}).get("first_admin_reply_at")),
            "jira_link": ca.get("Jira Ticket Link"),
            "linked_tickets": [o["id"] for o in c["linked_objects"]["data"] if o["type"] == "ticket"],
            "snippet": strip(src.get("body"))[:200],
        })

    campaigns = Counter(o["subject_key"] for o in out if o["subject_key"] in campaign_keys)
    for o in out:
        o["campaign"] = o["subject_key"] if o["subject_key"] in campaign_keys else None

    with open(a.out, "w") as f:
        json.dump({"start": a.start, "end": a.end, "conversations": out,
                   "campaigns": campaigns, "trackers": trackers}, f, indent=1)
    test = sum(1 for o in out if o["type"] == "Internal / Test / Spam")
    print(f"{len(out)} Baldwin conversations ({test} test or spam), "
          f"{len(campaigns)} campaign subject(s), {len(trackers)} tracker tickets")


if __name__ == "__main__":
    main()
