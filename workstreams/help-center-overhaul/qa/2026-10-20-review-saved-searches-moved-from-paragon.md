# QA: Review Saved Searches Moved from Paragon

- **Article:** Review Saved Searches Moved from Paragon
- **Old title:** Your Data: Saved Searches from Paragon
- **Old Notion page:** https://app.notion.com/p/34a8b9e0143880f9ab10eb4f502d0453 (Master Article List, read only)
- **Intercom:** article 14725825, content 17292991, Baldwin help center, collection Then vs. Now
- **Mirror:** `docs/help-center/baldwin/your-data-saved-searches-from-paragon.md` (synced September 4, 2026); live body also read with `get_article` on October 20, 2026
- **New Notion page:** https://app.notion.com/p/3ff8b9e0143881099613ed164d6bcd6d (Draft)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-20-review-saved-searches-moved-from-paragon-rewrite.md`
- **Scored by:** Claude for Kevin, October 20, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old pointed back with "(outlined above)" |
| 2 visual_content_text | Fail | Pass | Old images had no alt text; new placeholders carry it |
| 3 undefined_terms | Pass | Pass | RESO defined in both |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old headings were bare nouns ("Saved Searches", "Filter Translation") |
| 6 self_contained_sections | Fail | Pass | Old opened sections with "However" and pointed back above |
| 7 audience_specification | Pass | Pass | Every member except invited clients; nothing gates it |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old first section mixed both causes, the prefix, renaming, and the pending refresh |
| 10 restate_questions | Pass | Pass | Both tables have an intro sentence |
| 11 overview_jtbd | Fail | Pass | "You will learn how" replaced with "Use this article to" |
| 12 instruction_completeness | Fail | Pass | Old said to review and rename with no steps; new has steps and outcomes |
| 13 limitations_workarounds | Fail | Pass | Old listed untranslatable filters with no route; new gives the Perchwell filter for each |
| 14 numerical_clarity | Fail | Pass | "Approximately 92%" and "multiple reasons" cut on Kevin's approval |

Old: 5 of 14 pass. New: 14 of 14.

## Plain language gate

Pass. No do-not-list terms. Old used "arbitrary filter elimination", "data share", "rectify", "linkages", and "integrity", all cut; the member-facing replacements are "dropped some filters", "linked to the contacts", and "may be missing filters".

## Dimensions

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 8.6 (2/7) | 25.7 (6/7) | +17.1 |
| Chunk independence | 25 | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 6.3 (5/8) | 10.0 (8/8) | +3.7 |
| Accuracy and confidence | 10 | 4.0 (2/5) | 8.0 (4/5) | +4.0 |
| **Total** | 100 | 34.3, Not retrievable as written | 93.7, Fin-ready | +59.4 |

Old failures: title, description, opening, headings, and echo (retrieval); backward references, mixed topics, H1 section headings, the filter-drop explanation stated twice (chunk); no steps, alerts-off not stated, no route for untranslatable filters, "approximately", no links (completeness); bold throughout, no alt text, horizontal rules (formatting); a pending pre-cutover refresh stated as fact, Paragon named, "You will be able to" (accuracy).

New failures, both from naming Paragon: Retrieval signals check 1 and Accuracy and confidence check 4. This is the same pending exception as Find and Update Contacts Moved from Paragon, and here the on-screen prefix itself reads From Paragon. With a generic title and body the score would be 100.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| Why do my saved searches say From Paragon: Unreviewed? | Yes | Yes |
| How do I remove Unreviewed from my saved search name? | Partly (no steps) | Yes |
| Why is my saved search missing filters I set in Paragon? | Yes | Yes |
| Why aren't my clients getting alerts from my Paragon saved searches? | No | Yes |
| Where did Active New Construction go in my saved search? | No (cause only, no route) | Yes |
| Which clients are linked to my saved searches from Paragon? | Yes | Yes |
| I made a saved search in Paragon after my transfer. Why isn't it in Perchwell? | Partly (said to recreate it in Paragon) | Yes |

## Source differences and decisions

- The live article and the old Notion page carry the same text. The old page has no video; its "In this article" line said contacts, a copy error. Its Comments field asked for "a section for how to review your searches", now added.
- Cut as stale, confirmed by Kevin: the Paragon data share fix by May 6, 2026, and the refresh of searches still carrying the prefix. No refresh will run after the August 3, 2026 cutover.
- "Recreated in Paragon" corrected to recreated in Perchwell, confirmed by Kevin.
- Alerts off on migrated saved searches: from the live Your Data: Perchwell Best Practices, confirmed by Kevin. The live Search FAQ says the opposite ("will come over from Paragon with the alerts turned on") in the same answer that tells members to turn alerts on; that FAQ answer needs fixing in its own rewrite.
- The prefix is removed by editing the name, confirmed by Kevin. Steps use the Edit Search window as recorded in `docs/product-context.md`.
- Review guidance (compare Applied Filters with what the search is for) approved by Kevin.
- "Approximately 92%" cut on Kevin's approval. The Gulf Shores example table became one sentence.
- The Perchwell route for each changed filter comes from the live Field & Data Representation Upgrade (14459773), Baldwin.
- "One-time sync at the beginning of each cohort" became "the week before your Perchwell access date", from Your Data: Perchwell Best Practices and matching the contacts sibling.
- Construction Status and Community Amenities are filters on the Filters tab, confirmed by Kevin, October 20, 2026.
- An All Features search is rebuilt by selecting the matching filters in Search, confirmed by Kevin. The draft names Community Amenities and Pool Features as examples, both from Field & Data Representation Upgrade.
- Contact links (Contacts column, Shared Searches tab) confirmed by Kevin; the route to add a missing contact comes from `docs/product-context.md`.

## Open items

- **Title names Paragon.** Same exception as Find and Update Contacts Moved from Paragon, pending Tara. The on-screen prefix [From Paragon: Unreviewed] is an exact label, so the body names Paragon even under a generic title. Fallback: "Review Saved Searches Moved from a Legacy Platform". Kevin had not picked a title when the draft was written; the Paragon title was used to match the sibling.
- Area was removed in Perchwell (Field & Data Representation Upgrade), so a saved search that filtered on Area also needs a new filter. Neither source listed it as a cause; ask whether to add a row.
- **Both live images show contact names** (My Searches window and a contact's Shared Searches tab, captured April 20, 2026). If any are real clients rather than staff or test accounts, replace the images in the live article now. Both images are also outdated: they show a Modified column and a "Search by name" field.
- The live Your Data: Perchwell Best Practices (14725404) links to this article by its old URL.
