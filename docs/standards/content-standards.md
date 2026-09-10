# Help center content standards

The approved writing, structure, naming, and formatting standard for every Perchwell help center article. This file replaces the bundled fallback rules that used to live in `.claude/skills/article-draft/references/style-rules.md`. The golden questions (`golden-questions.md` in this folder) apply on top of it, and the Fin-readiness scorecard (`fin-readiness-scorecard.md`) measures how far an article is from meeting both.

Owner: Tara, project lead, [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com). Approvers: Kelly Miragliotta, Baldwin content audit owner, [kelly.miragliotta@perchwell.com](mailto:kelly.miragliotta@perchwell.com), and Rafe Petkovic, Fin answer-quality owner, [rafe.petkovic@perchwell.com](mailto:rafe.petkovic@perchwell.com). Written September 4, 2026. Migration and scorecard sections added September 9, 2026 after the first migration test. Audience, limitations, redundancy, and bold rules revised September 10, 2026 after the team reviewed that test.

Related Notion pages: [Help Center Article & Collection Naming Standards](https://app.notion.com/p/3ce8b9e0143881b790c6c7c29eb11009) (naming, approved) and [Template Article](https://app.notion.com/p/3d18b9e0143880189917f12bdc34c500) (this standard rendered as a fill-in template).

## Why these rules exist

Fin answers members from published help center articles, and it retrieves sections, not whole articles. A section that does not stand on its own does not get retrieved well, and a heading that does not name what it answers scores poorly. Most rules below trace to Intercom's own Fin guidance, cited at the bottom of this file. Where a rule exists only for the human reader, it says so.

Two rules from the old fallback were retired on September 4, 2026 because no live article used them and neither helps Fin:

- The `## In this article:` heading. The opening paragraph replaces it, in a stronger form. See Opening paragraph.
- The "Connect with our Support Team" footer. Intercom already renders Related Articles and a feedback prompt at the end of every article.

## Article types

| Type | When to use it | Title pattern |
|---|---|---|
| Workflow | One primary task the member completes in Perchwell | Task-led, for example "Create a Market Conditions Addendum Report (1004MC)" |
| Overview | Orients the member to a page or area rather than one task | "\<Page\> Overview", for example "Search Page Overview" |
| FAQ | Several short questions about one area, none large enough for its own article | "\<Area\> FAQ" |

One primary goal per article. When the content starts branching into a second workflow, link out instead of expanding.

## Titles

Follow the approved Notion naming standard. In short:

- Write clear, natural, task-focused titles that name the outcome. "Manage Your Saved Searches" beats "Saved Searches" and "Sharing Functionality."
- Title case, following the [Perchwell Product Style Guide](https://app.notion.com/p/2a48b9e014388092a38cd7d1f4b4cb60) for acronyms, hyphenated words, and prepositions.
- Prefer concise, action-led phrasing and drop "How to" when the meaning survives without it. Questions, "How to" phrasing, and -ing constructions are permitted when they read more naturally or match how members search. Do not apply a grammatical formula at the expense of clarity.
- Use MLS-specific terminology only when that MLS has a distinct term, rule, or workflow the member needs to recognize. Belonging to one help center is not on its own a reason to change a title.
- The article title and the Notion `Article Name` match exactly.

## Description

The description is the Intercom search-result snippet and one of the first things Fin sees.

- 120 to 140 characters. Intercom caps the field at 140.
- State what the member will accomplish and name the feature.
- Example: "Generate a 1004MC Market Conditions Addendum Report from your search results and export it to PDF for your appraisal workfile."

## Opening paragraph

The body opens with one paragraph that states what the member will accomplish, not what the article is about. This is the jobs-to-be-done form Intercom asks for, and it carries the article's key terms into the first chunk Fin reads.

- Formula: "Use this article to \<outcome 1\>, \<outcome 2\>, and \<outcome 3\>."
- Name the feature in the sentence, not just in the title.
- Say who the article is for only when a role or access level gates the workflow: "Use this article, as a broker or brokerage admin, to ..." When every member has the feature, say nothing. See Audience and permissions.
- Do not write "This article covers ..." or "In this article, you will learn how to ..." Both describe the topic instead of the outcome, and Intercom names the first as the weak form.

If a Loom or Arcade walkthrough exists, it goes directly under this paragraph. The article must stand on its own without it, and the written steps must match the video exactly.

## Structure and heading levels

Intercom renders the article title in its own tag, and recommends an H1 carrying the title for assistive technology, then H2 and H3 for the sections inside. Perchwell articles follow that exactly:

| Level | Use |
|---|---|
| H1 | The article title only. One per article |
| H2 | Major sections |
| H3 | Subsections, and the `Steps:` heading |

Section order for a workflow article, dropping what does not apply: when to use it, create or start, customize or configure, share or export, tips.

Similar features use the same section names so a member who has read one recognizes the next. Reports, for example: "Create a \<report\>", "Customize the \<report\>", "Share the \<report\>".

## Section headings

Headings are weighted heavily in Fin's retrieval scoring, so they carry more of the work than any other line in the article.

- Name what the section answers, in the member's words. "Set the report max date" beats "Settings." "Refunds for cancelled subscriptions" beats "Refunds."
- Include the feature name in the heading where it fits naturally. Sections are retrieved on their own, so a heading that reads "Overall trend" tells Fin nothing about which report it belongs to.
- FAQ articles use one heading per question, in question form. Question-form headings are allowed in any article type when they match how members ask.
- Do not use bare nouns ("Settings", "Options") or bare imperatives with no object ("Get started").
- Do not repeat the same heading twice in one article.

**Heading echo.** The first sentence under a heading repeats the heading's key terms. Fin sometimes fails to capture headings from the HTML, and the echo means the section still identifies itself. Under "Set the stable range", open with "The stable range controls ...", not "This controls ..."

**Self-contained sections.** Every section must make sense retrieved on its own. Do not open with "Then", do not write "as described above" or "the field shown above", and restate what a step depends on rather than pointing back at it.

**One topic per section.** Break a long section up with H3 subheadings rather than letting two topics share one block. Keep paragraphs short, two to four sentences, so a retrieved passage carries a whole thought.

## Say each fact once

Fin retrieves sections alone, so some repetition is required. That is not a license to state the same fact in three places. The two are different, and confusing them produces an article that is long, thin, and no easier to retrieve.

**Repeat these.** They are what makes a retrieved section identify itself:

- The feature name, in every section, instead of falling back to "it".
- The heading's key terms, in the first sentence beneath it.
- Whatever a step depends on, restated rather than pointed back at.

**Do not repeat these.** Every fact gets one canonical home:

- The same enumeration in two sections. If "When to use" lists the three things the feature finds and "What it returns" lists them again, one of the two sections is doing no work.
- A fact stated in a lead paragraph and again in a bullet underneath it.
- A limit or a redirect stated in one section and again in another.

When a later section needs a fact that lives elsewhere, name the section or link the article instead of restating it. Repeating the feature name costs a reader nothing; repeating its capabilities costs them the answer they came for.

## Steps

- Heading is exactly `Steps:` at H3, under the section it belongs to.
- Numbered list, one action per step, no terminal period.
- Name the UI element exactly, unbolded: `1. Click Actions`, `2. Select Print`.
- Optional steps start with *(Optional)*.
- Finish with one sentence on what happens after the last step: the confirmation, the toast, the file that appears, where the member lands. Do not stop at the final click.

## Lists and tables

- Multi-step processes are numbered lists. Sets of options or items are bullet lists. Never describe steps or enumerations in flowing prose. If a sentence ends in "the following:", a list follows it.
- Expand a single-sentence feature description into a lead sentence plus a bullet list, one concrete action or option per bullet.
- Use a table when the same result can be reached more than one way, or to compare options. One column for the option, one for the steps or for when to choose it.
- Every table gets an intro sentence above it saying what the table covers and where it applies. A retrieved table with no heading context is unusable.

## Callouts

Intercom's guidance is that a bold label is what marks a passage as something Fin should carry into an answer. The colored callout block is for the human reader. Emoji do nothing for retrieval, and the golden questions ban them as pointers, so the old emoji convention is retired.

- Format: a callout block whose first words are a bold label, then one or two sentences. This label and the `**Description:**` line are the only bold in an article.
- Labels: **Note:** for system behavior worth flagging, **Important:** for a limit, a deadline, or something that cannot be undone, **Tip:** for a recommendation.
- In the repo's markdown mirror these appear as blockquotes, for example `> **Important:** The report supports up to 500 listings.`
- Do not stack two callouts back to back, and do not use a callout for something a plain sentence in the flow would carry just as well. Both model articles state most limits as ordinary sentences directly under the steps that produce them.

Links to related articles are ordinary sentences or bullets, not callouts. Vary the phrasing: "Learn how column templates work in \<link\>", "\<Link\> covers tag sharing in detail", "For step-by-step guidance on inviting clients, see \<link\>". Never write "click here" or "view our article here".

## Audience and permissions

State a role only when a role gates the workflow, or when the feature behaves differently depending on who is looking at it. Silence means every member has it.

- When a workflow is admin-only or broker-only, say so before the steps, not after them, and do not assume the member knows their own role.
- When the feature is open to everyone, write nothing. A sentence whose only content is that everyone has the feature tells the member nothing and pushes the answer they came for further down the page.
- When you cannot tell from the sources whether a restriction exists, leave a `[confirm: ...]` marker on its own. Never assert universal availability and then mark it unconfirmed in the same breath; the claim and the marker contradict each other, and the claim is the part Fin will quote.

The Notion `Roles` property still records the audience for every article, whether or not the body says anything.

## Constraints, and where to go instead

Articles describe what Perchwell does. A member reading about a feature should come away knowing what it is for and where to go for the neighboring job, not carrying a list of what the feature fails to do.

- **No Limitations section by default.** Do not open a section to catalog shortcomings, and do not go looking for downsides to fill one.
- **State a constraint where the member meets it,** in the section they are already reading, and phrase it as the route forward: "To look up several listings at once, open the Search page and enter the IDs in the MLS ID filter, separated by commas." Not: "The Universal Search Bar cannot search more than one listing at a time."
- **Prefer the positive frame.** "Saved Searches keep a search and send alerts" beats "quick lookups are not saved and do not send alerts." Both carry the same fact; only one leaves the member knowing what to do.
- **A dedicated section is reserved** for a hard cap with an exact number that a member will hit mid-workflow, or for something irreversible. The 1004MC report's 500-listing cap is the model case. Even then, lead with the capability and follow with the number and the fix.
- **Never a bare deficit.** A constraint with no alternative path and no consequence for the member does not go in the article at all.

Where a limit is stated, it is stated precisely. All numbers, thresholds, limits, and durations are exact. No "some", "a few", "shortly", or unbounded ranges. If the real number is unknown, mark it `[confirm: <what is missing>]` and ask rather than guessing.

**Do not strengthen a hedged source.** Precision means matching the source, not sounding more certain than it. When the source says "statuses like Active, Pending, and Closed", the rewrite says "statuses such as", not "every status". When it says results appear, the rewrite does not say where they appear. Turning an example list into a complete one, or an unstated detail into a stated one, is the most common way a false fact enters a migrated article, because the stronger sentence reads better and nothing in the draft flags it as new. If the confident version is what the team wants to publish, confirm it first and then write it.

**A `[confirm: ...]` marker covers only what it names.** Attaching a marker to a detail does not license the sentence around it. "The Universal Search Bar works the same way on mobile as in the browser. `[confirm: where it sits in the mobile app]`" asserts the behavior and questions only the location, so the half most likely to be wrong is the unmarked half. It was wrong: on mobile the bar appears on the Search tab alone. When the claim itself is unverified, mark the claim or leave the sentence out.

## Closing sections

- A closing recap is optional. Include one only when there are system behaviors or recommendations that did not fit naturally into a section, and never to repeat something already stated.
- Heading is `Things to Know` when the items are system behaviors, or `Tips` when every item is a recommendation.
- No support-contact footer. Intercom renders Related Articles and "Did this answer your question?" automatically.

## Voice and terminology

- Second person, imperative, matter of fact. You are an experienced support professional guiding a busy real estate professional.
- Remove "you can", "allows you to", "you are able to". Write "Click Manage widgets to customize your layout".
- Avoid the verb "use" as a stand-in for the real action. Open, click, select, run, apply, enter, drag, check. "When to use" headings are the accepted exception, along with the "Use this article to ..." opening.
- Active voice, short sentences, one idea per sentence.
- No marketing adjectives or framing: streamlined, powerful, elegant, seamless, professional leave-behind, uncover insights, smarter decision-making, ideal for, perfect for, game-changing. Describe the function instead.
- Name the actual UI element the member sees. "Filter by Recently Created or New" beats "filter your contacts". Name it exactly; do not bold it.
- Do not inventory what is already on the screen. A member looking at a listing card can see the price and the bed count, and listing those fields back adds length without adding an answer. Say what a display covers or what it does, not which fields it renders: "Listings in every status appear, including Active, Pending, Closed, and Expired" earns its place; "each card shows the address, city, price, bedrooms, and bathrooms" does not. Screenshot alt text is the exception, because it exists for people who cannot see the image.
- State system behavior explicitly: what happens automatically, what is included by default, what is required, what cannot be undone.
- Translate system terms into member behavior with a "which means" clause. "The report max date acts as the anchor date for every reporting period, which means each time window counts backward from this date."
- A pop-up window that opens over the page is a modal, named that way throughout the article rather than drifting to "window" or "panel".
- Define abbreviations and product-specific terms on first use, including MLS-specific ones. Repeat the feature name through the article rather than switching to "it" after the first mention, because sections are retrieved alone. Repeat the name, not the facts attached to it. See Say each fact once.
- Hedge predictions about people. "Members may ask" beats "members will ask".
- No internal language: no employee names, no internal product terms the member cannot see, no casual asides.
- Legacy platforms are never named in an article. One article serves more than one MLS, and members came from different systems, so write "a legacy platform" and keep the legacy feature name the member would recognize. Full transition voice in `docs/product-context.md`. Never "old system", "retired", or "sunsetted".

## Formatting

- No bold in the body. Not on clickable elements, button labels, filter names, menu items, navigation targets, toggles, status labels, concepts, or feature names. Write "Click Actions, then select Print", not "Click **Actions**, then select **Print**". Naming the exact on-screen label is still required; the label carries itself without the weight, and a page peppered with bold reads as emphasis on nothing.
- Two exceptions, both labels that introduce a block rather than emphasis inside a sentence: the callout labels **Note:**, **Important:**, and **Tip:**, which Intercom names as the signal Fin reads, and the `**Description:**` line at the top of the article.
- Never use em dashes. Use commas, periods, colons, or semicolons.
- No horizontal rules. Headings carry the separation.
- Plain markdown only. No toggles, no columns, no HTML.
- American English spelling and punctuation.

## Media

- Videos: Loom preferred, Arcade acceptable. The primary video sits under the opening paragraph; a section-level video sits under its section heading.
- Screenshots follow the Figma-approved specs from CS and sit after the step they illustrate.
- Every image needs descriptive alt text. An image with no alt text is invisible to Fin and to anyone using a screen reader, and it fails the golden questions. Describe what the screenshot shows in the surrounding text as well; never introduce an image with a bare trailing colon.
- Placeholders while the media does not exist yet, one per line:
  - `> Video placeholder: <what the video should show, from where to where>`
  - `> Screenshot placeholder: <the exact screen or modal to capture> | Alt text: <the alt text the image will carry>`
- The screenshot or video owner removes the placeholder when the asset lands, before the article goes to Intercom.

## Internal linking

- Link to a related article whenever a workflow is referenced instead of re-explaining it.
- Descriptive link text, always the article title or the task. Never "here".
- Prefer the public help center URL for the article's own MLS (`support.perchwell.com/baldwin/en/...`). A link into the default help center (`support.perchwell.com/en/...`) is flagged at transfer so CS can confirm it resolves for that MLS's members. If only the Notion page is known, link that and flag it for replacement at Intercom transfer.
- Do not recreate a workflow that already has an article.

## Migrating an existing article

Articles that predate this standard live in the old Notion Master Article List and in the live help center. When one is brought into the Perchwell Help Center Database [Sep 2026], it is rewritten to this standard, not copied.

- **Source precedence.** The live Intercom article (mirrored under `docs/help-center/`) wins on facts, because it is what members and Fin see today. The old Notion page supplies the video link, the properties, and the click script as a hint for the article's outcomes. Every difference between the two is listed for the reviewer, never merged silently.
- **Drop:** the `In this article:` heading, horizontal rules, emoji-led lines and emoji pointers, the "Click Script" toggle (a video script, not article content), the trailing Perchwell banner image, the support footer, and internal prefixes such as `NYC|`.
- **Carry:** the Loom or Arcade URL, directly under the opening paragraph; every image, with alt text written for it; the legacy-platform comparison, with the platform genericized and the legacy feature name kept.
- **Retitle** when the old title is a bare noun, following the naming standard, and record the old title so the Intercom redirect and the audit can find it. The team may keep a familiar bare-noun title; when it does, the description and the opening paragraph carry the task words instead.
- **Feature name versus on-screen label.** When the feature's name is not what the member sees on screen (the Universal Search Bar is the Search field in the top navigation), the first step names the on-screen label exactly and the lead sentence ties the two together.
- **Alt text comes from the actual screenshot.** Open the image and describe what it shows; do not write alt text from the surrounding prose. A migrated article keeps its live Intercom CDN images when their URLs are stable.
- **`[confirm: ...]` markers stay in the Notion draft** so reviewers can see exactly what the writer could not verify from the sources. They are resolved or removed before transfer.
- **Shared articles.** An article mirrored in both `baldwin/` and `crmls/` is in both help centers through a shared collection. The new database holds one MLS per row, so the draft goes in under the MLS the old row names and the shared status is an open item for the team.
- The old Master Article List row is read and left alone. Never update its status or mirror a change back into it.

## Fin-readiness scorecard

Every draft and every migrated article is scored with `fin-readiness-scorecard.md` in this folder: the 14 golden questions as a pass-or-fail gate, then 0 to 100 across five weighted dimensions (retrieval signals, chunk independence, answer completeness, Fin-parsable formatting, accuracy and confidence). A migration is scored before and after so the delta shows what the rewrite bought. The result goes in `workstreams/help-center-overhaul/qa/`, one file per article, with five to eight Fin test questions the team can run after transfer. An article moves to `Ready to Transfer` in the Fin-ready band (90 or above) with the gate passed, or in the Ready with fixes band with the listed fixes applied.

## Quality checklist

Confirm before saving a draft:

- Title is task-focused, title case, and matches the Notion `Article Name`
- Description is 120 to 140 characters and names the feature
- Body opens with "Use this article to ..." and states the outcomes, not the topic
- A role is stated only where one gates the workflow; no unverified claim that everyone has the feature
- One primary goal; branching workflows link out
- Title is the only H1; sections are H2; subsections and `Steps:` are H3
- Every heading names what the section answers and carries the feature name where it fits
- The first sentence under each heading echoes the heading's key terms
- No section depends on "above", "then", or a previous section to make sense
- No fact or enumeration appears in more than one section; the feature name repeats, its capabilities do not
- No inventory of fields the member can already see on screen, outside of image alt text
- Paragraphs run two to four sentences; long sections are broken up with subheadings
- Steps are numbered, one action each, no terminal periods, UI elements named exactly, and the block ends with what happens next
- Tables carry an intro sentence
- Callouts lead with a bold **Note:**, **Important:**, or **Tip:** label; no emoji; none stacked
- No bold in the body; only the callout labels and the `**Description:**` line carry it
- No "you can", "allows you to", or the verb "use" outside the accepted exceptions
- No marketing adjectives from the do-not list
- Defaults and irreversible actions are stated with exact numbers; constraints are framed as the route forward, with no Limitations section unless a hard cap or an irreversible action earns one
- System terms carry a "which means" clause
- Abbreviations and product terms are defined on first use
- Images have alt text; placeholders carry the alt text they will use
- No em dashes, no horizontal rules, no HTML, no support footer, no "In this article:" heading
- Every fact traces to release notes or a live article; anything invented is marked `[confirm: ...]`
- All 14 golden questions pass
- Scorecard run; band is Fin-ready, or the failed checks are listed with their fixes
- Links point at this MLS's help center, and any default help center link is flagged for transfer

## Sources

- Intercom, [Optimizing content for Fin](https://www.intercom.com/help/en/articles/7860255-optimizing-content-for-fin): opening paragraph must state what the reader will accomplish; headers divide content into focused single-topic sections; include header text in the paragraph below it; lists over dense paragraphs.
- Intercom, [Optimize your Help Center for Fin AI Agent](https://www.intercom.com/help/en/articles/7269326-optimize-your-help-center-for-fin-ai-agent): 140-character description limit; bold "Note" or "Important" labels flag what Fin should include; numbered lists for steps.
- Intercom, [Format an article](https://www.intercom.com/help/en/articles/56978-format-an-article): H1 carries the title for assistive technology, H2 and H3 divide the sections.
- Fin, [Optimizing content for Fin](https://fin.ai/help/en/articles/13975766-optimizing-content-for-fin): headers make content scannable for Fin and humans; one header per question in FAQ articles.
- `golden-questions.md` in this folder: Intercom's 14 content readiness factors, which every in-scope article must pass.
