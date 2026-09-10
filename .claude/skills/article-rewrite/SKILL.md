---
name: article-rewrite
version: 2.0.0
description: "Rewrite, migrate, or score an existing Perchwell help center article. Use when the user wants to update, improve, or rewrite an existing article for style and clarity without new release notes; when they want to migrate an old article from the Notion Master Article List into the Perchwell Help Center Database [Sep 2026] ('move this article to the new database', 'migrate this article', 'old Notion article', 'run this article through the new standard'); or when they want an article scored for Fin ('score this article for Fin', 'how Fin-ready is this', 'rank this article'). Also use when the user mentions 'help center,' 'help article,' 'knowledge base article,' 'support article,' 'update this article,' 'rewrite this help doc,' 'improve this help page,' pastes a Notion article URL, or points at a file under docs/help-center/. Applies the content standard, the ten transformation patterns, the 14 golden questions, and the Fin-readiness scorecard, saves the draft and QA file to the repo, and creates a Draft page in the new Notion database. Intercom and the old Master Article List are never written to."
---

# Help Center Article Rewriter and Migrator

> For net-new articles from release notes, or deciding what a feature release changes in the help center, use `/article-draft` (`.claude/skills/article-draft/`). This skill covers an article that already exists: rewriting it, migrating it into the new Notion database, and scoring it for Fin.

You are an experienced support professional updating help center articles for Perchwell. Your goal is to make articles clearer, more actionable, and easier for busy real estate professionals to scan, and to make them retrievable by Fin, which answers members from sections of published articles rather than whole articles.

## Inputs

One of three:

- **An old Notion page URL** from the Master Article List (`collection://1c78b9e0-1438-80b8-951d-000bc128f119`). This is the migration case: the article is rewritten to the standard and created as a Draft in the Perchwell Help Center Database [Sep 2026].
- **A mirror path** under `docs/help-center/baldwin/` or `docs/help-center/crmls/`, or an article name that can be found in the folder's `README.md` index.
- **Pasted text.** Works, but the result cannot be traced to a live article, so say so in the report.

Mode hints:

- "no notion": rewrite and score, save the files, skip the Notion write.
- "score only": ingest and run the scorecard on the article as it stands. No rewrite, no Notion write. Use this for the audit backlog.
- "just do it": skip the source-difference and title confirmations and go straight to the Notion "go" summary.

## Before editing

**Read the standards first.** Read `docs/standards/content-standards.md` in full. It is the rulebook, and where it and this file ever differ, it wins. Read `docs/standards/golden-questions.md` (the 14 factors the rewrite has to pass) and `docs/standards/fin-readiness-scorecard.md` (how the before-and-after score is calculated). Read `docs/product-context.md` for feature names, roles, and terminology, including the legacy platform transition voice.

**Get the live article from the mirror whenever one exists.** The mirror is what members and Fin see today. If `sync-state.json` in the mirror folder shows a `last_run` more than a week old, suggest `/sync-help-center` before relying on it.

## Workflow

1. **Ingest.**
   - Notion URL: fetch the page with the Notion connector's fetch tool. Read its properties (`Resource Title`, `Collection in Intercom`, `MLS`, `Roles`, `Video`, `Video Links`, `Screenshot`, `Help Center URL (Public)`, `HC Status`, `MLS update notes`). Take the Intercom article ID from the last path segment of `Help Center URL (Public)` (the digits before the slug), then grep `intercom_id: "<id>"` across `docs/help-center/*/` to find the mirror file(s). Read both bodies.
   - Mirror path or name: read the file. Its frontmatter carries the Intercom article ID, content ID, public URL, collection, state, and labels; keep them with the rewrite so the reviewer knows which live article it replaces.
   - **Shared articles.** The same `intercom_id` appearing in both `baldwin/` and `crmls/` means the article is shared through a collection that sits in both help centers. Flag it: the new database's `MLS/AOR` is single-select, so the draft goes in under one MLS and the shared status goes in Open items for the team.
2. **Diff the sources.** When there is both an old Notion body and a live mirror body, list every fact, step, bullet, and tip that appears in one and not the other, or reads differently. The live mirror wins on facts because it is newer and it is what members see. The old Notion page supplies the video link, the properties, and the click script as a hint for the article's outcomes. Show the differences to the user before drafting unless they said "just do it"; never merge them silently.
3. **Score the original.** Run the scorecard in `docs/standards/fin-readiness-scorecard.md` against the live article as it stands: gate (14 golden questions) and the five dimensions. Record the checks that fail; they are the rewrite's worklist.
4. **Map properties.** For a migration, fill the new database's seven properties from the old row using the mapping table under "Migrating a row from the Master Article List" in `.claude/skills/article-draft/references/notion-publishing.md`. Anything the table cannot resolve becomes a question in the confirmation summary, never a guess. Run the duplicate check query from the same section; if a row with the same `Article Name` already exists in the new database, stop and ask.
5. **Choose the article type and title.** Workflow, Overview, or FAQ, per `docs/standards/content-standards.md`. Take the skeleton from `.claude/skills/article-draft/references/article-template.md` and model the result on `.claude/skills/article-draft/references/example-article.md`. When the old title is a bare noun ("Universal Search Bar"), propose a task-led title per the naming standard and offer the old one as the alternative; the user picks. Record the old title in the report either way.
6. **Rewrite** with the ten transformation patterns below. What to drop from an old article: the `In this article:` heading, horizontal rules, emoji-led lines and emoji pointers, the "Click Script" toggle (it is a video script, not article content), the trailing Perchwell banner image, the "Connect with our Support Team" footer, and any `NYC|` or internal prefix. What to carry: the Loom or Arcade URL, placed directly under the opening paragraph; every image, as the real image with alt text when its URL is a stable Intercom CDN link, or as a screenshot placeholder carrying the alt text otherwise; the legacy-platform comparison, with the platform name genericized to "a legacy platform" and the legacy feature name kept. Apply the standard silently; the article never talks about its own rules.
7. **Self-review.** Run the 14 golden questions and list every one that fails with the fix or the question for the user. Then run the quality checklist at the end of `docs/standards/content-standards.md`. Then grep the draft for em dashes, "you can", "allows you to", "able to", the verb "use" outside the accepted exceptions, "MLS number", "MLS #", and the marketing do-not list. Then grep for `**` and confirm every hit is a callout label or the `**Description:**` line; nothing else in the body is bold. Then run the verb pass: grep for "appear", "appears", "display", and "displays", and for each hit confirm the member is acting on the product rather than the screen acting back, as in "adjust which widgets display" over "change which widgets appear"; a sentence whose subject is genuinely the system, such as "the widget updates automatically", is correct as written. In the same pass, check possessive density: where "your" appears more than twice in one sentence or repeats before every item in a list, let one "your" govern the run, as in "your contacts, saved searches, tags, and listings" rather than "your contacts, your saved searches, your tags, and your listings", and drop it where it earns nothing, as in "near the upper left" rather than "near the upper left of your screen". Keep it where it separates the member's own things from everyone else's ("your own listings", "your MLS permissions"), and never touch it inside a linked article's exact title. Then run the list-order pass: take every enumeration in the opening paragraph and in each section's lead sentence, and confirm the sections that follow run in the same order and that every listed item has a section behind it. Then run the redundancy pass: list every distinct fact in the draft and confirm each appears in exactly one section, collapsing any enumeration that shows up twice. Last, check that no sentence claims every member has the feature, and that no availability claim sits next to a `[confirm: ...]` marker that undercuts it. Fix everything before scoring.
8. **Score the rewrite.** Same scorecard, then the delta per dimension and in total. Write the five to eight Fin test questions and mark, for each, whether the old and the new article answer it from one section.
9. **Save the draft** to `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<slug>-rewrite.md`. Top of file: the mirror frontmatter, plus `source_notion_url: <old page url>` and `migrated_from: master-article-list` for a migration. Then a blank line and the metadata comment `<!-- Article Status: Draft | MLS/AOR: <value> | Collection: <value> | Roles: <value> | Videos: <Yes or No> | Visuals: <Yes or No> | Notion: <page url once created> | Old title: <old title, if changed> -->`, then the article. Never edit the mirror file itself; only `/sync-help-center` writes there.
10. **Save the QA file** to `workstreams/help-center-overhaul/qa/YYYY-MM-DD-<slug>.md` in the shape given in the scorecard standard. No member identifiers.
11. **Publish to Notion as a Draft.** Skip if the user said "no notion" or "score only". Follow `.claude/skills/article-draft/references/notion-publishing.md` exactly: read `notion://docs/enhanced-markdown-spec` once per session, convert the body with the markdown-to-Notion mapping, show the compact page-and-properties summary, wait for "go", then create the page in data source `3d18b9e0-1438-80cc-ab0f-000bf0fc1389` with `Article Status: Draft`. Write the new page URL back into the draft's metadata comment.
12. **Report.** Old title and new title; before-and-after score, band, and delta per dimension; golden questions that still fail and why; the source differences and which side won; the property mapping and any decision taken; open `[confirm: ...]` items; the Notion URL; and the manual CS steps that remain: peer review in Notion, `Ready to Transfer`, transfer to Intercom as a draft, Fin labels per `docs/standards/fin-labeling.md`, MLS audience, publish.

## Rules

- **Accuracy.** Every fact traces to the live article, the old Notion page, or a sibling live article. Unknowns are `[confirm: ...]`, never guesses. A draft with three confirm markers is more useful than a fluent one that is wrong.
- **Never strengthen a hedged source.** "Statuses like Active and Pending" becomes "statuses such as", never "every status". "Results populate as you type" does not become "results appear in a panel below the field". Both of those escaped into the first migration, because the more confident sentence reads better and nothing marks it as invented. After rewriting, diff every factual claim against the source sentence it came from and check that the rewrite is not more certain, more complete, or more specific than what it was built on. A claim with no source sentence at all does not belong in the draft, however reasonable it sounds.
- **A `[confirm: ...]` marker covers only what it names.** Marking a detail does not license the sentence holding it. The first migration asserted that the feature works the same way on mobile as in the browser and marked only the location as unconfirmed; the location was fine to ask about and the behavior claim was false. Mark the claim, or leave the sentence out.
- **Fin retrieves sections, not articles.** Each section identifies itself: the heading names what it answers and carries the feature name, and the first sentence echoes the heading.
- **Golden questions are a gate, not a suggestion.** All 14 pass, or the failures are reported with the fix or the question.
- **Write nothing outside the draft and the QA file.** Never edit a mirror file. Never write to Intercom. Never write to the old Master Article List, not even to update its status. Never overwrite a row in the new database whose `Article Status` is `Live in Intercom`.
- **Legacy platforms are never named in an article.** One article serves more than one MLS, and members came from different systems, so write "a legacy platform" and keep the legacy feature name, which is the term a member actually searches for: "Members who came from a legacy platform may know the Universal Search Bar as Power Search." Migrating an older article means genericizing the platform name it carries. Never "old system", "retired", or "sunsetted".
- **No em dashes, no horizontal rules, no emoji.**

## Transformation patterns

Apply these ten patterns when rewriting. `references/transformation-patterns.md` has before-and-after examples of each.

### 1. Jobs-to-be-done opening
Every article opens with one paragraph stating what the reader will accomplish, not what the article is about: "Use this article to <outcome 1>, <outcome 2>, and <outcome 3>." Name the feature in the sentence. Say who the article is for only when a role gates the workflow; when every member has the feature, say nothing. Retire the older "In this article:" heading and the "You will learn how..." phrasing; both describe the topic instead of the outcome, and Intercom names that the weaker form.

### 2. Specific over vague
Replace generic descriptions like "allows you to stay connected by storing information" with concrete actions: "Filter by **Recently Created** or **New**." Name the actual UI elements the reader will see.

### 3. Grouped structure
Consolidate related content under meaningful parent headings. If five widgets each have their own H2, group them under a single section instead. Remove standalone sections that state the obvious.

### 4. Bullet-point capabilities
Expand single-sentence feature descriptions into a short lead sentence plus a bullet list of specific things the reader can do. One concrete action or option per bullet. Expand into actions, never into an inventory of what is on screen: a bullet list of the fields a listing card renders is longer than the sentence it replaced and answers nothing the member cannot already see.

### 5. Imperative voice
Remove "You can" and "allows you to." Instead of "You can use the Manage widgets button to customize your layout," write "Click **Manage widgets** to customize your layout." Tell the reader what to do, not what the system permits.

### 6. Descriptive section titles
Make section titles specific enough that a reader scanning the page can find what they need, and specific enough that Fin can tell what the section answers when it retrieves it alone. Carry the feature name into the heading, then echo the heading's key terms in the first sentence beneath it, since Fin sometimes misses headings in the HTML.

### 7. Callout labels and varied link phrasing
Callouts lead with a bold label: **Note:** for system behavior, **Important:** for a limit or something irreversible, **Tip:** for a recommendation. Intercom says the bold label is what marks a passage for Fin to carry into an answer, so drop the old emoji-led callouts. Links to related articles are ordinary sentences, not callouts, and their phrasing varies. Never "click here" or "view our article here."

### 8. Coverage gaps
Look for features, options, and workflows that exist in the product but are missing from the article, and for steps that stop short of what happens next. Add what a sibling live article confirms. Mark anything you are not sure exists as `[confirm: ...]` rather than inventing it. This is a hunt for missing capabilities, not for shortcomings: add a constraint only when a member will hit it, and write it as the route forward in the section where they meet it.

### 9. Name UI elements exactly, and do not bold them
Name every clickable element, filter, button, menu item, and navigation target by its exact on-screen label. Do not bold any of them. Bold survives in two places only: the callout labels **Note:**, **Important:**, and **Tip:**, which Intercom names as the signal Fin reads, and the `**Description:**` line. Migrating an older article means stripping its bold, since the previous house style bolded every UI element.

### 10. Say it once
The feature name repeats in every section; the facts attached to it do not. Give each fact one canonical home, and when a later section needs one that lives elsewhere, name that section or link the article instead of restating it. Two sections that enumerate the same capabilities mean one of them is doing no work. The first migration test stated the same three record types six times in 84 lines, which is the worked example in `references/transformation-patterns.md`.

## Output format

- H1 for the article title and nothing else; H2 for major sections; H3 for subsections and the `Steps:` heading
- `**Description:**` line, then the opening paragraph with no heading above it, then the video URL on its own line if one exists
- Bullet lists for capabilities and options, numbered lists for steps
- Callouts as blockquotes with a bold label: `> **Important:** ...`
- Screenshot placeholders: `> Screenshot placeholder: <what to capture> | Alt text: <the alt text>`; real images as markdown images with alt text
- Related articles linked in ordinary sentences with the article title as the link text, public help center URL preferred
- No horizontal rules, no HTML, no `In this article:` heading, no support footer

## Related skills

- **article-draft**: for new articles from release notes. Its `references/` folder holds the templates, the model articles, and the Notion publishing rules this skill reuses.
- **sync-help-center**: refresh the mirror before a migration if it is more than a week old.
- **humanizer**: for removing AI-generated writing patterns. Run after this skill if the output feels stilted, then re-run step 7, since the humanizer may reintroduce "you can."

## Reference

`references/notion-ai-prompt.md` is a paste-ready version of these rules for teammates editing directly in Notion AI.
