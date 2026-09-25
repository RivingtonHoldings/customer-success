# QA: Customize Your Search Results View

**Old title:** Customize Your Search View
**Sources:** old Notion page `https://app.notion.com/p/1d58b9e0143880c5816ac052fbead122` (Master Article List) | Intercom article `11962073`, content `13190641` | mirror `docs/help-center/baldwin/customize-your-search-view.md` and `docs/help-center/crmls/customize-your-search-view.md` (shared article, one Intercom record in both help centers)
**Scored by:** Claude, for Tara, 2026-09-24
**Check set:** September 10, 2026 set, revision 2

Product questions were answered by Tara on 2026-09-24 before drafting, with four screenshots of the live product: the Search page, Expanded, List, and Tiles views, the map layers panel, the Columns control on the Templates tab, and the Save Column Template modal. The live article's own nine images were read at full resolution before the questions were asked.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | "Click the view a different format of the Results page" was broken; nine images sat under bare headings with no description. Every control is now named by label or position |
| 2 | visual_content_text | Fail | Pass | All nine live images carry an empty `alt` attribute, confirmed in the browser. All nine now carry alt text written from the image; three placeholders carry the alt text they will use |
| 3 | undefined_terms | Fail | Pass | "column template", "Template Search", and "Analytics View" were undefined. "column template" is now defined at first use; Search Analytics is distinguished from the Analytics page |
| 4 | structured_enumeration | Fail | Pass | The five views were bold-label prose blocks. They are now a labeled bullet list, as are the map controls and the layer types |
| 5 | query_answer_symmetry | Pass | Pass | Old headings already named what they answered |
| 6 | self_contained_sections | Fail | Pass | "Once you're done customizing your search results view..." plus an orphaned `Steps:` block under no heading. Sections now name the surface and cross-reference by name |
| 7 | audience_specification | Pass | Pass | No role gates this workflow; both versions correctly say nothing |
| 8 | entity_distribution | Pass | Pass | Feature names repeat in every section |
| 9 | semantic_chunk_boundaries | Fail | Pass | The columns section held three procedures, two of them near-identical. Now one procedure per section |
| 10 | restate_questions | Pass | Pass | Old article had no tables. The new default-template table carries an intro sentence |
| 11 | overview_jtbd | Fail | Pass | "In this article: You will learn how to..." replaced with "Use this article to ..." |
| 12 | instruction_completeness | Fail | Pass | No `Steps:` block said what happens next. Both now do |
| 13 | limitations_workarounds | Fail | Pass | The old article implied columns were unavailable in Tiles and never said so. Now stated as the route forward, with Location and Status covered the same way |
| 14 | numerical_clarity | Pass | Pass | Neither version makes a vague quantity claim |

**Old: 5 of 14 pass. New: 14 of 14 pass.**

## Plain language gate

**Old: fail. New: pass.**

Terms flagged in the old article and their replacements:

| Flagged | Replacement |
|---|---|
| "Click the view a different format of the Results page" (incomplete sentence) | "The View control above your search results changes how listings display on the Results tab of the Search page" |
| "you can do so from the Columns drop down"; "you can save your column layout" | imperative: "Add, remove, and reorder columns from the Columns control" |
| "Select Analytics View to use visual charts to view listing data" | "Analytics: Charts the listings that match your search criteria" |
| "a consumer focused view of listings" | "Displays listings as cards with larger photos and no columns" |
| "Once you're done customizing your search results view, you can save your column layout as a template for future searches" (restates the `Steps:` block below it, check 4) | cut; the section lead now states the purpose only |
| "3 dots", "6 dots" | "the handle on the right edge of the map", "the handle to the left of a column name" |

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| **Total** | **45.9** | **100.0** | **+54.1** |

**Old band:** Not retrievable as written (0 to 49)
**New band:** Fin-ready (90 to 100), with one open `[confirm: ...]` to resolve before transfer

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I see photos in my search results? | No. The views are bold sub-blocks inside one long section | Yes. Change how listings display with the View control |
| How do I add a column to my search results? | Partly. Two near-identical procedures compete | Yes. Add, remove, and reorder columns in your search results |
| Why can't I remove the Location column? | No. Not mentioned | Yes. Add, remove, and reorder columns in your search results |
| How do I make my columns stay the same on every search? | No. The article points at a star that is not in the Columns control | Yes. Set a default column template for new searches |
| Why don't I see columns in Tiles? | No. Implied once, never stated | Yes. Add, remove, and reorder columns in your search results |
| How do I turn on the satellite map? | Partly. Layers listed in a bullet with no steps and the wrong base map name | Yes. Resize, hide, and change layers on the search map |
| How do I get the map out of the way? | Yes | Yes. Resize, hide, and change layers on the search map |
| What's the difference between Update and Save New? | No. The old article named neither button | Yes. Save your columns as a column template |

## Open items

1. `[confirm: what the Flood and Parcels overlays draw on the map]` in the map layers section. The toggle names are on screen; what each overlay renders is not sourced.
2. **Shared article.** Intercom record `11962073` sits in a collection in both the Baldwin and the CRMLS help center. Per Tara, 2026-09-24, the row carries `MLS/AOR: Baldwin, CRLMS All`, matching Universal Search Bar. Cross-links in the body point into the Baldwin help center only; flag at port.
3. **Link needs replacing when the new article lands.** The default-template hand-off currently points at the live *Customize Your Search Defaults with Template Searches*. Tara has *Create a Default Saved Search Template* planned as its own article; swap the link then.
4. **Two errors in the live article that this rewrite drops.** Step 5 of both column procedures said "Click Save and name the template. You can select the star to save it as the default column view." There is no Save button and no star in the Columns control; the star belongs to saved searches. And the base map is Roads, not Roadmap.
5. **Sibling check passed.** Search Page Overview states that Location and Status "can be reordered but cannot be removed." Confirmed correct by Tara, 2026-09-24. No fix needed to that draft.
6. **Three new screenshots needed:** the Save Column Template modal, the Templates tab with a filled star, and the map layers panel. `Media Update Needed: Yes` is set so the row reaches the production board.
7. The nine carried images are the live article's own, July 2026, and show real addresses, as they do today in production. Replace or crop if the team's localization pass covers them.
