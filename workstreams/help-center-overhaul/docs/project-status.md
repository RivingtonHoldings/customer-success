# Project status: help center overhaul

Living document. Update in place; do not append dated sections. Last updated: 2026-09-09.

## Roles and contacts

Emails confirmed from the Notion workspace directory on 2026-09-04. Titles in brackets are not yet confirmed and should be filled in from Notion or by the person.

| Person | Role on this project | Title | Email |
|---|---|---|---|
| Tara | Project lead. Owns standards, video scoping, and the overall timeline | [title] | [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com) |
| Kelly Miragliotta | Baldwin content audit owner; approver on standards | [title] | [kelly.miragliotta@perchwell.com](mailto:kelly.miragliotta@perchwell.com) |
| Rafe Petkovic | Sets the Fin answer-quality pass rate; approver on standards; owns post-project maintenance ownership decision | [title] | [rafe.petkovic@perchwell.com](mailto:rafe.petkovic@perchwell.com) |
| Jeff Wakeland | Intercom and Fin mechanics: labels, retrieval scoping, Content from Conversations | [title] | [jeffrey.wakeland@perchwell.com](mailto:jeffrey.wakeland@perchwell.com) |
| Leo Jedynak | Marketing partner and repo owner. Defines the release-to-help-center workflow with CS | [title] | [leo.jedynak@perchwell.com](mailto:leo.jedynak@perchwell.com) |

Escalation for repo or Claude Code problems: Leo. Escalation for project scope: Tara.

## Resources

- Notion project page (system of record): https://app.notion.com/p/3c88b9e0143880ec8fbee25ec0b38975
- Notion deliverables database: https://app.notion.com/p/3c88b9e014388087a2e8e299bb63d0f1
- Perchwell Help Center Database [Sep 2026], where project articles live: https://app.notion.com/p/3d18b9e0143880558dc9d9574f5abab8
- Template Article, the standard as a fill-in page: https://app.notion.com/p/3d18b9e0143880189917f12bdc34c500
- Fin-readiness scorecard: `docs/standards/fin-readiness-scorecard.md`; per-article results in `workstreams/help-center-overhaul/qa/`
- Naming standards page: https://app.notion.com/p/3ce8b9e0143881b790c6c7c29eb11009
- Master Article List (old, read-only for this project): https://app.notion.com/p/1c78b9e01438802082c4eb08025fbb0a
- Baldwin help center: https://support.perchwell.com/baldwin/en
- CRMLS help center: [confirm: public URL]
- Local mirror: `docs/help-center/baldwin/` and `docs/help-center/crmls/`

## Current status

- Project status in Notion: Not Started as of September 1, 2026.
- Repo bootstrapped September 4, 2026, with the help center mirror and the golden questions checklist in place (see `docs/build-log.md`).
- Baldwin cutover happened August 3, 2026. The two weeks after cutover (August 3 to 17) are the reference window for Fin baseline reporting.
- First article migrated on September 9, 2026: Universal Search Bar, now a Draft in the new database with six `[confirm: ...]` items for review. Scorecard 50.0 before, 91.4 after.

## Active initiatives

| Initiative | Owner | Due | Status |
|---|---|---|---|
| Help center standards finalized and approved | Tara, with Rafe and Kelly | Sep 4, 2026 | Content standards, Template Article, and the Fin-readiness scorecard reconciled on Sep 9 after the first migration test; awaiting Kelly and Rafe review. Fin labeling still drafted with [decide] items for Tara |
| All 115 Baldwin articles audited with recommendation, rationale, priority | Kelly Miragliotta | Sep 11, 2026 | Not started |
| Fin answer-quality pass-rate target set | Rafe Petkovic | Sep 15, 2026 | Open |
| Article updates and new content complete | Tara | Sep 18, 2026 | Not started |
| Visual and video updates complete | Tara | Sep 25, 2026 | Not started |
| QA and Fin validation | Tara | Oct 2, 2026 | Not started |

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| The new database dropped the `Fin AI`, `Text`, `Screenshot`, and `Video` workflow-status fields. Is per-asset progress tracked somewhere else, or is it out of scope now? | Tara | Sep 11, 2026 |
| 26 articles are shared between the Baldwin and CRMLS help centers, but the new database holds one `MLS/AOR` per row. Does a shared article get one row (Baldwin) or two? Universal Search Bar is the first case | Tara | Sep 11, 2026 |
| The `MLS/AOR` option in the new database reads `CRLMS All`. Should it be renamed to CRMLS? Writes must use the string exactly as it appears until it changes | Tara | Sep 11, 2026 |
| Do Baldwin members have a Presentations widget or a Days on Market widget on the Dashboard? Three documentation signals say no, but only product can confirm, and the answer decides whether one Dashboard Overview body can serve every MLS. See `audit/dashboard-widget-lineup-2026-09-10.md` | Tara, with product | Sep 18, 2026 |
| Does the CRMLS Dashboard have one Days on Market widget or two? `crmls/customizing-your-dashboard.md` lists one, and two separate live CRMLS articles describe Days Active in MLS and Days Active on Market as different widgets | Kelly Miragliotta | Sep 18, 2026 |
| Is NYC in scope when we say an article should serve every MLS? It is an `MLS/AOR` option and has its own Dashboard Overview row, but `docs/product-context.md` puts NYC outside this project | Tara | Sep 11, 2026 |
| Should FAQ answers get an exception to the "you can" ban, the way "When to use" headings are excepted from the verb-"use" ban? "You can add as many as you'd like" is the natural answer under a question-form heading, and 12 of 16 FAQ articles fail scorecard check 5 on it. Three of the eleven worst-offender articles are FAQs, so the answer changes the backlog ranking. See `audit/voice-sweep-2026-09-10.md` | Tara and Kelly Miragliotta | Sep 11, 2026 |
| How do members reach help content in each market: the help center directly, or through Perchie? | Kevin Liang | Sep 3, 2026 |
| Which platform(s) are CRMLS members migrating from, and how does that affect the eight Then vs. Now articles? | Kelly Miragliotta | Sep 3, 2026 |
| Is Content from Conversations enabled in Intercom, and how should it feed maintenance? | Jeff Wakeland | Sep 8, 2026 |
| Can labels be applied to many articles at once, or to a whole collection? | Jeff Wakeland | Sep 8, 2026 |
| How should Fin retrieval be scoped so members only get content for their MLS? | Jeff Wakeland | Sep 8, 2026 |
| What Fin pass rate is required across two consecutive test runs before CRMLS cutover? | Rafe Petkovic | Sep 15, 2026 |
| Who owns the article inventory and Fin label schema after October 2? | Rafe Petkovic | Oct 2, 2026 |

## Risks

- Fin pass-rate target undefined; blocks the launch gate. Rafe, due Sep 15.
- Number of CRMLS videos to re-record unconfirmed. Tara to confirm during video scoping.
- Possible migration from Intercom to another CS platform would force a redo of Fin-specific labeling and testing. Keep standards platform-agnostic where possible.
