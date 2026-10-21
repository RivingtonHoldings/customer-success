# QA: Create a Media Report

- **Article:** Create a Media Report (title unchanged)
- **Sources:** live Intercom article 8955781, content 9099077; mirrors `docs/help-center/baldwin/create-a-media-report.md` and `docs/help-center/crmls/create-a-media-report.md` (shared article); old Master Article List rows [Baldwin](https://app.notion.com/p/25a8b9e0143880a8a849efed4c91a49f) and [CRMLS draft](https://app.notion.com/p/3198b9e01438806f8de6f1e6c6a7269d); the live article's three screenshots; product answers from the teammate, October 12, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-12-create-a-media-report-rewrite.md`
- **Scored by:** Claude for Kevin, October 12, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Three images had no alt text; every placeholder now carries it |
| 3 undefined_terms | Fail | Pass | PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Media Report creation (Search)", "Media Report customization", "Media Report sharing" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gate; Roles property is All Except Client |
| 8 entity_distribution | Fail | Pass | Seven customization sections never named the Media Report |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | No opening paragraph; added "Use this article to ..." |
| 12 instruction_completeness | Fail | Pass | Create steps stopped before Next; share steps stopped at the click |
| 13 limitations_workarounds | Pass | Pass | 15-images-per-listing cap stated; add or remove listings routed to a new report |
| 14 numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. No do-not-list terms; every on-screen label named at the point of use.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting (10) | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **54.9, Needs rewrite** | **100.0, Fin-ready** | **+45.1** |

Old failures: description over 140 characters and "In this article" form; no opening; headings without the feature name or echo; multiple H1s; no outcome after steps; no defaults; PDF undefined; bold on every label; horizontal rules; no alt text; labels that contradict the live screenshots ("Select Email", Report Label, option names); "Use a Media Report".

Biggest accuracy finding: the live article documents six customization options (Report Label, link behavior, listing details, contact information, image types, layout) that the teammate confirmed are not on the Media Report's Customize Report step. Reordering listings is the only change it offers.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I create a media report? | Partly, stops before Next | Yes |
| Can I make a media report from a listing page? | No | Yes |
| How do I change the order of listings in a media report? | Yes | Yes |
| How many photos does a media report include? | No | Yes |
| How do I remove a listing from my media report? | No | Yes |
| How do I email a media report to a client? | Yes, with wrong labels | Yes |
| Where do I find a media report I made before? | No | Yes |

## Open items

- [confirm: whether each image prints on its own page]. Resolved October 12, 2026: the report takes the first 15 images from each listing's Listing Detail Page
- New screenshot needed of the Customize Report step for a Media Report; the live image shows options the step no longer has
- Generate Report image reused from the live article (default subject Media Report); confirm it is current when capturing the new Customize Report screenshot
- Shared article: one row with MLS/AOR Baldwin and CRLMS All, per the September 17 rule; cross-links point into one help center at port
- Roles set to All Except Client to match the Reports siblings; the old row had no role
- The CRMLS Guide to Creating a Report also lists Media Report and may need a pass when touched
