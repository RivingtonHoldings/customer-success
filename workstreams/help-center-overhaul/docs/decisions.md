# Decisions: help center overhaul

One entry per decision, newest first. Each entry says what was decided, why, and who decided. Keep entries short; the rationale is the useful part.

## 2026-09-04: The Perchwell Help Center Database [Sep 2026] is where project articles live

Decided by Tara. The team created a new Notion database for this project to simplify the work and make each article's state obvious, and set its properties the way they want them. For the rest of this project, an article we draft or update is added to the new database. The old Master Article List is read-only: query it for history, never write to it, and do not mirror a change back into it. `Article Name`, `Article Status`, `MLS/AOR`, `Collection`, `Roles`, `Videos`, `Visuals`. Database `https://app.notion.com/p/3d18b9e0143880558dc9d9574f5abab8`, data source `collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389`.

Two consequences to watch: the new database has no equivalent of the old `Fin AI`, `Text`, `Screenshot`, and `Video` workflow-status fields, so per-asset progress is not tracked in Notion any more, and `docs/standards/fin-labeling.md` now derives labels from `MLS/AOR` and `Collection` plus the article's shape.

## 2026-09-04: Content standards written and grounded in Intercom's Fin guidance

Decided by Tara, with Kelly and Rafe as approvers. `docs/standards/content-standards.md` is now the single rulebook; the bundled fallback in `.claude/skills/article-draft/references/style-rules.md` is retired to a pointer. Three rules changed because Intercom's own Fin guidance contradicted the old house style, and because no live article followed it:

- Articles open with a jobs-to-be-done paragraph ("Use this article to ...") instead of an `In this article:` heading. Intercom names the topic-describing form as the weaker one.
- The "Connect with our Support Team" footer is gone. Intercom renders Related Articles and a feedback prompt itself, and no live article carried the footer.
- Callouts lead with a bold **Note:**, **Important:**, or **Tip:** label instead of an emoji. Intercom says the bold label is what flags a passage for Fin; emoji do nothing for retrieval.

Heading levels are now fixed at H1 title, H2 sections, H3 subsections and `Steps:`, following Intercom's formatting guidance. Three sampled live articles used three different schemes, which cost retrieval quality since headings are weighted heavily. This also settles the standing conflict between golden question 5 and the old house style: headings must name what the section answers and carry the feature name, question form is required in FAQ articles and allowed anywhere it matches how members ask.

The two model articles the team chose as the standard are [How to Share a Tag](https://support.perchwell.com/baldwin/en/articles/16221617-how-to-share-a-tag) and [Create a Market Conditions Addendum Report (1004MC)](https://support.perchwell.com/baldwin/en/articles/16414760-create-a-market-conditions-addendum-report-1004mc). Both are reproduced, normalized, and annotated in `.claude/skills/article-draft/references/example-article.md`.

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
