# QA: Create a Full Report

- **Article name:** Create a Full Report
- **Old title:** Create and Share Full Reports
- **Sources:** old Notion page https://app.notion.com/p/2a08b9e01438803ea469d8c6ae438e82; Intercom article ID 12816757, content ID 14457971; mirror paths `docs/help-center/baldwin/create-and-share-full-reports.md` and `docs/help-center/crmls/create-and-share-full-reports.md` (shared article, identical bodies)
- **Product evidence:** teammate screenshots captured October 12, 2026: the Listing Detail Page Actions menu (Print full report under Create), the Print report window, the Search results Actions menu (Create a Report), and the Customize Report step for a Full Report. Teammate answers the same day: there is no footer action bar, Customize Report then Generate Report follow as in the other reports, collapsing a section on the Listing Detail Page collapses it in the report, Full Reports appear in the Report library, and the video needs re-recording
- **Scored by:** Claude for Kevin, October 12, 2026
- **Scorecard:** September 10, 2026 set, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Live article has no images; the new draft's placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | PDF defined on first use |
| 4 structured_enumeration | Pass | Pass | Report versions are a labeled list |
| 5 query_answer_symmetry | Fail | Pass | Bare "Tips" heading removed |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the workflow |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening |
| 12 instruction_completeness | Fail | Pass | Search route now runs through Customize Report and Generate Report |
| 13 limitations_workarounds | Pass | Pass | Adding listings framed as creating a new report |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. No term from the do-not list. "Print full report", "Print report", "For agent", "For client", "Both", and "Include Listing History" are exact on-screen control labels.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 | 25.0 | +8.3 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 6.3 | 10.0 | +3.7 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| **Total** | **52.5** | **100.0** | **+47.5** |

Old band: Needs rewrite. New band: Fin-ready. No `[confirm: ...]` markers remain.

Old failures: description in the "In this article, you will learn" form at about 185 characters; no "Use this article to" opening; bare "Tips" heading; Tips without a heading echo; H1 used for sections; the print-the-whole-page fact stated twice; Search steps stop at Next; PDF undefined; no related links; step labels stale ("actions", "Full Report") and one step combining a choice with sub-bullets; bold throughout; horizontal rules; "great way" in a tip; "Use this option" twice.

The live article's facts were stale, not just its form: today's screenshots show Print full report in the Actions menu, a Print report window with For agent and For client and an Include Listing History checkbox, and a Search route through Actions and Create a Report rather than a footer action bar. A score cannot see that; the screenshots did.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I print a full report for a listing? | Partly; the menu label is wrong | Yes |
| How do I make a full report for multiple listings? | No; the route described no longer exists | Yes |
| What is the difference between the agent and client report? | Yes, for one route only | Yes |
| Can I leave the listing history out of a full report? | No | Yes |
| How do I hide a section from the full report? | No | Yes |
| Can I email a full report to a client? | No | Yes |
| Where do I find a full report I already made? | No | Yes |

## Open items

- Resolved October 12, 2026 by the teammate: selecting Full Report goes straight to Customize Report; the For agent and For client descriptions from the live article still hold; Both creates two reports, one agent version and one client version; Include Listing History is on by default; the Email Subject field has no default text; Full Reports from a Listing Detail Page appear in the Report library. No `[confirm: ...]` markers remain
- Collapsed sections: confirmed for the Listing Detail Page route. Unknown whether sections collapsed on a listing carry into a Full Report built from search results; the draft says nothing about it
- The collapse arrow next to each Listing Detail Page section has no hover label, confirmed October 12, 2026; the step names it by shape
- The report window shows its labels in capitals (FOR AGENT, FOR CLIENT, BOTH); the draft writes them as the Print report window spells them, For agent and For client
- Title: "Create a Full Report" chosen by the teammate October 12, 2026, to match the set (Create a Listing Report, Create a Show Sheet). Old title recorded for the Intercom redirect and audit
- Shared article: the same Intercom record sits in the Baldwin and CRMLS Reports collections. Row set to MLS/AOR Baldwin and CRLMS All, matching the Listing Report and Show Sheet rows
- CRMLS also has "Creating One Page and Full Reports" in Critical Workflows, which describes the old three-dot menu and an "action window at the bottom of the page". It overlaps this article and is stale
- One more live Baldwin article carries the stale "Select Full Report" step: Appraiser Capabilities in Perchwell ("Save a Full Report for your records")
- Video: re-record. The old Notion row and the live article point to two different Arcade recordings (`ndx68YWX…` and `IDl2eNP0…`); both predate the Print full report label
- Screenshots: three new teammate captures saved under `outputs/drafts/images/` plus the shared profile-menu capture from the Show Sheet draft; no member names appear in the new captures
