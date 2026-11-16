#!/usr/bin/env python3
"""Numbers and Sheets chart requests for the weekly Baldwin trends slides.

The Doc half of the weekly run (the runbook) leaves three files behind:
<date>-collected.json and <date>-classified.json in the confidential staging
folder, and history.json with the finished week appended. This script turns
them into the small, name-free numbers the slides need, and into the
update_spreadsheet requests that draw the three charts on the week's tab of
the chart data spreadsheet, so no one counts days or row indexes by hand.

Subcommands:
  data    Write slide-data.json: totals, conversations per day, request types,
          theme trend across weeks, signals, and the rows to write to the
          week's tab starting at A1.
  charts  Print the addChart requests for one week's tab, given its sheetId.

Usage:
  python3 -I slide_data.py data --collected C.json --classified K.json \
      --history history.json --out slide-data.json
  python3 -I slide_data.py charts --data slide-data.json --sheet-id 123456789
"""

import argparse
import json
from collections import Counter, OrderedDict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
TEST_THEME = "Internal / Test / Spam"
# classified.json "kind" -> the request types on the slide, in display order.
KIND_LABELS = OrderedDict([
    ("question", "How-to"),
    ("bug", "Bug"),
    ("request", "Feature request"),
    ("feedback", "Other"),
    ("admin", "Other"),
])
TREND_WEEKS = 6   # weeks shown in the theme trend chart
TREND_THEMES = 5  # themes shown, by this week's count

# Column layout of the week's tab. Each block starts in row 1 with a header.
DAILY_COL, TYPES_COL, TREND_COL = 0, 3, 6  # A, D, G


def week_days(start, end):
    """Calendar days (Eastern) that the window touches, in order."""
    d = datetime.fromtimestamp(start, ET).date()
    last = datetime.fromtimestamp(end - 1, ET).date()
    out = []
    while d <= last:
        out.append(d)
        d += timedelta(days=1)
    return out


def cmd_data(a):
    collected = json.load(open(a.collected))
    classified = json.load(open(a.classified))
    history = json.load(open(a.history))
    weeks = [w for w in history["weeks"] if w.get("complete")]
    this = weeks[-1]
    prior = weeks[-2] if len(weeks) > 1 else None

    convs = {str(c["id"]): c for c in collected["conversations"]}
    counted = {cid: v for cid, v in classified.items()
               if v.get("theme") != TEST_THEME and cid in convs}

    # Conversations per day, Eastern time.
    days = week_days(collected["start"], collected["end"])
    per_day = Counter(
        datetime.fromtimestamp(convs[cid]["created_at"], ET).date() for cid in counted)
    daily = [["Day", "Conversations"]] + [
        [d.strftime("%a %b ") + str(d.day), per_day.get(d, 0)] for d in days]

    # Request types.
    kinds = Counter(v.get("kind") for v in counted.values())
    types = OrderedDict((label, 0) for label in KIND_LABELS.values())
    for k, n in kinds.items():
        types[KIND_LABELS.get(k, "Other")] += n
    request_types = [["Type", "Conversations"]] + [[k, n] for k, n in types.items()]

    # Theme trend: this week's top themes across the last weeks, oldest first.
    shown = weeks[-TREND_WEEKS:]
    top = [t for t, _ in sorted(this["themes"].items(), key=lambda kv: -kv[1])
           if t != "Other"][:TREND_THEMES]
    trend = [["Theme"] + [w["label"] for w in shown]]
    for t in top:
        trend.append([t] + [w["themes"].get(t, 0) for w in shown])

    # Rows for the week's tab, A1 onward: three side-by-side blocks.
    height = max(len(daily), len(request_types), len(trend))
    width = TREND_COL + len(trend[0])
    grid = [[""] * width for _ in range(height)]
    for col, block in ((DAILY_COL, daily), (TYPES_COL, request_types), (TREND_COL, trend)):
        for r, row in enumerate(block):
            for c, v in enumerate(row):
                grid[r][col + c] = v

    out = {
        "label": this["label"],
        "start": collected["start"],
        "end": collected["end"],
        "conversations": len(counted),
        "history_conversations": this["conversations"],
        "prior_label": prior["label"] if prior else None,
        "prior_conversations": prior["conversations"] if prior else None,
        "signals": this.get("signals", {}),
        "kinds": dict(kinds),
        "daily": daily,
        "request_types": request_types,
        "theme_trend": trend,
        "sheet_rows": grid,
    }
    if out["conversations"] != this["conversations"]:
        out["warning"] = ("Counted %d conversations but history.json says %d for %s; "
                          "check that the staging files are this week's."
                          % (out["conversations"], this["conversations"], this["label"]))
    json.dump(out, open(a.out, "w"), indent=2)
    print(json.dumps({k: out[k] for k in ("label", "conversations", "prior_conversations",
                                          "kinds")}, indent=2))
    if "warning" in out:
        print("WARNING:", out["warning"])


def rng(sheet_id, rows, col, cols=1):
    return {"sourceRange": {"sources": [{
        "sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": rows,
        "startColumnIndex": col, "endColumnIndex": col + cols}]}}


def chart(sheet_id, kind, rows, col, series_cols, anchor_row, axis_title, legend):
    series = [{"series": rng(sheet_id, rows, col + 1 + i),
               "targetAxis": "BOTTOM_AXIS" if kind == "BAR" else "LEFT_AXIS"}
              for i in range(series_cols)]
    return {"addChart": {"chart": {
        "spec": {
            "fontName": "Arial",
            "basicChart": {
                "chartType": kind,
                "legendPosition": "BOTTOM_LEGEND" if legend else "NO_LEGEND",
                "axis": [{"position": "BOTTOM_AXIS" if kind != "BAR" else "LEFT_AXIS",
                          "title": ""},
                         {"position": "LEFT_AXIS" if kind != "BAR" else "BOTTOM_AXIS",
                          "title": axis_title}],
                "domains": [{"domain": rng(sheet_id, rows, col)}],
                "series": series,
                "headerCount": 1}},
        "position": {"overlayPosition": {"anchorCell": {
            "sheetId": sheet_id, "rowIndex": anchor_row, "columnIndex": col}}}}}}


def cmd_charts(a):
    d = json.load(open(a.data))
    sid = a.sheet_id
    below = len(d["sheet_rows"]) + 2
    reqs = [
        chart(sid, "COLUMN", len(d["daily"]), DAILY_COL, 1, below, "Conversations", False),
        chart(sid, "BAR", len(d["request_types"]), TYPES_COL, 1, below + 20, "Conversations", False),
        chart(sid, "BAR", len(d["theme_trend"]), TREND_COL, len(d["theme_trend"][0]) - 1,
              below + 40, "Conversations", True),
    ]
    print(json.dumps({"requests": reqs}, indent=2))
    print("Charts in order: conversations per day, request types, theme trend.",
          file=__import__("sys").stderr)


# Drawn charts. The Slides connector refuses createSheetsChart ("Permission
# denied"), so the charts are drawn in the deck from rectangles and text boxes.
# Frames are the template's outlined rectangles (runbook "Slides" section).
EMU = 914400
FRAMES = {  # objectId of the frame, page, x, y, w, h in EMU
    "daily": ("h418bda9a80e95acc_0_3", "h5fd9f7b563dd3a42_0_461", 485275, 3108325, 3258000, 1450500),
    "trend": ("h418bda9a80e95acc_0_5", "h5fd9f7b563dd3a42_0_461", 4585625, 1617800, 4340100, 2398800),
    "types": ("h418bda9a80e95acc_0_8", "h5fd9f7b563dd3a42_0_229", 333475, 1606700, 3829800, 2819400),
}
PLACEHOLDER_TEXT = {"daily": "h418bda9a80e95acc_0_1", "trend": "h418bda9a80e95acc_0_4",
                    "types": "h418bda9a80e95acc_0_9"}
FONT = "Inter"
THIS = {"red": 0.17, "green": 0.33, "blue": 0.62}
PRIOR = {"red": 0.74, "green": 0.76, "blue": 0.80}


def _box(oid, page, x, y, w, h, kind="TEXT_BOX"):
    return {"createShape": {"objectId": oid, "shapeType": kind, "elementProperties": {
        "pageObjectId": page,
        "size": {"width": {"magnitude": max(int(w), 12700), "unit": "EMU"},
                 "height": {"magnitude": max(int(h), 12700), "unit": "EMU"}},
        "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x), "translateY": int(y), "unit": "EMU"}}}}


def _text(oid, page, x, y, w, h, text, size, align="START", bold=False):
    reqs = [
        _box(oid, page, x, y, w, h),
        {"insertText": {"objectId": oid, "text": text}},
        {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"}, "style": {
            "fontFamily": FONT, "fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold},
            "fields": "fontFamily,fontSize,bold"}},
        {"updateShapeProperties": {"objectId": oid, "shapeProperties": {
            "contentAlignment": "MIDDLE"}, "fields": "contentAlignment"}},
    ]
    if align != "START":
        reqs.append({"updateParagraphStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                                              "style": {"alignment": align}, "fields": "alignment"}})
    return reqs


def _bar(oid, page, x, y, w, h, color):
    return [
        _box(oid, page, x, y, w, h, "RECTANGLE"),
        {"updateShapeProperties": {"objectId": oid, "shapeProperties": {
            "shapeBackgroundFill": {"solidFill": {"color": {"rgbColor": color}}},
            "outline": {"propertyState": "NOT_RENDERED"}}, "fields": "shapeBackgroundFill,outline"}},
    ]


def _hbars(key, rows, series_colors, legend=None):
    """Horizontal bars inside a frame. rows: [(label, [v1, v2...])]."""
    _, page, fx, fy, fw, fh = FRAMES[key]
    pad = int(0.1 * EMU)
    x0, y0, w, h = fx + pad, fy + pad, fw - 2 * pad, fh - 2 * pad
    reqs = []
    if legend:
        lx = x0
        for i, (name, color) in enumerate(legend):
            reqs += _bar(f"{key}_lg{i}", page, lx, y0 + int(0.07 * EMU), int(0.12 * EMU), int(0.12 * EMU), color)
            reqs += _text(f"{key}_lgt{i}", page, lx + int(0.15 * EMU), y0, int(1.6 * EMU), int(0.26 * EMU), name, 10)
            lx += int(1.75 * EMU)
        y0 += int(0.32 * EMU)
        h -= int(0.32 * EMU)
    label_w = int(w * 0.42)
    value_w = int(0.35 * EMU)
    bar_x = x0 + label_w + int(0.05 * EMU)
    bar_max = w - label_w - value_w - int(0.1 * EMU)
    top = max(max(vs) for _, vs in rows) or 1
    row_h = h / len(rows)
    nser = len(rows[0][1])
    bar_h = row_h * 0.7 / nser
    for r, (label, vs) in enumerate(rows):
        ry = y0 + r * row_h
        reqs += _text(f"{key}_l{r}", page, x0, ry, label_w, row_h, label, 10, align="END")
        for s, v in enumerate(vs):
            by = ry + row_h * 0.15 + s * bar_h
            bw = bar_max * v / top
            if v:
                reqs += _bar(f"{key}_b{r}_{s}", page, bar_x, by, bw, bar_h, series_colors[s])
            reqs += _text(f"{key}_v{r}_{s}", page, bar_x + bw + int(0.03 * EMU), by - bar_h * 0.25,
                          value_w, bar_h * 1.5, str(v), 9 if nser > 1 else 10, bold=(s == nser - 1))
    return reqs


def _columns(key, rows):
    """Vertical columns inside a frame. rows: [(label, value)]."""
    _, page, fx, fy, fw, fh = FRAMES[key]
    pad = int(0.08 * EMU)
    x0, y0, w, h = fx + pad, fy + pad, fw - 2 * pad, fh - 2 * pad
    label_h, value_h = int(0.24 * EMU), int(0.2 * EMU)
    plot_h = h - label_h - value_h
    col_w = w / len(rows)
    top = max(v for _, v in rows) or 1
    reqs = []
    for i, (label, v) in enumerate(rows):
        cx = x0 + i * col_w
        bh = plot_h * v / top
        by = y0 + value_h + plot_h - bh
        if v:
            reqs += _bar(f"{key}_b{i}", page, cx + col_w * 0.18, by, col_w * 0.64, bh, THIS)
        reqs += _text(f"{key}_v{i}", page, cx, by - value_h, col_w, value_h, str(v), 10, align="CENTER", bold=True)
        reqs += _text(f"{key}_l{i}", page, cx, y0 + value_h + plot_h, col_w, label_h, label, 9, align="CENTER")
    return reqs


def cmd_shapes(a):
    d = json.load(open(a.data))
    # One batch per chart keeps each update_presentation call small.
    # Conversations per day: "Mon Nov 9" -> "Mon 9".
    daily = [(f"{lab.split()[0]} {lab.split()[2]}", int(v)) for lab, v in d["daily"][1:]]
    types = [(lab, [int(v)]) for lab, v in d["request_types"][1:]]
    head = d["theme_trend"][0]
    trend = [(row[0], [int(row[-2]), int(row[-1])]) for row in d["theme_trend"][1:]]
    out = {
        "daily": [{"deleteObject": {"objectId": PLACEHOLDER_TEXT["daily"]}}] + _columns("daily", daily),
        "types": [{"deleteObject": {"objectId": PLACEHOLDER_TEXT["types"]}}] + _hbars("types", types, [THIS]),
        "trend": [{"deleteObject": {"objectId": PLACEHOLDER_TEXT["trend"]}}]
                 + _hbars("trend", trend, [PRIOR, THIS], legend=[(head[-2], PRIOR), (head[-1], THIS)]),
    }
    print(json.dumps(out, separators=(",", ":")))
    print("Batches: " + ", ".join(f"{k} {len(v)} requests" for k, v in out.items())
          + f". Theme bars compare {head[-2]} with {head[-1]}.", file=__import__("sys").stderr)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("data")
    d.add_argument("--collected", required=True)
    d.add_argument("--classified", required=True)
    d.add_argument("--history", required=True)
    d.add_argument("--out", required=True)
    c = sub.add_parser("charts")
    c.add_argument("--data", required=True)
    c.add_argument("--sheet-id", type=int, required=True)
    s = sub.add_parser("shapes")
    s.add_argument("--data", required=True)
    a = p.parse_args()
    {"data": cmd_data, "charts": cmd_charts, "shapes": cmd_shapes}[a.cmd](a)


if __name__ == "__main__":
    main()
