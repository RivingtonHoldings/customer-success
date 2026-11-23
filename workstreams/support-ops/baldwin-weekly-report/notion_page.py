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

  main  --current FETCH --history history.json --trends-spec TRENDS.json
        [--perchie PERCHIE.md]
      Edits the main page as it is now, so a teammate's own formatting and
      any section the run does not own are kept. FETCH is a saved
      notion-fetch result of the main page (the JSON, or just its content).
      The script changes only three things:
        - the week page links: every week in history.json with a notion_url
          is listed right after the line "Newest first.", newest first, and
          any copy of those links elsewhere on the page (a new child page
          lands at the bottom) is removed. The text inside a <page> tag is
          the child page's title, and replace_content renames the page to it,
          so each link keeps the title the page already shows; a page not yet
          on the main page gets "Week of <first> to <last>, <year>" from the
          week's start and end (or its notion_title in history.json);
        - the "Trends across weeks" section, up to the next level 2 heading;
        - with --perchie, the body of the "Perchie Review Loop" toggle.
      It stops with an error if an anchor is missing instead of guessing.
      Send the output with notion-update-page replace_content.

Usage: python3 -I notion_page.py week SPEC.json
       python3 -I notion_page.py main --current F --history H.json --trends-spec T.json [--perchie P.md]
"""

import argparse
import json
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

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


def page_content(raw):
    """Accept a saved notion-fetch result (JSON or text) and return the page body."""
    try:
        raw = json.loads(raw).get("text", raw)
    except (ValueError, AttributeError):
        pass
    m = re.search(r"<content>\n?(.*)\n?</content>", raw, re.S)
    return m.group(1) if m else raw


def trends_md(trends):
    tb = trends["blocks"]
    if tb and tb[0]["style"] in ("h1", "title"):
        return render([{"style": "h2", "text": tb[0]["text"]}]) + "\n\n" + render(tb[1:], shift=1)
    return render(tb, shift=1)


def week_title(w):
    """The week page's full title, as the week spec's h1 writes it:
    "Week of November 16 to 23, 2026", "Week of October 31 to November 9, 2026",
    or "Week of December 28, 2026 to January 3, 2027". A notion_title in the
    week's history entry wins."""
    if w.get("notion_title"):
        return w["notion_title"]
    def day(v, back=0):
        # history.json holds Unix seconds; the oldest week has an ISO date instead.
        if isinstance(v, str):
            return datetime.fromisoformat(v).date()
        return datetime.fromtimestamp(v - back, ET).date()
    first, last = day(w["start"]), day(w["end"], back=1)
    if first.year != last.year:
        span = f"{first:%B} {first.day}, {first.year} to {last:%B} {last.day}, {last.year}"
    elif first.month != last.month:
        span = f"{first:%B} {first.day} to {last:%B} {last.day}, {last.year}"
    else:
        span = f"{first:%B} {first.day} to {last.day}, {last.year}"
    return "Week of " + span


def merge_main(current, history, trends, perchie=None):
    text = current
    # 1. Week page links.
    weeks = [w for w in reversed(history["weeks"]) if w.get("notion_url")]
    if not weeks:
        raise SystemExit("No week in history.json has a notion_url")
    ids = [w["notion_url"].rstrip("/").split("/")[-1].split("?")[0][-32:] for w in weeks]
    # The text inside a <page> tag is the child page's title, and replace_content
    # renames the page to it. Keep the title the page already shows; build it from
    # the week's dates only for a page not yet on the main page.
    titles = []
    for pid, w in zip(ids, weeks):
        m = re.search(r'<page url="[^"]*' + pid + r'[^"]*">(.*?)</page>', text, re.S)
        titles.append(m.group(1).strip() if m and m.group(1).strip() else esc(week_title(w)))
    for pid in ids:
        text = re.sub(r'\n*<page url="[^"]*' + pid + r'[^"]*">.*?</page>', "", text, flags=re.S)
    anchor = "Newest first."
    if text.count(anchor) != 1:
        raise SystemExit('Expected the line "Newest first." exactly once on the main page')
    tags = "\n\n".join(f'<page url="https://app.notion.com/p/{pid}">{t}</page>'
                        for pid, t in zip(ids, titles))
    text = text.replace(anchor, anchor + "\n\n" + tags, 1)
    # 2. Trends across weeks, up to the next level 2 heading (plain or toggle).
    start = text.find("## Trends across weeks")
    if start < 0:
        raise SystemExit('No "## Trends across weeks" heading on the main page')
    nxt = re.compile(r"\n(## (?!#)|<toggle heading=\"h[12]\">|</toggle>)")
    m = nxt.search(text, start + 3)
    end = m.start() if m else len(text)
    text = text[:start] + trends_md(trends) + "\n" + text[end:]
    # 3. The Perchie Review Loop toggle body.
    if perchie is not None:
        m = re.search(r'(<toggle heading="h[123]">\s*Perchie Review Loop\s*\n)(.*?)(\n</toggle>)', text, re.S)
        if not m:
            raise SystemExit('No "Perchie Review Loop" toggle heading on the main page')
        text = text[:m.start(2)] + "\n" + perchie.strip() + "\n" + text[m.end(2):]
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["week", "main"])
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--current")
    ap.add_argument("--history")
    ap.add_argument("--trends-spec")
    ap.add_argument("--perchie")
    a = ap.parse_args()
    if a.mode == "week":
        print(json.dumps(week(json.load(open(a.spec))), ensure_ascii=False))
    else:
        if not (a.current and a.history and a.trends_spec):
            raise SystemExit("main needs --current, --history and --trends-spec")
        perchie = open(a.perchie).read() if a.perchie else None
        sys.stdout.write(merge_main(page_content(open(a.current).read()), json.load(open(a.history)),
                                    json.load(open(a.trends_spec)), perchie))
