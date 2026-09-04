# Decisions: help center overhaul

One entry per decision, newest first. Each entry says what was decided, why, and who decided. Keep entries short; the rationale is the useful part.

## 2026-09-04: Repo is read-only toward Intercom until pushes are turned on (target September 11)

Decided by Leo during repo bootstrap. The skills document how Intercom pushes will work, but the article write tools sit on the ask list and no skill calls them today. Reason: the team wants to trust the mirror and the review flow before anything touches production.

## 2026-09-04: Notion is the review layer, Intercom is production, the repo mirrors Intercom

Decided by Leo, matching the marketing repo's pattern. Drafts are created in Notion for comments and approval. Intercom holds what members and Fin see. The repo keeps a read-only copy of Intercom so Claude can search and cross-link without live calls.

## 2026-09-04: Perchwell's Fin resolution definition is the project metric

From the Notion project page. Fin resolved means Fin answered, no teammate message followed, and no same-topic follow-up from the member within 48 hours. Reported weekly next to Intercom's number, never blended, so the two cannot be confused.

## 2026-09-04: Golden questions sample the two weeks after Baldwin cutover

Decided by Leo. Window is August 3 to August 17, 2026, because that is when new-member questions were densest and Fin's gaps most visible. Filter problems found while building the first set are logged below for Session 2.

## Session 2 notes

Filter problems and follow-ups discovered while running `/golden-questions` v1 on 2026-09-04.

- Internal test traffic is inside the Baldwin workflow. Teammates testing Fin with +alias perchwell.com accounts created 52 conversations in the window (637 raw, 585 after removing them). The MLS attribute is Baldwin at creation and is only changed to "Test / Internal" by hand afterward, so the pool now drops any conversation whose author email ends in @perchwell.com or whose attributes say Test / Internal. Two such conversations still reached the sample before the filter existed and were excluded at extract time.
- The compact `search` rows have no created_at, so the sample spreads across the window by conversation ID order rather than by day. IDs increase with creation time, so the spread is right, but per-day counts are only available after `get_conversation`.
- Paging with the compact `search` tool is sorted by last update, and jumping ahead with synthetic cursors left an 88-conversation gap the first time. The skill now pages sequentially with the cursors the API returns and verifies the unique count against total_count.
- A bare acknowledgement ("thanks", "yes", "got it") after Fin's answer was counted as a same-topic follow-up in the first pass, which marked four clean Fin answers unresolved. The extract now ignores short acknowledgements. Session 2 should confirm this reading of the Perchwell definition with Rafe.
- Teammate courtesy check-ins after a correct Fin answer ("let me know if you need anything else") count as intervention under the Perchwell definition as written. Three of the 12 interventions in the sample were courtesy only. Decide whether a check-in with no new information should count.
- Fin cites articles from the default help center and Fin snippets that are not in the Baldwin help center; the mirror lookup reports these as "not in Baldwin mirror". Related to the retrieval scoping question Jeff owns.
- Scrubbing replaces every member and teammate name the run saw, but third parties named inside a message (a client, a colleague) are only caught when they match a known name. The committed set avoids quoting those messages; Session 2 should add a general capitalized-name pass or a review step.
- The sample's Perchwell-resolved share was 13 of 25 (52 percent) with a teammate stepping in on 12 of 25 (48 percent), in line with the roughly 40 percent human intervention the project page cites for Baldwin.
