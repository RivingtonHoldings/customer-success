# QA: Filter Your Search by Keyword

- **Article:** Filter Your Search by Keyword
- **Old titles:** Filter Your Search with Keywords (Baldwin), Filter Your Search by Keywords (CRMLS)
- **Sources:** Baldwin Intercom 16053548, content 19293451, `docs/help-center/baldwin/filter-your-search-with-keywords.md`; CRMLS Intercom 11011163, content 11832879, `docs/help-center/crmls/filter-your-search-by-keywords.md` (a separate article, not shared); old Master Article List row https://app.notion.com/1db8b9e01438808b8af1e2bd939f9059; Tara's screenshots of the Filters tab and the Text search column, October 12 and 13, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-filter-your-search-by-keyword-rewrite.md`
- **Scored by:** Claude, October 13, 2026, scorecard revision 2
- **Original scored:** the live Baldwin article

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Both live images had no alt text; placeholders now carry it |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | Or and And now a labeled list |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the filter; Roles property is All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old description was "In this article: You will learn"; no jobs opening |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with the result |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | |

Old: 11 of 14. New: 14 of 14.

## Plain language gate

New: pass. No do-not-list terms. "keyword" is the member's word and leads every heading; Text Search, Applied Filters, and Search filters and values appear only where the member has to find the control.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30, 7 checks) | 21.4 (5/7: description 165 characters with "In this article:", no "Use this article to" opening) | 30.0 (7/7) | +8.6 |
| Chunk independence (25, 6 checks) | 16.7 (4/6: H1s inside the body; quotation-mark advice stated three times) | 25.0 (6/6) | +8.3 |
| Answer completeness (25, 7 checks) | 17.9 (5/7: no outcome after the steps; dropdown behavior and default unstated) | 25.0 (7/7: Or confirmed as the default, October 13, 2026) | +7.1 |
| Fin-parsable formatting (10, 8 checks) | 3.8 (3/8: terminal periods and bold in steps, emoji callout with no label, bold throughout, no alt text) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence (10, 5 checks) | 6.0 (3/5: "Text filter" and the NOT option are wrong on screen; "Use OR", "Use the Text filter") | 10.0 (5/5) | +4.0 |
| **Total** | **65.8, Needs rewrite** | **100.0, Fin-ready** | **+34.2** |

New: Fin-ready score; gate passed; plain language passed. Rescored after Tara's review edits and the default check, October 13, 2026; the edits changed no check result.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I search listings by keyword? | Yes | Yes |
| How do I search for an exact phrase like high ceilings? | Yes | Yes |
| How do I search for two keywords at once? | No, commas never mentioned | Yes |
| Does keyword search include agent remarks? | No | Yes |
| Where is the keyword filter on the Filters tab? | Partly, "search for the Text filter" names a label the screen does not show | Yes |
| Can I add a keyword column to my search results? | No | Yes |
| How do I remove a keyword filter? | No | Yes |
| Can I exclude listings that mention a word? | Answers wrongly, with a NOT option the Text Search dropdown does not have | Yes, section 2 says Text Search does not exclude a word |

## Open items

- Resolved October 13, 2026: Or is the Text Search dropdown default, checked on a new search. Earlier evidence conflicted: And in the October 12 screenshots, Or in the July 2026 article image.
- Deliberate exception to "never a bare deficit": section 2 states that Text Search does not exclude listings that mention a word, with no workaround. Hide does not work as one, since hiding the keyword results leaves nothing. Kept because the live Baldwin article told members to pick NOT and golden question 13 asks for known limitations; Tara's call, October 13, 2026. Ask product whether a keyword exclusion is planned; if one ships, this sentence becomes its home.
- Replace now: the live Baldwin article's first image shows a real saved search name and an agent's full name. It is published today.
- The live Baldwin article's second image shows the Body of Water filter, not Text Search.
- CRMLS article 11011163 is a separate Intercom article, not shared. It needs its own port or a redirect once this draft is live.
- The link to Customize Your Search View points into the default help center (`/en/`); confirm at transfer, and switch to Customize Your Search Results View once that draft is ported.
- Resolved October 13, 2026: Search Page Overview said column filters leave the Filters tab unchanged. Tara confirmed Text search and Price column filters both add to the Filters tab, and the section was rewritten.
- Vocabulary: older live articles say "keyword" for SearchWell and for the Search filters and values field. Watch Fin test runs for crossed answers.
