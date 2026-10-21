# QA: Review Your Data Moved from Paragon

- **Article:** Review Your Data Moved from Paragon
- **Old title:** Your Data: Perchwell Best Practices
- **Sources:** Intercom article 14725404, content ID 17292415; mirror `docs/help-center/baldwin/your-data-perchwell-best-practices.md` (synced September 4, 2026); live body also read with `get_article` on October 20, 2026. No old Notion page; the live article was the only source. Product facts confirmed by Kevin, October 20, 2026.
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-20-review-your-data-moved-from-paragon-rewrite.md`
- **New Notion page:** https://app.notion.com/p/3ff8b9e014388183b0abf485f15577e1 (Draft)
- **Scored by:** Claude for Kevin, October 20, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | "Mixed; see below" in the table removed |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholder carries alt text |
| 3 undefined_terms | Fail | Pass | Cohort, Parallel, Live-Synced, and Partials were undefined; cohort and parallel cut, draft listing and system of record defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "1. Get Started Immediately" replaced with task headings |
| 6 self_contained_sections | Fail | Pass | Each section names Paragon and its subject |
| 7 audience_specification | Pass | Pass | No role gates the workflow |
| 8 entity_distribution | Fail | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Two H1s and mixed blocks split into H2 sections |
| 10 restate_questions | Pass | Pass | Table replaced by a labeled list with a lead sentence |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Fail | Pass | "Remove the prefix" now has steps and an outcome |
| 13 limitations_workarounds | Fail | Pass | Items that did not move are named, with a route where one exists |
| 14 numerical_clarity | Fail | Pass | "High" and "Mixed" completeness replaced with "where the data allowed" (Kevin's wording) |

Old: 4 of 14. New: 14 of 14.

## Plain language gate

Pass. "System of record" is a glossary term and carries a "That means" clause. "Partials" appears once in the description as the legacy name members search with.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 25.7 (6/7) | +17.1 |
| Chunk independence (25) | 4.2 (1/6) | 25.0 (6/6) | +20.8 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 6.3 (5/8) | 10.0 (8/8) | +3.7 |
| Accuracy and confidence (10) | 6.0 (3/5) | 8.0 (4/5) | +2.0 |
| **Total** | 32.2, Not retrievable as written | 93.7, Fin-ready | +61.5 |

The new draft's two failed checks both come from naming Paragon: Retrieval signals check 1 (the title names a legacy platform) and Accuracy and confidence check 4. This matches the pending exception on Find and Update Contacts Moved from Paragon. With a generic title and body the score would be 100.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Did my saved searches come over from Paragon? | Yes (table) | Yes |
| Why am I not getting alerts for my saved searches? | Partly (a heading only) | Yes |
| What does From Paragon: Unreviewed mean? | Partly | Yes |
| How do I remove From Paragon: Unreviewed from my saved search? | No | Yes |
| Did my contacts' notes and reactions transfer? | Yes (table) | Yes |
| Where are my partials from Paragon? | Partly (table row only) | Yes |
| Did my Listing Carts or Market Monitor move to Perchwell? | No | Yes |
| Why can't I share a listing with a contact from Paragon? | No | Yes (with link) |

## Open items

- **Scope and title chosen by default.** Kevin answered the product questions but not scope or title; the draft uses the recommended hub scope (option A) and "Review Your Data Moved from Paragon". The cohort timing and "Get Started Immediately" section were cut as no longer relevant after the August 3, 2026 switch.
- **Title and body name Paragon.** Same pending exception as Find and Update Contacts Moved from Paragon, awaiting Tara. Fallback: "Review Your Data Moved from a Legacy Platform", with the body genericized.
- **Live facts corrected by Kevin.** The live table's partial cutoff of 1/1/2023 is wrong; every partial created before July 20, 2026 moved. Alerts on moved saved searches are off. The Search FAQ and Client Collaboration FAQ in the mirror say saved searches "come over with the alerts turned on"; both need correcting when next touched.
- **Bare deficits kept.** Shared listing history and contacts' notes and reactions have no route forward. Kept because the live article listed them and members may ask Fin.
- **Screenshot needed:** the My Searches window with test saved searches carrying the prefix.
- **Privacy, replace now:** the published My Searches screenshot in Your Data: Saved Searches from Paragon (14725825) shows what appear to be real contact names in the Contacts column.
- **Links to flag at transfer:** Find and Update Contacts Moved from Paragon and Find Your Partial Listings in Perchwell are Notion drafts; replace with Intercom URLs at transfer. How to Create a Tag may be retitled Create and Edit a Tag by its rewrite. Your Data: Saved Searches from Paragon still has stale pre-switch content (the May 6 refresh, recreating searches in Paragon) and has no rewrite yet.
- **Unverified step:** step 2 of the review steps assumes clicking a saved search's name in the My Searches window opens it; confirm on screen.
