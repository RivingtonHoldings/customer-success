# QA: Search in the Perchwell Mobile App

- **Article:** Search in the Perchwell Mobile App
- **Old title:** Search Page Overview (renamed: the desktop article 13903243 carries the same title)
- **Sources:** live Intercom article 14786263, content 17381674, mirror `docs/help-center/baldwin/search-page-overview-14786263.md`; the article's four live screenshots, read October 20, 2026; the teammate's answers about the current mobile app, October 20, 2026. No Master Article List row exists for this article.
- **Scored by:** Claude for Kevin, October 20, 2026, scorecard revision 2
- **Set:** Mobile collection rows in the new database: Listing Detail Page in the Perchwell Mobile App and Manage Contacts in the Perchwell Mobile App (both Draft). Title pattern, Roles (All Except Client), and "Tap" verbs match them.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live images had no alt text; every placeholder now carries it |
| 3 undefined_terms | Fail | Pass | CMA defined; CSV no longer used |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Headings now name the task and the mobile app |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates Search; Roles property records All Except Client |
| 8 entity_distribution | Fail | Pass | Old sections never said "mobile app", so they read as the desktop page |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with its outcome |
| 13 limitations_workarounds | Pass | Pass | Chart export gap stated with the browser route |
| 14 numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

New: Pass. No term from the do-not list. "My Searches", "Search Filters", and "Search this area" are control labels named where the member finds them.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 (1/7) | 30.0 (7/7) | +25.7 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 3.8 (3/8) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **37.3** | **100.0** | **+62.7** |

Old band: Not retrievable as written. New band: Fin-ready, gate passed; five `[confirm: ...]` markers must be resolved before transfer.

Old failures: title collides with the desktop Search Page Overview; description starts "In this article" and runs 141 characters; no jobs opening; headings never name the mobile app; list order crossed; multiple H1s and H4s; Map, Listings, and Analytics stated twice; Steps blocks stop at the click; CMA and CSV undefined; bold UI labels, an emoji, horizontal rules, no alt text; "What You Can Do" heading; labels and Analytics behavior contradicted by the article's own screenshots.

## Fin test questions

| Question | Old, one section? | New, one section? |
|---|---|---|
| How do I save a search in the Perchwell app? | Yes, with labels the screenshot contradicts | Yes |
| Where are my saved searches on my phone? | Partly, in the layout list | Yes |
| How do I switch the map to satellite on mobile? | Yes | Yes |
| Can I export analytics charts from the mobile app? | Yes, but wrongly says yes | Yes, correctly says no and gives the browser route |
| How do I hide listings in the mobile app? | No | Yes |
| How do I clear all my filters on my phone? | No | Yes |
| How do I search just the area I'm looking at on the map? | No | Yes |
| How do I share listings from my phone? | Yes | Yes |

## Source differences and how they were settled

- My Searches and Save: the text named both; the screenshot showed the saved search's name in a dropdown with New beside it. The teammate confirmed the My Searches dropdown, Save next to it, and New starting a new saved search.
- Actions: the text listed five options; the screenshot shows six, adding Hide listings. The screenshot labels are used.
- Analytics: the text promised Market Share, Distribution, and Location reports with CSV or PDF export; the screenshot shows charts with Add chart, and the teammate confirmed charts cannot be exported on mobile. Stated once as a bare-deficit exception, since the live article promised export, with the browser route.
- Location re-center arrow icon: the text and the screenshot both show it; the teammate says there is no arrow icon now. Removed.
- Search this area and Reset: in the screenshots, not the text; behavior confirmed by the teammate and added.
- Quick Filters: Year Built confirmed by the teammate, though not visible in the screenshots.

## Custom boundary section, added October 21, 2026

Added at the teammate's request after their answers, October 21, 2026. Sources: the teammate's answers; the live Mobile: Drawing Custom Boundaries article (Intercom 12257768, published in the default help center, not in the Baldwin help center); its Arcade (recorded on an older app layout, used for step order only); the live Search Filters screenshot showing Select Custom Boundaries under Location. Corrections to the old article: there is no + button; the freehand tool is the pointer-finger icon; Include or Exclude is chosen after the boundary closes; boundaries are kept only when the search is saved, not reused across searches. The Radius and Commute definitions follow the browser's Map Tools in Search, which the teammate said the mobile tools are similar to. The section's lead, steps, outcome, and the save sentence were run through the step 7 greps and draft-quality pass; the golden questions still pass 14 of 14. The Notion page does not have this section yet, by the teammate's instruction.

The Notion page was edited after creation (Article Review Status set to Review Finished; "x" changed to “X” in the Quick Filters section). The repo draft was synced to that wording on October 21, 2026.

## Open items

- `[confirm: how you return to your search results after drawing a boundary]`.
- `[confirm: how you close a polygon, such as by tapping the first point again]`.
- `[confirm: whether polygon, radius, and commute boundaries also offer Include or Exclude]`.
- The shapes of the polygon and pin tool icons, so the article can name them by shape like the pointer-finger icon.
- What the Boundary Type row on the Search Filters screen ("Overlapping boundary types") does with two or more boundaries.
- Whether the radius distance and commute settings match the browser (0.25 to 20 miles; Driving, Cycling, or Walking; 15 to 60 minutes).
- The old Mobile: Drawing Custom Boundaries article (12257768) and the Drawing Custom Boundaries on an Apple Device row in the Master Article List carry the outdated + button steps. Once this article is live, the team may retire or redirect 12257768.
- Android: the old unpublished Android draft of this article omits Quick Filters and lists the standard map option as Roadmap. Not verified on an Android phone.

- `[confirm: the label of the button that finishes saving]` in Save a new search.
- `[confirm: whether Save shows next to the dropdown at all times, or only after you change filters]`. The live text says Save reappears after you edit filters; the first screenshot shows New, not Save, beside the dropdown.
- `[confirm: the on-screen labels of the two options]` when updating a saved search.
- `[confirm: whether Select All selects every listing in the results or only the listings loaded so far]`.
- `[confirm: whether Contact agents opens a text, an email, or both]`.
- Hide listings: whether hidden listings stay hidden only after the search is saved, as on desktop (Actions Menu Options on the Search Page). Inferred from the desktop draft, so left out of the body.
- Whether tapping a filter on the Search Filters screen opens a sub-screen that needs a back step. Steps 2 and 3 are written generically.
- The label on the My Searches dropdown when no saved search is open. The teammate calls it My Searches; no screenshot shows that state.
- **Privacy, replace now:** three live screenshots (Group 98, Group 81, Group 80) show saved search names that appear to carry client names. They are published today; replace or crop them in Intercom now, not at port.
- Default help center links (`/en/`) to Manage Your Saved Searches, Share and Export Analytics Charts, Message Clients in Perchwell, and Create a Listing Report; flag at transfer.
- The Listing Detail Page in the Perchwell Mobile App link points at its Notion draft; replace with the public URL at transfer.
- Intercom lists a second parent collection (19637741) for this article that the mirror does not show; check at port.
