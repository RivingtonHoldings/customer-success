# QA: Create a Template Search

Retitled from "Customize Your Search Defaults with Template Searches" (live) and "Create a Default Saved Search Template" (old Notion row). Scored October 6, 2026 by Claude for Tara, against scorecard revision 2.

## Sources

- Old Notion page: https://app.notion.com/p/1d88b9e014388066ba5ed34cfc8ca910 (Master Article List, read only)
- Intercom article ID 13903342, content ID 16154717
- Mirror: `docs/help-center/baldwin/customize-your-search-defaults-with-template-searches.md` (Baldwin only, not shared)
- Live article images, captured July 4, 2026: the My Searches window (out of date, and it shows real contact names) and the Save Search window (still current)
- Tara's screenshots, October 6, 2026: the My Searches window with a green star on the Template Search, and the Save Search window after changing a search
- Tara's answers on October 6, 2026: the Saved Searches button label, Start New and New Search both apply the Template Search, the Perchwell logo goes to the Dashboard and does not reset the search, Update Current on a new search does not change the Template Search, what the Template Search saves (map zoom, layer, size, sort order), starring a different search moves the Template Search, clicking the filled star turns it off, the star's hover label, changing the Template Search with Update Current, keeping the Arcade as a video placeholder
- Sibling drafts read for set consistency: Customize Your Search Results View, Search Page Overview, Set Up Email Alerts for Saved Searches
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-06-create-a-template-search-rewrite.md`, revised the same day with Tara's edit (tighter leads that name the task and place instead of the click, Start New and New Search labeled by location) plus seven fixes restoring "default", the view-icon location, "hide the map", "dropdown menu", the *(Optional)* format, the hover label in the lead, and a contrast lead for changing the Template Search. Scores below are for the revised draft and are unchanged
- Notion draft: https://app.notion.com/p/3f18b9e0143881f798baf9e86734ac7b

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old step: "Find the saved search you just created" |
| 2 visual_content_text | Fail | Pass | Old images had no alt text |
| 3 undefined_terms | Fail | Pass | Old used "column template" with no definition or link |
| 4 structured_enumeration | Pass | Pass | What a Template Search saves is a labeled list |
| 5 query_answer_symmetry | Fail | Pass | Old headings: "Template Search setup", "Step 2: Save the search" |
| 6 self_contained_sections | Fail | Pass | Old Step 3 depended on Step 2 |
| 7 audience_specification | Pass | Pass | No role gate; silence |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass, pending one marker | Every Steps block ends with the outcome. Step 9 of the save procedure carries a confirm marker on the button that confirms the name |
| 13 limitations_workarounds | Fail | Pass | One Template Search at a time, and its priority over a default column template, stated where the member sets it |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "columns/template dropdown menu" is the set's settled name for that control. "base template" appears only inside the star's exact hover label. No term from the do-not list.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7: title shares "Customize Your Search" with Customize Your Search View, description is 166 characters and opens "You will learn", no opening paragraph, headings do not name what they answer, no heading echo) | 30.0 | +21.4 |
| Chunk independence (25) | 12.5 (3/6: Step 3 points back at Step 2, "Save the search" carries no feature name, sections at H1) | 25.0 | +12.5 |
| Answer completeness (25) | 7.1 (2/7: no step block ends with an outcome, turning off and changing the template missing, one-template limit missing, column template not defined, no related links) | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 5.0 (4/8: terminal periods on steps, bold throughout, no alt text, horizontal rules) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5: the button is labeled Saved Searches, not My Searches; "You can adjust" and "How to use") | 10.0 | +4.0 |
| **Total** | **39.2, Not retrievable as written** | **100.0, Fin-ready** | **+60.8** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I make a saved search my default for new searches? | Partly; button label is wrong | Yes |
| What does a template search save? | Partly; no sort order or map detail | Yes |
| How do I change my template search? | No | Yes |
| How do I turn off my template search? | No | Yes |
| If I save a new search I started from my template, does it change the template? | Partly | Yes |
| Can I have more than one template search? | No | Yes |
| Why are my new searches not using my default column template? | No | Yes |
| Where do I start a new search with my template applied? | Partly; New Search only | Yes |

## Open items

- `[confirm: the button that confirms the name, and whether Save asks for a name on a search that has not been saved yet]`, step 9 of the save procedure. Create a Search with Filters says Start New asks for a name, so the name may already be set before Save is clicked.
- Not in the draft: whether refreshing the page resets the search to the Template Search. The old Click Script said so; Tara confirmed only that the Perchwell logo does not.
- MLS/AOR set to Baldwin and CRLMS All (Tara, October 6, 2026). The live article is in the Baldwin help center only, so adding it to a CRMLS collection is a step at port time. Its links point into the Baldwin help center.
- The live article's first image shows real contact names. Replace it at port, or sooner.
- Customize Your Search Results View links to this article by its old title and live URL. Update that link when this article is ported.
- Manage Your Saved Searches (live, not yet migrated) repeats this article's steps in "Set a template search". When it is migrated, cut that section to one sentence and a link here.
- The link to Customize Your Search Results View points at its Notion draft. Replace it with the live URL at transfer.
- Arcade video kept as a placeholder; the team is replacing all videos.
