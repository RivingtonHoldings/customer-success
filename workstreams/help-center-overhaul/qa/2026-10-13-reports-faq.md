# QA: Reports FAQ

- Article name: Reports FAQ (title unchanged)
- Old Notion page: https://app.notion.com/p/3658b9e014388064ab11cc67b5988819
- Intercom article ID 15201097, content ID 17971160
- Mirror: `docs/help-center/baldwin/reports-faq.md`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-reports-faq-rewrite.md`
- Scored by Claude for Kevin, October 13, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Fail | Pass | CMA, DOM, and PDF now defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the content |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Two near-duplicate layout questions merged |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Vague field-selection directions replaced; Steps blocks end at the outcome |
| 13 limitations_workarounds | Fail | Pass | Layout limit and collapsed-section limit stated as the route forward; roadmap promise dropped |
| 14 numerical_clarity | Fail | Pass | Landscape 12 fields and Portrait 9, confirmed by Kevin October 13, 2026 |

## Plain language gate

Pass on the rewrite. No do-not-list terms; "dialog" and "PDF" are the words a member uses.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 12.5 | 25.0 | +12.5 |
| Answer completeness (25) | 7.1 | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 8.8 | 10.0 | +1.2 |
| Accuracy and confidence (10) | 4.0 | 10.0 | +6.0 |
| Total | 49.5 | 100.0 | +50.5 |

Old: Not retrievable as written. New: Fin-ready, 14 of 14 golden questions, plain language gate passed.

Old failures: description under 120 characters, no opening, no heading echo under Include exact address, every question an H1, layout fact stated twice, bold headings and bold "full report", no links, "some" fields and layouts, "You can" three times, an exact-address claim the Quick CMA articles contradict, and a 14-field list that no longer matches the product.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Can I change the layout of my CMA? | Partly, two sections with no detail | Yes |
| How many fields can I put on a Quick CMA? | No | Yes |
| Why aren't the addresses in my CMA clickable? | Partly, and contradicted by the Quick CMA article | Yes |
| Can I do a CMA for rentals? | Yes | Yes |
| How do I remove the showing instructions section before I print a listing for a client? | Partly | Yes |
| How do I email a report to my client? | No | Yes |
| Where do I find a CMA I sent last week? | No | Yes |
| Do my clients need to log in to open the listings in my CMA? | No | Yes |

## Open items

- Landscape allows 12 fields per listing and Portrait 9, confirmed by Kevin October 13, 2026. The live Create a Quick CMA Report article says 10 for Landscape and is wrong; the Create a Quick CMA Report draft still carries a `[confirm: ...]` on the Landscape cap and should be updated to 12.
- Common Perchwell FAQs (live) repeats the collapsed-sections answer, "will not appear in the full report shared with clients." It is now confirmed to be both versions and Listing Detail Page only; flag for that article's rewrite.
- Create a Full Report link points at the default help center URL of the live Create and Share Full Reports article; flag at transfer.
- Visuals: none in the live article. The old row flagged New Screenshots, so one screenshot placeholder was added under Include exact address (link and Additional Options settings), and Media Update Needed and Visuals Included set to Yes so the row appears on the Help Center Production Tracker. Tracker ID and Visual Owner left for the tracker owner.
- October 19, 2026: the layout answer was expanded from the Quick CMA and Full Report to all eight report types, per the reviewer's inline comment, using the Notion drafts of each report article as the source. Every new claim traces to one of those drafts; none adds a number they do not state. Rescore not needed: the section keeps its heading, echo, and labeled-list shape, and its eight links now form a "For more information:" list.
- All "For more information:" links use the `/baldwin/en/` form; five of the eight live articles are stored under the default help center, so confirm each resolves for Baldwin members at transfer.
