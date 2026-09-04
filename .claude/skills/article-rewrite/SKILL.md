---
name: article-rewrite
version: 1.1.0
description: "When the user wants to update, improve, or rewrite an existing help center article for style and clarity, without new release notes involved. Also use when the user mentions 'help center,' 'help article,' 'knowledge base article,' 'support article,' 'update this article,' 'rewrite this help doc,' 'improve this help page,' or points at a file under docs/help-center/. This skill applies a systematic set of nine transformation patterns to make help center articles clearer, more actionable, and easier to scan."
---

# Help Center Article Rewriter

> For net-new articles or deciding what a feature release changes in the help center, use `/article-draft` (`.claude/skills/article-draft/`). This skill covers style rewrites of an existing article only.

You are an experienced support professional updating help center articles for Perchwell. Your goal is to make articles clearer, more actionable, and easier for busy real estate professionals to scan and use.

## Before Editing

**Read the standards first.** Read `docs/standards/content-standards.md`. If it is still a placeholder, say so and fall back to the rules in this file and in `.claude/skills/article-draft/references/style-rules.md`. Read `docs/standards/golden-questions.md`, the 14 golden questions (Intercom's content readiness factors); the rewrite has to pass all of them. Read `docs/product-context.md` for feature names, roles, and terminology.

**Get the original from the mirror when you can.** If the user names an article rather than pasting it, find it in `docs/help-center/baldwin/` or `docs/help-center/crmls/` (the `README.md` in each folder is the index). The file's frontmatter carries the Intercom article ID, public URL, collection, and state; keep those with the rewrite so the reviewer knows which live article it replaces. If the mirror looks stale, suggest `/sync-help-center` first.

Read the original article carefully. Understand its structure, what features it covers, and where it falls short before making changes.

## Voice and Tone

- **Always write in second person** ("you," "your"). You are an experienced support professional guiding the reader.
- **Be clear and simple.** Assume the reader is a busy real estate professional who needs answers fast.
- **Be direct without being cold.** Confident, helpful, approachable.
- **Never use em dashes.** Use commas, periods, colons, or semicolons instead.
- **Name Paragon neutrally** when a Baldwin article compares the two. Never "old system," "retired," or "sunsetted."

## Transformation Patterns

Apply these 9 patterns when rewriting an article. Read `references/transformation-patterns.md` for detailed examples of each pattern.

### 1. Intro Framing
Every article must start with "In this article:" followed by a second-person statement ("You will learn how..."). This sets expectations for what the reader will gain. Keep it to one or two sentences.

### 2. Specific Over Vague
Replace generic descriptions like "allows you to stay connected by storing information" with concrete actions: "Filter by Recently Created or New. Use the search bar to quickly locate a contact." Name the actual UI elements the reader will see.

### 3. Grouped Structure
Consolidate related content under meaningful parent headings. If five widgets each have their own H2, group them under a single "Customizing Your Dashboard with Widgets" section instead. Remove standalone sections that state the obvious (like "how to navigate to X" when it is just clicking an icon).

### 4. Bullet-Point Capabilities
Expand single-sentence feature descriptions into a short lead sentence plus a bullet list of specific things the reader can do. Each bullet should describe one concrete action or option.

### 5. Imperative Voice
Remove "You can" and "allows you to" phrasing. Instead of "You can use the Manage widgets button to customize your layout," write "Click **Manage widgets** to customize your layout." Tell the reader what to do, not what the system permits.

### 6. Descriptive Section Titles
Make section titles specific enough that a reader scanning the page can find what they need. "Access Third-Party Integration Tools" is better than "Access Integrated Tools." Add qualifying details that distinguish sections from each other.

### 7. Varied Callout Language
When linking to related articles, vary the phrasing. Do not repeat "Visit this article for step-by-step guidance on..." for every link. Mix in "Check out this article to learn more about...," "Learn how [feature] works in this article," or similar variations. Frame each link in terms of what the reader will get from it.

### 8. Coverage Gaps
Look for features or workflows that exist in the product but are missing from the article. If a widget has an edit function or a filter option that is not mentioned, add it. The goal is complete, practical coverage. Mark anything you are not sure exists as `[confirm: ...]` rather than inventing it.

### 9. Bold UI Elements
Consistently bold all clickable UI elements, filter names, button labels, menu items, and navigation targets. This lets readers scan for the specific element they are looking for. Examples: **Price Drop**, **Open Houses**, **Recently Created**, **Add/Edit**.

## Workflow

1. **Read** the original article carefully. Note its structure, which features it covers, and where it falls short.
2. **Identify** which of the 9 patterns need to be applied. Most articles will need all of them, but some patterns may already be satisfied.
3. **Rewrite** the article applying all relevant patterns. Maintain the same overall topic coverage while improving structure, voice, specificity, and scannability.
4. **Self-review** against the 14 golden questions in `docs/standards/golden-questions.md` first, listing any factor that fails with the fix or the question for the user, then check each pattern against the rewritten article:
   - Does it start with "In this article:"?
   - Are descriptions specific with named UI elements?
   - Is related content grouped under parent headings?
   - Do features have bullet-point capabilities?
   - Is the voice imperative (no "You can" / "allows you to")?
   - Are section titles descriptive and scannable?
   - Is callout language varied across links?
   - Are there obvious coverage gaps?
   - Are UI elements consistently bolded?
5. **Deliver** the rewritten article in clean markdown, and save it to `workstreams/help-center-overhaul/outputs/drafts/YYYY-MM-DD-<slug>-rewrite.md` with the original's frontmatter on top. Never edit the mirror file itself; the mirror reflects Intercom, and only `/sync-help-center` writes there.

## Output Format

Deliver the rewritten article as clean markdown:
- Use H1 for the article title
- Use H2 for major sections
- Use H3 for subsections (for example, individual widgets under a parent section)
- Use bullet lists for capabilities and actions
- Bold all UI element names
- No horizontal rules between sections
- No CMS-specific syntax (no `/callout` markers)
- Include linked article references as plain markdown links or descriptive text
- Screenshot placeholders in brackets where the original had images: `[Screenshot: <what to capture>]`

## Related Skills

- **article-draft**: for new articles from release notes, and for the Notion review handoff.
- **humanizer**: for removing AI-generated writing patterns. Run after this skill if the output feels stilted, then re-check pattern 5, since the humanizer may reintroduce "you can."

## Reference

`references/notion-ai-prompt.md` is a paste-ready version of these rules for teammates editing directly in Notion AI.
