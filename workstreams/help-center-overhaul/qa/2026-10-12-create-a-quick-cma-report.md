# QA: Create a Quick CMA Report

Title unchanged: Create a Quick CMA Report.

Sources:
- Intercom article 13959293, content 16237971, shared through the Reports collection in both help centers (collection 17797980 in Baldwin, 16867011 in CRMLS)
- Mirror: `docs/help-center/baldwin/create-a-quick-cma-report.md` and `docs/help-center/crmls/create-a-quick-cma-report.md`, identical bodies. The mirror last synced September 29, 2026, so the live body was read fresh with `get_article`
- Old Notion page: https://app.notion.com/p/25a8b9e0143880c4b9dfdaa625e6320e (Baldwin row; two more old rows cover CRMLS)
- The three live screenshots (Intercom CDN, about March 2026), read at full resolution: the Search Actions menu, the Select Report Type step, and the Customize Report fields screen. No member names or emails in any of them
- Teammate screenshots, October 12, 2026: the Customize Report listings screen, the layout and fields screen (two captures), and the Generate Report step
- Product answers from the teammate, October 12, 2026: Quick CMA appears after Actions, then Report on the Listing Detail Page; in a listing preview, Quick CMA is not directly in Actions and Actions acts on all selected listings; no Create Report on a Tag; Portrait and Landscape both exist and the field cap changes with orientation; no report title or subtitle; default subject Comparative Market Analysis; swap the video for a placeholder
- Set read from the new database (Reports): Create a Listing Report, Create a Show Sheet, Create a CMA with a Subject Property, Create a Market Conditions Addendum Report (1004MC), all Draft

Scored by Claude for Kevin Liang, October 12, 2026. Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Three live images had no alt text; every placeholder now carries alt text |
| 3 undefined_terms | Fail | Pass | CMA, OLP, DOM, CDOM, and PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Email", "Download", "Print", "Quick CMA Creation" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the workflow; Roles property records All Except Client |
| 8 entity_distribution | Fail | Pass | Every section names the Quick CMA |
| 9 semantic_chunk_boundaries | Fail | Pass | Tips list mixed navigation, Report library, and search; split into their sections |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Creation and email steps end with the outcome |
| 13 limitations_workarounds | Pass | Pass | Field cap and missing-detail behavior stated where the member meets them |
| 14 numerical_clarity | Pass | Pass | Portrait cap of 9 and Landscape cap of 12 exact; Landscape confirmed by Kevin October 13, 2026 |

Old: 7 of 14. New: 14 of 14.

## Plain language gate

New: pass. No term from the plain language do-not list. "Use" appears only in "Use this article to" and the "When to use" heading. "Report library", "Subdivision/Condo", "HOA/YR", and the link option labels are exact on-screen labels.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3 of 7) | 30.0 | +17.1 |
| Chunk independence (25) | 8.3 (2 of 6) | 25.0 | +16.7 |
| Answer completeness (25) | 10.7 (3 of 7) | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 2.5 (2 of 8) | 10.0 | +7.5 |
| Accuracy and confidence (10) | 6.0 (3 of 5) | 10.0 | +4.0 |
| Total | 40.4 | 100.0 | +59.6 |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed, with open confirm markers below.

Old failures:
- Description over 140 characters, opens "In this article", and ends in a typo (".ui")
- No opening paragraph; section headings at H1
- Bare-noun headings ("Email", "Download", "Print") with no feature name or echo
- CMA never defined
- Listing Detail Page and Tags steps stop at "Select Quick CMA"
- Exact-address fact stated three times (a step, a note, and Add optional sections); the remove X stated twice
- No links to Create a CMA with a Subject Property or the Report library
- Bold UI labels, an unlabeled "NOTE:" callout, an emoji tip, horizontal rules, images with no alt text
- "You can", "Use this option"
- Wrong facts, all confirmed against current screenshots: Add to Report on the Listing Detail Page, a Tags page route, a separate "CMA editor", report title and subtitle fields, Portrait capped at 8 fields, a 15-field list missing OLP, CDOM, List Date, Sold Date, Subdivision/Condo, and Price Per Acre and carrying the retired Status Date and List/Sold, "agent contact information" for what is the member's own, a "Select Email" step

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I make a quick CMA? | Yes | Yes |
| Can I create a CMA from a listing page? | Yes, with a button that does not exist | Yes |
| How do I add listings from a tag to my CMA? | Yes, with a route that does not exist | Yes |
| How many fields can I show on a CMA? | Partly, with the wrong Portrait number | Yes |
| Can I add CDOM to my CMA? | No | Yes |
| How do I add a subject property to a quick CMA? | Yes | Yes |
| Why aren't the addresses in my CMA clickable? | Partly, inside a numbered step | Yes, the Tip |
| Where do I find a CMA I already sent? | No, one Tips bullet | Yes |

## Open items

- Resolved October 13, 2026: Landscape allows 12 fields per listing (Kevin). The live article says 10 and is wrong.
- [confirm: whether a Next click follows selecting Quick CMA, as it does for a Show Sheet]
- [confirm: what the Add Subject Property window asks for, and whether it also finds listed properties]
- [confirm: selecting a Tag adds all of its listings, and more than one Tag can be selected]
- [confirm: what Include summary section shows]
- Email Report is grayed out in the screenshot while the To field is empty. The draft does not state when it becomes available; confirm if members ask.
- Field list is a plain bullet list with abbreviations defined, not a labeled list. Each field only adds that detail to every listing, so a sentence per field would restate the label. Reviewer's call.
- Shared article: one row carries both Baldwin and CRLMS All, per the September 17, 2026 rule. The Create a CMA with a Subject Property link points into the Baldwin help center; flag at port for CRMLS readers.
- Video: both Arcade links (live `demo.arcade.software/nbB5nnBrlab5j5Ez0mXt`, old Notion `app.arcade.software/share/PzRDwfoLY5TWwpkv8gWd`) replaced with a placeholder at the teammate's request, since they predate the current flow.
- Screenshots: the live Search Actions menu and Select Report Type images are not reused (the picker predates the 1004MC report). The October 12, 2026 captures are saved in `outputs/drafts/images/` as `2026-10-12-quick-cma-*.png`. The listings capture shows a public listing address; crop it before port if the team prefers.
- Set consistency, not edited from this session:
  - The Create a CMA with a Subject Property draft says "In a listing preview on the Search page, click Actions, then select Quick CMA." The teammate confirmed Quick CMA is not directly in Actions, and Actions acts on all selected listings. That sentence needs correcting.
  - The Create a Listing Report and Create a Show Sheet drafts describe a single Emails field on the Generate Report step. The Quick CMA Generate Report step has To, CC, and BCC fields and an Include signature on shared report checkbox. Either the step differs by report type or those drafts were written from older screenshots; check.
  - The Reports FAQ lists Quick CMA fields with the same stale 15-field list and should be updated when it is migrated.
