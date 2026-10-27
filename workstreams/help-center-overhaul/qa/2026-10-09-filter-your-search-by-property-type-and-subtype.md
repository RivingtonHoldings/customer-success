# QA: Filter Your Search by Property Type and Subtype

- **Article:** Filter Your Search by Property Type and Subtype
- **Old title:** Filter Your Search by Property Types
- **Old Notion page:** https://app.notion.com/p/3198b9e0143880d1a49fe2e98125f547
- **Intercom article ID:** 13922158, content ID 16183571
- **Mirror path:** `docs/help-center/baldwin/filter-your-search-by-property-types.md` (Baldwin only, not shared)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-09-filter-your-search-by-property-type-and-subtype-rewrite.md`
- **Scored by:** Claude, with Tara, October 9, 2026
- **Check set:** September 10, 2026, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Pass | Pass | |
| 2. visual_content_text | Pass | Pass | Live article has no images; every placeholder in the draft carries alt text |
| 3. undefined_terms | Pass | Pass | |
| 4. structured_enumeration | Pass | Pass | |
| 5. query_answer_symmetry | Fail | Pass | Live "Tips" heading was a bare noun |
| 6. self_contained_sections | Pass | Pass | |
| 7. audience_specification | Pass | Pass | Open to every member except clients; body says nothing, per the standard |
| 8. entity_distribution | Pass | Pass | |
| 9. semantic_chunk_boundaries | Pass | Pass | |
| 10. restate_questions | Pass | Pass | Table carries an intro sentence |
| 11. overview_jtbd | Fail | Pass | Live article had no opening paragraph |
| 12. instruction_completeness | Fail | Pass | Live steps stopped at the last click |
| 13. limitations_workarounds | Pass | Pass | Live sales-and-rentals tip was stated with a workaround, but was wrong; removed |
| 14. numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "Property sub type" is named only where the member selects from that field; prose uses "subtype". "Quick filters" matches the Search Page Overview draft.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4/7) | 30.0 (7/7) | +12.9 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| **Total** | **56.0, Needs rewrite** | **100.0, Fin-ready** | **+44.0** |

Old failures: description over 140 characters and written as "In this article, you will learn"; no opening paragraph; "Tips" heading; sections at H1; no outcome after steps; "Some property types"; no links; bold throughout; horizontal rules; "you can" and "Use"; the Edit control and the sales-and-rentals tip no longer match the product; "may also be able to" left an unverified option unmarked.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I filter my search by property type? | Yes | Yes |
| I can't find Property Type when I search the filters. Where is it? | No | Yes |
| Can I search for sale and rental listings at the same time? | No, answers wrong | Yes |
| How do I search only attached homes? | Partly, via Edit | Yes |
| How do I find multi-family rentals? | No | Yes |
| What subtypes are under Commercial Lease? | No | Yes |
| How do I search rentals but leave out land? | No | Yes |
| What was Class in Paragon called in Perchwell? | No | Yes |

## Sources and decisions

- Tara's screenshots, October 9, 2026, settled the subtype flow: no Edit button; selecting a type opens its Property sub type field; All changes to the number of subtypes selected; the Or dropdown holds Or, And, and Not.
- Tara confirmed: the x on the Property Type button clears the filter and the round x in the Property sub type field clears every subtype; Property Type is a quick filter only and is not searchable in the Search filters and values field; Lease can be combined with another property type in one search; cover all three of Or, And, and Not; Not is the way to exclude, and the live "include or exclude listings without a subtype" option was dropped.
- Subtype lists and spellings from Tara's voice memo and follow-up, October 9, 2026.
- Lease description narrowed to homes and land, since Lease has no multi-family subtype; multi-family rentals sit under Commercial Lease.
- Legacy names from the live New Terminology article: Class became Property Type, and Property Type became Property Subtype.

## Open items

- The Arcade video (https://app.arcade.software/share/6T5f7kivMeluXIIEkJao) shows the retired Edit flow, so the draft carries a video placeholder instead.
- Search Page Overview's Notion draft and repo copy said every Quick Filter is also on the Filters tab. Fixed October 9, 2026 to say Property Type and Year Built are set from the Quick Filters only.
- The live Property Types in Perchwell article mixes types and subtypes, lists Land Lease and Other, and says Lease includes multi-family. It needs its own rewrite and a link back to this article.
- Search for a Condo is stored with a default help center link (`/en/`); the draft links the Baldwin path. Confirm at port.
- Confirm what distinguishes the four Multi-family classifications (the Multi-family property type and the Multi-family subtype under Commercial Sale, Commercial Lease, and Lots and Land), then decide whether the article needs a second sentence on capturing all multi-family listings.
- October 15, 2026: the property type table moved to What Each Property Type Includes (the rewrite of Property Types in Perchwell). This article's last section is now a link there, and "see what each Baldwin property type includes" left the opening. Comment threads on the table's What it covers header and the Multi-family sentence were attached to removed text. The link uses the 14709796 URL, whose slug changes when the new title is ported.
- Mobile is not covered.
- Fin labels, MLS audience, and publishing stay manual.
