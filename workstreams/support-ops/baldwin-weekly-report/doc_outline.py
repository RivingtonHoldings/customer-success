"""Print a saved read_doc result as a short outline, to find tab IDs and check a run's output.

Usage: python3 -I doc_outline.py READ_DOC.json [TAB_TITLE]

Without TAB_TITLE it lists the tabs and the revisionId. With it, it prints that
tab paragraph by paragraph: style, a bullet mark, *bold* and [linked] text,
table rows joined with |, and a character count for the two-page check.
"""

import json
import sys


def walk(content, out):
    for el in content:
        if "paragraph" in el:
            p = el["paragraph"]
            txt = ""
            for e in p["elements"]:
                tr = e.get("textRun")
                if not tr:
                    continue
                t, ts = tr["content"].rstrip("\n"), tr["textStyle"]
                txt += f"[{t}]" if ts.get("link") else (f"*{t}*" if ts.get("bold") else t)
            out.append((p["paragraphStyle"]["namedStyleType"], "•" if "bullet" in p else " ", txt))
        elif "table" in el:
            for r in el["table"]["tableRows"]:
                cells = []
                for c in r["tableCells"]:
                    o = []
                    walk(c["content"], o)
                    cells.append(" ".join(x[2] for x in o))
                out.append(("TABLE", " ", " | ".join(cells)))


with open(sys.argv[1]) as f:
    d = json.load(f)
d = d.get("content", d)
print("revisionId:", d["revisionId"])
for t in d["tabs"]:
    print(f"tab {t['tabProperties']['tabId']}  index {t['tabProperties'].get('index', 0)}  {t['tabProperties']['title']}")
if len(sys.argv) > 2:
    tab = next(t for t in d["tabs"] if t["tabProperties"]["title"] == sys.argv[2])
    rows = []
    walk(tab["documentTab"]["body"]["content"], rows)
    for style, mark, txt in rows:
        print(style[:9].ljust(9), mark, txt)
    print("characters:", sum(len(r[2]) for r in rows))
