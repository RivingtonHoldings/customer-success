# QA: Listing Detail Page Overview

- Article: Listing Detail Page Overview (title unchanged)
- Old Notion page: https://app.notion.com/p/27e8b9e0143880b68605f5a239b02e4f (Master Article List, read only)
- Intercom article ID 14074994, content ID 16398662
- Mirror: `docs/help-center/baldwin/listing-detail-page-overview.md`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-listing-detail-page-overview-rewrite.md`
- Notion: https://app.notion.com/p/3f88b9e014388166b58cd03802c85489 (Draft, created October 13, 2026)
- Scored by Claude for Kevin Liang, October 13, 2026, against scorecard check set revision 2
- Product answers: Kevin Liang, October 13, 2026, with screenshots of History, Mortgage & Tax, and the tabs and photo gallery

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old: "see Showings below" |
| 2 visual_content_text | Fail | Pass | Old: four images, no alt text |
| 3 undefined_terms | Fail | Pass | CMA and BCAR defined; CRS, RPR, ShowingTime, and InfoSparks are integration names |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old: "Listing Header", "Integrations", "Sale Data" |
| 6 self_contained_sections | Fail | Pass | Old: "Then, scroll down" |
| 7 audience_specification | Pass | Pass | Agent Only and own-listings limits stated where they apply |
| 8 entity_distribution | Fail | Pass | Every section lead names the Listing Detail Page |
| 9 semantic_chunk_boundaries | Fail | Pass | Old: Documents steps inside the tabs section; five H1s |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Fail | Pass | Old: Documents steps stop without an outcome |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Interest rate and Down payment starting values stated |

Old: 5 of 14. New: 14 of 14.

## Plain language gate

New: pass. No term from the do-not list. "tile" no longer used. "Listing Summary" and "Action Panel" removed because the product no longer has them. "MLS#" on the History screen is a readout and is not written.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 (1/7) | 30.0 (7/7) | +25.7 |
| Chunk independence (25) | 4.2 (1/6) | 25.0 (6/6) | +20.8 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| Total | 25.7 | 100.0 | +74.3 |

Old band: Not retrievable as written. New band: Fin-ready, gates passed.

Retrieval check 1 scored 95.7 until October 13, 2026, because the Mobile collection's article 14784837 has the identical title. Kevin Liang decided to retitle the mobile article to Listing Detail Page Overview in the Mobile App and keep this title, which lifts the score to 100.0. The pass holds only once that retitle lands: it must reach Intercom before or with this article's port.

Old accuracy failures: the Actions menu listed Print, One Pager, Add to Report, Auto CMA, and Edit Listing, and a Share submenu of Email, Text, Tags, and Public Link; the menu now reads Contact agent, Share, Send as in-app message, Share via Text, Report, Print one page report, Print full report, CMA Subject Property, Edit this listing, and Integrations. The Listing Summary panel, Similar Listings, the Change Log Details view, and the Showings card are no longer on the page.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where do I see a listing's price history? | Yes | Yes |
| How do I print a listing? | No, stale label | Yes |
| How do I report a listing with wrong information? | Yes | Yes |
| Can my clients see agent remarks on a listing? | Partly | Yes |
| How do I see all the photos for a listing? | No | Yes |
| How do I estimate the mortgage payment for a listing? | Yes | Yes |
| Where are the documents for a listing? | Yes | Yes |
| How do I edit my listing from the listing page? | No, stale label | Yes |

## Open items

- Replace now, not at port: the live Sale Data screenshot (August 17, 2026) shows full agent remarks with a person's name and phone number, and a selling team name.
- Resolved October 13, 2026 by Kevin Liang: BCAR spelled out as written; Property Details is one section of fields, not Interior, Exterior, Land & Lot, and Tax Information groups; the map type control is Map layers and Street View is still on the Map; Visible only to you keeps Lifetime mortgage payment off printed reports; Interest rate starts at 7% and Down payment at 20%; the grid icon has no hover label; floor plans and virtual tours show when the listing has them.
- Video: the Arcade (https://app.arcade.software/share/Qxza2lPVECHzhJvVNxPz) was recorded with the removed Listing Summary panel and the old Action Panel, and the old row marks it Update Required. Replaced with a video placeholder.
- Title collision, decided: retitle Mobile article 14784837 to Listing Detail Page Overview in the Mobile App before or with this article's port. Not started.
- Sibling claims now wrong: Listings FAQ and Common Perchwell FAQs both answer "How are similar listings determined on the listing details page?", and Similar Listings is no longer on the page. Listings FAQ also says other agents see open house remarks "in the Showings card and the Upcoming Showings dialog"; the Listing Agent card now shows only Email, the phone numbers, and the profiles.
- Repo copy of the integrations draft is titled Open Your MLS Integrations from the Dashboard; the Notion row reads Access Integrations from the Dashboard or a Listing. This draft links the Notion title.
- Links to One Page Report and Full Report use the draft titles; the live titles are Create One Page Reports and Create and Share Full Reports until those port.
- Roles: the old row had no Roles value; set to All Except Client, approved with the Notion create.
