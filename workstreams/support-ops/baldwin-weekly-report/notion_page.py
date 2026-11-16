"""Turn the weekly report specs into Notion-flavored Markdown.

The report lives on one Notion page, "Baldwin Weekly Trends and Perchie Review
Loop", with a child page per week. Each run writes two small JSON specs, the
week's and the Trends one, then runs this script.

Spec format:
{
  "blocks": [
    {"style": "h1", "text": "Week of October 19 to 25, 2026"},
    {"style": "p", "text": "Status: open. Jira: PWEB-123",
     "bold": ["Status:", "Jira:"],
     "links": [{"text": "PWEB-123", "url": "https://..."}]},
    {"style": "bullet", "text": "Conversation 215476..."},
    {"style": "table", "rows": [["Issue", "Status"], ["Phone numbers", "PWEB-1"]],
     "links": [{"row": 1, "col": 1, "text": "PWEB-1", "url": "https://..."}]}
  ]
}

style is one of: title, h1, h2, h3, p, bullet, table. bold and links name
substrings of the block's text; the first match is used unless a link gives
"at", its offset in the text. A table's first row is its header row, and its
links name text inside one cell.

  week  SPEC.json
      Prints {"title": ..., "content": ...} for the week's child page. The
      spec's h1 becomes the page title, so it is left out of the content.

  main  --history history.json --trends-spec TRENDS.json
      Prints the whole main page as Markdown: the intro, the week pages newest
      first (every week in history.json with a notion_url), Trends across
      weeks from the trends spec, and how the report is built. Send it with
      notion-update-page replace_content; the <page> tags keep the child pages
      and set their order.

Usage: python3 -I notion_page.py week SPEC.json
       python3 -I notion_page.py main --history H.json --trends-spec T.json
"""

import argparse
import json
import sys

SPECIAL = "\\*_`[]<>~$"


def esc(s):
    return "".join("\\" + c if c in SPECIAL else c for c in s)


def inline(text, bold=(), links=()):
    """Render text with bold substrings and links, escaping everything else."""
    marks = []
    for b in bold:
        at = text.find(b)
        if at < 0:
            raise SystemExit(f"{b!r} not found in {text!r}")
        marks.append((at, at + len(b), "bold", None))
    for l in links:
        at = l.get("at", -1)
        if at < 0:
            at = text.find(l["text"])
        if at < 0:
            raise SystemExit(f"{l['text']!r} not found in {text!r}")
        marks.append((at, at + len(l["text"]), "link", l["url"]))
    marks.sort()
    out, pos = [], 0
    for s, e, kind, url in marks:
        if s < pos:
            continue  # overlapping mark; keep the first
        out.append(esc(text[pos:s]))
        piece = esc(text[s:e])
        out.append(f"**{piece}**" if kind == "bold" else f"[{piece}]({url})")
        pos = e
    out.append(esc(text[pos:]))
    return "".join(out)


def table(block):
    rows = block["rows"]
    by_cell = {}
    for l in block.get("links", []):
        by_cell.setdefault((l["row"], l["col"]), []).append(l)
    lines = ['<table header-row="true">']
    for r, row in enumerate(rows):
        cells = "".join(f"<td>{inline(c, links=by_cell.get((r, k), []))}</td>" for k, c in enumerate(row))
        lines.append(f"<tr>{cells}</tr>")
    lines.append("</table>")
    return "\n".join(lines)


def render(blocks, shift=0):
    """Blocks to Markdown. shift moves headings down a level (h1 -> h2)."""
    parts, bullets = [], []
    for b in blocks:
        if b["style"] != "bullet" and bullets:
            parts.append("\n".join(bullets))
            bullets = []
        if b["style"] == "table":
            parts.append(table(b))
        elif b["style"] == "bullet":
            bullets.append("- " + inline(b["text"], b.get("bold", []), b.get("links", [])))
        elif b["style"] in ("title", "h1", "h2", "h3"):
            level = {"title": 1, "h1": 1, "h2": 2, "h3": 3}[b["style"]] + shift
            parts.append("#" * min(level, 3) + " " + esc(b["text"]))
        else:
            parts.append(inline(b["text"], b.get("bold", []), b.get("links", [])))
    if bullets:
        parts.append("\n".join(bullets))
    # Blank lines keep each paragraph its own Notion block.
    return "\n\n".join(parts)


def week(spec):
    blocks = spec["blocks"]
    if not blocks or blocks[0]["style"] not in ("h1", "title"):
        raise SystemExit("The week spec must start with its h1 title")
    return {"title": blocks[0]["text"], "content": render(blocks[1:])}


INTRO = (
    "A running record of what Baldwin members are saying, asking, and complaining about in Intercom, "
    "with the focus on what keeps coming back. Each week gets its own page that names the recurring themes, "
    "whether each is growing or fading, and how members feel about it, with links to example conversations. "
    "Trends across weeks, below, tracks every theme's count week by week."
)

HOW = [
    "A scheduled Claude task runs every Friday at 10 PM Eastern. In one run it collects the week's Baldwin conversations, "
    "groups them into themes, compares them with earlier weeks, adds the week's page here, updates Trends across weeks, "
    "and makes that week's slide deck. A report week runs from one Friday at 10 PM to the next, so weekend conversations "
    "land in the following report.",
    "Every Baldwin conversation counts: questions, bugs, feature requests, and feedback. A conversation is Baldwin when its "
    "MLS attribute is Baldwin, it went to the Baldwin VIP team, Fin answered it through the Baldwin workflow, or MLS staff "
    "sent it. Test and spam conversations are left out.",
    "Sentiment comes from what members write, member conversation ratings (ratings from MLS staff are left out because "
    "they are not reliable), Fin thumbs-down ratings, and how often Fin hands a conversation to a teammate.",
    "Member names and contact details are left out; open a linked conversation for them.",
]

WHERE = (
    "`workstreams/support-ops/baldwin-weekly-report/baldwin-weekly-trends-runbook.md` in the customer-success repo, "
    "run by the baldwin-weekly-trends skill. Until November 16, 2026 this report lived in a Google Doc, "
    "Baldwin Member Feedback Trends; this page replaced it."
)


def main_page(history, trends):
    pages = []
    for w in reversed(history["weeks"]):
        if w.get("notion_url"):
            pages.append(f'<page url="{w["notion_url"]}">{esc(w.get("notion_title", w["label"]))}</page>')
    if not pages:
        raise SystemExit("No week in history.json has a notion_url")
    tb = trends["blocks"]
    if tb and tb[0]["style"] in ("h1", "title"):
        tb = [{"style": "h2", "text": tb[0]["text"]}] + tb[1:]
        rest = render(tb[:1]) + "\n\n" + render(tb[1:], shift=1)
    else:
        rest = render(tb, shift=1)
    parts = [
        esc(INTRO),
        "## Weekly reports",
        "Newest first.",
        "\n".join(pages),
        rest,
        "## How it is built",
        "\n\n".join(esc(p) for p in HOW),
        "## Where the instructions live",
        WHERE,
    ]
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["week", "main"])
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--history")
    ap.add_argument("--trends-spec")
    a = ap.parse_args()
    if a.mode == "week":
        print(json.dumps(week(json.load(open(a.spec))), ensure_ascii=False))
    else:
        if not (a.history and a.trends_spec):
            raise SystemExit("main needs --history and --trends-spec")
        sys.stdout.write(main_page(json.load(open(a.history)), json.load(open(a.trends_spec))))
