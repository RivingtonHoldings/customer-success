# QA: Find and Contact Buyer's Agents with Reverse Prospecting

- **Article name:** Find and Contact Buyer's Agents with Reverse Prospecting
- **Old title:** Reverse Prospecting
- **Sources:** live Intercom article 16201667 (content ID 19515818), checked with `get_article` on October 9, 2026 and matching the mirror at `docs/help-center/baldwin/reverse-prospecting.md`; the five live screenshots dated August 4, 2026, read at full resolution; product answers from Kevin, October 9, 2026; the Contacts Page Overview and Set Up Email Alerts for Saved Searches drafts for shared control names. No old Master Article List row exists.
- **Scored by:** Claude, for Kevin, October 9, 2026
- **Scorecard:** revision 2 (September 10, 2026 check set)

## Source differences

The live article's text disagreed with its own screenshots. Kevin confirmed the screenshots on October 9, 2026, so the rewrite follows them.

| Live article text | Screen, confirmed by Kevin |
|---|---|
| Metrics: Matched Searches, Contact Views, Agent Views, Shares, Tag Adds | Saved Searches, Tagged, Shared, Agent Views, Client Views |
| Table columns: Buyer's Agent, Brokerage, Price Range, Property Type, Location | First Name, Last Name, Email, Cell Phone (the buyer's agent's details), Listings in search, Modified, Shared with client, Last Contacted |
| "Click Email", "Customize your message" | Email button at the upper right of the table; an email window with the selected agents, Subject and Message fields, and Send and Cancel. Sends a regular email; Last Contacted updates |
| No limit | Up to 10 saved searches per email |
| Matches are "active" saved searches; on by default for "all clients and unassociated saved searches" | Only saved searches with a contact added are included; the toggle is on by default |
| Opt out: "Open the saved search or client", "Turn off Reverse Prospecting" | My Searches window, pencil icon, Edit Search window, Reverse Prospecting toggle, Update. Per client: the toggle on the contact's Contact Details tab |

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old: emoji callouts |
| 2 | visual_content_text | Fail | Pass | Old: five images with no alt text. New: alt text on all five, plus one placeholder carrying its alt text |
| 3 | undefined_terms | Pass | Pass | |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | Old: "Metrics panel", "Matched-searches table", an empty H2 |
| 6 | self_contained_sections | Fail | Pass | Old: Listings In Search explained under an H4 that began "Perchwell sends your message..." |
| 7 | audience_specification | Pass | Pass | Agents and brokers have access; clients do not. Roles property is All Except Client |
| 8 | entity_distribution | Fail | Pass | Old: metrics and table sections never named Reverse Prospecting |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old: the email outcome and the Listings In Search column shared one block |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Old: no "Use this article to" opening; description was "In this article: you will learn about..." |
| 12 | instruction_completeness | Pass | Pass | |
| 13 | limitations_workarounds | Fail | Pass | Old: the 10-search cap was missing. New: stated in the step, with the route forward |
| 14 | numerical_clarity | Pass | Pass | |

Old: 6 of 14. New: 14 of 14.

## Plain language gate

New: pass. No term from the do-not list. The table's on-screen heading (a readout, not a control) is named once where the member looks for it, and is "the saved searches table" elsewhere. Each section carries the member's verb: open, track, review, email, turn off.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 (1 of 7) | 30.0 (7 of 7) | +25.7 |
| Chunk independence (25) | 8.3 (2 of 6) | 25.0 (6 of 6) | +16.7 |
| Answer completeness (25) | 17.9 (5 of 7) | 25.0 (7 of 7) | +7.1 |
| Fin-parsable formatting (10) | 1.3 (1 of 8) | 10.0 (8 of 8) | +8.7 |
| Accuracy and confidence (10) | 4.0 (2 of 5) | 10.0 (5 of 5) | +6.0 |
| **Total** | **35.8** | **100.0** | **+64.2** |

Old band: Not retrievable as written. Old failures: the title was a bare noun matching the page name; the description and opening used the weak form; the headings were bare nouns, including one empty H2; the opening's list order crossed the sections; there was an H4 and no H1; there was emoji, bold, a horizontal rule, and an em dash; no image had alt text; the metric and column names did not match the screen; there was a "you can"; the 10-search cap was missing; the "contact flow you already use elsewhere" had no link.

New band: Fin-ready. It is held at Draft until the three open `[confirm: ...]` markers are resolved.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I see which agents have buyers looking for my listing? | Partly (open and review are split, and the names are wrong) | Yes |
| How do I email buyer's agents from Reverse Prospecting? | Partly (vague steps) | Yes |
| How many agents can I email at once in reverse prospecting? | No | Yes |
| Why isn't my saved search showing up in reverse prospecting? | No (says active searches only) | Yes |
| What does Listings in search mean? | Yes, from an orphaned H4 | Yes |
| What does Agent Views mean on reverse prospecting? | Yes | Yes |
| How do I stop other agents from seeing my saved search? | Yes (vague steps) | Yes |
| How do I turn off reverse prospecting for a client? | Partly | Yes |

## Open items

- `[confirm: Tagged counts what the live article called Tag Adds]`
- Resolved by Kevin, October 9, 2026: Client Views is the number of times clients viewed the listing; Modified is when the saved search was last changed; the Subject and Message fields come pre-filled with a template, so steps 3 and 4 are now optional edits.
- Not checked against a screenshot: the My Listings table label on the Reverse Prospecting landing page, which comes from the live text only.
- The Loom (August 2026) needs a check against the written steps. It may show what the live article's text described.
- A screenshot is needed of the email window opened from Reverse Prospecting.
- Title: the task-led title was used by default. Revert to "Reverse Prospecting" if the team prefers the page name. Contacts Page Overview links this article by its old title and URL, so update the link text there if the title changes.
- "saved search" capitalization differs across the set: lowercase in Set Up Email Alerts and here, "Saved Searches" in Contacts Page Overview.
- The article lives only in the Baldwin help center. Whether it should also go to CRMLS is a team decision.
