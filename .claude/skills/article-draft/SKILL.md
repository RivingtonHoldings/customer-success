---
name: article-draft
description: Draft new Perchwell help center articles, or propose updates to existing ones, from feature release notes. Use this skill whenever the user mentions "help center article," "help article," "write a help doc for," "document this feature for the help center," "release notes to help center," "does this need a new article," "what help center changes does this need," or pastes release notes and asks what support documentation should change. It reads docs/standards/ and the local Intercom mirror, checks the Notion Master Article List to decide new article vs. update, saves markdown to the repo, and creates a Draft page in Notion for review. Intercom is never written to by this skill today.
---

# Article Draft

Turn feature release notes into help center content that matches the live Baldwin and CRMLS help centers. The reader is a busy real estate agent, broker, admin, or MLS staffer on support.perchwell.com who needs the answer fast; the voice is matter-of-fact and instructional, not marketing. The CS team owns the help center; this skill produces review-ready drafts in the team's review layer, Notion, and stops there.

## Inputs

- **Release notes** (required): pasted text, a repo path, or a Notion link. Read the whole thing before extracting.
- **MLS scope** (optional, default Baldwin): which help center the article belongs in. Baldwin or CRMLS.
- **Media** (optional): Loom, Arcade, or screenshot links. Without them, the draft carries placeholders.
- **Mode hints** (optional): "just draft it" skips the triage confirmation; "triage only" stops after the decision table; "no notion" skips the Notion write.

If the release notes leave out a UI label, a default, a limit, or a step, do not invent it. Write `[confirm: <what is missing>]` inline and list every marker under Open items. A draft with three confirm markers is more useful than a fluent one that is wrong.

## Workflow

1. **Read context.** Read `docs/standards/content-standards.md` first; if it is still a placeholder, say so in the report and use `references/style-rules.md` as the fallback. Read `references/style-rules.md` in full either way. Read `docs/product-context.md` for feature names, roles, and terminology, including the Paragon transition rules.
2. **Extract the feature facts.** Fill the fact table in `references/triage-rubric.md` (Step 1) from the release notes only. Every blank becomes a `[confirm: ...]` marker.
3. **Check the mirror.** Scan the local mirror index for the MLS in scope, `docs/help-center/baldwin/README.md` or `docs/help-center/crmls/README.md`, for articles in the same area. Open the likely candidates; each file carries the article's Intercom ID, public URL, collection, and state in its frontmatter, which is what the triage table and cross-links need. If `sync-state.json` in that folder shows the last run is more than a week old, suggest `/sync-help-center` before relying on it.
4. **Triage against the Master Article List.** Run the queries in `references/notion-publishing.md` (by product area, by title keyword, by Intercom collection, plus rows already flagged for update). Fetch the bodies of the live candidates not already read from the mirror. Skim one or two sibling articles in the same area so headings and phrasing match the neighbors. Apply `references/triage-rubric.md` to reach one decision: A new article, B update, C both, D no change. Present the triage table and wait for confirmation unless the user said to just draft it.
5. **Draft.** New articles follow `references/article-template.md` and are modeled on `references/example-article.md`. Updates use the update change sheet in `references/article-template.md`: one file per release, one heading per affected article, each edit written once as `"current" → "proposed"`, paste-ready text only for sections that are new or fully rewritten, and a single tagged open-items list. Never reproduce untouched sections and never restate the release per article. Apply the style rules silently; the article never talks about its own rules.
6. **Self-review.** Run the quality checklist at the end of `references/style-rules.md`. Also grep the draft for em dashes, "you can," "allows you to," "able to," the verb "use," and the marketing do-not list. Fix everything before saving.
7. **Save markdown.** See Saving the output.
8. **Publish to Notion as a Draft.** Follow `references/notion-publishing.md`: read the Notion markdown spec once per session, convert the body, summarize the page and properties in one compact block, wait for "go," then create the page. New articles become a new row with `HC Status: Draft`. Update change sheets go wherever the user points (a launch task page, a release note, a Master Article List row); if no target is given, create one sibling row titled `Help center changes: <feature> (YYYY-MM-DD)`. The live pages are never overwritten. Offer, but do not assume, to flag the source rows `Update Needed`.
9. **Intercom push: not implemented.** Do not call any Intercom write tool. `references/intercom-push.md` describes the future step and its preconditions; today the report ends with the manual steps in step 10.
10. **Report.** State the decision, the saved path(s), the Notion URL(s), the open `[confirm: ...]` items, and the manual CS steps that remain: peer review in Notion, transfer to Intercom as a draft, public URL, Fin label, MLS audience, publish.

## Rules

**Titles.** Title Case. No gerunds, no questions. Task-based and front-loaded. "How to ..." only for one specific feature. Overviews are "<Page> Overview," FAQs are "<Area> FAQ."

**Structure.** One primary goal per article. `## In this article:` then "You will learn how ..." Sections in sentence case, descriptive, grouped under parent headings. Order: what it is and when to use it, create or start, customize, share or export, Things to Know. `### Steps:` with numbered one-action steps and no terminal periods. Key workflows begin on **Search**. Tables for multi-path workflows. Support footer at the end.

**Voice.** Second person, imperative, active. Cut "you can," "allows you to," and the verb "use." Name the UI element the reader sees and bold it. State defaults, limits, and what cannot be undone. Translate system terms with a "which means" clause. No marketing adjectives. No internal names or jargon. Hedge predictions about people.

**Formatting.** Bold clickable elements, filters, buttons, nav items, and status labels; never concepts. Emoji-led blockquote callouts: 💡 tip, ⚠️ notice, 📖 related article, 📹 video, ⚒️ legacy vs Perchwell. Vary link phrasing; never "click here." No em dashes, no horizontal rules, no HTML. Media placeholders where a screenshot or video belongs.

**Accuracy.** Every fact traces to the release notes, the mirror, or a live Notion page. Unknowns are `[confirm: ...]`, never guesses. Quote current text exactly in update change lists. Never edit a `Live ✅` Notion page. Never edit a mirror file; only `/sync-help-center` writes to `docs/help-center/`.

## Saving the output

- New article: `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<slug>.md`
- Update change sheet: `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<feature-slug>-changes.md` (one file per release, all affected articles inside)
- Line 3 of every file is the metadata comment: `<!-- Status: Draft | MLS: <Baldwin or CRMLS> | Collection: <Collection in Intercom> | Roles: <Roles> | Notion: <page url> -->` (add the Notion URL after the page exists). Change sheets use the header from the change-sheet template instead.
- Do not add drafts to the mirror index. The mirror reflects Intercom only.
- Re-running the skill on the same feature the same day overwrites the file. A later day creates a new dated file and the report links the previous one.

## Handoffs

- Stilted output: run `/humanizer` on the saved file, then re-run the quality checklist, since the humanizer may reintroduce "you can."
- Rewriting an old article for style with no release notes involved: `/article-rewrite`.
- Support macros for the same feature: `/intercom-macros`.

## Worked example

Release notes (abridged): "Market Conditions Addendum Report (1004MC). From Search, select listings or leave all selected, then Actions > Create a Report > Market Conditions Addendum Report. Options: report max date (defaults to today, anchors the three periods: current 3 months, prior 4 to 6, prior 7 to 12), stable range high and low limit % (default 0%), checkbox to remember the range, checkbox to include search criteria and listing summary. Max 500 listings. Missing fields exclude a listing from that metric only. Available to all roles except invited clients."

Fact table highlights: product area Presentation & Reports; entry point Search > Actions > Create a Report; limits 500 listings; defaults: max date today, stable range 0%; roles All - but client; media none yet.

Mirror check finds the Reports collection articles in `docs/help-center/baldwin/` (Print Reports for Appointments, Reports FAQ, Create a Listing Report), none covering 1004MC. Notion triage adds Appraiser Capabilities in Perchwell (New Article Request).

```
Decision: C. New article, plus two light updates. No existing article covers the 1004MC report; two siblings should point to it.

| Candidate article | HC Status | Update Status | Why it is affected | Action |
|---|---|---|---|---|
| (new) Create a Market Conditions Addendum Report (1004MC) | | | No article covers 1004MC | New article |
| Appraiser Capabilities in Perchwell | New Article Request | Transfer to Intercom | Lists appraiser tools; should name the report | Update: add bullet + 📖 link |
| Reports FAQ | Live ✅ | Updated ✅ | Readers may ask which report supports 1004MC | Update: add one Q&A |

Open items: [confirm: exact label of the "remember stable range" checkbox] [confirm: whether the report can be exported to PDF from inside Perchwell or only via browser print]
```

After confirmation, the new article is drafted from the workflow template, saved to `workstreams/help-center-overhaul/outputs/drafts/2026-08-14-create-a-market-conditions-addendum-report.md`, and created in Notion as a Draft with Product Area `Presentation & Reports`, Collection `Reports`, Roles `All - but client`, Screenshot `New Screenshots`, Video `New Video`. The two updates go in one change sheet, `2026-08-14-market-conditions-addendum-report-changes.md`, published as a single Notion page. The report closes with the manual CS steps that remain.
