# QA: Filter Your Search with Map Tools

- **Article:** Filter Your Search with Map Tools
- **Old title:** Map Tools in Search
- **Old Notion page:** none given; rewritten from the live article
- **Intercom:** article 14744497, content 17317672, Baldwin help center only (Search / Filters). Not in the CRMLS help center
- **Mirror:** `docs/help-center/baldwin/map-tools-in-search.md`, checked against `get_article` October 12, 2026; no differences
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-filter-your-search-with-map-tools-rewrite.md`
- **New Notion draft:** https://app.notion.com/p/3f88b9e0143881e28aacdefe9bf5244b
- **Scored by:** Claude for Tara, October 13, 2026, against scorecard revision 2
- **Product answers:** Tara, October 12 to 13, 2026, from seven current screenshots and answers. Hover labels: Address search, Polygon tool, Freehand tool, and Delete all boundaries in the toolbar; Clear all boundaries on a boundary's trash icon; no labels on the check mark, X, or commute travel icons. Map open by default; the pin alone does not filter; radius starts at 1 mi, ranges 0.25 to 20 mi, and resizes by field, minus and plus, or edge handle; commute starts at driving, 15 min, Mon, Rush Hour, and Other takes a whole number from 1 to 60; polygon needs three points and closes on the first; freehand closes near its start; Include is the default; boundaries and Location filters combine as Or; boundaries save with a Saved Search; excluded boundaries count toward Any boundary and Overlaps only. October 13, 2026: the toolbar trash icon removes every boundary and a boundary's own trash icon removes only that boundary; a commute area cannot be excluded; the Freehand tool icon is a hand

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Three live images had no alt text; placeholders now carry it |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Commute Filter", "Tips", and "Circle Shapes (Radius Boundaries)" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the map tools |
| 8 entity_distribution | Fail | Pass | Old shape sections never named the map tools |
| 9 semantic_chunk_boundaries | Fail | Pass | Old Tips section mixed eight unrelated facts |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | No old Steps block said what happens to the results |
| 13 limitations_workarounds | Pass | Pass | Location filter Or behavior now stated with the route forward |
| 14 numerical_clarity | Pass | Pass | |
| **Total** | 8 of 14 | 14 of 14 | |

## Plain language gate

Pass. No term from the do-not list. "Polygon" and "Freehand" are on-screen hover labels, used where the member finds the control.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 (7 of 7) | +21.4 |
| Chunk independence (25) | 8.3 (2 of 6) | 25.0 (6 of 6) | +16.7 |
| Answer completeness (25) | 14.3 (4 of 7) | 25.0 (7 of 7) | +10.7 |
| Fin-parsable formatting (10) | 1.3 (1 of 8) | 10.0 (8 of 8) | +8.7 |
| Accuracy and confidence (10) | 2.0 (1 of 5) | 10.0 (5 of 5) | +8.0 |
| **Total** | **34.5, Not retrievable as written** | **100.0, Fin-ready** | **+65.5** |

What the old article failed:
- Retrieval: bare-noun title, a description over 140 characters starting "In this article", no opening paragraph, and headings with no feature name and no heading echo
- Chunk independence: three H1s in the body, an eight-item Tips section, and the control-bar tip repeated three times
- Answer completeness: no outcome after any Steps block, no defaults for radius or commute, and no related links
- Formatting: bold UI labels, emoji tips, horizontal rules, em dashes, nested sub-steps, and images without alt text
- Accuracy: stale facts (a map you had to expand, a "search icon", a 60-minute commute, Roadmap), "ideal for", "You can use", and a coming-soon promise referring to a previous platform

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I search within a few miles of an address? | Yes | Yes |
| How do I find homes within 30 minutes of my client's office? | Yes | Yes |
| Can I draw my own shape on the map? | Yes | Yes |
| How do I exclude an area from my search? | Partly | Yes |
| What is the difference between Any boundary and Overlaps only? | Partly | Yes |
| Why am I seeing listings outside the shape I drew? | No | Yes |
| Do my map shapes save with my saved search? | No | Yes |
| How do I remove the shapes from the map? | Partly | Yes |

## Open items

- Resolved October 13, 2026, by Tara's test: with an included radius and an excluded polygon, Any boundary drops the overlap and Overlaps only gives the same count; with both included, Overlaps only shows only the overlap. The article now defines both options by included boundaries and says excluded boundaries keep their listings out under either option
- Resolved October 13, 2026: Rush Hour is 8:30 AM and Off-peak is 9:00 PM, local time. Now is not defined in the article
- Resolved October 13, 2026: a boundary's trash icon removes only that boundary, a commute area cannot be excluded, and the Freehand tool icon is a hand. Both markers removed
- For product, not the article: a boundary's trash icon removes only that boundary, but its hover label reads Clear all boundaries
- Resolved October 13, 2026: with the Address search field open, the pin can be dragged to any spot on the map instead of searching. Added as an alternative in step 2 of the radius and commute steps
- Dropped from the live article: "Multi-select driving directions are coming soon", which promised a future feature and referred to a previous platform, and the "re-center to your current location" tip. The lower-right icon's hover label is Return to persisted location, which is a different action
- Map layers stay with Customize Your Search Results View, which covers them in full. The link points at the live Customize Your Search View until that draft is ported
- Set conflict, fixed October 13, 2026: the Search Page Overview draft said a shape shows only listings that also match the Filters tab. Rewritten in Notion and the repo copy to say a shape and a Location filter combine as Or. Its unconfirmed claim that a shape works with every other filter was dropped rather than kept. The comment thread on that sentence was already resolved
- Retitle: the Search Page Overview and Customize Your Search Results View drafts both link "Map Tools in Search" by title; update their link text when this is ported
- CRMLS: the article is in the Baldwin help center only. At port it also needs a CRMLS collection, and three older CRMLS articles (Create Custom Boundaries with the Draw Filter, Filter Your Search by Commute, Using the Map on the Search Page) describe superseded flows and should be reviewed for retirement or redirect
- Video: placeholder. The two Looms in How To Run a Map Search (Getting Started, August 13, 2026) cover these tools and could replace it if they match the current screen
- The live Create a Search with Filters in Perchwell article links "Learn more here" to a Notion URL, which members cannot open
- Screenshots: all placeholders. The three live images show a Listings tab and a 60 min option and are out of date
