---
name: baldwin-weekly-trends
description: Run the weekly Baldwin support trends report end to end. Collects the week's Baldwin Intercom conversations, updates the Baldwin Member Feedback Trends Google Doc, then makes that week's Google Slides deck from Kevin's "support trend slides Template" (conversations per day, request type breakdown, persisting topics, trend feedback). Use whenever a teammate types /baldwin-weekly-trends, or says "run the Baldwin trends," "make this week's Baldwin slides," "weekly Baldwin report," "Baldwin trend deck," "support trend slides," or asks what Baldwin members were asking about this week and wants it in the doc or the slides. Also the procedure the Friday 10 PM scheduled task follows. Not for the Baldwin Bible (use baldwin-bible-maintenance) or for CRMLS.
---

# Baldwin weekly trends: doc and slides

One run does two things, in this order:

1. **The doc.** Follow the runbook, `workstreams/support-ops/baldwin-weekly-report/baldwin-weekly-trends-runbook.md`, "Weekly run" section, steps 1 to 11. It collects the week's Intercom conversations, classifies them, updates `history.json`, and writes the week's tab and the Trends tab in the Baldwin Member Feedback Trends doc. Everything in its "Rules for every run" applies to this whole skill.
2. **The slides.** Make a new deck for the same week from the template, filled with charts and numbers from step 1. The steps are below.

The slides come second because they reuse step 1's numbers. Building them from a separate collection would give two different counts for the same week.

Read the runbook in full before you start. Its "Slides" section holds the file IDs this skill uses.

## Modes

- **Full run (default, and what the Friday task does):** doc, then slides.
- **Slides only:** when the teammate says "slides only" or "just the slides," or when the last week in `history.json` ended less than 24 hours ago and its staging files are still in the confidential folder. Make the slides for that finished week and leave the doc and `history.json` alone. A full run started early would cut the week short and leave the Friday run a sliver of a window, so if it is not Friday evening and the teammate did not ask for a full run, ask before collecting.

## Tools

Match connector tools by the part of the name after the last `__`; the server ID differs per teammate.

| Need | Connector | Tools |
|---|---|---|
| Conversations | Intercom (read only) | `search_conversations`, `get_conversation` |
| The doc | Google Docs | `read_doc`, `update_doc` |
| Chart data | Google Sheets | `get_spreadsheet`, `update_spreadsheet`, `update_values` |
| Copy the template, export to check | Google Drive | `copy_file`, `get_file_metadata`, `download_file_content` |
| The deck | Google Slides | `read_presentation`, `update_presentation` |

Before any Google write, load the `anthropic-skills:google-workspace` skill and read its `references/slides.md` (Slides connector part) and the Charts section of `references/sheets.md`. Its helper `scripts/slides_helper.py outline` gives real slide geometry.

If a connector is missing, say which one in plain words ("Google Slides is not connected yet. In claude.ai, open Settings, then Connectors, connect Google Slides, then start a new session.") and stop that half. A missing Slides connector still lets the doc half run; say so in the summary.

## Slides steps

All staging files go in `workstreams/support-ops/confidential/baldwin-weekly-report/` (git-ignored). `<date>` is the staging date the doc half used.

### 1. Compute the slide numbers

```
python3 -I .claude/skills/baldwin-weekly-trends/scripts/slide_data.py data \
  --collected <staging>/<date>-collected.json \
  --classified <staging>/<date>-classified.json \
  --history workstreams/support-ops/baldwin-weekly-report/history.json \
  --out <staging>/<date>-slide-data.json
```

It counts the week's conversations (tests left out), conversations per Eastern calendar day, request types (How-to, Bug, Feature request, Other, from each conversation's `kind`), and this week's top five themes across the last six weeks. If it prints a WARNING that its count differs from `history.json`, the staging files are from another week: find the right ones before going on.

On a full run, also add the week's `kinds` from the output to the week's entry in `history.json` as `"kinds"`, so later weeks can compare request types.

### 2. Put the chart data in the week's own tab

The chart data spreadsheet is named in the runbook's "Slides" section. Each week gets its own tab, named with the week label (`Nov 9 to 13`), so a linked chart in an older deck never changes when a new week is added. If the spreadsheet does not exist yet, create it with Drive `create_file` (`application/vnd.google-apps.spreadsheet`, title "Baldwin support trends chart data", same parent folder as the template) and write its ID into the runbook.

1. `update_spreadsheet` with `addSheet` titled the week label. If a tab with that title exists (a rerun), delete it in the same batch first. The reply gives the new `sheetId`.
2. `update_values` the `sheet_rows` from slide-data.json into `'<label>'!A1`.

The tab is the record of the numbers. The deck does not link to it: the Slides connector refuses `createSheetsChart`, so the charts are drawn in step 4.

### 3. Copy the template

Drive `copy_file` on the template, into the same parent folder, titled `Baldwin support trends, <label>, <year>` (for example `Baldwin support trends, Nov 9 to 13, 2026`). Never edit the template itself. On a rerun for the same week, make a new copy and tell the teammate the older copy can be deleted; do not trash it yourself.

### 4. Fill the copy

Read the copy with `read_presentation` and the field mask from the Slides reference, save the result, and run `slides_helper.py outline` on it. Find each placeholder box by its text. The runbook's "Slides" section lists the object IDs once a run has recorded them; check them against the read, since a teammate may have changed the template.

| Placeholder text in the template | Replace with |
|---|---|
| "Image of New Conversations from Past Week" | A number box: `<N> new Baldwin conversations` on the first line, `<M> the week before (<label of prior week>)` on the second. Keep the box; replace its text and make the first line large and bold. |
| "Graph of Conversations per Day over the past week" | Columns, one per day |
| "Graph of Persisting Trends from the Past week..." | Paired bars for this week's top five themes, last week against this week |
| "Graph from Intercom Dashboard of ticket breakdown..." | Bars for How-to, Bug, Feature request, Other |
| "Any additional/helpful trend feedback..." | Three or four short lines (see below) |

Each chart placeholder is a text box inside an outlined frame rectangle. The charts are drawn from rectangles and text boxes inside the frame, because the Slides connector refuses `createSheetsChart` with "Permission denied" (seen November 16, 2026; plain edits work). Run:

```
python3 -I .claude/skills/baldwin-weekly-trends/scripts/slide_data.py shapes --data <staging>/<date>-slide-data.json > <staging>/<date>-shapes-req.json
```

It prints one batch per chart (`daily`, `types`, `trend`), each starting by deleting that chart's placeholder text box and keeping the frame. Send each batch in its own `update_presentation` call, guarded by `writeControl.requiredRevisionId` from a fresh `read_presentation` with `fields` `["revisionId"]`; one combined batch is too large to send reliably. Then fill the two text boxes in one more guarded call: `deleteText` all, then `insertText`, which keeps the box's own style. Leave the slide titles ("Persisting Topics," "Weekly Volume," "Weekly Request Type Breakdown") as they are.

If a later run finds that `createSheetsChart` works, linked charts from the week's tab are the better choice: try one first, and keep the drawn charts if it is refused.

**The feedback box.** Plain lines, no names, no em dashes, hedged predictions:
- the week's top three macro-trends, one line each, taken from the bold takeaways in `<date>-week-spec.json`;
- one sentiment line from member ratings and Fin signals only (never MLS staff ratings), such as "Members rated 6 chats 4 or 5 and 1 chat 1 or 2; Fin handed 31 chats to a teammate."

If the lines do not fit the box at its current font size, cut words. Slides does not shrink text.

### 5. Check it

Read the copy again with the field mask from the Slides reference, run `slides_helper.py outline`, and fix every overflow or empty placeholder flag. Check that every placeholder text is gone and each chart sits inside its frame. If this Mac has `pdftoppm` (poppler), also export a PDF and look at the pages with the google-workspace skill's `render_export.py`; if not, say in the summary that the layout was checked from geometry only and ask the teammate to look at the deck.

### 6. Record it

On a full run, add `"slides_url"` to the week's entry in `history.json`. If the object IDs in the runbook's "Slides" section are missing or wrong, update them there.

## Finish

End with one short summary:
- the doc link and the deck link,
- the week's conversation count against the week before,
- the top three macro-trends, one line each,
- anything that failed or looked off, including any connector that was missing.

Do not commit or push. A teammate session commits `history.json` and any runbook change later, after checking `git status` for anything under `confidential/`.
