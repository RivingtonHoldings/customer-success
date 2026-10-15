# QA: Search for Condos and Condo Complexes

- **Article:** Search for Condos and Condo Complexes
- **Old title:** Search for a Condo
- **Old Notion page:** https://app.notion.com/p/36f8b9e014388048888ec6897d03a1f8 (Master Article List, read only)
- **Intercom:** article 15363551, content 18225099, collection Search / Filters, Baldwin
- **Mirror:** `docs/help-center/baldwin/search-for-a-condo.md`
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-search-for-condos-rewrite.md`
- **Scored by:** Claude for Tara, October 15, 2026, scorecard revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Fail | Pass | Live images had no alt text; both kept images and the placeholder now carry it |
| 3 | undefined_terms | Pass | Pass | |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "Use Structure Style Filter" named the tool, not the task |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | No role gate; Roles property records All Except Client |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Live article had no opening paragraph |
| 12 | instruction_completeness | Pass | Pass | Live "Run your search" step was stale; results update on their own |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | |

Old: 11 of 14. New: 14 of 14.

## Plain language gate

Pass. "Property sub type" appears only in the step that clicks the field. "Structure style" in the outcome sentence is the filter's own name, which members coming from a legacy platform already know by that name.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: description 152 characters, no opening, headings name the tool, no heading echo) | 30.0 | +17.1 |
| Chunk independence (25) | 20.8 (5/6: section headings were H1) | 25.0 | +4.2 |
| Answer completeness (25) | 17.9 (5/7: no defaults stated, no related links) | 25.0 | +7.1 |
| Fin-parsable formatting (10) | 5.0 (4/8: labels misspelled, bold, no alt text, horizontal rule) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5: "will return condominium listings" overclaims Residential attached; "You can") | 10.0 | +4.0 |
| **Total** | **62.6, Needs rewrite** | **100.0, Fin-ready** | **+37.4** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I search for condos? | Yes | Yes |
| Which property type and subtype do I pick to find condos? | Yes, with stale labels | Yes |
| Why are duplexes showing up in my condo search? | No | Yes |
| Where is the Structure Style filter? | No | Yes |
| How do I find condos in Gulf Shores? | No | No; the City section was cut in review as not condo-specific, so Fin combines this article with Create a Search with Filters |
| How do I search for listings in a specific condo complex? | Yes, with stale steps | Yes |
| How do I leave condos out of my search? | No | No; the Or to Not sentence was cut in review |
| How do I find listings that are not in a subdivision? | No | Yes |
| How do I leave one condo complex out of my search? | No | Yes |

## Source differences and decisions

- The old Notion page had a "Filter Filter" section the live article lacked. It became the step that finds each filter by name in the Search filters and values field.
- Labels corrected from the live images and the sibling draft: Residential-Single Family, Property sub type, Residential attached.
- "This search will return condominium listings" corrected: Property Types in Perchwell defines Residential attached as any home with a common wall, including condos, duplexes, triplexes, and 4-10 unit properties.
- Subdivision/Condo is a pick list under Location, confirmed by Tara's screenshot, October 14, 2026. The live image showed it under Location & Site Context; Apx Acreage is still under Location & Site Context.
- Confirmed by Tara: lead with Property Type and subtype; Structure Style narrows a Residential attached search; Structure Style offers Or, And, and Not; Subdivision/Condo offers Or and Not, since a listing holds one subdivision; None finds listings with no subdivision entered; add the City filter. October 15, 2026: Subdivision/Condo allows more than one name, with Or or Not, and the City filter is labeled City.
- Title changed to Search for Condos and Condo Complexes, Tara's pick. No collision found in the mirror, collection names, or page names.

## Open items

- The Structure Style image (Group 109) still shows Subdivision/Condo under Location & Site Context in the background. The focus of the image is current; refresh at the media owner's discretion.
- The Subdivision/Condo image (Group 112) shows the old panel name and is replaced with a placeholder.
- The link to Filter Your Search by Property Types describes the Notion draft that will replace it, which lists subtypes; the live article does not yet. Port that sibling first or together.
- The Search FAQ draft links this article by its old title and a default help center URL (`/en/`). Update the link text at port.
- Video: the old row says "New Video" with no link; the draft carries a video placeholder.
