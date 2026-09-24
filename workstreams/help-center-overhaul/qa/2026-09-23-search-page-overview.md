# QA: Search Page Overview

Article name: Search Page Overview (title unchanged)
Scored by: Claude, for Tara, 2026-09-23. Body rewritten by Tara and merged 2026-09-24; rescored, band unchanged.
Scorecard set: September 10, 2026, revision 2

## Sources

- New Notion draft: https://app.notion.com/p/3e58b9e0143881dd8234e6ec3dfc3397 (created 2026-09-23)
- Old Notion page: https://app.notion.com/p/2f58b9e014388073a886f83c03b8ab7c (Master Article List, read only, left unchanged)
- Intercom article ID: 13903243, content ID: 16154547
- Mirror: `docs/help-center/baldwin/search-page-overview.md`
- Live stored body read with `get_article`, not from the mirror, to check link targets
- Six current product screenshots supplied by Tara, 2026-09-23, plus the article's own Intercom CDN images read from the public help center page

## Scope decision

Tara chose orientation-only (option a, 2026-09-23). The Search page's procedures are handed to the articles that already own them; this article orients and links. Roughly 70 percent of the live article's body is therefore gone, not lost: every removed procedure has a named destination in the table under Open items.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old named four controls by shape ("three lines", "6 dots", "3 dots", "layer icon") and used an emoji pointer. New names controls by function and position |
| 2 | visual_content_text | Fail | Pass | Old had about 20 images and no alt text. New has three placeholders carrying their alt text |
| 3 | undefined_terms | Fail | Pass | CSV now expanded; "Filter Filter", an internal nickname, is gone |
| 4 | structured_enumeration | Fail | Pass | Old broke its own numbering in the Keep block and used bold pseudo-headings for the share methods |
| 5 | query_answer_symmetry | Fail | Pass | Old had bare headings ("Change listing view", "Share listings") |
| 6 | self_contained_sections | Fail | Pass | Old Flood Zones section opened "Navigate over to the search map", then "On the bottom right" |
| 7 | audience_specification | Pass | Pass | No role gates the Search page; the body stays silent, per the house rule |
| 8 | entity_distribution | Fail | Pass | Every section now names the Search page, the Filters tab, or the Results tab |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old put email, public link, tags, viewing tags, and messaging in one H2 |
| 10 | restate_questions | Pass | Pass | No tables in either |
| 11 | overview_jtbd | Fail | Pass | Old used "In this article: You will learn how to", the form Intercom names as weakest |
| 12 | instruction_completeness | Fail | Pass | Old stopped at "Click Save and name your search". New carries no step-by-step blocks at all; every procedure is handed off with a descriptive link, which is the scope decision above |
| 13 | limitations_workarounds | Fail | Pass | New states two constraints where the member meets them: Location and Status cannot be removed, and Keep and Hide do not survive a reload unsaved |
| 14 | numerical_clarity | Pass | Pass | No vague quantities in either |

Old: 3 of 14. New: 14 of 14, gate passed.

## Plain language gate

**Pass.** No term from the do-not list in the sense it bans. "Tiles" appears only as the on-screen label in the View control. The live article's "Filter Filter" was removed: it is not on screen, the control is a search field labelled Search filters and values, and the old Notion page carries an unresolved comment thread on that exact phrase.

## Dimensions

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 4.3 (1/7) | 25.7 (6/7) | +21.4 |
| Chunk independence | 25 | 4.2 (1/6) | 25.0 (6/6) | +20.8 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence | 10 | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **100** | **24.1** | **95.7** | **+71.6** |

Old band: Not retrievable as written. New band: Fin-ready.

**The one failed check.** Retrieval signals check 1, title collision. Article 14786263, in the Baldwin Mobile collection, is also titled "Search Page Overview" — identical string, same help center. Tara chose to keep this title and retitle the Mobile article, so the check passes once that lands. It is scored as a failure here because it is a failure in the artifact as it stands today.

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I get back the listings I hid in my search? | No. The old text named an "Unhide icon" that does not exist; Search FAQ answered it separately | Yes, "Narrow your search results without changing your filters" |
| Why did my hidden listings come back? | No. The old article never stated that Keep and Hide need a save | Yes, same section, in the Important callout |
| Can I remove the Location column? | No | Yes, "Work through listings on the Results tab" states that Location and Status reorder but do not come out |
| Where do I save a column template? | No. The old article said "Click Save" twice; the buttons are Update and Save New | Yes, same section |
| What is the difference between Filters and Results? | No. The old bullets called the second tab both "Search view" and "Results" | Yes, "Move between the Filters and Results tabs on the Search page" |
| How do I tag a listing for a different client mid-search? | No. The old article stated it as an emoji tip with no mechanism | Yes, "Tag listings for more than one client without leaving your search" |
| What charts can I add to my search? | No. The old article listed "Trends", which is not a category | Yes, "See market charts for your results with Search Analytics" |
| Is Search Analytics the same as the Analytics page? | No | Yes, Note callout in the same section |
| Why can't I print my search results? | No | Yes, "Act on the listings you select in Search" names Tiles view as the cause and the switch as the fix |

## Open items

**Tara's pass, 2026-09-24.** Tara rewrote all nine sections and the merged version is what stands. Her structure carried: the tabs, views, Keep and Hide, and the chart controls all became bullet lists with colon lead-ins, which is what factor 4 asks for and what the prose version was working around. Two of her changes were outright corrections: the Location and Status constraint is scoped to List and Expanded views, where columns exist, and the Print constraint is stated as a Note where a member meets it.

Her pass reintroduced ten instances of the verb "use" as a stand-in and of "you can", both on the do-not list and both scored under Accuracy and confidence check 5. This is the documented humanizer side-effect the skill warns about, and all ten were fixed on merge. Four counter-proposals were also applied: the surface restored to the "Take action" heading, the non-parallel third bullet lifted out of the Search Analytics list, "a different chart" corrected to "chart type", and a lead sentence added to the tag section so the heading's promise is delivered in the first line rather than the last.

**Tag terminology settled by screenshot, 2026-09-24.** The column is Tag Search, the filter popover is headed Tags, and the field inside it is Search tags. The draft had used "Tags column" in one sentence and now uses Tag Search throughout. Each tag in the list carries a count of the listings it holds; that detail was added to the draft from the same screenshot.

**No `[confirm: ...]` markers remain. Every fact in the draft is sourced.**

Three were opened during the rewrite and all three were resolved by Tara on 2026-09-23:

- **The Filters tab search field.** The control has no product name; "Filter Filter" is an internal team nickname and the field searches filter names and their values. The draft names neither the nickname nor a label the control does not have, and says what the field does instead.
- **Keep and Hide in the Actions menu.** Confirmed present by the September Actions screenshot.
- **Whether the Location column can be removed.** Tara's answers 5 and 11 conflicted; she confirmed answer 5. Location and Status can be reordered but not removed, and the draft states it as what the member keeps rather than as a bare deficit: every listing keeps its address and status on screen whichever template is applied. The greyed checkbox on Location in the September screenshot is the constraint rendering correctly.

**Corrections this rewrite found that outlive it**

Four labels are wrong in the live article, and three of them are wrong in sibling articles too. Ruling on where this backlog lives is still owed.

| Wrong label | Actual | Also wrong in |
|---|---|---|
| "Filter Filter" | an internal team nickname for a control that has no product name; the field searches filter names and their values. Confirmed by Tara, 2026-09-23. The house standard bans internal terms the member cannot see | Create a Search with Filters, Getting Started in Perchwell, Run a Basic Search |
| "the Unhide icon" | an unlabelled crossed-out eye icon with a hidden count | Search FAQ calls it "the eyeball icon", closer but still not the label |
| "Flood Zone" | Flood, a toggle beside Parcels, under the Roads / Terrain / Satellite base styles | Customize Your Search View has "Roadmap", "Flood layers", "Parcel layers" |
| "Click Save" for a column template | Update and Save New | Customize Your Search View has Save New and is correct |
| "Trends" as a chart category | Median | |
| "Share via Messenger" | Share via Message, in the Actions menu | |
| "the Analytics view" | Search Analytics, the product's own name for it, used in the empty-state panel and in Analytics FAQ | |

**The Actions menu has changed since the July 2026 capture,** which is why this article names it rather than listing it. Tag and Share via Email are no longer separate items; both now sit inside the Share modal, whose tabs are Email, Text, Tags, and Public link. Share via Text, Driving Directions, and Print are new. Multi-Listing Actions on the Search Page owns that menu and needs the same check.

**Live-article defects, separate from this rewrite**

The stored article carries four links a Baldwin member cannot use: two to internal Notion pages (`app.notion.com/p/1d88b9e0…` for column templates, and `…/2ef8b9e0…` with the link text "here"), and two to a different help center (`intercom.help/perchwell/en/…` for Export and Analytics). Found with `get_article`; the mirror does not show them.

**Default help center links in the new draft**

Six of the twelve outbound links point at `/en/` rather than `/baldwin/en/`, because that is the canonical URL Intercom holds for those articles: Customize Your Search View, Share Multiple Listings in Perchwell, Export Listings in Perchwell, Manage Your Saved Searches, and Share and Export Analytics Charts. All to be confirmed at transfer.

**Media**

- No video. Tara confirmed 2026-09-23 that Arcade is retired and Looms will be recorded, so the old Arcade embed was dropped and a video placeholder stands in its place.
- Three screenshot placeholders. Tara's screenshots of the tag flow and the confirmation card contain real contact names and a real street address and must be cropped or re-shot before upload. No identifiers were carried into this file or the draft.

**Decisions taken, 2026-09-23**

- The Mobile twin (14786263) will be rewritten separately, at a later date. Until it is, the title collision stands and Retrieval signals check 1 stays failed. This is a known, accepted cost of keeping the familiar title on the article members land on.
- The four broken links in the live article are flagged to Kelly rather than fixed in this rewrite.

**Decision still owed**

- Where the label-correction backlog above is recorded. It spans at least four live Baldwin articles and outlives this rewrite.
