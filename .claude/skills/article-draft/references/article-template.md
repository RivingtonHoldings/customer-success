# Article Templates

Copy the skeleton that matches the article type. Replace every `<...>`. Remove sections that do not apply. Every rule these skeletons encode is explained in `docs/standards/content-standards.md`; read that first when something here looks arbitrary.

Heading levels are fixed: H1 is the article title and nothing else, H2 is a major section, H3 is a subsection and the `Steps:` heading. Intercom renders the title in its own tag and expects H2 and H3 inside the body, and Fin weights headings heavily when it retrieves.

## Workflow article (default)

```markdown
# <Title, Task-Focused, Title Case>

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: <Collection> | Roles: <Roles> | Videos: <Yes or No> | Visuals: <Yes or No> | Notion: <page url once created> -->

**Description:** <120 to 140 characters: what the member will accomplish, naming the feature.>

Use this article to <outcome 1>, <outcome 2>, and <outcome 3> in Perchwell.<Only if a role gates the workflow, say so here: "You need <role> access to ..." Otherwise write nothing; silence means every member.><If a walkthrough exists, the Loom or Arcade link goes on the next line.>

> Video placeholder: <what the walkthrough should show, from where to where>

## When to use <the feature>

<One or two sentences naming the feature and the situation it fits. The first sentence repeats the heading's key terms.>

- <Situation or outcome 1>
- <Situation or outcome 2>

## <Create or start the key workflow, named>

<Lead sentence that repeats the section heading's key terms and says where the workflow begins and what to set up first.>

### Steps:

1. Go to **Search**
2. <Action> **<UI element>**
3. <Action> **<UI element>**
4. *(Optional)* <Action>

<One sentence on what happens after the last step: the confirmation, the file, where the member lands.>

> Screenshot placeholder: <the exact screen or modal to capture> | Alt text: <the alt text the image will carry>

## <Customize or configure, named>

<Lead sentence echoing the heading.>

### <Option group, named>

- **<Option>** (default) <what it does>
- **<Option>** <what it does>

### <Option group, named>

<Explain the behavior, including defaults and limits, with a "which means" clause for any system term.>

## <Share, export, or print, named>

<Lead sentence, then steps or bullets.>

<Plain sentence or bullet linking the related article, phrasing varied: "Learn how column templates work in [<Related Article Title>](<url>).">

## <Only when a hard cap or an irreversible action earns it: name the capability, not the deficit>

<Most articles have no section here. Delete it unless the feature has a hard cap with an exact number that a member hits mid-workflow, or something irreversible. A softer constraint goes in the section where the member meets it, written as the route forward: "To look up several listings at once, open the **Search** page and enter the IDs in the **MLS ID** filter, separated by commas." Never open a section to catalogue what the feature will not do.>

- <The exact number, then what to do instead, in the same bullet>

## Things to Know

<Optional. Only system behaviors the member cannot discover alone and that no earlier section already stated. Use `## Tips` instead when every item is a recommendation. Delete the section when there is nothing left to say.>

- <System behavior, default, or irreversible action not already called out>
```

Notes on the skeleton:

- No `In this article:` heading and no support footer. The opening paragraph does that work in the form Intercom asks for, and Intercom renders Related Articles and the feedback prompt itself.
- The audience sentence is required when a role gates the workflow and omitted when it does not. Silence means every member; a line saying everyone has the feature tells the member nothing and pushes their answer down the page. See "How the house standard resolves factor 7" in `docs/standards/golden-questions.md`.
- Each fact belongs in one section. The feature name repeats throughout so a retrieved section identifies itself; its capabilities do not. If "When to use" and a later section enumerate the same things, cut one.
- Screenshot placeholders carry the alt text the image will use, so the media owner does not have to invent it later.

## Multi-path workflow table

Insert inside any section when the same result can be reached more than one way. The intro sentence is required: a retrieved table with no heading context cannot be read.

```markdown
Tags can be added from the Search page or from a listing's detail page. Both add the listing to the same Tag.

| Option | Steps or when to choose it |
|---|---|
| **From the Search page** | 1. Select listings, 2. Click **Actions**, 3. Select **Add to Tag** |
| **From the listing detail page** | 1. Open the listing, 2. Click the **tag** icon, 3. Select the Tag |
```

## Overview article

For "\<Page\> Overview" articles that orient the member rather than walk one workflow.

```markdown
# <Page> Overview

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: <Collection> | Roles: <Roles> | Videos: <Yes or No> | Visuals: <Yes or No> | Notion: <url> -->

**Description:** <120 to 140 characters>

Use this article to find your way around the **<Page>** page in Perchwell, understand what each area does, and reach the workflows that start there.

## What you do on the <Page> page

<Two or three sentences. What the member does here and how it connects to the rest of Perchwell. Repeat the page name.>

## <Area or widget group, named>

<Lead sentence echoing the heading, then bullets of concrete actions.>

- <Action> **<UI element>** to <result>
- <Action> **<UI element>** to <result>

<Sentence linking the article that covers the deeper workflow.>

## <Area or widget group, named>

<Same shape.>

## Things to Know

<Optional, same rule as the workflow article.>
```

## FAQ article

For "\<Area\> FAQ" articles. Every heading is one question in the member's words. Intercom recommends a header per question, and question-form headings are how a member's phrasing gets matched.

```markdown
# <Area> FAQ

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: FAQs | Roles: <Roles> | Videos: <Yes or No> | Visuals: <Yes or No> | Notion: <url> -->

**Description:** <120 to 140 characters>

Use this article to answer the questions members ask most about <area> in Perchwell.

## Can I <question, in the member's words>?

<Answer in one to three sentences, opening by restating the question's key terms. Steps become a numbered list under a `### Steps:` heading. Link the workflow article when one exists.>

## Why does <question, in the member's words>?

<Same shape. Each answer stands alone: no "as described above", no reliance on the question before it.>
```

## Update change sheet

Used when the triage decision is "update." One file per release, covering every affected article. The sheet is a diff, not a document: a reviewer should see each edit once, in the form "this line becomes that line," and nothing else.

Rules that keep it short:

- State each fact once. Do not restate the release in a per-article preamble; the one-line header covers it.
- No rewritten bodies. Untouched sections are never reproduced. When a whole section is rewritten or added, include only that section, in final form, ready to paste.
- No Reason column. Add a reason in parentheses only when the reader could not guess it.
- Quote current text exactly (it is how CS finds the line in Intercom). Keep proposed text in final form so it can be pasted.
- One open-items list for the whole release, each item tagged with the article it affects.
- Do not include the triage table or the CS SOP steps; the triage table lives in the chat, and the SOP is CS's.

```markdown
# Help center changes: <feature external name> (YYYY-MM-DD)

<!-- Status: Update proposal | Trigger: <release note url> | Enable: <flag or date note> | Articles: <count> -->

Release: <one line on what changed for the member>. Hold Intercom transfer until <flag or date condition>.

## <Existing Article Title> ([Notion](url) · [Live](url))

- **<Section heading>**: "<quoted current text>" -> "<proposed text>"
- **<Section heading>**, step <n>: "<quoted>" -> "<proposed>"
- **<Section heading>** (new): paste-ready section follows
- **Media**: <what to re-record or capture, with alt text, or "none">

### <New or rewritten section heading>

<Final-form section, only when a full section is added or rewritten.>

## <Second Article Title> ([Notion](url) · [Live](url))

- ...

## Open items

- [confirm: <what is missing>] (<article>)
```

When an article being updated predates this standard, bring the sections you touch up to it and note the rest in Open items. Do not silently rewrite the whole article inside an update sheet.
