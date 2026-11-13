# Baldwin weekly trends runbook

A running Google Doc that tracks what Baldwin members are saying, asking, and complaining about in Intercom, with the focus on recurring sentiment and issues that keep coming back. One scheduled Claude task on Kevin's Mac collects the week's data and publishes the report every Friday night.

- **Owner:** Kevin Liang, [kevin.liang@perchwell.com](mailto:kevin.liang@perchwell.com)
- **Doc:** [Baldwin Member Feedback Trends](https://docs.google.com/document/d/1iNA80EIx1pbQelLRf5omcQPnYNaYCGWUb6r_N3jDlwE/edit), ID `1iNA80EIx1pbQelLRf5omcQPnYNaYCGWUb6r_N3jDlwE`
- **Schedule:** Fridays at 10 PM Eastern (the app adds a few minutes). A report week runs from the previous run's cutoff, normally the Friday before at 10 PM, to this Friday at 10 PM, so weekend conversations land in the next report.
- **Scheduled task:** `baldwin-trends-friday-collect`, shown as "Baldwin trends: weekly report (Friday 10 PM)". It runs while the Claude desktop app is open; a run missed while the app was closed starts the next time it opens, and its window simply runs longer.

## The doc

Tabs, left to right:

1. **The newest week,** titled with the first and last day of the window, like `Oct 31 to Nov 6`.
2. **Trends:** rebuilt every run from `history.json`. One table of theme counts per week with a direction column, and one table of sentiment signals per week.
3. **Earlier weeks, newest first.** A tab titled `DRAFT ...` is a hand-made partial week; the next run deletes it.
4. **About:** what the doc is and how it is built. Change it only when the method changes.

## Files here

| File | What it is |
|---|---|
| `baldwin-weekly-trends-runbook.md` | This runbook. The scheduled task reads it on every run. |
| `history.json` | Theme counts, sentiment signals, and the persisting issues list for every finished week. The Trends tab and the week-over-week comparisons come from it. No member names. |
| `collect.py` | Reduces saved Intercom search pages to the Baldwin conversations in a window, flags email campaign replies, drops MLS staff ratings, and lists tracker tickets. |
| `build_tab_requests.py` | Turns a tab spec (headings, paragraphs, bullets, tables, bold, links) into one `update_doc` request list for an empty tab. |
| `doc_outline.py` | Prints a saved `read_doc` result as tab IDs, or one tab as an outline with a character count. |

Staging data for the current week goes in `workstreams/support-ops/confidential/baldwin-weekly-report/`, which is git-ignored, because it holds conversation snippets.

## Rules for every run

- **Intercom is read-only.** Never reply, add notes, tag, assign, or change a conversation or ticket.
- **Write only to the doc above,** to `history.json`, and to the confidential staging folder. Never commit or push.
- **No member names, emails, phone numbers, brokerage names, or addresses** in the doc or in `history.json`. Say "an agent", "an appraiser", "MLS staff". Listing MLS numbers and Jira keys are fine. Link a conversation instead of quoting it.
- **MLS staff ratings do not count.** MLS staff do not give reliable CSAT scores, so sentiment uses member ratings only; `collect.py` already sets `member_rating` to null for MLS staff.
- **Two pages at most for a week tab:** about 4,500 characters of text plus one table of no more than 10 rows. Check with `doc_outline.py`.
- **Writing:** no em dashes, plain words, hedge predictions ("may", "points to"), name Paragon when members do.
- **If something fails** (a connector is missing, a write is rejected twice), stop, leave the doc as it was, and say what failed in the run summary.

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
7. Write the week tab spec (`<staging>/<date>-week-spec.json`) for `build_tab_requests.py`, in this order:
   - `h1` "Week of October 31 to November 6, 2026" (the window's first and last day)
   - `p` "N Baldwin conversations, against M the week before. Theme counts by week are on the Trends tab."
   - `h2` "Macro-trends", then 3 or 4 `p` blocks, each opening with a one-sentence bold takeaway. These are patterns across weeks, not single tickets: which themes keep growing, what members are measuring Perchwell against, where frustration concentrates, whether questions point to help center gaps. The last one is sentiment, from member ratings and Fin signals only.
   - Only when the week had an email campaign: `h2` "Feedback from the <subject> email", a `p` with reply count, how many carried feedback, the tone, and whether the asks match persisting issues, then `bullet` blocks by area with reply counts and a "Follow-up" bullet. Do not list every conversation.
   - `h2` "Persisting issues", a one-line `p`, then a `table` with header `Issue | First seen | Reports | Status`, Jira keys linked to `https://perchwell.atlassian.net/browse/<KEY>`.
   - `h2` "Rising, fading, and new": `bullet` blocks starting with bold "Rising:", "Fading:", "New:".
   - `h2` "Needs attention": up to 4 `bullet` blocks, such as conversations with no teammate answer, repeat issues with no tracker, duplicate trackers. Link conversations as numbered links (1, 2, 3).
   - `p` one line on how the week was counted.
   Conversation links: `https://app.intercom.com/a/inbox/trq7czv5/inbox/conversation/<id>`. Tracker links: `https://app.intercom.com/a/apps/trq7czv5/conversations/<id>`.
8. Update `history.json`: append the week (label, start, end as Unix seconds, conversations, themes, signals, `complete: true`) and replace `persisting`. The next run starts from this `end`.
9. Write the Trends spec (`<staging>/<date>-trends-spec.json`): `h1` "Trends across weeks", a one-line `p`, `h2` "Themes", a `table` with `Theme`, the last 8 weeks oldest to newest, and `Direction`; then `h2` "Sentiment signals" and a `table` of the signals per week. Direction compares the last two weeks: Up when the count rose by 2 or more and at least 25 percent, Down for the same fall, otherwise Steady.
10. Update the doc:
   - `read_doc` the doc (the result is saved to a file) and run `doc_outline.py` on it for the tab IDs.
   - One `update_doc` call: `deleteTab` the `Trends` tab and any tab whose title starts with `DRAFT`, then `addDocumentTab` the week's label at index 0 and "Trends" at index 1, so the newest week is always the first tab (Kevin's choice, November 5). The reply gives the new tab IDs.
   - Put the tab IDs into both specs, run `build_tab_requests.py` on each, `read_doc` again for the `revisionId`, and send both request lists in one `update_doc` call with `writeControl.requiredRevisionId`. On a revision error, read again and resend once.
11. Verify: `read_doc` again, run `doc_outline.py` on the week tab and the Trends tab, and check the headings, the table, the links, and that the week tab is under 4,500 characters of text. Fix anything wrong.
12. Finish with a short summary: the doc link, the week's top three macro-trends in one line each, and anything that failed or looked off.

## Changing the format

The format above was agreed with Kevin on October 29, 2026, after three rounds of feedback: trends and recurring sentiment over issue lists, two pages at most, macro-trends and persisting issues up front, campaign feedback summarized, and MLS staff ratings left out. Edit this file to change it; the task reads it on every run. On October 29 Kevin also moved to a single Friday 10 PM run that collects and publishes, instead of a Friday collection and a Monday report.
