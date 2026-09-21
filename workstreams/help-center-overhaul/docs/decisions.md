# Decisions: help center overhaul

One entry per decision, newest first. Each entry says what was decided, why, and who decided. Keep entries short; the rationale is the useful part.

## 2026-09-16: Production status splits from the article's media fields

Decided by Tara; recorded 2026-09-21. Screenshot and video production is now tracked separately from what an article contains, so the two can no longer be confused.

**The three article-level fields describe the article as it stands.** `Visuals Included` (the article contains visuals or screenshots), `Video Included` (the article contains a video), `Media Update Needed` (the existing media has been flagged for a refresh). Renamed from `Visuals`, `Videos`, and `Needs Updated Video/Visuals`.

**The four production fields describe the work.** `Visual Owner`, `Visual Status`, `Video Owner`, `Video Status`, owned by the Help Center Production Tracker at `https://app.notion.com/p/3dd8b9e0143881bbbaf4ea0964bd34f9`. The tracker is a view over the same data source, not a second database, so these stay columns on the same rows and are read through the view.

**The rule the split exists to enforce:** never read an article-level media field as evidence that production work is outstanding. `Media Update Needed: Yes` means someone flagged the media for a refresh and says nothing about whether that refresh is done. Do not flag an article's visuals or video as incomplete on that basis when reviewing or scoring, and do not report a media field as an open item on a port.

The mistake is real, not hypothetical: on 2026-09-19 a session read `Video Status: Not Started` on two live articles and reported their Looms as stale on that basis alone, without checking the video.

## 2026-09-18: "tile" is banned in alt text too, and alt text takes a period

Decided by Tara during the Dashboard Overview port. **Awaiting Kelly and Rafe**, since both change `content-standards.md`.

**The alt-text exception for "tiles" is struck.** The September 15 entry below recorded it as one of three false positives the plain language grep produces. It was the wrong call, and the article that produced it shows why: the body of Dashboard Overview had been rewritten specifically to drop "is a tile that", on the reasoning that a definition saying what a thing does beats one saying what shape it is on screen. The exception then preserved in the alt text exactly the word the body had been cleaned of. Alt text stands in for the image, so it should name what a sighted reader would see named. "showing widgets across the page" says the same thing in the article's own vocabulary.

The word survives where it is the on-screen label: Tiles View on the Search page, the Perchwell tile at login, the collapsible tiles on the Listing Detail Page. That is the same on-screen-label rule the September 16 entry settled for "scope".

The no-inventory exception is untouched. Alt text may still list what is on screen, because it exists for someone who cannot see it. Listing things and naming their shape are different problems, and conflating them is how the first exception got written.

**Alt text ends with a period; a numbered step does not.** The standard was silent, so this was settled by counting across the set, the way hyphenation and bullet labels were. Every alt text attached to a placed image ran with a period, 8 of 9, against 11 of 11 without on `Screenshot placeholder:` lines, which are a different form. The count was not the deciding argument, though: a screen reader reads alt text as a sentence and uses the period as a pause, which is work the period does not do at the end of a step. A convention with a functional reason behind it is settled on the reason, not the tally.

Propagated through `content-standards.md` (the do-not list, the false-positive note, the media rules), `fin-readiness-scorecard.md` (plain language check 1), and the plain language pass in both article skills.

## 2026-09-17: Pushes to Intercom are on

Decided by Tara, porting the Universal Search Bar rewrite. This closes the 2026-09-04 decision that held the repo read-only toward Intercom until the team trusted the mirror and the review flow. Both now exist: the mirror has run clean since September 4, and four articles have been through the standard, reviewed, and scored.

- **Rung 3 is unchanged.** An update to a live article still requires all four conditions: the full before-and-after diff in the conversation, explicit confirmation for that one article with "yes to all" refused, an entry in `docs/help-center/changelog.md`, and a `/sync-help-center` afterward.
- **Rung 2 is unchanged.** A new article is created in `draft` state. Claude never sets an article to published; that stays a human action in Intercom.
- **`/port-to-intercom` is the implementation.** It carries the five preconditions from `intercom-push.md`, converts the Notion body to Intercom HTML, and closes the loop by moving the Notion row to `Live in Intercom`.

Noted while turning it on: the `ask` list in `.claude/settings.json` was not binding. It names the Intercom connector by a server ID that differs per teammate, so on a session with a different ID the article write tools fell through to the default prompt rather than the explicit one. Both IDs are now listed, and `docs/connector-tools.md` says the list is additive.

## 2026-09-17: A shared article gets one Notion row, not two

Decided by Tara during the Universal Search Bar port, settling the question `project-status.md` has carried since September 4.

One row. Intercom serves a shared article from a single record, 11002620 in this case, held in a Baldwin collection and a CRMLS collection at once. There is no second article to write to, so a second row would describe something that does not exist.

The cost is that the article's cross-links can only point into one help center. Universal Search Bar now sends CRMLS readers to four Baldwin-only articles, one of which maps Paragon terms, and Paragon is Baldwin's legacy platform rather than CRMLS's. Accepted for now, logged in `project-status.md` as a split to do later. When the split happens the article becomes two Intercom records, and only then does it become two rows.

## 2026-09-16: Agreement between sources is not verification

Decided by Tara after the Listings widget migration, from a retro on the session. **Awaiting Kelly and Rafe**, since it changes `content-standards.md`.

The standard already says what to do when sources disagree: the live article wins on facts, a newer Notion page does not outrank it, and a tie goes to product. None of that helps when the sources agree and are both wrong, which is what happened four times on one article. The live article and the old Notion page both listed a Recently Added filter the product no longer has, both omitted Active Under Contract which it does have, and both called the Add/Edit form "the listing management form". Agreement read as corroboration.

Every one was caught by a screenshot or a one-line answer from Tara, never by a check, and every one was sourced, which is the condition under which nothing flags it. That is the third and fourth time on this project that sourced-and-wrong has reached a draft.

- **The rule.** Where an article documents a screen's controls, their labels, or what a control opens, ask for a current screenshot before drafting and treat what the documents agree on as the question rather than the answer.
- **The workflow change that follows from it.** Both article skills now list the product questions they would otherwise mark `[confirm: ...]` and ask them up front, alongside the source differences. All three markers on this article closed the same day because Tara was at her desk; a marker would have taken a review cycle to reach the same answer, and the answers contradicted both documents rather than picking one.
- **A quality-checklist line** so the audit and the QA pass see it too.

Three smaller things from the same retro, all skill-level:

- **Load-bearing claims are checked in three places.** A claim that sets up the article lands in the description, the opening paragraph, and a section lead at once. This draft asserted that the widget's Search field narrows the list, with no source at all, in all three. Fixing the one you notice leaves the other two, which is how that shape survives a review.
- **`transformation-patterns.md` said to keep bold on bullet lead-in labels.** It was the last place in the repo still teaching the style retired on September 10, it contradicted Fin-parsable check 3, and it contradicted what was actually done on Universal Search Bar, where unbolding those labels is what restored 8 of 8 and 95.7. Corrected.
- **The set-consistency pass now covers the small conventions**, hyphenation of position words and whether bullet lead-in labels take a period or a colon, settled by counting across the set rather than by preference. "top right corner" runs 8 to 0 unhyphenated.

## 2026-09-16: An on-screen label licenses the control, not the vocabulary

Decided by Tara, during the Listings widget migration. The draft passed the plain language gate on the word "scope" and she caught it anyway, which is the second time in two days that a human found what a check could not.

The gate's check 3 asked one question, whether the word is on screen. "Scope" passed it, because the Listings widget's menu is headed Scope by. On the strength of that the draft went on to use the word as its own vocabulary: an H3 reading "Choose the listing scope", a lead reading "The scope sets whose listings the widget shows", and a control called "the scope button", which nothing on screen calls it. An agent looking at a button labeled MLS Listings does not know the word for it is scope.

Check 3 now asks two questions. Is the word on screen, and would a member use it when the control is not in front of them? A term that passes the first and fails the second is named once, where the member has to find the thing, and described by what it does everywhere else. The article now says "choose whose listings you see" and "the button in its top right", and uses Scope by exactly once in the body.

This is the mirror of the modal rule from September 10. There the answer was to keep a word that sounds technical; here it is to drop one that is genuinely on screen. Same check, opposite outcomes, which is why both are written down rather than left to judgment.

In `docs/standards/content-standards.md` under Voice and terminology and in the quality checklist, in `docs/standards/fin-readiness-scorecard.md` as check 3 of the plain language gate, and in the plain language pass of both article skills. No score changes: the gate is pass or fail and touches no dimension.

Noted while there: the control has no fixed on-screen label, since the button reads whichever option is selected. It is identified by position until the product gives it a stable name.

## 2026-09-15: Plain language is a gate, not a score

Decided by Tara, after reviewing the four articles migrated between September 9 and 15. All four passed 14 of 14 golden questions and scored 95.7 to 100.0, and all four still needed a hand pass on their words before the team would accept them. The scorecard could not see the defect: voice is worth 4 of its 100 points, in two prohibitions, and none of the 14 factors is a voice factor.

- **Write the word a member would type.** Name the real things, not the category that contains them: "listing, agent, or contact", not "record". Kelly's reason was retrieval rather than readability, which is what lets this sit beside the Fin rules instead of competing with them: "they will search and type into Perchie those words they know and we want to make sure we show the right answer." A word an agent would not say is a word Fin cannot match them on, so the headings change too.
- **A plain language do-not list, sense-scoped.** Each term is banned in one sense, not as a word, and each is paired with its replacement. Tested against the four finished articles first: a blanket word ban flagged "public records", "return to the Dashboard", and "tiles" inside alt text, all three legitimate and all three live in articles the team has approved. A grep finds candidates; a person decides.
- **Check a candidate before swapping it.** "Modal" was changed to "search window" during the de-jargon pass and reverted the same day, because `product-context.md` already required it, for the same Fin-matching reason Kelly was arguing. The pass was right to go past her literal list, since she asked it to; what it skipped was checking each candidate against the terminology rules first.
- **Enforced as a second gate, not as a scored check.** Pass or fail, reported next to the 14 golden questions and never blended into them, the same way Perchwell's Fin-resolved number is reported next to Intercom's. A scored check would have created revision 3, changed the Accuracy divisor from 5 to 6, and made every score in `qa/` incomparable, to move a failing article by 1.67 points and out of no band. The gate costs nothing and says the thing plainly. `Ready to Transfer` now needs all three: the Fin-ready band, the golden questions, and plain language.
- **A plainly stated benefit is not a marketing adjective.** "Together they give you a quick view across several areas of Perchwell" earns its place. The do-not list bans praise, not usefulness, and it read broadly enough to suppress both.
- **The humanizer is part of the review, not a fallback.** It was documented as "run it if the output feels stilted", and stiltedness is what the writer is worst placed to notice. Three of its patterns are overridden where they fight the house standard: its "Personality and soul" section, pattern 15 on bullet lead-in labels, and pattern 16 on heading case.

Propagated through `docs/standards/content-standards.md` (Voice and terminology, the new do-not list, the quality checklist), `docs/standards/fin-readiness-scorecard.md` (the second gate, the bands, the QA file shape), both article skills, `transformation-patterns.md` (new pattern 11), the Notion AI prompt, and the root `CLAUDE.md`. **No score changes and no rescore:** the gate adds no check to any dimension and moves no divisor, so revision 2 numbers stand.

Also corrected while in these files: three places still teaching the bold style retired on September 10, in transformation patterns 2 and 5, in `transformation-patterns.md`, and in `docs/product-context.md`, whose Feature names line contradicted its own terminology rule twelve lines below it. The root `CLAUDE.md` carried the same stale instruction and a retired screenshot placeholder format.

**What this does not settle.** The FAQ exception to the "you can" ban is still open, owned by Tara and Kelly and overdue from September 11. The plain language gate does not touch it. The verb pass, the possessive-density pass, and the list-order pass still live only inside the two skills, duplicated word for word and absent from the standard; consolidating them is a separate job.

## 2026-09-10: Four standard changes from the first article review

Decided by Tara, after the team read the Universal Search Bar migration. Three of the four traced to the standard rather than to the skill: the skill wrote what the rules told it to write.

- **MLS ID is the term.** Never "MLS number," "MLS #," or "listing number," in articles, macros, or replies. Perchwell labels the filter and the listing card **MLS ID**, and the live help center used both terms, sometimes in the same article. Recorded in the `docs/product-context.md` glossary and terminology rules.
- **Silence means every member.** A role is named only where a role gates the workflow or changes the behavior. A sentence saying everyone has the feature tells the member nothing and pushes their answer down the page. An availability claim paired with a `[confirm: ...]` marker now fails the audience factor rather than passing it. The Notion `Roles` property still records the audience either way.
- **Constraints are written as the route forward.** No Limitations section by default, and no hunting for downsides. A constraint the member will hit is stated where they meet it, as the alternative path: "To look up several listings at once, open the **Search** page and enter the IDs in the **MLS ID** filter." A dedicated section is reserved for a hard cap with an exact number that a member hits mid-workflow, or something irreversible; the 1004MC report's 500-listing cap is the model case, kept because suppressing it would generate the tickets the help center exists to prevent.
- **Say each fact once.** The feature name repeats in every section so a retrieved section identifies itself. The facts attached to it do not. Golden question 8 asks for entities, not facts, and reading it loosely produced a draft that stated the same three record types six times in 84 lines.
- **Articles never name a legacy platform.** Members came from different systems depending on their MLS, and one article serves several, so articles say "a legacy platform" and keep the legacy feature name the member would recognize and search for. Conversation replies and macros are exempt, because you know which MLS you are talking to. In the root `CLAUDE.md`, `docs/product-context.md`, the content standard, the scorecard's accuracy check 4, and the article and macro skills. Open consequence: genericizing prose does not make an article portable while its internal links still point at one MLS's help center.
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

Decided by Tara. The team created a new Notion database for this project to simplify the work and make each article's state obvious, and set its properties the way they want them. For the rest of this project, an article we draft or update is added to the new database. The old Master Article List is read-only: query it for history, never write to it, and do not mirror a change back into it. `Article Name`, `Article Status`, `MLS/AOR`, `Collection`, `Roles`, `Video Included`, `Visuals Included`, `Media Update Needed`, plus the four production fields covered in the 2026-09-16 entry. Database `https://app.notion.com/p/3d18b9e0143880558dc9d9574f5abab8`, data source `collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389`.

One consequence to watch: `docs/standards/fin-labeling.md` derives labels from `MLS/AOR` and `Collection` plus the article's shape, never from the media fields.

The media fields were renamed and their meaning settled on 2026-09-16; see that entry. This entry originally said the database had no equivalent of the old per-asset workflow-status fields, which was wrong: `Visual Status` and `Video Status` were columns from the start.

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
