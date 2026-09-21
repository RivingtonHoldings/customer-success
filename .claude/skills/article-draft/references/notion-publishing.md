# Notion Publishing: Perchwell Help Center Database [Sep 2026]

The CS team created a new Notion database for the September 2026 help center project, to simplify the work and make the state of each article obvious. It is the system of record for this project.

**The rule for the rest of the project:** articles this project drafts or updates are added to the new database. The old Master Article List is read-only. Query it for history and triage, never write to it, and do not mirror a change into it.

Intercom is downstream of both: approved Notion pages are transferred to Intercom as unpublished drafts by hand, and a human publishes them there. Fin reads published articles only.

## IDs

| Thing | Value |
|---|---|
| Perchwell Help Center Database [Sep 2026] | `https://app.notion.com/p/3d18b9e0143880558dc9d9574f5abab8` |
| Data source (use for SQL and create-pages) | `collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389` |
| Data source ID (for `parent.data_source_id`) | `3d18b9e0-1438-80cc-ab0f-000bf0fc1389` |
| Template Article (the standard as a fill-in page) | `https://app.notion.com/p/3d18b9e0143880189917f12bdc34c500` |
| Notion project page (system of record for the project) | `https://app.notion.com/p/3c88b9e0143880ec8fbee25ec0b38975` |
| Article & Collection Naming Standards | `https://app.notion.com/p/3ce8b9e0143881b790c6c7c29eb11009` |
| Perchwell Product Style Guide | `https://app.notion.com/p/2a48b9e014388092a38cd7d1f4b4cb60` |
| Baldwin public help center | `https://support.perchwell.com/baldwin/en` |
| Master Article List (old, read-only) | `collection://1c78b9e0-1438-80b8-951d-000bc128f119` |

Before the first Notion write in a session, read `notion://docs/enhanced-markdown-spec` with the Notion connector's fetch tool so the body markdown is valid. Tool names are in `docs/connector-tools.md`; the server ID differs per teammate, so match on the tool name, not the full prefix.

## Schema

Nine properties an article carries, plus four production fields covered under Media fields below. `Last updated` is system-managed; do not set it.

| Property | Type | Values |
|---|---|---|
| `Article Name` | title | The article title, matching the title in the body exactly |
| `Article Status` | status | `New Article Request`, `Draft`, `Ready to Transfer`, `Live in Intercom`, `Deprecated` |
| `Intercom URL` | url | The live article's public URL, set by `/port-to-intercom` after a push. Empty until the article reaches Intercom |
| `MLS/AOR` | select | `Baldwin`, `CRLMS All`, `NYC` |
| `Collection` | select | `Getting Started Guide`, `Then vs. Now`, `Dashboard`, `Search`, `Tags`, `Client Collaboration`, `Manage People`, `Manage Listings`, `Reports`, `Analytics`, `User Settings`, `Client Experience`, `FAQs`, `Mobile`, `What's New`, `Integrations` |
| `Roles` | select | `All`, `Agent`, `Admin/Broker`, `Invited Client`, `All Except Client` |
| `Video Included` | select | `Yes`, `No`. Whether the article contains a video |
| `Visuals Included` | select | `Yes`, `No`. Whether the article contains visuals or screenshots |
| `Media Update Needed` | multi-select | `Yes`, `No`. Whether the existing visuals or video need refreshing |
| `Last updated` | last_edited_time | Read only |

`Collection` and `Roles` are single selects, so an article belongs to exactly one collection and one role group. An article that needs two collections needs splitting, or a decision from the user about which one wins.

`MLS/AOR` is a multi-select, and an article that serves two MLSs takes **one row with both values**, not two rows. Settled 2026-09-17 during the Universal Search Bar port: Intercom serves a shared article from a single record held in a collection in each help center, so there is no second article for a second row to describe. The cost is that the article's cross-links can only point into one help center; flag that at port time rather than splitting the row.

## Media fields

Two sets of fields, and confusing them is the mistake this section exists to prevent.

**The three article-level fields describe the article as it stands today:**

- `Visuals Included`: the article contains visuals or screenshots.
- `Video Included`: the article contains a video.
- `Media Update Needed`: the existing visuals or video have been identified as needing a refresh.

**The four production fields describe the work, and live in the Help Center Production Tracker:** `Visual Owner`, `Visual Status`, `Video Owner`, `Video Status`. The tracker is a view, not a second database. It sits at `https://app.notion.com/p/3dd8b9e0143881bbbaf4ea0964bd34f9` and reads the same data source, so these are columns on the same rows, surfaced through a view built for assigning and tracking production. The tracker is the source of truth for all four; do not infer any of them from the article-level fields.

**The rule:** never read `Visuals Included`, `Video Included`, or `Media Update Needed` as evidence that assigned production work is outstanding. `Media Update Needed: Yes` means someone has flagged the article's media for a refresh, and says nothing about whether that refresh has been shot, edited, or delivered. Check the Production Tracker for that.

Two consequences when reviewing or scoring:

- Do not flag an article's visuals or video as incomplete because `Media Update Needed` reads `Yes`. Judge the media that is in the article.
- Do not report a media field as an open item on a port. A port moves the article body; it does not close production work, and the flag's state is not the port's business.

Split on 2026-09-16, when the Production Tracker view was created, and the three article-level fields were renamed from `Videos`, `Visuals`, and `Needs Updated Video/Visuals`. Recorded here 2026-09-21.

One open item for the team, flagged rather than worked around:

- The `MLS/AOR` option reads `CRLMS All`. If that is meant to be CRMLS, the option needs renaming in Notion; use the string exactly as it appears until then, since a select write with an unknown option fails.

`docs/standards/fin-labeling.md` derives Fin labels from Notion fields, and derives them from `MLS/AOR` and `Collection`, never from the media fields.

## Triage queries

Query the new database first with the Notion connector's query-data-sources tool. The table name in SQL is the data source URL in double quotes.

By collection:

```sql
SELECT "Article Name", "Article Status", "MLS/AOR", "Collection", "Roles", url, "Last updated"
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "Collection" = ?
  AND "Article Status" != 'Deprecated'
ORDER BY "Last updated" DESC
```

By title keyword (run once per keyword, binding `%keyword%`):

```sql
SELECT "Article Name", "Article Status", "MLS/AOR", "Collection", url
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "Article Name" LIKE ?
ORDER BY "Last updated" DESC
```

By MLS:

```sql
SELECT "Article Name", "Article Status", "Collection", url
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "MLS/AOR" = ?
ORDER BY "Last updated" DESC
```

The new database only holds what this project has touched, so an article that exists in the live help center may have no row yet. When a keyword search comes back empty, check the mirror in `docs/help-center/`, then the old Master Article List for the article's history:

```sql
SELECT "Resource Title", "HC Status", "Update Status", "MLS", "Help Center URL (Public)", url
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Resource Title" LIKE ?
ORDER BY "Last Updated" DESC
```

That query is for reading only. When an article with an old row needs work, create a new row in the new database and carry the facts across. Leave the old row alone.

## Migrating a row from the Master Article List

`/article-rewrite` uses this section when its input is an old Notion page URL. The old row is read, never written. The new row's article-level properties come from the old row through this table; anything the table cannot resolve is a question in the confirmation summary, never a guess.

| Old property | New property | Rule |
|---|---|---|
| `Resource Title` | `Article Name` | Retitle per the naming standard when the old title is a bare noun; the user picks between the proposed task-led title and the old one, and the report records both |
| `Collection in Intercom` (multi-select) | `Collection` (single select) | Same-name matches carry across: Search, Tags, Client Collaboration, Manage People, Dashboard, Reports, Analytics, User Settings, Client Experience, Mobile, Integrations, Getting Started Guide, Then vs. Now. Listing Maintenance and Listing Management map to Manage Listings. General, FAQ Tips and What's New in Perchwell, and FAQs & What's Coming map to FAQs when the article is question-and-answer and to What's New when it is release content. Anything else, or more than one value on the old row, is a question |
| `MLS` (multi-select) | `MLS/AOR` (single select) | Baldwin to Baldwin; CRMLS to `CRLMS All`, written exactly as the option reads until it is renamed; NYC to NYC. All Regions, ICAAR, or more than one value is a question. When the same `intercom_id` is mirrored in both `docs/help-center/baldwin/` and `docs/help-center/crmls/`, the article is shared: pick the MLS the old row names and put the shared status in Open items |
| `Roles` (multi-select) | `Roles` (single select) | All to All; Agent to Agent; Admin / Broker to Admin/Broker; Invited client to Invited Client; All - but client to All Except Client. More than one value is a question |
| `Video` status, `Video Links`, a Loom or Arcade URL in the body | `Video Included` | Yes when a video URL exists or the draft carries a video placeholder; otherwise No. This records what the article contains, never whether the video is finished |
| `Screenshot` status, images in the body | `Visuals Included` | Yes when the article has images or the draft carries screenshot placeholders; otherwise No. Same rule: contents, not progress |
| any | `Media Update Needed` | Not set by a migration. It is a judgment the team makes about the live article, so leave it empty and raise it in Open items when the migrated screenshots look stale |
| `Screenshot Owner`, `Video Owner`, and the other per-asset workflow fields | `Visual Owner`, `Video Owner`, `Visual Status`, `Video Status` | Not carried by the migration. These are production fields owned by the Help Center Production Tracker; a human sets them there |
| `HC Status`, `Update Status`, `Fin AI`, `Text`, `Text Owner`, `Final Review & Upload`, `Due Date`, `Baldwin?`, `CRMLS?`, `NYC?`, `Links to another articles`, `Product Area (Internal)` | none | Not carried |
| any | `Article Status` | Always `Draft` |

Before creating the row, check that it does not already exist:

```sql
SELECT "Article Name", "Article Status", url
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "Article Name" = ? OR "Article Name" = ?
```

Bind the proposed title and the old title. A match means stop and ask; a row whose `Article Status` is `Live in Intercom` is never overwritten.

## Creating a page

Confirm once with the user before writing: a compact summary of the page and its properties, then wait for "go."

```
Creating 1 Draft in the Perchwell Help Center Database [Sep 2026]:
- Create a Market Conditions Addendum Report (1004MC)
  Article Status: Draft | MLS/AOR: Baldwin | Collection: Reports
  Roles: All Except Client | Video Included: No | Visuals Included: Yes
Go?
```

Call shape:

```json
{
  "parent": { "type": "data_source_id", "data_source_id": "3d18b9e0-1438-80cc-ab0f-000bf0fc1389" },
  "pages": [{
    "properties": {
      "Article Name": "<title>",
      "Article Status": "Draft",
      "MLS/AOR": "Baldwin",
      "Collection": "<collection>",
      "Roles": "<role>",
      "Video Included": "<Yes or No>",
      "Visuals Included": "<Yes or No>"
    },
    "content": "<Notion markdown body>"
  }]
}
```

`Video Included` and `Visuals Included` record whether the finished article will carry them, so a draft with screenshot placeholders is `Visuals Included: Yes`. Leave `Media Update Needed` empty on a new draft; it describes media that already exists. Do not pass `template_id` together with `content`; the skill writes the full body itself.

## Publishing an update change sheet

Never overwrite a page whose `Article Status` is `Live in Intercom`. The change sheet is one page for the whole release.

If the user names a target page, write the sheet there with the Notion update-page tool (`insert_content` at the end, or `replace_content` if the user says the page is empty or theirs to overwrite). Otherwise create one sibling row in the new database:

- `Article Name`: `Help center changes: <feature> (YYYY-MM-DD)`
- `Article Status`: `Draft`
- `MLS/AOR` and `Collection`: from the release note's target
- `content`: the change sheet body

Notion shape for the sheet: a one-line intro, an `##` heading per article with the Notion page mentioned via `<mention-page>`, plain bullets for edits using `->`, an `###` heading plus final-form text only for new or rewritten sections, and one `## Open items` list. No callouts or tables in the sheet.

After publishing, offer to set the affected rows' `Article Status`. Only do it when the user says yes.

## Markdown to Notion mapping

The repo file is plain markdown. Convert when building `content`:

| Repo markdown | Notion markdown |
|---|---|
| `# Title` line at the top | Omit. The title lives in `Article Name` |
| `<!-- Article Status: ... -->` metadata comment | Omit |
| `**Description:** text` | Keep as the first paragraph, `**Description:** text` |
| Opening `Use this article to ...` paragraph | Keep as an ordinary paragraph, no heading above it |
| `## Section` / `### Subsection` / `### Steps:` | Unchanged |
| `> **Note:** text` | `<callout color="gray_bg">` then a tab-indented line `**Note:** text`, then `</callout>` |
| `> **Important:** text` | `<callout color="yellow_bg">` with the same shape |
| `> **Tip:** text` | `<callout color="gray_bg">` with the same shape |
| A link to a related article | An ordinary sentence with a markdown link, or `<mention-page url="<notion url>"/>` when the target is a Notion page |
| A bare Loom or Arcade URL under the opening paragraph | `<video src="<url>"></video>` |
| `> Video placeholder: ...` / `> Screenshot placeholder: ... | Alt text: ...` | `<callout color="orange_bg">` with the placeholder text, so owners can spot it |
| Markdown image with alt text | Keep the alt text; it is required |
| Markdown table | `<table header-row="true">` with `<tr>` and `<td>` rows; cells hold plain rich text |
| Blank lines | Drop them. Notion spaces blocks itself; use `<empty-block/>` only if a visual gap is essential |
| Em dashes | Must not exist. Fix before converting |

There is no support footer and no `In this article:` heading to convert. Both were retired on September 4, 2026.

Escape `*`, `[`, `]`, `<`, `>`, `|`, `{`, `}` when they appear as literal text outside markdown syntax (for example `1004MC / Form 71 [MC]` needs `\[MC\]`).

## After publishing

Report the new page URL(s). What happens next:

1. Peer review in Notion, by a person
2. Move the row to `Ready to Transfer`
3. Run `/port-to-intercom`. It converts the body, moves each image's alt text into Intercom's `alt` attribute, shows the diff, pushes on your confirmation, writes the changelog, sets `Article Status` to `Live in Intercom` and fills `Intercom URL`, and re-syncs the mirror
4. Set the Fin labels per `docs/standards/fin-labeling.md`, by a person. `update_article` cannot write tags
5. Assign the MLS audience, by a person
6. Publish in Intercom, by a person, for a new article. A port to an already-live article keeps its published state

Step 3 used to be the step that got missed, and the part of it that got missed was the alt text: Notion has no separate alt text field, so the alt text sits in the caption and the draft looks finished. Left alone, every published article carried a visible description under each screenshot and no alt text at all, which is exactly what golden question 2 tests for. The skill now does that conversion, so the remaining manual steps are the ones the connector cannot reach.
