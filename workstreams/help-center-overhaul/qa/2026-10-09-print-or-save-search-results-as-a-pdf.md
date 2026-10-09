# QA: Print or Save Search Results as a PDF

- **Article:** Print or Save Search Results as a PDF
- **Old title:** Print Search Results
- **Old Notion page:** https://app.notion.com/p/3b88b9e01438802dad0de2c083a95a3c (Master Article List, read only)
- **Intercom:** article 16302253, content 19647378, Baldwin only. The old row's Intercom Internal URL points at content 12887977 (Export Listings in Perchwell), and its public URL field is empty
- **Mirror:** `docs/help-center/baldwin/print-search-results.md`
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-09-print-or-save-search-results-as-a-pdf-rewrite.md`
- **New Notion draft:** https://app.notion.com/p/3f48b9e0143881c18b61d09ddd6add77
- **Scored by:** Claude for Tara, October 9, 2026, against scorecard revision 2
- **Product answers:** Tara, October 9, 2026: no selection needed; every listing in the result count prints, including unloaded ones; header reads Search Results plus the saved search name; Landscape seen in six accounts but may be sticky; keep the Loom

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live image had no alt text; placeholders now carry alt text |
| 3 undefined_terms | Pass | Pass | PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates Print |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | First Steps block stopped at Click Print |
| 13 limitations_workarounds | Fail | Pass | Tiles view restriction added with the route forward |
| 14 numerical_clarity | Pass | Pass | |
| **Total** | 10 of 14 | 14 of 14 | |

## Plain language gate

Pass. No terms from the do-not list. "Print", "Keep", "Hide", "Layout", and "Destination" are on-screen control labels.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4 of 7) | 30.0 (7 of 7) | +12.9 |
| Chunk independence (25) | 20.8 (5 of 6) | 25.0 (6 of 6) | +4.2 |
| Answer completeness (25) | 14.3 (4 of 7) | 25.0 (7 of 7) | +10.7 |
| Fin-parsable formatting (10) | 7.5 (6 of 8) | 10.0 (8 of 8) | +2.5 |
| Accuracy and confidence (10) | 10.0 (5 of 5) | 10.0 (5 of 5) | 0 |
| **Total** | **69.7, Needs rewrite** | **100.0, Fin-ready** | **+30.3** |

What the old article failed:
- Retrieval: description was "In this article..." at over 140 characters, there was no opening paragraph, "Control which listings appear" did not name the feature, and the description listed listings before columns while the sections ran the other way
- Chunk independence: sections were H1
- Answer completeness: the first Steps block had no outcome, the Tiles restriction was missing, and the related link was "view our help center article here" with a bare URL
- Formatting: UI elements were bolded, and the image had no alt text

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I print my search results? | Yes | Yes |
| Can I save my search results as a PDF? | Yes | Yes |
| Why don't I see Print in the Actions menu? | No | Yes |
| Do I have to select listings before I print? | No | Yes |
| Will it print all my results or only the ones on the screen? | Partly | Yes |
| How do I change which columns print? | Yes | Yes |
| How do I take some listings off my printout? | Yes | Yes |
| Do photos print with my search results? | No | Yes |

## Open items

- Resolved by Tara, October 9, 2026: the print window's button switches from Print to Save when Destination is Save as PDF, and listings hidden with Keep do not print. Both markers removed
- Landscape is not stated as the default, since Tara saw it in six accounts but it may be the last value selected
- Load count: Tara confirmed October 9, 2026 that 30 listings load at first, which matches Search Page Overview and Export Listings to a CSV File. This article gives no number
- The Customize Your Search Results View link points at its Notion draft; replace it with the public URL at port
- The live article is in the Baldwin help center only. At port, it also needs adding to a CRMLS collection
- Screenshots: both are placeholders. The live August 10 image is out of date: it shows Columns: New and a different Actions menu
