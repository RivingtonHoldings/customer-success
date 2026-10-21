# QA: Create a Show Sheet

Title unchanged: Create a Show Sheet.

Sources:
- Intercom article 8955767, content 9099063, shared through the Reports collection in both help centers
- Mirror: `docs/help-center/baldwin/create-a-show-sheet.md` and `docs/help-center/crmls/create-a-show-sheet.md`, identical bodies
- Old Notion page: https://app.notion.com/p/25a8b9e01438806ebf17ee25cc419fde (Baldwin row; a second old row covers NYC and CRMLS)
- The three live screenshots, read at full resolution, and four current screenshots from the teammate, October 12, 2026

Scored by Claude for Kevin Liang, October 12, 2026. Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Three live images had no alt text; every placeholder now carries alt text |
| 3 undefined_terms | Pass | Pass | DOM and PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Show Sheet creation", "Show Sheet customization", "Tips" replaced |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the workflow; Roles property records All Except Client |
| 8 entity_distribution | Fail | Pass | "Email the Report", "Choose how listing links open" now name the Show Sheet |
| 9 semantic_chunk_boundaries | Fail | Pass | Tips list mixed advice and system facts; split into their sections |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Creation steps now include Next and the outcome; email steps match the screen |
| 13 limitations_workarounds | Pass | Pass | Tags route and the 13-photo limit stated where the member meets them |
| 14 numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

New: pass. No term from the plain language do-not list. "Use" appears only in "Use this article to" and the "When to use" heading. "Floorplan", "DOM", and "Report library" are exact on-screen labels.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 | +21.4 |
| Chunk independence (25) | 12.5 (3 of 6) | 25.0 | +12.5 |
| Answer completeness (25) | 14.3 (4 of 7) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 5.0 (4 of 8) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 (3 of 5) | 10.0 | +4.0 |
| Total | 46.4 | 100.0 | +53.6 |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed, with open confirm markers below.

Old failures: description over 140 characters and opens "In this article"; no opening paragraph; bare-noun headings with no echo; description promises Tags with no section behind it; H1 section headings; Tips mixed topics; creation steps stop before Next; no defaults stated; bold UI labels and horizontal rules; three images without alt text; labels that no longer match the screen (Select Email, Open in Perchwell, Listing agent information, ten field checkboxes); "Use this option".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I make a show sheet? | Yes | Yes |
| Can I create a show sheet from a tag? | No, and the Tips list implies it works | Yes |
| Does the show sheet have a QR code? | No | Yes |
| Where did the neighborhood and transit options go on the show sheet? | No, the old list still shows them | Yes, the current field list |
| How many photos can I put on a show sheet? | No | Yes |
| How do I email a show sheet to my client? | Yes, with a wrong first step | Yes |
| Where do I find a show sheet I already sent? | No, one Tips bullet | Yes |
| How do I change a show sheet to portrait? | Yes | Yes |

## Open items

- [confirm: dragging sets the order the photos print in]
- [confirm: whether the Show Sheet starts with the listing's first 13 photos, whether a photo can be removed or swapped, and how photos work with more than one listing]
- [confirm: listings still reorder by dragging; the Customize Report instruction text no longer mentions it]
- [confirm: the Generate Report step is unchanged by the new Show Sheet release, and the default subject still reads Marketing Materials for Listing]
- Shared article: one row carries both Baldwin and CRLMS All. Links in the body can only point into one help center; there are none today.
- Set consistency with the Create a Listing Report draft: the teammate confirmed October 12, 2026 that Perchwell remembers the member's last selections, so that draft's "selected by default" lines need revising. Not edited from this session. That draft also says selecting Listing Report moves straight to Customize Report, while the live Show Sheet screenshot shows a Next button on the first step; still to check.
- The live customize screenshot is stale (ten field checkboxes); replace it at port with the October 12, 2026 capture. The live picker screenshot predates the Market Conditions Addendum Report and is not reused.
- Teammate screenshots show a staff profile photo and, in the profile menu capture, a staff name and the staff-only Stop assuming identity button. The teammate chose to use the full screenshots, October 12, 2026.
