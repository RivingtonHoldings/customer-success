# QA: Create a Listing Report

Old title: Create a Listing Report (unchanged)

## Sources

- Old Notion page (Master Article List, read only): https://app.notion.com/p/25a8b9e0143880948bf6eaf8783c8a8b
- Intercom article ID 8955755, content ID 9099049
- Mirror: `docs/help-center/baldwin/create-a-listing-report.md` and `docs/help-center/crmls/create-a-listing-report.md` (shared article). Stored body checked with `get_article` on October 9, 2026; it matches the mirror
- New Notion draft: https://app.notion.com/p/3f78b9e014388131a087de313201af98
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-12-create-a-listing-report-rewrite.md`
- Live screenshots (Intercom CDN, three images, the customize image from about March 2026): the Select Report Type step, the Customize Report step, and the Generate Report step. They corrected the Report Label field name and showed the 70-character Report Subtitle limit, the exact link and checkbox labels, and that the Generate Report step has no Email option to select
- Teammate screenshots, October 12, 2026: the current Customize Report step with the Listings section, and the profile menu with Report library
- Product answers from the teammate, October 12, 2026: no Tags route and no Add to Report on the Listing Detail Page; the Results tab is required; defaults per the screenshot; the Emails field takes multiple addresses; Print opens the browser dialog and Download saves a PDF; Report library sits in the profile menu, upper right; a 500-listing maximum
- Set read from the new database (Reports): no rows yet. Siblings read from the mirror only: Create a Show Sheet, Create an Itinerary Report, Create a Quick CMA Report

Scored by Claude with /article-rewrite on October 12, 2026, against the scorecard check set revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Three live images have no alt text; every placeholder carries it |
| 3 undefined_terms | Fail | Pass | CMA and PDF defined on first use; DOM already was |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Listing Report customization", "Steps:" at H2, and "Tips" replaced with task headings |
| 6 self_contained_sections | Fail | Pass | "After you select Listing Report" and "After you review your settings" leads replaced |
| 7 audience_specification | Pass | Pass | No role gate; Roles property records All Except Client |
| 8 entity_distribution | Fail | Pass | "Email the Report" and siblings now carry Listing Report |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Opening paragraph added |
| 12 instruction_completeness | Fail | Pass | Create, Print, and Download now end with what happens |
| 13 limitations_workarounds | Fail | Pass | The heading promised a Tags route with no section; cut. The 500 cap and "create a new report to add listings" stated where met |
| 14 numerical_clarity | Fail | Pass | 500-listing email threshold and 70-character subtitle limit added |

## Plain language gate

Pass. Checked and kept: Report Label, Report Subtitle, DOM, and the checkbox labels are control labels named where the member selects them. "Chip", the teammate's word for each address in the Emails field, was left out; agents would not say it.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| Total | 40.4 | 100.0 | +59.6 |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, no `[confirm: ...]` markers.

Old failures, in brief: no opening paragraph; headings without the feature name; a lead promising a Tags route with no section; H1 sections; dependent leads; Download, Print, and the create steps stopping at the last click; no defaults; bold throughout; an emoji callout; horizontal rules; no alt text; "Select Email" and "report title" contradicting the screen; "Use this option".

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I make a listing report? | Yes | Yes |
| How many listings can I put in a listing report? | No | Yes |
| Can I email a listing report to more than one person? | No | Yes |
| Will my client have to log in to see the listings in my report? | No | Yes |
| Where do I find a report I already sent? | Partly, a bare tip | Yes |
| How do I take a listing out of my report? | Yes | Yes |
| How do I change the title on my listing report? | Partly, called "report title" | Yes |
| Can I make a listing report from a tag? | No, the heading promised it | No; not supported, so the false promise is gone |

## Open items

- Resolved October 12, 2026: Report Subtitle fills in from the search filters; a report past 500 listings is emailed to the agent (written as a Note); there is no Tags route, since a Listing Report needs multiple listings selected at once.
- The live Create a Show Sheet and Create a Quick CMA articles both document Add to Report on the Listing Detail Page, which the teammate confirmed does not exist. Both need correcting.
- Shared article: one row with MLS/AOR Baldwin and CRLMS All. The separate CRMLS row in the old list, "CRMLS| Creating a Listing Report" (Transfer to Intercom), was not read in detail.
- Roles: the old row has no value; All Except Client is proposed.
- Screenshots: reuse the live Select Report Type and Generate Report images; capture a new Customize Report image with test listings and a cropped profile menu showing no name or photo.
