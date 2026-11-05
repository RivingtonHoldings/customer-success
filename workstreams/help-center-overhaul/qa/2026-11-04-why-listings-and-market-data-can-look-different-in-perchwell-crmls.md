# QA: Why Listings and Market Data Can Look Different in Perchwell (CRMLS)

Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-04-why-listings-and-market-data-can-look-different-in-perchwell-crmls.md`. New article with no Baldwin counterpart. Source: the Matrix doc "External Then vs Now: CRMLS Matrix → Perchwell". Tracker ID: TRK-136 (next free number at Tara's direction, Nov 4, 2026). Notion row name carries a "(CRMLS)" suffix for now. Original article title blank in the master sheet: brand-new article.

## Checks run

- Title (no collision with an existing CRMLS article or a Perchwell page name), description (120 characters), "Use this article to ..." opening, heading levels, tables with intro sentences, numbered sequence for the listing path: pass.
- No em dashes, bold, horizontal rules, "you can": pass.
- Fin-readiness score and the 14 golden questions: not run. Five confirm markers remain.

## Where the doc rows landed

- CRIB flow and 5-minute step: How a CRMLS listing reaches Perchwell (this is the one home; What Changed links here).
- 11 of the 14 data-difference rows are in three tables, grouped by what the member sees.
- Three rows (missing property subtype, $0 or 0 value, Hold vs. Temporarily Off Market) live in Listing Field Changes in Perchwell (CRMLS), so each fact has one home. This article points to it in its last paragraph.

## Open items

| Marker | Question | Notes |
|---|---|---|
| V5 | How can a member tell a change has reached CRIB? | The doc says to check again 5 minutes after it reaches CRIB, with no way to see that |
| V14 | "Rely on the Perchwell and Matrix figure": wording | Ambiguous; the draft keeps the doc's words |
| V2 | Workaround for Market Activity counts mixing in rentals | The doc's own marker |
| V12 | Do known issues (map pin, address search) stay in the article? | The standards keep bugs out unless a member would get stuck; a workaround exists for each, so they are kept pending Tara's call |
| Link | CRMLS Listing Field Changes in Perchwell | Link marker; the record has no public link yet |

## Judgment calls to confirm

- Source wording is kept for numbers and reasons ($25,000, 1 or more days, about 20%, 5 minutes), unverified by a second source (V10).
- "Perchwell leaves out sales under $25,000 on purpose" is stated as the doc states it; it is internal-sounding and may need a Product check.
- The doc mentions "CRMLS dashboards" without naming them; confirm members know them by that name.
- The heading "Why Market Analytics and ranking numbers look off" covers Market Analytics, Market Activity, Agent Ranking, and Office Ranking.

## Fin test questions

1. Why is my listing different in Perchwell than in Matrix?
2. How long does a listing change take to show in Perchwell?
3. Why is the median sold price higher in Perchwell than on the CRMLS dashboards?
4. Why do Market Analytics prices look low?
5. Why does an agent appear twice in Agent Ranking?
6. Why is there a blank office in Office Ranking?

## Review results, Nov 4, 2026

Scored by Claude against `docs/standards/fin-readiness-scorecard.md` (check set revision 2, plain language gate), after the draft-quality pass in `.claude/skills/article-rewrite`. Self-scored, so a second reviewer's read is still pending. New article: no old score to compare.

### Golden questions

| Factor | Result | Note |
|---|---|---|
| 1 disambiguation | Pass | No "this screen", "above", or emoji pointers. |
| 2 visual_content_text | Pass | No images; nothing to describe. |
| 3 undefined_terms | Pass | Abbreviations defined at first use after review. |
| 4 structured_enumeration | Pass | Steps and sequences are numbered; sets are bulleted or tabled. |
| 5 query_answer_symmetry | Pass | Headings name what each section answers, per the house reading of factor 5. |
| 6 self_contained_sections | Pass | No dependence on earlier sections; navigation named where a step needs it. |
| 7 audience_specification | Pass | Open to all members; Notion Roles is All. Silence is correct. |
| 8 entity_distribution | Pass | Feature and product names repeat in each section. |
| 9 semantic_chunk_boundaries | Pass | One topic per section. |
| 10 restate_questions | Pass | Every table has an intro sentence. |
| 11 overview_jtbd | Pass | "Use this article to ..." opening. |
| 12 instruction_completeness | Pass | No procedure beyond the outcome sentences. |
| 13 limitations_workarounds | Pass | Gaps are stated once with the route forward, or marked. |
| 14 numerical_clarity | Pass | Exact numbers or a marker for unknowns. |

All 14 pass as drafted, with confirm markers still open. Markers must clear before the row moves to Ready to Transfer.

### Plain language gate

Flag, not a pass: "CRMLS member records" uses "records" as a stand-in. The replacement noun depends on what the two entries are (V-new: ask Product). Gate stays pending on this term.

### Dimension scores (new article)

| Dimension | Checks passed | Score |
|---|---|---|
| Retrieval signals | 7 of 7 | 30.0 of 30 |
| Chunk independence | 6 of 6 | 25.0 of 25 |
| Answer completeness | 7 of 7 | 25.0 of 25 |
| Fin-parsable formatting | 8 of 8 | 10.0 of 10 |
| Accuracy and confidence | 5 of 5 | 10.0 of 10 |

Total 100.0 of 100, band Fin-ready. The score does not count open confirm markers against accuracy, so it will not move when they clear.

### Changes the review made

- Heading now names Market Activity, which the section covers (heading-covers-section rule).
- Replaced "a few listings and searches" and "some recent sales" with an unvague sentence and a marker (factor 14).
- Defined CRMLS and MLS at first use, using the doc's own sentence (factor 3).
- Split a 26-word closing sentence.

## Markers resolved, Nov 5, 2026

- CRIB (V5): Tara said remove the marker. Removed. The sentence "Check the listing in Perchwell again 5 minutes after the change reaches CRIB" remains, and a member cannot see when a change reaches CRIB; consider rewording.
- Removed at Tara's direction: the rows "Days on market for recent sales ..." (clearing the which-recent-sales and instruction-wording markers) and "Market Activity counts look high ..." (clearing the Market Activity workaround marker), and the whole section "Why a listing or search result looks wrong" with its table and its known-issues marker (map pin, address search, impossible price or date).
- Follow-on edits: the Market Analytics section heading and lead no longer name Market Activity, since no row covers it; the pointer to Listing Field Changes moved to the end of the first section so it is not orphaned.
- Open now: the link to Listing Field Changes.

## Row name, Nov 5, 2026

The "(CRMLS)" suffix was removed from this article's Notion Article Name at Tara's request, so the row now carries the exact article title for the port. The master sheet's title columns were not changed.

## Synced from Notion, Nov 5, 2026

Notion was ahead of the repo. Kelly is the Article Reviewer on all nine rows, Article Due is Nov 12, 2026, Article Status is Ready to Transfer, and Roles is All Except Client, all set by Tara or the team. Article Review Status is still Not Started; the CRMLS port needs Review Finished or Complete. No screenshots on this article.

## Decisions, Nov 5, 2026

- CRIB sentence: Tara approved the reword. The paragraph now ends "The last step takes about 5 minutes after CRMLS sends the change." I also changed the sentence before it from "has usually not reached CRIB yet" to "has usually not reached Perchwell yet", so the two sentences agree and the member is not asked to think about CRIB.
- Plain language gate: Tara confirmed the noun is member ID. "The agent has two CRMLS member IDs." The gate flag from earlier is cleared; the gate now passes.
