# Decisions: help center overhaul

One entry per decision, newest first. Each entry says what was decided, why, and who decided. Keep entries short; the rationale is the useful part.

## 2026-09-10: Four standard changes from the first article review

Decided by Tara, after the team read the Universal Search Bar migration. Three of the four traced to the standard rather than to the skill: the skill wrote what the rules told it to write.

- **MLS ID is the term.** Never "MLS number," "MLS #," or "listing number," in articles, macros, or replies. Perchwell labels the filter and the listing card **MLS ID**, and the live help center used both terms, sometimes in the same article. Recorded in the `docs/product-context.md` glossary and terminology rules.
- **Silence means every member.** A role is named only where a role gates the workflow or changes the behavior. A sentence saying everyone has the feature tells the member nothing and pushes their answer down the page. An availability claim paired with a `[confirm: ...]` marker now fails the audience factor rather than passing it. The Notion `Roles` property still records the audience either way.
- **Constraints are written as the route forward.** No Limitations section by default, and no hunting for downsides. A constraint the member will hit is stated where they meet it, as the alternative path: "To look up several listings at once, open the **Search** page and enter the IDs in the **MLS ID** filter." A dedicated section is reserved for a hard cap with an exact number that a member hits mid-workflow, or something irreversible; the 1004MC report's 500-listing cap is the model case, kept because suppressing it would generate the tickets the help center exists to prevent.
- **Say each fact once.** The feature name repeats in every section so a retrieved section identifies itself. The facts attached to it do not. Golden question 8 asks for entities, not facts, and reading it loosely produced a draft that stated the same three record types six times in 84 lines.
- **A confirm marker covers only what it names.** Marking a detail does not license the sentence around it. The first migrated draft did this twice: it claimed every member role has the feature while marking only the invited-client case, and it claimed the feature works the same way on mobile while marking only the location. Both unmarked halves were wrong. Mark the claim, or leave the sentence out. Generalized from the audience rule on 2026-09-10 into the standard, the scorecard, and the rewrite skill.
- **Never strengthen a hedged source.** Two false facts reached the first migrated draft the same way: "Results populate as you type" became "results appear in a panel below the field", and "statuses like Active, Pending, Closed, and Expired" became "Listings in every status appear". Neither was flagged, because the more confident sentence reads better and nothing marks it as new. The rewrite must be no more certain, complete, or specific than the sentence it came from. In the standard under Constraints, in the scorecard's accuracy check 2, and in the rewrite skill's rules.
- **No bold in the body.** The house style bolded every clickable element, filter, button, and status label. That is retired. Name the exact on-screen label and leave it plain; a page where every other phrase is bold puts emphasis on nothing. Two exceptions survive, both labels that introduce a block rather than emphasis inside a sentence: the callout labels **Note:**, **Important:**, and **Tip:**, which Intercom names as the signal Fin reads, and the `**Description:**` line. Transformation pattern 9 was rewritten from "Bold UI Elements" to its opposite, and the two model articles were stripped.
- **A pop-up window is a modal.** One word, used consistently through an article, rather than drifting between "window", "panel", and "pop-up". In the glossary and the terminology rules.
- **No inventory of the screen.** Do not list the fields a display renders. A member reading search results is looking at the listing card and can see the price and the bed count. Say what a display covers or does instead. Image alt text is the exception, since it exists for people who cannot see the image. Added after the same review, once the pattern showed up in the Listings bullet.

Propagated through `docs/product-context.md`, `docs/standards/content-standards.md` (new "Say each fact once" section; `Limitations` became `Constraints, and where to go instead`), `docs/standards/golden-questions.md` (house resolutions for factors 7, 8, and 13, following the factor 5 precedent), `docs/standards/fin-readiness-scorecard.md` (Chunk independence now six checks, two Answer completeness checks reworded), and both article skills with their templates and the Notion AI prompt. Scores recorded before this date are not comparable to scores after it.

The Universal Search Bar draft was rewritten and rescored against the new rules: 91.4, unchanged in total, but the September 9 draft scores 77.6 on the new check set, which is what the review caught.

## 2026-09-09: /article-rewrite is the migration path into the new database

Decided by Leo. Rather than a separate migration skill, `/article-rewrite` (version 2.0.0) now takes an old Master Article List page URL, merges it with the live mirror copy, rewrites to the standard, scores before and after, saves the draft and QA file, and creates the row in the Perchwell Help Center Database [Sep 2026] as a Draft. Property mapping from the old database lives in `.claude/skills/article-draft/references/notion-publishing.md` so both article skills share it. First article through: Universal Search Bar, Notion Draft `https://app.notion.com/p/3d68b9e01438810cb386f3ea550d097c`, scored 50.0 before and 91.4 after.

## 2026-09-09: The Fin-readiness scorecard is the per-article yardstick

Decided by Leo; Tara owns it, Rafe owns the Fin answer-quality side. `docs/standards/fin-readiness-scorecard.md`: the 14 golden questions as a pass-or-fail gate, then 0 to 100 across five weighted dimensions (retrieval signals 30, chunk independence 25, answer completeness 25, Fin-parsable formatting 10, accuracy and confidence 10), with bands at 90, 75, and 50. It is a standard rather than a skill reference because the audit, the QA pass, and both article skills need the same number. Scores live in the chat report and one QA file per article under `workstreams/help-center-overhaul/qa/`; the Notion database schema was left alone.

## 2026-09-09: The live Intercom article wins over the old Notion page on facts

Decided by Leo during the Universal Search Bar test. When an old Notion page and the live article disagree, the live article is the source of truth because it is newer and it is what members and Fin see. The Notion page supplies the video link, the properties, and the click script as a hint for outcomes. Every difference is listed in the QA file, never merged silently.

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
