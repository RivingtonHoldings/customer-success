# QA: Filter Your Search by Open House Date

- **Article:** Filter Your Search by Open House Date
- **Old title:** Search for Open Houses
- **Sources:** Intercom 11517245, content 12507731, shared in both help centers (`docs/help-center/baldwin/search-for-open-houses.md`, collection 17797942; `docs/help-center/crmls/search-for-open-houses.md`, collection 16866944); old Master Article List row https://app.notion.com/p/2088b9e014388025ac99ee6787a5cc57; Tara's screenshots of the Open house filter on the Filters tab and the Open house column filter, and her product answers, October 14, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-14-filter-your-search-by-open-house-date-rewrite.md`
- **Scored by:** Claude, October 14, 2026, scorecard revision 2
- **Original scored:** the live article (same body in both help centers)

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | "the column drop down" and "Click on the filter" named no control |
| 2 visual_content_text | Pass | Pass | Live article has no images; placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | Removal options now a labeled list |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the filter; Roles property is All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Tips mixed Tag promotion into a search article |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old description "In this article, you will learn"; no jobs opening |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with the result |
| 13 limitations_workarounds | Fail | Pass | Day-button behavior stated (written as fixed, today forward; see open items) |
| 14 numerical_clarity | Pass | Pass | |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

New: pass. No do-not-list terms. "open house" leads every heading; Select date range, Search filters and values, and Applied Filters appear only where the member has to find the control.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30, 7 checks) | 17.1 (4/7: no "Use this article to" opening; bare "Tips" heading; Tips lead does not echo) | 30.0 (7/7) | +12.9 |
| Chunk independence (25, 6 checks) | 16.7 (4/6: H1s inside the body; Tips mixes topics) | 25.0 (6/6) | +8.3 |
| Answer completeness (25, 7 checks) | 10.7 (3/7: no outcomes; day-button and no-Submit behavior unstated; past-date constraint unstated; add-a-column steps re-explained instead of linked) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10, 8 checks) | 3.8 (3/8: bold in steps and throughout, emoji callout with no label, horizontal rules) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence (10, 5 checks) | 8.0 (4/5: "Navigate", "type", "Use the date range") | 10.0 (5/5) | +2.0 |
| **Total** | **56.3, Needs rewrite** | **100.0, Fin-ready** | **+43.7** |

New: Fin-ready score; gate passed; plain language passed. No `[confirm: ...]` markers remain. Rescored after the review round of October 14, 2026 (description, opening, Filters tab steps, day-button section, column lead and outcome, removal section); the edits changed no check result. The day-button section describes the fix, not current behavior, so Accuracy check 1 holds only once the fix ships.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I find open houses this weekend? | Partly, no calendar instructions | Yes |
| How do I search for open houses on one day? | No | Yes |
| Where is the open house filter? | Partly, "filter search bar" is not the on-screen label | Yes |
| How do I find open houses in the next 30 days? | No | Yes, once the day-button fix ships |
| Can I see open house times in my search results? | No | Yes |
| Can I filter open houses from the results columns? | Yes | Yes |
| How do I remove the open house filter? | No | Yes |

## Open items

- Resolved October 14, 2026: in the Open house column, one click on a date updates the results right away. The confirm marker was removed.
- Notion draft: https://app.notion.com/p/3f98b9e0143881918ce0c6728621e7b0. Tracker ID not yet set; look it up under "Search for Open Houses" in the master sheet.
- Saved searches: whether a search saved with 30 days rolls forward daily or keeps fixed dates. Tara is confirming with the team, October 14, 2026. Left out of the draft until answered; it affects alerts.
- Product question: the 30, 60, 180, and 365 days buttons select a range ending today (30 days set 9/14/2026 to 10/14/2026 on October 14), and open houses before today do not appear. The buttons therefore find no upcoming open houses. Tara flagged this as a likely bug and is confirming with the team, October 14, 2026. At her direction the section is now written as if fixed (today forward), with no marker in the draft, also at her direction. Do not port until the fix is live; if it does not ship, restore the current-behavior version.
- Shared article: the same Intercom article sits in a Baldwin collection and a CRMLS collection. The row takes both MLS/AOR values.
- Video: the old row's Arcade (https://app.arcade.software/share/274RA2GqevHsXDQFvOyX) is marked Update Required and the live article does not embed it; the draft carries a video placeholder.
- Set: the Search FAQ draft answers "How do I search for listings with an open house?" in two sentences. Once this article is ported, that answer should link here.
- Dropped from the live Tips: combining with other filters (owned by Create a Search with Filters) and promoting open houses with a Tag link (a Tags job). Tara agreed, October 14, 2026.
- No legacy-platform name for the Open house filter appears in the mirror's terminology files, so the draft has no legacy sentence.
- The Customize Your Search View link points at the Baldwin help center; switch to Customize Your Search Results View once that draft is ported.
