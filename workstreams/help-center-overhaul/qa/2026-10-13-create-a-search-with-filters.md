# QA: Create a Search with Filters

- **Article:** Create a Search with Filters
- **Old title:** Create a Search with Filters in Perchwell
- **Old Notion page:** none supplied; migrated from the live article
- **New Notion page:** https://app.notion.com/p/3f98b9e014388102af41ea01de363ecf
- **Intercom article ID:** 13903380, content ID 16154782
- **Mirror path:** `docs/help-center/baldwin/create-a-search-with-filters-in-perchwell.md` (Baldwin only, not shared). The mirror copy is from September 4, 2026 and is missing the Price shortcut tip and Polygon; the stored article from `get_article` was used as the live source
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-create-a-search-with-filters-rewrite.md`
- **Scored by:** Claude, with Tara, October 13, 2026
- **Check set:** September 10, 2026, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Fail | Pass | Live article pointed with emoji (💡, 📍, 📖) |
| 2. visual_content_text | Fail | Pass | Three of five live images had no alt text; every placeholder carries alt text |
| 3. undefined_terms | Fail | Pass | "Filter Filter" is a team name members never see; now the Search filters and values field |
| 4. structured_enumeration | Pass | Pass | |
| 5. query_answer_symmetry | Fail | Pass | "Using the Filter Filter Results:" and "Sort Listings" |
| 6. self_contained_sections | Pass | Pass | |
| 7. audience_specification | Pass | Pass | Every member, including invited clients; body says nothing, per the standard |
| 8. entity_distribution | Pass | Pass | |
| 9. semantic_chunk_boundaries | Fail | Pass | Columns and sorting shared one H1 section |
| 10. restate_questions | Pass | Pass | No tables |
| 11. overview_jtbd | Fail | Pass | No opening paragraph |
| 12. instruction_completeness | Fail | Pass | Steps stopped at the last click |
| 13. limitations_workarounds | Fail | Pass | Three-sort limit was missing; "every filter appears as a column" was false. New: fourth sort drops sort 3; to sort by a field that is not displayed, add it as a column first |
| 14. numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "Filter Filter" removed. Quick Filters is the product-context feature name, not an on-screen label, and is used as the name of the row. The green sort badge is a readout and is described by what it shows.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| **Total** | **39.0, Not retrievable as written** | **100.0, Fin-ready** | **+61.0** |

Old failures: description written as "In this article, you will learn"; no opening; sections at H1 with an H2 `Steps:`; headings that do not echo; sort priority stated twice; no outcomes after steps; links reading "article" and "here", one to a Notion page members cannot open; bold, emoji, horizontal rules, terminal periods in steps; images without alt text; "You can" and "Use"; four claims the product no longer supports (Property Type Edit button, Exact Matches setting minimums and maximums, every filter becoming a column, clearing a sort with the number then the arrow).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I start a new search? | Partly, wrongly says it asks for a name | Yes |
| Why does my new search already have Active and Coming soon checked? | Partly | Yes |
| How do I search for exactly 3 bedrooms? | No | Yes |
| How do I search full and half baths separately? | Partly | Yes |
| Can I type 500k in the price filter? | Yes (stored version only) | Yes |
| I can't find a filter. How do I search for it? | Partly | Yes |
| How do I exclude a city from my search? | Yes | Yes |
| How do I sort by more than one column, and how do I remove a sort? | No, answers wrong | Yes |
| I added a filter but it isn't showing as a column. How do I sort by it? | No, answers wrong | Yes, add it as a column first |

## Sources and decisions

- Tara's screenshots, October 12, 2026: the Search page on Start New, Property Type, Beds (range and Exact match), Baths on Type, Sqft range with the circular arrows icon, the And, Or, Not dropdown on Lot Description, and three-column sort badges.
- Tara confirmed, October 13, 2026: Start New does not ask for a name, only Save does; new searches start with Coming soon and Active unless a Template Search is set; Exact match allows more than one number; Baths opens on Type for a new search and on the saved tab for a saved search; the circular arrows clear both From and To; the x on a Quick Filter button clears the whole filter; k and m work in either case; sort is by clicking anywhere on the column header except the x that clears a column filter, first click ascending, then descending, then off; up to three sorts, the newest becomes 1, a fourth drops sort 3; sort is saved with the search; adding a filter does not add a column; the "came back on the market" tip and the Arcade video are removed.
- Tara kept the proposed title "Create a Search with Filters", kept the Price-then-Bedrooms sort example, and set Roles to All, since invited clients can build searches too (October 13, 2026). The circular arrows icon has no hover label, so it is named by shape. Clicking a selected number in Beds again, or clicking the circular arrows icon, returns Beds or Baths to its default with nothing selected; with Exact match and two numbers selected, clicking one again removes only that number. The live "every filter you add also appears as a column" was read as "every filter can also be a column": adding a filter does not add a column, but Named Waterfront Y/N is available in the Columns menu, so the draft says a field already set as a filter can be added as a column. Tara chose the general wording; only Named Waterfront Y/N was tested (October 14, 2026).
- Scope option A, chosen by default because no pick was given: Property Type, Status & Activity, map tools, and columns each get a sentence and a link; sort stays here because no other Baldwin article covers it.
- Legacy note from the live Key Workflow Changes article: one combined Features field with OR logic became one filter per feature category, with no OR across filters.

## Open items

- Links use live titles and Baldwin paths: Customize Your Search View, Customize Your Search Defaults with Template Searches, and Filter Your Search by Property Types are being retitled in their drafts; Manage Your Saved Searches, Understand Status and Activity Filter, and Customize Your Search View are stored as default help center (`/en/`) links. Update at port.
- Set consistency: settled on "Quick Filters", matching Search Page Overview and `docs/product-context.md`; the Property Type draft was updated in Notion and the repo, October 13, 2026.
- Search Page Overview, Universal Search Bar, and Create a Template Search now link this article as "Create a Search with Filters", in Notion and the repo, October 13, 2026. The URL keeps the old slug until the port.
- CRMLS "Sorting Listings on the Search Page" describes a Sort control and rearrangeable sort fields that do not match the column-header sort in Tara's screenshots. Needs its own review.
- Understand Status and Activity Filter labels (Current Status, Property Status) no longer match the Status & Activity panel. Needs its own rewrite.
- Live images were checked for member names; none found in the sort image. The four other live images are superseded by placeholders.
- Mobile is not covered.
- Fin labels, MLS audience, and publishing stay manual.
