# QA: Export Listings to a CSV File

Retitled from "Export Listings in Perchwell" (live and old Notion row). Scored October 7, 2026 by Claude for Tara, against scorecard revision 2.

## Sources

- Old Notion page: https://app.notion.com/p/1d58b9e014388069a171f5c4b5d680f6 (Master Article List, read only)
- Intercom article ID 11776740, content ID 12887977, last updated July 2, 2026
- Mirror: `docs/help-center/baldwin/export-listings-in-perchwell.md` and `docs/help-center/crmls/export-listings-in-perchwell.md` (shared article, same body)
- Live article images: two copies of the same Export window screenshot, from before the window title showed a listing count. Labels still current: Quick export, Template, MLS Template (Master), Template Name, Set as default list, Search columns, Select all, Deselect all, Save as template, Export
- Tara's screenshots, October 7, 2026: one listing selected with the Actions menu open (Export CSV), the Export 1 listing window with a New Template form, a saved template with trash, copy, and Edit template controls, and the full field list split into Selected and Unselected
- Tara's answers on October 7, 2026: Export CSV exports only checked listings; select all covers listings in view, and the results load 30 more as you scroll; limit believed to be 5,000; the CSV downloads to the computer and is not emailed; templates are optional, one per kind of export; Export CSV is in every view; templates can be edited and deleted; search columns do not carry over to export templates
- Tara's second round, October 7, 2026: the select all checkbox in the header row (screenshot), the export limit left out of the article, Quick export fields can be selected, cleared, and reordered (screenshot), edit mode saves with Save template, delete asks for confirmation and cannot be undone (screenshot), Set as default list makes the template the default starting point, the copy icon saves Copy of [template name], MLS Template cannot be edited but can be copied, and the plus, trash, and copy icons have no hover labels
- Sibling articles checked: Search FAQ (exportable fields), Multi-Listing Actions on the Search Page, Key Workflow Changes, and the drafts Search Page Overview, Customize Your Search Results View, and Share Listings with Clients from Search
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-07-export-listings-to-a-csv-file-rewrite.md`
- Notion draft: https://app.notion.com/p/3f28b9e0143881e7ae22f09afa774206
- Revised October 7, 2026 with Tara's edit: "fields" for the export and "columns" for search results, "select" for templates in the Export window, Quick export or a template as a required step, the scope fact moved into the export outcome, and the Land and residential example cut. Eight fixes were applied on top of her edit: the description restored to 130 characters; a task-and-place export lead; Excel and Numbers restored; *(Optional)* on three steps; the field-list fact moved into the create lead; "you can" cut from the copy lead; the MLS Template route folded into its bullet; and two instructions tightened under 20 words. The scores below are for the revised draft and did not change

## Source differences and how they were settled

| Topic | Live | Old Notion | Settled by |
|---|---|---|---|
| Entry point | Export button, upper right of Search | Actions, then the Export icon | Tara's screenshot: Actions, then Export CSV, after selecting listings |
| Delivery | Emailed | Emailed, as a download link | Tara: downloads to the computer |
| Save button | Save Template | Save Template | Screenshot: Save as template |
| Template list label | Templates | Templates | Screenshot: Template |
| Window name | Panel and page | Panel and page | Screenshot title: Export 1 listing; called the Export window |
| App needed to open the CSV | Not stated | Excel, Numbers | Carried |
| MLS Template | Not stated | Click script: fields curated by your MLS | Carried, hedged as "set up by your MLS" |
| Use cases | Tips: any field, unlimited templates | Search columns, property types, periodic reports, appraisers | Tara: one template per kind of export, such as Land or residential; search columns are advice only |

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Old images had no alt text; placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | CSV defined in the opening |
| 4 structured_enumeration | Pass | Pass | Export window options are a labeled list |
| 5 query_answer_symmetry | Fail | Pass | Old headings: "Export panel access", "Quick Export", "Template creation" |
| 6 self_contained_sections | Fail | Pass | Old Quick Export section never said how to open the panel |
| 7 audience_specification | Pass | Pass | No role gate; silence. Roles property: All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with the outcome, including the Delete this template confirmation |
| 13 limitations_workarounds | Fail | Pass | Selected listings only, select all with scroll loading, MLS Template copy-then-edit, and deletion is permanent, each stated where the member meets it |
| 14 numerical_clarity | Pass | Pass | 30 listings per scroll |

## Plain language gate

Pass. No term from the do-not list. "Master" appears only as the badge the member sees next to MLS Template. "Excel" is added so members who type it can find the article.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: description is 180 characters and opens "In this article", no opening paragraph, bare-noun headings, no heading echo under Template creation) | 30.0 | +17.1 |
| Chunk independence (25) | 20.8 (5/6: sections at H1) | 25.0 | +4.2 |
| Answer completeness (25) | 7.1 (2/7: template creation ends at the click, Set as default list unexplained, no selection or limit constraint, CSV undefined, no related links) | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 5.0 (4/8: wrong labels in steps, bold throughout, no alt text, horizontal rules) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5: entry point and email delivery are out of date; "Use Quick Export") | 10.0 | +4.0 |
| **Total** | **51.8, Needs rewrite** | **100.0, Fin-ready** | **+48.2** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I export listings to Excel? | Partly; wrong entry point, no mention of Excel | Yes |
| I exported listings but never got an email. Where is my file? | No; says it is emailed | Yes |
| How do I export all of my search results? | No | Yes |
| Can I change the fields in the MLS Template? | No | Yes |
| How do I create an export template? | Partly; wrong button label | Yes |
| Why doesn't my CSV match the columns in my search results? | No | Yes |
| How do I edit, copy, or delete an export template? | No | Yes |
| What is the MLS Template in the export window? | No | Yes |

## Open items

- No confirm markers remain. The export limit (believed to be 5,000 listings) is left out of the article at Tara's call.
- Shared article: the live article sits in the Baldwin and CRMLS Search collections, so the row carries both MLS values. Its link points to a Notion draft; replace it with the live Baldwin URL at transfer.
- The Arcade (https://app.arcade.software/share/ESlHf9VUW6p2Kjeqenbe) and Loom (https://www.loom.com/share/f620e5612df448c4baf2a931f6cef546) on the old page show the earlier Export icon and email delivery, so the draft carries a video placeholder instead.
- Search Page Overview (draft) and Share Listings with Clients from Search link to this article by its old title and URL. Update them when this article is ported.
- Multi-Listing Actions on the Search Page (live, not yet migrated) does not list Export CSV in its Action Panel tables. Add it when that article is migrated.
- Appraiser Capabilities in Perchwell (live) calls the option "Export to CSV". Update it to Export CSV.
- Search FAQ (live) says "You can export any field". Fix the wording when it is migrated.
- The CRMLS article Export to Excel covers Create a Report, then Export to Excel, which is a different surface. Members may confuse the two.
