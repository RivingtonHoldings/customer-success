# QA: Create a Market Conditions Addendum Report (1004MC)

Title unchanged from the live article. Old Notion title: Creating a Market Conditions Addendum Report (1004MC).

Sources:
- Intercom article 16414760, content 19805100, Baldwin Reports collection only
- Mirror: `docs/help-center/baldwin/create-a-market-conditions-addendum-report-1004mc.md`
- Old Notion page: https://app.notion.com/p/3bc8b9e01438813688acd503b01d0508
- Product answers from the teammate, October 12, 2026. The live article has no images.

Scored by Claude for Kevin Liang, October 9 (original) and October 12, 2026 (rewrite). Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images live; the placeholder carries alt text |
| 3 undefined_terms | Pass | Pass | 1004MC and PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Report creation", "Report configuration", "Reading the report", "Tips" replaced |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Agents and brokers both create it; no role gates the workflow |
| 8 entity_distribution | Fail | Pass | Every section now names the 1004MC report |
| 9 semantic_chunk_boundaries | Fail | Pass | Tips split into creation, setup, and calculation sections |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Next, the Generate Report step, Print, and Download now documented |
| 13 limitations_workarounds | Pass | Pass | 500-listing cap with the fix; search results as the only starting point |
| 14 numerical_clarity | Pass | Pass | Stable range starts at 5% and -5% |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

New: pass. "Use" appears only in "Use this article to" and the "When to use" heading. Max List Date, Stable Range High, Stable Range Low, and Orientation are on-screen labels named where the member sets them. "Comp set" replaced with "comparable listings".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3 of 7) | 30.0 | +17.1 |
| Chunk independence (25) | 8.3 (2 of 6) | 25.0 | +16.7 |
| Answer completeness (25) | 17.9 (5 of 7) | 25.0 | +7.1 |
| Fin-parsable formatting (10) | 7.5 (6 of 8) | 10.0 | +2.5 |
| Accuracy and confidence (10) | 8.0 (4 of 5) | 10.0 | +2.0 |
| Total | 54.6 | 100.0 | +45.4 |

Old band: Needs rewrite. New band: Fin-ready, both gates passed, with open confirm markers below.

Old failures beyond the gate: description over 140 characters and opens "In this article"; H1 section headings; bold UI labels; terminal period in a step; "you can" and "To use"; no lead under several headings; "exact listings" stated twice. Facts the teammate overturned: stable range defaults (0% became 5% and -5%), the date field's name (report max date became Max List Date), the High Limit % and Low Limit % labels (now Stable Range High and Stable Range Low), the All listings and Selected listings choice (not on screen), and the optional summary checkbox (the summary is always included).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I create a 1004MC report? | Yes, but stops before generating | Yes |
| What is the default stable range on the market conditions report? | Yes, but wrong (0%) | Yes |
| Can I run a 1004MC from a listing page? | No | Yes |
| How do I download the 1004MC as a PDF? | No | Yes |
| How many listings can a market conditions addendum report have? | Yes | Yes |
| Why does the report say Decreasing when the form says Declining? | Yes | Yes |
| How do I change the effective date on the 1004MC? | Partly, under "report max date" | Yes |
| Why doesn't my median sale-to-list ratio match the medians? | Yes, in Tips | Yes |

## Open items

Resolved by the teammate, October 12, 2026, with a screenshot of the Customize Report step:

- A report needs at least one selected listing; the live article's "leave them unselected to use every listing" is wrong and was removed.
- Email Report exists on the Generate Report step; the email section was added.
- Use this overall stable range next time does not exist; left out.
- Step names Customize Report and Generate Report confirmed. The report type reads 1004MC Market Conditions Addendum.
- The report has no reporting period options; the period list was dropped. The Max List Date anchor sentence stays, from the live article.
- Stable Range High (%) and Stable Range Low (%): blank means 0%, high must be 0 or greater, low must be 0 or less, from the on-screen hint.

Still open:

- Report library: not mentioned, since the teammate did not confirm a 1004MC report is saved there.
- The Customize Report screenshot was shared in chat but not saved to disk; save it to `outputs/drafts/images/2026-10-12-1004mc-customize-step.png`.
- The Notion-only sentence that the report reflects the comp set "not a broad market average" was not carried; the When to use lead already says the metrics come from the exact listings researched.
- Screenshot needed: the Customize Report step for this report. Video: the old row asked for a new one; none exists, so Video Included is No.
