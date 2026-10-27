# Notion markdown to Intercom HTML

The mapping `/port-to-intercom` uses. Every rule here was read off the HTML Intercom actually stores on Perchwell articles, not invented, so a ported article sits in the editor looking like one a teammate typed.

## The three rules that break an article

1. **No stray whitespace between block tags, and a blank line where Tara wants one.** Intercom converts a newline or an indent between two block elements into an empty paragraph, which renders as a blank gap. Emit the body as one line, `</p><h2>`, except for the house spacing: after a paragraph or an image, when the next block is a paragraph, an image, a heading, or a video, insert `<p class="no-margin"></p>` followed by a newline. Put nothing before a list or a callout, nothing after a list, heading, callout, or video, and nothing at the end. The rule was read off Tara's own edit of Create a Search with Filters (13903380) on 2026-10-23. An empty paragraph sent without the newline is stripped on save; with the newline it is stored and renders as one 24px line, which is the form the Intercom editor saves.
2. **No caption and no alt text.** Notion keeps the alt text in the image caption. Drop the whole caption, and do not write an `alt` attribute: Intercom does not support alt text (Tara, October 23, 2026). Read the caption only for its `Baldwin |` or `CRMLS |` label, which decides whether the image goes to this help center.
3. **Nothing in the body is bold** except a callout label. The Notion draft has already had bold removed by the standard; do not add it back while converting. If the source has stray `**` on a UI element, stop and say so rather than carrying it through.

## Mapping

| Notion markdown | Intercom HTML |
|---|---|
| `# Title` | Omit. It becomes the `title` field. |
| `**Description:** text` | Omit. `text` becomes the `description` field. |
| Opening `Use this article to…` paragraph | Stays, as the first body paragraph |
| `## Heading` | `<h2>Heading</h2>` |
| `### Heading` | `<h3>Heading</h3>` |
| Paragraph | `<p class="no-margin">text</p>` |
| `1.` numbered list | `<ol><li><p class="no-margin">item</p></li></ol>` |
| `-` bulleted list | `<ul><li><p class="no-margin">item</p></li></ul>` |
| Nested bullet | A second `<ul>` inside the parent `<li>`, after its `<p>` |
| `[text](url)` | `<a href="url">text</a>` |
| `<mention-page url="notion url"/>`, or `[text](notion url)` | `<a href="intercom url">Article Name</a>`, with the Intercom URL resolved from the linked Notion row. Never emit a Notion URL. See step 5 of `SKILL.md`. |
| `![alt](url)` or `<image>` with a caption | `<div class="intercom-container"><img src="url"></div>`, with the caption and alt text dropped |
| `<video src="https://www.loom.com/share/ID"></video>` | `<div class="intercom-h2b-video"><iframe src="https://www.loom.com/embed/ID" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="autoplay; fullscreen; picture-in-picture; encrypted-media"></iframe></div>` |
| `> **Note:** text`, `> **Important:** text`, `> **Tip:** text` | A callout. See Callouts below; the color depends on the label. |
| `![Baldwin \| Alt text: alt](url)` or `![CRMLS \| Alt text: alt](url)` | The same `<img>` with no caption or alt text, when the label matches the target help center. Omit it when the label names the other MLS. See step 5 of `SKILL.md`. |
| `> Screenshot placeholder: …` | Omit, and report it. A placeholder means the image does not exist yet. A placeholder labeled `(Baldwin)` or `(CRMLS)` is reported only when the label matches the target help center. |
| `&`, `<`, `>` in text | `&amp;`, `&lt;`, `&gt;` |

Heading levels are fixed by the house standard: H1 is the title and never appears in the body, H2 is a major section, H3 is a subsection and the `Steps:` heading. Do not emit `id` attributes; Intercom generates its own anchors.

## Callouts

One wrapper serves all three labels. Only the two colors change, and the label keeps its `<b>`:

```html
<div class="intercom-interblocks-callout" style="background-color: BG; border-color: BORDER;"><p class="no-margin"><b>Note:</b> text</p></div>
```

| Label | Notion color | BG | BORDER |
|---|---|---|---|
| `**Note:**` | `gray_bg` | `#f4f5f7` | `#dfe2e6` |
| `**Tip:**` | `gray_bg` | `#f4f5f7` | `#dfe2e6` |
| `**Important:**` | `yellow_bg` | `#feedaf80` | `#fbc91633` |

Take the color from the label, not from the Notion block's own color. They agree when the draft is right, and a callout sitting in the wrong Notion color is a draft defect to report rather than a color to carry through.

The `<b>` on the label is deliberate and is the one exception to rule 3 above. Intercom names the bold label as what marks a passage for Fin to carry into an answer, so a callout converted without it loses the thing the callout was for.

The gray pair was read off Dashboard Overview (13903062) on 2026-09-18, where both callouts are Notes. The yellow pair was confirmed on Actions Menu Options on the Search Page (13623271) on 2026-10-23: Intercom stored it as sent, and it renders light yellow on the public page.

A `> Screenshot placeholder:` line is not a callout here. Notion holds it in an orange callout so owners can spot it, and the conversion omits it and reports it.

## What Intercom changes on save

Observed on the Universal Search Bar port, 2026-09-17. None of these is an error to fix; they are the editor normalizing, and knowing them saves a panic on the verify step.

- **Heading levels shift up one.** Send `<h2>` and it is stored as `<h1>`; send `<h3>` and it is stored as `<h2>`. Intercom maps the shallowest heading in the body to its own Heading 1. Keep sending H2 and H3, which is what the house standard and the templates specify, and expect the stored HTML to read H1 and H2. The rendered hierarchy is still correct and still matches every other Perchwell article. This contradicts the note in `article-template.md` that Intercom "expects H2 and H3 inside the body"; what it expects is a consistent hierarchy, which it then renumbers.
- **`author_id` is reassigned to the acting admin.** Omitting `author_id` on an update does *not* preserve the original author, the way omitting `state` preserves the publish state. Intercom stamps whoever owns the connector. There is no way to avoid this through the API, so say it in the report and put it in the changelog line rather than letting a teammate discover the byline changed.
- **Image URLs are re-signed.** Send the bare CDN path with no `?expires=&signature=` and Intercom attaches fresh credentials of its own. This is why stripping the expiring query is safe.
- **Links gain `target="_blank"` and `class="intercom-content-link"`.** Emit a plain `<a href>` and let Intercom decorate it.
- **Anchor `id`s are generated.** `<h2>Steps:</h2>` comes back as `<h2 id="h_3d75a56c5c">`, and the on-page table of contents is built from them.

## Loom links

A Loom share URL and a Loom embed URL are different paths on the same ID. `loom.com/share/ID` must become `loom.com/embed/ID` or the iframe renders a share page instead of a player.

## Images

**The Articles API re-hosts images.** Give it an `<img src>` pointing anywhere publicly reachable and Intercom downloads the file, stores it on its own CDN, and rewrites the `src`. Intercom's own documentation: "The image will be uploaded to Intercom from the source you specify, and an Intercom link will be used to display it in your article." PNG, JPEG, SVG and GIF; the URL must be absolute, not relative.

That is why a Notion draft's screenshots need no download, no Chrome, and no manual upload. It also explains why every image in the live help centers sits on an Intercom host: not because someone uploaded each one by hand, but because Intercom re-hosts everything it is given.

**Use a scratch draft as the shelf.** A Notion image URL is signed and dies five minutes after the page is read, so do not spend that window on a live article:

1. Fetch the Notion page for fresh signatures.
2. `create_article` with `state: "draft"`, no `parent_id`, and a throwaway body holding every image at its Notion URL.
3. `get_article` on that draft. The `src` values now point at `perchwell.intercom-attachments-1.com`. Strip the `?expires=…&signature=…` query; the bare path is stable and Intercom re-signs it on read.
4. Build the real body from those URLs, so the live article never contains a URL that can expire.

Reuse the CDN URL already on the live article whenever the draft points at the same image. Carry `width` and `height` over from the current body when you have them, so the layout does not shift; on a freshly re-hosted image, omit them and let Intercom size it.

The connector has no delete tool, so say in the report that the scratch draft needs deleting by hand in Intercom.

## Worked example

Notion:

```
**Description:** Find a listing, agent, or contact from any page in Perchwell.
Use this article to open the Universal Search Bar from any page.
## When to use the Universal Search Bar
Open it when you already know which listing you want.
### Steps:
1. Click the Search field
2. Type an address
```

Intercom (`description` field carries the first line; body is one unbroken line):

```html
<p class="no-margin">Use this article to open the Universal Search Bar from any page.</p><h2>When to use the Universal Search Bar</h2><p class="no-margin">Open it when you already know which listing you want.</p><h3>Steps:</h3><ol><li><p class="no-margin">Click the Search field</p></li><li><p class="no-margin">Type an address</p></li></ol>
```
