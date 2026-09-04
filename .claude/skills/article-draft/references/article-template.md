# Article Templates

Copy the skeleton that matches the article type. Replace every `<...>`. Remove sections that do not apply. Heading levels match the live Notion Master Article List pages: `## In this article:` for the intro, `#` for major sections, `###` for subsections and `### Steps:`.

## Workflow article (default)

```markdown
# <Title in Title Case, No Gerund>

<!-- Status: Draft | MLS: Baldwin | Collection: <Collection in Intercom> | Roles: <Roles> | Notion: <notion url once created> -->

**Description:** <120 to 160 characters: what the reader will accomplish, with the primary keyword.>

## In this article:

You will learn how to <primary task> from the **<page>** page, <secondary task>, and <secondary task>.

> 📹 Video placeholder: <what the walkthrough should show>

# <When to use this feature, or a one-sentence description heading>

<One or two sentences: what the feature does and the situation it fits. Bullets if there are multiple concrete situations.>

- <Situation or outcome 1>
- <Situation or outcome 2>

# <Create or start the key workflow>

<One lead sentence about where the workflow begins and anything to set up first.>

### Steps:

1. Go to **Search**
2. <Action> **<UI element>**
3. <Action> **<UI element>**
4. *(Optional)* <Action>

<One sentence about what happens after the last step.>

> 🖼️ Screenshot placeholder: <exact screen or modal>

> 💡 **Tip**: <one recommendation>

# <Customize or configure>

<Lead sentence.>

### <Option group 1>

- **<Option>** (default) <what it does>
- **<Option>** <what it does>

### <Option group 2>

<Explain the behavior, including defaults and limits, with a "which means" clause for any system term.>

# <Share, export, or print>

<Lead sentence, then steps or bullets.>

> 📖 <Varied link phrasing> [<Related Article Title>](<url>).

# Things to Know

- <System behavior the reader cannot discover on their own>
- <Limit, default, or irreversible action not already called out>

> **Connect with our Support Team:**
> ✉️ **Email:** [support@perchwell.com](mailto:support@perchwell.com)
> 💬 **Chat:** Click the chat icon at the bottom of the page to reach our support team.
```

## Multi-path workflow table

Insert inside any section when the same result can be reached more than one way.

```markdown
| Option | Steps or when to choose it |
|---|---|
| **From the Search page** | 1. Select listings, 2. Click **Actions**, 3. Select **Add to Tag** |
| **From the listing detail page** | 1. Open the listing, 2. Click the **tag** icon, 3. Select the Tag |
```

## Overview article

For "<Page> Overview" articles that orient the reader rather than walk one workflow.

```markdown
# <Page> Overview

<!-- Status: Draft | MLS: Baldwin | Collection: <Collection> | Roles: <Roles> | Notion: <url> -->

**Description:** <120 to 160 characters>

## In this article:

You will learn how the **<Page>** page is organized and what each area is for.

# What the <Page> page is for

<Two or three sentences. What the reader does here and how it connects to the rest of Perchwell.>

# <Area or widget group 1>

<Lead sentence, then bullets of concrete actions.>

- <Action> **<UI element>** to <result>
- <Action> **<UI element>** to <result>

> 📖 <Varied link phrasing> [<Article for the deeper workflow>](<url>).

# <Area or widget group 2>

...

# Things to Know

- ...

> **Connect with our Support Team:**
> ✉️ **Email:** [support@perchwell.com](mailto:support@perchwell.com)
> 💬 **Chat:** Click the chat icon at the bottom of the page to reach our support team.
```

## FAQ article

For "<Area> FAQ" articles. Each question is an H1 in the reader's words (questions are allowed here, in headings only, never in the article title); the answer is a short imperative paragraph or steps.

```markdown
# <Area> FAQ

<!-- Status: Draft | MLS: Baldwin | Collection: <Collection> | Roles: <Roles> | Notion: <url> -->

**Description:** <120 to 160 characters>

## In this article:

You will find answers to the most common questions about <area> in Perchwell.

# Can I <question 1>?

<Answer in one to three sentences. Link to the workflow article if steps exist.>

# Why <question 2>?

<Answer.>

> **Connect with our Support Team:**
> ✉️ **Email:** [support@perchwell.com](mailto:support@perchwell.com)
> 💬 **Chat:** Click the chat icon at the bottom of the page to reach our support team.
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

Release: <one line on what changed for the reader>. Hold Intercom transfer until <flag or date condition>.

## <Existing Article Title> ([Notion](url) · [Live](url))

- **<Section heading>**: "<quoted current text>" → "<proposed text>"
- **<Section heading>**, step <n>: "<quoted>" → "<proposed>"
- **<Section heading>** (new): paste-ready section follows
- **Media**: <what to re-record or capture, or "none">

### <New or rewritten section heading>

<Final-form section, only when a full section is added or rewritten.>

## <Second Article Title> ([Notion](url) · [Live](url))

- ...

## Open items

- [confirm: <what is missing>] (<article>)
```
