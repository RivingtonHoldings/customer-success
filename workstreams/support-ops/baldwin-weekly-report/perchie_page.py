"""Build the Perchie Review Loop page (one HTML file) from perchie-review.json.

Each Friday run reviews 20 Baldwin conversations Perchie (Fin) handled, adds
the week to perchie-review.json, runs this script, and republishes the HTML to
the same artifact URL, so the link in Notion never changes.

perchie-review.json:
{
  "artifact_url": "https://claude.ai/...",
  "weeks": [                      # oldest first
    {"label": "Nov 9 to 16", "year": 2026, "notion_url": "...",
     "pool": 67,                  # Baldwin conversations Perchie handled that week
     "conversations": [
       {"id": "2154...", "question": "...", "perchie_answer": "...",
        "verdict": "Correct", "cause": "None", "source_article": "file.md" | null,
        "source_title": "...", "source_url": "https://support.perchwell.com/...",
        "fix_id": "F1" | null}],
     "fixes": [
       {"id": "F1", "type": "article" | "rule", "target": "Article title or rule name",
        "change": "What changes, in a sentence or two",
        "status": "Proposed" | "Waiting on a teammate" | "Drafted" | "Live",
        "conversations": ["2154..."],
        "where": "Notion or Intercom link, optional"}]}
  ]
}

No member names, emails, phone numbers, brokerage names, or addresses. The
question and answer fields are short paraphrases.

Usage: python3 -I perchie_page.py perchie-review.json OUT.html [TOGGLE.md]
TOGGLE.md, when given, gets the body of the "Perchie Review Loop" toggle on
the main Notion page, for notion_page.py main --perchie.
"""

import html
import json
import sys

VERDICTS = ["Correct", "Partly correct", "Wrong", "No answer", "Should have handed off", "Not a Perchie question"]
TONE = {"Correct": "good", "Partly correct": "warn", "Wrong": "bad", "No answer": "bad",
        "Should have handed off": "warn", "Not a Perchie question": "muted"}
STATUS_TONE = {"Live": "good", "Drafted": "info", "Proposed": "muted", "Waiting on a teammate": "warn"}
CONVO = "https://app.intercom.com/a/inbox/trq7czv5/inbox/conversation/"


def e(s):
    return html.escape(str(s or ""))


def score(week):
    """Share Perchie got right, among the questions it was meant to answer."""
    judged = [c for c in week["conversations"] if c["verdict"] != "Not a Perchie question"]
    right = sum(c["verdict"] == "Correct" for c in judged)
    return right, len(judged)


def chip(text, tone):
    return f'<span class="chip {tone}">{e(text)}</span>'


def week_block(w, open_=False):
    right, judged = score(w)
    pct = round(100 * right / judged) if judged else 0
    counts = {v: sum(c["verdict"] == v for c in w["conversations"]) for v in VERDICTS}
    fixes = w.get("fixes", [])
    num = {c["id"]: n for n, c in enumerate(w["conversations"], 1)}

    def refs(f):
        ids = [i for i in f.get("conversations", []) if i in num]
        if not ids:
            return ""
        links = ", ".join(f'<a href="{CONVO}{e(i)}">{num[i]}</a>' for i in ids)
        return f'<span class="refs">From conversation{"s" if len(ids) > 1 else ""} {links}</span>'

    fix_rows = "".join(
        f'<li class="fix"><div class="fixhead"><span class="fid">{e(f["id"])}</span>'
        f'{chip(f["status"], STATUS_TONE.get(f["status"], "muted"))}'
        f'<span class="kind">{"Article" if f["type"] == "article" else "Perchie rule"}</span>'
        f'<strong>{e(f["target"])}</strong></div><p>{e(f["change"])}</p>'
        f'<div class="fixfoot">{refs(f)}'
        + (f'<a href="{e(f["where"])}">Open the fix</a>' if f.get("where") else "")
        + "</div></li>" for f in fixes) or '<li class="fix"><p>No fixes needed this week.</p></li>'
    rows = []
    for n, c in enumerate(w["conversations"], 1):
        if c.get("source_url"):
            src = f'<a href="{e(c["source_url"])}">{e(c.get("source_title") or c["source_article"])}</a>'
        elif c.get("source_article"):
            src = e(c["source_article"].removesuffix(".md").replace("-", " "))
        else:
            src = "None"
        rows.append(
            f'<tr><td class="num"><a href="{CONVO}{e(c["id"])}">{n}</a></td>'
            f'<td>{chip(c["verdict"], TONE.get(c["verdict"], "muted"))}</td>'
            f'<td>{e(c["question"])}</td><td>{e(c["perchie_answer"])}</td>'
            f'<td>{e(c["cause"])}</td><td>{src}</td><td>{e(c.get("fix_id") or "")}</td></tr>')
    tally = " ".join(f'{chip(f"{v} {counts[v]}", TONE[v])}' for v in VERDICTS if counts[v])
    return f'''<details class="week" {"open" if open_ else ""}>
<summary><span class="wk">Week of {e(w["label"])}, {e(w["year"])}</span>
<span class="sum"><b>{right} of {judged}</b> right ({pct}%) &middot; {len(w["conversations"])} reviewed of {e(w.get("pool", "?"))} &middot; {len(fixes)} fix{"es" if len(fixes) != 1 else ""}</span></summary>
<div class="tally">{tally}</div>
<h3>Fixes</h3>
<ul class="fixes">{fix_rows}</ul>
<h3>Conversations reviewed</h3>
<div class="scroll"><table>
<thead><tr><th>#</th><th>Verdict</th><th>Member asked</th><th>Perchie said</th><th>Cause</th><th>Source article</th><th>Fix</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
{f'<p class="note"><a href="{e(w["notion_url"])}">This week in the Baldwin trends report</a></p>' if w.get("notion_url") else ""}
</details>'''


def trend(weeks):
    cells = []
    for w in weeks[-8:]:
        right, judged = score(w)
        pct = round(100 * right / judged) if judged else 0
        cells.append(f'<div class="bar"><div class="track"><div class="fill" style="height:{pct}%"></div></div>'
                     f'<b>{pct}%</b><span>{e(w["label"])}</span></div>')
    return "".join(cells)


def page(data):
    weeks = data["weeks"]
    latest = weeks[-1]
    right, judged = score(latest)
    live = sum(f["status"] == "Live" for w in weeks for f in w.get("fixes", []))
    open_fixes = [f for w in weeks for f in w.get("fixes", []) if f["status"] != "Live"]
    blocks = "\n".join(week_block(w, open_=(i == 0)) for i, w in enumerate(reversed(weeks)))
    return f'''<title>Perchie Review Loop</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap">
<style>
/* Layout: one reading column; the latest week open, earlier weeks folded below. */
:root {{
  --bg: #f6f7f9; --panel: #ffffff; --fg: #1b2230; --muted: #5d6677; --line: #dfe3ea;
  --accent: #2b549e; --accent-soft: #e6ecf7;
  --good: #1f7a4d; --good-bg: #e3f3ea; --warn: #8a5a00; --warn-bg: #fbf0d9; --bad: #a32c2c; --bad-bg: #f8e3e3;
  --display: "Space Grotesk", "Inter", system-ui, sans-serif; --body: "Inter", system-ui, -apple-system, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #12161d; --panel: #1a2029; --fg: #e6e9ef; --muted: #9aa3b2; --line: #2c3442;
  --accent: #8fb0ea; --accent-soft: #1f2a3d;
  --good: #7fd1a6; --good-bg: #183327; --warn: #f0c46b; --warn-bg: #352a14; --bad: #f19b9b; --bad-bg: #3a1d1d; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #12161d; --panel: #1a2029; --fg: #e6e9ef; --muted: #9aa3b2; --line: #2c3442;
  --accent: #8fb0ea; --accent-soft: #1f2a3d;
  --good: #7fd1a6; --good-bg: #183327; --warn: #f0c46b; --warn-bg: #352a14; --bad: #f19b9b; --bad-bg: #3a1d1d; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 15px/1.55 var(--body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 32px 48px; }}
main {{ max-width: 1080px; margin: 0 auto; display: grid; gap: 24px; }}
h1, h2, h3 {{ font-family: var(--display); text-wrap: balance; margin: 0; }}
h1 {{ font-size: 30px; letter-spacing: -0.01em; }}
h2 {{ font-size: 18px; }}
h3 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin-top: 8px; }}
p {{ margin: 0; }}
a {{ color: var(--accent); }}
a:focus-visible, summary:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.lede {{ color: var(--muted); max-width: 68ch; }}
.head {{ display: grid; gap: 8px; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }}
.stat {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; display: grid; gap: 2px; }}
.stat b {{ font: 600 26px/1.1 var(--display); font-variant-numeric: tabular-nums; }}
.stat span {{ color: var(--muted); font-size: 13px; }}
.trend {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 16px; display: grid; gap: 12px; }}
.bars {{ display: flex; gap: 16px; align-items: flex-end; overflow-x: auto; }}
.bar {{ display: grid; justify-items: center; gap: 4px; min-width: 64px; font-size: 12px; color: var(--muted); }}
.bar b {{ color: var(--fg); font-variant-numeric: tabular-nums; }}
.track {{ width: 28px; height: 90px; background: var(--accent-soft); border-radius: 4px; display: flex; align-items: flex-end; overflow: hidden; }}
.fill {{ width: 100%; background: var(--accent); }}
.week {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 4px 16px 16px; }}
.week[open] {{ display: grid; gap: 12px; }}
summary {{ cursor: pointer; padding: 12px 0 8px; display: flex; flex-wrap: wrap; gap: 4px 16px; align-items: baseline; }}
.wk {{ font: 600 18px var(--display); }}
.sum {{ color: var(--muted); font-size: 14px; }}
.sum b {{ color: var(--fg); }}
.tally {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.chip {{ display: inline-block; padding: 1px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; white-space: nowrap; }}
.chip.good {{ color: var(--good); background: var(--good-bg); }}
.chip.warn {{ color: var(--warn); background: var(--warn-bg); }}
.chip.bad {{ color: var(--bad); background: var(--bad-bg); }}
.chip.muted {{ color: var(--muted); background: var(--accent-soft); }}
.fixes {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }}
.fix {{ border: 1px solid var(--line); border-radius: 8px; padding: 10px 12px; display: grid; gap: 4px; }}
.fixhead {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
.chip.info {{ color: var(--accent); background: var(--accent-soft); }}
.fid {{ font: 600 13px var(--display); color: var(--muted); font-variant-numeric: tabular-nums; }}
.fixfoot {{ display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 13px; color: var(--muted); }}
.kind {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }}
.scroll {{ overflow-x: auto; min-width: 0; }}
table {{ border-collapse: collapse; width: 100%; min-width: 860px; font-size: 13.5px; }}
th, td {{ text-align: left; vertical-align: top; padding: 8px 10px; border-bottom: 1px solid var(--line); }}
th {{ font-size: 12px; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }}
td.num {{ font-variant-numeric: tabular-nums; }}
.note {{ font-size: 13px; color: var(--muted); }}
.how {{ color: var(--muted); font-size: 13.5px; display: grid; gap: 6px; max-width: 80ch; }}
</style>
<main>
<header class="head">
<h1>Perchie Review Loop</h1>
<p class="lede">Every week we read 20 Baldwin conversations Perchie answered, grade each answer, and fix the help center article or Perchie rule behind every miss. Newest week first.</p>
</header>
<section class="stats">
<div class="stat"><b>{right} of {judged}</b><span>right in the week of {e(latest["label"])}</span></div>
<div class="stat"><b>{len(latest["conversations"])}</b><span>conversations reviewed this week</span></div>
<div class="stat"><b>{len(open_fixes)}</b><span>fixes not live yet</span></div>
<div class="stat"><b>{live}</b><span>fixes live in Intercom so far</span></div>
</section>
<section class="trend"><h2>Share Perchie got right, by week</h2><div class="bars">{trend(weeks)}</div></section>
{blocks}
<section class="how"><h2>How the review works</h2>
<p>The sample is every conversation Perchie handed to a teammate or got a thumbs down or a 1 or 2 rating on, then conversations Perchie marked resolved, spread across the week's themes, up to 20.</p>
<p>"Right" counts only questions Perchie was meant to answer; bug reports and MLS staff requests are marked "Not a Perchie question" and left out of the share.</p>
<p>The sample leans toward likely misses on purpose, so the share right runs lower than across all of Perchie's conversations. Compare it week to week, not with Intercom's resolution rate.</p>
<p>A fix is Proposed when the change is written here, Waiting on a teammate when product or MLS staff must confirm the facts first, Drafted once the article change is in the Notion help center database or the rule text is ready to paste, and Live once a teammate has published it in Intercom. Perchie reads published articles only, which means a fix changes its answers only once it is Live.</p>
</section>
</main>
'''


def toggle_md(data):
    """Body of the "Perchie Review Loop" toggle on the main Notion page."""
    w = data["weeks"][-1]
    right, judged = score(w)
    fixes = w.get("fixes", [])
    arts = sum(f["type"] == "article" for f in fixes)
    live = sum(f["status"] == "Live" for f in fixes)
    return (
        "Every week we read 20 Baldwin conversations Perchie (Fin) answered, grade each answer, and fix the help "
        "center article or Perchie rule behind every miss. The results page lists every conversation, its grade, "
        "and each fix with its status. It keeps the same link and gets a new week each Friday.\n\n"
        f"[Perchie Review Loop results]({data['artifact_url']})\n\n"
        f"**Latest, week of {w['label']}:** {right} of {judged} right, from {len(w['conversations'])} conversations "
        f"reviewed. {len(fixes)} fixes: {arts} articles and {len(fixes) - arts} Perchie rules, "
        f"{live if live else 'none'} live yet.\n")


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(page(data))
    if len(sys.argv) > 3 and data.get("artifact_url"):
        open(sys.argv[3], "w").write(toggle_md(data))
