# QA: Add Charts to the Analytics View on Search

- Article name: Add Charts to the Analytics View on Search
- Old title: Analytics Tab Walkthrough (Baldwin only, Analytics / Analytics Tools collection)
- Sources: live Intercom article 17453999, content ID 22673263 (read with `get_article`, last updated October 8, 2026); mirror `docs/help-center/baldwin/analytics-tab-walkthrough.md`; Tara's four Charts window screenshots (November 17, 2026), used as context for accuracy, not as article images. No old Master Article List row and no row in the Help Center Database existed for this article.
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-17-add-charts-to-the-analytics-view-on-search-rewrite.md`
- New Notion page: https://app.notion.com/p/41c8b9e0143881a88faadd8d58f1778f (created November 18, 2026, Draft; due dates left empty)
- Scored by Claude for Tara, November 17, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Old images had no alt text and the steps led into them with a trailing colon. New placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | DOM defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old headings were bare nouns ("Chart setup", "Chart creation") |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the view; Notion Roles is All Except Client, matching Analytics FAQ |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables in the new version |
| 11 overview_jtbd | Pass | Pass | |
| 12 instruction_completeness | Fail | Pass | Old steps stopped at "Choose a chart type"; nothing is added until Update Dashboard |
| 13 limitations_workarounds | Fail | Pass | 8-chart limit now stated with the route forward (Analytics FAQ) |
| 14 numerical_clarity | Pass | Pass | 8 charts, 4 categories, chart counts per category |

## Plain language gate

Pass on the rewrite. No do-not-list terms. Charts, Update Dashboard, Already added, Market Share, Distribution, Location, Median, and the chart names are on-screen labels of controls or chart options. "DOM" is a chart label and is defined on first use as days on market.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 | 30.0 | +25.7 |
| Chunk independence (25) | 16.7 | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 2.5 | 10.0 | +7.5 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 43.8 | 100.0 | +56.2 |

Old: Not retrievable as written. New: Fin-ready, 14 of 14 golden questions, plain language gate passed.

Old failures: title is a bare noun next to Analytics Page Overview; description in the "In this article, you will learn" form; no "Use this article to" opening; headings are bare nouns and the first sentences do not echo them; the opening bullets do not match the sections; H1 used for every section; steps stop before Update Dashboard; no 8-chart limit; no defaults; bold on UI elements and a bold emoji callout; horizontal rules; images with no alt text; wrong Market Share and Median descriptions.

## Source differences

| Item | Live article | Screenshots and siblings | Decision |
|---|---|---|---|
| Market Share | "amenities and feature availability" | Two charts only: Bedrooms, Price (Tara confirmed) | Screenshot wins; live description dropped |
| Median example | "price per square foot or price per bedroom" | No per-bedroom chart; Price per SqFt and Price per Acre exist | Screenshot wins |
| Final step | Stops at "Choose a chart type" | Update Dashboard adds the selected charts | Step added |
| Where to click | "Switch to the Listings view", then "View ribbon" | Search Page Overview and Analytics FAQ say the Results tab and "Analytics next to View"; Tara's screenshot shows Results highlighted | Results tab used; see open items |
| Button name | "+ Charts" | Screenshot shows Charts with a plus icon; Search Page Overview says Charts | "Charts" used |
| Last overview bullet | "Add charts to Reports or Market Analytics" | Not in any sibling or screenshot | Dropped; see open items |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I open Analytics on the Search page? | Yes | Yes |
| How do I add a chart to my search results? | Partly, no Update Dashboard step | Yes |
| What charts are in the Market Share category? | No, wrong description | Yes |
| Is there a price per acre chart? | No | Yes |
| Why can't I select a chart in the Charts window? | No | Yes |
| How many charts can I add to Analytics? | No | Yes |
| What is the difference between the Analytics page and the Analytics view? | No | Yes, via link to Analytics FAQ |
| What does the Location category show? | Partly | Yes |

## Open items

1. **Results tab or Listings view.** The live article says "Switch to the Listings view"; two sibling drafts and Tara's screenshot point to the Results tab. Confirm the live label is outdated.
2. **Purpose lines carried from the live article.** Distribution ("spread across a range") and Location ("across areas") come from the live descriptions, which were not contradicted but not rechecked against the charts. Market Share and Median lines are built only from chart names. Confirm all four read right.
3. **"Add charts to Reports or Market Analytics"** (live opening bullet) is not in any sibling article or screenshot, so it was dropped. Confirm whether it is still true; if so it needs its own sentence or a link.
4. **Naming across the set.** Resolved November 18, 2026: Tara chose "Analytics view". The Search Page Overview section was trimmed to a sentence and a link and now uses that name; two CRMLS Then vs. Now rows were updated too. The live articles, the mirror, and a few other pages (Customize Your Search Results View, Find Familiar Features by Their Perchwell Names, Common Perchwell FAQs, Appraiser Capabilities in Perchwell) still say "Search Analytics" until checked and ported.
5. **Links to the old title.** Analytics FAQ and Analytics Page Overview, both Live in Intercom, link to "Analytics Tab Walkthrough". Analytics FAQ also calls the button "+ Charts". Update both when this article ports. The article's Intercom URL stays the same.
6. **Legacy name.** No legacy name for the Analytics view is known, so the legacy-platform sentence is omitted. Confirm none exists.
7. **Tracker ID.** TRK-003 is inferred (Analytics FAQ is TRK-001, Analytics Page Overview is TRK-002, alphabetical by live title) and not verified in the master sheet.
8. **Video.** Loom 956e4116 confirmed accurate by Tara on November 17, 2026. Video Status Baldwin is set to Complete as an assumption.
9. **CRMLS.** Resolved November 18, 2026: CRMLS has five categories (adds Trends) and different chart names, so it has its own row, "Add Charts to the Analytics View on Search (CRMLS)", TRK-004. See the QA file for that row.
10. **Screenshot placeholders.** Two Baldwin placeholders. The View ribbon screenshots in the live article are signed Intercom links that expire, so they were not carried.
