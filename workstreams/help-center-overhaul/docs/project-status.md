# Project status: help center overhaul

Living document. Update in place; do not append dated sections. Last updated: 2026-09-16.

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
- First article migrated on September 9, 2026: Universal Search Bar. Scorecard 50.5 before, 95.7 after, which is the agreed ceiling for this article. All six `[confirm: ...]` items were resolved on September 10, 2026; none remain.
- **First article ported to Intercom on September 17, 2026:** Universal Search Bar, article 11002620, live in both the Baldwin and CRMLS help centers. Pushes were turned on the same day and `/port-to-intercom` now carries the transfer. The Notion row is `Live in Intercom` and holds the live URL in the new `Intercom URL` property.
- **Score figures.** The QA file in `qa/` is authoritative when it and these docs disagree. Two earlier entries here and in `decisions.md` quoted 50.0/91.4 and 50.5/95.0, both taken before the September 15 rescore; the settled numbers are **50.5 before, 95.7 after**.

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
| **Resolved Sep 17, 2026: one row.** A shared article is a single Intercom record held in a collection in each help center, so one row with both `MLS/AOR` values. What remains open is the consequence: a shared article's cross-links can only point into one help center, and Universal Search Bar now shows CRMLS members four Baldwin links, one of which maps Paragon terms. Splitting the 26 shared articles into per-MLS records is the fix; until then, every port of a shared article flags its links. Needs a decision before more shared articles are ported | Tara | Sep 24, 2026 |
| The `MLS/AOR` option in the new database reads `CRLMS All`. Should it be renamed to CRMLS? Writes must use the string exactly as it appears until it changes | Tara | Sep 11, 2026 |
| Six live CRMLS articles still document Listing Presentations, which was removed from CRMLS. Fin answers from published articles, so CRMLS members can be told about a feature they do not have today. Correct them before or after the audit is finalized? One Notion row is also queued at `Transfer to Intercom` for the removed feature. List and priority order in `audit/dashboard-widget-lineup-2026-09-10.md` | Tara and Kelly Miragliotta | Sep 11, 2026 |
| **Resolved Sep 23, 2026: neither MLS has it.** Tara confirmed CRMLS no longer has the Days on Market widget, which answers the old one-or-two question at zero and settles the shared Dashboard Overview spine at five widgets. What remains is the consequence: four live CRMLS articles still document it, two of them entirely (The Days Active on Market Widget, 13921294, and The Days Active in the MLS Widget, 11010483), plus the widget list in `crmls/customizing-your-dashboard.md` and the chart section in `crmls/the-dashboard-page-overview.md`. Same shape as the Listing Presentations row above, and it should be handled with it: ten CRMLS articles now describe features CRMLS does not have, and Fin answers from all of them. Days on Market as a listing field is unaffected, so the fix removes widget references, not every mention of the metric | Tara and Kelly Miragliotta | Sep 18, 2026 |
| Do the approved `<Page> Overview` and `<Area> FAQ` title patterns satisfy Fin-readiness Retrieval check 1, which wants a task-led title? The article types table in `content-standards.md` approves both patterns; check 1 reads "task-focused and names the outcome". The two have been scored inconsistently: "Dashboard Overview" passed check 1 and scored 30.0 of 30, "Listings Widget Overview" failed it and scored 8.6, and the Universal Search Bar QA file asserts that adding "Overview" would not satisfy check 1. **28 live articles are exposed**, 15 titled `<X> Overview` and 13 titled `<X> FAQ`. If the patterns pass, Dashboard Overview is right and the Listings Widget before-score is understated by 4.3. If they do not, Dashboard Overview is overscored and 28 articles carry a 4.3-point penalty they cannot escape without abandoning the type pattern. Same shape as the FAQ "you can" question below, and it moves the backlog ranking the same way. **Third data point, Sep 22, 2026:** the Dashboard FAQ migration scored the check-1 failure, siding with Listings Widget Overview against Dashboard Overview, and capped at 95.7 with the gate passed. A ruling that the patterns pass would make it 100.0 without changing its band | Tara and Kelly Miragliotta | Sep 18, 2026 |
| Should FAQ answers get an exception to the "you can" ban, the way "When to use" headings are excepted from the verb-"use" ban? "You can add as many as you'd like" is the natural answer under a question-form heading, and 12 of 16 FAQ articles fail scorecard check 5 on it. Three of the eleven worst-offender articles are FAQs, so the answer changes the backlog ranking. See `audit/voice-sweep-2026-09-10.md`. **Evidence against needing the exception, Sep 22, 2026:** the sentence quoted here is the Dashboard FAQ's, and its migration answered the same question as "Add as many Hot Sheets to the Perchwell Dashboard as you need." That reads naturally under a question-form heading, so the ban appears satisfiable without an exception | Tara and Kelly Miragliotta | Sep 11, 2026 |
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
