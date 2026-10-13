# QA: Manage Your Saved Searches

- **Article name:** Manage Your Saved Searches (title unchanged)
- **Old Notion page:** https://app.notion.com/p/1c78b9e0143880b2ae2cd8b183a59401 (Master Article List, read only)
- **Intercom article ID:** 8955646, content ID 9098936
- **Mirror paths:** `docs/help-center/baldwin/manage-your-saved-searches.md`, `docs/help-center/crmls/manage-your-saved-searches.md` (shared article)
- **Notion draft:** https://app.notion.com/p/3f78b9e014388149aeb3e080acee2f74
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-12-manage-your-saved-searches-rewrite.md`
- **Scored by:** Claude, October 12, 2026, against current screenshots and Tara's product answers of October 9 to 12, 2026
- **Check set:** revision 2 (September 10, 2026)

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old: 📖 emoji pointer, "In the pop-up" |
| 2 | visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 | undefined_terms | Pass | Pass | |
| 4 | structured_enumeration | Pass | Pass | Old alerts step packed three choices into one step |
| 5 | query_answer_symmetry | Fail | Pass | Old "Open Search Settings", "Enable alerts" |
| 6 | self_contained_sections | Fail | Pass | Old alerts and client-edit steps depended on the Open Search Settings section |
| 7 | audience_specification | Pass | Pass | No role gate |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old used H1 for sections and had an empty H2 |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Old had no opening paragraph; description in "In this article" form |
| 12 | instruction_completeness | Fail | Pass | Old open, delete, and template steps stopped at the click |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. No em dashes, no "you can", "allows you to", or "able to", and no verb "use" outside the "Use this article to" opening. No term from the plain language do-not list. My Searches, Edit Search, Save Search, New Search, Save changes, Delete Saved Search, Update Current, Save New, Open Contacts, and the toggle names are exact on-screen labels. "Copy icon", "pencil icon", "bell icon", and "star icon" are shape names; none of the four has a hover label.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting (10) | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **46.4** | **100.0** | **+53.6** |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed.

Old failures: description over 140 characters in "In this article" form; no opening paragraph; bare-imperative headings; description promises "filter" with no section; alerts steps depend on an earlier section; H1 section headings and an empty H2; steps with no outcome; sharing, alerts, and templates re-explained instead of linked; bold on every UI label; 📖 emoji; horizontal rules; "Search Settings", the sort options, and the alerts Save button no longer match the screen; "How you can use saved searches".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where do I find my saved searches? | Yes | Yes |
| How do I rename a saved search? | No | Yes |
| How do I make a copy of a saved search? | No | Yes |
| How do I delete a saved search? | No (steps name no real control) | Yes |
| How do I sort my saved searches? | No (sort options are stale) | Yes |
| I changed the filters on my saved search. How do I save them? | No | Yes |
| Can I edit the filters in the Edit Search window? | No | Yes |
| What does the Reverse Prospecting toggle on a saved search do? | No | Yes |

## Open items

Reviewed section by section with Tara, October 12, 2026, after the reviewer's pass: the Save changes list was corrected from a test (Discard and Save, with Save opening the Save Search or New Search window and leaving the member on the search), the Start a new search section now covers Start New and its Unsaved Changes window with Open New Tab, client portal is defined on first use, and the Rename, Duplicate, and Delete outcomes were tightened. Final greps clean: no em dashes, no "you can", no verb "use" outside the opening, no bold outside the Description line, no markers. Score holds at 100.0; both gates pass.

Revised October 12, 2026, from a reviewer's first pass: shorter description and opening, Save changes rebuilt around Update Current and Save New, Template Search cut to one link, Edit Search settings shortened, duplicate claim narrowed. The three markers that revision added were resolved by Tara the same day: Contacts sorts by the first name of the first contact added (also the one listed first) with no-contact searches last; Updated lists the most recently changed first; a duplicate keeps filters and contacts but its alerts are off. No markers remain.
- Notifications column: the article says only that it shows who receives a saved search's alerts. Its behavior after the bell icon is still being investigated; do not change that sentence until it is confirmed.

- The Arcade video predates the current screens and may still show Search Settings; the written steps must match the video, so it needs a re-record or a check.
- Bell icon: turning alerts on or off with the bell does not update the Notifications column until the member opens the Edit Search window and clicks Update. Tara is filing it as a bug or feature request; the article does not document it.
- Links to Share a Saved Search with a Client and Create a Template Search point at the live articles they replace (8955682 and 13903342), so the link text carries the new titles. Confirm at port that both retitles landed.
- Shared article: one Notion row with MLS/AOR Baldwin and CRLMS All; cross-links point into the Baldwin help center.
