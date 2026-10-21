# QA: View Shared Saved Searches

- Article name: View Shared Saved Searches (title unchanged; kept because Share a Saved Search with a Client and Accept Your Agent's Perchwell Invitation link to it by name)
- Old Notion page: https://app.notion.com/p/2ef8b9e014388066b423e6ba45da2513 (Master Article List, read only)
- Intercom article ID 14743530, content ID 17316361
- Mirror: `docs/help-center/baldwin/view-shared-saved-searches.md`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-14-view-shared-saved-searches-rewrite.md`
- Scored by Claude for Kevin, October 14, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Emoji callout removed; "Switch to the results view by clicking Search" named the wrong control |
| 2 visual_content_text | Pass | Pass | Old article had no images; the rewrite's three placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | Client portal and DOM (days on market) defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Saved Search overview", "Results navigation", "Listing access", "Filter updates" replaced with task headings |
| 6 self_contained_sections | Fail | Pass | "Listing access" never named the saved search |
| 7 audience_specification | Fail | Pass | Article is for invited clients and never said so; opening now does; Roles: Invited Client |
| 8 entity_distribution | Fail | Pass | "Shared saved search" in every heading |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening replaces "In this article, you will learn" |
| 12 instruction_completeness | Fail | Pass | Steps stopped at selecting the search; each block now ends at the outcome |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Up to three sort columns stated |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Client portal" is the settled term, defined on first use. DOM is the on-screen column label and is expanded on first use.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 12.5 | 25.0 | +12.5 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 8.0 | 10.0 | +2.0 |
| Total | 51.5 | 100.0 | +48.5 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed, with no open confirm markers.

Old failures: no opening, and the description in the retired "In this article, you will learn" form; description promised Sort with no section behind it; bare-noun headings; multiple H1s; "update automatically" stated twice; steps with no outcome; no audience stated for a client-only article; bold UI labels including "Saved Searches button"; emoji callout; horizontal rules; the results control named "Search" when the screen reads Results (the April 2026 Arcade shows it as Listings).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where do I find the saved search my agent shared with me? | Yes | Yes |
| How do I see the listings in my saved search? | Partly, wrong control name | Yes |
| How do I see the newest listings first? | No | Yes |
| How do I sort listings by price? | No | Yes |
| Can I change the filters on a search my agent shared? | Partly, one sentence with no steps | Yes |
| If I change the saved search, does my agent see it? | No | Yes |
| How do I open the full listing details? | Partly | Yes |
| Do I need to recreate the search to see new listings? | Yes | Yes |

## Source differences

- Live article and old Notion page match apart from one heading ("Shared Saved Search access" live, "Saved Search access" in Notion), the Notion "In this article" line, and the Notion support footer. Neither covers Sort.
- Both said "Switch to the results view by clicking Search." The Arcade shows Listings; Kevin confirmed the current label is Results, October 14, 2026.
- Confirmed by Kevin, October 14, 2026: clients open shared searches through Saved Searches and My Searches like agents; clients can save their own searches; Open saved search in the email opens the search; clients sort by column header like agents, and DOM sorts newest first; Save shows Update Current and Save New; the icon in Preview opens the full Listing Detail Page.

## Open items

- Resolved October 14, 2026, by Kevin: the square-and-arrow icon in Preview has no hover label, so the draft names it by shape; the DOM column shows in a client's results by default.
- Question for the team, not in the draft: when a client clicks Save New on a shared search, can the agent see the new search? The draft says only that the shared search stays as it was.
- Privacy, replace now: the live Arcade (https://demo.arcade.software/0TAXLJjsebpNZr2VUrYT) shows a contact's full name and personal Gmail address in the Share window, and a saved search named for that person. It is replaced in the draft by a video placeholder; the live Arcade needs removing or re-recording with demo names now, or confirmation that the name and email belong to a demo persona.
- The Arcade also spends half its steps sharing a listing with the agent, which belongs to Share Listings with Your Agent. The replacement video should stop at saving.
- Set consistency: Receive Alerts About New Listings (live, Client Experience) tells clients to "Sort results by Newest First", which is not a control. It should say to sort by the DOM column when it is migrated.
