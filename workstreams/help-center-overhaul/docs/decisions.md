# Decisions: help center overhaul

One entry per decision, newest first. Each entry says what was decided, why, and who decided. Keep entries short; the rationale is the useful part.

## 2026-09-04: Repo is read-only toward Intercom until pushes are turned on (target September 11)

Decided by Leo during repo bootstrap. The skills document how Intercom pushes will work, but the article write tools sit on the ask list and no skill calls them today. Reason: the team wants to trust the mirror and the review flow before anything touches production.

## 2026-09-04: Notion is the review layer, Intercom is production, the repo mirrors Intercom

Decided by Leo, matching the marketing repo's pattern. Drafts are created in Notion for comments and approval. Intercom holds what members and Fin see. The repo keeps a read-only copy of Intercom so Claude can search and cross-link without live calls.

## 2026-09-04: Perchwell's Fin resolution definition is the project metric

From the Notion project page. Fin resolved means Fin answered, no teammate message followed, and no same-topic follow-up from the member within 48 hours. Reported weekly next to Intercom's number, never blended, so the two cannot be confused.

## 2026-09-04: "Golden questions" means Intercom's 14 content readiness factors

Decided by Leo. The golden questions are the checklist every article must pass (`docs/standards/golden-questions.md`), not a set of mined member questions. A first pass at mining member questions from the two weeks after Baldwin cutover was built and then dropped; its findings that still matter for the weekly Fin report are below.

## Notes for Fin reporting (from the dropped member-question pull, 2026-09-04)

- Teammate test traffic sits inside the Baldwin chat workflow with `MLS: Baldwin` at creation; it is only relabeled Test / Internal by hand later. 52 of 637 Fin conversations in August 3 to 17 were tests. Any Fin count should drop conversations whose author email ends in @perchwell.com or whose attributes say Test / Internal.
- A bare acknowledgement from the member ("thanks", "yes", "got it") after Fin's answer should not count as a same-topic follow-up under the Perchwell definition; confirm with Rafe.
- Teammate courtesy check-ins after a correct Fin answer count as intervention under the definition as written. Decide whether a check-in with no new information should count.
- Fin cites articles from the default help center and Fin snippets that are not in the Baldwin help center. Related to the retrieval scoping question Jeff owns.
- In a 25-conversation sample, 13 met the Perchwell resolved definition and a teammate stepped in on 12, in line with the roughly 40 percent human intervention the project page cites.
