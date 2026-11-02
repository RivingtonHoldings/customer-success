"""Turn a report spec into Google Docs update_doc requests that fill one empty tab.

The Monday run writes each tab (the week's tab and the Trends tab) as a small
JSON spec, adds an empty tab to the running Google Doc, then runs this script
to get the requests that fill it in one update_doc call. Doing the index
arithmetic here keeps the unattended run from miscounting positions.

Spec format:
{
  "tabId": "t.abc123",
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

style is one of: title, h1, h2, h3, p, bullet, table.
bold and links name substrings of the block's text; the first match is used
unless a link gives "at", the offset of its text within the block.
A table sits after the text block before it (it cannot be the first block),
gets a bold header row, and its links name text inside one cell.

Usage: python3 -I build_tab_requests.py SPEC.json > requests.json
"""

import json
import sys

STYLES = {
    "title": "TITLE",
    "h1": "HEADING_1",
    "h2": "HEADING_2",
    "h3": "HEADING_3",
    "p": "NORMAL_TEXT",
    "bullet": "NORMAL_TEXT",
}


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def table_requests(tab, at, block):
    """Insert a filled table after the paragraph whose newline sits at `at`."""
    rows = block["rows"]
    R, C = len(rows), len(rows[0])
    if any(len(r) != C for r in rows):
        raise SystemExit("Every table row needs the same number of cells")
    reqs = [{"insertTable": {"rows": R, "columns": C, "location": {"index": at, "tabId": tab}}},
            # The empty paragraph Google adds after the table would otherwise
            # take the style of the paragraph the table was inserted into.
            {"updateParagraphStyle": {
                "range": {"startIndex": at + 3 + R * (2 * C + 1), "endIndex": at + 4 + R * (2 * C + 1), "tabId": tab},
                "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}}]

    def empty_pos(r, c):
        return at + 4 + r * (2 * C + 1) + 2 * c

    # Fill from the last cell to the first so each insert only shifts filled cells.
    for r in reversed(range(R)):
        for c in reversed(range(C)):
            if rows[r][c]:
                reqs.append({"insertText": {"location": {"index": empty_pos(r, c), "tabId": tab}, "text": rows[r][c]}})

    # After filling, a cell's text starts at its empty position plus every earlier cell's length.
    final, before = {}, 0
    for r in range(R):
        for c in range(C):
            final[(r, c)] = empty_pos(r, c) + before
            before += u16(rows[r][c])
    for c in range(C):
        if rows[0][c]:
            s = final[(0, c)]
            reqs.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(rows[0][c]), "tabId": tab},
                                             "textStyle": {"bold": True}, "fields": "bold"}})
    for link in block.get("links", []):
        cell = rows[link["row"]][link["col"]]
        k = cell.find(link["text"])
        if k < 0:
            raise SystemExit(f"{link['text']!r} not found in cell {cell!r}")
        s = final[(link["row"], link["col"])] + u16(cell[:k])
        reqs.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(link["text"]), "tabId": tab},
                                         "textStyle": {"link": {"url": link["url"]}}, "fields": "link"}})
    return reqs


def build(spec):
    tab = spec["tabId"]
    blocks = spec["blocks"]
    if blocks and blocks[0]["style"] == "table":
        raise SystemExit("A table cannot be the first block")
    for b in blocks:
        if b["style"] == "table":
            continue
        if b["style"] not in STYLES:
            raise SystemExit(f"Unknown style {b['style']!r}")
        if "\n" in b["text"]:
            raise SystemExit("A block's text cannot contain a newline; split it into blocks")

    text_blocks = [b for b in blocks if b["style"] != "table"]

    # A new tab holds one empty paragraph starting at index 1. Inserting the
    # joined text there leaves the last block in that original paragraph.
    full = "\n".join(b["text"] for b in text_blocks)
    requests = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": full}}]

    pos = 1
    spans = []
    tables = []  # (index of the newline the table goes before, table block)
    for b in blocks:
        if b["style"] == "table":
            tables.append((spans[-1][2] - 1, b))
            continue
        start = pos
        end = start + u16(b["text"]) + 1  # include the paragraph's newline
        spans.append((b, start, end))
        pos = end

    for b, start, end in spans:
        # A new tab's paragraphs are already Normal text; only headings need a request.
        if STYLES[b["style"]] == "NORMAL_TEXT":
            continue
        style = {"namedStyleType": STYLES[b["style"]]}
        fields = "namedStyleType"
        if b["style"] in ("title", "h1", "h2", "h3"):
            style["keepWithNext"] = True
            fields += ",keepWithNext"
        requests.append({"updateParagraphStyle": {
            "range": {"startIndex": start, "endIndex": end, "tabId": tab},
            "paragraphStyle": style, "fields": fields}})

    # Consecutive bullet blocks become one list.
    run = None
    for b, start, end in spans + [(None, None, None)]:
        if b is not None and b["style"] == "bullet":
            run = (run[0], end) if run else (start, end)
            continue
        if run:
            requests.append({"createParagraphBullets": {
                "range": {"startIndex": run[0], "endIndex": run[1] - 1, "tabId": tab},
                "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
            run = None

    for b, start, end in spans:
        for key, text_style, fields in (
            ("bold", {"bold": True}, "bold"),
            ("links", None, "link"),
        ):
            for item in b.get(key, []):
                needle = item if key == "bold" else item["text"]
                # A link may give "at" when its text also appears earlier in the block.
                at = item.get("at", -1) if key == "links" else -1
                if at < 0:
                    at = b["text"].find(needle)
                if at < 0:
                    raise SystemExit(f"{needle!r} not found in block {b['text']!r}")
                s = start + u16(b["text"][:at])
                style = text_style or {"link": {"url": item["url"]}}
                requests.append({"updateTextStyle": {
                    "range": {"startIndex": s, "endIndex": s + u16(needle), "tabId": tab},
                    "textStyle": style, "fields": fields}})

    # Tables go in last, the one lowest in the tab first, so an inserted table
    # never moves the anchor of a table above it.
    for at, b in sorted(tables, key=lambda t: -t[0]):
        requests.extend(table_requests(tab, at, b))

    return requests


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(json.dumps({"requests": build(json.load(f))}, separators=(",", ":")))
