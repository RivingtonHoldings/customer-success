# QA: What Each Property Type Includes

- **Article:** What Each Property Type Includes
- **Old title:** Property Types in Perchwell
- **Old Notion page:** https://app.notion.com/p/3498b9e01438806f86afca336708fa2b
- **Intercom article ID:** 14709796, content ID 17268842
- **Mirror path:** `docs/help-center/baldwin/property-types-in-perchwell.md` (Baldwin only, not shared)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-what-each-property-type-includes-rewrite.md`
- **Scored by:** Claude, with Kevin, October 15, 2026
- **Check set:** September 10, 2026, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Pass | Pass | |
| 2. visual_content_text | Pass | Pass | Live article has no images; the placeholder carries alt text |
| 3. undefined_terms | Pass | Pass | |
| 4. structured_enumeration | Pass | Pass | Subtypes are bullet lists |
| 5. query_answer_symmetry | Fail | Pass | Live article's only H2 was empty |
| 6. self_contained_sections | Pass | Pass | |
| 7. audience_specification | Pass | Pass | Open to every member except clients; body says nothing, per the standard |
| 8. entity_distribution | Pass | Pass | Each section names its property type |
| 9. semantic_chunk_boundaries | Fail | Pass | One table carried all seven rows; now one section per property type |
| 10. restate_questions | Fail | Pass | Live table had no intro sentence; the draft has no tables |
| 11. overview_jtbd | Fail | Pass | Live article had no opening paragraph |
| 12. instruction_completeness | Pass | Pass | No procedures |
| 13. limitations_workarounds | Pass | Pass | Lease has no Multi-family subtype, stated where a member looks; the route is a `[confirm]` |
| 14. numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "Subtype" is the prose word for the Property sub type field, matching the Filter Your Search by Property Type and Subtype draft. "Parcels" in the Lots and Land section is plain real estate vocabulary. No do-not list hits.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 20.8 (5/6) | 25.0 (6/6) | +4.2 |
| Answer completeness (25) | 21.4 (6/7) | 25.0 (7/7) | +3.6 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **64.3, Needs rewrite** | **100.0, Fin-ready** | **+35.7** |

Old failures: bare-noun title; description over 140 characters, written as "In this article", and promising filing rules the body never covers; no opening paragraph; empty H2; no links; bold table header; table with no intro sentence; five rows contradicting the current product (Land Lease and Other as property types, duplex, triplex, and 4-10 under Residential attached, Multi-family under Lease, no Commercial Sale or Commercial Lease).

The new score holds only once the two `[confirm]` markers are resolved; until then the article is not ready to transfer.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| What property type do I choose for a condo? | Partly, via Residential Attached | Yes |
| Where do I list a boat slip or a garage? | No, answers Other | Yes |
| What happened to Land Lease? | No, lists it as a type | Yes |
| Is a duplex Residential attached or Multi-family? | No, answers wrong | Yes |
| What subtypes are under Commercial Sale? | No | Yes |
| What was Class called in Perchwell? | No | Yes |
| Can I list a multi-family rental under Lease? | No, answers wrong | Partly, until the `[confirm]` is resolved |

## Sources and decisions

- Kevin, October 15, 2026: drop the filing-requirement claim; Garage is a subtype under Residential-Single Family; Duplex and Triplex are subtypes under Multi-family; the Add/Edit Property type dropdown lists the same six types and subtypes as the search filter (screenshot); define the six types only and list subtypes without definitions.
- Scope, Kevin: option 2, a definitions page. The table in Filter Your Search by Property Type and Subtype is trimmed to a link here.
- Subtype lists from the Filter Your Search by Property Type and Subtype draft (Tara, October 9, 2026), plus Garage.
- Type definitions from the live article and the live Filter Your Search by Property Types article. "All unimproved property" for Lots and Land was dropped, since its subtypes include RV lot improved and Mobile home.
- Legacy names from the live New Terminology article (Class is Property Type) and the live Most Common Questions Asked to MLS Staff article (the Other class merged into Residential-Single Family).
- Subtypes are a bare list, by Kevin's call, rather than the labeled list the standard asks for with named options.

## Open items

- `[confirm: which property type a multi-family rental is listed under]`
- `[confirm: when to choose the Multi-family property type over the Multi-family subtype under another property type]`
- Label case differs by surface: the Add/Edit dropdown reads Residential-single family, Lots and land, Commercial sale, Commercial lease; the Search Quick Filter in the live Search for Condos image reads Residential-Single Family. The draft follows the search spelling used across the set. Confirm the Quick Filter spelling for every type.
- Garage is not visible in the Residential-Single Family subtype list in the live Search for Condos image (June 2026). Confirm its position in the list; the draft places it last.
- Title change from Property Types in Perchwell; the Intercom URL slug changes at port, so links to `14709796` should be checked.
- Collection: the old FAQs & Cheat Sheets has no match in the new database; Manage Listings proposed, FAQs or Search are the alternatives.
- Search for Condos and Condo Complexes said Residential attached includes duplexes and triplexes. Fixed October 15, 2026 in Notion and the repo: a duplex or triplex unit sold on its own is not Residential attached.
- `docs/product-context.md` says the full subtype lists live in the Filter Your Search by Property Type and Subtype draft, and has no Garage.
- Mobile is not covered.
- Fin labels, MLS audience, and publishing stay manual.
