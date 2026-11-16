# Baldwin weekly trends runbook

A running Notion page that tracks what Baldwin members are saying, asking, and complaining about in Intercom, with the focus on recurring sentiment and issues that keep coming back. One scheduled Claude task on Kevin's Mac collects the week's data and publishes the report every Friday night.

- **Owner:** Kevin Liang, [kevin.liang@perchwell.com](mailto:kevin.liang@perchwell.com)
- **Notion page:** [Baldwin Weekly Trends and Perchie Review Loop](https://app.notion.com/p/41a8b9e01438802a8037c6028b515ad9), ID `41a8b9e01438802a8037c6028b515ad9`, in the Customer Success Team Space. Also stored as `notion_page_id` in `history.json`.
- **Retired Google Doc:** [Baldwin Member Feedback Trends](https://docs.google.com/document/d/1iNA80EIx1pbQelLRf5omcQPnYNaYCGWUb6r_N3jDlwE/edit). Every tab was moved to Notion on November 16, 2026 (Kevin's call); runs no longer write to it.
- **Schedule:** Fridays at 10 PM Eastern (the app adds a few minutes). A report week runs from the previous run's cutoff, normally the Friday before at 10 PM, to this Friday at 10 PM, so weekend conversations land in the next report.
- **Scheduled task:** `baldwin-trends-friday-collect`, shown as "Baldwin trends: weekly Notion page and slides (Friday 10 PM)". It runs while the Claude desktop app is open; a run missed while the app was closed starts the next time it opens, and its window simply runs longer.

## The Notion page

The main page holds, top to bottom:

1. **An intro** saying what the report is.
2. **Weekly reports:** one child page per week, newest first, titled like `Week of November 9 to 16, 2026`. Each week's page link is stored as `notion_url` in `history.json`.
3. **Trends across weeks:** rebuilt every run from `history.json`. One table of theme counts per week with a direction column, and one table of sentiment signals per week.
4. **How it is built** and **Where the instructions live.** The text is in `notion_page.py`; change it there only when the method changes.

The whole main page is rewritten every run from `notion_page.py main`, so edits made by hand on the main page are lost; comments and edits on a week's page are kept. The Oct 19 to 25 week has no page because it was never a tab in the doc; its counts still show in the Trends tables.

## Files here

| File | What it is |
|---|---|
| `baldwin-weekly-trends-runbook.md` | This runbook. The scheduled task reads it on every run. |
| `history.json` | Theme counts, sentiment signals, and the persisting issues list for every finished week, plus each week's `notion_url` and `slides_url`. Trends across weeks and the week-over-week comparisons come from it. No member names. |
| `collect.py` | Reduces saved Intercom search pages to the Baldwin conversations in a window, flags email campaign replies, drops MLS staff ratings, and lists tracker tickets. |
| `notion_page.py` | Turns the week spec into the week page's title and Markdown (`week`), and builds the whole main page from `history.json` and the Trends spec (`main`). Its docstring holds the spec format. |

Staging data for the current week goes in `workstreams/support-ops/confidential/baldwin-weekly-report/`, which is git-ignored, because it holds conversation snippets.

## Rules for every run

- **Intercom is read-only.** Never reply, add notes, tag, assign, or change a conversation or ticket.
- **Write only to the Notion page above and its week pages,** the chart data spreadsheet and the week's new deck (see "Slides"), `history.json`, and the confidential staging folder. Never edit the slides template itself. Never commit or push.
- **No member names, emails, phone numbers, brokerage names, or addresses** in Notion or in `history.json`. Say "an agent", "an appraiser", "MLS staff". Listing MLS numbers and Jira keys are fine. Link a conversation instead of quoting it.
- **MLS staff ratings do not count.** MLS staff do not give reliable CSAT scores, so sentiment uses member ratings only; `collect.py` already sets `member_rating` to null for MLS staff.
- **Short week pages:** about 4,500 characters of text plus one table of no more than 10 rows. Check the length of the `content` that `notion_page.py week` prints.
- **Writing:** no em dashes, plain words, hedge predictions ("may", "points to"), name Paragon when members do.
- **If something fails** (a connector is missing, a write is rejected twice), stop, leave the Notion pages as they were, and say what failed in the run summary.

## Themes

Every non-test conversation goes into exactly one theme. Use these names so the Trends table lines up week to week. Add a new theme only when 3 or more conversations in a week fit none of these, and add it to `history.json` with 0 for earlier weeks.

| Theme | Covers |
|---|---|
| Printing and reports | Printing, one page and full reports, CMAs, PDFs, CSV export, font size, report layout |
| Listing status changes | Expire, reactivate, relist, close, cancel, suspended, Awaiting Activation, editing closed or expired listings |
| Finding listings and search | Search filters, sorting, address or MLS number lookup, saved searches, search history |
| Contacts and client sharing | Contacts, client invitations, sharing links, alerts to clients, emailing agents |
| Agent phone numbers | An agent's number showing wrong, as a landline, or not saving |
| Missing subdivisions and areas | Requests to add subdivisions, cities, counties to lookups |
| Listing entry and duplicating | Entering or editing a listing in Add/Edit, required fields, drafts that will not save, open house entry, duplicating or cloning a listing (added Nov 9, 2026) |
| Listing documents and photos | Documents, photos, media in a listing |
| Listing data accuracy (CDOM, HOA) | Wrong values on a listing: DOM, CDOM, HOA, room data |
| Seller activity report | Listing activity or performance reports for sellers |
| Login and account access | Logging in, accounts, permissions |
| Social sharing and syndication | Facebook, Zillow, virtual tours, open houses on other sites |
| Other | Anything else; never a headline theme |

## Weekly run

1. Work out the window: `start` = the `end` of the last week in `history.json` (Unix seconds), `end` = now. `label` = the first and last calendar day of the window in Eastern time, like `Oct 31 to Nov 6`. The staging date is today's date. Use Python's `zoneinfo` (`America/New_York`) for any conversion.
2. Search Intercom twice with `search_conversations`, `per_page` 150, following `pages.next.starting_after` until it is gone:
   - `created_at` `>` start minus 1 (the week's new conversations)
   - `updated_at` `>` start minus 1 (to pick up tracker tickets linked this week)
   Each page is large and is saved to a file by the app; keep every saved path. If a page comes back inline, write it to a file in the staging folder.
3. Run `collect.py --start START --end END --out <staging>/<date>-collected.json` on all the page files.
4. Classify every conversation in the output that is not `Internal / Test / Spam`. For each, decide:
   - `theme` (from the table above), `kind` (question, bug, request, feedback, admin), `sentiment` (positive, neutral, negative), `paragon` (true when the member names Paragon or the old system),
   - and a one-sentence `summary` with no names.
   The title and snippet are enough for most how-to questions. Read the full conversation with `get_conversation` for bugs, feature requests, campaign replies, untagged conversations a teammate answered, Fin thumbs-down, and anything whose title is vague. For more than 12 reads, hand them to subagents in batches of about 12, each told to return JSON only and no member names.
5. Save the classifications to `<staging>/<date>-classified.json`, keyed by conversation ID. If a run stops partway, the next attempt can reuse this file instead of classifying again.
6. Compute for the week:
   - theme counts and the signals: Fin handed to a teammate (`fin_state` escalated), Fin thumbs down (`negative_feedback`), member ratings of 1 or 2, member ratings of 4 or 5;
   - campaigns from `collect.py` (`campaigns`), with replies grouped by area;
   - profile edits and invited contact edits, counted as two separate persisting issues because they are different problems (Kevin, November 9). Profile edits: an agent tried to change their own profile (name, email, phone, photo, office) and the change reverted, would not save, or was locked. Invited contact edits: an agent tried to change an invited contact's name, email, or phone and it reverted or was locked. Add each count to its own persisting issue and name the week's counts in a macro-trend when either is 2 or more. Conversations 215476664724468 and 215476664874074 (contact) and 215476666264527 (profile) are already counted.
   - persisting issues: start from `history.json` `persisting`, add this week's reports to matching issues, add any issue seen in two or more weeks or on a tracker ticket with 2 or more reports, and drop issues with no reports for 4 weeks or a resolved tracker. Keep the 10 with the most reports.
7. Write the week spec (`<staging>/<date>-week-spec.json`) for `notion_page.py`, in this order:
   - `h1` "Week of October 31 to November 6, 2026" (the window's first and last day; it becomes the page title)
   - `p` "N Baldwin conversations, against M the week before. Theme counts by week are in Trends across weeks on the main page."
   - `h2` "Macro-trends", then 3 or 4 `p` blocks, each opening with a one-sentence bold takeaway. These are patterns across weeks, not single tickets: which themes keep growing, what members are measuring Perchwell against, where frustration concentrates, whether questions point to help center gaps. The last one is sentiment, from member ratings and Fin signals only.
   - Only when the week had an email campaign: `h2` "Feedback from the <subject> email", a `p` with reply count, how many carried feedback, the tone, and whether the asks match persisting issues, then `bullet` blocks by area with reply counts and a "Follow-up" bullet. Do not list every conversation.
   - `h2` "Persisting issues", a one-line `p`, then a `table` with header `Issue | First seen | Reports | Status`, Jira keys linked to `https://perchwell.atlassian.net/browse/<KEY>`.
   - `h2` "Rising, fading, and new": `bullet` blocks starting with bold "Rising:", "Fading:", "New:".
   - `h2` "Needs attention": up to 4 `bullet` blocks, such as conversations with no teammate answer, repeat issues with no tracker, duplicate trackers. Link conversations as numbered links (1, 2, 3).
   - `p` one line on how the week was counted.
   Conversation links: `https://app.intercom.com/a/inbox/trq7czv5/inbox/conversation/<id>`. Tracker links: `https://app.intercom.com/a/apps/trq7czv5/conversations/<id>`.
8. Update `history.json`: append the week (label, start, end as Unix seconds, conversations, themes, signals, `complete: true`) and replace `persisting`. The next run starts from this `end`.
9. Write the Trends spec (`<staging>/<date>-trends-spec.json`): `h1` "Trends across weeks", a one-line `p`, `h2` "Themes", a `table` with `Theme`, the last 8 weeks oldest to newest, and `Direction`; then `h2` "Sentiment signals" and a `table` of the signals per week. Direction compares the last two weeks: Up when the count rose by 2 or more and at least 25 percent, Down for the same fall, otherwise Steady.
10. Update Notion (tools `notion-fetch`, `notion-create-pages`, `notion-update-page`):
   - Run `notion_page.py week <staging>/<date>-week-spec.json`. It prints the page `title` and `content`.
   - If the week in `history.json` has no `notion_url`, create the page with `notion-create-pages`, parent `page_id` = `notion_page_id` from `history.json`, icon 🗓️, `allow_async` false. Save the returned URL, in the form `https://app.notion.com/p/<id without dashes>`, as the week's `notion_url` in `history.json`. On a rerun for a week that already has a page, `replace_content` that page instead of making a second one.
   - Run `notion_page.py main --history workstreams/support-ops/baldwin-weekly-report/history.json --trends-spec <staging>/<date>-trends-spec.json` and send its output with `notion-update-page` `replace_content` on the main page. The `<page>` tags it writes keep every week page and put the newest first (Kevin's choice, November 5). If the tool says child pages would be deleted, stop and say which; never retry with `allow_deleting_content`.
11. Verify: `notion-fetch` the main page and the week page. Check the headings, the tables, the links, that each macro-trend is its own paragraph (single newlines turn into line breaks inside one block; `notion_page.py` puts blank lines between blocks), and that every week page is still listed. Fix anything wrong with `update_content`.
12. Finish with a short summary: the Notion page link, the week's top three macro-trends in one line each, and anything that failed or looked off.

## Slides

After step 11, the same run makes a new Google Slides deck for the week, following `.claude/skills/baldwin-weekly-trends/SKILL.md` (also `/baldwin-weekly-trends`). Agreed with Kevin on November 13, 2026: the whole template file is the template, every week gets its own copy, and Kevin reviews the deck before sharing it.

- **Template:** [Kevin- support trend slides Template](https://docs.google.com/presentation/d/1-fJ_FQe9TwnbWLQKxiC82SopBj3J9nv9lm8KTcFFyos/edit), ID `1-fJ_FQe9TwnbWLQKxiC82SopBj3J9nv9lm8KTcFFyos`, Drive folder `0AH14cZfpOD3iUk9PVA`. Never edited by a run.
- **Weekly decks:** copies in the same folder, titled `Baldwin support trends, <label>, <year>`. Each week's link is stored as `slides_url` in `history.json`.
- **Chart data spreadsheet:** [Baldwin support trends chart data](https://docs.google.com/spreadsheets/d/1Ovxs2i6pdsakgllE4ruhq_50E3B9m7dUYnqmVpLX-U8/edit), ID `1Ovxs2i6pdsakgllE4ruhq_50E3B9m7dUYnqmVpLX-U8`, created November 16, 2026. One tab per week, named with the week label, holding the numbers behind that week's charts.
- **Charts are drawn in the deck, not linked.** On November 16, 2026 the Google Slides connector refused `createSheetsChart` ("Permission denied") even as a still image, while plain edits worked. So `slide_data.py shapes` draws each chart from bars and labels inside its frame: conversations per day as columns, request types as bars, and this week's top five themes as paired bars against the week before.
- **Placeholder object IDs in the template** (read November 13, 2026; a copy keeps the same IDs). Page is 10 x 5.625 in.

| Slide | Header box | Placeholder text box | Frame rectangle | Fill with |
|---|---|---|---|---|
| 1 (`h5fd9f7b563dd3a42_0_461`), left | "Weekly Volume" `h418bda9a80e95acc_0_6` | `h418bda9a80e95acc_0_0` "Image of New Conversations..." | none | Number box: new conversations against the week before |
| 1, left | | `h418bda9a80e95acc_0_1` "Graph of Conversations per Day..." | `h418bda9a80e95acc_0_3` | Conversations per day chart |
| 1, right | "Persisting Topics" `h5fd9f7b563dd3a42_0_477` | `h418bda9a80e95acc_0_4` "Graph of Persisting Trends..." | `h418bda9a80e95acc_0_5` | Theme trend chart |
| 2 (`h5fd9f7b563dd3a42_0_229`), left | "Weekly Request Type Breakdown" `h418bda9a80e95acc_0_7` | `h418bda9a80e95acc_0_9` "Graph from Intercom Dashboard..." | `h418bda9a80e95acc_0_8` | Request types chart |
| 2, right | | `h418bda9a80e95acc_0_10` "Any additional/helpful trend feedback..." | `h418bda9a80e95acc_0_11` | Feedback lines; keep the frame |

A chart takes its frame rectangle's position and size, and replaces both the frame and the text box. The thin lines `h5fd9f7b563dd3a42_0_476` and `h5fd9f7b563dd3a42_0_467` divide each slide's two columns; leave them.
- **Needs the Google Slides connector.** Without it the Notion half still runs and the summary says the slides were skipped.

## Changing the format

The format above was agreed with Kevin on October 29, 2026, after three rounds of feedback: trends and recurring sentiment over issue lists, two pages at most, macro-trends and persisting issues up front, campaign feedback summarized, and MLS staff ratings left out. Edit this file to change it; the task reads it on every run. On October 29 Kevin also moved to a single Friday 10 PM run that collects and publishes, instead of a Friday collection and a Monday report.
