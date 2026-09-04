# Help Center Style Rules

These are the bundled fallback rules. When `docs/standards/content-standards.md` is filled in, it takes priority over anything here; read it first and apply it where the two differ.

The merged rulebook for Perchwell help center articles. Sources, in priority order when they conflict: the live Baldwin help center (support.perchwell.com/baldwin), the Notion "One Pager Author Style Guide" and "SEO Guidelines for Help Center Articles" (Master Resource Center), the CS "Help Center Article Formatting Rules," and the transformation patterns in `.claude/skills/article-rewrite/`. Apply every rule silently; the article never mentions these rules.

## Core principle

Help center content is instructional documentation, not product marketing. Every article should answer four questions: What does this do? How do I do it? What happens next? What should I know before I click?

If it sounds like marketing, simplify it. If it sounds vague, clarify it. If it sounds long, tighten it.

## Titles

- Title Case. Example: "Create a Market Conditions Addendum Report (1004MC)".
- No gerunds. "Create a Tag," not "Creating a Tag." "Print Search Results," not "Printing Search Results."
- No questions. "Reset Your Perchwell Password," not "How Do I Reset My Password?"
- Task-based and front-loaded: lead with the action or the object the reader is looking for. "Share Listings with Clients" beats "Sharing Functionality."
- "How to ..." is allowed when the article covers one specific feature. "How to Create a Tag" is fine; "How to Use Perchwell" is not.
- Overview articles: "<Page> Overview" (for example "Tags Page Overview"). FAQ articles: "<Area> FAQ."
- Keep the article title and the Notion `Resource Title` identical.

## Description

- Every article carries a description of 120 to 160 characters. It is shown in Intercom search results and stored on the Notion page.
- Summarize what the reader will accomplish and include the primary keyword naturally.
- Example: "Create and manage saved searches to track listings and receive real-time updates in Perchwell."

## Opening

- The body starts with the heading `## In this article:` followed by one or two sentences in second person that begin "You will learn how ...". Bold the UI surfaces mentioned.
- Example: "You will learn how to print your search results from the **Search** page, choose a page layout, and save your results as a PDF."
- If a Loom or Arcade exists, it goes directly under the intro. If one is needed but does not exist yet, add a placeholder (see Media).

## Structure

- One primary goal per article. If the content starts branching into another workflow, link out instead of expanding.
- Feature articles follow this order, dropping sections that do not apply: description and when to use it, create or start, customize or configure, share or export, Things to Know.
- Similar features use the same section names so readers recognize the pattern. Reports, for example: "Create a <report>", "Customize the <report>", "Share the <report>".
- Section headings are sentence case and descriptive enough that a scanning reader can find what they need. "Access third-party integration tools" beats "Access integrated tools." "Set the report max date" beats "Settings."
- Group related content under one parent heading rather than giving five small features five sections. Remove sections that state the obvious (a section on "how to navigate to X" when it is one click).
- Key workflows begin on the **Search** page, or the MLS default page if it differs.
- When there are two or more ways to complete the same workflow, present them in a table: one column for the option or workflow type, one for the steps or when to choose it.
- Expand single-sentence feature descriptions into a short lead sentence plus a bullet list of specific actions or options. One concrete action or option per bullet.

## Steps

- Heading is exactly `### Steps:` under the section it belongs to.
- Numbered list, one action per step, no terminal period.
- Name the UI element in bold: `1. Click **Actions**`, `2. Select **Print**`.
- Optional steps start with *(Optional)*.
- Follow the list with one sentence describing what happens next, if it is not obvious.

## Things to Know

- Default closing heading is `## Things to Know`. Use `## Tips` only when every bullet is a recommendation rather than a system behavior.
- Only include items that are important to the workflow and relevant to the reader. If an item was already covered in a callout or section, do not repeat it here.
- Prefer system behaviors readers cannot discover on their own: defaults, limits, what is saved automatically, what requires confirmation, what cannot be undone, where data comes from.
- If an item is worth noting but fails the two tests above, move it to the area FAQ article instead.

## Voice

- Second person, always. You are an experienced support professional guiding a busy real estate professional.
- Imperative. Remove "you can," "allows you to," "you are able to." Write "Click **Manage widgets** to customize your layout," not "You can use the Manage widgets button."
- Avoid the verb "use." Replace with the concrete action: open, click, select, run, apply, enter, drag, check. "Open **Search** and run a search" beats "Use Search to find listings." (The phrase "In this article" template and "When to use" headings are the accepted exceptions.)
- Active voice, short sentences, one idea per sentence. Break multi-clause instructions into steps.
- Matter-of-fact. Do not use marketing adjectives or framing: streamlined, powerful, elegant, seamless, professional leave-behind, uncover insights, smarter decision-making, ideal for, perfect for, game-changing. Describe the function instead. "Generates a formatted property summary for sharing or printing" replaces "A clean, professional report perfect for client presentations."
- Name the actual UI element the reader will see. "Filter by **Recently Created** or **New**" beats "filter your contacts."
- Clarify system behavior explicitly: what happens automatically, what is included by default, what is required, what cannot be undone. "Deleting a tag removes the folder and clears the tag from all associated listings. Listings are not deleted from Perchwell."
- Translate system terms into reader behavior with a "which means" clause. "The report max date acts as the anchor date for every reporting period, which means each time window counts backward from this date."
- Hedge predictions about people. "Clients may ask" beats "clients will ask."
- No internal language: no employee names, no internal product terms the reader cannot see, no casual asides ("And just like that, you're in!").
- Use cases, when included, stay practical and neutral. Format: `## Use case: <situation>`, one short scenario, then "How <feature> helps:" and numbered steps ending in the result.
- Paragon and other legacy systems: follow the Baldwin transition voice in the Paragon transition rules in `docs/product-context.md`. Never "old system," "retired," or "sunsetted."

## Formatting

- Bold every clickable element, button label, filter name, menu item, navigation target, toggle, and status label: **Search**, **Actions**, **Print**, **Price Drop**, **pencil** icon, **Coming Soon**.
- Do not bold general concepts, section titles, or feature names used as ordinary nouns ("hot sheets update automatically").
- Never use em dashes. Use commas, periods, colons, or semicolons.
- No horizontal rules in the markdown output. Section headings carry the separation.
- Plain markdown only. No toggles, no columns, no HTML.
- American English spelling and punctuation.
- Use tables only for multi-path workflows or option comparisons. Cells contain plain rich text, no lists.

## Callouts

Callouts are blockquotes that begin with an emoji. Keep them to one or two sentences. Do not stack two callouts back to back.

| Emoji | Purpose | Example |
|---|---|---|
| 💡 | Tip or recommendation | `> 💡 **Tip**: Use fewer columns to keep the printout easy to read.` |
| ⚠️ | Notice about a limit, a deadline, or something irreversible | `> ⚠️ **Note**: Once a client is added to a Tag, they cannot be removed. Delete the Tag to revoke access.` |
| 📖 | Link to a related article | `> 📖 Learn how column templates work in [Customize Your Search View](url).` |
| 📹 | Link to a video that supports the section | `> 📹 Watch a short walkthrough of saving a search: [Loom](url).` |
| ⚒️ | Legacy platform vs Perchwell comparison | `> ⚒️ **Paragon vs. Perchwell**: In Paragon, reports lived in several tabs. In Perchwell, every report starts from **Search**.` |

Link phrasing varies. Rotate among: "Learn how <feature> works in <link>." "Check out <link> to learn more about <topic>." "Visit <link> for step-by-step guidance on <task>." "<Link> covers <topic> in detail." Never repeat the same opener twice in one article, and never write "click here."

## Media

- Videos: Loom preferred. Arcade demos are acceptable. Place the primary video directly under the intro; section-level videos go under the section heading.
- The article must stand on its own without the video. Written steps match the video exactly.
- Screenshots follow the Figma-approved specs from CS. Place them after the step they illustrate.
- Placeholders when media does not exist yet, one per line, each on its own blockquote:
  - `> 📹 Video placeholder: <what the video should show, from where to where>`
  - `> 🖼️ Screenshot placeholder: <the exact screen or modal to capture>`
- Placeholders are removed by the screenshot or video owner before the article goes to Intercom.

## Internal linking

- Link to a related article whenever a workflow is referenced instead of re-explaining it.
- Use descriptive link text (the article title or the task), never "here."
- Prefer the public help center URL. If only the Notion page is known, link the Notion page and flag it for replacement during Intercom transfer.
- Do not recreate a workflow that already has an article. Link and, if useful, add a "Related workflows" section.

## Support footer

Every article ends with this block, verbatim:

```
> **Connect with our Support Team:**
> ✉️ **Email:** [support@perchwell.com](mailto:support@perchwell.com)
> 💬 **Chat:** Click the chat icon at the bottom of the page to reach our support team.
```

## Quality checklist

Confirm before saving:

- Title is Title Case, no gerund, not a question, front-loaded with the task
- Description is 120 to 160 characters and includes the primary keyword
- Body opens with `## In this article:` and "You will learn how ..."
- One primary goal; branching workflows link out
- Section headings are sentence case and specific
- Every step block uses `### Steps:`, numbered, one action per step, no terminal periods
- Every clickable element, filter, button, and nav item is bold; concepts are not
- No "you can," "allows you to," or the verb "use" outside the accepted exceptions
- No marketing adjectives from the do-not list
- Defaults, limits, and irreversible actions are stated
- System terms carry a "which means" clause
- No em dashes, no horizontal rules, no HTML
- Callouts use the emoji chart; link phrasing does not repeat
- Media placeholders are present where a screenshot or video is expected
- Things to Know contains only items not already covered
- Support footer is present
- Every fact traces to the release notes or a live article; anything invented is marked `[confirm: ...]`
