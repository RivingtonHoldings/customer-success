# QA: Create a One Page Report

- **Article:** Create a One Page Report. Old title: Create One Page Reports
- **Sources:** Intercom article 12816780, content 14458010; mirror `docs/help-center/baldwin/create-one-page-reports.md` and `docs/help-center/crmls/create-one-page-reports.md` (shared through the Reports collection in both help centers); old Notion page https://app.notion.com/p/3128b9e0143880afb11ce589bc1a1ac8; product screenshots captured October 12 and 13, 2026, and answers from Kevin, October 13, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-create-a-one-page-report-rewrite.md`; Notion https://app.notion.com/p/3f88b9e014388179861ed2092d599187
- **Scored by:** Claude for Kevin, October 13, 2026. Scorecard check set revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | "Use this option" and "the actions button" pointed at nothing a member can find; new steps name Actions, Print one page report, and One Pager exactly |
| 2 | visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 | undefined_terms | Pass | Pass | PDF defined on first use |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "QR code use" and "Tips" replaced by task headings carrying the feature name |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | No role gate; Roles property records All Except Client |
| 8 | entity_distribution | Fail | Pass | Tips section never named the One Page Report |
| 9 | semantic_chunk_boundaries | Fail | Pass | Tips mixed editing listings with the Report library |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 | instruction_completeness | Fail | Pass | Old Search steps stopped at Next |
| 13 | limitations_workarounds | Pass | Pass | Adding listings framed as creating a new report |
| 14 | numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. On-screen labels (Print one page report, One Pager, For agent, For client, For both) appear only where the member clicks them; the article's own noun is One Page Report throughout.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3 of 7: description over 140 characters and "In this article" form, no opening, headings and echoes) | 30.0 | +17.1 |
| Chunk independence (25) | 12.5 (3 of 6: Tips lacks feature name, mixes topics, H1 used for sections) | 25.0 | +12.5 |
| Answer completeness (25) | 14.3 (4 of 7: Search steps end at Next, no defaults, Report library not explained) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 6.3 (5 of 8: bolded UI, inexact labels, horizontal rules) | 10.0 | +3.7 |
| Accuracy and confidence (10) | 6.0 (3 of 5: stale labels stated as fact, verb "use") | 10.0 | +4.0 |
| **Total** | **51.9, Needs rewrite** | **100.0, Fin-ready** | **+48.1** |

The three `[confirm: ...]` markers in the first draft were resolved by Kevin on October 13, 2026, so the score stands with no conditions.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I print a one page report for a listing? | Yes, but with the stale "actions button" label and no Print one page report | Yes |
| Can I make a one pager for multiple listings? | Yes, but through a footer action bar that no longer exists | Yes |
| What's the difference between the agent and client version? | Yes, inside the Listing Detail Page steps only | Yes |
| Can I print the agent and client versions at the same time? | No | Yes |
| How do I email a one page report to a client? | No | Yes |
| Does the one page report have a QR code, and what does it open? | Yes | Yes |
| Where do I find a one page report I made last week? | Partly; Tips names the Report Library without saying how to open it | Yes |

## Open items

- Resolved October 13, 2026 by Kevin: selecting One Pager moves straight to the Customize Report step; the Customize Report step offers For agent, For client, and For both; For agent is the default. Markers removed from the draft
- [confirm, not in body] The new tab that opens from a Listing Detail Page has the same Emails, Email Subject, and Message fields and Email Report, Print, and Download buttons as the Generate Report step, and whether a One Page Report created there is saved to the Report library. If yes, the email, print, and download section lead can say so
- [confirm, not in body] Default text in the Email Subject field for a One Pager
- Video: the live Arcade walkthrough (demo.arcade.software/q8cqAyPuAnqnPRjIZdlD) shows the old flow, so it was replaced with a re-record placeholder. The old Notion page links a different Arcade (app.arcade.software/share/UjC5lZYyOXAeDdarz7Ys)
- Shared article: lives in both Baldwin and CRMLS Reports collections; one row with both MLS values, per the set
- Set: Create a Full Report links this article by its old title, Create One Page Reports. Update that link text when this article ports. This article links the live Create and Share Full Reports, which becomes Create a Full Report at its port
- Set: the "Choose the agent or client version" heading matches Create a Full Report but does not name the both option; if the team changes one, change both
- Screenshot: the Listing Detail Page Actions image shows the capturer's profile photo in the upper right; crop it before placing
