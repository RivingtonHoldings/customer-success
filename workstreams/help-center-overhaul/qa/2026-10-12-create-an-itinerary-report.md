# QA: Create an Itinerary Report

- **Article name:** Create an Itinerary Report (title unchanged)
- **Sources:** old Notion page https://app.notion.com/p/25a8b9e0143880c7aa1fcac7946b6a4c; Intercom article ID 8955772, content ID 9099068; mirror paths `docs/help-center/baldwin/create-an-itinerary-report.md` and `docs/help-center/crmls/create-an-itinerary-report.md` (shared article, identical bodies, checked against `get_article` October 12, 2026)
- **Product evidence:** frames of the live Arcade walkthrough (recorded March 12, 2026, edited July 17, 2026): the Select Report Type step, the Itinerary Details and Listings screen, a listing open with Appointment Time, Notes (45 / 400), and Include map, the report details screen, and the Generate Report step. Teammate screenshot of the report details screen, October 12, 2026. Teammate answers the same day: no Itinerary from a Tag, no Itinerary from the Listing Detail Page, the client name prints as "Prepared for" in the report header, Itinerary reports appear in the Report library, keep the video
- **Scored by:** Claude for Kevin, October 12, 2026
- **Scorecard:** September 10, 2026 set, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | "the itinerary editor" named no screen; now the Customize Report step |
| 2 visual_content_text | Pass | Pass | Live article has no images; placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | Itinerary Details fields, report details, and link options are labeled lists |
| 5 query_answer_symmetry | Fail | Pass | Bare "Email", "Print", "Download", "Tips", "Tour schedule" headings replaced |
| 6 self_contained_sections | Fail | Pass | "After the itinerary editor opens" and "After you review" openers removed |
| 7 audience_specification | Pass | Pass | No role gates the workflow |
| 8 entity_distribution | Fail | Pass | Feature name now in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening |
| 12 instruction_completeness | Fail | Pass | Search steps, Print, and Download now end with the outcome |
| 13 limitations_workarounds | Fail | Pass | Description promised Tags with no route; Tag listings now routed through the MLS ID filter |
| 14 numerical_clarity | Pass | Pass | Notes limit of 400 characters added |

## Plain language gate

Pass. No term from the do-not list. "Itinerary", "Create a Report", "Prepared for", "Include map", and the nine detail checkboxes are on-screen labels. "Itinerary editor" and "tour stop details" from the live article are gone.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 | 30.0 | +21.4 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 6.3 | 10.0 | +3.7 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| **Total** | **39.9** | **100.0** | **+60.1** |

Old band: Not retrievable as written. New band: Fin-ready. No `[confirm: ...]` markers remain.

Old failures: description in the "In this article, you will learn" form at 165 characters and promising a Tags route the article does not have; no "Use this article to" opening; H1 used for sections; bare headings; section openers depending on the previous section; feature name missing from the sharing sections; sharing order in the description (Email, Download, Print) crossing the sections (Email, Print, Download); Tips restating the map toggle; Search steps and Print and Download ending without an outcome; no defaults stated; PDF undefined; one step combining sub-bullets; bold throughout; horizontal rules; "Use an Itinerary report" and "Use this option".

The live labels were stale as well as the form: "Appointment Date", "Prepare For", "map view", "Open in Perchwell", and the "Include ..." checkbox names do not match the screen. The Arcade's own frames settled every one.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I make an itinerary for a showing tour? | Partly; stops at Select Itinerary | Yes |
| Can I create an itinerary from a tag? | No; promised in the description, never answered | Yes |
| How do I add appointment times to each house on the itinerary? | Partly; labels stale | Yes |
| Can I put my client's name on the itinerary? | Partly; "Prepare For" label wrong, header result not stated | Yes |
| How do I take the map off one listing in the itinerary? | Partly | Yes |
| Does my client get a copy when I email the itinerary? | Yes | Yes |
| What's the default subject line on the itinerary email? | No | Yes |
| Where do I find an itinerary I already made? | Partly; one line under Tips | Yes |

## Open items

- Resolved October 12, 2026 by the teammate: 7 of 9 details are selected by default (Agent name and Agent phone number clear); Brokerage, Agent name, and Agent phone number show the listing brokerage's name and the listing agent's name and phone number, confirmed against a finished report
- Unknown whether Perchwell remembers the last detail selections for Itineraries, as it does for Show Sheets; the draft says nothing
- Include map selected by default is read from the Arcade frame captured before the recorder touched the listing
- Tags: no Itinerary from a Tag or from the Listing Detail Page, confirmed October 12, 2026. The old Notion page's "Start from Tags" section (footer action bar, all Tag listings included) is stale and was not carried. The live description still promises Tags until this article is ported
- Video: kept by the teammate. The Arcade's click script mentions "the action bar at the bottom"; its frames show Actions in the upper right, which matches today
- Arcade privacy flag: its frames show a saved search named with two first names in the Search page header. Raised October 12, 2026; the teammate chose to leave it
- Shared article: the same Intercom record sits in the Baldwin and CRMLS Reports collections. Row set to MLS/AOR Baldwin and CRLMS All, matching the other report rows
- Screenshots: the report details capture is saved at `outputs/drafts/images/2026-10-12-itinerary-customize-fields.png`, no member names. A capture of a finished Itinerary report (the sample report the old row asked for) is in the git-ignored `confidential/` folder because it shows a listing agent's name and brokerage; blur them before placing it. The listing-edit screen (Appointment Time, Notes, Include map) still needs a capture
- The live Search Page Overview lists "CMA, Listing, or Itinerary report" under Create Report; no change needed
