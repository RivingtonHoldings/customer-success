# QA: Filter Your Search by Status and Price Changes

- **Article:** Filter Your Search by Status and Price Changes
- **Old titles:** Search Alerts for Price changes, Status changes, and Open houses (Intercom 16170546, Baldwin); Understand Status and Activity Filter (Intercom 11010696, content 11832103, shared in Baldwin and CRMLS, collection 17797941)
- **Sources:** the live 16170546 body and its eight images, read October 15, 2026 (dated August 1, 2026); the mirror copies of 11010696 (`docs/help-center/baldwin/understand-status-and-activity-filter.md`, `docs/help-center/crmls/understand-status-and-activity-filter.md`); Tara's eight screenshots of the Status & Activity panel, the Rolling window, Date range, and Reporting period tabs, the Reporting period calendar and month picker, and the Edit Search window with Alerts on; Tara's product answers, October 15, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-filter-your-search-by-status-and-price-changes-rewrite.md`
- **Scored by:** Claude, October 15, 2026, scorecard revision 2
- **Original scored:** 16170546, the article Tara linked

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | "Duplicate Search button" and "Filter Finder" are not on-screen labels; "Then select the Now for the status" |
| 2 visual_content_text | Fail | Pass | Eight images, no alt text; placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | "date window", "rolling date window" undefined; Now, Rolling window, Date range, and Reporting period now defined where met |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Price section answered with a workaround the Alerts options replace |
| 6 self_contained_sections | Fail | Pass | Three sections repeat the same duplicate and alerts steps; "Then select" leads |
| 7 audience_specification | Pass | Pass | No role gates the filter; Roles property is All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Each old section mixed filtering, duplicating, and alerts |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Description "This article will guide you"; no opening; promised "A more streamlined approach is coming!" |
| 12 instruction_completeness | Fail | Pass | No step said what the member gets |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Fail | Pass | "appropriate date range" now 30 and 180 day defaults and exact button values |

Old: 5 of 14. New: 14 of 14.

## Plain language gate

New: pass. No do-not-list terms. Temp off mkt stays as the on-screen label. "Now" and the tab names appear where the member clicks them.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30, 7 checks) | 12.9 (3/7: no opening; headings do not name the filter; leads do not echo) | 30.0 (7/7) | +17.1 |
| Chunk independence (25, 6 checks) | 12.5 (3/6: repeated duplicate and alert steps; "Then" leads; open house mixed in) | 25.0 (6/6) | +12.5 |
| Answer completeness (25, 7 checks) | 7.1 (2/7: no defaults, no window tabs, no outcomes, outdated workaround) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10, 8 checks) | 3.8 (3/8: bold throughout, emoji callout, horizontal rules, no Steps blocks) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence (10, 5 checks) | 4.0 (2/5: names Paragon; "Easily"; outdated Notifications window) | 10.0 (5/5) | +6.0 |
| **Total** | **40.3, Needs rewrite** | **100.0, Fin-ready** | **+59.7** |

New: Fin-ready band, gate passed, plain language passed. No `[confirm: ...]` markers remain.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I find listings that were pending in the last 30 days? | No | Yes |
| How do I find listings with a price drop? | Partly, buried in an alerts workaround | Yes |
| What does Now mean next to Active? | No | Yes |
| Why does my Pending search show closed listings? | No | Yes |
| What is the difference between a rolling window and a date range? | No | Yes |
| How do I find year-to-date closed sales? | No | Yes |
| How do I get alerts when a listing's price changes? | Yes, outdated method | Yes, links Set Up Email Alerts |

## Sources and decisions

- Scope A chosen by Tara, October 15, 2026: a filter article that replaces both 11010696 and 16170546. Alerts get one section and a link, since Set Up Email Alerts for Saved Searches owns the Status, Open House, and Price alert options.
- Tara confirmed, October 15, 2026: Coming soon, Active, Active under contract, and Pending show Now when selected; the other six statuses start at 180 days (later refined: a window finds listings in that status at some point during it; see Open items); the Reporting period day buttons set the start date that many days before today; after Submit on Date range or Reporting period, the button shows the dates.
- From the screens: Price increase and Price drop show 30 days when selected; Rolling window Window end defaults to 0 for today; Date range has 30, 60, and 180 days; Rolling window and Reporting period have 30, 60, 180, and 365 days; the Reporting period month name opens a month picker with a year dropdown.
- The old duplicate-a-search workaround is dropped: the Edit Search window now has Status, Open House, and Price under the Alerts toggle, which the old article's "A more streamlined approach is coming!" anticipated.
- Legacy name kept, genericized: the old description said members may know these as drip campaigns in Paragon.
- The 16170546 videos (three Looms) teach the duplicate workaround and are not carried. The 11010696 Arcade (https://demo.arcade.software/0yyPSAepaeTxyH9XBgxH) shows the retired Any Date control; the draft carries a video placeholder.

## Open items

- Resolved October 15, 2026, by Tara: Now matches only the listing's status today; a date window on any status finds listings that were in that status at some point during the window, so results can include listings whose status today is different. This replaced the earlier "changed to Closed in 30 days" wording and removed the confirm marker. Rolling window day buttons set Window start; Date range day buttons select a range ending today; the circular arrows icon clears the selected dates, and after a day button it returns Window start to the default of 30; a status plus a price change finds only listings that match both.
- Replace now: a live 16170546 image shows a saved search named after a person, which may be a client name, plus teammate test names (alerts screenshot, Screenshot 2026-08-01 at 12:19:46 PM). The image is already published.
- The live 16170546 copy icon shows a "Duplicate search" hover label (August 1, 2026); `docs/product-context.md` says it has no hover label (October). Not needed by this draft; check for Manage Your Saved Searches.
- 16170546 has no collection and is missing from the mirror, and has no row in either Notion database. At port, redirect it and 11010696 to this article, or retire them.
- Two Baldwin Getting Started Guide articles teach the same workaround with the same Looms: Set-up Automatic Emails and Search Alerts (16392739) and Set up Search Alert for a Status Change (16392773). Both promise "A more streamlined approach is coming soon!" They need a decision: point them to Set Up Email Alerts for Saved Searches, or retire them.
- Shared article: 11010696 sits in both help centers, so the row takes both MLS/AOR values.
- Links: Set Up Email Alerts for Saved Searches is linked by its Baldwin path; switch at port if its ID changes.
- Verify: whether Closed, Leased, Expired, Canceled, Temp off mkt, and Withdrawn always return to 180 days when selected again, or keep a window set earlier. The draft says "default to 180 days when selected" (reviewer note, October 15, 2026).
- Cut in review, October 15, 2026: the Rolling window reset sentence ("To return Window start to 30, click the circular arrows icon"). Tara said the icon returns a day-button window to the default of 30, but statuses that start at 180 days were not tested. Restore only once the reset is confirmed per status and price change.
- Tara confirmed, October 15, 2026: Closed, Leased, Expired, Canceled, Temp off mkt, and Withdrawn cannot be set to Now; only Coming soon, Active, Active under contract, and Pending filter by current status. The draft now says so in both status sections.
- Notion draft: https://app.notion.com/p/3fa8b9e0143881d38844c5b289f384c8. Tracker ID TRK-087, set October 15, 2026.
- Fin labels, MLS audience, and publishing stay manual.
