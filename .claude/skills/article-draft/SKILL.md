---
name: article-draft
description: Draft new Perchwell help center articles, or propose updates to existing ones, from feature release notes. Use this skill whenever the user mentions "help center article," "help article," "write a help doc for," "document this feature for the help center," "release notes to help center," "does this need a new article," "what help center changes does this need," or pastes release notes and asks what support documentation should change. It reads docs/standards/ (including the content standards and the 14 golden questions) and the local Intercom mirror, checks the Notion help center database to decide new article vs. update, saves markdown to the repo, and creates a Draft page in Notion for review. Intercom is never written to by this skill today.
---

# Article Draft

Turn feature release notes into help center content that matches the live Baldwin and CRMLS help centers. The reader is a busy real estate agent, broker, admin, or MLS staffer on support.perchwell.com who needs the answer fast; the voice is matter-of-fact and instructional, not marketing. The CS team owns the help center; this skill produces review-ready drafts in the team's review layer, Notion, and stops there.

## Inputs

- **Release notes** (required): pasted text, a repo path, or a Notion link. Read the whole thing before extracting.
- **MLS scope** (optional, default Baldwin): which help center the article belongs in. Baldwin or CRMLS.
- **Media** (optional): Loom, Arcade, or screenshot links. Without them, the draft carries placeholders.
- **Mode hints** (optional): "just draft it" skips the triage confirmation; "triage only" stops after the decision table; "no notion" skips the Notion write.

If the release notes leave out a UI label, a default, a limit, or a step, do not invent it. Write `[confirm: <what is missing>]` inline and list every marker under Open items. A draft with three confirm markers is more useful than a fluent one that is wrong.

Two sibling articles agreeing on a label is not verification either; documents written from the same screen go stale together. Where the draft documents a screen's controls, their labels, or what a control opens, list those questions and ask them before drafting rather than marking them after. A teammate at their desk answers in minutes what a marker takes a review cycle to resolve, and the answer often contradicts every document rather than matching one.

## Workflow

1. **Read context.** Read `docs/standards/content-standards.md` in full. It is the standard; everything about titles, structure, headings, steps, callouts, voice, media, and formatting lives there, and it carries the quality checklist this skill runs in step 6. Read `docs/product-context.md` for feature names, roles, and terminology, including the legacy platform transition rules.
2. **Extract the feature facts.** Fill the fact table in `references/triage-rubric.md` (Step 1) from the release notes only. Every blank becomes a `[confirm: ...]` marker.
3. **Check the mirror.** Scan the local mirror index for the MLS in scope, `docs/help-center/baldwin/README.md` or `docs/help-center/crmls/README.md`, for articles in the same area. Open the likely candidates; each file carries the article's Intercom ID, public URL, collection, and state in its frontmatter, which is what the triage table and cross-links need. If `sync-state.json` in that folder shows the last run is more than a week old, suggest `/sync-help-center` before relying on it.
4. **Triage against Notion.** Run the queries in `references/notion-publishing.md` against the Perchwell Help Center Database [Sep 2026], and against the old Master Article List for history. Fetch the bodies of the live candidates not already read from the mirror. Skim one or two sibling articles in the same area so headings and phrasing match the neighbors. Apply `references/triage-rubric.md` to reach one decision: A new article, B update, C both, D no change. Present the triage table and wait for confirmation unless the user said to just draft it.
5. **Draft.** New articles follow `references/article-template.md` and are modeled on `references/example-article.md`. Updates use the update change sheet in `references/article-template.md`: one file per release, one heading per affected article, each edit written once as `"current" -> "proposed"`, paste-ready text only for sections that are new or fully rewritten, and a single tagged open-items list. Never reproduce untouched sections and never restate the release per article. Apply the standard silently; the article never talks about its own rules.
6. **Self-review.** Run the 14 golden questions (Intercom's content readiness factors) in `docs/standards/golden-questions.md` against the draft and list every one that fails, with the fix or the question for the user; do not invent limits, roles, or numbers to satisfy a factor, and read factors 7, 8, and 13 through the house resolutions at the end of that file. Then run the quality checklist at the end of `docs/standards/content-standards.md` and grep the draft for em dashes, "you can," "allows you to," "able to," the verb "use," "MLS number," "MLS #," and the marketing do-not list. Then grep for `**` and confirm every hit is a callout label or the `**Description:**` line; nothing else in the body is bold. Then run the verb pass: grep for "appear", "appears", "display", and "displays", and for each hit confirm the member is acting on the product rather than the screen acting back, as in "adjust which widgets display" over "change which widgets appear"; a sentence whose subject is genuinely the system, such as "the widget updates automatically", is correct as written. In the same pass, check possessive density: where "your" appears more than twice in one sentence or repeats before every item in a list, let one "your" govern the run, as in "your contacts, saved searches, tags, and listings" rather than "your contacts, your saved searches, your tags, and your listings", and drop it where it earns nothing, as in "near the upper left" rather than "near the upper left of your screen". Keep it where it separates the member's own things from everyone else's ("your own listings", "your MLS permissions"), and never touch it inside a linked article's exact title. Then run the plain language pass: grep the draft for the plain language do-not list in `docs/standards/content-standards.md`, read every hit in context rather than trusting the grep, and keep the ones the list does not actually ban, as in "public records", "return to the Dashboard", and "tiles" inside alt text. Then read the description, the opening paragraph, and every heading as an agent would, and name any word an agent would not say out loud. Ask two questions of every term that reads as product vocabulary, not one: is the word on screen, and would a member use it when the control is not in front of them? A term that passes the first and fails the second belongs at the moment the member has to find the thing and nowhere else, so name the label once there and say what the control does everywhere else. Before swapping any term, check it against the terminology rules in `docs/product-context.md` and against the on-screen label; "modal", MLS ID, Saved Search, Hot Sheet, and timeframe are settled and stay. In the same pass, confirm that no sentence restates the `Steps:` block in the abstract, and that the verb a member would type for the task appears in the section that covers it rather than only inside a link's title. Then run the list-order pass: take every enumeration in the opening paragraph and in each section's lead sentence, and confirm the sections that follow run in the same order and that every listed item has a section behind it. Then run the redundancy pass: list every distinct fact in the draft and confirm each appears in exactly one section. Then check the load-bearing claims: a claim that sets up the article is written into the description, the opening paragraph, and a section lead at once, so confirm all three against the same source rather than spot-checking one. That shape is how an unsourced claim survives a review, because fixing the sentence you noticed leaves the other two. Last, check that no sentence claims every member has the feature and that no availability claim sits next to a `[confirm: ...]` marker that undercuts it. Fix everything, then score the draft once with `docs/standards/fin-readiness-scorecard.md`, run both gates, and report the band with any failed checks and the plain language gate's result alongside the golden questions.
7. **Save markdown.** See Saving the output.
8. **Publish to Notion as a Draft.** Follow `references/notion-publishing.md`: read the Notion markdown spec once per session, convert the body, summarize the page and properties in one compact block, wait for "go," then create the page in the Perchwell Help Center Database [Sep 2026] with `Article Status: Draft`. Update change sheets go wherever the user points; if no target is given, create one sibling row titled `Help center changes: <feature> (YYYY-MM-DD)`. Never write to the old Master Article List, and never overwrite a page whose `Article Status` is `Live in Intercom`.
9. **Stop at the Notion draft.** Do not call any Intercom write tool from this skill. The transfer is `/port-to-intercom`, run after a person has reviewed the draft and moved the row to `Ready to Transfer`; `references/intercom-push.md` holds the rules it follows.
10. **Report.** State the decision, the saved path(s), the Notion URL(s), the golden questions that fail and why, the open `[confirm: ...]` items, and what remains: peer review in Notion, move the row to `Ready to Transfer`, then `/port-to-intercom`, which handles the transfer and the image alt text. Fin labels, MLS audience, and publishing stay manual. The full checklist is under "After publishing" in `references/notion-publishing.md`.

## Rules

The rulebook is `docs/standards/content-standards.md`. Do not restate it here and do not keep a second copy of it in this skill; when the standard changes, this skill follows automatically. The four things worth repeating because they are how drafts most often go wrong:

- **Accuracy.** Every fact traces to the release notes, the mirror, or a live Notion page. Unknowns are `[confirm: ...]`, never guesses. Quote current text exactly in update change lists.
- **Fin retrieves sections, not articles.** Each section has to identify itself and stand alone: the heading names what the section answers and carries the feature name, and the first sentence under it echoes the heading's terms.
- **Golden questions are a gate, not a suggestion.** All 14 in `docs/standards/golden-questions.md` pass, or the failures are reported with the fix or the question.
- **Write nothing outside the draft.** Never edit a mirror file; only `/sync-help-center` writes to `docs/help-center/`. Never write to Intercom. Never write to the old Master Article List.

## Saving the output

- New article: `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<slug>.md`
- Update change sheet: `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<feature-slug>-changes.md` (one file per release, all affected articles inside)
- Line 3 of every file is the metadata comment: `<!-- Article Status: Draft | MLS/AOR: <Baldwin or CRLMS All> | Collection: <Collection> | Roles: <Roles> | Videos: <Yes or No> | Visuals: <Yes or No> | Notion: <page url> -->` (add the Notion URL after the page exists). Change sheets use the header from the change-sheet template instead.
- Do not add drafts to the mirror index. The mirror reflects Intercom only.
- Re-running the skill on the same feature the same day overwrites the file. A later day creates a new dated file and the report links the previous one.

## Handoffs

- Stilted output: run `/humanizer` on the saved file, then re-run the quality checklist, since the humanizer reintroduces "you can", which is a scored failure. Its "Personality and soul" section, pattern 15 (it collapses the bullet lead-in labels the standard keeps), and pattern 16 (it sentence-cases headings the naming standard wants in title case) are overridden by the house standard. `.claude/skills/article-rewrite/SKILL.md` lists which of its patterns apply.
- Rewriting an old article for style with no release notes involved, migrating an article from the old Master Article List into the new database, or scoring an existing article for Fin: `/article-rewrite`.
- Support macros for the same feature: `/intercom-macros`.

## Worked example

Release notes (abridged): "Market Conditions Addendum Report (1004MC). From Search, select listings or leave all selected, then Actions > Create a Report > Market Conditions Addendum Report. Options: report max date (defaults to today, anchors the three periods: current 3 months, prior 4 to 6, prior 7 to 12), stable range high and low limit % (default 0%), checkbox to remember the range, checkbox to include search criteria and listing summary. Max 500 listings. Missing fields exclude a listing from that metric only. Available to all roles except invited clients."

Fact table highlights: collection Reports; entry point Search > Actions > Create a Report; limits 500 listings; defaults: max date today, stable range 0%; roles All Except Client; media none yet.

Mirror check finds the Reports collection articles in `docs/help-center/baldwin/` (Print Reports for Appointments, Reports FAQ, Create a Listing Report), none covering 1004MC. Notion triage adds Appraiser Capabilities in Perchwell.

```
Decision: C. New article, plus two light updates. No existing article covers the 1004MC report; two siblings should point to it.

| Candidate article | Article Status | Why it is affected | Action |
|---|---|---|---|
| (new) Create a Market Conditions Addendum Report (1004MC) | | No article covers 1004MC | New article |
| Appraiser Capabilities in Perchwell | New Article Request | Lists appraiser tools; should name the report | Update: add bullet and a link |
| Reports FAQ | Live in Intercom | Members may ask which report supports 1004MC | Update: add one Q&A |

Open items: [confirm: exact label of the "remember stable range" checkbox] [confirm: whether the report can be exported to PDF from inside Perchwell or only via browser print]
```

After confirmation, the new article is drafted from the workflow template, saved to `workstreams/help-center-overhaul/outputs/drafts/2026-08-14-create-a-market-conditions-addendum-report.md`, and created in the Perchwell Help Center Database [Sep 2026] as a Draft with Collection `Reports`, MLS/AOR `Baldwin`, Roles `All Except Client`, Visuals `Yes`, Videos `No`. The two updates go in one change sheet, `2026-08-14-market-conditions-addendum-report-changes.md`, published as a single Notion page. The report closes with the manual CS steps that remain.
