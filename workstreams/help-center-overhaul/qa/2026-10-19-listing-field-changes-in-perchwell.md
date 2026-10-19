# QA: Listing Field Changes in Perchwell

- Old title: Field & Data Representation Upgrade
- Sources: old Notion page https://app.notion.com/p/3378b9e01438809f8c78ebaf9b98a4cf; Intercom article 14459773, content 16905918; mirror `docs/help-center/baldwin/field-data-representation-upgrade.md` (matches the live stored body, checked with `get_article` October 19, 2026)
- Product answers and screenshots: Kevin, October 19, 2026 (Location filters, Construction Status filter, Features filters)
- Scored by Claude for Kevin, October 19, 2026. Scorecard check set revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Fail | Pass | ANC, DOM, and FKA were undefined; DOM and RESO now defined, ANC and FKA gone |
| 4 structured_enumeration | Pass | Pass | Location filters now a labeled list |
| 5 query_answer_symmetry | Fail | Pass | Each heading names the field that changed and what replaced it |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Every member; nothing stated |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Six unrelated changes in one table became one H2 each |
| 10 restate_questions | Pass | Pass | No tables now |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening |
| 12 instruction_completeness | Pass | Pass | No Steps blocks |
| 13 limitations_workarounds | Pass | Pass | Area removal gives the filters to use instead |
| 14 numerical_clarity | Pass | Pass | 2030 upper limit dropped; Kevin found no fixed upper limit |

## Plain language gate

Pass. Greps for the do-not list returned "records" in "when records were lost", the ordinary real-world word, kept. "many" replaced with "shared across".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 12.5 (3/6) | 20.8 (5/6) | +8.3 |
| Answer completeness (25) | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| Total | 48.9 | 95.8 | +46.9 |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, no confirm markers open.

Old failures: bare-noun title; 178-character "In this article" description; no jobs opening; H1 used as a section heading; vague headings; one table mixing six topics; Class and Property Type stated in both tables; ANC, DOM, FKA undefined; no links; bold in body; horizontal rules; Paragon named seven times; "modern best practices" framing.

New failure: Chunk independence check 4. The Construction Status section keeps a one-sentence paragraph ("To find these listings, select Under construction ..."), which is a separate task from the paragraph around it.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where did the Area field go? | Partly, inside a table row | Yes |
| How do I search by school district now? | No, mentions school district only | Yes |
| What happened to Active New Construction? | Partly, table row | Yes |
| How do I find new construction listings? | No | Yes |
| Where is boat slip in Perchwell? | Partly, table row | Yes |
| What is Class called in Perchwell? | Yes, table | Yes |
| Where do I enter pool information? | Partly, table row | Yes |
| What year should I enter if year built is unknown? | Partly, table row | Yes, with a link for storm damage |

## Source differences

- Live article and old Notion page agree except for two trailing periods. Live wins; no conflict.
- Year Built: live says 1500 to 2030. Kevin found no fixed upper limit, so the draft states only 1500 or later.
- Area: live says location is defined by "school district". The Filters tab has Elementary School, Intermediate School, Middle School, and High School filters, not a school district filter (Kevin's screenshot). The fair housing reason keeps "school districts", quoted from the source's reason.
- Construction Status: the live article and both sibling drafts write "Under Construction". The Construction Status filter option reads "Under construction" (Kevin's screenshot); the draft follows the screen.
- Pool Features: "both private and community pools" combines the live article (Community Amenity and Property Amenity pool options consolidated) and Getting Started in Perchwell (covers private and public pools).

## Open items

- Resolved October 19, 2026: More than 2 pets allowed is an option in the Community Amenities filter under Features (Kevin's screenshot), spelled "More than 2 pets allowed". The Add/Edit field is taken from the live article (Community Amenities); not separately checked.
- Construction Status in the Add/Edit form: confirm the option reads Under construction there too, as it does in the filter.
- Year Built: whether any upper limit applies, such as rejecting a future year or 99999. Left out of the article.
- Set consistency: What Changed When You Moved to Perchwell and Find Familiar Features by Their Perchwell Names write "Under Construction". If the Add/Edit form also reads "Under construction", update both, along with the MLS Rules and Compliance FAQ and What Each Listing Status Means drafts.
- Live Listing Detail Page Overview says the Land and Lot section shows "MLS area". Kevin confirmed the Listing Detail Page has only a Map section, so that line is stale.
- Live Getting Started in Perchwell says "Active Under Contract is now Active with a construction status of Under Construction". It should say Active New Construction.
- Old row note: "Can use for MLSs coming from Paragon. Will need to do one for each MLS tech provider." The draft is Baldwin-specific (the Area and fair housing decision is Baldwin's); a CRMLS version needs its own facts.
- Link titles use the new draft names (What Each Property Type Includes, MLS Rules and Compliance FAQ, Filter Your Search with Map Tools) with the live URLs; recheck at port.
