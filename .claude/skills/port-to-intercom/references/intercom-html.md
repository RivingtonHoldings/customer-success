# Notion markdown to Intercom HTML

The mapping `/port-to-intercom` uses. Every rule here was read off the HTML Intercom actually stores on Perchwell articles, not invented, so a ported article sits in the editor looking like one a teammate typed.

## The three rules that break an article

1. **No whitespace between block tags.** Intercom converts a newline or an indent between two block elements into an empty paragraph, which renders as a blank gap. Emit the whole body as one line: `</p><h2>`, never `</p>\n<h2>`. For a deliberate blank line use a paragraph whose only content is `&nbsp;`.
2. **Alt text goes in `alt=`, never in a caption.** Notion has no alt text field, so the alt text sits in the image caption and the draft looks finished. Left alone, the published article carries a visible description under every screenshot and no alt text at all, which is what golden question 2 tests for. This conversion is the step that fixes it, and it is the step `notion-publishing.md` says always gets missed when a human does it.
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
| `![alt](url)` | `<div class="intercom-container"><img src="url" alt="alt" width="W" height="H" style="height: auto;"></div>` |
| `<video src="https://www.loom.com/share/ID"></video>` | `<div class="intercom-h2b-video"><iframe src="https://www.loom.com/embed/ID" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="autoplay; fullscreen; picture-in-picture; encrypted-media"></iframe></div>` |
| `> **Note:** text` | `<div class="intercom-interblocks-callout" style="background-color: #feedaf80; border-color: #fbc91633;"><p class="no-margin">text</p></div>` |
| `> Screenshot placeholder: …` | Omit, and report it. A placeholder means the image does not exist yet. |
| `&`, `<`, `>` in text | `&amp;`, `&lt;`, `&gt;` |

Heading levels are fixed by the house standard: H1 is the title and never appears in the body, H2 is a major section, H3 is a subsection and the `Steps:` heading. Do not emit `id` attributes; Intercom generates its own anchors.

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

Reuse the CDN URL already on the live article whenever the draft points at the same image, and **strip the `?expires=…&signature=…` query**. Those credentials expire; the bare path does not. Carry `width` and `height` over from the current body so the layout does not shift.

A draft that introduces a genuinely new image cannot be ported by this skill: the file has to be uploaded through the Intercom editor by a human first. Report it and stop rather than pushing an article with a missing picture.

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
