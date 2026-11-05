# QA: Find Familiar Features by Their Perchwell Names (CRMLS)

Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-04-find-familiar-features-by-their-perchwell-names-crmls.md`. First article of the CRMLS Then vs. Now collection, mirrored from the Baldwin article of the same title (Baldwin record 14459704). Source for every term: the Matrix doc "External Then vs Now: CRMLS Matrix → Perchwell". Tracker ID: TRK-129 (next free number at Tara's direction, added to the master sheet Nov 4, 2026; Tara will confirm the numbering with the team). Notion row name carries a "(CRMLS)" suffix for now, to be removed at port if the team keeps the plain title.

## Checks run

- Title, description (124 characters), opening ("Use this article to ..."), H1/H2 levels, table intro sentences, "For more information:" lists for three or more links: pass.
- No em dashes, horizontal rules, bold, "you can", or banned plain-language terms: pass (one "you can" was found and removed).
- Legacy platform named (Matrix, OneHome), allowed for Then vs. Now: pass.
- All 14 doc terms placed: Power Bar, Search Criteria, Narrow / Discard, Display, Add/Edit, Supplements, External Links, Township, Market Watch, Stats tab, Auto email, Carts, OneHome, MLS Touch.
- 14 golden questions and the Fin-readiness score: not run. The draft carries 8 confirm markers, so it is not ready to score until they are resolved. A reviewer pass is still needed.

## Differences from the Baldwin article, on purpose

- Four tables instead of five: Matrix has only one mobile term, so mobile joins client collaboration.
- No Perchwell-only rows (Class, Active New Construction, CRS Autofill, Roster, About Me Page, Help): the doc has no Matrix equivalents. Not invented.
- Baldwin's Listing tools table is about partial and duplicate listings; CRMLS has no listing entry in Perchwell, so its table is Add/Edit, Supplements, External Links, Township.

## Open items (resolve before Ready to Transfer)

| Marker | Question | Notes |
|---|---|---|
| V9 | Is the Matrix feature Power Bar or Power Search? | The doc's terms table says Power Bar; its search rows say Power Search. One term per row |
| V8 | Is the CRMLS Universal Search Bar's Search field in the top navigation? | Doc says "Universal search, the Search field in the top navigation"; Baldwin says upper right. Draft uses the doc's location and the product name Universal Search Bar |
| V1 | Does Add/Edit stay in Matrix for every CRMLS association? | The doc's own marker |
| V8 | Where does Documents (Supplements) appear in Perchwell? | Doc gives only the name |
| V8 | Is it the Integrations sidebar or panel? | Baldwin and the Integration Tools article may say panel; the doc says sidebar |
| V8 | Where do Market Analytics, Search Analytics, and Market Activity open? | Doc gives names only |
| V8 | What does Workspaces refer to for Tags? | Doc writes "Tags (Workspaces)"; no other source |
| Link | Link to the CRMLS What Changed article and the CRMLS Listing Field Changes article | Neither exists yet; add when written |

## Inferences to confirm with a CRMLS screenshot

Written from Baldwin's Perchwell behavior, not the Matrix doc. The doc only gives the Perchwell name for these.

- Search Criteria: set on the Filters tab of the Search page (a CRMLS article already mentions the Filters tab).
- Narrow / Discard: Keep and Hide are options for selected listings in search results.
- Display: the Columns menu above search results.
- Township: wording "which appears under subdivision and complex" is the doc's phrase, lightly edited; confirm the Community field's location.

## Links to repoint before port

These point at Baldwin because no CRMLS public record exists yet (draft or unwritten). Run the link pass once CRMLS records exist.

- Add a Hot Sheet to the Dashboard (Baldwin 13893409; CRMLS draft 18232986)
- Tags Page Overview (Baldwin 14465546; CRMLS draft 8955795)
- Accept Your Agent's Perchwell Invitation (Baldwin 15521326; CRMLS draft 18231917)

Back-links to add when the other collection articles exist: What Changed, Listing Field Changes, Find OneHome Features in the Perchwell Client Portal (from the OneHome row).

## Fin test questions

1. What is Power Bar called in Perchwell?
2. Where did my Matrix Carts go in Perchwell?
3. What replaces Market Watch in Perchwell?
4. What is Narrow / Discard in Perchwell?
5. Can I still add or edit listings in Perchwell? (expected: keep using Matrix, pending V1)
6. What is the Perchwell version of MLS Touch?

## Review results, Nov 4, 2026

Scored by Claude against `docs/standards/fin-readiness-scorecard.md` (check set revision 2, plain language gate), after the draft-quality pass in `.claude/skills/article-rewrite`. Self-scored, so a second reviewer's read is still pending. New article: no old score to compare.

### Golden questions

| Factor | Result | Note |
|---|---|---|
| 1 disambiguation | Pass | No "this screen", "above", or emoji pointers. |
| 2 visual_content_text | Pass | No images; nothing to describe. |
| 3 undefined_terms | Pass | Abbreviations defined at first use after review. |
| 4 structured_enumeration | Pass | Steps and sequences are numbered; sets are bulleted or tabled. |
| 5 query_answer_symmetry | Pass | Headings name what each section answers, per the house reading of factor 5. |
| 6 self_contained_sections | Pass | No dependence on earlier sections; navigation named where a step needs it. |
| 7 audience_specification | Pass | Open to all members; Notion Roles is All. Silence is correct. |
| 8 entity_distribution | Pass | Feature and product names repeat in each section. |
| 9 semantic_chunk_boundaries | Pass | One topic per section. |
| 10 restate_questions | Pass | Every table has an intro sentence. |
| 11 overview_jtbd | Pass | "Use this article to ..." opening. |
| 12 instruction_completeness | Pass | No procedure beyond the outcome sentences. |
| 13 limitations_workarounds | Pass | Gaps are stated once with the route forward, or marked. |
| 14 numerical_clarity | Pass | Exact numbers or a marker for unknowns. |

All 14 pass as drafted, with confirm markers still open. Markers must clear before the row moves to Ready to Transfer.

### Plain language gate

Pass. The "entry" in "listing entry" and "above" in "above your search results" are the product's own sense, not the banned one.

### Dimension scores (new article)

| Dimension | Checks passed | Score |
|---|---|---|
| Retrieval signals | 7 of 7 | 30.0 of 30 |
| Chunk independence | 6 of 6 | 25.0 of 25 |
| Answer completeness | 7 of 7 | 25.0 of 25 |
| Fin-parsable formatting | 8 of 8 | 10.0 of 10 |
| Accuracy and confidence | 5 of 5 | 10.0 of 10 |

Total 100.0 of 100, band Fin-ready. The score does not count open confirm markers against accuracy, so it will not move when they clear.

### Changes the review made

- No changes needed; the review found nothing to fix.


## Aligned to Baldwin, Nov 4, 2026

Description reworded to follow the Baldwin article's wording, with Matrix terms swapped in and only enough added to reach 120 characters. Opening and headings were already close to Baldwin's.

## Reviewer input considered, Nov 4, 2026

The reviewer's description ("Find the Perchwell equivalents of familiar Matrix features, including Carts, Power Bar, Market Watch, and Search Criteria.", 122 characters) passed the length rule and was applied, then reverted at Tara's direction in favor of the Baldwin-mirror wording below (124 characters). Reasons: "Perchwell name" is the term the title, headings, and column header already use; the reviewer's version nearly restates the title; and "and more" fits an article with 14 terms. The reviewer's two-sentence opening was not applied: it does not use the "Use this article to" form, it restates the description, and its "see ..." link sentence is the link filler the standard replaces with "<Article> explains how ...".

## Markers resolved, Nov 5, 2026

- Add/Edit (V1): Tara confirmed no one enters listings in Perchwell for CRMLS. The row stays in the table so the Matrix term has a home; marker removed.
- Integrations (V8): the Matrix External Links tool is the Integrations panel, the name Baldwin's Dashboard articles and the CRMLS Dashboard Overview draft use. Marker removed; location added from the Dashboard Overview draft.
- Still open: Power Bar or Power Search (V9), the Documents location, where Market Analytics, Search Analytics, and Market Activity open, what Workspaces refers to, and the two link markers.

- Power Bar (V9): Tara confirmed the Matrix term is Power Bar. Marker removed. The doc's "Power Search" in its search rows is Paragon's term and is not used.

## Markers resolved, Nov 5, 2026 (screenshot and Tara)

- Documents (V8): Tara's screenshot shows Documents as a tab in the same tab strip as Mortgage & Tax (Overview, Listing Details, Property Details, Rooms, Features, Map, Auction Information, Documents, History, Mortgage & Tax), with a table of Type, Visibility, File, and Uploaded. The screenshot is Search page Preview; the row says Listing Detail Page because Baldwin's glossary places Mortgage & Tax, in the same strip, on the Listing Detail Page. Marker removed.
- Workspaces (V8): Tara confirmed Workspaces is the same as Tags. The row now reads Tags; the "(Workspaces)" alias was dropped as redundant. Restore "also called Workspaces" if members know Tags by that name.
- Still open: where Market Analytics, Search Analytics, and Market Activity open, and the two link markers.

## Marker resolved, Nov 5, 2026: Stats tab

Tara supplied where each one lives: Market Analytics is the Analytics tab in the top navigation and opens the Analytics Dashboard; Search Analytics is inside a search and adds charts to the search; Market Activity is a report inside the Analytics tab. The Stats tab row now says so and the marker is removed. Check later: Baldwin's Analytics Page Overview description lists Market Analytics beside Market Activity and the rankings, as if it were a report on the Analytics page, not the page itself. Tara's wording governs here; confirm the two articles agree when either is next reviewed. Still open on this article: the two link markers (What Changed, Listing Field Changes).

## Reviewer edit considered, Nov 5, 2026: Stats tab row

Tara's shorter cell applied with two changes. Kept: the three names and their one-phrase locations (the tighter form, which loses the Analytics Dashboard name and the top navigation location, both still in Tara's earlier note and in the Analytics Overview link under the table). Changes: (1) parentheses became commas and semicolons, the appositive form every other row in the four tables uses ("Property Type, a Quick Filter ..."); (2) "within Search" became "within a search", Tara's earlier phrasing, because Search is also the page name and the article means the open search. If a member should see the Analytics Dashboard name or that the tab is in the top navigation, restore it from the previous version of this row.

## Markers resolved, Nov 5, 2026 (Tara's answer and two screenshots)

- Township row updated to match Listing Field Changes: Community is a section of the Filters tab with the Subdivision name and Subdivision name other fields. Replaces the doc's "under subdivision and complex".

## Row name, Nov 5, 2026

The "(CRMLS)" suffix was removed from this article's Notion Article Name at Tara's request, so the row now carries the exact article title for the port. The master sheet's title columns were not changed.

## Synced from Notion, Nov 5, 2026

Notion was ahead of the repo. Kelly is the Article Reviewer on all nine rows, Article Due is Nov 12, 2026, Article Status is Ready to Transfer, and Roles is All Except Client, all set by Tara or the team. Article Review Status is still Not Started; the CRMLS port needs Review Finished or Complete. No screenshots on this article.
